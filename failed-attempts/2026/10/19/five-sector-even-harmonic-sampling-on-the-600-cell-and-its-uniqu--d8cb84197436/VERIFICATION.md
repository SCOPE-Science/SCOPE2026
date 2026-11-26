---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The degree-ell harmonic space comprises the matrix coefficients of Sym^ell(C^2); Schur orthogonality for Haar probability introduces the factor ell+1 in the kernel. Even ell descends to A5 regardless of antipodal representative. The class weights 1,15,20,12,12 and half-angles 0, pi/2, pi/3, pi/5, 2pi/5 give the stated restricted character. Schur orthogonality on the unweighted target gives sector dimension d_rho^2 and convolution scalar 60(ell+1)m_rho/d_rho. The kernel projectors and pseudoinverse correctly give the range and the unique minimum-norm interpolant. The nonidentity characters repeat under ell+60 and the identity increment adds one regular character, giving the permanent full rank from 60. An independent exact Chebyshev recurrence in Z[phi], `python3 /workspace/branches/replay_2_3.py`, gives both rank tables, first rank 60 at 20 and last deficiency at 58; the latter has multiplicities (0,3,3,4,5). Rank 59 loses only the trivial sector. Equal remaining sector eigenvalues make the restricted character constant away from the identity; by the angle residues this is possible only in degree 0 or 58 modulo 60. Only 58 is rank 59, and its character is 59 at the identity and -1 elsewhere, making G=3540 I-59*11*. Bounded nonidentity character values prove the stated conditioning estimate; the nonzero entry at perpendicular lines excludes exact full orthogonality. The frozen checker was inspected, not executed.

## originality

FAIL

A distinct indexed record, 13f75a70c530, determines the exact-degree Gram spectrum and ranks on all 120 vertices for both parities, including the equal 59 positive values at 58. Even-degree antipodal compression with the source-norm rescaling yields this frozen spectrum, including the five sectors, and the later inspected parity-sharp record also gives the conditioning rate. The rank-59 uniqueness and reconstruction statements then follow mechanically. This is a finding of demonstrable equivalent coverage, not a claim that the later-dated catalogue labels establish historical precedence. The unavailable 1974 text is not the basis for failure.

## value

FAIL

Exact-degree sampling on this configuration is well motivated and the analysis is correct; the assessed exact invariant and rank/tightness cutoff are nevertheless mechanically available from a stronger indexed exact spectrum on the same vertices. Reexpressing it with five character rows and the normalization appropriate for interpolation is useful exposition, but no independently valuable new finding survives this coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
