---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Cube vertex translations and permutations of bit coordinates act transitively on ordered incident edge pairs; on the circulant the translations and multipliers -1 and 5 give arc transitivity. The circulant's neighborhoods are exactly the two neighboring residue classes of i modulo 6, each with two lifts. The states were checked with an independent exact NumPy census (python3 /workspace/audit_excitable.py <source>/kahn_census.txt), writing neither source nor evidence files. Both complete successor maps were built from the labelled graphs and the synchronous rule, then iterated images were taken until stable, not by the supplied trajectory or indegree algorithms and not with a cutoff. The stable image is precisely the periodic states (restriction is surjective on a finite set, and all periodic points belong to every image). The iterated image sizes were (531441,104156,8781,621,121,37,25) and (531441,97154,8345,973,285,183,147). Least period and smallest phase label were computed by returns on the stable image; first entry and ultimate orbit were tallied from every input. All entry/period and per-orbit basin multiplicities agreed exactly, including depth-six populations 72 and 8592 and circulant period-four and period-six basins 32 times 180 and 2 times 12810. Thus the circulant oscillates from 31386 states and the cuboctahedron from 24, with the stated exact uniform probabilities. For the quotient check, independent swaps of the false twins are automorphisms, act transitively on the fibre of a histogram signature, and commute with the map. A quotient-periodic signature recurs on a finite fibre that is mapped onto itself by the return map (equivariance and transitivity), so quotient first-entry time is also labelled first-entry time. The equivariance justifies the canonical-lift period check and explains why quotient period alone is insufficient. The frozen C++ sources and their outputs were inspected, not executed; the independent census supplies full coverage.

## originality

PASS

Pass for the stated comparison of the two quartic arc-transitive graphs and the complete circulant census, not for either any standalone cuboctahedral count or the generic occurrence of periods four or six. The cuboctahedral census is an independently corroborated comparator: a distinct same-day record and its published attachments already state exactly that entire part. No temporal priority for either record is inferred from the common date. The materially distinct result is the labelled dynamics of C_12(1,5) and its quantitative contrast with that comparator.

## value

PASS

The canonical comparison holds small global graph statistics fixed while isolating stark differences in recurrence. The exact labelled circulant result matters beyond example periods: the cycle-lift effect yields 32 primitive four-orbits with exact basin sizes, and the relative rarity of recurrent phases versus mass in basins would not follow from merely finding period witnesses. Matching the sharp entry bound but not the attractor structure makes the known cuboctahedral census a good control. This is a finite benchmark, not an arbitrary-graph or causal geometry theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
