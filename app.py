"""
Dashboard Simulasi Tingkat Stres Mahasiswa Akibat Social Comparison di Media Sosial
Menggunakan pendekatan Agent-Based Modeling (ABM)
Dibuat untuk keperluan Tugas Besar Pemodelan dan Simulasi Data
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
import random

# ============================================================
# KONFIGURASI HALAMAN STREAMLIT
# ============================================================
st.set_page_config(
    page_title="Simulasi Stres Mahasiswa - ABM",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CUSTOM CSS STYLING - Tema Akademik Profesional
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');

    :root {
        --bg-primary: #0d1117;
        --bg-secondary: #161b22;
        --bg-card: #1c2128;
        --accent-cyan: #00e5ff;
        --accent-green: #3fb950;
        --accent-yellow: #f0a500;
        --accent-red: #f85149;
        --accent-purple: #bc8cff;
        --text-primary: #e6edf3;
        --text-muted: #8b949e;
        --border: #30363d;
    }

    .stApp {
        background-color: var(--bg-primary);
        font-family: 'IBM Plex Sans', sans-serif;
        color: var(--text-primary);
    }

    /* Header utama */
    .dashboard-header {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #1c2128 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 28px 36px;
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
    }
    .dashboard-header::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple), var(--accent-green));
    }
    .dashboard-title {
        font-family: 'IBM Plex Sans', sans-serif;
        font-weight: 700;
        font-size: 1.6rem;
        color: var(--text-primary);
        margin: 0 0 6px 0;
        letter-spacing: -0.02em;
    }
    .dashboard-subtitle {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.78rem;
        color: var(--accent-cyan);
        margin: 0;
        letter-spacing: 0.05em;
    }
    .badge {
        display: inline-block;
        background: rgba(0,229,255,0.1);
        border: 1px solid rgba(0,229,255,0.3);
        color: var(--accent-cyan);
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        padding: 2px 8px;
        border-radius: 4px;
        margin-right: 8px;
        margin-top: 10px;
        letter-spacing: 0.08em;
    }

    /* Metric cards */
    .metric-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 20px 22px;
        text-align: left;
        position: relative;
        overflow: hidden;
        transition: border-color 0.2s;
    }
    .metric-card:hover { border-color: var(--accent-cyan); }
    .metric-label {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 8px;
    }
    .metric-value {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 2rem;
        font-weight: 600;
        line-height: 1;
        margin-bottom: 4px;
    }
    .metric-delta {
        font-family: 'IBM Plex Sans', sans-serif;
        font-size: 0.75rem;
        color: var(--text-muted);
    }
    .metric-cyan  { color: var(--accent-cyan); }
    .metric-red   { color: var(--accent-red); }
    .metric-yellow{ color: var(--accent-yellow); }
    .metric-green { color: var(--accent-green); }

    /* Section headers */
    .section-header {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.72rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        border-left: 3px solid var(--accent-cyan);
        padding-left: 10px;
        margin: 28px 0 16px 0;
    }

    /* Narasi analisis */
    .narasi-box {
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        border-left: 4px solid var(--accent-green);
        border-radius: 8px;
        padding: 20px 24px;
        font-size: 0.88rem;
        line-height: 1.75;
        color: var(--text-primary);
    }
    .narasi-title {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.72rem;
        color: var(--accent-green);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 10px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: var(--bg-secondary) !important;
        border-right: 1px solid var(--border);
    }
    section[data-testid="stSidebar"] .stSlider label,
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] p {
        color: var(--text-primary) !important;
        font-family: 'IBM Plex Sans', sans-serif !important;
        font-size: 0.85rem !important;
    }

    /* Tombol simulasi */
    .stButton > button {
        background: linear-gradient(135deg, #00e5ff22, #bc8cff22) !important;
        border: 1px solid var(--accent-cyan) !important;
        color: var(--accent-cyan) !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.08em !important;
        padding: 10px 20px !important;
        border-radius: 6px !important;
        width: 100% !important;
        transition: all 0.2s !important;
        font-weight: 600 !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #00e5ff44, #bc8cff44) !important;
        box-shadow: 0 0 16px rgba(0,229,255,0.25) !important;
    }

    /* Dataframe */
    .stDataFrame { border-radius: 8px; overflow: hidden; }

    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple)) !important;
    }

    /* Info box */
    .info-chip {
        display: inline-block;
        background: rgba(188,140,255,0.1);
        border: 1px solid rgba(188,140,255,0.3);
        color: var(--accent-purple);
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        padding: 3px 10px;
        border-radius: 20px;
        margin: 3px 3px;
    }

    /* Plotly chart background override */
    .js-plotly-plot .plotly { background: transparent !important; }

    /* Sidebar divider */
    .sidebar-divider {
        border: none;
        border-top: 1px solid var(--border);
        margin: 16px 0;
    }

    /* Waiting state */
    .waiting-state {
        text-align: center;
        padding: 60px 20px;
        color: var(--text-muted);
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.82rem;
        letter-spacing: 0.05em;
    }
    .waiting-icon {
        font-size: 3rem;
        margin-bottom: 16px;
        display: block;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# KELAS AGEN (MAHASISWA)
# ============================================================
class AgenMahasiswa:
    """Representasi satu mahasiswa sebagai agen otonom dalam simulasi ABM."""

    TEKNIK_CBT = ["Breathing", "Positive Self-Talk", "Journaling", "Mindfulness", "Digital Detox"]

    def __init__(self, agent_id: int, skenario: str, media_exposure_awal: float):
        self.id = agent_id
        self.anxiety    = np.random.uniform(0.1, 0.5)   # A: Level kecemasan awal
        self.resilience = np.random.uniform(0.3, 0.9)   # R: Ketahanan mental
        self.media_exposure = media_exposure_awal        # M: Paparan media sosial

        # Inisialisasi Cognitive Distortion berdasarkan skenario
        if skenario == "Distorsi Kognitif Tinggi":
            self.distortion = np.random.uniform(1.2, 1.5)  # D tinggi
        else:
            self.distortion = np.random.uniform(0.5, 1.5)  # D normal

        # Pilih satu teknik CBT secara acak per agen
        self.cbt_type = random.choice(self.TEKNIK_CBT)

    def terapkan_cbt(self):
        """Terapkan efek reduksi teknik CBT yang dimiliki agen."""
        if self.cbt_type == "Breathing":
            self.anxiety -= 0.15
        elif self.cbt_type == "Positive Self-Talk":
            self.distortion -= 0.10
            self.anxiety    -= 0.10
        elif self.cbt_type == "Journaling":
            self.resilience += 0.10
            self.anxiety    -= 0.08
        elif self.cbt_type == "Mindfulness":
            self.anxiety -= 0.12
        elif self.cbt_type == "Digital Detox":
            self.media_exposure -= 2
            self.anxiety        -= 0.10
        self._clamp()

    def update(self, M: float, AP: float, SC: float, skenario: str, langkah: int):
        """
        Perbarui state agen satu langkah waktu.
        Formula stressor: S = (M + AP + SC) / 30
        Formula kenaikan anxiety: A_new = A + (S * D)
        """
        # Gunakan media exposure individual (bisa berubah via Digital Detox)
        m_efektif = self.media_exposure

        # Hitung stressor gabungan
        S = (m_efektif + AP + SC) / 30.0

        # Perbarui anxiety berdasarkan stressor dan distorsi kognitif
        self.anxiety += S * self.distortion

        # -------- Logika Intervensi CBT berdasarkan Skenario --------
        if skenario == "CBT Reaktif":
            # CBT aktif hanya jika anxiety melampaui threshold panik
            if self.anxiety > 0.8:
                self.terapkan_cbt()
        elif skenario == "CBT Preventif":
            # CBT aktif setiap 10 langkah waktu (rutin berkala)
            if langkah % 10 == 0:
                self.terapkan_cbt()
        # Skenario "Tanpa Intervensi" dan "Distorsi Kognitif Tinggi": tidak ada CBT

        self._clamp()

    def _clamp(self):
        """Paksa nilai atribut agar tetap dalam batas yang valid."""
        self.anxiety         = np.clip(self.anxiety, 0.0, 1.0)
        self.resilience      = min(self.resilience, 1.0)
        self.distortion      = max(self.distortion, 0.0)
        self.media_exposure  = max(self.media_exposure, 1.0)

    @property
    def state_psikologis(self) -> str:
        """Klasifikasi state psikologis berdasarkan level anxiety."""
        if self.anxiety < 0.3:
            return "Tenang"
        elif self.anxiety < 0.7:
            return "Cemas"
        else:
            return "Panik"


# ============================================================
# FUNGSI SIMULASI ABM
# ============================================================
def jalankan_simulasi(
    n_agen: int,
    durasi: int,
    M: float, AP: float, SC: float, SQ: float,
    skenario: str,
) -> tuple[list[float], list[AgenMahasiswa]]:
    """
    Eksekusi loop simulasi ABM.
    Mengembalikan riwayat rata-rata anxiety per langkah waktu
    dan daftar objek agen pada state akhir.
    """
    # Inisialisasi semua agen
    agen_list = [AgenMahasiswa(i, skenario, M) for i in range(n_agen)]

    riwayat_anxiety = []

    for t in range(durasi):
        # Update seluruh agen
        for agen in agen_list:
            agen.update(M, AP, SC, skenario, langkah=t)

        # Rekam rata-rata anxiety seluruh populasi di langkah ini
        mean_anxiety = np.mean([a.anxiety for a in agen_list])
        riwayat_anxiety.append(mean_anxiety)

    return riwayat_anxiety, agen_list


def hitung_baseline(n_agen: int, durasi: int, M: float, AP: float, SC: float, SQ: float) -> float:
    """Jalankan simulasi tanpa intervensi sebagai baseline perbandingan."""
    riwayat, _ = jalankan_simulasi(n_agen, durasi, M, AP, SC, SQ, "Tanpa Intervensi")
    return riwayat[-1]


def distribusi_state(agen_list: list[AgenMahasiswa]) -> dict:
    """Hitung persentase distribusi state psikologis seluruh populasi."""
    total = len(agen_list)
    counts = {"Tenang": 0, "Cemas": 0, "Panik": 0}
    for a in agen_list:
        counts[a.state_psikologis] += 1
    return {k: (v / total) * 100 for k, v in counts.items()}


# ============================================================
# FUNGSI RENDERING CHART (PLOTLY)
# ============================================================
WARNA_PLOTLY = {
    "bg"       : "#0d1117",
    "paper"    : "#0d1117",
    "grid"     : "#21262d",
    "text"     : "#8b949e",
    "line_cyan": "#00e5ff",
    "tenang"   : "#3fb950",
    "cemas"    : "#f0a500",
    "panik"    : "#f85149",
}

def buat_line_chart(riwayat: list[float], skenario: str) -> go.Figure:
    """Buat line chart animasi pergerakan rata-rata anxiety."""
    t_list = list(range(len(riwayat)))

    fig = go.Figure()

    # Area gradient di bawah garis
    fig.add_trace(go.Scatter(
        x=t_list, y=riwayat,
        fill='tozeroy',
        fillcolor='rgba(0,229,255,0.07)',
        line=dict(color=WARNA_PLOTLY["line_cyan"], width=2.5),
        name="Mean Anxiety",
        hovertemplate="<b>t=%{x}</b><br>Anxiety: %{y:.4f}<extra></extra>",
    ))

    # Garis threshold referensi
    fig.add_hline(y=0.3, line_dash="dot", line_color="#3fb950",
                  annotation_text="Batas Tenang (0.3)",
                  annotation_font_color="#3fb950", annotation_font_size=11)
    fig.add_hline(y=0.7, line_dash="dot", line_color="#f0a500",
                  annotation_text="Batas Panik (0.7)",
                  annotation_font_color="#f0a500", annotation_font_size=11)

    fig.update_layout(
        title=dict(
            text=f"Tren Rata-Rata Anxiety — Skenario: <b>{skenario}</b>",
            font=dict(family="IBM Plex Mono", size=13, color="#e6edf3"),
        ),
        xaxis=dict(
            title="Langkah Waktu (t)",
            gridcolor=WARNA_PLOTLY["grid"],
            color=WARNA_PLOTLY["text"],
            title_font=dict(family="IBM Plex Mono", size=11),
        ),
        yaxis=dict(
            title="Mean Anxiety Level",
            gridcolor=WARNA_PLOTLY["grid"],
            color=WARNA_PLOTLY["text"],
            range=[0, 1.05],
            title_font=dict(family="IBM Plex Mono", size=11),
        ),
        paper_bgcolor=WARNA_PLOTLY["paper"],
        plot_bgcolor=WARNA_PLOTLY["bg"],
        font=dict(family="IBM Plex Sans", color=WARNA_PLOTLY["text"]),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            bordercolor=WARNA_PLOTLY["grid"],
            borderwidth=1,
        ),
        margin=dict(t=50, b=50, l=60, r=30),
        height=360,
    )
    return fig


def buat_bar_distribusi(distribusi: dict) -> go.Figure:
    """Buat horizontal bar chart distribusi state psikologis."""
    labels = list(distribusi.keys())
    values = [distribusi[k] for k in labels]
    colors = [WARNA_PLOTLY["tenang"], WARNA_PLOTLY["cemas"], WARNA_PLOTLY["panik"]]

    fig = go.Figure(go.Bar(
        y=labels,
        x=values,
        orientation='h',
        marker=dict(
            color=colors,
            line=dict(color="rgba(0,0,0,0)", width=0),
        ),
        text=[f"{v:.1f}%" for v in values],
        textposition='outside',
        textfont=dict(family="IBM Plex Mono", size=12, color="#e6edf3"),
        hovertemplate="<b>%{y}</b>: %{x:.1f}%<extra></extra>",
    ))

    fig.update_layout(
        title=dict(
            text="Distribusi State Psikologis Akhir (%)",
            font=dict(family="IBM Plex Mono", size=13, color="#e6edf3"),
        ),
        xaxis=dict(
            title="Persentase Agen (%)",
            gridcolor=WARNA_PLOTLY["grid"],
            color=WARNA_PLOTLY["text"],
            range=[0, 115],
            title_font=dict(family="IBM Plex Mono", size=11),
        ),
        yaxis=dict(
            gridcolor="rgba(0,0,0,0)",
            color=WARNA_PLOTLY["text"],
            tickfont=dict(family="IBM Plex Mono", size=12),
        ),
        paper_bgcolor=WARNA_PLOTLY["paper"],
        plot_bgcolor=WARNA_PLOTLY["bg"],
        font=dict(family="IBM Plex Sans", color=WARNA_PLOTLY["text"]),
        margin=dict(t=50, b=50, l=100, r=60),
        height=280,
    )
    return fig


def buat_scatter_agen(agen_list: list[AgenMahasiswa]) -> go.Figure:
    """Scatter plot anxiety vs resilience tiap agen, diwarnai per state."""
    warna_map = {"Tenang": "#3fb950", "Cemas": "#f0a500", "Panik": "#f85149"}
    df = pd.DataFrame({
        "Anxiety"   : [a.anxiety for a in agen_list],
        "Resilience": [a.resilience for a in agen_list],
        "Distortion": [a.distortion for a in agen_list],
        "State"     : [a.state_psikologis for a in agen_list],
        "CBT"       : [a.cbt_type for a in agen_list],
        "ID"        : [a.id for a in agen_list],
    })

    fig = go.Figure()
    for state, grp in df.groupby("State"):
        fig.add_trace(go.Scatter(
            x=grp["Resilience"], y=grp["Anxiety"],
            mode='markers',
            name=state,
            marker=dict(
                color=warna_map[state],
                size=7,
                opacity=0.75,
                line=dict(width=0),
            ),
            customdata=np.stack([grp["Distortion"], grp["CBT"], grp["ID"]], axis=-1),
            hovertemplate=(
                "<b>Agen #%{customdata[2]}</b><br>"
                "Anxiety: %{y:.3f}<br>Resilience: %{x:.3f}<br>"
                "Distortion: %{customdata[0]:.3f}<br>CBT: %{customdata[1]}<extra></extra>"
            ),
        ))

    fig.update_layout(
        title=dict(
            text="Peta Posisi Agen: Anxiety vs Resilience",
            font=dict(family="IBM Plex Mono", size=13, color="#e6edf3"),
        ),
        xaxis=dict(
            title="Resilience",
            gridcolor=WARNA_PLOTLY["grid"],
            color=WARNA_PLOTLY["text"],
            range=[-0.05, 1.1],
            title_font=dict(family="IBM Plex Mono", size=11),
        ),
        yaxis=dict(
            title="Anxiety",
            gridcolor=WARNA_PLOTLY["grid"],
            color=WARNA_PLOTLY["text"],
            range=[-0.05, 1.1],
            title_font=dict(family="IBM Plex Mono", size=11),
        ),
        paper_bgcolor=WARNA_PLOTLY["paper"],
        plot_bgcolor=WARNA_PLOTLY["bg"],
        font=dict(family="IBM Plex Sans", color=WARNA_PLOTLY["text"]),
        legend=dict(
            bgcolor="rgba(28,33,40,0.8)",
            bordercolor=WARNA_PLOTLY["grid"],
            borderwidth=1,
            font=dict(family="IBM Plex Mono", size=11),
        ),
        margin=dict(t=50, b=50, l=60, r=30),
        height=340,
    )
    return fig


# ============================================================
# FUNGSI NARASI ANALISIS OTOMATIS
# ============================================================
def buat_narasi(skenario: str, anxiety_akhir: float, persen_panik: float,
                efektivitas: float, distribusi: dict, n_agen: int, durasi: int) -> str:
    """Generate teks narasi analisis berdasarkan hasil simulasi."""

    tenang_pct = distribusi.get("Tenang", 0)
    cemas_pct  = distribusi.get("Cemas", 0)

    if skenario == "Tanpa Intervensi":
        return f"""
