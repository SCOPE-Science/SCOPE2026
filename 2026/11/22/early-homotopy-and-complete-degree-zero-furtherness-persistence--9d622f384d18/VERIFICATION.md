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

# Verification of the finite checks

The exact checker is `verify.py`. From the directory containing that file, run `python3 verify.py`. It uses the Python standard library, explicitly constructs the truncated downsets (rather than the proposed closed weight formula), enumerates all poset vertices, comparable pairs and strict three-element chains at threshold zero, one, \(r\), \(r+1\) and \(r+2\), and reduces the resulting first two simplicial boundary maps over \(\mathbb F_2\).

It confirms the predicted \(H_0\) and \(H_1\) dimensions at all these stages for all 35 triples \(3\le n\le7\), \(2\le r<n\), \(r\le k<n\). It also embeds a basis of early one-cycles in the later edge space and tests that their independent homology classes remain independent modulo later 2-boundaries. Replay output:

```
VERIFY_OK cases=35 2_simplices_scanned=8380 H1_injections=35
```

The tests work over one finite field and finitely many small parameter triples; they are not a proof of universal integral homotopy, integer torsion-freeness or later higher-degree persistence. The written argument establishes those precisely claimed integral facts using the contractible-core graph quotient and integral cycle-space injection. No external independent audit has been performed.
