import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Interactive map
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
# logo = "https://i.imgur.com/UbOXYAU.png"
# st.sidebar.image(logo)

st.title("Interactive Map")

# Basemap options
basemap_options = list(leafmap.basemaps.keys())
basemap_index = basemap_options.index("OpenTopoMap")

basemap = st.sidebar.selectbox("Select a basemap:", basemap_options, basemap_index)

# PDOK datasets
pdok_datasets = {
    "PDOK Luchtfoto RGB": {
        "url": "https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0?",
        "layers": "Actueel_orthoHR",
    },
    "Kadastralekaart": {
        "url": "https://service.pdok.nl/kadaster/kadastralekaart/wms/v5_0?",
        "layers": "perceel",
    },
    "Bestuurlijke Grenzen": {
        "url": "https://service.pdok.nl/kadaster/bestuurlijkegebieden/wms/v1_0?",
        "layers": "Gemeentegebied",
    },
}

selected_datasets = st.sidebar.multiselect(
    "Select PDOK datasets:",
    list(pdok_datasets.keys()),
    default=["PDOK Luchtfoto RGB"]
)

# Create map
m = leafmap.Map(
    center=[52.1326, 5.2913],
    zoom=7,
    locate_control=True,
    latlon_control=True,
    draw_export=True,
    minimap_control=True,
)

m.add_basemap(basemap)

for dataset in selected_datasets:
    config = pdok_datasets[dataset]

    m.add_wms_layer(
        url=config["url"],
        layers=config["layers"],
        name=dataset,
        attribution="PDOK",
        transparent=True,
        format="image/png",
    )

m.add_layer_control()

# Full width map
m.to_streamlit(height=700)
