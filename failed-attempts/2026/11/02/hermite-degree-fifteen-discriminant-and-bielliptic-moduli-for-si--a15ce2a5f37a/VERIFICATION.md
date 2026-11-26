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

I checked the unambiguous set equality stated immediately after the product formula: the image is the intersection of H=0 with the squarefree sextics. The normal form pairs the roots into three quadratic differences summing to zero. Conversely, a vanishing pairing determinant has rank two with all relation coefficients nonzero by disjointness of the pairs. Scaling by this relation reconstructs a split cubic with zero root sum. At each of the six roots it has exactly one simple difference zero and c4 nonzero (a nonzero double root and a distinct third root in the depressed local cubic), giving I2; the degree-one fundamental bundle gives a rational elliptic surface. The product has degree 15 in each root form, and the permutation sign character is trivial by a nonvanishing specialization with two roots equal. It descends to coefficient degree 15, with the claimed GL2 weight. The involution configurations are irreducible, there is no discriminant component, and the witnessed unique zero factor has nonzero derivative in a root coordinate. The pencil is base-point-free and of degree two. Conversely, a nonhyperelliptic order-two lift cannot fix a branch point downstairs: a local parameter at that branch point would have a lift with derivative squaring to −1, not +1. Thus the descended involution exchanges three pairs. The cross-ratio check at {±1,±2,±3} gives exactly identity and negation, verifying generic pairing uniqueness on the irreducible locus. Common scaling and the S3 relabeling do not change the isomorphism class of the split Weierstrass surface, giving the generic inverse. Independent exact cross-ratio replay: `python3 /workspace/review_evidence/check_3.py`.

## originality

FAIL

Substantial prior implication is established, not merely plausible overlap or a same-title match. Combining the published split-cubic classification with the older exact linear-dependence criterion makes the squarefree surface-image equivalence a direct corollary. The classical invariant/degree and generic uniqueness on the bielliptic side were also already available. The determinant product and cubic reparametrization are explicit realizations of this implication, not a distinct new classification in the frozen scope.

## value

FAIL

Question 25 gives a real motivation and the synthesis is useful exposition. As a distinct research finding, however, the narrow identification and invariant are mechanically supplied by the earlier parametrization, exact pairing test and classical involution hypersurface. Writing determinants for the old test and inverting a linear difference map do not give an additional unknown exact fact. The frozen result expressly leaves the exceptional moduli fibers and degenerations out of scope; the later two-branch theorem is not a remainder proved here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
