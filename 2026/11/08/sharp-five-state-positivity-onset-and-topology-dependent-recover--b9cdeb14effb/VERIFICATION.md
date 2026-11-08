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

Run `python checker.py` with SymPy installed. The accompanying `checker_output.txt` was produced by executing this exact script. It reports 239 exact symbolic/rational assertions, the algebraic cycle threshold, and the isolated positive absorbing threshold. The script computes exact inverse matrices in dimensions two through five for cycles and through six for pure-birth chains, checks rational entry formulas, and tests exact rational points across the two boundary values.

The all-dimensional conclusions are **analytical**. The coefficient \(-1/4\) of \(z^4\) in \(r(z)=(1-z+z^2/2)^{-1}\) gives a negative distance-four coefficient for every sufficiently small step on all larger cycles and birth chains. For every fixed finite cycle, all nonconstant Fourier modes vanish in the large-step limit, yielding the strictly positive uniform rank-one projector. For every fixed finite birth chain, transient forward-distance coefficients are asymptotically \(2(j+1)/h^2>0\), and absorption probabilities tend to one. Those are mathematical arguments, not claims that a finite test enumerated all sizes.

The self-review assessed correctness, originality and mathematical value; it is not independent scientific verification. Source text comparisons were performed with arXiv:2102.11939 (2021), arXiv:1303.6651 (2013), and arXiv:2412.15142 (2024), and analogous published research summaries. The conclusion is restricted to the unit-rate graph families stated in RESULT.md. No formal proof certificate or external certification was produced.
