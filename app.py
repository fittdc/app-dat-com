import streamlit as st
import json
from datetime import datetime

def load_menu():
    with open("menu.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_order(order):
    try:
        with open("orders.json","r",encoding="utf-8") as f:
            orders = json.load(f)
    except:
        orders = []
    orders.append(order)
    with open("orders.json","w",encoding="utf-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

st.set_page_config(page_title="App Đặt Cơm", layout="wide")
st.title("🍱 Ứng dụng Đặt Cơm")

menu = load_menu()
selected = []
cols = st.columns(3)

for i, item in enumerate(menu):
    with cols[i % 3]:
        st.image(item["image"], width=200)
        st.markdown(f"### {item['name']}")
        st.markdown(f"💰 {item['price']:,} VND")
        qty = st.number_input(f"Số lượng - {item['name']}", 0, 20, 0, key=i)
        if qty > 0:
            selected.append({"name": item["name"], "price": item["price"], "quantity": qty})

st.markdown("---")
st.header("📝 Thông tin đặt hàng")

with st.form("order_form"):
    name = st.text_input("Tên người đặt")
    phone = st.text_input("Số điện thoại")
    note = st.text_area("Ghi chú (nếu cần)")
    submit = st.form_submit_button("📤 Gửi đơn hàng")

    if submit:
        if not name or not phone:
            st.warning("Vui lòng nhập tên và số điện thoại.")
        elif not selected:
            st.warning("Bạn chưa chọn món.")
        else:
            order = {
                "name": name,
                "phone": phone,
                "note": note,
                "items": selected,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            save_order(order)
            st.success("✅ Đơn hàng đã được gửi thành công!")
            st.balloons()
