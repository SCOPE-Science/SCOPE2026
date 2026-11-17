---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: Since q is even, Q=P+N is idempotent iff P^2=P and PN+NP=N. With a canonical decomposition U plus W plus Z of dimensions (r,r,s), N:W->U identity and elsewhere zero, the anticommutator forces P=[[A,B,C],[0,I-A,0],[0,H,K]]. Direct squaring gives A^2=A, K^2=K, AB+BA=CH, AC+CK=C, HA+KH=0. For rank(A)=a and rank(K)=b, the C and H constraints allow opposite/equal eigenspaces respectively and have combined dimension rs; CH is off-diagonal with respect to A, so the B-commutator map has a^2+(r-a)^2 free entries. Gaussian-binomial numbers of projections A,K yield exactly the claimed product-sum H(n,r,b). Reordering to (U,Z,W) makes the idempotent triangular with diagonal A,K,I-A, so both summands have common rank r+b and no other ranks. Direct independent literal enumeration of all n=2,3 matrices over F2 for r=0,1 agrees: n=3,r=1 has eight solutions rank1 and eight rank2; n=3,r=0 has 1,28,28,1. Inspected actual extension-field verification code for F4/F8; it is finite corroboration, not proof of all fields.

## originality

PASS

PASS (best of knowledge, with significant access risk): The 2009 de Seguins Pazzis paper solves existence of two-idempotent sums using Jordan-type criteria and contains no finite-field ordered witness/rank enumeration. A same-day published theorem gives complete rank-one-summand fibers, including the rank-one target subcase 2q^(n-1); this is credited and does NOT imply the unrestricted decomposition ranks of arbitrary square-zero targets. Xu 2015 precisely characterizes when a combination of two idempotents is square-zero; only its abstract was accessible despite arXiv/OA search and authorized Oxford attempt (VPN disconnected), so potential stronger mathematical overlap remains. A general Hall-algebra or structure-constant theorem could also imply the formula.

## value

PASS

PASS: Prescribing a square-zero sum and asking for all ordered decompositions into idempotents is a natural finite-field refinement of a classical existence/classification question. The complete rank distribution for arbitrary nilpotent square-zero target rank, and forced equality of summand ranks, are nontrivial structural/counting facts; inclusion of boundary targets and extension fields makes it a complete natural invariant rather than a narrow arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
