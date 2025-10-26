from pathlib import Path


def test_copy_html_contains_expected_text():
    html_path = Path(__file__).resolve().parent.parent / "copy.html"
    content = html_path.read_text(encoding="utf-8")
    assert "aaa" in content
