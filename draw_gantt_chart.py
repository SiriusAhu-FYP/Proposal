from datetime import datetime, timedelta

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# Task data (unchanged)
tasks = [
    ["Project Setup & Research Finalization", 1, 1, "A - Setup"],
    ["Core Architecture Design (Orchestrator & MCP API)", 1, 2, "A - Setup"],
    ["Relational Core (v1 Stub & Live2D Setup)", 3, 4, "D - Relational Core"],
    ["Voice Loop Module (STT/TTS)", 3, 4, "D - Relational Core"],
    ["[LONG] Orchestrator & MCP Bus (v1 -> v3 Integration)", 2, 15, "B - Core System"],
    ["[LONG] Functional Core (v1 Train -> v2 Transfer)", 8, 15, "C - Functional Core"],
    ["Perception Module (v1 for Phase 1 Games)", 6, 7, "C - Functional Core"],
    ["GCC I/O Module (Keyboard/Mouse Control)", 6, 7, "C - Functional Core"],
    ["Safety Core (BacktrackAgent-style Verifier)", 11, 12, "B - Core System"],
    ["Phase 1: Functional Evaluation (Run Tests)", 13, 13, "E - Evaluation"],
    ["Perception Module (v2 for Phase 2 Game)", 13, 14, "C - Functional Core"],
    [
        "Relational Core (v2 Proactive & Full Integration)",
        14,
        15,
        "D - Relational Core",
    ],
    ["Phase 2: A/B User Study (Recruit & Run Tests)", 16, 17, "E - Evaluation"],
    ["Final Code Cleanup & Bug Fixing", 16, 18, "F - Finalization"],
    ["Final Documentation (Code & System)", 16, 20, "F - Finalization"],
    ["Final Demo Video Prep", 18, 19, "F - Finalization"],
]

# Task colors
task_colors = {
    "A - Setup": "#B3D9FF",
    "B - Core System": "#FFB3B3",
    "C - Functional Core": "#FFD699",
    "D - Relational Core": "#99FF99",
    "E - Evaluation": "#FF6666",
    "F - Finalization": "#CCCCFF",
    "Holiday": "#D3D3D3",  # Color for "Holiday" section
}

holiday_patch = mpatches.Patch(color=task_colors["Holiday"], label="Winter Holiday")

# Build ticks (unchanged values)
ticks_1 = [
    "Sem 1: " + str(datetime(2025, 11, 24) + timedelta(weeks=i))[:10] for i in range(4)
]
ticks_2 = ["Holiday: week " + str(i) for i in range(1, 5)]
ticks_3 = [
    "Sem 2: " + str(datetime(2026, 3, 2) + timedelta(weeks=i))[:10] for i in range(10)
]
ticks = ticks_1 + ["..."] + ticks_2 + ["..."] + ticks_3  # total = 20

# Correct tick positions and labels to match the timeline
positions = list(range(1, 21))  # Now there are 20 positions, one for each week

# Create the plot
fig, ax = plt.subplots(figsize=(14, 6))

# Draw background color for the entire holiday section, from the first "..." to the second "..."
# Adjust this range according to your desired holiday section
ax.axvspan(4, 10, color=task_colors["Holiday"], alpha=0.3)

# Draw bars with specific colors
seen = set()
for task_name, start_week, end_week, category in tasks:
    left = start_week - 1
    width = end_week - start_week + 1
    label = category if category not in seen else None
    seen.add(category)
    ax.barh(task_name, width, left=left, label=label, color=task_colors[category])

# Adjust the x-axis ticks and positions to the middle of each period
ax.set_xlim(0, 20)  # ensures first & last ticks fully visible
ax.set_xticks(positions)  # Set tick positions
ax.set_xticklabels(ticks)  # Set tick labels

# Enable grid lines
ax.grid(True, axis="x", linestyle="--", alpha=0.7)

# Axis labels/title
ax.set_xlabel("Timeline Units")
ax.set_ylabel("Tasks")
ax.set_title("Gantt Chart of Project Timeline")

# Rotate tick labels and tighten layout
for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_ha("right")

ax.margins(x=0)  # no extra horizontal margin
ax.legend(
    handles=[holiday_patch] + [patch for patch in ax.get_legend_handles_labels()[0]],
    loc="upper left",
    bbox_to_anchor=(1.0, 1.0),
)

# Final adjustments
plt.tight_layout()

# Show the plot
# plt.show()

# Save the plot as an image file
plt.savefig("assets/images/gantt_chart.png", dpi=300)
