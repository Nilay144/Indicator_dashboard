import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Interactive map
"""

st.sidebar.title("About")
st.sidebar.info(markdown)

logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Interactive Map")

basemap_options = list(leafmap.basemaps.keys())
basemap_index = basemap_options.index("OpenTopoMap")
basemap = st.sidebar.selectbox("Select a basemap:", basemap_options, basemap_index)

pdok_datasets = {
    "PDOK Luchtfoto RGB": {
        "url": "https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0?",
        "layers": "Actueel_orthoHR",
        "opacity": 1.0,
    },
    "Kadastralekaart": {
        "url": "https://service.pdok.nl/kadaster/kadastralekaart/wms/v5_0?",
        "layers": "perceel",
        "opacity": 0.8,
    },
    "Bestuurlijke Grenzen": {
        "url": "https://service.pdok.nl/kadaster/bestuurlijkegebieden/wms/v1_0?",
        "layers": "Gemeentegebied",
        "opacity": 0.7,
    },
}

selected_datasets = st.sidebar.multiselect(
    "Select PDOK datasets:",
    list(pdok_datasets.keys()),
    default=["PDOK Luchtfoto RGB", "Kadastralekaart", "Bestuurlijke Grenzen"]
)

m = leafmap.Map(
    center=[52.1326, 5.2913],
    zoom=8,
    locate_control=True,
    latlon_control=True,
    draw_export=True,
    minimap_control=True,
)

m.add_basemap(basemap)

# Add luchtfoto first as background
if "PDOK Luchtfoto RGB" in selected_datasets:
    cfg = pdok_datasets["PDOK Luchtfoto RGB"]
    m.add_wms_layer(
        url=cfg["url"],
        layers=cfg["layers"],
        name="PDOK Luchtfoto RGB",
        attribution="PDOK",
        transparent=True,
        format="image/png",
    )

# Add overlays after luchtfoto so they appear above it
for dataset in selected_datasets:
    if dataset == "PDOK Luchtfoto RGB":
        continue

    cfg = pdok_datasets[dataset]
    m.add_wms_layer(
        url=cfg["url"],
        layers=cfg["layers"],
        name=dataset,
        attribution="PDOK",
        transparent=True,
        format="image/png",
    )

m.add_layer_control()
m.to_streamlit(height=750)
