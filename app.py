import streamlit as st
import pandas as pd

traits_df = pd.read_excel('TraitsCombine-helen-Dorothy.xlsx', sheet_name=0)
values_df = pd.read_excel('Value.xlsx')

st.title("🌿 Trait & Value Viewer")

trait_list = sorted(traits_df['trait'].unique())
selected_trait = st.selectbox("🔍 Select a Trait", options=trait_list)

trait_info = traits_df[traits_df['trait'] == selected_trait]

st.header(f"📝 Trait Information: {selected_trait}")

for col in trait_info.columns:
    value = trait_info.iloc[0][col]
    st.write(f"**{col}**: {value}")

st.subheader("📋 Associated Values & Descriptions")

value_table = values_df[values_df['trait'] == selected_trait][['allowed_values_levels', 'categorical_trait_description']]

if not value_table.empty:
    value_table = value_table.rename(columns={
        'allowed_values_levels': 'Value',
        'categorical_trait_description': 'Description'
    })
    st.dataframe(value_table)
else:
    st.info("No associated values found for this trait.")
