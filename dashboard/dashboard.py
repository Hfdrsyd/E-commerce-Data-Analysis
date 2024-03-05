import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df_orders = pd.read_csv('./dashboard/orders.csv')
df_order_product = pd.read_csv('./dashboard/order_product.csv')
df_order_review_order_item = pd.read_csv('./dashboard/order_review_order_item.csv')
st.title('Hasil Analisis Data E-commerce-public-dataset')
df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])

df_orders['month'] = df_orders['order_purchase_timestamp'].dt.strftime('%B')

st.write(df_orders.head())

st.markdown("## Permintaan penjualan paling banyak")
st.write("Grafik Jumlah Pembelian per Bulan")
monthly_counts = df_orders['month'].value_counts()
plt.bar(monthly_counts.index, monthly_counts.values)
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pembelian')
plt.xticks(rotation=45)
st.pyplot(plt)
st.write("Permintaan paling banyak terjadi pada bulan Agustus dengan 11115 permintaan pembelian, diikuti Mei dengan 9670 permintaan pembelian, dan Juli dengan 8641 permintaan pembelian.")
st.markdown("## kategori yang paling laris dan paling tidak laris?")
category_counts = df_order_product['product_category_name_english'].value_counts()

kecil_to_besar = category_counts.sort_values(ascending=True)[:10]
besar_to_kecil = category_counts.sort_values(ascending=False)[:10]
st.write(besar_to_kecil)
plt.figure(figsize=(10, 6))
plt.barh(besar_to_kecil.index, besar_to_kecil.values)
plt.xlabel('Jumlah Pembelian')
plt.ylabel('Kategori')
plt.title('10 Kategori dengan Pembelian Terbanyak')
plt.gca().invert_yaxis() 
st.pyplot(plt)

st.write("10 Kategori dengan Pembelian Terendah")
st.write(kecil_to_besar)

plt.figure(figsize=(10, 6))
plt.barh(kecil_to_besar.index, kecil_to_besar.values)
plt.xlabel('Jumlah Pembelian')
plt.ylabel('Kategori')
plt.title('10 Kategori dengan Pembelian Terendah')
plt.gca().invert_yaxis() 
st.pyplot(plt)
st.title("Kategori Paling Laris dan Paling Tidak Laris")
st.write("5 kategori yang paling laris:")
st.write("- bed_bath_table")
st.write("- health_beauty")
st.write("- sports_leisure")
st.write("- furniture_decor")
st.write("- computers_accessories")

st.write("5 kategori yang paling tidak laris:")
st.write("- security_and_services")
st.write("- fashion_childrens_clothes")
st.write("- cds_dvds_musicals")
st.write("- la_cuisine")
st.write("- arts_and_craftmanship")
st.markdown("## Review skor terburuk")
average_review_score = df_order_review_order_item.groupby('product_id')['review_score'].mean()
average_review_score_sorted = average_review_score.sort_values(ascending=True)[:5]
st.write(average_review_score_sorted)
st.title("Produk dengan Review Score Paling Buruk")
st.write("Terdapat banyak produk dengan rata-rata review paling buruk berupa satu(1) point, dan produk tidak memiliki nama sehingga berikut merupakan sebagian product id dengan review paling buruk:")
st.write("- 7f7a6b07907da42addc3ec06b4a62cfb    1.0 ")
st.write("- a8e59319e3c44b5af3a5412d713af5bb    1.0 ")
st.write("- b33fb5f691f9219b5d60d856191aea6a4    1.0 ")
