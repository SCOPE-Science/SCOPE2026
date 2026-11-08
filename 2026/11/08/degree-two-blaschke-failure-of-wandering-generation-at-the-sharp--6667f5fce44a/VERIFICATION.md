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

Analytical checks: monomial norms from beta integration; even part of the binomial kernel; complete Cayley-transform zero equation for \(1<\alpha+2\leq3\); bounded division by a Blaschke factor in the original weighted Bergman norm; cyclicity of the even subspace; point-evaluation obstruction; and unitary equivalence of degree-one Blaschke multipliers with the ordinary Bergman shift.

Reproducible finite checker: run `python3 kernel_checker.py` with Python 3 (standard library only). It prints `EVEN_BERGMAN_KERNEL_EXACT_OK 363` after 363 exact assertions. This finite test does not establish infinite-dimensional properties or all-parameter zero completeness; those follow from the proof in RESULT.md.

The result is restricted to the stated degree threshold and cyclic witness family. No independent mathematical audit or publication-priority certification is claimed.
