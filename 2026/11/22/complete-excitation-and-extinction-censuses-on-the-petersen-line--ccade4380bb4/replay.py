#!/usr/bin/env python3
"""Recompute complete ternary functional graphs using two distinct finite algorithms."""
import os
import pathlib
import subprocess
import tempfile

BASE = pathlib.Path(__file__).resolve().parent
EXPECTED = {
    1: {"orbit": {1: (1, 277077), 3: (220810, 13229250), 4: (60, 201240), 5: (30, 536580), 8: (60, 104760)},
        "depth": [663301, 711247, 2415219, 4096486, 3082074, 1856250, 660330, 476160, 274080, 93120, 14640, 4800, 1200]},
    2: {"orbit": {1: (1, 14348907)}, "depth": [1, 32767, 1986454, 9546631, 2642574, 139550, 930]},
    3: {"orbit": {1: (1, 14348907)}, "depth": [1, 32767, 8504178, 5811961]},
    4: {"orbit": {1: (1, 14348907)}, "depth": [1, 32767, 13475228, 840911]},
}
SECTIONS = ["cycles_by_period", "by_depth", "depth_by_period", "basin_hist_by_period"]

def extract(text):
    first = next(line for line in text.splitlines() if line.startswith("n_states "))
    tokens = first.split()
    header = {tokens[i]: int(tokens[i+1]) for i in (0, 2, 4)}
    out = {s: [] for s in SECTIONS}
    section = None
    for line in text.splitlines():
        if line in SECTIONS:
            section = line
            continue
        if line in ("period_representatives",) or line.startswith(("longest_trajectory", "witness_sequence")):
            section = None
        if section:
            out[section].append(tuple(map(int, line.replace("states", "").replace("basin_total", "").split())))
    return header, out

with tempfile.TemporaryDirectory(prefix="gh-replay-") as tmp:
    for src, name in [("threshold_census.cpp", "direct_trits"), ("independent.cpp", "two_bit_planes")]:
        subprocess.run(["g++", "-std=c++17", "-O3", str(BASE/src), "-o", tmp+"/"+name], check=True, capture_output=True)
    for theta in (1, 2, 3, 4):
        first = second = None
        for exe, saved in (("direct_trits", f"threshold{theta}.txt"), ("two_bit_planes", f"independent{theta}.txt")):
            proc = subprocess.run([tmp+"/"+exe, str(theta)], capture_output=True, text=True, timeout=180, check=True)
            observed = extract(proc.stdout)
            recorded = extract((BASE/saved).read_text(encoding="utf8"))
            assert observed == recorded, (theta, exe, "recorded-output mismatch")
            if exe == "direct_trits": first = observed
            else: second = observed
        assert first is not None and first == second, (theta, "independent implementations disagree")
        header, catalog = first
        assert header["n_states"] == 3**15
        assert header["max_depth"] == len(EXPECTED[theta]["depth"])-1
        assert [entry[1] for entry in catalog["by_depth"]] == EXPECTED[theta]["depth"]
        assert sum(EXPECTED[theta]["depth"]) == 3**15
        counts = {row[0]: (row[1], row[3]) for row in catalog["cycles_by_period"]}
        assert counts == EXPECTED[theta]["orbit"], (theta, counts)
        assert sum(row[1] for row in catalog["cycles_by_period"]) == header["n_attractors"]
        assert sum(row[-1] for row in catalog["cycles_by_period"]) == header["n_states"]
        assert sum(row[-1] for row in catalog["depth_by_period"]) == header["n_states"]
        assert sum(row[2] for row in catalog["basin_hist_by_period"]) == header["n_attractors"]
        print(f"theta={theta} complete: {header['n_states']} states; {header['n_attractors']} cycles; sharp entry={header['max_depth']}; two algorithms agree")
print("All finite-state census, basin, entry-time, and reproducibility checks passed.")
