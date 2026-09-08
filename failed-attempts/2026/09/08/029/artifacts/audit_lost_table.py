"""Audit Jablan Lost table (Table \\ref{Lost}) from committed source jablan_QATables.tex.
Stdlib-only. Prints entries and checks count/conway strings verbatim.
"""
import re, pathlib
SRC = pathlib.Path(__file__).parent.parent.parent / "jablan_QATables.tex"
# fallback: workspace root layout
if not SRC.exists():
    SRC = pathlib.Path("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-121/jablan_QATables.tex")
text = SRC.read_text()
i = text.find("Candidates for 12-crossing")
seg = text[max(0,i-2500):i+800]
# extract tabular rows of Lost table: lines with 12n_
rows = re.findall(r"\$12n_\{(\d+)\}\$\s*&\s*\$?([^$&]*?)\$?\s*&", seg)
# more robust: grab the tabular block
m = re.search(r"12n_\{139\}.*12n_\{838\}.*?\n", text, re.S)
block_start = text.find("$12n_{139}$")
block = text[block_start:block_start+600]
print("=== Lost-table block (verbatim) ===")
print(block)
print("=== end block ===")
labels = re.findall(r"\$12n_\{(\d+)\}\$", block)
print("labels in block:", labels)
assert labels == ["139","331","397","414","768","838"], labels
print("count:", len(labels))
print("OK: exactly 6 Lost candidates")
# record Conway strings verbatim (manual transcription checked against block):
conway = {
 "12n139": ".2.(-2 1,2).2",
 "12n331": "(-3,-2 -1)(3,2+)",
 "12n397": "2 1 1:-2 -1 0:2 0",
 "12n414": "-2 -1 0.3.2.2 0",
 "12n768": "2:-3 -1 0:3 0",
 "12n838": "-2.-2.-2 0.2.2.2 0",
}
for k,v in conway.items():
    assert v in block or v.replace(" ","") in block.replace(" ","").replace("\\,",""), k
print("Conway strings verified present (modulo TeX spacing).")
# flag 12n397 dual listing
j = text.find("and $12n_{397}$")
print("--- 12n397 dual-listing context (verbatim) ---")
print(text[j-200:j+300])
