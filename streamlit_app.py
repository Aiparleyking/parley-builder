# streamlit_app.py

import streamlit as st
from main import main

st.set_page_config(page_title="Parlay Builder Machine", page_icon="⚾", layout="wide")

st.title("⚾ Daily Parlay Builder")

st.write("""
Welcome to your private MLB Parlay AI!
Click below to scrape today's games, cross-reference players, and build winning parlays.
""")

if st.button('Build Today\'s Parlays 🚀'):
    st.success("Running... Please wait 1–2 minutes for scrapes and calculations.")
    eligible_players, vip_players = main()

    if eligible_players:
        st.header("🎯 Today's Recommended Parlays")
        for player in eligible_players:
            st.write(f"- {player['name']} ({player['team']} vs {player['opponent']}) | Confidence: {player['confidence']} Stars")

    if vip_players:
        st.header("🔥 VIP Single Prop Picks")
        for vip in vip_players:
            st.write(f"🔥 {vip['name']} ({vip['team']} vs {vip['opponent']}) | Confidence: {vip['confidence']} Stars")

    if not eligible_players and not vip_players:
        st.warning("⚠️ No eligible picks found today. Try again later.")

    st.success("✅ Done! Picks have also been saved to your daily_picks/ folder.")

