---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The angular dependence of the Hermite STFT matrix coefficients gives diagonalization, and t=π(x²+ξ²) makes the radial integral use dt. The Laguerre square is a Poisson mass times C_q(k;t)^2/(q!t^q), including k<q by the falling-factorial polynomial identity. For u=(k−c)/√c in a compact set, bounded t−c, coefficient extraction from exp(−s√t)(1+s/√t)^k and Stirling give the compact-uniform limit F_q. For no escape, the recurrence bounds t^−q/2|C_q| by a fixed polynomial in 1+r, r=|k−t|/√t. For k≥t/2, Stirling gives a bounded prefactor times exp(−b min(r²,r√t)) for the rescaled mass, by the rate function I(s)=s log s−s+1; for k<t/2 the exp(−bt) bound absorbs the possible √t prefactor. Use r≥(|k−c|−w/2)/√(c+w/2), not a uniformly additive o(1) comparison over all k. The tails and compact convergence give the supremum, every maximizing index, and the converse. Differentiating the three low-order F_q gives the stated constants and sets. At q=1 the compact expansion at the two peaks is F_1(u)+c^−1/2 H(u)+O_w(c^−1), with H(u)=F_1(u)(u³−3u)/6. The density's first two t log derivatives on those bands are O(c^−1/2) and O(c^−1); symmetry therefore makes the midpoint error O_w(c^−1) relative. Near a peak u_0, F_1 drops at least quadratically and H is Lipschitz. Comparing with a nearest lattice point gives |u−u_0|=O_w(c^−1/2) for each band maximizer and its normalized value F_1(u_0)+c^−1/2 H(u_0)+O_w(c^−1). The negative peak's correction wins, including for any integer ties. This supplies the sharp index bound without derivative estimates in the signal degree. The frozen `python3 check_annular_hermite.py` (SymPy and mpmath) reports 160 finite assertions; inspection shows its numerical mode searches are restricted to an index band and do not certify the global tail. The script was not executed.

## originality

FAIL

The separately featured first-window theorem is exactly covered by distinct published record 4e06172f4f4e. For the leading all-fixed-order statement, record 74fee70a2be4 supplies the stronger compact-uniform normalized eigenvalue expansion at every fixed order and a fixed-degree Poisson-tail argument in its order-two application. The same estimate with polynomial degree 2q immediately yields the all-fixed-order no-escape step. The norm and index statements then follow by maximization and lattice approximation, without a further new term or a genuinely different regime. This is mathematical coverage, including proof-level implication for the all-order leading statement; it is not an assertion that the 11/8 catalogue entries were published before the frozen 10/18 package. The matched records are distinct from the input.

## value

PASS

The functional-analytic content is meaningful: it finds the sharp optimal concentration over unbounded mode indices, rather than just the behavior of one index or a disk approximation. The first correction also breaks an otherwise exact limiting tie. That intrinsic utility does not distinguish the result from the specifically overlapping catalogue findings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
