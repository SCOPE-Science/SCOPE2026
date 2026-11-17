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

Run `python3 verify_pair_shortcuts.py` with Python 3.8+ and no nonstandard dependencies. Expected terminal output:

```
VERIFY_OK independent face/links/Euler cases=90; modular boundary cases=114; faces_examined=166469
```

The checker enumerates all arc subsets of both-shortcut digraphs for \(6\le n\le12\) and all inequivalent cyclic separations, directly verifies degree at most one at each source/target, detects directed cycles by following successor pointers, and checks the exact simplicial link of the second shortcut. It also checks both stage inclusions and the reduced Euler characteristics for the 90 resulting stages. For \(6\le n\le10\), it independently constructs signed boundary columns and reduces them over \(\mathbb F_2\) and \(\mathbb F_3\), checking the stated reduced Betti vectors at each stage.

These finite computations neither establish an infinite family nor prove absence of all integral torsion. The written exact link-cone decompositions, their nullhomotopic attaching maps and the resulting wedge decompositions provide the infinite-parameter integral proof. No machine proof assistant or independent human audit is claimed.
