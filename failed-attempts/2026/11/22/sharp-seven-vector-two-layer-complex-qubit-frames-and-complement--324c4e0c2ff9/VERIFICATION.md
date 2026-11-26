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

PASS

The Pauli representation gives projective overlap (1+u·v)/2 and tightness precisely when the Bloch vectors sum to zero. Hence for Z=[U V] the whole Gram matrix is (2N/(N−1))(I−11ᵀ/N), of rank N−1≤6. At N=7, append the normalized constant column to √(3/7)Z. The Gram identity makes the resulting square matrix orthogonal, giving all stated cross- and within-layer column identities and, in reverse, the converse. This is independent of the coordinate construction. Rechecked every explicit example for N=2,…,7 in exact radicals with review-work/frames.py (output review-work/frames.txt): unit rows, zero centroids, full summed Gram, and all three seven-point moment blocks. For real projective qubit lines, doubling the angle gives the analogous coordinates in R², so two layers have rank at most four and N≤5; the displayed pentagon with the second layer at doubled frequency attains five there as well. The numerical frozen verifier is supplementary, not the basis for the universal proof.

## originality

FAIL

The central claimed advances are covered by a direct specialization of established balanced-frame results, not merely by related fusion-frame parameters. Heineken–Morillas–Tarazaga, arXiv:1904.00920v1 (2019), §3.7 and §4.5, give the real spherical 2-design equivalence, the dimension and Gram of the centered balanced complement, equal-norm preservation, and the equivalence with a direct-sum simplex. The end of their §6 explicitly records existence of real balanced unit-norm tight frames of seven points in dimension three, citing Mimura (1990). Their standard construction therefore gives the two three-dimensional layers and exactly the structural splitting of the extremal statement. The six-point case is a direct construction from the same paper's balanced real harmonic coordinates, sharing the one-dimensional alternating mode with equal weights between the layers as shown below. The Bloch lift is the known correspondence, and the upper bound and small sizes were already known or immediate. Not having the same SUNTF terminology or exact coordinate tuple in the prior sources does not make the claimed theorem new. This is a finding of mathematical coverage, not a priority finding about an identical formulation or an attribution claim about specific chosen coordinates.

## value

FAIL

Sharpness at the first complex-versus-real dimension is a worthwhile question, and the explicit coordinates can be useful as exposition. As an independent new result, however, the claimed sharp threshold combines the previously known rank bound with a direct Bloch reformulation of known balanced design feasibility and complement theory; the saturated rigidity is exactly the standard centered simplex split. No new classification of extremizers, distinct geometric constraint, or independently motivated new invariant of the particular explicit pairs is established. No surviving repair of independent scientific value was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
