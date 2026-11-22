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

# Verification

The proof in RESULT.md is valid for every integer in its stated domain; the finite program is not used to extrapolate to infinitely many cases. `VERIFY_CYLINDER.py` contains two check paths: a shortest-path-layer breadth-first search that forbids other selected vertices, and a deterministic construction of the same-band and inter-band paths, with independent checks of geodesic length and internal-vertex avoidance.

Execute with standard Python 3, no third-party packages:

```sh
python3 VERIFY_CYLINDER.py
```

Observed output from the embedded script:

```text
VISIBILITY_CYLINDER_VERIFY_OK instances 360 height_range 3..17 circumference 6s-6 and 6s-4..6s+18
```

The tested parameters have \(3\le s\le17\) and \(n=6s-6\) or \(6s-4\le n\le6s+18\). These cover all three residues of the circumference, both arithmetic boundary forms and graphs of increasing size. No complete optimization enumeration of all vertex subsets is asserted; the analytic upper bound proves optimality. No independent external mathematical audit is claimed.
