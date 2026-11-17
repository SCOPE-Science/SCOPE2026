---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For the explicitly specified rooted comb and unweighted parent shift, S^n(S^n)* is diagonal with entries equal to nth-generation descendant counts. A spine vertex j has one continuing spine descendant plus one per branch in A_alpha∩[j,j+n−1], while tooth vertices have one. For beta=1/alpha>1, convexity bounds the maximum branch count by n^alpha+O(1) and j=0 attains that order; n=1 gives norm sqrt2. Increasing branch gaps imply every fixed-n diagonal except finitely many entries is <=2 and infinitely many equal 2, so all positive-power essential norms equal sqrt2. SS*>=I gives a right inverse Q of norm <=1, enabling Neumann-factor surjectivity S−lambda for |lambda|<1; infinitely many disjoint sibling differences give infinite nullity, so the Caradus Rota universality criterion applies. The spectral radius from power norms and inner eigenvalues gives closed unit-disk spectrum. Neumann resolvent sum gives O(epsilon^-1-alpha/2); normalized tooth-ray inputs on ~N^alpha branches in [N,2N) produce >=cN sqrt(N^alpha), proving a matching lower bound. Power-growth exponents distinguish alpha up to similarity. Finite check_comb.py diagnostics are supplemental only.

## originality

PASS

PASS at best of knowledge: Buckley–Seco parent-shift work gives a general descendant-count formula and a universality theorem under disjoint-branch assumption (A4), which this single-spine comb fails; direct surjectivity and infinite kernel are proved here. Older directed-tree weighted shifts and Cesaro-space tree operators provide different operator models and do not deliver this exact unweighted Hilbert-space package of n^(alpha/2) growth, constant essential powers, universal open disk and exact resolvent exponent. The paper could be covered by a yet-unread general sparsely branching shift theorem, noted as risk.

## value

PASS

PASS: The concrete leafless degree<=2 sparse comb shows ordinary operator powers can grow at any exponent alpha/2∈(0,1/2) while every Calkin power has fixed norm sqrt2, and simultaneously obtains the sharp resolvent exponent and Rota universality. This is a motivated structural separation of ordinary/essential power growth and quantitative boundary resolvent behavior, not just a reweighted classical shift example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
