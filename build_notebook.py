import nbformat
from pathlib import Path

project_folder = Path(__file__).parent

notebook = nbformat.v4.new_notebook()

# Title
notebook.cells.append(
    nbformat.v4.new_markdown_cell(
        """# DATAFLOW COHORT 2 — WEEK 1

## Python Overview, Introduction & Setup

**Student:** Jennifer Emmanuel  
**Cohort:** DataFlow Cohort 2  
**Week:** 1  
**Topic:** Python Programming Fundamentals

---

This notebook contains my Week 1 Python practice tasks,
assignments, and assessments.
"""
    )
)

# TASKS
notebook.cells.append(
    nbformat.v4.new_markdown_cell("# 1. Python Practice Tasks")
)

tasks_folder = project_folder / "tasks"

for file in sorted(tasks_folder.glob("*.py")):
    notebook.cells.append(
        nbformat.v4.new_markdown_cell(
            f"## {file.stem.replace('_', ' ').title()}"
        )
    )

    code = file.read_text(encoding="utf-8")
    notebook.cells.append(
        nbformat.v4.new_code_cell(code)
    )

# ASSIGNMENTS
notebook.cells.append(
    nbformat.v4.new_markdown_cell("# 2. Week 1 Assignments")
)

assignments_folder = project_folder / "assignments"

for file in sorted(assignments_folder.glob("*.py")):
    notebook.cells.append(
        nbformat.v4.new_markdown_cell(
            f"## {file.stem.replace('_', ' ').title()}"
        )
    )

    code = file.read_text(encoding="utf-8")
    notebook.cells.append(
        nbformat.v4.new_code_cell(code)
    )

# ASSESSMENTS
notebook.cells.append(
    nbformat.v4.new_markdown_cell("# 3. Week 1 Assessments")
)

assessments_folder = project_folder / "assessments"

for file in sorted(
    assessments_folder.glob("assessment_*.py"),
    key=lambda x: int(x.stem.split("_")[1])
):
    number = file.stem.split("_")[1]

    notebook.cells.append(
        nbformat.v4.new_markdown_cell(
            f"## Assessment {number}"
        )
    )

    code = file.read_text(encoding="utf-8")
    notebook.cells.append(
        nbformat.v4.new_code_cell(code)
    )

# SAVE
output_file = project_folder / "DataFlow_Week_1_Python_Practice.ipynb"

with open(output_file, "w", encoding="utf-8") as file:
    nbformat.write(notebook, file)

print("Notebook created successfully!")
print(f"Location: {output_file}")
