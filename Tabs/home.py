"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Stress is an omnipresent facet of modern life, impacting individuals across all demographics and occupations. From the demands of work and education to personal relationships and societal pressures, the sources of stress are manifold and pervasive. Understanding stress requires delving into its multifaceted nature, encompassing physiological, psychological, and emotional dimensions. This introductory exploration aims to elucidate the complexities of stress, shedding light on its prevalence, effects, and management strategies. Defined as the body's response to perceived threats or challenges, stress triggers a cascade of physiological reactions designed to mobilize resources for coping. While short-term stress can be adaptive, enhancing performance and alertness, chronic exposure to stressors can exert profound detrimental effects on physical and mental health. From cardiovascular disorders and immune dysfunction to anxiety and depression, the toll of chronic stress on well-being is undeniable. In the following discourse, we will delve deeper into the intricacies of stress, examining its impact on various aspects of health and exploring evidence-based strategies for stress management and resilience-building. A user interface is provided allowing the user to control the data accessibility and visibility. SaYoPillow is novel, with security features as well as consideration of sleeping habits for stress reduction, with an accuracy of up to 96%.
        </p>
    """, unsafe_allow_html=True)
