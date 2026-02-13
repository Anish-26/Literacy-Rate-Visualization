# India Literacy Rate Visualization (SDG-4)

An interactive mapping project visualizing Sustainable Development Goal 4 (Quality Education) literacy rates across Indian states using Python, Folium, and Altair.

## 🚀 Features

- **Interactive Choropleth Map**: Visualizes literacy rates using a curated color scale (Built with Folium).
- **Analytical Insight Panel**: Floating dashboard showing Top 5 and Bottom 5 states by literacy rate.
- **Dynamic Search Control**: Search for any Indian state and the map will automatically zoom and highlight it.
- **Click-to-Zoom**: Interactive boundary clicking for detailed state examination.
- **Embedded Bar Charts**: Click on any state to see its literacy rate progress in a popup bar chart (Built with Altair).
- **High-Performance Rendering**: Clean, responsive map exported as a standalone `index.html`.

## 📂 Project Structure

```text
minor/
├── DATA/
│   └── Clean/
│       └── clean_SDG4.csv        # Processed literacy rate data
├── GEOJASON/                         # Source geospatial files
├── MAP/
│   ├── maping.ipynb             # Main development notebook
│   └── index.html               # Generated interactive map
├── OUTPUT/
│   └── Map_data_restored.geojson # Harmonized mapping data
├── compare_states.py             # Data validation script
└── restore_map_data.py           # Geospatial data restoration script
```

## 🛠️ Tech Stack

- **Python 3.x**
- **Folium**: Core mapping engine.
- **Pandas**: Data manipulation.
- **GeoPandas**: Geospatial data handling.
- **Altair**: Interactive bar charts for popups.
- **Branca**: HTML/CSS injection in maps.

## 🏃 How to Run

1. **Install Dependencies**:
   ```bash
   pip install folium pandas geopandas altair branca
   ```

2. **Run the Notebook**:
   Open `MAP/maping.ipynb` in VS Code or Jupyter and execute the cells.

3. **View the Map**:
   Open `MAP/index.html` in any modern web browser.

## 📊 Data Source

The data is based on SDG-4 (Quality Education) indicators for India, focusing on state-wise literacy rates.

## ⚖️ License
This project is created for educational and analytical purposes.
