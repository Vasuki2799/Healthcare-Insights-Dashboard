# Healthcare Insights Dashboard

## 📌 Project Overview
This project is a **Healthcare Insights Dashboard** designed to analyze healthcare data and provide interactive visualizations. The dashboard helps hospital administrators make data-driven decisions based on patient trends, billing data, and facility utilization.

## 🏥 Key Features
- **Interactive Charts**: Visualizations with Plotly for better insights.
- **SQL Integration**: Fetch data dynamically from a MySQL database.
- **Business Use Cases**: Supports decision-making by analyzing patient demographics, billing trends, and facility utilization.
- **User-Friendly Interface**: Developed using **Streamlit** with an intuitive sidebar navigation.
- **Filtering Options**: Users can filter data using date ranges, dropdown selections, and billing amount ranges.

## 🛠️ Technologies Used
- **Python** (Pandas, Streamlit, Plotly, MySQL Connector)
- **MySQL** (Data storage and retrieval)
- **Streamlit** (For creating an interactive web-based dashboard)

## 📂 Project Structure
```
Healthcare_Insights_Dashboard/
│── app.py                 # Main Streamlit app file
│── requirements.txt       # Dependencies list
│── README.md              # Project documentation
│── images/                # Folder to store dashboard images
│── data/                  # (If any sample data is used)
└── queries/               # SQL queries used in the project
```

## 📊 Dashboard Sections
### **1️⃣ Home**
- Provides an overview of the project, objectives, and key features.
- Displays an introductory image and an embedded video.

### **2️⃣ Top Chart**
- Displays key **business insights** in the form of **bar, pie, and line charts**.
- Covers:
  - **Total Patients**
  - **Max & Min Billing Amount**
  - **Billing Amount by Bed Type**
  - **Total Billing by Doctor**
  - **Average Billing by Diagnosis**
  - **Health Insurance Analysis**

### **3️⃣ Explore Data**
- Provides deep insights into **healthcare facility usage and service trends**.
- Covers:
  - **Treatment & Service Trends**
  - **Admission Trends Over Time**
  - **Data-Driven Decision Making for Hospitals**
  - **Filtering Options:**
    - **Date Filter** – Select a range of **admission** or **discharge** dates.
    - **Dropdown Filter** – Choose specific **Doctors, Diagnosis, or Bed Occupancy**.
    - **Range Slider** – Filter data by **Billing Amount** dynamically.

### **4️⃣ About**
- Explains the **development process** step-by-step with headings and subheadings.
- Includes an **image** for reference.

## 📥 Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Healthcare_Insights_Dashboard.git
   cd Healthcare_Insights_Dashboard
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv env
   source env/bin/activate  # On Mac/Linux
   env\Scripts\activate     # On Windows
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

## 🗂️ SQL Queries Used
The project retrieves data dynamically using SQL queries. Some examples include:
- **Finding total patients:**
  ```sql
  SELECT COUNT(DISTINCT Patient_ID) AS total_patients FROM healthcare_data;
  ```
- **Finding maximum and minimum billing amounts:**
  ```sql
  SELECT MAX(Billing_Amount) AS max_billing, MIN(Billing_Amount) AS min_billing FROM healthcare_data;
  ```
- **Average billing by bed occupancy type:**
  ```sql
  SELECT Bed_Occupancy, AVG(Billing_Amount) FROM healthcare_data GROUP BY Bed_Occupancy;
  ```

## 🎨 Dashboard Preview
(Add screenshots of the dashboard here to showcase different sections.)

## 🏆 Future Enhancements
- Add more **filters** to customize patient data views.
- Implement **machine learning models** for patient admission predictions.
- Improve **UI/UX design** for a better user experience.



## 📃 Project Details
- **Name:** VASUKI ARUL
- **Batch Code:** DS-C-WD-E-B29
- **LinkedIn URL:** (https://www.linkedin.com/in/vasuki27/)
- **Demo Video URL:** (https://www.linkedin.com/posts/vasuki27_sql-dynamic-interactive-activity-7291319779997462528-irc-?utm_source=share&utm_medium=member_desktop)


