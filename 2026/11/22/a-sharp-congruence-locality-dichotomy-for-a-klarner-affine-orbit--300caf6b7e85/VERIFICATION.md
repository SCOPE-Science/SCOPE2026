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

Run the self-contained `verify.py` with a standard Python 3 interpreter. Its BFS constructs the exact forward residue orbit of \(0\) for every modulus \(1\le m\le2000\). It asserts the equivalence between full reachability and \(6\nmid m\) and checks the missing residue \(1\pmod6\) for all relevant moduli. The checker passed in an independent execution before packaging and in a replay extracted from the actual delivered package.

The code checks only finitely many moduli. Universal correctness is supplied by the separately written group-action and two-/threefold lifting proof in RESULT.md. No computer-assisted claim beyond exact finite BFS is made. No independent audit has been performed.
