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

After eliminating the nonzero peripheral diagonal coordinates, the shifted clique block is uniformly symmetric. Normalize the rank-t surviving coupling to I_t plus zeros. The paired block [[U,I],[I,0]] is nonsingular and its inverse has zero clique-to-clique block, so eliminating it leaves the original symmetric restriction on the k−t uncoupled clique directions. This is the needed fact even in characteristic two; no alternating bilinear form is assumed. Rectangular factorization modulo GL_t gives the rank count. Choosing the radical and then an invertible quotient form gives the symmetric rank count. In particular, bordering gives h_d=(1−1/q)h_(d−1)+q^(−1)(1−q^(−(d−1)))h_(d−2) with h_0=1 and h_1=1−1/q: only old radicals of dimension zero or one can contribute to nonsingularity. With dimension one the new column must pair nontrivially with the radical. The recurrence yields the odd-factor product. Nonsingularity then forces s=t and a nonsingular residual form. For critical scaling the difference from (S_m−k)_+ is twice the rectangular defect plus the residual symmetric corank. The first is uniformly tight by a kernel-subspace union bound, the second by the expected number (<1) of nonzero nullvectors, since each fixed nonzero vector can be made the first basis vector and the corresponding column is uniform. The CLT and Slutsky apply. An m^(1/4) band about k has o(1) probability at critical scale, while on S_m<k−m^(1/4) the two rank factors converge uniformly to 1 and h_∞; the strict sides follow by binomial concentration. Independently, python /workspace/reproductions/nullity.py matched the complete spectra for five additional (q,k,m) triples over prime fields by counting kernel vectors, not by replaying uploaded code. This is bounded corroboration, not the all-field or asymptotic proof.

## originality

PASS

The known dense symmetric rank law is an ingredient; preset-zero full-rank bounds for independent entries and graph minimum-rank classifications are not a census for this symmetric allowed-support ensemble. The strongest distinct Resultary overlap is a tridiagonal census with a linear-density CLT, not the split-pattern mixture or its critical window. The supported distinct claim is the exact split-pattern distribution and its fixed-field limits, not a new unrestricted rank formula.

## value

PASS

The all-corank census is an exact invariant of a natural random symmetric pattern. The distinction between scaled corank zero and actual invertibility is substantive: the limiting invertibility includes an independent dense finite-field factor that the atom of the scaled distribution alone cannot determine. The finite formula also gives every rank multiplicity, not only the asymptotic threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
