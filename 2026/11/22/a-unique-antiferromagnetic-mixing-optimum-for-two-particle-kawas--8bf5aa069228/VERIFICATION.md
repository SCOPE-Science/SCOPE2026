---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the two-positive-spin sector of K_{r,r}, a same-shore pair to opposite-shore pair move lowers energy by 4J, so its rate is a and its reverse has rate b=1-a. Let C be the rectangular incidence between same-shore pairs and opposite-shore cells. On functions of the latter cells, CᵀC=E⊗U+U⊗E, with U the r-by-r all-ones matrix and E=(r-2)I+U (the within-shore vertex-by-pair incidence Gram matrix). Its eigenvalues are 4r(r-1), r(r-2), and 0 on the constant, one-coordinate zero-sum, and doubly zero-sum subspaces, respectively. This verifies the positive singular pairs and both null spaces independently of a sector-average reduction. The diagonal exit rates are 2ra and 2(r-1)b. For r>2 the nonconstant positive singular pairs yield the stated quadratic, and the lower root is positive and strictly below both exit rates, hence below all unpaired eigenvalues and the constant-sector nonzero eigenvalue. For r=2 only the constant singular pair remains, yielding min(4a,2b) with its unique cusp at a=1/3. For r>2 differentiating the smaller root gives strict concavity and derivatives of opposite signs at a=0 and a=1/2. The stationarity equation 2g=c_r(1-2a) selects the smaller root t=1/(2r-1+sqrt(r(r-2))) for t=1-2a, so the antiferromagnetic logistic map yields the stated unique positive beta optimum. The gap decreases for a>1/2 (ferromagnet), and g(1/2)=r/2. The peak gain is r/[2(2r-1+sqrt(r(r-2)))(r-1+sqrt(r(r-2)))], reproducing the stated 1/(12r) asymptotic; t asymptotics yield the inverse-temperature constant. Nine independent exact full characteristic-polynomial comparisons agree for r=2,3,4 and a=1/3,1/2,2/3.

## originality

PASS

The exact constant-rate exclusion spectrum for complete bipartite graphs is prior coverage of the baseline. The same-day star result is a close analogue of the antiferromagnetic phenomenon and the incidence technique, but not an exact biclique gap or optimum. The supported contribution is the interaction-dependent full-chain classification in this specific nontrivial biclique sector, including selection of the active spectral branch, the cusp-to-smooth distinction and the exact optimizing temperature.

## value

PASS

Two particles are the first sector where their arrangement on these two shores changes the exchange energy; balanced complete bipartite graphs give a natural symmetric test of interaction-dependent local relaxation. The exact result identifies a universal nonmonotone temperature response and which eigenmodes create it, including an exceptional mode crossing at r=2. The absolute gain is small for large r, but the structural classification and exact scaling of both gain and location give reusable benchmarks for spectral analysis, rather than inferring significance from a small numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
