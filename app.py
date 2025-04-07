import streamlit as st
import time
from PIL import Image

# Title
st.title("🌍🚀 Journey from Earth to Mars 🪐")

# Introduction
st.markdown("""
Welcome aboard! In this five-minute journey, we'll travel from Earth to Mars.
You'll experience each phase of the mission with visuals, narration, and cool space facts!
""")

# Phase 1: Launch from Earth
st.header("Phase 1: Launch from Earth")
image_earth = Image.open("images/earth_launch.jpg")
st.image(image_earth, caption="Liftoff from Earth")
st.audio("audio/narration_launch.mp3")
st.markdown("**Fact:** Rockets need to reach speeds over 28,000 km/h to escape Earth’s gravity.")
time.sleep(5)

# Phase 2: Leaving Earth's Orbit
st.header("Phase 2: Leaving Earth's Orbit")
image_orbit = Image.open("images/earth_orbit.jpg")
st.image(image_orbit, caption="Leaving Earth’s Orbit")
st.audio("audio/narration_orbit.mp3")
st.markdown("**Fact:** Satellites and spacecraft orbit Earth due to a perfect balance between gravity and forward motion.")
time.sleep(5)

# Phase 3: Cruising through Space
st.header("Phase 3: Cruising through Space")
image_space = Image.open("images/deep_space.jpg")
st.image(image_space, caption="Cruising Through Space")
st.audio("audio/narration_space.mp3")
st.markdown("**Fact:** The journey to Mars takes about 6-9 months depending on alignment and speed.")
time.sleep(5)

# Phase 4: Approaching Mars
st.header("Phase 4: Approaching Mars")
image_mars_approach = Image.open("images/mars_approach.jpg")
st.image(image_mars_approach, caption="Approaching the Red Planet")
st.audio("audio/narration_mars.mp3")
st.markdown("**Fact:** Mars is about half the size of Earth and has seasons like Earth due to its tilted axis.")
time.sleep(5)

# Phase 5: Mars Landing
st.header("Phase 5: Mars Landing")
image_mars_surface = Image.open("images/mars_surface.jpg")
st.image(image_mars_surface, caption="Touchdown on Mars")
st.audio("audio/narration_landing.mp3")
st.markdown("**Fact:** Mars rovers have discovered signs that water once flowed on the Martian surface.")
time.sleep(5)

# Wrap-up
st.success("Mission Accomplished! You've arrived on Mars!")
st.balloons()

st.markdown("""
**Thanks for traveling with us!**
Want to learn more about Mars missions? Check out [NASA's Mars Exploration Program](https://mars.nasa.gov/).
""")
