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

The complete theorem and all analytic estimates appear in `RESULT.md`. The standalone `checker.py` requires Python 3 and only its standard library; run `python checker.py` from a directory containing that file. It prints `CHECK_OK` after exact fractional-arithmetic checks of the conserved-energy cancellation and the transformed-force derivative, monotonic period comparisons on sampled amplitudes, numerical large-amplitude normalizations across fixed and varying parameters, and turning-layer CDF comparisons to the arcsine limit.

The exact period identity is \(T=2I_A/[A\sqrt\beta\sqrt{1+\alpha A^2}]\), with \(I_A\to\pi\). The proof of its coefficient uniformity uses an explicit \(L^1\) bound and exponential tail estimate, not computation. The total-variation conclusion is derived from the same \(L^1\) limit and the exact physical-time density. Tests cover only finitely many parameter values and do not establish the all-amplitude or all-parameter statements.

The connection with the prior global-center classification is verified at coefficients \(a_4=-\alpha\), \(a_6=-\beta\), and all remaining cubic coefficients zero. The zero-restoring boundary is explicitly acknowledged as previously studied. Publication priority against literature outside the searched and inspected corpus is not certified.
