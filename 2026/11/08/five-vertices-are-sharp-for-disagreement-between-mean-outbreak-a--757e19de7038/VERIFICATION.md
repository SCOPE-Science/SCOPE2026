---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification scope

Execute `python check.py` with Python 3 and SymPy at least 1.11; it requires no network datasets, network services or private files. `census.txt` contains the expected complete list of \(21\) canonical five-vertex types and witnesses for the universal dual optimum or exceptional pairs.

The actual checker execution produced counts \(1,2,6,21\) of connected isomorphism types on \(2,3,4,5\) vertices, respectively; \(105\) exact comparisons between direct edge-state enumeration and the independently decomposed infected-component formula; \(19\) universal dual-optimal five-vertex classes; and exactly \(2\) exceptional five-vertex types. The exceptional mean and tail differences were checked symbolically, and all rival deletions were excluded by exact rational root-isolation inequalities on the entire open unit interval.

The smaller-order proof uses the exact spanning-subgraph chain on at most three remaining vertices and needs no machine enumeration. Polynomial root isolation is finite and exact, not a numerical sample; the checker proves only the bounded graph census, not any assertion about larger populations or a general SIR process. Scientific priority is assessed in the accompanying review, and no independent external audit has occurred.
