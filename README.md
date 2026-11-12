# 📊 Sales Analysis Performance Dashboard (Power BI)

An interactive Power BI dashboard for analyzing retail sales performance across **brands, stores, regions, product categories and time**. The data is prepared using a **Medallion Architecture** (Bronze → Silver → Gold), and the dashboard is built on the clean, business-ready Gold layer.

🔗 **Live Dashboard:** [View in Power BI](https://app.powerbi.com/reportEmbed?reportId=4a461ab1-8974-411f-9a3f-a65bc9f520da&autoAuth=true&ctid=45da25de-8003-4abf-bea8-55aba615e5e7)

---

## Table of Contents

1. [Overview](#overview)
2. [Objectives](#objectives)
3. [Data Architecture – Medallion](#data-architecture--medallion)
4. [Dashboard Pages](#dashboard-pages)
   - [Page 1: Brand Wise Sales](#page-1-brand-wise-sales)
   - [Page 2: Store Wise Sales](#page-2-store-wise-sales)
5. [Filters and Navigation](#filters-and-navigation)
6. [How to Use the Dashboard](#how-to-use-the-dashboard)
7. [Tools and Techniques](#tools-and-techniques)
8. [Repository Structure](#repository-structure)
9. [Future Enhancements](#future-enhancements)

---

## Overview

The dashboard analyzes sales for four fashion brands — **ONLY, JACK & JONES, SELECTED and VERO MODA** — across stores and regions in India. It has two report pages connected through navigation buttons:

- **Brand Wise Sales** – analysis by brand, category and sub-category.
- **Store Wise Sales** – analysis by store, region and month.

Users can filter by store, year, month, season, region and sub-category to explore the data from different angles.

---

## Objectives

- Track overall sales, margin and units sold in one place.
- Compare brand performance year over year.
- Identify top-selling and low-margin categories and sub-categories.
- Find the best performing stores and regions.
- Understand monthly and seasonal trends to support planning and stock decisions.

---

## Data Architecture – Medallion

The data behind this dashboard is organized in three layers, where each layer improves data quality step by step before it reaches the report.

```
Source Data  ──►  🥉 Bronze  ──►  🥈 Silver  ──►  🥇 Gold  ──►  📊 Power BI Dashboard
(raw files)       (raw)          (cleaned)       (business-ready)
```

### 🥉 Bronze Layer – Raw Data
- Stores data exactly as it arrives from the source (sales transactions, store details, product details).
- No changes are made, so the original data is always available for reprocessing or audit.
- Ingestion metadata such as load time can be added for tracking.

### 🥈 Silver Layer – Cleaned and Standardized Data
- Removes duplicate records and handles missing or invalid values.
- Standardizes data types, date formats and text values (for example, store and brand names).
- Applies data quality checks so only valid records move forward.
- Joins related data such as sales with store and product details.

### 🥇 Gold Layer – Business-Ready Data
- Contains aggregated, reporting-ready tables designed for analysis.
- Organized around business needs such as sales by brand, store, region, category and month.
- Includes key measures like total sales, net margin and units sold.
- Power BI connects to this layer, so the dashboard always uses clean and trusted data.

### Why Medallion Architecture?
- **Data quality:** Each layer improves accuracy and consistency.
- **Traceability:** Any number in the dashboard can be traced back to raw data.
- **Reusability:** Silver and Gold tables can be reused by other reports and teams.
- **Performance:** Power BI reads pre-aggregated Gold tables, so visuals load faster.

---

## Dashboard Pages

### Page 1: Brand Wise Sales

![Brand Wise Sales](images/brand_wise_sales.png)

This page helps users understand performance by **brand, category and sub-category**.

| Visual | What It Shows | How to Use It |
|--------|---------------|---------------|
| **KPI Cards** | Total sales, total margin and total units sold for all brands | Check overall performance; the values update automatically when filters are applied |
| **Brand Logos** | The four brands covered in the analysis | Quick visual reference |
| **Lowest Margin Sub-Categories** (bar chart) | Sub-categories with the lowest margin, using a color gradient | Identify products with weak profitability that may need pricing or assortment review |
| **Distribution of Total Sales** (decomposition tree) | Breakdown of sales from category to sub-category | Click the **+** icons to drill down and see which categories drive sales |
| **Brand-wise Total Sales** (clustered column chart) | Yearly sales for each brand side by side | Compare brands and track their growth over the years |
| **Top 5 Sub-Categories – Sales Over Months** (line chart) | Monthly sales trend for the top five sub-categories | Spot seasonal peaks and slow months for each sub-category |

---

### Page 2: Store Wise Sales

![Store Wise Sales](images/store_wise_sales.png)

This page helps users understand performance by **store, region and month**.

| Visual | What It Shows | How to Use It |
|--------|---------------|---------------|
| **KPI Cards** | Total sales, net margin and units sold | Check overall performance for the selected filters |
| **Sum of Net Margin by Region** (donut chart) | Share of net margin contributed by each region | Compare regions and click a segment to filter the page by that region |
| **Top 5 Performing Stores by Rank Over Years** (line chart) | Yearly rank of the top five stores (rank 1 = best) | Track how store rankings improve or drop over time |
| **Total Units Sold Over the Months** (area chart) | Units sold for each month across all years | Identify peak and slow months for stock and promotion planning |
| **Top 10 Store-wise Total Sales** (column chart) | The ten stores with the highest sales, with a color gradient | Find top revenue stores for benchmarking |

---

## Filters and Navigation

### Slicers

| Slicer | Available On | Purpose |
|--------|--------------|---------|
| Store Name | Both pages | View results for one or more specific stores |
| Year | Both pages | Focus on a particular year |
| Month | Both pages | Focus on specific months |
| Season | Both pages | Filter by season (for example, AW18, AW19) |
| Sub-Category | Brand Wise Sales | Filter by product sub-category |
| Region | Store Wise Sales | Filter by East, North, South or West |

### Navigation Buttons

| Button | Action |
|--------|--------|
| **Brand Wise Sales** | Opens the brand analysis page |
| **Store Wise Sales** | Opens the store analysis page |
| **Reset Filter** | Clears all slicer selections and returns to the default view |

---

## How to Use the Dashboard

1. **Open the dashboard** using the live link above, or open the `.pbix` file in Power BI Desktop.
2. **Choose a page** using the **Brand Wise Sales** or **Store Wise Sales** buttons on the left.
3. **Apply filters** by selecting values in the slicers. You can select multiple values by holding **Ctrl** while clicking.
4. **Cross-filter visuals** by clicking any bar, line point or donut segment. All other visuals on the page update to show related data. Click the same item again to remove the selection.
5. **Drill down** in the Distribution of Total Sales tree by clicking the **+** icons to move from category to sub-category.
6. **View details** by hovering over any visual to see tooltips with exact values.
7. **Focus on a visual** by clicking the **Focus mode** icon at the top-right of the visual to open it in full view.
8. **Reset the view** by clicking **Reset Filter** to clear all selections.

### Example Questions You Can Answer
- Which brand performed best in a particular year?
- Which sub-categories have the lowest margin?
- Which region contributes the most margin?
- Which stores consistently rank in the top five?
- Which months have the highest and lowest sales?

---

## Tools and Techniques

- **Medallion Architecture** – Bronze, Silver and Gold layers for data preparation
- **Power BI Desktop** – data modeling and report design
- **Power BI Service** – publishing and sharing
- **Power Query** – data transformation
- **DAX** – measures for sales, margin, units and store ranking
- **Visuals:** KPI cards, column and bar charts, decomposition tree, line charts, donut chart, area chart and slicers
- **Bookmarks and Buttons** – page navigation and filter reset
- **Conditional Formatting** – color gradients to highlight high and low values

---

## Repository Structure

```
sales-analysis-dashboard/
├── README.md
├── Sales_Analysis_Dashboard.pbix     # Power BI report file
└── images/
    ├── brand_wise_sales.png          # Screenshot of page 1
    └── store_wise_sales.png          # Screenshot of page 2
```

---

## Future Enhancements

- Add year-over-year growth and margin percentage measures.
- Add drill-through pages for individual store and brand details.
- Add target vs actual sales tracking.
- Schedule automatic data refresh in Power BI Service.

---
