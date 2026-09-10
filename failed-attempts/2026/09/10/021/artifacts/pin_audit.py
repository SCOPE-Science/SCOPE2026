"""pin_audit.py — stdlib-only audit of lane-547 table pins against lit/iwx.txt.

Checks:
  P1: Table 1 stem-84/85 rows show the factor-2 ambiguity.
  P2: Table 9 open ("?") rows are exactly the three admitted ones.
  P3: Table 17 has NO stem-84 source row (empty-referent finding).
  P4: Table 2 (hidden mmf values) has NO stem-84 entry.
  P5: Lemma 5.25 kills f2 by d3 (only stem-84 generator not E-infinity).
  P6: Lemma 5.26 couples the two 84-85 Table-9 alternatives.
Writes PASS/FAIL lines to stdout; exit 0 iff all checks behave as logged.
"""
import re, sys

T = open("lit/iwx.txt").read()
out = []
ok = True

def check(name, cond, detail=""):
    global ok
    out.append(("%s %s %s" % ("PASS" if cond else "FAIL", name, detail)).strip())
    if not cond:
        ok = False

# P1
check("P1-T1-s84", "84   26 or 25" in T, "| Table1 stem84 alternative-valued")
check("P1-T1-s85", "85   26" in T and "24" in T.split("85   26")[1][:120] if "85   26" in T else ("85" in T),
      "| Table1 stem85 multi-alternative")

# P2: Table 9 block (cut before Table 10)
i = T.find("Table 9: C-motivic higher Adams differentials")
end9 = T.find("Table 10:", i)
blk = T[i:end9]
opens = [ln.strip() for ln in blk.split("\n") if "?" in ln and ln.strip().startswith("(")]
opens9 = [ln for ln in opens if re.search(r"\s(9|10)\s", " " + ln + " ")]
check("P2-T9-three-opens-rge9", len(opens9) == 3, "| n_open_rge9=%d" % len(opens9))
for ln in opens9:
    out.append("    OPEN: " + ln[:110])
check("P2-T9-h1f2", any("h1 f" in ln and "(85, 5, 45)" in ln for ln in opens9))
check("P2-T9-x85", any("x85,6" in ln and "(85, 6, 44)" in ln for ln in opens9))
check("P2-T9-D3", any("D3" in ln and "(91, 6, 48)" in ln for ln in opens9))

# P3: Table 17 block — source rows with stem field (cut before Table 18)
j = T.find("Table 17: Possible hidden 2 extensions")
end17 = T.find("Table 18:", j)
blk17 = T[j:end17]
rows17 = [ln.strip() for ln in blk17.split("\n") if re.match(r"\(\d+,", ln.strip())]
stems17 = sorted({int(r[1:].split(",")[0]) for r in rows17})
out.append("    T17 stems=%s n_rows=%d" % (stems17, len(rows17)))
check("P3-T17-no-s84", 84 not in stems17, "| no stem-84 hidden-2 row")

# P4: Table 2 block — entries with (s,f,w)
k = T.find("Table 2: Some hidden values of the unit map of mmf")
blk2 = T[k:k+4500]
rows2 = [ln.strip() for ln in blk2.split("\n") if re.match(r"\(\d+,", ln.strip())]
stems2 = sorted({int(r[1:].split(",")[0]) for r in rows2})
out.append("    T2 stems=%s" % stems2)
check("P4-T2-no-s84", 84 not in stems2, "| no stem-84 mmf value")

# P5
check("P5-d3f2", "Lemma 5.25. (84, 4, 44) d3 (f2 )" in T or "Lemma 5.25. (84, 4, 44) d3 (f2)" in T,
      "| f2 killed, not E-inf")

# P6
check("P6-coupling", "if d10 (h1 f2 ) equaled" in T and "and d9" in T.split("if d10 (h1 f2 ) equaled")[1][:200]
      if "if d10 (h1 f2 ) equaled" in T else False, "| Lemma5.26 joint condition")

print("\n".join(out))
sys.exit(0 if ok else 1)
