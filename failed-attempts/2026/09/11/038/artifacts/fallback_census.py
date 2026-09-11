"""Bounded IW-X census for stem-55 fallback attempt (shuffling + Ext-cycle survival).
Parses workspace iwx.txt (Isaksen-Wang-Xu) Tables 1,3,4,6,9,10,11,15,17,18,20,23,24.
Prints: Table10/11/3 stems around 55, stem-55 E2/differential rows, hidden-extension rows at 55.
Reproducible with stdlib only: python3 output/artifacts/fallback_census.py
"""
import re, pathlib
P = pathlib.Path(__file__).resolve()
# locate iwx.txt: workspace root is two levels up from output/artifacts
for cand in [P.parents[2]/"iwx.txt", P.parents[1]/"iwx.txt", pathlib.Path("iwx.txt")]:
    if cand.exists():
        IW = cand; break
else:
    raise SystemExit("iwx.txt not found")
full = IW.read_text(errors="replace")
def seg_between(start_marker, end_markers, start_idx=0, window=9000):
    outs=[]
    for m in re.finditer(re.escape(start_marker), full):
        seg=full[m.start():m.start()+window]
        # cut at first end marker occurring after start
        cut=len(seg)
        for e in end_markers:
            j=seg.find(e, len(start_marker))
            if j!=-1: cut=min(cut,j)
        outs.append(seg[:cut])
    return outs
# Table 10 stems
segs10=seg_between("Table 10: Some Toda brackets", ["Table 11", "Table 12"])
rows10=[]
for s in segs10: rows10 += re.findall(r'^\s*\((\d+),\s*(\d+)\)', s, re.M)
stems10=sorted(set(int(a) for a,_ in rows10))
# Table 11 stems
i11=full.index("Table 11: Some null Toda brackets"); i12=full.index("Table 12", i11)
rows11=re.findall(r'^\s*\((\d+),\s*(\d+)\)', full[i11:i12], re.M)
stems11=sorted(set(int(a) for a,_ in rows11))
# Table 3: only true Massey block (two pages), bounded manually-verified window:
# page1 header at first occurrence, page2 header second; take until Table 4
i3=[m.start() for m in re.finditer(r'Table 3: Some Massey products in ExtC', full)]
rows3=[]
for h in i3:
    seg=full[h:h+6000]
    # cut at Table 4 or next Table header
    for e in ["Table 4:", "8. TABLES"]:
        pass
    rows3 += re.findall(r'^\s*\((\d+),\s*\d+,\s*\d+\)', seg, re.M)
# restrict to actual Massey rows: filter to segments before Table 4 header
# (the raw regex above can bleed into Table 4 E2 rows; so recompute tightly)
tight3=[]
for h in i3:
    tail=full[h:h+6000]
    # Table 3 page ends before the page-footer "8. TABLES" + next Table header; use first 2600 chars (one page)
    tight3 += re.findall(r'^\s*\((\d+),\s*\d+,\s*\d+\)', tail[:2600], re.M)
stems3=sorted(set(int(a) for a in tight3))
print("Table10 stems:", stems10)
print("Table10 gap 45->57, 55 present?", 55 in stems10)
print("Table11 stems:", stems11, "55 present?", 55 in stems11)
print("Table3 stems (tight):", stems3, "55 present?", 55 in set(int(a) for a in tight3))
print("--- stem-55 E2/diff/hidden rows (grep '(55') ---")
for i,l in enumerate(full.splitlines(),1):
    if "(55" in l: print(f"{i}: {l.strip()}")
print("--- Table 1 stem-55 group row ---")
for i,l in enumerate(full.splitlines(),1):
    s=l.strip()
    if re.match(r'^55\s', s): print(f"{i}: {l.rstrip()}")
