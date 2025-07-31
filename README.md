# Himalayan Expeditions Analytics Project

**George Brown College | Capstone Project | 2025**
**Course**: Big Data Tools and Technologies II
**Dataset Source**: [Kaggle - Himalayan Expeditions](https://www.kaggle.com/datasets/siddharth0935/himalayan-expeditions)

## Project Overview

This project presents a complete end-to-end data analytics pipeline that analyzes real-world mountaineering data from Himalayan expeditions. The objective is to derive meaningful insights into patterns of success, risk, and logistics associated with high-altitude climbing activities across multiple decades.

By integrating tools such as Alteryx, Snowflake, SSAS Tabular Model, PySpark, and Power BI, this project demonstrates the application of modern big data technologies to answer business-relevant questions.

## Objectives

* Perform data cleaning, transformation, and modeling using industry tools.
* Conduct distributed data analysis using PySpark.
* Build semantic models for interactive querying in SSAS.
* Design insightful dashboards using Power BI to answer analytical questions.

## Tools and Technologies

| Tool         | Purpose                                  |
| ------------ | ---------------------------------------- |
| Alteryx      | ETL, Data Cleaning, Aggregation          |
| Snowflake    | Cloud Data Warehouse and Schema Modeling |
| SSAS Tabular | Semantic Model and DAX Queries           |
| PySpark      | Distributed Analysis on VM               |
| Power BI     | Data Visualization and Reporting         |

## Dataset Summary

The project uses data from three CSV files:

* `peaks.csv`: Contains metadata for 480 Himalayan peaks including height, region, and accessibility.
* `exped.csv`: Details of 11,417 expeditions such as season, route, success rate, and oxygen usage.
* `members.csv`: Information on 88,965 individual expedition members including demographics, summit success, and fatalities.

Each dataset was preprocessed, joined, and modeled into fact and dimension tables.

## Data Modeling Workflow

### Step 1: Data Preprocessing (Alteryx)

* Input, cleaned, and joined data from all three CSV files.
* Replaced missing values, handled type mismatches, and filtered outliers.
* Created:

  * `Fact_Expeditions.csv`
  * `Dim_Peaks.csv`
  * `Dim_Expeditions.csv`
  * `Dim_Members.csv`

### Step 2: Data Modeling (Snowflake & SSAS)

* Uploaded processed files to Snowflake.
* Defined schema and staged data using `PUT` and `COPY INTO` commands.
* Created a joined view for analysis.
* Imported model into SSAS to define relationships and prepare for Power BI connection.

## Analytical Queries (PySpark)

Executed five core analytical queries using PySpark on a VM:

1. Correlation between peak height and success rate.
2. Binning expeditions by success rate and team size.
3. Frequency analysis of expedition seasons.
4. Nation-wise ranking based on summit counts.
5. Average expedition duration by region and year.

## Business Questions Addressed

1. How does peak height influence the number of expeditions and success rates?
2. What trends exist in expedition outcomes across seasons and years?
3. Which peaks have the highest fatality rates?
4. Which countries contribute the most climbers and expeditions?
5. How does the use of supplemental oxygen relate to expedition safety and success?

## Power BI Visualizations

* Scatter plots to analyze expedition size and success by peak height.
* Line graphs showing seasonal success trends from 1950 to 2024.
* Donut charts highlighting the most dangerous peaks by death count.
* Bar charts representing nation-wise participation in expeditions.
* Area charts comparing success and fatalities with and without oxygen use.

## Key Insights

* Mt. Everest has the highest number of expeditions and fatalities.
* Spring and Autumn are the most favorable seasons for summiting.
* Supplemental oxygen is associated with higher success and lower death rates.
* Smaller teams showed a higher success rate in some conditions.
* European nations dominate expedition contributions to the Himalayas.

## Challenges and Resolutions

| Challenge                               | Resolution                                                   |
| --------------------------------------- | ------------------------------------------------------------ |
| Data type mismatches in SSMS/Snowflake  | Adjusted schema and column formats                           |
| Inconsistent or missing values          | Replaced using Alteryx cleansing tools and conditional logic |
| Partial data loads in Snowflake         | Used `ON_ERROR = CONTINUE` and reconfigured `CSV_FORMAT`     |
| Null handling in joins and aggregations | Applied full joins and column standardization techniques     |

## Deliverables

* Cleaned and joined CSV files (Fact and Dimensions)
* Snowflake schema and SQL scripts
* SSAS tabular model
* PySpark scripts (`.py`)
* Power BI report file (`.pbix`)
* Project report (PDF)

## License

This project was developed strictly for academic and learning purposes.
All dataset rights belong to the original source published on Kaggle.


