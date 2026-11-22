---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Reconstructed the component-count identity k(A)=sum_B k_B(A_B)-(|B|-1), block-product factorization and connectivity as product of block-route local events. A cycle of open-edge weights z under random cluster has independent Bernoulli base probabilities p_e=z_e/(q+z_e), with all-open configuration reweighted by q. For two local demands the four terminal-arrangement cases have covariance numerator (R0+q W0)/(q+Z0)^2. Independently enumerated all nonempty failed-arc masks and used symbolic polynomial expansion to verify all four displayed R0 identities and coefficientwise W0>=0; R0>0 for positive arc odds. Strictness for bridges is Bernoulli variance. Product comparison gives global strict iff route intersection, and disjoint supports yield independence. Forest limit z_e=q lambda_e followed by q->0 retains all positive R0 terms and bridge probabilities lambda/(1+lambda). An independent exact rational exhaustive test on a triangle--bridge--triangle cactus verified all 225 ordered nontrivial pair comparisons, including strictness/equality, at q=1/7,1/2,1,3 and the forest law (1125 comparisons). This proves the submitted statement by its symbolic/structural argument; the finite checks corroborate examples only. Assigned eight Git blobs reconstructed tree SHA 90e3a037d357c8ae0b30194dee8383800f8b1527.

## originality

FAIL

Earlier 2026-11-02 all-weight cactus theorem proves the identical random-cluster q>0 and forest covariance inequality under arbitrary positive heterogeneous weights on every finite connected cactus. Its explicit cycle formula SU-RC has strictly positive xw and/or yz terms whenever both nontrivial two-terminal arc partitions exist. Thus strict local positive covariance and the shared-block iff criterion follow immediately using its published block-factorization proof. Earlier 2026-10-12 and 2026-10-25 forest theorems state the exact shared-block strictness/independence criterion verbatim. The new submission's four endpoint cases are a different re-expansion, not a new mathematical result. The motivating 2026-09-30 primary paper states a general conjecture, which does not itself prove the cactus special case; the decisive prior is the published November 2 mathematical proof and its October forest predecessors.

## value

FAIL

The all-positive-weight cactus random-cluster/forest theorem is a mathematically natural valuable invariant, but the entire claimed conclusion is already established by the published Nov 2 all-weight cactus theorem and its coefficientwise positive polynomial, with forest strictness explicitly published on Oct 12 and Oct 25. Rearranging the cycle proof into four terminal-interlacement formulas and rechecking small graphs supplies no separate structural lemma, new boundary, natural invariant, or independent scientific fact. Reproducibility and correctness do not supply novelty or independent value. An unstudied wider-graph extension is not present in this record and cannot rescue the existing theorem by disclaimer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
