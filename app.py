import streamlit as st
import pandas as pd

# Load trait and value data from Excel files
traits_df = pd.read_excel('TraitsCombine-helen-Dorothy.xlsx', sheet_name=0)  # Trait metadata
values_df = pd.read_excel('Value.xlsx')  # Trait value descriptions

st.title("🌿 Trait & Value Viewer")

# Trait selector
trait_list = sorted(traits_df['trait'].unique())
selected_trait = st.selectbox("🔍 Select a Trait", options=trait_list)

# Display basic trait information
trait_info = traits_df[traits_df['trait'] == selected_trait]
st.header(f"📝 Trait Information: {selected_trait}")

for col in trait_info.columns:
    value = trait_info.iloc[0][col]
    st.write(f"**{col}**: {value}")

# Display associated values and descriptions
st.subheader("📋 Associated Values & Descriptions")

value_table = values_df[values_df['trait'] == selected_trait][['allowed_values_levels', 'categorical_trait_description']]

if not value_table.empty:
    value_table = value_table.rename(columns={
        'allowed_values_levels': 'Value',
        'categorical_trait_description': 'Description'
    })
    st.dataframe(value_table)  # Show table of values
else:
    st.info("No associated values found for this trait.")
