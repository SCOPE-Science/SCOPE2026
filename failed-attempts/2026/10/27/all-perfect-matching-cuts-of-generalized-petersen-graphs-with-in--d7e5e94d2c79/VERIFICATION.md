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

The outer cut indicators p have no adjacent ones and force the spoke discrepancy s_i=1-p_(i-1)-p_i. Substituting b_i=a_i XOR s_i in b_i XOR b_(i+2) cancels the interior p terms and gives p_(i-1) XOR p_(i+2). The inner equation forces p_(i-3)=p_(i+2) for each admissible adjacent pair: if both p's are zero, both outer bits must also be zero; otherwise the inner equation reduces to equality of those outer bits. Thus p has period five; when 5 does not divide n, gcd(n,5)=1 forces p=0. On a five-cycle a singleton 1 violates the zero-pair rule; the five rotations of (1,0,1,0,0) each meet it (the only adjacent zero pair is between its two trailing zeros). The empty and two-one patterns have even parity, so integration around the ring closes and leaves only a global colour flip. Reconstruction gives the stated template up to shift and complement, also at n=5. For a connected graph the crossing-edge indicators determine all colours once one vertex colour is fixed. Thus the cut enumeration is precisely half the labelled count.

## originality

FAIL

The entire finding is already covered in the distinct indexed companion SCOPE-20261027-d218a251c534 under its minimum 1-limited dominating set formulation. This is mathematical equivalence and same-day corpus duplication, not a claim that either record historically preceded the other. The alternative proof does not leave an independent new census or invariant.

## value

FAIL

A periodic classification of exact matching cuts would be a worthwhile graph-theoretic census in isolation, and the short intrinsic argument is useful corroboration. Here the exact census is already supplied by a distinct equivalent record and the edge count is its immediate quotient. The outer-bit restatement does not identify an independent surviving result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
