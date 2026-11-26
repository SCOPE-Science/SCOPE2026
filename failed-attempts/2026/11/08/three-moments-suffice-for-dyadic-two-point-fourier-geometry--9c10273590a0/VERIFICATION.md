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

At fixed s=u+v the pair product w controls p₂=s²−2w and p₃=s³−3sw. For odd s the cubic fixes w in R; an even w gives two simple roots modulo 2 which lift uniquely, while an odd w gives none. For even s the quadratic fixes w modulo Q=N/2 and that is sufficient for the cubic; (u−s/2)²≡(s/2)²−w mod Q has two R lifts per root and is independent of the chosen half. A square of valuation 2j<m has an odd square factor mod 2^(m−2j); the odd squaring kernel has sizes 1,2,4 in exponents 1,2,≥3, as follows by factoring x²−1 and noting that consecutive even numbers x−1,x+1 have one valuation exactly 1 for odd x. There are 2^j lifts per odd root and 2^floor(m/2) roots at zero. Summing the resulting strata gives the two closed image sizes. For the energy, an odd s contributes 2N and an even s contributes 2(k−1)N: at k≥3 the latter is 32 times the zero-product count modulo 2^(k−3), including modulus 1, and for k=2 both factors must be even, giving 2N directly. This sums to kN², with normalized Fourier orthogonality giving exactly that number. The recurrence for pⱼ preserves the even-s invariance under changing w by Q because every pⱼ is even. The two pairs (0,1) and (Q,1−Q) agree through degree two and split by Q at degree three, including k=2. The independent script compares the whole predicted support and multiplicities to unordered enumeration weighted to count ordered inputs, checks the valuation histogram and aggregates for k=2 through 10 and higher moments through degree 9 for k≤8. Replay: python3 /workspace/reproductions/frozen_checks.py 1. The universal statements rely on the proof, not the finite run.

## originality

FAIL

A distinct indexed record establishes exactly the same three-moment closure, least initial degree and dyadic energy in an all-moduli theorem. Its proof also classifies when all pairs with a given sum collide, by product equality in R for odd sums and modulo N/2 for even sums. The frozen pointwise refinements are not printed in that record, but follow from that collision classification by the quadratic with given sum and product: for odd s ordinary simple lifting gives two roots; for even s completing the square gives the ordinary dyadic square-root fibers. Counting the standard valuation strata then gives the parity-dependent support. This is a judgment about demonstrable coverage and routine implications, not which same-day entry was first.

## value

FAIL

The full distribution is a meaningful invariant of a natural Fourier surface, and the frozen account is a usable explicit calculation. As a contribution beyond the distinct all-moduli energy and closure analysis, however, it only converts the known sum/product collision classes to standard dyadic square-root counts and sums them. It does not supply an independently unknown arithmetic phenomenon or a result about weighted extension beyond that mechanical specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
