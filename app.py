import streamlit as st
import json

st.set_page_config(page_title="Ứng dụng Đặt Cơm", layout="wide")

# Tiêu đề
st.title("🍱 Ứng dụng Đặt Cơm Online")
st.markdown("Chọn món ăn bạn muốn đặt bên dưới:")

# Tải dữ liệu từ menu.json
with open("menu.json", "r", encoding="utf-8") as f:
    menu = json.load(f)

# Khởi tạo danh sách đơn hàng
if "orders" not in st.session_state:
    st.session_state.orders = []

# Hiển thị danh sách món ăn
cols = st.columns(3)
for index, item in enumerate(menu):
    with cols[index % 3]:
        st.image(item["image"], width=250)
        st.markdown(f"### {item['name']}")
        st.markdown(f"**Giá:** {item['price']:,}đ")
        if st.button(f"🛒 Đặt món", key=f"order_{index}"):
            st.session_state.orders.append(item)
            st.success(f"Đã đặt: {item['name']}")

# Hiển thị giỏ hàng
st.markdown("---")
st.header("🧾 Món bạn đã đặt")

if st.session_state.orders:
    total = 0
    for i, order in enumerate(st.session_state.orders):
        st.write(f"- {order['name']} ({order['price']:,}đ)")
        total += order["price"]
    st.markdown(f"### 💰 **Tổng cộng: {total:,}đ**")
    if st.button("🗑️ Xoá tất cả món đã đặt"):
        st.session_state.orders = []
        st.experimental_rerun()
else:
    st.info("Bạn chưa đặt món nào.")
