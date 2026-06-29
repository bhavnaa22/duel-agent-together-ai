import streamlit as st
from helper import simulate_duel

st.set_page_config(page_title="Together AI Duel", page_icon="⚔️")
st.title("🤺 Duel Agent Simulator using Together AI")

agent1 = st.text_input("Enter Agent 1 persona", value="Philosopher")
agent2 = st.text_input("Enter Agent 2 persona", value="Comedian")
turns = st.slider("Number of turns", 1, 10, 5)

if st.button("Start Duel"):
    with st.spinner("Summoning agents via Together AI..."):
        duel_log = simulate_duel(agent1, agent2, turns)
        st.markdown(f"### 💬 {agent1} vs {agent2} — {turns} turns")
        st.text(duel_log)