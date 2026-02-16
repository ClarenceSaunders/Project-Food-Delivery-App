import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set page title and icon
st.set_page_config(
    page_title="Food Order Analytics Dashboard",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select a Page",
    ["Home", "Data Overview", "Business Metrics", "Exploratory Data Analysis", "Advanced Analytics"]
)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('food_order_cleaned.csv')
    # Convert rating to numeric if needed
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    return df

df = load_data()

# Calculate key metrics
@st.cache_data
def calculate_metrics():
    total_orders = df['order_id'].nunique()
    total_customers = df['customer_id'].nunique()
    avg_order_value = df['cost_of_the_order'].mean()
    avg_rating = df['rating'].mean()
    avg_prep_time = df['food_preparation_time'].mean()
    avg_delivery_time = df['delivery_time'].mean()
    total_revenue = avg_order_value * total_orders
    
    return {
        'total_orders': total_orders,
        'total_customers': total_customers,
        'avg_order_value': avg_order_value,
        'avg_rating': avg_rating,
        'avg_prep_time': avg_prep_time,
        'avg_delivery_time': avg_delivery_time,
        'total_revenue': total_revenue
    }

metrics = calculate_metrics()

# ============================================================================
# HOME PAGE
# ============================================================================
if page == "Home":
    st.title("🍕 Food Order Analytics Dashboard")
    st.subheader("Welcome to the Food Order Data Explorer!")
    
    st.write("""
        This interactive dashboard provides comprehensive insights into food order data. 
        Explore order patterns, customer behavior, delivery performance, and more!
        
        **Features:**
        - 📊 Real-time business metrics
        - 📈 Visual data exploration
        - 🔍 Detailed analytics
        - 🎯 Performance indicators
        
        Use the sidebar to navigate through different sections.
    """)
    
    st.divider()
    
    # Key metrics overview
    st.subheader("📈 Quick Metrics Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Orders", f"{metrics['total_orders']:,}", delta="Orders")
    
    with col2:
        st.metric("Total Customers", f"{metrics['total_customers']:,}", delta="Customers")
    
    with col3:
        st.metric("Avg Order Value", f"${metrics['avg_order_value']:.2f}", delta="USD")
    
    with col4:
        st.metric("Avg Rating", f"{metrics['avg_rating']:.2f}/5.0", delta="Stars")
    
    st.divider()
    
    # Additional info
    col5, col6, col7 = st.columns(3)
    
    with col5:
        st.metric("Total Revenue", f"${metrics['total_revenue']:,.2f}", delta="USD")
    
    with col6:
        st.metric("Avg Prep Time", f"{metrics['avg_prep_time']:.0f} min", delta="Minutes")
    
    with col7:
        st.metric("Avg Delivery Time", f"{metrics['avg_delivery_time']:.0f} min", delta="Minutes")

