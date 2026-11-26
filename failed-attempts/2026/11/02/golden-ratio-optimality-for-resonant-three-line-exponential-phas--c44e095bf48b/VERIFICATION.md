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

The three real-axis intensities recover |c|²+|d|², |c|²−|d|², and Re(c conjugate(d)) by their even and odd differences; the fourth recovers the imaginary part exactly when sin(πkα)≠0. At zero sine the two choices d=±i with c=1 collide. Any three magnitudes leave a nonzero Hermitian kernel matrix. For spanning evaluation vectors it must be indefinite, and its two rank-one spectral parts give the ambiguity; for nonspanning vectors there is already an invisible coefficient vector. The interference Gram matrix has trace 3 and determinant 2sin²(πkα), so the least singular value is g(∥kα∥) with g(d)/d→π√(2/3). A minimizing index j_N tends to infinity and Nγ_N≥j_N s_{j_N}, while Nγ_N≤Ns_N, giving the stated liminf. For golden-ratio sharpness one can bypass the redundant initial Fibonacci indexing: with α′=−φ and p nearest to qα, |(qα−p)(qα′−p)|=|p²+pq−q²|≥1 and |qα′−p|≤√5q+1/2. This proves the lower sharpness bound; Hurwitz gives the upper bound. Finally the two witness vectors have squared norms 5 and mutual inner-product modulus 4, giving quotient distance √2, while the interference differences have the stated signs and sizes.

## originality

FAIL

The exact spectrum advanced as distinguishing content is a direct specialization of the earlier-indexed exact Gaussian interference spectrum, with identical normalized profiles and row permutation. The headline sharp constant follows from that exact law by small-angle expansion, the elementary running-minimum identity, and sharp Hurwitz. The earlier item need not state the numerical constant or the running-minimum wording to cover its substantive spectral input. The explicit four raw sites and sampled separation are not found verbatim; they are realization details, not an independently supported original spectral or design theorem.

## value

FAIL

A sharp conditioning design for prescribed observations is a worthwhile aim, but here the central optimized invariant is extracted mechanically from the known wider spectrum and classical Hurwitz constant. The four raw samples furnish a clean minimal realization of a two-dimensional lifted system, and the elementary witness illustrates failure near resonance, but neither introduces a new stability invariant or result beyond that routine realization substantial enough to sustain the headline finding. In particular no sharp design or noise guarantee for the raw samples is obtained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
