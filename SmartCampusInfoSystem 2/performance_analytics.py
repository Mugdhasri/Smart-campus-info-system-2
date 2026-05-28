# -*- coding: utf-8 -*-
# ============================================================
# Lab 8: Student Performance Analysis
# Using NumPy, Pandas, and Matplotlib
# Smart Campus Information System
# ============================================================

import os

# ── Safe imports with user-friendly error messages ───────────
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    LIBS_AVAILABLE = True
except ImportError as e:
    LIBS_AVAILABLE = False
    IMPORT_ERROR = str(e)

CSV_FILE = "student_performance.csv"


def create_sample_csv():
    """Create a sample CSV file if it does not exist."""
    if not os.path.exists(CSV_FILE):
        data = (
            "Name,Math,Science,English\n"
            "Priya,88,92,85\n"
            "Rahul,72,78,80\n"
            "Anita,95,90,93\n"
            "Kiran,65,70,74\n"
            "Sneha,80,85,88\n"
        )
        with open(CSV_FILE, "w") as f:
            f.write(data)
        print(f"Sample CSV '{CSV_FILE}' created.")


def analyze_performance():
    """Run full performance analytics using NumPy, Pandas, Matplotlib."""
    if not LIBS_AVAILABLE:
        print(f"\n[Error] Required library not found: {IMPORT_ERROR}")
        print("Install via: pip install numpy pandas matplotlib")
        return

    print("\n" + "=" * 45)
    print("  STUDENT PERFORMANCE ANALYTICS (NumPy/Pandas)")
    print("=" * 45)

    try:
        create_sample_csv()
        df = pd.read_csv(CSV_FILE)

        # ── Raw Data ─────────────────────────────────────────
        print("\n--- Raw Data ---")
        print(df.to_string(index=False))

        # ── Statistical Summary via Pandas ───────────────────
        print("\n--- Statistical Summary (Pandas) ---")
        print(df.describe().round(2).to_string())

        # ── NumPy Analysis ───────────────────────────────────
        scores       = df[["Math", "Science", "English"]].to_numpy()
        mean_scores  = np.mean(scores,  axis=0)
        median_scores= np.median(scores,axis=0)
        std_scores   = np.std(scores,   axis=0)

        subjects = ["Math", "Science", "English"]
        print("\n--- NumPy Analysis ---")
        for i, subj in enumerate(subjects):
            print(f"  {subj:10s} | Mean: {mean_scores[i]:.2f} | "
                  f"Median: {median_scores[i]:.2f} | Std Dev: {std_scores[i]:.2f}")

        # ── Top Performers ───────────────────────────────────
        top_math    = df.loc[df["Math"].idxmax(),    "Name"]
        top_science = df.loc[df["Science"].idxmax(), "Name"]
        top_english = df.loc[df["English"].idxmax(), "Name"]

        print("\n--- Top Performers ---")
        print(f"  Math    : {top_math}")
        print(f"  Science : {top_science}")
        print(f"  English : {top_english}")

        # ── Visualizations ───────────────────────────────────
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle("Smart Campus – Student Performance Analytics", fontsize=14, fontweight="bold")

        # Chart 1: Average scores per subject
        colors = ["#4C72B0", "#55A868", "#C44E52"]
        axes[0].bar(subjects, mean_scores, color=colors, edgecolor="black")
        axes[0].set_title("Average Scores per Subject")
        axes[0].set_xlabel("Subject")
        axes[0].set_ylabel("Average Score")
        axes[0].set_ylim(0, 100)
        for i, v in enumerate(mean_scores):
            axes[0].text(i, v + 1, f"{v:.1f}", ha="center", fontweight="bold")

        # Chart 2: Student-wise performance
        x = range(len(df["Name"]))
        width = 0.25
        for i, (subj, color) in enumerate(zip(subjects, colors)):
            axes[1].bar([p + i * width for p in x], df[subj], width,
                        label=subj, color=color, edgecolor="black")
        axes[1].set_title("Student-wise Performance Comparison")
        axes[1].set_xlabel("Students")
        axes[1].set_ylabel("Scores")
        axes[1].set_xticks([p + width for p in x])
        axes[1].set_xticklabels(df["Name"])
        axes[1].legend()
        axes[1].set_ylim(0, 110)

        plt.tight_layout()
        chart_path = "performance_chart.png"
        plt.savefig(chart_path)
        print(f"\n[Charts saved as '{chart_path}']")
        plt.show()

    except FileNotFoundError:
        print(f"Error: '{CSV_FILE}' not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    analyze_performance()
