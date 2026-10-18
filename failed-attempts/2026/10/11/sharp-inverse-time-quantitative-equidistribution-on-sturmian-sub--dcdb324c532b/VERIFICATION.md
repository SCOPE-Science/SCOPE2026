---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Huang–Jenkinson–Xu–Zhang Theorem D supplies exact f-mu(f)=c_f(Phi-alpha)+u∘sigma-u, |c_f|≤Lip/(1-theta)^2 and |u|Lip≤theta Lip/(1-theta)^3. Sturmian digit balance gives |S_n(Phi-alpha)|<1. Summation and diameter≤1 give the claimed [n(1-theta)^3]^-1 Wasserstein estimate by duality; triangle inequality and Birkhoff–von Neumann equal-weights transport give the upper F_n bound. For every irrational n alpha, the two possible digit counts floor(n alpha),ceil(n alpha) both occur, and the first-symbol 1-Lipschitz observable proves sup F_n≥1/n. Every n and every irrational alpha is covered without finite approximation; constants are upper bounds, not claimed optimum.

## originality

FAIL

This claimed endpoint Wasserstein and matching theorem is a near-immediate corollary of published Huang–Jenkinson–Xu–Zhang Theorem D (arXiv:2610.03619v1, October 2 2026) and its own explicit Sturmian balance lemma, combined only with standard Wasserstein duality and the permutation representation. The source contains precisely the quantitative Lipschitz constants and uniform balance needed; the lower bound follows mechanically from two adjacent word counts. Under claim-versus-prior implication and corollary coverage rules, a previously proved stronger cohomological statement covers the substance even though it does not spell out the n^-1 matching theorem. FAIL O, not failure to locate literature.

## value

PASS

The endpoint n^-1 scale for intrinsic empirical orbit matching is a natural quantitative unique-ergodicity benchmark and the two-sided explicit estimate could be useful to compare other subshifts. Its meaning is motivated by prior tau<1 results, even though this particular derivation is already forced by the earlier published source and therefore not original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
