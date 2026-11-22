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

Each nonzero decomposable tensor is on one of (q+1)^3 projective Segre points, each scalar class summed by character orthogonality. A two-slice representation gives F(T)=q(q B(T)-q-2), with B the number of hyperbolic quadric Q=P1xP1 points in the projective common kernel. Rank-two slice pairs correspond to all P3 lines with multiplicity |GL2(q)|; the quadric has 2(q+1) contained generators, (q+1)^2(q-1) tangents, q^2(q+1)^2/2 secants and q^2(q-1)^2/2 external lines. Rank-one slices correspond to tangent or non-tangent hyperplane sections, and rank zero contributes T=0; these disjoint cases sum to q^8. The six signed values are q(qB-q-2), hence only B=0 and B=1 negative, and B=2 vanishes only at q=2. Fourier inversion gives the exact convolution ℓ1 and ℓ∞ norms by the absolute kernel sum. The general all-prime-power conclusion follows combinatorial counting, not the finite q tests. Independently checked q=2 by complete 256-input integer Walsh transform: 108 zeros and norm 55/16.

## originality

PASS

The general tensor-Cayley character-incidence reduction is already in Byrne–François (2026), and q=2 rank Fourier shell information also overlaps prior computations. The claimed increment is the evaluated all-q six-row line/hyperplane multiplicity table, the exact harmonic endpoint norm and q=2-only cancellation transition. Checked general theorem statements did not explicitly supply these exact evaluations; risk remains that an unexamined specialized table or a direct published corollary already computes them.

## value

PASS

The natural smallest nontrivial three-factor rank-one tensor cone is a finite-field tensor/Cayley graph frequency set. Its full all-q spectrum, exceptional cancellation transition and sharp norm quantify arithmetic harmonic projection amplification and are useful exact invariants beyond the general spectral-reduction identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
