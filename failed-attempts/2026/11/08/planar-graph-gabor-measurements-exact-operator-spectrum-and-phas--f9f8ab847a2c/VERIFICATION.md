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

With N=q², Fourier transforming the output in modulation is unitary and splits the lift by lag h=z−w. On the h band the map is sqrt(N) times translation correlation with k_h(z)=g(z)g(z−h). For a lag with nonzero first coordinate, planarity makes k_h a delta so all N singular values of that band are q. Nonzero vertical lag gives a zero band. At zero lag, the Fourier transform over translations is diagonal up to signs with coefficients q times the character sums of the graph. These sums have magnitudes q at the trivial character, zero at (r,0) for r≠0, and sqrt(q) at (r,s) for s≠0 by expanding the square and using the permutation of differences. This verifies the full spectrum and rank under the actual counting normalization, and the kernel is arbitrary within-fibre off-diagonal matrices plus a diagonal constant on each fibre with constants summing to zero. For ss*−tt* in the kernel, two nonzero cross-fibres force the same fibre support and reciprocal scalars up to phase; a third produces unimodular scalars all equal. In the two-fibre case a nontrivial reciprocal rescaling must act on flat profiles, and preservation of total energy gives the unique unequal-amplitude swap. In the one-fibre case the same support preserves each individual modulus, and a different fibre is possible only with full flat profiles of equal energy. Total energy is measured, so zero is unique. These checks use arbitrary complex signals and any planar f, not just a quadratic prime-field example.

## originality

FAIL

A distinct nonlinear phase-fibre classification as the central contribution is not established. The same-day cubic-chirp record provides necessary and sufficient data which, under a unitary Fourier transform within each block, are exactly the planar-window data when q=p≥5 is prime. This is an equivalence of the measurement fibres, not just a similar two-case description: the other record's proof data imply the one-fibre clause as well, and the spectra agree after window normalization. Its same-day date does not determine priority, and its theorem does not literally cover all odd prime powers or all planar windows. What is left beyond the demonstrably equivalent prime-case normal form is an application to the larger planar family: the requisite band magnitudes are direct outputs of the classical relative-difference-set identities and standard Gabor multiplier, and the nonlinear step then repeats the same block algebra with q instead of p. No materially distinct nonlinear result is established in the frozen finding beyond that extension; this is not a claim of chronological priority or that an earlier paper prints the entire theorem verbatim.

## value

PASS

Independently of priority, identifying exactly what a natural family of relative-difference-set windows can and cannot recover is scientifically useful. The result separates failure of arbitrary-matrix tomography from support-free phase uniqueness on a large class of rank-one signals, and characterizes the exceptional ambiguities rather than just producing a rank defect. The evaluation in terms of omitted matrix directions identifies which signal structure matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
