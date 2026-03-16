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

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


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

    # PDOK luchtfoto RGB WMS
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
    m.to_streamlit(height=700)
