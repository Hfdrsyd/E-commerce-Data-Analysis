import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

df_orders = pd.read_csv('./dashboard/orders.csv')
df_order_product = pd.read_csv('./dashboard/order_product.csv')
df_order_review_order_item = pd.read_csv('./dashboard/order_review_order_item.csv')
rfm_df = pd.read_csv("./dashboard/rfm_df.csv")

st.markdown('### Hasil Analisis Data E-commerce-public-dataset')
df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3"]
df_orders['month'] = df_orders['order_purchase_timestamp'].dt.strftime('%B')

st.write(df_orders.head())

st.markdown("## Permintaan penjualan paling banyak tiap bulan")
monthly_counts = df_orders['month'].value_counts()
st.write(monthly_counts)
plt.bar(monthly_counts.index, monthly_counts.values, color=colors_)
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pembelian')
plt.title('Grafik Jumlah Pembelian per Bulan')
plt.xticks(rotation=45)
st.pyplot(plt)

st.write("Permintaan paling banyak terjadi pada bulan Agustus dengan 10843 permintaan pembelian, diikuti Mei dengan 10573 permintaan pembelian, dan Juli dengan 10318 permintaan pembelian.")
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
st.markdown("## Kategori yang paling laris dan paling tidak laris?")
category_counts = df_order_product['product_category_name_english'].value_counts()

kecil_to_besar = category_counts.sort_values(ascending=True)[:10]
besar_to_kecil = category_counts.sort_values(ascending=False)[:10]
st.markdown("### 10 Kategori dengan Pembelian Tertinggi")
st.write(besar_to_kecil)
plt.figure(figsize=(10, 6))
plt.barh(besar_to_kecil.index, besar_to_kecil.values, color=colors_)
plt.xlabel('Jumlah Pembelian')
plt.ylabel('Kategori')
plt.title('10 Kategori dengan Pembelian Terbanyak')
plt.gca().invert_yaxis() 
st.pyplot(plt)

st.markdown("### 10 Kategori dengan Pembelian Terendah")
st.write(kecil_to_besar)

plt.figure(figsize=(10, 6))
plt.barh(kecil_to_besar.index, kecil_to_besar.values, color=colors_)
plt.xlabel('Jumlah Pembelian')
plt.ylabel('Kategori')
plt.title("10 Kategori dengan Pembelian Terendah")
plt.gca().invert_yaxis() 
st.pyplot(plt)

st.markdown("## Review skor terburuk")
average_review_score = df_order_review_order_item.groupby('product_id')['review_score'].mean()
average_review_score_sorted = average_review_score.sort_values(ascending=True)[:5]
st.write(average_review_score_sorted)
st.markdown("### Produk dengan Review Score Paling Buruk")
st.write("Terdapat banyak produk dengan rata-rata review paling buruk berupa satu(1) point, dan produk tidak memiliki nama sehingga berikut merupakan sebagian product id dengan review paling buruk:")
st.write("- 7f7a6b07907da42addc3ec06b4a62cfb    1.0 ")
st.write("- a8e59319e3c44b5af3a5412d713af5bb    1.0 ")
st.write("- b33fb5f691f9219b5d60d856191aea6a4    1.0 ")


st.markdown("## RFM ANALYSIS")
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
# Plot for Recency
plt.figure(figsize=(10, 6))
top_5_recency = rfm_df.sort_values(by="recency", ascending=True).head(5)
sns.barplot(x="recency", y="customer_id", data=top_5_recency, palette=colors_, hue="customer_id")
plt.title("Top 5 Customers by Recency (days)")
plt.xlabel("Recency (days)")
plt.ylabel("Customer ID")
st.write("Top 5 Customers by Recency:")
st.write(pd.concat([top_5_recency['customer_id'], top_5_recency['recency']], axis=1))
st.pyplot(plt)

# Plot for Frequency
plt.figure(figsize=(10, 6))
top_5_frequency = rfm_df.sort_values(by="frequency", ascending=False).head(5)
sns.barplot(x="frequency", y="customer_id", data=top_5_frequency, palette=colors_, hue="customer_id")
plt.title("Top 5 Customers by Frequency")
plt.xlabel("Frequency")
plt.ylabel("Customer ID")
st.write("\nTop 5 Customers by Frequency:")
st.write(pd.concat([top_5_frequency['customer_id'], top_5_frequency['frequency']], axis=1))
st.pyplot(plt)

# Plot for Monetary
plt.figure(figsize=(10, 6))
top_5_monetary = rfm_df.sort_values(by="monetary", ascending=False).head(5)
sns.barplot(x="monetary", y="customer_id", data=top_5_monetary, palette=colors_, hue="customer_id")
plt.title("Top 5 Customers by Monetary")
plt.xlabel("Monetary")
plt.ylabel("Customer ID")
st.write("\nTop 5 Customers by Monetary:")
st.write(pd.concat([top_5_monetary['customer_id'], top_5_monetary['monetary']], axis=1))
st.pyplot(plt)
