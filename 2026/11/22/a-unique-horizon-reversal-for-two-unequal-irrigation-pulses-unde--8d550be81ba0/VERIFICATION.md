---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the empty scalar store and T ≥ τ, integration of each exponentially decaying segment gives the stated log of a positive rational function. For an independent cross-multiplication, put y = exp(−kτ), z = exp(−kT), P = (K+A)(K+Ay+B)(K+By), Q = (K+B)(K+By+A)(K+Ay). The sign numerator is K(P−Q)+(z/y)[(By+A)P−(Ay+B)Q]. Grouping the first and third factors gives P−Q = ABy(A−B)(y−1); weighting P and Q gives the linear coefficient before division by y as K(A−B)(1−y)[(K+B+Ay)(K+By+A)+ABy]. The bracket expands to D in the record. Thus the only sign-changing factor is zD−ABy². Since D−ABy = (K+A+B)(K+y(A+B))+AB(1−y)² > 0, its unique zero is strictly between 0 and y; z decreases continuously from y to 0. This gives the full strict ordering, the exact tie and T*>τ. After τ, the AB state minus the BA state is (A−B)(y−1)exp(−k(t−τ))<0, so the instantaneous and cumulative comparisons are correctly distinguished. Substitution of A=2, B=K=k=1 and y=1/2 gives D=23/2 and T*=log 23; the rational score ratios follow from the integral formula. Replay: frozen RESULT.md lines 25–83 and supporting verify.py lines 8–47 (inspected, not executed); quadrature is supplementary, not a universal certificate. Equal pulses or a zero gap do not give the strict result. No physical uptake or empirical validation is implied.

## originality

PASS

The exact model and full score formula are already present in two closely related same-day records; no originality is assigned to either. On inspected evidence the distinct claim is the global comparison of two permutations at a fixed gap as the horizon varies. The optimum-delay classifications do not prove that comparison; cancellation in the swapped-order difference and strict feasibility of its horizon root are additional mathematical steps. Same-day indexing does not establish publication order. The conclusion is bounded to the actual comparison and is not a priority guarantee.

## value

PASS

Changing which of two fixed doses goes first while preserving doses and slots is a motivated decision distinct from moving the second slot. The all-parameter crossing explains why uniformly superior instantaneous response after the second dose can give the opposite ranking over finite cumulative windows and identifies precisely when that ends. The result is a benchmark of the scalar saturating model, not a claim about crop yield or actual optimized irrigation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
