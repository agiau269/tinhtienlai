import streamlit as st
st.set_page_config(page_title="Tính Thuế TNCN", page_icon="💰")
# Logo
st.image("logo.jpg", width=200)
# Tiêu đề
st.title("💰 APP TÍNH THUẾ THU NHẬP CÁ NHÂN 2026")
st.subheader("ĐOÀN ANH GIÀU")
# Nhập dữ liệu
salary = st.number_input(
    "Nhập thu nhập tháng (VNĐ)",
    min_value=0,
    value=30000000,
    step=1000000
)
dependents = st.number_input(
    "Nhập số người phụ thuộc",
    min_value=0,
    value=0
)
# Luật mới
PERSONAL_DEDUCTION = 15_500_000
DEPENDENT_DEDUCTION = 6_200_000
# Hàm tính thuế
def calculate_tax(income):
    brackets = [
        (10_000_000, 0.05),
        (30_000_000, 0.10),
        (60_000_000, 0.20),
        (100_000_000, 0.30),
        (float("inf"), 0.35)
    ]
    tax = 0
    previous = 0
    for limit, rate in brackets:
        if income > limit:
            tax += (limit - previous) * rate
            previous = limit
        else:
            tax += (income - previous) * rate
            break
    return max(tax, 0)
# Nút tính
if st.button("Tính thuế"):
    insurance = salary * 0.105
    taxable_income = (
        salary
        - insurance
        - PERSONAL_DEDUCTION
        - dependents * DEPENDENT_DEDUCTION
    )
    taxable_income = max(0, taxable_income)
    tax = calculate_tax(taxable_income)
    net_income = salary - insurance - tax
    annual_tax = tax * 12
    st.subheader("📊 Kết quả")
    st.success(
        f"Thu nhập tính thuế: {taxable_income:,.0f} VNĐ"
    )
    st.success(
        f"Thuế TNCN phải nộp: {tax:,.0f} VNĐ/tháng"
    )
    st.success(
        f"Thu nhập thực nhận: {net_income:,.0f} VNĐ/tháng"
    )
    st.success(
        f"Thuế dự kiến cả năm: {annual_tax:,.0f} VNĐ"
    )
    # Tax Health Score
    score = 100
    ratio = tax / salary if salary > 0 else 0
    if ratio > 0.20:
        score -= 40
    elif ratio > 0.15:
        score -= 30
    elif ratio > 0.10:
        score -= 20
    elif ratio > 0.05:
        score -= 10
    score += min(dependents * 5, 20)
    score = min(score, 100)
    st.subheader("🏆 Tax Health Score")
    st.progress(score / 100)
    st.info(
        f"Điểm sức khỏe thuế của bạn: {score}/100"
    )
    # AI Advisor
    st.subheader("🤖 AI Tax Advisor")
    if score >= 80:
        st.success(
            "Tình hình thuế của bạn khá tối ưu."
        )
    elif score >= 60:
        st.warning(
            "Bạn đang ở mức thuế trung bình."
        )
    else:
        st.error(
            "Gánh nặng thuế tương đối cao."
        )
