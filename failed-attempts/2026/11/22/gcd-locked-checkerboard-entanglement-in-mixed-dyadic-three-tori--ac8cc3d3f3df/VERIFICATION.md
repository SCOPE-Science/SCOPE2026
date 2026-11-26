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

In characteristic two the C_M multiplier is (Z+1)^2/Z on K[Z]/((Z+1)^M), so its j-th kernel has dimension min(2j,M) and it has two zero blocks of size h=M/2. For each twice-odd cycle the local dimension is two; the root 1 has zero multiplier and a nontrivial root gives one size-two block because the derivative is nonzero. A transverse resonance has η=ζ or ζ^{-1}, so there are the identity pair and 2(g−1) nontrivial ordered pairs. The identity gives four J_1 blocks, the others each two J_2 blocks under the square-zero sum. For h a power of two with h≥2, J_h⊞J_2 is two J_h blocks since K[U,V]/(U^h,V²)=K[U+V,V]/((U+V)^h,V²). Nonzero transverse eigenvalues cannot become zero by a sum with a nilpotent longitudinal operator. This yields exactly 16g−8 blocks of size h, not a generalized nullspace of dimension 16g−8. The off-diagonal block form gives rank B=(N−dim ker A)/2 and character orthogonality makes the positive reduced-state eigenvalues equal to 2^{−rank B}. The two equal-volume examples evaluate as claimed. An independent physical-adjacency GF(2) check agreed for (4,6,6), (4,6,10), (8,6,6), and (4,10,10), including all power ranks through h+1, without executing supplied scripts; replay: /workspace/branches/7a6309c0-ea6d-4bfe-8b18-7f8e5c4751e8/record5_independent.py. Those checks are finite, not the proof.

## originality

FAIL

The principal exact invariant is mechanically implied by the published two-adic rectangular parity-torus classification and its explicit dyadic block-sum calculation, together with the standard graph-state cut-rank identity. This is demonstrated implication, not an exact-title match or a verdict based on lack of access. In particular, the frozen record's view that the two-dimensional classification does not yield the result as a direct corollary is not sustained by the comparison below.

## value

FAIL

The checkerboard entropy and its gcd sensitivity are natural quantities, but this narrow exact claim is a mechanical composition of an existing classification with its known dyadic fusion rule, followed by the standard rank-to-entropy translation. The equal-volume example is a parameter substitution once that composition is made. The frozen scope yields no independently valuable remaining theorem beyond that consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
