---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Every word with A>=2 letters a uniquely has gaps b^(x0)a b^(x1)...a b^(xA). The scattered a b^r a pattern occurs exactly when p=sum(x1..x_(A-1))>=r. The exact count by |w|_(ab)=sum(i x_i) factors over p<r as q^p Gaussian[A+p-2,p] times sum_(v=0)^(B-p) q^(Av). For r=3, the p=0,1 terms contribute 1 in every feasible C, and the p=2 interior indices i<=j give the finite sum h_A(i+j), at most two possible residue lifts. Counting unordered nonzero residue pairs modulo A bounds each fiber by 1+floor(A/2), with equality at C=A when B>=2. Independent brute binary scattered-pattern enumeration tested all C for (A,B)=(3,3),(4,4),(5,3). The infinite parameter formulas follow the gap bijection, not experiments.

## originality

FAIL

The entire submitted all-A,B,r>=3 avoidance Gaussian polynomial, including the nontrivial r=3 five-letter case, is *identical* to a published 2026-10-18 Resultary theorem’s exact polynomial (there called t rather than r). The r=1,2 extensions are immediate from the strictly stronger 2026-11-02 published joint interior-span distribution, which enumerates every p. The new maximum of 1+floor(A/2) is a short residue pair-count corollary of those known r=3 coefficients, not an independent significant result. The claim is mathematically correct, but already covered.

## value

FAIL

Fixed-Parikh-class avoidance is a motivated natural parameter but the exact target distribution and pattern-filtered counts are already published; the small r=3 modular maximum follows straightforwardly from their coefficients and does not supply independently worthwhile new structure. Rephrasing the known Gaussian formula or adding a certificate cannot make this original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
