---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For real a_i, d>=2, boundaries a0=a_{d+1}=0 and Σa_i=0, continuous zero-mean H_0^1 inequality follows by decomposing positive/negative supports into Dirichlet Green intervals: if M=∫u+=∫u−, support lengths p,n with p+n<=1, E>=12M²(p^-3+n^-3)>=192M²; hence ∫|u|<=||u′||/√48 with equality only for two adjacent equal-length opposite parabolas ±u*. Piecewise linear mesh interpolation has ∫U=0 and ∫|U′|²=(d+1)E(a); opposite-sign trapezoid error<=h|Δa|/4, yielding upper (d+1)^{3/2}/√48+√(d+1)/4. Exact antisymmetric discrete Poisson witnesses for d=2k give K²>=k(k+1)(k²+k+1)/[3(2k+1)], approaching 1/48 under N³ scaling; appending a zero coordinate transfers odd d. For normalized near-extremizers, bounded H_0^1, compact uniform embedding, sharp equality class and weak-to-strong Hilbert norm convergence establish distance to ±u* tends to zero in H_0^1. Exact sign-dual Green checks d=2..10 corroborate, not prove, this unbounded claim.

## originality

PASS

The unrestricted real/complex first-difference norm and one-sign Landau extremizers are previously known; enforcing exactly one zero moment fundamentally changes admissible profiles. The proof derives a sharp signed continuum inequality with unique two-lobe profile and transfers that through discrete interpolation and near-extremizer compactness. No inspected stronger source states the zero-mean asymptotic or H1 profile convergence.

## value

PASS

One vanishing moment is a natural algebraic constraint (polynomial factor z−1), and the sharp discrete embedding constant and signed two-lobe rigidity are substantive spectral/Sobolev structure. The result explains a factor-two loss, exhibits nearly sharp finite witnesses, and characterizes near-optimizers rather than relabeling unrestricted bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
