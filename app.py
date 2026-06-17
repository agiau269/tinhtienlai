import streamlit as st
st.image("logo.jpg")
# Tiêu đề app
st.title("APP TÍNH TIỀN GỬI TIẾT KIỆM_ĐỀ TÀI 2_TS. VŨ ĐỨC BÌNH")

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền gửi (triệu đồng)",
    min_value=0.0,
    value=100.0
)

i = st.number_input(
    "Nhập lãi suất tiết kiệm theo năm (%)",
    min_value=0.0,
    value=6.0
)

n = st.number_input(
    "Nhập số tháng gửi",
    min_value=1,
    value=12
)

# Đổi % sang số thập phân
i = i / 100

# Nút tính toán
if st.button("Tính toán"):
    
    # Lãi đơn
    A = C * (1 + i * n / 12)

    # Lãi kép
    B = C * (1 + i / 12) ** n

    st.subheader("Kết quả")

    st.success(
        f"Tổng tiền nhận được theo lãi đơn: {A:,.4f} triệu đồng"
    )

    st.success(
        f"Tổng tiền nhận được theo lãi kép: {B:,.4f} triệu đồng"
    )
