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

For a fixed full target, surjectivity follows by solving the two-sided first-order recurrence separately on each residue modulo k (both end coefficients are nonzero); each F^t-fiber is an affine translate of ker F^t. On one residue the order-t recurrence has exactly t free consecutive coordinates. Their evaluation dual is the Laurent polynomial quotient by (a+bz)^t: the recurrence annihilates evaluation and the first t monomials are independent. Writing u=z+a/b, zeta=-a/b, and h=N/g=v d with p not dividing d, z^h-zeta^h is u^v times a unit before truncation at u^t. Triangular replacement of powers of z^h by powers of z^h-zeta^h is valid in every characteristic; orders jv<t give independent coordinates and all later powers are zero. Thus each sampled residue class contributes min(s_c,ceil(t/v)); multiplication by the first site's monomial is invertible. Ordinal indices agree on residues iff congruent modulo R=k/g, and their within-class stride is N/g. The affine trace cardinality is therefore as stated. For the individual cylinder converse, if H is the proper kernel trace space, choose w outside H and a configuration with trace P-w. Its F^t-target cannot have a preimage with any given prescribed trace P, since its fiber traces are P-w+H. So no cylinder has full image below the threshold. The largest s_c is ceil(m/R), giving the stated first integer time, also when R>=m or v>=t. Inspected RESULT.md proof steps 1–5 and verify_reach.py/VERIFICATION.md; the 4,326 reported prime-field comparisons are finite support only and the uploaded code was not executed. The proof also handles extension fields.

## originality

PASS

The distinguishing statement is the exact affine trace rank at every integer time for every sampled arithmetic progression of the scalar binomial rule, and the resulting first uniform exactness time. Known kernel-density criteria and indexed two-site, short-support clock-time and three-site laws give qualitative statements or strict subregimes, not a demonstrated dominating theorem. This is a bounded originality judgment, not a priority or publication-order claim.

## value

PASS

An exact obstruction to mixing on sparse cylinders is a natural quantitative invariant left undetermined by qualitative mixing. The result gives all attainable-pattern cardinalities, not merely eventual covering, and shows that with k and m fixed the covering time grows by arbitrarily large factors solely from prime divisibility of the spacing. The proof is elementary but identifies an arithmetic resonance and all its plateaux at sharp integer cutoffs; that information is not a routine restatement of the cited transitivity criteria or examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
