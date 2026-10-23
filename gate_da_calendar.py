
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
from pathlib import Path
import textwrap

output_dir = Path(__file__).parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "gate_da_30_day_plan.png"

start_date = datetime(2027, 1, 1)

# Daily study topics
topics = {
    1: "Counting, Permutations, Probability Axioms",
    2: "Counting, Permutations, Probability Axioms",
    3: "Independence, Conditional Probability, Bayes",
    4: "Independence, Conditional Probability, Bayes",
    5: "Expectation, Variance, Correlation",
    6: "Expectation, Variance, Correlation",
    7: "Practice + Revision (Week 1)",
    8: "Discrete RVs: Bernoulli, Binomial, Poisson",
    9: "Discrete RVs: Bernoulli, Binomial, Poisson",
    10: "Continuous RVs: Uniform, Normal, Exponential",
    11: "Continuous RVs: Uniform, Normal, Exponential",
    12: "t, Chi-squared, CDFs",
    13: "CLT, Confidence Intervals",
    14: "Hypothesis Testing + Practice",
    15: "Vector Spaces, Matrices",
    16: "Vector Spaces, Matrices",
    17: "Linear Systems, Gaussian Elimination",
    18: "Eigenvalues, LU Decomposition",
    19: "SVD, Quadratic Forms",
    20: "Calculus: Limits, Taylor, Maxima/Minima",
    21: "Python, Stacks, Queues, Linked Lists",
    22: "Trees, Hash Tables, Sorting",
    23: "Divide & Conquer, Graph Basics",
    24: "Graph Algorithms: Traversals, Shortest Path",
    25: "Databases: ER, SQL, Normalization",
    26: "Data Warehousing, Schema, Measures",
    27: "ML: Regression, k-NN, Naive Bayes",
    28: "ML: LDA, SVM, Trees, CV",
    29: "ML: Clustering, PCA",
    30: "AI: Search, Logic, Reasoning",
}

dates = [
    start_date + timedelta(days=i)
    for i in range(30)
]


# Layout settings
fig = plt.figure(figsize=(18, 13), facecolor="#F7F9FC")

fig.text(
    0.5, 0.965,
    "GATE DA 2027 — 30-Day Study Plan",
    ha="center", va="top",
    fontsize=24, fontweight="bold", color="#0F172A"
)
fig.text(
    0.5, 0.928,
    "Daily topics • January 1 – February 1, 2027",
    ha="center", va="top",
    fontsize=12, color="#64748B"
)

left, right = 0.045, 0.955
bottom, top = 0.055, 0.885
cols, rows = 5, 6
gap_x, gap_y = 0.009, 0.014

card_w = (right - left - (cols - 1) * gap_x) / cols
card_h = (top - bottom - (rows - 1) * gap_y) / rows

for i in range(30):
    day = i + 1
    row, col = divmod(i, cols)

    x = left + col * (card_w + gap_x)
    y = top - (row + 1) * card_h - row * gap_y

    # Independent axes prevent text from crossing card boundaries
    card_ax = fig.add_axes([x, y, card_w, card_h])
    card_ax.set_xlim(0, 1)
    card_ax.set_ylim(0, 1)
    card_ax.axis("off")

    face = "#FFFFFF" if row % 2 == 0 else "#F0F6FF"

    card = mpatches.FancyBboxPatch(
        (0.01, 0.01), 0.98, 0.98,
        boxstyle="round,pad=0.008,rounding_size=0.035",
        linewidth=1.1,
        edgecolor="#CBD5E1",
        facecolor=face
    )
    card_ax.add_patch(card)

    date = start_date + timedelta(days=i)

    card_ax.text(
        0.06, 0.83, f"DAY {day:02d}",
        fontsize=12, fontweight="bold",
        color="#1D4ED8", va="center"
    )

    card_ax.text(
        0.06, 0.65, date.strftime("%a, %b %d"),
        fontsize=9.5, color="#64748B",
        va="center", style="italic"
    )

    card_ax.plot(
        [0.06, 0.94], [0.53, 0.53],
        color="#DBE4F0", linewidth=0.9
    )

    topic = textwrap.fill(
        topics[day], width=27,
        break_long_words=False
    )

    card_ax.text(
        0.06, 0.43, topic,
        fontsize=9.1, color="#1F2937",
        va="top", ha="left",
        linespacing=1.3,
        clip_on=True
    )

fig.savefig(
    output_path,
    dpi=300,
    facecolor=fig.get_facecolor(),
    bbox_inches="tight",
    pad_inches=0.2
)

plt.show()
plt.close(fig)