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

# Reproducibility and verification

Execute commands from the root of this extracted artifact. The package is self-contained for the **exact** checks and exhaustive integer proof; a separate NumPy/SciPy installation is needed only for the corroborative separate MILP check.

```
python3 src/verify_exact.py
g++ -O3 -std=gnu++17 src/max_clique.cpp -o max_clique
./max_clique 6
python3 src/milp_crosscheck.py
```

The first command reconstructs every Dyck word of semilength one through six, all one-bit received balls, every packed codeword list, every sparse rational primal/dual coefficient and every primal/dual constraint. Its terminating line is `EXACT_ALL_OK`. The executable separately generates the source set and checks the maximum clique by full branch-and-bound with a proper greedy coloring bound. The six-pair run reports `MAX 22 NODES 3250007 ... WORDS 132`. The optional integer-programming cross-check generates the sources by combinations and reports `MILP_ALL_OK`. The secondary solver reports exact mixed-integer optimal statuses with zero requested MIP gap, but it is not relied on as a standalone mathematical upper-bound certificate.

The integer and fractional results apply to \(1\le n\le6\) only. Nothing in the finite run is a proof about larger semilengths. Each source code is a list of *bitmasks* with bit zero representing the first word position, and a one denoting an upward Dyck step. For the fractional program, the dual output masks include all one-substitution outputs even if they are not Dyck words.
