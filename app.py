import streamlit as st
import pandas as pd

# 새로운 엑셀 파일과 첫 번째 시트 사용
traits_df = pd.read_excel('TraitsCombine-helen-Dorothy.xlsx', sheet_name=0)
values_df = pd.read_excel('Value.xlsx')

st.title("🌿 Trait & Value Viewer")

# 🔹 알파벳 순 정렬된 드롭다운
trait_list = sorted(traits_df['trait'].unique())
selected_trait = st.selectbox("🔍 Select a Trait", options=trait_list)

# Trait 정보 출력
trait_info = traits_df[traits_df['trait'] == selected_trait]

st.header(f"📝 Trait Information: {selected_trait}")

for col in trait_info.columns:
    value = trait_info.iloc[0][col]
    st.write(f"**{col}**: {value}")

# Value + 설명
st.subheader("📋 Associated Values & Descriptions")

value_table = values_df[values_df['trait'] == selected_trait][['allowed_values_levels', 'categorical_trait_description']]

if not value_table.empty:
    value_table = value_table.rename(columns={
        'allowed_values_levels': 'Value',
        'categorical_trait_description': 'Description'
    })
    st.dataframe(value_table)   # 스크롤 가능한 표로 출력
else:
    st.info("No associated values found for this trait.")
