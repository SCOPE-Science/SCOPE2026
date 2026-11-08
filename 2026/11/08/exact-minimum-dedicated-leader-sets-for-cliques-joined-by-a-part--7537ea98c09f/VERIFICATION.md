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

# Reproducibility and limits

The claim concerns only the unit-weight, undirected matched-clique graphs
with integer parameters \(m\ge3\) and \(2\le k\le m\).

Execute `python verify.py` with Python 3 and SymPy installed. The script
constructs each exact integer Laplacian for \(3\le m\le5\), computes exact
eigenvector bases, and tests full PBH coordinate restrictions for *every*
minimum-size candidate subset in nine parameter cases. It also computes
a full Kalman rank independently in one representative case and compares
the minimum-leader classification against zero forcing for \(m=3,k=2\).

Observed replay: 1,094 minimum-size subsets checked, 420 controllable
minimum sets, all matching the respective closed formulas; the full
Kalman rank equals the state dimension; only four of twelve fixed-Laplacian
minimum sets for \(m=3,k=2\) are zero forcing.

The finite replay is not a proof for arbitrarily large graphs; the
general PBH/eigenspace proof appears in `RESULT.md`. No exact claim for
arbitrary weights, unequal cliques, \(k=1\), or \(m=2\) is made.
