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

For the 12 regular icosahedron vertices and normalized 9-dimensional spherical harmonics up to degree 2, exact fourth moments give U*U=I_9. The row projection kernel is (1+3t+5P_2(t))/12, giving diagonal 3/4, antipodal 1/4, and all other off-diagonal ±1/(4 sqrt5). After erasing E the retained Gram matrix is I_9−U_E*U_E, whose nonunit eigenvalues are one minus those of the |E|×|E| kernel. Explicit 1-, 2- and 3-point matrix diagonalizations give the claimed spectra; an antipodal pair forces eigenvalue one in the erased kernel. For any |E|>=4 there are <=8 retained observations, so rank 9 is impossible. Counting antipodal pairs gives 1,12,60,160 successful masks. Six vertex axes give an equiangular tight frame with Seidel spectrum ±sqrt5 threefold, hence trace(S^3)=0 and exactly 10 positive and 10 negative axis triples, or 80 each among 160 signed triples. The minimum good squared singular value is 1/4−1/(2 sqrt5), attained at 80 positive triples. Independently built the 12×9 numerical frame and directly checked the full small-erasure kernel/eigenvalue census (299 masks), all 233 good masks and the 80/80 split; the exact 5-design and Seidel arguments prove this exhaustively.

## originality

PASS

PASS under bounded literature comparison: spherical designs, random harmonic recovery and conditioning are prior frameworks, but inspected sources do not imply the exact icosahedral all-mask rank/spectrum/80-witness classification. A related published cuboctahedral quadratic-harmonic erasure classification concerns a different design and has different underlying Gram kernel, not a theorem dominating this icosahedral instance.

## value

PASS

Deterministic erasure resilience and exact worst-case stability of a natural tight icosahedral harmonic sampler is a meaningful complete finite classification: all 4096 masks are decided by a simple antipodal obstruction, the positive singular spectra are explicit, and sharp worst-case masks are classified. It is not just an arbitrary table or routine single instance; the symmetry and frame structure explain the boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
