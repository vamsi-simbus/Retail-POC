# 📊 Sales Analysis Performance Dashboard (Power BI)

An interactive Power BI dashboard that analyzes retail sales performance across **brands, stores, regions, categories and time**. It helps business users quickly understand total sales, margin and units sold, compare brand and store performance, and spot seasonal trends.

🔗 **Live Dashboard:** [View in Power BI](https://app.powerbi.com/your-report-link) *(replace with your published link)*

---

## Table of Contents

1. [Overview](#overview)
2. [Objectives](#objectives)
3. [Dashboard Pages](#dashboard-pages)
   - [Page 1: Brand Wise Sales](#page-1-brand-wise-sales)
   - [Page 2: Store Wise Sales](#page-2-store-wise-sales)
4. [Filters and Navigation](#filters-and-navigation)
5. [Key Metrics](#key-metrics)
6. [Key Insights](#key-insights)
7. [Data Fields Used](#data-fields-used)
8. [Tools and Techniques](#tools-and-techniques)
9. [How to Use the Dashboard](#how-to-use-the-dashboard)
10. [Repository Structure](#repository-structure)
11. [Future Enhancements](#future-enhancements)

---

## Overview

The dashboard covers sales data for four fashion brands — **ONLY, JACK & JONES, SELECTED and VERO MODA** — across multiple stores and regions in India from **2017 to 2020**.

| Metric | Value |
|--------|-------|
| Total Sales | ₹1,378.57M |
| Total Net Margin | ₹865.62M |
| Total Units Sold | 912.78K |

It has two report pages, connected with navigation buttons:

- **Brand Wise Sales** – brand, category and sub-category performance.
- **Store Wise Sales** – store, region and monthly unit performance.

---

## Objectives

- Track overall sales, margin and units sold in one place.
- Compare performance of brands year over year.
- Identify top-selling and lowest-margin categories and sub-categories.
- Find the best performing stores and regions.
- Understand monthly and seasonal sales patterns to support planning and stock decisions.

---

## Dashboard Pages

### Page 1: Brand Wise Sales

![Brand Wise Sales](images/brand_wise_sales.png)

This page focuses on **brands, categories and sub-categories**.

#### 1. KPI Cards
Three cards at the top show overall totals for all brands:
- **Total Sales:** ₹1,378.57M
- **Total Margin:** ₹865.62M
- **Total Units Sold:** 912.78K

The cards update dynamically based on the selected filters.

#### 2. Brand Logos
Logos of **ONLY, JACK & JONES, SELECTED and VERO MODA** give a quick visual reference for the brands covered.

#### 3. Lowest Margin Sub-Categories (Bar Chart)
Shows the five sub-categories with the lowest total margin, with a color gradient (lighter = lower margin):

| Sub-Category | Approx. Margin |
|--------------|----------------|
| Eyewear | ~2M |
| Innerwear | ~5M |
| Skirt | ~6M |
| Jumpsuit | ~9M |
| Footwear | ~12M |

**Purpose:** Helps identify product areas where profitability is weak and pricing, discounting or assortment may need review.

#### 4. Distribution of Total Sales (Decomposition Tree)
Breaks down total sales (₹1,378.57M) step by step from **Category → Sub-Category**:

| Category | Sales |
|----------|-------|
| Tops | ₹974.04M |
| Bottoms | ₹334.70M |
| Accessories | ₹61.68M |

Drilling into **Tops** shows its top sub-categories:

| Sub-Category | Sales |
|--------------|-------|
| Tops | ₹199.11M |
| Shirts | ₹198.05M |
| T-Shirts | ₹180.11M |

**Purpose:** Lets users explore which categories and sub-categories contribute most to sales by expanding the tree interactively.

#### 5. Brand-wise Total Sales (Clustered Column Chart)
Compares yearly sales for each brand:

| Year | Jack & Jones | Only | Selected | Vero Moda |
|------|--------------|------|----------|-----------|
| 2017 | ₹3.98M | – | – | ₹2.04M |
| 2018 | ₹177.65M | ₹122.92M | ₹33.34M | ₹270.61M |
| 2019 | ₹210.14M | ₹136.42M | ₹31.1M | ₹325.7M |
| 2020 | ₹24.18M | – | – | ₹5.12M |

*Values for 2017 and 2020 are small, which suggests partial-year data for those years.*

**Purpose:** Shows how each brand grew year over year and which brand leads in sales.

#### 6. Top 5 Sub-Categories – Sales Over Months (Line Chart)
Tracks monthly sales (all years combined) for the top five sub-categories: **Dresses, Jeans, Shirts, Tops and T-Shirts**.

**Purpose:** Highlights seasonal patterns, such as low sales in February and strong peaks around June–July and December.

---

### Page 2: Store Wise Sales

![Store Wise Sales](images/store_wise_sales.png)

This page focuses on **stores, regions and monthly unit sales**.

#### 1. KPI Cards
- **Sum of Total Sales:** 1,378.57M
- **Sum of Net Margin:** 865.62M
- **Sum of Units Sold:** 912.78K

#### 2. Sum of Net Margin by Region (Donut Chart)
Shows each region's share of net margin:

| Region | Share of Net Margin |
|--------|--------------------|
| West | 31.78% |
| South | 29.95% |
| North | 24.85% |
| East | 13.43% |

**Purpose:** Shows that West and South contribute most of the margin, while East has the most room to grow.

#### 3. Top 5 Performing Stores by Rank Over Years (Line Chart)
Tracks the yearly rank of the top five stores from 2017 to 2020 (rank 1 = best):
- MB Bangalore Indiranagar
- MB Hyderabad Jubilee Hills
- MB Mumbai – Palladium Mall
- VM Delhi – Pacific Mall
- VM Kolkata – RPG Quest

**Purpose:** Shows how store rankings changed over time. Several stores moved from low ranks in 2017 to top positions in 2018–2019, and MB Bangalore Indiranagar reached rank 1 by 2020.

#### 4. Total Units Sold Over the Months (Area Chart)
Units sold per month (all years combined):

| Month | Units | Month | Units |
|-------|-------|-------|-------|
| Jan | 65K | Jul | 83K |
| Feb | 33K | Aug | 46K |
| Mar | 43K | Sep | 38K |
| Apr | 49K | Oct | 41K |
| May | 49K | Nov | 43K |
| Jun | 81K | Dec | 77K |

**Purpose:** Highlights peak months (June, July, December and January) and slow months (February and September), which is useful for stock and promotion planning.

#### 5. Top 10 Store-wise Total Sales (Column Chart)
Ranks the ten stores with the highest total sales, with a color gradient for sales value. **MB Mumbai – Palladium Mall** leads with **₹169.58M**, followed by MB Bangalore at **₹126.59M**. Other stores in the top 10 include MB Hyderabad, VM Delhi, VM Kolkata, MB Goa, ON Bangalore, ON Delhi, MB Gurgaon and MB – CG Road, ranging down to about **₹58.31M**.

**Purpose:** Identifies the highest revenue stores for benchmarking and resource planning.

---

## Filters and Navigation

### Slicers
Both pages include slicers so users can filter all visuals at once:

| Slicer | Page | Example Values |
|--------|------|----------------|
| Store Name | Both | MB – CG Road Ahmedabad, MB Bangalore Indiranagar, MB Goa – MG Road Panjim |
| Year | Both | 2017, 2018, 2019, 2020 |
| Month | Both | January to December |
| Season | Both | AW18, AW19, … |
| Sub-Category | Brand Wise Sales | Accessories, Dresses, Eyewear, Footwear, Innerwear, Jeans, Jumpsuit, … |
| Region | Store Wise Sales | East, North, South, West |

### Navigation Buttons
- **Brand Wise Sales** – opens the brand analysis page.
- **Store Wise Sales** – opens the store analysis page.
- **Reset Filter** – clears all selected slicers and returns the page to its default view.

---

## Key Metrics

| Metric | Description |
|--------|-------------|
| Total Sales | Sum of sales value across all transactions |
| Net Margin | Sum of margin earned (sales minus cost) |
| Units Sold | Total quantity of items sold |
| Store Rank | Yearly ranking of stores based on sales performance |
| Margin Share by Region | Percentage of total net margin contributed by each region |

---

## Key Insights

1. **Vero Moda is the top brand**, with the highest sales in both 2018 (₹270.61M) and 2019 (₹325.7M).
2. **All major brands grew from 2018 to 2019**, except Selected, which stayed roughly flat.
3. **Tops is the biggest category**, contributing ₹974.04M, about 70% of total sales.
4. **Eyewear, Innerwear and Skirts have the lowest margins**, so they may need pricing or assortment review.
5. **West and South regions** together contribute over 60% of net margin; **East** contributes the least (13.43%).
6. **MB Mumbai – Palladium Mall** is the highest-selling store at ₹169.58M.
7. **Sales are seasonal:** units peak in June–July (81K–83K) and December–January (77K and 65K), and drop in February (33K) and September (38K).

---

## Data Fields Used

| Field | Description |
|-------|-------------|
| Brand | Brand name (ONLY, JACK & JONES, SELECTED, VERO MODA) |
| Store_Name | Store name and location |
| Region | East, North, South, West |
| Category | Tops, Bottoms, Accessories |
| Sub_Category | Product sub-category (Shirts, Jeans, Dresses, etc.) |
| Season | Season code (AW18, AW19, …) |
| Year / Month | Time of sale |
| Total_Sales | Sales value |
| Net_Margin / Total_Margin | Margin value |
| Units_Sold | Quantity sold |

---

## Tools and Techniques

- **Power BI Desktop** – data modeling and report design
- **Power BI Service** – publishing and sharing
- **Power Query** – data cleaning and transformation
- **DAX** – measures for totals, margin and store ranking
- **Visuals used:** KPI cards, clustered column charts, bar chart, decomposition tree, line charts, donut chart, area chart and slicers
- **Bookmarks and buttons** – page navigation and filter reset
- **Conditional formatting** – color gradients to highlight high and low values

---

## How to Use the Dashboard

1. Open the dashboard using the live link above, or open the `.pbix` file in Power BI Desktop.
2. Use the **Brand Wise Sales** and **Store Wise Sales** buttons to switch pages.
3. Select values in the slicers (Store, Year, Month, Season, Sub-Category, Region) to filter the visuals.
4. Click on any bar, line point or donut segment to cross-filter other visuals on the page.
5. In the **Distribution of Total Sales** tree, click the **+** icons to drill down into categories and sub-categories.
6. Click **Reset Filter** to clear all selections.

---

## Repository Structure

```
sales-analysis-dashboard/
├── README.md
├── Sales_Analysis_Dashboard.pbix     # Power BI report file
├── data/                             # Source data (if shareable)
└── images/
    ├── brand_wise_sales.png          # Screenshot of page 1
    └── store_wise_sales.png          # Screenshot of page 2
```

---

## Future Enhancements

- Add year-over-year growth % and profit margin % measures.
- Add a Spring/Summer season comparison alongside Autumn/Winter.
- Add drill-through pages for individual store and brand details.
- Add sales targets vs actuals tracking.
- Schedule automatic data refresh in Power BI Service.

---

## Author

**Your Name**
📧 your.email@example.com
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile)
