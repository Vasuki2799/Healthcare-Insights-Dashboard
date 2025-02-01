
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import pandas as pd
import plotly.express as px

# Customizing the page layout and background
st.set_page_config(page_title="Healthcare Insights Dashboard", layout="wide")

# Sidebar with navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Top Chart", "Explore Data", "About"],
        icons=["house", "bar-chart", "database", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f8f9fa"},
            "icon": {"color": "#333", "font-size": "20px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px", "color": "#333"},
            "nav-link-selected": {"background": "#007bff", "color": "white", "font-weight": "bold"},
        },
    )

# Title of the project
st.markdown("<h1 style='color: #007bff;'>🏥 Healthcare Insights Dashboard</h1>", unsafe_allow_html=True)

if selected == "Home":
    st.markdown("<h2 style='color: #0056b3;'>📊 Project Overview</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Objective:** Provide insights into healthcare data for better decision-making.
    - **Data Sources:** Patient demographics, treatment records, facility utilization.
    - **Analysis:** Trends in patient visits, billing amounts, and healthcare facility efficiency.
    """)
    
    st.markdown("<h2 style='color: #0056b3;'>🔍 Key Features</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Interactive Charts:** Explore patient data through visual analytics.
    - **SQL Queries:** Retrieve key metrics from the healthcare dataset.
    - **Business Use Cases:** Identify trends and optimize hospital resources.
    """)        

    # Video placeholder
    st.video("/Users/arul/Downloads/What is quality of care .mp4")
    
#Top Chart

elif selected == "Top Chart":
    st.markdown("<h2 style='color: #0056b3;'>📈 Top Chart</h2>", unsafe_allow_html=True)
    st.write("Visualizations of key healthcare metrics will be displayed here.")

    # Connect to MySQL database
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Arulezhil@71',
        'database': 'healthcare_dataset'
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # Query for average billing amount by bed occupancy type
    query_6 = """
    SELECT Bed_Occupancy, AVG(`Billing_Amount`) AS avg_billing
    FROM healthcare_data
    GROUP BY Bed_Occupancy
    ORDER BY avg_billing DESC;
    """
    df_billing = pd.read_sql(query_6, conn)
    
    # Query for total billing amount by doctor
    query_7 = """
    SELECT Doctor, SUM(`Billing_Amount`) AS total_billing
    FROM healthcare_data
    GROUP BY Doctor
    ORDER BY total_billing DESC;
    """
    df_doctor_billing = pd.read_sql(query_7, conn)
    
    # Query for average billing amount by diagnosis
    query_8 = """
    SELECT Diagnosis, AVG(`Billing_Amount`) AS avg_billing
    FROM healthcare_data
    GROUP BY Diagnosis
    ORDER BY avg_billing DESC;
    """
    df_diagnosis_billing = pd.read_sql(query_8, conn)
    
    # Query for average health insurance amount by diagnosisst.markdown("<h3 style='color: #007bff;'>Average Health Insurance Amount by Diagnosis</h3>", unsafe_allow_html=True)
    query_14 = """
    SELECT Diagnosis, AVG(`Health_Insurance_Amount`) AS avg_health_insurance
    FROM healthcare_data
    GROUP BY Diagnosis
    ORDER BY avg_health_insurance DESC;
    """
    df_health_insurance = pd.read_sql(query_14, conn)
    
    # Close connection
    cursor.close()
    conn.close()
    
    # Pie chart for average billing per bed occupancy type
    fig_pie = px.pie(df_billing, names='Bed_Occupancy', values='avg_billing', 
                     title='Average Billing Amount by Bed Occupancy Type', 
                     color_discrete_sequence=px.colors.sequential.Redor, 
                     hole=0.4)
    
    # Bar chart for total billing amount per doctor
    fig_bar = px.bar(df_doctor_billing, x='Doctor', y='total_billing',
                     title='Total Billing Amount by Doctor',
                     labels={'Doctor': 'Doctor', 'total_billing': 'Total Billing Amount'},
                     color='total_billing',
                     color_continuous_scale='Viridis')
    
    # Pie chart for average billing per diagnosis
    fig_pie_diag = px.pie(df_diagnosis_billing, names='Diagnosis', values='avg_billing', 
                          title='Average Billing Amount by Diagnosis', 
                          color_discrete_sequence=px.colors.sequential.Magma, 
                          hole=0.3)
    
    # Pie chart for average health insurance amount by diagnosis
    fig_pie_insurance = px.pie(df_health_insurance, names='Diagnosis', values='avg_health_insurance', 
                               title='Average Health Insurance Amount by Diagnosis', 
                               color_discrete_sequence=px.colors.sequential.Blues, 
                               hole=0.3)
    
    # Bar chart for average health insurance amount by diagnosis
    fig_bar_insurance = px.bar(df_health_insurance, x='Diagnosis', y='avg_health_insurance',
                               title='Average Health Insurance Amount by Diagnosis',
                               labels={'Diagnosis': 'Diagnosis', 'avg_health_insurance': 'Avg Health Insurance Amount'},
                               color='avg_health_insurance',
                               color_continuous_scale='Blues')
    
    # Display the charts in Streamlit
    st.plotly_chart(fig_pie)
    st.plotly_chart(fig_bar)
    st.plotly_chart(fig_pie_insurance)
    st.plotly_chart(fig_pie_diag)
    st.plotly_chart(fig_bar_insurance)

# Explore Data    

