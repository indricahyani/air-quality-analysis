import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Memuat dataset
air_df = pd.read_csv("dashboard/main_data.csv")

# Mengubah kolom datetime menjadi tipe datetime
air_df["datetime"] = pd.to_datetime(air_df["datetime"])

# Mengurutkan data berdasarkan waktu
air_df.sort_values(by="datetime", inplace=True)

# Judul dashboard
st.title("Air Quality Dashboard")
st.caption("Analisis kualitas udara di Beijing berdasarkan data dari 12 stasiun pemantauan.")

# Sidebar
st.sidebar.header("Filter Data")

# Filter stasiun
station_list = ["Semua Stasiun"] + sorted(air_df["station"].unique().tolist())

selected_station = st.sidebar.selectbox(
    "Pilih Stasiun:",
    station_list
)

# Memfilter data berdasarkan stasiun
if selected_station == "Semua Stasiun":
    filtered_df = air_df.copy()
else:
    filtered_df = air_df[air_df["station"] == selected_station]

# Filter rentang tanggal
start_date = st.sidebar.date_input(
    "Tanggal Awal:",
    air_df["datetime"].min().date()
)

end_date = st.sidebar.date_input(
    "Tanggal Akhir:",
    air_df["datetime"].max().date()
)

# Menerapkan filter tanggal
filtered_df = filtered_df[
    (filtered_df["datetime"].dt.date >= start_date) &
    (filtered_df["datetime"].dt.date <= end_date)
]

# Ringkasan statistik
st.subheader("Ringkasan Kualitas Udara")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Data", f"{len(filtered_df):,}")

with col2:
    st.metric("Rata-rata PM2.5", f"{filtered_df['PM2.5'].mean():.2f}")

with col3:
    st.metric("Rata-rata PM10", f"{filtered_df['PM10'].mean():.2f}")


# Data Preview
with st.expander("Lihat Dataset"):
    st.subheader("Dataset Air Quality")

    display_df = filtered_df.reset_index(drop=True)
    display_df.index = display_df.index + 1
    display_df.index.name = "No"

    st.dataframe(display_df, use_container_width=True)

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Data",
        data=csv,
        file_name="air_quality_data.csv",
        mime="text/csv"
    )

# Pertanyaan Bisnis 1
st.header("1. Perbandingan Kualitas Udara Antarstasiun")
st.write(
    "Bagaimana perbandingan rata-rata konsentrasi PM2.5 dan PM10 "
    "pada 12 stasiun pemantauan?"
)

station_pollution = filtered_df.groupby(
    "station"
)[["PM2.5", "PM10"]].mean()

station_pollution = station_pollution.sort_values(
    by="PM2.5", ascending=False
)

fig, ax = plt.subplots(figsize=(12, 6))

station_pollution.plot(kind="bar", ax=ax)

ax.set_xlabel("Stasiun")
ax.set_ylabel("Rata-rata Konsentrasi")
ax.set_title("Rata-rata PM2.5 dan PM10 Berdasarkan Stasiun")
ax.legend(title="Polutan")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

highest_station = station_pollution["PM2.5"].idxmax()
highest_pm25 = station_pollution["PM2.5"].max()

highest_pm10_station = station_pollution["PM10"].idxmax()
highest_pm10 = station_pollution["PM10"].max()

st.info(
    f"Insight: Stasiun {highest_station} memiliki rata-rata PM2.5 "
    f"tertinggi sebesar {highest_pm25:.2f}. "
    f"Sementara itu, rata-rata PM10 tertinggi ditemukan di "
    f"stasiun {highest_pm10_station} sebesar {highest_pm10:.2f}."
)


# Pertanyaan Bisnis 2
st.header("2. Pola Kualitas Udara Berdasarkan Waktu")
st.write(
    "Bagaimana pola rata-rata konsentrasi PM2.5 "
    "berdasarkan jam dan bulan?"
)

col1, col2 = st.columns(2)

# Grafik PM2.5 berdasarkan jam
with col1:
    st.subheader("Berdasarkan Jam")

    hourly_pm25 = filtered_df.groupby(
        filtered_df["datetime"].dt.hour
    )["PM2.5"].mean()

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.lineplot(
        x=hourly_pm25.index,
        y=hourly_pm25.values,
        marker="o",
        ax=ax
    )

    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata PM2.5")
    ax.set_xticks(range(24))
    ax.grid(True)
    plt.tight_layout()

    st.pyplot(fig)

