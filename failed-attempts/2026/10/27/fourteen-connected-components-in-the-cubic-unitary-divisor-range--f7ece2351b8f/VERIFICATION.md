---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The Euler factors are 1+p^(−3a) at a present prime. Defant Lemma 2.2 gives p_(j+1)^3<2p_j^3 for j>=10; the decreasing log(1+x)/x then gives w_j<2w_(j+1). Any failure w_j>S_j propagates, whereas the primes in (p_j,2p_j] make S_j/w_j tend to infinity by the prime number theorem. The remaining j=5..9 inequalities are finite. The greedy residual lies between zero and the remaining log-tail under either choice, yielding every point of [1,T] in the squarefree closure; higher exponents cannot enlarge this interval. The bound 1+p^(−3A_p)<=T makes the intervals for exponent 0 and A_p overlap, covering every higher exponent interval, also after scaling by any fixed other factors. Thus the finite union is exact. With common multiplier T on the right, sorted consecutive starting values x_i split components exactly where x_(i+1)/x_i>T. The independent rational replay with Q=2000 verified all five small-prime inequalities, four caps, all 134 consecutive comparisons, and all fourteen table rows and label counts, giving thirteen strict gaps; the common right-end multiplier exceeds 1.

## originality

FAIL

The October 13 Resultary theorem covers the full fourteen-interval closure with exactly the same endpoints, and the October 18 result gives another exact decomposition of the same closure. The new presentation with 135 overlapping labels does not change any maximal component. This is verified mathematical overlap between distinct records, not a claim of dependence or independently established publication priority.

## value

FAIL

An unknown exact component boundary at a natural parameter would answer a meaningful instance of Defant's question. Here both the full range and its maximal endpoint table are already covered. The denser rational interval certificate confirms them, but the numbers of redundant candidate intervals per component depend on the chosen finite representation and do not supply a separate scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
