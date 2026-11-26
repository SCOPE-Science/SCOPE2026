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

Reconstructed the result for iid uniform q-ary words with replacement, excluding distance zero. A common neighbor of a distance-one pair either uses a new distinguishing value with zero or one extra change, or uses an endpoint value with exactly one extra change. For distance two, the choices are two mixed endpoint combinations, one or two new values, or a mixed endpoint combination with one extra change. These give exactly c1 and c2. Conditional on the two words, each third word supplies an iid four-outcome trial; conditioning further only on the edge mixes the two powers with the stated weights. Both single-coordinate means stay p, so no between-type covariance term is missing. Forest independence follows by conditional leaf integration. Of distinct triples of edges only triangles contribute, and pairwise independence annihilates terms with exactly one repetition; the triangle centered moment is pΔ. Independently checked S1, S2, S3, binary S4, the two shifted base polynomials and the monotonicity certificate described below. For the cumulant sign, adding a Hamming coordinate changes p by (b/q)(Pr{H=0}−Pr{H=2}) for H∼Bin(d,b/q); this is negative for d≥3. In negative-Δ regimes p≥1/2, including equality at (2,1), and in positive-Δ regimes p≤1/2 except at (4,3). There p=9/16, Δ=5/256 and direct substitution gives the claimed 5n−17 factor. This checks d=1, n=3 and all strict/no-zero assertions.

## originality

PASS

On the sources inspected, the original content is the sharp specialization across both alphabet size and dimension, with the exact finite-sample sign exception. The general convolution/signed-triangle identity applies to every q through (Z/qZ)^d, not merely to the binary subcase; it and the standard intersection-number method are not new. The conditional PGF is an elementary consequence of those intersection counts and is not the main basis for this judgment.

## value

PASS

The first natural non-nearest-neighbor Hamming connection set already gives three distinct onset dimensions across alphabets. The exact covariance and its sign distinguish dependence hidden by pairwise independence; the lone finite-sample skewness reversal shows why triangle sign is not the entire edge-count story. This is a complete reusable classification of a canonical radius-two model, not a small numerical slice or a claim to have invented signed triangles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
