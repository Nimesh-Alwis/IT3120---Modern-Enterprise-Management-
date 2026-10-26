"""Convert the self-contained IT3120 HTML quiz data into a study-friendly Markdown paper."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "IT3120_Model_Paper_Lectures_01_to_05.html"
OUTPUT = ROOT / "IT3120_Model_Paper_Lectures_01_to_05_With_Answers.md"


def clean(value: object) -> str:
    """Make embedded HTML/JSON text readable in Markdown."""
    text = "" if value is None else str(value)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    return " ".join(text.split())


html = SOURCE.read_text(encoding="utf-8")
match = re.search(
    r'<script type="application/json" id="quizData">(.*?)</script>',
    html,
    flags=re.DOTALL,
)
if not match:
    raise RuntimeError("quizData JSON was not found in the source HTML")

data = json.loads(match.group(1))
questions = data["questions"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lines = [
    "# IT3120 Model Paper — Lectures 01 to 05",
    "",
    "> Practice paper with 75 multiple-choice questions. Some questions have more than one correct answer. Attempt all questions before consulting the answer key.",
    "",
    "## Coverage",
    "",
    "- Lecture 01: Introduction to Management Concepts",
    "- Lecture 02: Introduction to Marketing",
    "- Lecture 03: Introduction to Economics",
    "- Lecture 04: Introduction to Human Resource Management",
    "- Lecture 05: Introduction to Financial Accounting",
    "",
    "## Instructions",
    "",
    "- Total questions: 75",
    "- Suggested time: 90 minutes",
    "- Award one mark only when the selected option set exactly matches the answer key.",
    "- For questions marked **Select all that apply**, select every correct option and no incorrect options.",
    "",
    "## Questions",
    "",
]

for number, question in enumerate(questions, start=1):
    answer_count = len(question["ans"])
    question_type = "Select one" if answer_count == 1 else "Select all that apply"
    lines.extend(
        [
            f"### Question {number} — {clean(question.get('topic'))}",
            "",
            f"**{question_type}.** {clean(question.get('text'))}",
            "",
        ]
    )
    if question.get("table"):
        lines.extend([clean(question["table"]), ""])
    if question.get("code"):
        lines.extend(["```", str(question["code"]).strip(), "```", ""])
    for index, option in enumerate(question["opts"]):
        lines.append(f"- {letters[index]}. {clean(option)}")
    lines.append("")

lines.extend(["---", "", "## Answer Key and Explanations", ""])

for number, question in enumerate(questions, start=1):
    answer_letters = ", ".join(letters[index] for index in question["ans"])
    answer_text = "; ".join(
        f"{letters[index]}. {clean(question['opts'][index])}" for index in question["ans"]
    )
    lines.extend(
        [
            f"### {number}. Answer: {answer_letters}",
            "",
            f"**Correct option(s):** {answer_text}",
            "",
            f"**Explanation:** {clean(question.get('exp'))}",
            "",
            f"**Source:** {clean(question.get('src'))}",
            "",
        ]
    )

OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
print(f"Generated {OUTPUT.name} with {len(questions)} questions")
