#!/usr/bin/env python3
"""Bounded recovery test: DMZ Sec 5 / Cor 1.3 parity mechanism on the (6_1, m=1) cell.

Inputs are published primary-source integers (no new topology computed here):
  6_1: thin (alternating), det=9, tau=0, Arf=0, smoothly slice/ribbon (Katlas/KnotInfo/Gompf).
  4_1: thin control, det=5, tau=0, Arf=1.
DMZ Cor 1.3 condition: 2*Arf + |tau| in {1,2} mod 4  => S-nontrivial.
DMZ Sec 5 parity: # diagonal boxes = (D - 2|tau| - 1)/4; odd => staircase+box (s(a)=a+d, S-nontrivial),
even => bare connected complex (s = id, S-trivial).
"""
import json

def assess(name, D, tau, arf, thin=True):
    cong = (2 * arf + abs(tau)) % 4
    cor13 = thin and cong in (1, 2)
    assert (D - 2 * abs(tau) - 1) % 4 == 0, (name, "non-integral box count")
    boxes = (D - 2 * abs(tau) - 1) // 4
    s_nontrivial = cor13  # sufficient direction per DMZ Cor 1.3 / Sec 5
    return {"knot": name, "det": D, "tau": tau, "arf": arf,
            "cong_2arf_tau_mod4": cong, "cor13_applies": cor13,
            "diagonal_boxes": boxes, "boxes_parity": "odd" if boxes % 2 else "even",
            "s_nontrivial_via_cor13": s_nontrivial}

rows = [assess("6_1", 9, 0, 0), assess("4_1", 5, 0, 1)]
print(json.dumps(rows, indent=1))
k61 = rows[0]
assert k61["cong_2arf_tau_mod4"] == 0 and not k61["cor13_applies"]
assert k61["diagonal_boxes"] == 2 and k61["boxes_parity"] == "even"
assert not k61["s_nontrivial_via_cor13"]
assert rows[1]["cor13_applies"] and rows[1]["diagonal_boxes"] == 1  # control
print("RECOVERY_TEST_RESULT: 6_1 S-trivial via DMZ Sec-5 parity (2 even boxes); "
      "Thm 1.2/4.1/1.5 positive-witness route BLOCKED; 4_1 control reproduces S-nontriviality.")