# Grafik PM2.5 berdasarkan bulan
with col2:
    st.subheader("Berdasarkan Bulan")

    monthly_pm25 = filtered_df.groupby(
        filtered_df["datetime"].dt.month
    )["PM2.5"].mean()

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.lineplot(
        x=monthly_pm25.index,
        y=monthly_pm25.values,
        marker="o",
        ax=ax
    )

    ax.set_xlabel("Bulan")
    ax.set_ylabel("Rata-rata PM2.5")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels([
        "Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
        "Jul", "Agu", "Sep", "Okt", "Nov", "Des"
    ])
    ax.grid(True)
    plt.tight_layout()

    st.pyplot(fig)

# Grafik PM2.5 berdasarkan jam dan stasiun
st.subheader("Berdasarkan Jam pada Setiap Stasiun")

hourly_station_pm25 = filtered_df.groupby(
    [filtered_df["datetime"].dt.hour, "station"]
)["PM2.5"].mean().reset_index()

hourly_station_pm25.rename(
    columns={"datetime": "hour"},
    inplace=True
)

# Pastikan kolom jam memiliki nama hour
hourly_station_pm25.columns = ["hour", "station", "PM2.5"]

fig, ax = plt.subplots(figsize=(14, 7))

sns.lineplot(
    data=hourly_station_pm25,
    x="hour",
    y="PM2.5",
    hue="station",
    ax=ax
)

ax.set_title("Pola Rata-rata PM2.5 Berdasarkan Jam pada Setiap Stasiun")
ax.set_xlabel("Jam Pengamatan")
ax.set_ylabel("Konsentrasi Rata-rata PM2.5")
ax.set_xticks(range(24))
ax.legend(
    title="Stasiun",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)
ax.grid(True)
plt.tight_layout()

st.pyplot(fig)

# Menghitung insight
highest_hour = hourly_pm25.idxmax()
highest_hour_pm25 = hourly_pm25.max()

lowest_hour = hourly_pm25.idxmin()
lowest_hour_pm25 = hourly_pm25.min()

highest_month = monthly_pm25.idxmax()
highest_month_pm25 = monthly_pm25.max()

lowest_month = monthly_pm25.idxmin()
lowest_month_pm25 = monthly_pm25.min()


st.info(
    f"Insight: Rata-rata PM2.5 tertinggi terjadi pukul "
    f"{highest_hour:02d}.00 ({highest_hour_pm25:.2f}), "
    f"sedangkan terendah pukul {lowest_hour:02d}.00 "
    f"({lowest_hour_pm25:.2f}). Berdasarkan bulan, nilai "
    f"tertinggi tercatat pada bulan {highest_month} "
    f"({highest_month_pm25:.2f}) dan terendah pada "
    f"bulan {lowest_month} ({lowest_month_pm25:.2f}). "
    "Pola konsentrasi berdasarkan jam juga menunjukkan "
    "perbedaan antarstasiun, dengan sebagian besar stasiun "
    "mencapai konsentrasi tertinggi pada malam hari."
)

st.caption(
    "Catatan: Nilai rata-rata bulanan dihitung dari gabungan "
    "pengamatan pada bulan yang sama selama periode "
    "Maret 2013 hingga Februari 2017."
)



# Pertanyaan Bisnis 3
st.header("3. Kualitas Udara Berdasarkan Kondisi Cuaca")
st.write(
    "Bagaimana perbedaan rata-rata konsentrasi PM2.5 "
    "berdasarkan kategori kecepatan angin dan curah hujan?"
)

col1, col2 = st.columns(2)

# Grafik PM2.5 berdasarkan kecepatan angin
with col1:
    st.subheader("Kecepatan Angin")

    wind_pm25 = filtered_df.groupby(
        "wind_category"
    )["PM2.5"].mean()

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(
        x=wind_pm25.index,
        y=wind_pm25.values,
        ax=ax
    )

    ax.set_xlabel("Kategori Kecepatan Angin")
    ax.set_ylabel("Rata-rata PM2.5")
    plt.tight_layout()

    st.pyplot(fig)

