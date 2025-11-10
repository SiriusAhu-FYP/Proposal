from datetime import datetime, timedelta

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# Define the tasks data
tasks = [
    # --- BLOCK 1: Semester 1 (Weeks 1-4) ---
    ["Project Setup & Research Finalization", 1, 1, "A - Setup"],
    ["Core Architecture Design (Orchestrator & MCP API)", 1, 2, "A - Setup"],
    # --- Long-Running "Backbone" Tasks ---
    ["[LONG] Orchestrator & MCP Bus (v1 -> v3 Integration)", 2, 13, "B - Core System"],
    ["[LONG] Functional Core (v1 Train -> v2 Transfer)", 7, 13, "C - Functional Core"],
    # --- Iterative "Plug-in" Modules ---
    ["Relational Core (v1 Stub & Live2D Setup)", 3, 4, "D - Relational Core"],
    [
        "Relational Core (v2 Proactive & Full Integration)",
        13,
        14,
        "D - Relational Core",
    ],
    ["Perception Module (v1 for Phase 1 Games)", 5, 7, "C - Functional Core"],
    ["Perception Module (v2 for Phase 2 Game)", 11, 13, "C - Functional Core"],
    ["GCC I/O Module (Keyboard/Mouse Control)", 5, 6, "C - Functional Core"],
    ["Safety Core (BacktrackAgent-style Verifier)", 9, 10, "C - Functional Core"],
    # --- BLOCK 2: Winter Holiday (Weeks 5-8, 4 weeks total) ---
    # Note: Tasks 5-8 from the list above (Perception v1, GCC I/O, Functional Core v1 start)
    # are all designated to happen within this block.
    # --- BLOCK 3: Semester 2 (Weeks 9-18) ---
    ["Phase 1: Functional Evaluation (Run Tests)", 10, 11, "E - Evaluation"],
    ["Phase 2: A/B User Study (Recruit & Run Tests)", 14, 15, "E - Evaluation"],
    ["Final Code Cleanup & Bug Fixing", 16, 17, "F - Finalization"],
    ["Final Documentation (Code & System)", 16, 18, "F - Finalization"],
    ["Final Demo Video Prep", 18, 19, "F - Finalization"],
]


# Function to add "..." task for Winter Holiday break
def add_ellipsis_task(tasks):
    ellipsis_task = ["...", 5, 9, "Holiday"]
    new_tasks = []
    for task in tasks:
        new_tasks.append(task)
        if task[1] == 4:  # After Week 4 (the end of Semester 1 + Winter Holiday break)
            new_tasks.append(ellipsis_task)

    return new_tasks


# Apply the function to add the "..." task
tasks_with_ellipsis = add_ellipsis_task(tasks)

# Dates for plotting
start_date = datetime(2025, 11, 24)  # Week 1 starts on Nov 24, 2025
week_length = timedelta(weeks=1)

# Create a list of weeks starting from Week 1
dates = [start_date + i * week_length for i in range(18)]

# Gantt chart setup
fig, ax = plt.subplots(figsize=(15, 6))

# Add background for Winter Holiday (Weeks 5-8 and "...")
holiday_start = dates[4]  # Week 5 (index 4)
holiday_end = dates[8]  # Week 9 (index 8, inclusive of "...")
ax.axvspan(
    holiday_start,
    holiday_end,
    color="lightgray",
    alpha=0.5,
    label="Winter Holiday (Weeks 5-8 & '...')",
)

# Task colors
task_colors = {
    "A - Setup": "#B3D9FF",
    "B - Core System": "#FFB3B3",
    "C - Functional Core": "#FFD699",
    "D - Relational Core": "#99FF99",
    "E - Evaluation": "#FF6666",
    "F - Finalization": "#CCCCFF",
    "Holiday": "#D3D3D3",  # Color for "..." task
}

# Plot tasks with the "..." task included
for task in tasks_with_ellipsis:
    task_name, start_week, end_week, category = task
    task_start = dates[start_week - 1]
    task_end = dates[min(len(dates) - 1, end_week - 1)]  # Ensure no out-of-range errors

    ax.barh(
        task_name,
        task_end - task_start,
        left=task_start,
        height=0.4,
        color=task_colors.get(category, "#D3D3D3"),
    )

# Customize x-axis with dates
ax.set_xticks(dates)
ax.set_xticklabels([date.strftime("%b %d") for date in dates])
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

# Labels and title
ax.set_xlabel("Dates")
ax.set_ylabel("Tasks")
ax.set_title("Gantt Chart for Project Schedule (18 Weeks)")

# Add a legend
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in task_colors.values()]
labels = list(task_colors.keys())
ax.legend(handles, labels, loc="upper right", title="Task Categories")

plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()
