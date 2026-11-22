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

The accompanying `CHECK.py` is a standalone numerical/symbolic consistency test using Python 3, NumPy, SciPy and SymPy. Executing `python CHECK.py` produced:

```
PASS 363 independent symbolic/numerical assertions
benchmark D=v=beta=delta=1 r*= 1.0971675407097277
```

The checks encompass symbolic optimizer elimination and derivatives, root ordering, both reset-preparation slow-mode residues, independent Fourier inversion of the diffusive-phase resolvent, conditional right/left tails from integral-kernel inversion, and a separate bounded numerical maximizer for eight diverse parameter sets. Weak and strong reset asymptotic ratios were also tested. Tail ratios are evaluated after removing their common exponentially small scale to avoid floating-point underflow. These finite tests are supportive: strict positivity and uniqueness for all real positive parameters are proved in `RESULT.md`, not certified by the numerical grid. The proof relies on the elementary quadratic and monotonicity arguments stated there.

The novelty assessment is a self-review of inspected source claims, not an independent priority determination. No independent audit was performed.
