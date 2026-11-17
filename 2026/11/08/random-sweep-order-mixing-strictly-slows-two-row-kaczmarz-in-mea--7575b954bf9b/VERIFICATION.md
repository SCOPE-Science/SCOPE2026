---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For unit line directions with 0<c<1, full sweeps are rank-one F=cvuᵀ and R=cuvᵀ. Repeating one order yields squared contraction c⁴ after the initial step, switching gives c². Tracking squared-error mass by last sweep produces the exact positive 2×2 transfer K=[[pc⁴,pc²],[(1−p)c²,(1−p)c⁴]], trace c⁴ and determinant −p(1−p)c⁴(1−c⁴). Its Perron root is [c⁴+sqrt(c⁸+4p(1−p)c⁴(1−c⁴))]/2, strictly >c⁴ for 0<p<1 and maximal only at p=1/2. From positive left/right Perron vectors and u,v spanning R², this is the sharp expected-squared-error factor for every nonzero deterministic start. For fair p, row sums give exact finite-n formula. Independent Fraction arithmetic explicitly enumerated 2^n orientation words through n=5 at c=3/5, p=2/5, start (1,2) and agrees with transfer for each n. Orthogonal c=0, equal-line c=1 and p endpoints are not misrepresented.

## originality

PASS

The published October 18 four-way Kaczmarz shuffling theorem already gives the fair IID-per-epoch two-row factor c^{2t}[(1+c²)/2]^{t−1} under isotropic initialization and compares it with fixed repeated order. Thus the fair slowdown observation is prior coverage; the current result adds a complete bias-dependent Perron rate for arbitrary deterministic initial errors, the unique fair worst-bias classification and strict degradation for every p∈(0,1). These are not in the inspected earlier four-way theorem (which assumes uniform random permutations), nor in independent-row sampling theory. Remaining prior specialist two-projection random products are a risk.

## value

PASS

Order randomization is a central design choice for Kaczmarz sweeps, and an exact all-bias phase-free classification on the first nontrivial consistent system is a motivated invariant: every mixed sweep law strictly loses contraction, with a divergence of relative slowdown as lines approach orthogonality. Although part of the fair fact was known under isotropic random initialization, its sharp law for arbitrary bias and every deterministic initial vector is distinct and potentially useful for analyzing/choosing sweep policies; no claims about larger systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
