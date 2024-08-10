import streamlit as st
import pandas as pd
def multiple_tabs():

    # Load your data here (this is just a placeholder)
    data = {
        'Product': ['A', 'B', 'C', 'D'],
        'Sales': [100, 150, 200, 120],
        'Contribution (%)': [25, 37.5, 50, 30],
        'Date': pd.date_range(start='2023-01-01', periods=4, freq='D')
    }
    df = pd.DataFrame(data)

    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Data Overview", "Product Contribution", "Sales Analysis"])

    with tab1:
        st.header("Data Overview")
        st.write("This tab provides an overview of the data.")
        st.dataframe(df)

    with tab2:
        st.header("Product Contribution")
        st.write("This tab shows the contribution of each product.")
        st.bar_chart(df.set_index('Product')['Contribution (%)'])

    with tab3:
        st.header("Sales Analysis")
        st.write("This tab analyzes sales data.")
        st.line_chart(df.set_index('Product')['Sales'])

if __name__ == "__main__":
    multiple_tabs()
