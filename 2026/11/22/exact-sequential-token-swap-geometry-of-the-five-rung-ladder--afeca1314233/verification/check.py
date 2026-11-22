#!/usr/bin/env python3
"""Recompute finite ladder token-swapping metrics from two independent enumerations."""
import ast
import json
import pathlib
import re
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent
EXPECTED = json.loads((ROOT / "expected.json").read_text(encoding="utf8"))

def number_line(line, prefix):
    assert line.startswith(prefix), (prefix, line)
    return [int(s) for s in line[len(prefix):].strip().split()]

def permutations(line):
    return sorted(tuple(ast.literal_eval(s)) for s in re.findall(r"\[[^\]]*\]", line))

def run(binary, n):
    return subprocess.check_output([str(binary), str(n)], text=True).strip().splitlines()

def analyse(lines, method):
    header=lines[0]
    match=re.search(r"(?:states|nstate) (\d+).*diameter (\d+) antipodes (\d+)", header)
    assert match, header
    states, diameter, count=map(int,match.groups())
    layers=number_line(lines[1], "counts")
    assert len(layers)==diameter+1 and sum(layers)==states
    antipodes=permutations(lines[2])
    assert len(antipodes)==count
    match=re.match(r"maxgap (\d+) (?:(?:hist)|(?:count (\d+) histogram))(.*)", lines[3])
    assert match, lines[3]
    gap=int(match.group(1))
    gap_layers=[int(s) for s in match.group(3).strip().split()]
    assert len(gap_layers)==gap+1 and sum(gap_layers)==states
    gap_perms=permutations(lines[4])
    if method=="packed":
        assert int(match.group(2))==gap_layers[-1]
    else:
        assert len(gap_perms)==gap_layers[-1] if gap_layers[-1]<=10 else True
    return (states,diameter,antipodes,layers,gap,gap_layers,gap_perms)

def main():
    with tempfile.TemporaryDirectory() as tmp:
        t=pathlib.Path(tmp)
        bins={}
        for name,src in (("lehmer","lehmer_bfs.cpp"),("packed","packed_bfs.cpp")):
            binary=t/name
            subprocess.run(["g++","-std=c++17","-O2",str(ROOT/src),"-o",str(binary)],check=True)
            bins[name]=binary
        for cols in (3,4,5):
            one=analyse(run(bins["lehmer"],cols), "lehmer")
            two=analyse(run(bins["packed"],cols), "packed")
            assert one[:6]==two[:6], (cols,"independent enumerations differ")
            if cols==5:
                assert one[0]==EXPECTED["states"]
                assert one[1]==EXPECTED["diameter"]
                assert one[2]==sorted(map(tuple,EXPECTED["furthest"]))
                assert one[3]==EXPECTED["distance_layers"]
                assert one[4]==EXPECTED["max_transport_deficit"]
                assert one[5]==EXPECTED["deficit_layers"]
                assert one[6]==[tuple(EXPECTED["unique_max_deficit_state"])]
                assert two[6]==one[6]
                print("P2xP5 verified: 3628800 states, diameter 21, four antipodes, unique gap-eight placement")
            else:
                cal=EXPECTED["calibration"][str(cols)]
                assert one[0]==cal["states"] and one[1]==cal["diameter"]
                assert len(one[2])==cal["antipode_count"] and one[4]==cal["max_deficit"]
                print(f"P2xP{cols} calibration verified")
        print("Independent exhaustive checks: PASS")

if __name__=="__main__":
    main()
