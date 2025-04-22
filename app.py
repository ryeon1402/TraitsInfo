import streamlit as st
import pandas as pd

# 엑셀 파일 불러오기
traits_df = pd.read_excel('TraitsCombine.xlsx')
values_df = pd.read_excel('Value.xlsx')

st.title("🌿 Trait & Value Viewer")

# --- Trait 선택 ---
trait_list = traits_df['trait'].unique()
selected_trait = st.selectbox("🔍 Select a Trait", options=trait_list)

# --- 선택한 Trait 정보 표시 ---
trait_info = traits_df[traits_df['trait'] == selected_trait]

st.header(f"📝 Trait Information: {selected_trait}")

for col in trait_info.columns:
    value = trait_info.iloc[0][col]
    st.write(f"**{col}**: {value}")

# --- Value + 설명 표시 ---
st.subheader("📋 Associated Values & Descriptions")

value_table = values_df[values_df['trait'] == selected_trait][['allowed_values_levels', 'categorical_trait_description']]

if not value_table.empty:
    value_table = value_table.rename(columns={
        'allowed_values_levels': 'Value',
        'categorical_trait_description': 'Description'
    })
    st.table(value_table)
else:
    st.info("No associated values found for this trait.")