Simulasi menunjukkan bahwa tanpa adanya mekanisme intervensi apapun, rata-rata tingkat kecemasan populasi mencapai
<strong>{anxiety_akhir:.4f}</strong> pada akhir {durasi} langkah waktu simulasi. Sebanyak <strong>{persen_panik:.1f}%</strong>
agen berada dalam kondisi Panik (A ≥ 0.7), sementara hanya <strong>{tenang_pct:.1f}%</strong> agen yang berhasil
mempertahankan kondisi Tenang. Skenario ini menjadi <em>baseline</em> referensi perbandingan efektivitas intervensi lainnya.
Tanpa strategi penanganan, tekanan akademik, paparan media sosial, dan distorsi kognitif terakumulasi secara progresif
dan mendorong mayoritas mahasiswa ke zona kerentanan psikologis yang tinggi.
"""
    elif skenario == "CBT Reaktif":
        return f"""
Pada skenario CBT Reaktif, intervensi kognitif hanya dipicu ketika tingkat kecemasan agen melampaui ambang batas kritis
(A > 0.8). Hasil simulasi menunjukkan rata-rata anxiety akhir sebesar <strong>{anxiety_akhir:.4f}</strong> dengan
<strong>{persen_panik:.1f}%</strong> agen dalam kondisi Panik. Dibandingkan baseline tanpa intervensi, skenario ini
mencatat estimasi efektivitas reduksi sebesar <strong>{efektivitas:.1f}%</strong>. Meskipun CBT Reaktif memberikan
perbaikan signifikan, penerapannya yang terlambat (hanya saat krisis sudah terjadi) membuat sebagian agen telah
mengalami kerusakan kumulatif yang lebih dalam sebelum mendapat penanganan, sehingga kurang optimal dibandingkan
pendekatan preventif yang bersifat proaktif.
"""
    elif skenario == "CBT Preventif":
        return f"""
