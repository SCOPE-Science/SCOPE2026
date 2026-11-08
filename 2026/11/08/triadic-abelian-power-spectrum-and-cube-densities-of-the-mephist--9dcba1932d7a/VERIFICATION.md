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

# Verification and reproduction

Run `python3 verify.py` using Python 3.9 or newer, from the same directory. No external package or downloaded data is needed.

The checker constructs the fixed point from digit parity and separately from the substitution; checks the block-sum formula at every residue and 50 consecutive macroblock indices for each \(k\in\{0,\ldots,8\}\); tests the exact cube predicate and absence of triadic fourth powers on these finite cases; verifies the two-state signed prefix-sum recurrence and the cube-density numerators through \(k=8\); tests the transition and triple-run identities on 50,000 indices; and verifies the nontriadic four-block factor at index 37.

Expected output:

`VERIFY_OK checks= 3121982 density_numerators= [1, 2, 5, 13, 35, 96, 267, 750, 2123] nontriadic_witness=(start=37,length=7,blocks=4)`

The exact domain and universal proof are in RESULT.md. Finite tests are diagnostics only. The density result uses a proved \(O(\log N)\) discrepancy bound rather than empirical convergence. No external or independent audit was performed.
