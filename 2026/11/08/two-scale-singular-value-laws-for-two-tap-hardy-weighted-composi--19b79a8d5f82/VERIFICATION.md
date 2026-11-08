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

# Verification of two-scale two-tap Hardy spectral law

The attached `verify.py` is standalone and uses exact rational arithmetic from Python's standard library. Run it with `python3 verify.py`. On the package version, its result was:

`TWO_TAP_EXACT_CHECK_OK 129 rational assertions; infinite spectral limits require the written proof`

It enumerates finite cyclic nearest-neighbor words, checks the constant and circular endpoint moment polynomials for six powers and three positive rational tap amplitudes, and verifies explicit fourth and sixth moments. It then constructs three independently assembled rational finite Gram matrices and checks powers one through three against the analytic infinite trace, with a rigorous upper bound on all paths omitted by the compression.

A compressed \(N\)-column Gram matrix omits only closed walks that reach column \(N\) or higher. Such a length-\(k\) walk starts no lower than \(N-mk\), has minimum no lower than \(N-2mk\), and has at most \(3^k\) possible step sequences. For tap size \(a>0\) and dilation \(r\), its omitted exact trace is therefore bounded above by
\[
\frac{3^k(1+a^2)^k r^{2k(N-2mk)}}{1-r^{2k}},\qquad N\ge2mk.
\]
The checker verifies strict positivity and strict compliance with this bound in three independent nontrivial rational parameter families.

The finite checks do not establish the all-orders theorem or the limit distribution: those require the analytic walk decomposition and the moment-determinacy argument in `RESULT.md`. They do not establish novelty or independently validate the result. The full result has not undergone an independent mathematical audit.
