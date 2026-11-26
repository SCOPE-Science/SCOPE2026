---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The actual Palm identity and covariance formulas are correct. Given that a specified label has no incoming arrow, the remaining n-1 images are independent uniform on the remaining labels and deleting the specified label preserves all cycles. Summing the fixed-label identity gives the size bias and mean. The rooted-forest count gives P(L_m=k)=k(m)_k/m^(k+1), with the k=m case interpreted as the empty forest (determinant 1), and telescoping gives the stated tails. However, the Finding and Proof both assert strict increase of q_{m,k} in m for every fixed k>=2 without a domain restriction. This is false on the declared domain: q_{1,3}=q_{2,3}=0. Strict increase for the comparison q_{m-1,k}<q_{m,k} holds for m>=k, and that is sufficient for all the asserted negative covariances. The failure is of the subsidiary monotonicity assertion as written, not of the Palm or covariance laws.

## originality

FAIL

The primary p-mapping tail theorem already gives the claimed size-biased cyclic-count law by a direct specialization. Conditional on one specified label j having indegree zero, the original n-domain mapping has independent images with weights p_j=0 and p_i=1/(n-1) otherwise. Pitman (2001), Eq. (29), gives the conditional cyclic-count tails for these weights as k! times the kth elementary symmetric polynomial in p, exactly (n-1)_k/(n-1)^k. Those are the size-(n-1) uniform tails obtained by setting all weights equal on n-1 labels. Averaging this identical conditional law over j is exactly Z_n size bias; subtracting the unconditioned tails gives the covariance formula. No earlier verbatim statement of this Palm identity is asserted. The later catalogue overlaps independently give explicit broader coverage, but are not the basis for historical priority.

## value

FAIL

Palm conditioning is a clear explanation for a natural mixed-dependence identity, and strictness of the nontrivial tail covariances is valid. But for this submitted cyclic-count invariant the prior general p-mapping tail theorem already yields the exact biased and unbiased tails by direct choice of weights, and the sign follows at once from the elementary products. The presentation does not supply an independently unknown exact invariant or a further consequence beyond this direct specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