# Grafik PM2.5 berdasarkan curah hujan
with col2:
    st.subheader("Curah Hujan")

    rain_pm25 = filtered_df.groupby(
        "rain_category"
    )["PM2.5"].mean()

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(
        x=rain_pm25.index,
        y=rain_pm25.values,
        ax=ax
    )

    ax.set_xlabel("Kategori Curah Hujan")
    ax.set_ylabel("Rata-rata PM2.5")
    plt.tight_layout()

    st.pyplot(fig)

highest_wind = wind_pm25.idxmax()
highest_wind_value = wind_pm25.max()

highest_rain = rain_pm25.idxmax()
highest_rain_value = rain_pm25.max()

st.info(
    f"Insight: Kategori kecepatan angin {highest_wind} "
    f"memiliki rata-rata PM2.5 tertinggi sebesar "
    f"{highest_wind_value:.2f}. Pada kategori curah hujan, "
    f"nilai tertinggi ditemukan pada kategori {highest_rain} "
    f"sebesar {highest_rain_value:.2f}."
)

# Analisis Lanjutan
st.header("4. Analisis Korelasi Antarvariabel")
st.write(
    "Bagaimana hubungan antara konsentrasi PM2.5, PM10, "
    "kecepatan angin, dan curah hujan?"
)

correlation = filtered_df[
    ["PM2.5", "PM10", "WSPM", "RAIN"]
].corr(method="pearson")

fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1,
    ax=ax
)

ax.set_title("Matriks Korelasi Antarvariabel")
plt.tight_layout()

st.pyplot(fig)

st.info(
    f"Insight: PM2.5 memiliki korelasi positif kuat dengan PM10 "
    f"({correlation.loc['PM2.5', 'PM10']:.2f}) dan korelasi negatif "
    f"dengan WSPM ({correlation.loc['PM2.5', 'WSPM']:.2f}). "
    f"Sementara itu, hubungan PM2.5 dengan curah hujan tergolong "
    f"sangat lemah ({correlation.loc['PM2.5', 'RAIN']:.2f})."
)

# Analisis Lanjutan 2
st.header("5. Pengelompokan Stasiun Berdasarkan Konsentrasi PM2.5")
st.write(
    "Bagaimana pengelompokan 12 stasiun pemantauan "
    "berdasarkan rata-rata konsentrasi PM2.5?"
)

station_pm25 = filtered_df.groupby(
    "station"
)["PM2.5"].mean().reset_index()

if len(station_pm25) >= 3 and station_pm25["PM2.5"].nunique() >= 3:
    q1 = station_pm25["PM2.5"].quantile(1/3)
    q2 = station_pm25["PM2.5"].quantile(2/3)

    station_pm25["Kategori"] = pd.cut(
        station_pm25["PM2.5"],
        bins=[-float("inf"), q1, q2, float("inf")],
        labels=["Rendah", "Sedang", "Tinggi"],
        duplicates="drop"
    )
else:
    station_pm25["Kategori"] = "Tidak dapat dikelompokkan"

fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(
    data=station_pm25,
    x="station",
    y="PM2.5",
    hue="Kategori",
    dodge=False,
    palette={
        "Rendah": "#3498DB",
        "Sedang": "#F39C12",
        "Tinggi": "#2E8B57",
        "Tidak dapat dikelompokkan": "gray"
    },
    ax=ax
)

ax.set_xlabel("Stasiun")
ax.set_ylabel("Rata-rata PM2.5")
ax.set_title("Pengelompokan Stasiun Berdasarkan PM2.5")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

category_counts = station_pm25["Kategori"].value_counts()

highest_station = station_pm25.loc[
    station_pm25["PM2.5"].idxmax()
]

st.info(
    f"Insight: Sebanyak {category_counts.get('Rendah', 0)} stasiun "
    f"termasuk kategori rendah, {category_counts.get('Sedang', 0)} "
    f"stasiun kategori sedang, dan {category_counts.get('Tinggi', 0)} "
    f"stasiun kategori tinggi. Stasiun {highest_station['station']} "
    f"memiliki rata-rata PM2.5 tertinggi sebesar "
    f"{highest_station['PM2.5']:.2f}."
)

# Footer
st.divider()
st.caption("Air Quality Dashboard | Created by Ni Made Indri Cahyani")
