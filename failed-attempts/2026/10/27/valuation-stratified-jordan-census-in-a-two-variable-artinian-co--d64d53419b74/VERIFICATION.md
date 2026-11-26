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

The claim concerns all elements of the radical, not every element of the ambient algebra. Over R=F_q[y]/(y^n), the kth power of multiplication by f+xg maps (u,v) to (Fu,Gu+Fv), with F=f^k and G=k f^(k-1)g. Let A and H be their valuations capped at n. The first-coordinate image has dimension n-A, and the kernel of that projection within the image is the second-coordinate ideal FR+G ann(F)=y^min(A,H+n-A)R. Thus the rank is 2n-A-min(A,H+n-A). For p|k set H=n; otherwise H=min(n,(k-1)a+b), including f=0 at k=1 via f^0=1. If ka>=n only the lower-left entry can contribute; if ka<n, comparison of H with ka yields the two stated truncated positive parts. This independently checks the boundary cases and the source's Smith-factor computation. The weighted census follows by choosing each leading coefficient and the available later coefficients; its total is q^(2n-1). The entire profile is captured by powers through n since the radical has (n+1)st power zero; rank differences recover block counts. A block of size n+1 requires u^n=n x f^(n-1)g nonzero, equivalent to p not dividing n, a=1 and b=0. In that stratum the rank sequence is the one for (n+1,n-1): the divisibility branch agrees except potentially at k=n, which is excluded from that branch. This also checks n=2 and gives the probability and count in the source. The frozen checker was inspected, not run; the above is an algebraic proof, not inference from its finite experiments.

## originality

FAIL

A distinct indexed Resultary theorem on the identical algebra computes the identical power ranks of the nilpotent part and the complete weighted partition distribution for all elements, including nonhomogeneous elements, across all positive characteristics. Taking scalar part zero, or dividing each block-size profile count by the scalar multiplicity q, exactly recovers the radical census. A fixed reversible translation between block counts and ranks recovers the frozen enumerator; the top partition count likewise follows on all n, including n=2 from the general formula. This establishes mathematical coverage at review, not historical precedence: the broader record is catalogued later and no dependency or priority is inferred from the dates. The delegated wording 'all-element' has been compared against the actual original, which is radical-only.

## value

PASS

An exact census of Jordan types of all nonhomogeneous radical multipliers in this natural complete intersection is scientifically meaningful. The two valuations and characteristic resolve both typical and exceptional elements and give a precise finite-field size of the maximal type beyond its mere existence. This evaluates the mathematical question and result; the same value does not justify accepting a fully covered specialization as distinct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