# ============================================================================
# DATA OVERVIEW
# ============================================================================
elif page == "Data Overview":
    st.title("🔢 Data Overview")
    
    st.subheader("About the Dataset")
    st.write("""
        This food order dataset contains comprehensive information about food orders,
        including customer details, order values, ratings, and delivery performance metrics.
    """)
    
    # Dataset Display
    st.subheader("Dataset Preview")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.checkbox("Show Full DataFrame"):
            st.dataframe(df, use_container_width=True)
    
    with col2:
        if st.checkbox("Show Data Summary"):
            st.write("**Dataset Shape:**")
            st.write(f"Rows: {df.shape[0]:,} | Columns: {df.shape[1]}")
            
            st.write("\n**Data Types:**")
            st.dataframe(df.dtypes)
    
    st.divider()
    
    # Statistical Summary
    st.subheader("Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)
    
    st.divider()
    
    # Column Information
    st.subheader("Column Information")
    col_info = pd.DataFrame({
        'Column': df.columns,
        'Type': df.dtypes,
        'Non-Null': df.count(),
        'Missing': df.isnull().sum()
    })
    st.dataframe(col_info, use_container_width=True)

# ============================================================================
# BUSINESS METRICS
# ============================================================================
elif page == "Business Metrics":
    st.title("📊 Business Metrics Dashboard")
    
    # Key Metrics Display
    st.subheader("Key Performance Indicators (KPIs)")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Orders",
            f"{metrics['total_orders']:,}",
            delta="Orders Processed"
        )
    
    with col2:
        st.metric(
            "Total Customers",
            f"{metrics['total_customers']:,}",
            delta="Unique Customers"
        )
    
    with col3:
        st.metric(
            "Avg Order Value",
            f"${metrics['avg_order_value']:.2f}",
            delta="Per Order"
        )
    
    with col4:
        st.metric(
            "Customer Rating",
            f"{metrics['avg_rating']:.2f}/5.0",
            delta="Average"
        )
    
    st.divider()
    
    col5, col6, col7 = st.columns(3)
    
    with col5:
        st.metric(
            "Total Revenue",
            f"${metrics['total_revenue']:,.2f}",
            delta="USD"
        )
    
    with col6:
        st.metric(
            "Avg Prep Time",
            f"{metrics['avg_prep_time']:.0f} min",
            delta="Preparation"
        )
    
    with col7:
        st.metric(
            "Avg Delivery Time",
            f"{metrics['avg_delivery_time']:.0f} min",
            delta="Delivery"
        )
    
    st.divider()
    
    # Metrics Visualization
    st.subheader("Detailed Metrics Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Orders per Customer Distribution
        orders_per_customer = df.groupby('customer_id').size()
        fig = px.histogram(
            orders_per_customer,
            nbins=30,
            title="Orders per Customer Distribution",
            labels={'value': 'Number of Orders', 'count': 'Frequency'},
            color_discrete_sequence=['#636EFA']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Total Orders per Customer
        fig = px.box(
            orders_per_customer,
            title="Orders per Customer - Box Plot",
            labels={'value': 'Number of Orders'},
            color_discrete_sequence=['#EF553B']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Revenue Analysis
    col3, col4 = st.columns(2)
    
    with col3:
        # Revenue Distribution
        fig = px.histogram(
            df,
            x='cost_of_the_order',
            nbins=30,
            title="Order Value Distribution",
            labels={'cost_of_the_order': 'Order Cost ($)', 'count': 'Frequency'},
            color_discrete_sequence=['#00CC96']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        # Cumulative Revenue
        sorted_df = df.sort_values('cost_of_the_order')
        sorted_df['cumulative_revenue'] = sorted_df['cost_of_the_order'].cumsum()
        
        fig = px.line(
            sorted_df,
            y='cumulative_revenue',
            title="Cumulative Revenue",
            labels={'cumulative_revenue': 'Cumulative Revenue ($)', 'index': 'Order Number'},
            color_discrete_sequence=['#AB63FA']
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# EXPLORATORY DATA ANALYSIS
# ============================================================================
elif page == "Exploratory Data Analysis":
    st.title("📊 Exploratory Data Analysis (EDA)")
    
    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect(
        "Visualization Options",
        ['Order Value Distribution', 'Rating Analysis', 'Time Analysis', 'Scatterplots', 'Correlations']
    )
    
    obj_cols = df.select_dtypes(include='object').columns.tolist()
    num_cols = df.select_dtypes(include='number').columns.tolist()
    
    # Order Value Distribution
    if 'Order Value Distribution' in eda_type:
        st.subheader("💰 Order Value Distribution")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.histogram(
                df,
                x='cost_of_the_order',
                nbins=30,
                title="Order Cost Distribution",
                labels={'cost_of_the_order': 'Order Cost ($)', 'count': 'Frequency'},
                color_discrete_sequence=['#636EFA']
            )
            fig.add_vline(
                x=metrics['avg_order_value'],
                line_dash="dash",
                line_color="red",
                annotation_text=f"Avg: ${metrics['avg_order_value']:.2f}"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.box(
                df,
                y='cost_of_the_order',
                title="Order Cost - Box Plot",
                labels={'cost_of_the_order': 'Order Cost ($)'},
                color_discrete_sequence=['#EF553B']
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Rating Analysis
    if 'Rating Analysis' in eda_type:
        st.subheader("⭐ Rating Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.histogram(
                df,
                x='rating',
                nbins=20,
                title="Customer Rating Distribution",
                labels={'rating': 'Rating', 'count': 'Frequency'},
                color_discrete_sequence=['#00CC96']
            )
            fig.add_vline(
                x=metrics['avg_rating'],
                line_dash="dash",
                line_color="red",
                annotation_text=f"Avg: {metrics['avg_rating']:.2f}"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            rating_counts = df['rating'].value_counts().sort_index()
            fig = px.pie(
                values=rating_counts.values,
                names=rating_counts.index,
                title="Rating Distribution (Pie Chart)",
                color_discrete_sequence=px.colors.sequential.RdBu
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Time Analysis
    if 'Time Analysis' in eda_type:
        st.subheader("⏱️ Time Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.histogram(
                df,
                x='food_preparation_time',
                nbins=30,
                title="Food Preparation Time Distribution",
                labels={'food_preparation_time': 'Prep Time (minutes)', 'count': 'Frequency'},
                color_discrete_sequence=['#FF6692']
            )
            fig.add_vline(
                x=metrics['avg_prep_time'],
                line_dash="dash",
                line_color="darkred",
                annotation_text=f"Avg: {metrics['avg_prep_time']:.0f} min"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.histogram(
                df,
                x='delivery_time',
                nbins=30,
                title="Delivery Time Distribution",
                labels={'delivery_time': 'Delivery Time (minutes)', 'count': 'Frequency'},
                color_discrete_sequence=['#FFA15A']
            )
            fig.add_vline(
                x=metrics['avg_delivery_time'],
                line_dash="dash",
                line_color="darkred",
                annotation_text=f"Avg: {metrics['avg_delivery_time']:.0f} min"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Scatterplots
    if 'Scatterplots' in eda_type:
        st.subheader("📍 Scatterplot Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.scatter(
                df,
                x='cost_of_the_order',
                y='rating',
                title="Order Cost vs. Customer Rating",
                labels={'cost_of_the_order': 'Order Cost ($)', 'rating': 'Rating'},
                color_discrete_sequence=['#636EFA']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.scatter(
                df,
                x='food_preparation_time',
                y='delivery_time',
                title="Preparation Time vs. Delivery Time",
                labels={'food_preparation_time': 'Prep Time (min)', 'delivery_time': 'Delivery Time (min)'},
                color_discrete_sequence=['#EF553B']
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Correlations
    if 'Correlations' in eda_type:
        st.subheader("🔗 Correlation Analysis")
        
        # Filter numeric columns for correlation
        numeric_df = df.select_dtypes(include=[np.number])
        corr_matrix = numeric_df.corr()
        
        fig = px.imshow(
            corr_matrix,
            labels=dict(x="Features", y="Features", color="Correlation"),
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            color_continuous_scale="RdBu",
            zmin=-1,
            zmax=1,
            title="Feature Correlation Matrix",
            aspect="auto"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("**Correlation Values:**")
        st.dataframe(corr_matrix, use_container_width=True)

# ============================================================================
# ADVANCED ANALYTICS
# ============================================================================
elif page == "Advanced Analytics":
    st.title("🔬 Advanced Analytics")
    
    st.subheader("Segment Analysis")
    
    # Create price segments
    df_temp = df.copy()
    df_temp['price_segment'] = pd.cut(
        df_temp['cost_of_the_order'],
        bins=3,
        labels=['Budget', 'Standard', 'Premium']
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        segment_counts = df_temp['price_segment'].value_counts()
        fig = px.pie(
            values=segment_counts.values,
            names=segment_counts.index,
            title="Order Segments by Price",
            color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        segment_avg_rating = df_temp.groupby('price_segment')['rating'].mean()
        fig = px.bar(
            x=segment_avg_rating.index,
            y=segment_avg_rating.values,
            title="Average Rating by Price Segment",
            labels={'x': 'Price Segment', 'y': 'Average Rating'},
            color=segment_avg_rating.index,
            color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        segment_avg_value = df_temp.groupby('price_segment')['cost_of_the_order'].mean()
        fig = px.bar(
            x=segment_avg_value.index,
            y=segment_avg_value.values,
            title="Average Order Value by Segment",
            labels={'x': 'Price Segment', 'y': 'Average Order Value ($)'},
            color=segment_avg_value.index,
            color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Performance Metrics by Segment
    st.subheader("Performance Metrics by Price Segment")
    
    segment_stats = df_temp.groupby('price_segment').agg({
        'order_id': 'count',
        'cost_of_the_order': ['mean', 'sum'],
        'rating': 'mean',
        'food_preparation_time': 'mean',
        'delivery_time': 'mean'
    }).round(2)
    
    segment_stats.columns = ['Number of Orders', 'Avg Order Value', 'Total Revenue', 
                             'Avg Rating', 'Avg Prep Time (min)', 'Avg Delivery Time (min)']
    
    st.dataframe(segment_stats, use_container_width=True)
    
    st.divider()
    
    # Rating Categories
    st.subheader("Analysis by Rating Category")
    
    df_temp['rating_category'] = pd.cut(
        df_temp['rating'],
        bins=[0, 2, 3, 4, 5],
        labels=['Poor', 'Average', 'Good', 'Excellent']
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        rating_cat_counts = df_temp['rating_category'].value_counts()
        fig = px.bar(
            x=rating_cat_counts.index,
            y=rating_cat_counts.values,
            title="Orders by Rating Category",
            labels={'x': 'Rating Category', 'y': 'Number of Orders'},
            color=rating_cat_counts.index,
            color_discrete_sequence=['#FF6692', '#FFA15A', '#00CC96', '#636EFA']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        rating_cat_avg_value = df_temp.groupby('rating_category')['cost_of_the_order'].mean()
        fig = px.bar(
            x=rating_cat_avg_value.index,
            y=rating_cat_avg_value.values,
            title="Average Order Value by Rating Category",
            labels={'x': 'Rating Category', 'y': 'Average Order Value ($)'},
            color=rating_cat_avg_value.index,
            color_discrete_sequence=['#FF6692', '#FFA15A', '#00CC96', '#636EFA']
        )
        st.plotly_chart(fig, use_container_width=True)