elif selected == "Explore Data":
    st.markdown("<h2 style='color: #0056b3;'>🔬 Explore Data</h2>", unsafe_allow_html=True)
    st.write("Detailed breakdown of patient demographics and trends.")

    # Connect to MySQL database
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Arulezhil@71',
        'database': 'healthcare_dataset'
    }

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # Treatment and Service Trends
    st.markdown("<h3 style='color: #007bff;'>Treatment and Service Trends</h3>", unsafe_allow_html=True)
    query_trends = """
    SELECT Test, COUNT(*) AS frequency
    FROM healthcare_data
    GROUP BY Test
    ORDER BY frequency DESC;
    """
    df_trends = pd.read_sql(query_trends, conn)
    
    fig_treatment = px.bar(df_trends, x='Test', y='frequency',
                           title='Frequency of Treatments',
                           labels={'Test': 'Treatment Type', 'frequency': 'Number of Cases'},
                           color='frequency',
                           color_continuous_scale='Blues')
    
    st.plotly_chart(fig_treatment)
    
    
    # Healthcare Facility Utilization
    st.markdown("<h3 style='color: #007bff;'>Healthcare Facility Utilization</h3>", unsafe_allow_html=True)
    query_facility_utilization = """
    SELECT DATE(Admit_Date) AS admit_date, COUNT(*) AS num_patients
    FROM healthcare_data
    GROUP BY admit_date
    ORDER BY admit_date;
    """
    df_facility_utilization = pd.read_sql(query_facility_utilization, conn)
    
    fig_facility_utilization = px.line(df_facility_utilization, x='admit_date', y='num_patients',
                                       title='Admission Trends Over Time',
                                       labels={'admit_date': 'Date', 'num_patients': 'Number of Admissions'},
                                       markers=True)
    
    st.plotly_chart(fig_facility_utilization)
    
    
    # Data-Driven Decision Making
    st.markdown("<h3 style='color: #007bff;'>Data-Driven Decision Making</h3>", unsafe_allow_html=True)
    query_decision_making = """
    SELECT Diagnosis, COUNT(*) AS num_cases
    FROM healthcare_data
    GROUP BY Diagnosis
    ORDER BY num_cases DESC;
    """
    df_decision_making = pd.read_sql(query_decision_making, conn)
    
    fig_decision_making = px.pie(df_decision_making, names='Diagnosis', values='num_cases',
                                 title='Cases by Diagnosis Type',
                                 color_discrete_sequence=px.colors.sequential.Redor, 
                                 hole=0.4)
    
    st.plotly_chart(fig_decision_making)

    # Add Filtering Options
    st.markdown("<h3 style='color: #007bff;'>🔍 Filter Data</h3>", unsafe_allow_html=True)

    # Date Range Filter (Admission Date)
    st.markdown("📅 **Filter by Admission Date**")
    admit_start_date = st.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
    admit_end_date = st.date_input("End Date", value=pd.to_datetime("2024-12-31"))

    # Dropdown Filter (Doctor, Diagnosis, Bed Occupancy)
    st.markdown("👨‍⚕️ **Filter by Doctor, Diagnosis, or Bed Occupancy**")
    cursor.execute("SELECT DISTINCT Doctor FROM healthcare_data")
    doctor_list = [row[0] for row in cursor.fetchall()]
    doctor_selected = st.selectbox("Select Doctor", ["All"] + doctor_list)

    cursor.execute("SELECT DISTINCT Diagnosis FROM healthcare_data")
    diagnosis_list = [row[0] for row in cursor.fetchall()]
    diagnosis_selected = st.selectbox("Select Diagnosis", ["All"] + diagnosis_list)

    cursor.execute("SELECT DISTINCT Bed_Occupancy FROM healthcare_data")
    bed_list = [row[0] for row in cursor.fetchall()]
    bed_selected = st.selectbox("Select Bed Occupancy", ["All"] + bed_list)

    # Billing Amount Range Filter
    st.markdown("💰 **Filter by Billing Amount**")
    billing_range = st.slider("Select Billing Amount Range", min_value=0, max_value=100000, value=(500, 50000))

    # Constructing Query with Filters
    query_filter = f"""
    SELECT * FROM healthcare_data
    WHERE Admit_Date BETWEEN '{admit_start_date}' AND '{admit_end_date}'
    AND Billing_Amount BETWEEN {billing_range[0]} AND {billing_range[1]}
    """

    if doctor_selected != "All":
        query_filter += f" AND Doctor = '{doctor_selected}'"

    if diagnosis_selected != "All":
        query_filter += f" AND Diagnosis = '{diagnosis_selected}'"

    if bed_selected != "All":
        query_filter += f" AND Bed_Occupancy = '{bed_selected}'"

    # Fetch Data with Filters
    df_filtered = pd.read_sql(query_filter, conn)

    # Display Filtered Data
    st.markdown("<h3 style='color: #007bff;'>📋 Filtered Data</h3>", unsafe_allow_html=True)
    st.dataframe(df_filtered)

    # Close Connection
    cursor.close()
    conn.close()

#About
    

elif selected == "About":
    st.markdown("<h2 style='color: #0056b3;'>ℹ️ About</h2>", unsafe_allow_html=True)
    st.write("This dashboard provides insights into healthcare data.")

    st.markdown("""
    ### Project Overview
    - This dashboard provides insights into healthcare data.
    - It helps hospital administrators and stakeholders make data-driven decisions.

    ### Features
    - **Top Charts:** Summarized key statistics.
    - **Explore Data:** Interactive visualizations for treatment trends and facility utilization.
    - **SQL Integration:** Real-time query execution for updated insights.

    ### Technologies Used
    - Python, Streamlit, MySQL, Plotly, Pandas
    """)
    
    st.image("/Users/arul/Documents/images health/pexels-totalshape-2383010.jpg", use_container_width=True)
    