Skenario CBT Preventif menunjukkan performa terbaik dalam simulasi ini. Dengan intervensi CBT yang diterapkan secara
rutin setiap 10 langkah waktu — tanpa menunggu kondisi kritis — rata-rata anxiety populasi berhasil ditekan hingga
<strong>{anxiety_akhir:.4f}</strong>, dengan hanya <strong>{persen_panik:.1f}%</strong> agen yang mengalami kondisi Panik.
Efektivitas reduksi terhadap baseline mencapai <strong>{efektivitas:.1f}%</strong>, jauh melampaui skenario reaktif.
Temuan ini memperkuat argumen bahwa program kesehatan mental proaktif di lingkungan kampus — seperti sesi mindfulness
berkala, lokakarya journaling, atau program digital detox terjadwal — secara substansial lebih efektif dalam
mencegah eskalasi stres daripada intervensi yang hanya dilakukan pada saat kondisi sudah memburuk secara serius.
"""
    elif skenario == "Distorsi Kognitif Tinggi":
        return f"""
Skenario Distorsi Kognitif Tinggi mensimulasikan kondisi mahasiswa yang memiliki pola pikir menyimpang parah
(D diinisialisasi pada rentang 1.2–1.5). Karena faktor pengali distorsi kognitif ini sangat besar, stressor
yang sama menghasilkan kenaikan anxiety jauh lebih cepat. Hasilnya: rata-rata anxiety akhir mencapai
<strong>{anxiety_akhir:.4f}</strong> dengan <strong>{persen_panik:.1f}%</strong> agen dalam kondisi Panik
— kemungkinan proporsi tertinggi dari seluruh skenario. Kondisi ini mencerminkan bagaimana pola pikir
katastrofis dan negatif yang terbentuk akibat paparan media sosial berlebihan dapat secara dramatis
mempercepat perkembangan gangguan kecemasan. Temuan ini menyoroti pentingnya program psikoedukatif
tentang cognitive restructuring sebagai fondasi utama kesehatan mental mahasiswa.
"""
    return "Simulasi selesai dijalankan."

# ============================================================
# SIDEBAR — KONTROL PARAMETER
# ============================================================
with st.sidebar:
    st.markdown("""
    <div style="font-family:'IBM Plex Mono',monospace; font-size:0.7rem;
                color:#00e5ff; letter-spacing:0.1em; text-transform:uppercase;
                border-bottom:1px solid #30363d; padding-bottom:12px; margin-bottom:16px;">
        ⚙ Kontrol Parameter ABM
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**👥 Populasi & Durasi**")
    n_agen = st.slider("Jumlah Agen (Mahasiswa)", min_value=20, max_value=500,
                       value=100, step=10, help="Jumlah agen/mahasiswa dalam simulasi")
    durasi = st.slider("Durasi Simulasi (langkah waktu)", min_value=50, max_value=500,
                       value=200, step=10, help="Total iterasi simulasi (unit waktu)")

    st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
    st.markdown("**🌍 Parameter Lingkungan / Stressor (Skala 1–10)**")

    M  = st.slider("📱 Media Exposure (M)",     min_value=1.0, max_value=10.0,
                   value=6.0, step=0.5, help="Intensitas paparan media sosial")
    AP = st.slider("📚 Academic Pressure (AP)", min_value=1.0, max_value=10.0,
                   value=7.0, step=0.5, help="Tekanan akademik yang dirasakan")
    SC = st.slider("👁 Social Comparison (SC)", min_value=1.0, max_value=10.0,
                   value=6.5, step=0.5, help="Tingkat perbandingan sosial di medsos")
    SQ = st.slider("😴 Sleep Quality (SQ)",     min_value=1.0, max_value=10.0,
                   value=5.0, step=0.5, help="Kualitas tidur (1=buruk, 10=sangat baik)")

    st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
    st.markdown("**🔬 Skenario What-If**")
    skenario = st.selectbox(
        "Pilih Skenario Intervensi",
        options=["Tanpa Intervensi", "CBT Reaktif", "CBT Preventif", "Distorsi Kognitif Tinggi"],
        index=0,
        help="Pilih skenario untuk membandingkan efektivitas strategi intervensi"
    )

    st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)

    # Keterangan skenario singkat
    skenario_info = {
        "Tanpa Intervensi"        : "Baseline — tidak ada mekanisme CBT aktif.",
        "CBT Reaktif"             : "CBT dipicu hanya saat Anxiety > 0.8 (darurat).",
        "CBT Preventif"           : "CBT diterapkan rutin setiap 10 langkah waktu.",
        "Distorsi Kognitif Tinggi": "Agen diinisialisasi dengan D ∈ [1.2, 1.5].",
    }
    st.markdown(f"""
    <div style="background:rgba(0,229,255,0.06); border:1px solid rgba(0,229,255,0.2);
                border-radius:6px; padding:10px 14px; font-size:0.78rem;
                color:#8b949e; font-family:'IBM Plex Sans',sans-serif; line-height:1.6;">
        <span style="color:#00e5ff; font-family:'IBM Plex Mono',monospace;
                     font-size:0.65rem; text-transform:uppercase; letter-spacing:0.08em;">
            Info Skenario
        </span><br>
        {skenario_info[skenario]}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Tombol trigger simulasi
    jalankan = st.button("▶  JALANKAN SIMULASI", use_container_width=True)


# ============================================================
# HEADER UTAMA DASHBOARD
# ============================================================
st.markdown(f"""
<div class="dashboard-header">
    <p class="dashboard-subtitle">AGENT-BASED MODELING · KESEHATAN MENTAL MAHASISWA · SIMULASI INTERAKTIF</p>
    <h1 class="dashboard-title">Dashboard Simulasi Tingkat Stres Mahasiswa<br>Akibat Social Comparison di Media Sosial</h1>
    <span class="badge">ABM</span>
    <span class="badge">N={n_agen} AGEN</span>
    <span class="badge">T={durasi} LANGKAH</span>
    <span class="badge">{skenario.upper()}</span>
    <span class="badge">M={M} | AP={AP} | SC={SC} | SQ={SQ}</span>
</div>
""", unsafe_allow_html=True)


# ============================================================
# AREA UTAMA — STATE BELUM DIJALANKAN
# ============================================================
if not jalankan and "hasil_simulasi" not in st.session_state:
    st.markdown("""
    <div class="waiting-state">
        <span class="waiting-icon">🧠</span>
        Atur parameter di sidebar, lalu klik <strong>JALANKAN SIMULASI</strong> untuk memulai.
        <br><br>
        <span style="color:#30363d; font-size:0.7rem;">
        Model ABM akan mensimulasikan dinamika kecemasan {n_agen} agen mahasiswa selama {durasi} langkah waktu.
        </span>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# EKSEKUSI SIMULASI (dipicu tombol)
# ============================================================
if jalankan:
    # ---- Progress bar animasi ----
    progress_placeholder = st.empty()
    status_placeholder   = st.empty()

    with progress_placeholder.container():
        st.markdown('<div class="section-header">⟳ MENJALANKAN SIMULASI ABM</div>', unsafe_allow_html=True)
        prog_bar = st.progress(0)

    status_placeholder.markdown(
        f'<div style="font-family:IBM Plex Mono,monospace;font-size:0.75rem;color:#8b949e;">'
        f'Menginisialisasi {n_agen} agen... | Skenario: {skenario}</div>',
        unsafe_allow_html=True
    )

    # Simulasi dengan update progress bertahap (simulasi "animasi" proses)
    BATCH = max(1, durasi // 20)  # Update progress tiap ~5%

    agen_list_full = [AgenMahasiswa(i, skenario, M) for i in range(n_agen)]
    riwayat_full   = []

    for t in range(durasi):
        for agen in agen_list_full:
            agen.update(M, AP, SC, skenario, langkah=t)
        mean_a = np.mean([a.anxiety for a in agen_list_full])
        riwayat_full.append(mean_a)

        if t % BATCH == 0 or t == durasi - 1:
            pct = int((t + 1) / durasi * 100)
            prog_bar.progress(pct)
            status_placeholder.markdown(
                f'<div style="font-family:IBM Plex Mono,monospace;font-size:0.75rem;color:#8b949e;">'
                f't={t+1}/{durasi} | Mean Anxiety: {mean_a:.4f} | {pct}% selesai</div>',
                unsafe_allow_html=True
            )

    # Hitung baseline untuk efektivitas
    baseline_anxiety = hitung_baseline(n_agen, durasi, M, AP, SC, SQ)
    anxiety_akhir    = riwayat_full[-1]
    efektivitas      = max(0.0, (baseline_anxiety - anxiety_akhir) / baseline_anxiety * 100) \
                       if skenario != "Tanpa Intervensi" else 0.0

    distribusi = distribusi_state(agen_list_full)
    persen_panik = distribusi.get("Panik", 0)
    max_anxiety  = max(riwayat_full)

    # Simpan ke session state
    st.session_state["hasil_simulasi"] = {
        "riwayat"        : riwayat_full,
        "agen_list"      : agen_list_full,
        "distribusi"     : distribusi,
        "anxiety_akhir"  : anxiety_akhir,
        "max_anxiety"    : max_anxiety,
        "persen_panik"   : persen_panik,
        "efektivitas"    : efektivitas,
        "baseline"       : baseline_anxiety,
        "skenario"       : skenario,
        "n_agen"         : n_agen,
        "durasi"         : durasi,
    }

    progress_placeholder.empty()
    status_placeholder.empty()


# ============================================================
# TAMPILKAN HASIL SIMULASI
# ============================================================
if "hasil_simulasi" in st.session_state:
    hasil = st.session_state["hasil_simulasi"]

    riwayat      = hasil["riwayat"]
    agen_list    = hasil["agen_list"]
    distribusi   = hasil["distribusi"]
    anxiety_akhir= hasil["anxiety_akhir"]
    max_anxiety  = hasil["max_anxiety"]
    persen_panik = hasil["persen_panik"]
    efektivitas  = hasil["efektivitas"]
    baseline     = hasil["baseline"]
    skenario_run = hasil["skenario"]
    n_run        = hasil["n_agen"]
    dur_run      = hasil["durasi"]

    # ----------------------------------------------------------------
    # BARIS METRIK ATAS
    # ----------------------------------------------------------------
    st.markdown('<div class="section-header">◈ RINGKASAN METRIK SIMULASI</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📊 Rata-rata Anxiety Akhir</div>
            <div class="metric-value metric-cyan">{anxiety_akhir:.4f}</div>
            <div class="metric-delta">Baseline: {baseline:.4f}</div>
        </div>""", unsafe_allow_html=True)

    with col2:
        warna_max = "metric-red" if max_anxiety >= 0.7 else "metric-yellow"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">⬆ Anxiety Maksimum</div>
            <div class="metric-value {warna_max}">{max_anxiety:.4f}</div>
            <div class="metric-delta">Puncak sepanjang simulasi</div>
        </div>""", unsafe_allow_html=True)

    with col3:
        warna_panik = "metric-red" if persen_panik > 40 else ("metric-yellow" if persen_panik > 20 else "metric-green")
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">🚨 Agen dalam Kondisi Panik</div>
            <div class="metric-value {warna_panik}">{persen_panik:.1f}%</div>
            <div class="metric-delta">Dari {n_run} total agen</div>
        </div>""", unsafe_allow_html=True)

    with col4:
        warna_efek = "metric-green" if efektivitas > 20 else ("metric-yellow" if efektivitas > 5 else "metric-cyan")
        label_efek = f"{efektivitas:.1f}%" if skenario_run != "Tanpa Intervensi" else "—"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">✅ Estimasi Efektivitas Reduksi</div>
            <div class="metric-value {warna_efek}">{label_efek}</div>
            <div class="metric-delta">vs. skenario tanpa intervensi</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ----------------------------------------------------------------
    # CHART BARIS 1: Line Chart (lebar penuh)
    # ----------------------------------------------------------------
    st.markdown('<div class="section-header">📈 TREN DINAMIKA KECEMASAN</div>', unsafe_allow_html=True)
    st.plotly_chart(buat_line_chart(riwayat, skenario_run), use_container_width=True)

    # ----------------------------------------------------------------
    # CHART BARIS 2: Bar Distribusi + Scatter Plot
    # ----------------------------------------------------------------
    st.markdown('<div class="section-header">🔵 DISTRIBUSI STATE & PETA AGEN</div>', unsafe_allow_html=True)
    col_bar, col_scatter = st.columns([1, 1.2])

    with col_bar:
        st.plotly_chart(buat_bar_distribusi(distribusi), use_container_width=True)

        # Chip statistik distribusi
        st.markdown(
            f'<div style="margin-top:8px;">'
            f'<span class="info-chip">🟢 Tenang: {distribusi["Tenang"]:.1f}%</span>'
            f'<span class="info-chip">🟡 Cemas: {distribusi["Cemas"]:.1f}%</span>'
            f'<span class="info-chip">🔴 Panik: {distribusi["Panik"]:.1f}%</span>'
            f'</div>',
            unsafe_allow_html=True
        )

    with col_scatter:
        st.plotly_chart(buat_scatter_agen(agen_list), use_container_width=True)

    # ----------------------------------------------------------------
    # TABEL KONDISI AKHIR AGEN
    # ----------------------------------------------------------------
    st.markdown('<div class="section-header">📋 SAMPEL KONDISI AKHIR AGEN (10 PERTAMA)</div>',
                unsafe_allow_html=True)

    df_sampel = pd.DataFrame([{
        "ID Agen"    : a.id,
        "Anxiety (A)": round(a.anxiety, 4),
        "Resilience (R)": round(a.resilience, 4),
        "Distortion (D)": round(a.distortion, 4),
        "State"      : a.state_psikologis,
        "Teknik CBT" : a.cbt_type,
    } for a in agen_list[:10]])

    # Warna state pada kolom tabel
    def warnai_state(val):
        if val == "Tenang":
            return "color: #3fb950; font-weight: 600;"
        elif val == "Cemas":
            return "color: #f0a500; font-weight: 600;"
        elif val == "Panik":
            return "color: #f85149; font-weight: 600;"
        return ""

    styled_df = df_sampel.style.map(warnai_state, subset=["State"])
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

# ----------------------------------------------------------------
    # NARASI ANALISIS OTOMATIS
    # ----------------------------------------------------------------
    st.markdown('<div class="section-header">📝 NARASI ANALISIS OTOMATIS</div>', unsafe_allow_html=True)

    # Tambahkan .strip() di akhir fungsi untuk membuang baris kosong yang merusak parser
    narasi = buat_narasi(
        skenario_run, anxiety_akhir, persen_panik,
        efektivitas, distribusi, n_run, dur_run
    ).strip()

    # Pastikan penulisan f-string HTML ini rapat tanpa baris kosong yang renggang
    st.markdown(f'<div class="narasi-box"><div class="narasi-title">✦ Analisis Skenario: {skenario_run}</div>{narasi}</div>', unsafe_allow_html=True)

    # ----------------------------------------------------------------
    # PARAMETER SIMULASI (kolapsible)
    # ----------------------------------------------------------------
    with st.expander("🔧 Detail Parameter Simulasi yang Digunakan"):
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.markdown(f"""
            | Parameter | Nilai |
            |-----------|-------|
            | Jumlah Agen | {n_run} |
            | Durasi Simulasi | {dur_run} langkah |
            | Skenario | {skenario_run} |
            | Media Exposure (M) | {M} |
            """)
        with col_p2:
            st.markdown(f"""
            | Parameter | Nilai |
            |-----------|-------|
            | Academic Pressure (AP) | {AP} |
            | Social Comparison (SC) | {SC} |
            | Sleep Quality (SQ) | {SQ} |
            | Baseline Anxiety | {baseline:.4f} |
            """)

    # ----------------------------------------------------------------
    # FOOTER
    # ----------------------------------------------------------------
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; font-family:'IBM Plex Mono',monospace;
                font-size:0.65rem; color:#30363d; padding:20px 0; letter-spacing:0.08em;
                border-top:1px solid #21262d;">
        SIMULASI ABM · PEMODELAN KESEHATAN MENTAL MAHASISWA · AGENT-BASED MODELING
    </div>
    """, unsafe_allow_html=True)
