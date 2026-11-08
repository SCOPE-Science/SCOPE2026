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

# Reproducibility

The three standalone scripts use Python 3 standard library only. Run them at the package root:

```
python3 code/census_bitmask.py > /tmp/census_bitmask.json
python3 code/verify_direct.py > /tmp/verify_direct.json
python3 code/check_structure.py > /tmp/check_structure.txt
```

The files in `outputs/` record the exact output of these commands. The two census programs independently reproduce, for rook versus Shrikhande, 302 versus 142 fixed states, 1,197 versus 685 two-cycle orbits, and maximum first-entry times three versus five. They also agree exactly on the full time/period table and the initial fixed and two-periodic counts by number of occupied sites. The third program directly checks the graph identity \(A^2=4I+2J\) and eight versus zero four-cliques/four-site fixed states.

`code/census_bitmask.py` builds all 65,536 successors for each graph, and exhaustively decomposes the functional graph without assuming the period-two theorem. `code/verify_direct.py` instead creates separate coordinate-neighbor lists and evaluates signed-neighbor sums on each successive iterate. Its bound of sixteen candidate entrance times is sufficient on both graphs because the program asserts that **every one** of the 65,536 inputs is classified, rather than assigning a default class to unvisited inputs. Witnesses of maximum entrance time are included in its output. The structural check does not use either trajectory program.

Both census outputs were executed and the common tables compared exactly. Outputs alone are not proofs: the elementary complete-enumeration algorithms, explicit finite domain, and assertion that every state is processed constitute the computational proof, with the analytic fixed-four-site argument furnishing an independent structural check.

The limitations are finite scope, reliance on reproducible exhaustive computation for most exact numbers, and the absence of an independent external audit. No claims are made for other graph sizes or threshold rules.
