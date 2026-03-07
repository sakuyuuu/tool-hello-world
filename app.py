import streamlit as st
st.set_page_config(page_title="失業保険 計算ツール【2026年最新】", page_icon="💰")

st.markdown('<meta name="google-site-verification" content="lPwzXiM6si21AlWWtB_s3rN1kl7NIgDVJXDgkOAbxA0" />', unsafe_allow_html=True)

st.title("💰 失業保険 給付額 計算ツール")
st.caption("2026年最新版｜3項目を入力するだけで給付額を即診断")
st.divider()
age = st.selectbox("① あなたの年齢", ["30歳未満", "30〜44歳", "45〜59歳", "60〜64歳"])
reason = st.radio("② 退職理由", ["自己都合", "会社都合・解雇"])
months = st.number_input("③ 直近6ヶ月の月給（額面・万円）", min_value=10, max_value=100, value=30, step=1)
if st.button("💡 給付額を計算する"):
    daily_wage = months * 10000 / 30
    if daily_wage <= 5110:
        rate = 0.80
    elif daily_wage <= 12580:
        rate = 0.60
    else:
        rate = 0.50
    daily_benefit = daily_wage * rate
    # 給付日数
    if reason == "自己都合":
        days = 90
    else:
        if age == "30歳未満":
            days = 90
        elif age == "30〜44歳":
            days = 120
        elif age == "45〜59歳":
            days = 180
        else:
            days = 150
    total = daily_benefit * days
    st.divider()
    st.subheader("📋 診断結果")
    col1, col2, col3 = st.columns(3)
    col1.metric("1日あたり", f"¥{int(daily_benefit):,}")
    col2.metric("給付日数", f"{days}日")
    col3.metric("給付総額（目安）", f"¥{int(total):,}")
    st.info("※ あくまで目安です。正確な金額はハローワークにご確認ください。")
    st.divider()
    st.markdown("### 🏦 給付を受け取りながら転職を有利に進めませんか？")
    st.markdown("""
転職エージェントに登録すると、求職活動実績にもなります。
失業給付を受け取りながら、理想の転職先を探しましょう。
""")
    st.link_button("✅ 無料で転職サポートを受ける →", "https://www.doda.jp/")
