import streamlit as st
import secrets
import hashlib
import json
from datetime import datetime, timezone

st.set_page_config(
    page_title="Winly — Losowanie zwycięzców",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #f7f8fc;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.brand {
    font-size: 30px;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #5b4bdb;
}

.brand span {
    color: #252541;
}

.hero {
    background: linear-gradient(120deg, #5b4bdb, #8575f5);
    border-radius: 24px;
    padding: 36px;
    color: white;
    margin: 18px 0 28px 0;
    box-shadow: 0 12px 35px rgba(91, 75, 219, 0.18);
}

.hero h1 {
    color: white;
    font-size: 38px;
    line-height: 1.2;
    letter-spacing: -1.5px;
    margin: 0 0 12px 0;
}

.hero p {
    color: #eeebff;
    font-size: 16px;
    margin: 0;
}

.section-title {
    color: #252541;
    font-size: 21px;
    font-weight: 750;
    margin: 12px 0 5px 0;
}

.section-subtitle {
    color: #77788e;
    font-size: 14px;
    margin-bottom: 18px;
}

.panel {
    background: white;
    border: 1px solid #e9eaf3;
    border-radius: 18px;
    padding: 24px;
    margin-bottom: 18px;
}

.metric-card {
    background: white;
    border: 1px solid #e9eaf3;
    border-radius: 16px;
    padding: 20px;
    min-height: 105px;
}

.metric-label {
    color: #77788e;
    font-size: 13px;
    margin-bottom: 8px;
}

.metric-value {
    color: #252541;
    font-size: 27px;
    font-weight: 800;
}

.winner-card {
    background: linear-gradient(135deg, #ffffff, #f2efff);
    border: 1px solid #e5defe;
    border-radius: 18px;
    padding: 20px;
    margin: 10px 0;
    display: flex;
    align-items: center;
    gap: 16px;
}

.winner-number {
    background: #e8e2ff;
    color: #5b4bdb;
    border-radius: 12px;
    width: 46px;
    height: 46px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 800;
    font-size: 19px;
    flex-shrink: 0;
}

.winner-name {
    color: #252541;
    font-size: 18px;
    font-weight: 700;
    overflow-wrap: anywhere;
}

.winner-caption {
    color: #85859a;
    font-size: 12px;
    margin-top: 3px;
}

div.stButton > button {
    border-radius: 12px;
    min-height: 48px;
    font-weight: 700;
    transition: all 0.2s ease;
}

div.stButton > button[kind="primary"] {
    background: #5b4bdb;
    border: 1px solid #5b4bdb;
    color: white;
}

div.stButton > button[kind="primary"]:hover {
    background: #4938c6;
    border-color: #4938c6;
    transform: translateY(-1px);
}

div[data-testid="stTextArea"] textarea {
    border-radius: 12px;
    border-color: #dedfeb;
    background: #fcfcff;
    font-size: 14px;
}

div[data-testid="stNumberInput"] input {
    border-radius: 10px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

.footer {
    text-align: center;
    color: #9999ad;
    font-size: 12px;
    padding-top: 25px;
}

@media (max-width: 700px) {
    .hero {
        padding: 25px;
    }

    .hero h1 {
        font-size: 29px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# NAGLOWEK
st.markdown(
    '<div class="brand">winly<span>.</span></div>',
    unsafe_allow_html=True,
)

st.markdown("""
<div class="hero">
    <h1>Każdy konkurs<br>zasługuje na zwycięzcę.</h1>
    <p>Proste, szybkie i wygodne losowanie zwycięzców Twojego konkursu.</p>
</div>
""", unsafe_allow_html=True)

# FORMULARZ
left, right = st.columns([1.45, 1], gap="large")

with left:
    st.markdown(
        '<div class="section-title">📝 Uczestnicy konkursu</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="section-subtitle">Wklej listę — jedna osoba w każdym wierszu.</div>',
        unsafe_allow_html=True,
    )

    participants_text = st.text_area(
        "Lista uczestników",
        placeholder="anna123\nmarek456\nola789\nkasia123",
        height=260,
        label_visibility="collapsed",
    )

    remove_duplicates = st.checkbox(
        "Usuń powtarzające się wpisy",
        value=True,
    )

    participants = [
        line.strip()
        for line in participants_text.splitlines()
        if line.strip()
    ]

    if remove_duplicates:
        participants = list(dict.fromkeys(participants))

    st.caption("🔒 Lista nie jest zapisywana w bazie danych.")

with right:
    # st.markdown(
    #     '<div class="section-title">⚙️ Ustawienia losowania</div>',
    #     unsafe_allow_html=True,
    # )
    # st.markdown(
    #     '<div class="section-subtitle">Dostosuj losowanie do swojego konkursu.</div>',
    #     unsafe_allow_html=True,
    # )

    # st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("**Liczba uczestników**")
    st.markdown(
        f'<div style="font-size:32px;font-weight:800;color:#5b4bdb;'
        f'margin:4px 0 20px 0">{len(participants)}</div>',
        unsafe_allow_html=True,
    )

    if participants:
        winner_count = st.number_input(
            "Liczba zwycięzców",
            min_value=1,
            max_value=len(participants),
            value=1,
            step=1,
        )
    else:
        winner_count = 1
        st.number_input(
            "Liczba zwycięzców",
            min_value=1,
            value=1,
            disabled=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)

    draw_clicked = st.button(
        "🎲 Losuj zwycięzców",
        type="primary",
        use_container_width=True,
        disabled=len(participants) == 0,
    )

    if draw_clicked:
        winners = secrets.SystemRandom().sample(
            participants, int(winner_count)
        )

        canonical_list = json.dumps(
            participants,
            ensure_ascii=False,
            separators=(",", ":"),
        )

        st.session_state["winners"] = winners
        st.session_state["draw_time"] = (
            datetime.now(timezone.utc).isoformat()
        )
        st.session_state["list_hash"] = hashlib.sha256(
            canonical_list.encode("utf-8")
        ).hexdigest()
        st.session_state["input_hash"] = hashlib.sha256(
            participants_text.encode("utf-8")
        ).hexdigest()
        st.session_state["participant_count"] = len(participants)

# UNIEWAZNIENIE WYNIKU PO ZMIANIE LISTY
current_input_hash = hashlib.sha256(
    participants_text.encode("utf-8")
).hexdigest()

if (
    "input_hash" in st.session_state
    and st.session_state["input_hash"] != current_input_hash
):
    for key in (
        "winners",
        "draw_time",
        "list_hash",
        "input_hash",
        "participant_count",
    ):
        st.session_state.pop(key, None)

# STATYSTYKI
st.markdown("---")
st.markdown(
    '<div class="section-title">📊 Podsumowanie</div>',
    unsafe_allow_html=True,
)

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Uczestnicy</div>
        <div class="metric-value">{len(participants)}</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Zwycięzcy do wylosowania</div>
        <div class="metric-value">{int(winner_count)}</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    previous_count = len(st.session_state.get("winners", []))
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Ostatni wynik</div>
        <div class="metric-value">{previous_count}</div>
    </div>
    """, unsafe_allow_html=True)

# WYNIKI
if "winners" in st.session_state:
    st.markdown("---")
    st.markdown(
        '<div class="section-title">🏆 Gratulacje dla zwycięzców!</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="section-subtitle">Oto wynik Twojego losowania.</div>',
        unsafe_allow_html=True,
    )

    for number, winner in enumerate(
        st.session_state["winners"], start=1
    ):
        st.markdown(f"""
        <div class="winner-card">
            <div class="winner-number">{number}</div>
            <div>
                <div class="winner-name">{winner}</div>
                <div class="winner-caption">ZWYCIĘZCA KONKURSU</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.caption(
        f"Czas losowania (UTC): {st.session_state['draw_time']}"
    )

    report = {
        "winners": st.session_state["winners"],
        "draw_time_utc": st.session_state["draw_time"],
        "participant_count": st.session_state["participant_count"],
        "participant_list_sha256": st.session_state["list_hash"],
    }

    c1, c2 = st.columns(2)

    with c1:
        st.download_button(
            "📥 Pobierz raport JSON",
            data=json.dumps(
                report,
                ensure_ascii=False,
                indent=2,
            ),
            file_name="winly_wynik.json",
            mime="application/json",
            use_container_width=True,
        )

    with c2:
        if st.button("🗑️ Wyczyść wynik", use_container_width=True):
            for key in (
                "winners",
                "draw_time",
                "list_hash",
                "input_hash",
                "participant_count",
            ):
                st.session_state.pop(key, None)
            st.rerun()

else:
    st.markdown("""
    <div class="panel" style="text-align:center;padding:35px 20px;">
        <div style="font-size:42px;">🎁</div>
        <div style="font-size:18px;font-weight:750;color:#252541;margin:10px 0;">
            Czas wyłonić zwycięzców
        </div>
        <div style="color:#85859a;font-size:14px;">
            Wklej listę uczestników i kliknij przycisk losowania.
            Wyniki pojawią się tutaj.
        </div>
    </div>
    """, unsafe_allow_html=True)

# STOPKA
st.markdown("""
<div class="footer">
    WINLY · Proste losowanie konkursów · Wersja prototypowa
</div>
""", unsafe_allow_html=True)
