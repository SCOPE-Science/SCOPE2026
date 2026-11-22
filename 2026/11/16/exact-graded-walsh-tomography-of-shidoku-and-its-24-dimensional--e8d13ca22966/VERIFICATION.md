---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Independently generated all 288 4x4 Sudoku boards from allowed permutations with row/column/2x2-block constraints. The monomial Gram identity K_d(u,v)=sum_{j<=d} binom(a(u,v),j), with a the number of identical cell-symbol placements, holds because each common placement admits exactly binom(a,j) conjunctions; Walsh and monomial degree filtrations coincide by (-1)^x=1-2x. Independent modular Gaussian elimination on the 288x288 integer Gram matrices over both p=1009 and p=10007 gave lower bounds (1,25,151,264,288). To certify *rational upper* bounds, reconstructed exact integer null projectors independently (without reading the supplied compressed binary) from approximate eigenspaces as candidates, then rounded and checked every matrix identity in int64 exact arithmetic: for d=1,2,3 with scales 288,2880,2880 and kernel dimensions 263,137,24, each X is symmetric, X^2=sX, K_d X=0 and trace X=s*(288-r_d). All exact products had zero residual and entries fit signed int16/int64. This proves rational nullities at least these values; paired with modular lower bounds it proves the exact real ranks. Since the constant feature belongs to E_0, nonzero degree-three null vectors have total mass zero, and epsilon perturbations of the uniform strictly positive law supply different positive laws with identical low-degree marginals; degree-four full rank proves uniqueness.

## originality

PASS

Best-of-knowledge PASS with a substantive historical risk. Arnold–Lucas–Taalman give the standard 288 Shidoku solutions and 64-variable ideal (not new here), and earlier 25,728 unique four-clue sets establish an existence-level upper endpoint; neither by itself specifies quadratic rank 151 nor 24-dimensional cubic marginal ambiguity. Fontana–Rogantin 2009 Indicator function and sudoku designs studies exactly Sudoku indicator polynomials and a CoCoA treatment of the 4x4 instance. The full text was inaccessible (institutional VPN disconnected) and the available abstract does not resolve whether the exact degree-filtered ranks are hidden there; document this risk, not automatically fail originality without a decisive implication.

## value

PASS

Low-degree identifiability of probability laws on a natural 288-point combinatorial design is an exact, nontrivial statistical tomography invariant. The 24-dimensional cubic blind space and sharp universal fourth-degree sufficiency quantify an explicit information gap, unlike the known grid count or existence of a single uniquely identifying four-clue set. A complete natural finite degree hierarchy can be valuable without extending to 9x9 Sudoku.

The dated certificate retains the supplied scientific assessment, sources and limitations.
