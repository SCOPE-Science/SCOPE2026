---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Factor the Fourier transform as product (1+exp(-2pi i at)), etc. Its zeros are three pairwise disjoint odd half-lattices; two edges with the same color at a vertex yield an even-integral difference that is in none, so every orthogonality clique is properly 3-edge-colored. Every triangle must use all three colors and gives odd xA-yB-zC=0; a unique primitive integer relation permits such odd coefficients iff all entries odd. K4 uniquely 3-edge-colors by opposite-edge matchings, and comparing integer multiples of the same rank-two primitive relation in its 3 triangles forces k=l=-k=0, contradicting odd edge coefficients. The rank-three case precludes triangles. For A=1+sqrt2, B=sqrt2, C=1, relation A-B-C=0; a=-1+sqrt2,b=sqrt2/2,c=1 yield 8 distinct subset sums by coefficient comparison over Q(sqrt2). Checker computes only that witness, not all families. No assumptions on irrationality have been omitted.

## originality

PASS

No full theorem with the precise primitive odd reciprocal relation and universal clique maximum 3 was identified in accessible primary material. Most related convolution theorem requires a subgroup Fourier-zero set, which fails; a plausible inaccessible full manuscript is kept as a risk.

## value

PASS

The maximum cardinality and full 3-clique geometry for the natural finite 3-Bernoulli convolution provide a sharp, structurally motivated non-spectral partial-orthogonality result. The unexpectedly rigid odd-parity integer relation and explicit eight-atom witness are meaningful beyond restating Fourier zeros. No assertion of new general finite-frame theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
