"""verify_census.py — independent replay checker for census_d1.json (stdlib only).

Re-derives from stored heights + triangulations:
  T0: lower hull == stored tris; unimodular; genus 3; K4 core; edge-conn 3.
  Each regular-certified row: lower hull of stored heights == stored new_tris;
    unimodular; genus 3; core edge-conn matches stored value.
Prints PASS/FAIL per check. Exit 0 iff all certified claims replay.
"""
import json
import os
import sys
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from honeycomb_flip import (PTS, IDX, lower_triangulation, check_triangulation,
                            skeleton_core, connectivity, genus_check, is_K4)

d = json.load(open(os.path.join(_HERE, 'census_d1.json')))
fails = []


def check(name, cond, extra=""):
    print(("PASS " if cond else "FAIL ") + name + ("  " + str(extra) if extra else ""))
    if not cond:
        fails.append(name)


T0 = [tuple(t) for t in d["T0_tris_idx"]]
h0 = [F(x) for x in d["T0_heights"]]
check("T0 lower-hull reproduces stored tris", sorted(lower_triangulation(h0)) == sorted(T0))
ok, msg = check_triangulation(sorted(T0))
check("T0 unimodular triangulation (16 tris, bdy/interior use)", ok, msg)
check("T0 genus == 3", genus_check(sorted(T0)) == 3)
n0, e0 = skeleton_core(sorted(T0))
check("T0 core is K4", is_K4(n0, e0), f"{n0} {e0}")
check("T0 core edge-conn == 3", connectivity(n0, e0)["edge_conn"] == 3)
check("T0 stored core matches", n0 == d["T0_core_nodes"] and
      sorted(map(tuple, d["T0_core_edges"])) == sorted(tuple(x) for x in e0))

ncert = 0
for r in d["rows"]:
    i = r["orbit"]
    nT = sorted(tuple(t) for t in r["new_tris"])
    ok, msg = check_triangulation(nT)
    check(f"row{i} unimodular triangulation", ok, msg)
    check(f"row{i} genus == 3", genus_check(nT) == 3)
    nodes, elist = skeleton_core(nT)
    ec = connectivity(nodes, elist)["edge_conn"]
    check(f"row{i} core edge-conn == stored ({r['edge_conn']})", ec == r["edge_conn"],
          f"core {nodes} {elist}")
    if r["regular_certified"]:
        ncert += 1
        h = [F(x) for x in r["regularity_heights"]]
        got = lower_triangulation(h)
        check(f"row{i} heights induce stored tris", got is not None and sorted(got) == nT)
    else:
        print(f"SKIP row{i} regularity replay (uncertified; heights=null)")

print(f"\n{len(fails)} failures; {ncert}/{len(d['rows'])} rows regular-certified")
sys.exit(1 if fails else 0)
