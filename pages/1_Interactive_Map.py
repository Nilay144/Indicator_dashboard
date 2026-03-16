import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
Interactive map
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

# PDOK datasets
pdok_datasets = {
    "PDOK Luchtfoto RGB": {
        "url": "https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0?",
        "layers": "Actueel_orthoHR",
    },
    "PDOK BGT Achtergrondkaart": {
        "url": "https://service.pdok.nl/brt/achtergrondkaart/wmts/v2_0?",
        "layer": "standaard",
        "type": "wmts",
    },
    "PDOK Kadastrale Kaart": {
        "url": "https://service.pdok.nl/kadaster/kadastralekaart/wms/v5_0?",
        "layers": "perceel",
    },
    "PDOK Bestuurlijke Grenzen": {
        "url": "https://service.pdok.nl/kadaster/bestuurlijkegebieden/wms/v1_0?",
        "layers": "Gemeentegebied",
    },
}


with col2:

    basemap = st.selectbox("Select a basemap:", options, index)

    selected_dataset = st.multiselect("Select PDOK datasets:", 
                                      list(pdok_datasets.keys()),
                                      default=["PDOK Luchtfoto RGB"])
                                      
with col1:

    m = leafmap.Map(
        center=[52.1326, 5.2913],   # Netherlands
        zoom=7,
        locate_control=True,
        latlon_control=True,
        draw_export=True,
        minimap_control=True,
    )
    m.add_basemap(basemap)

    PDOK luchtfoto RGB WMS
    m.add_wms_layer(
        url="https://service.pdok.nl/hwh/luchtfotorgb/wms/v1_0?",
        layers="Actueel_orthoHR",
        name="PDOK Luchtfoto RGB",
        attribution="PDOK",
        transparent=True,
        format="image/png",
    )

    # Optional layer control
    m.add_layer_control()    
    m.to_streamlit(height=700, width=1400)
