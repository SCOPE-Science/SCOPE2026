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

Independent coordinate rotations reduce each pair to z_j+ν_j z_j^-1 where ν_j=a_j b_j. Exact fourth-power multinomial Fourier expansion, followed by Parseval, has only zero-sum phase-exponent types e_i-e_j, 2e_i-2e_j, 2e_i-e_j-e_k and e_i+e_j-e_k-e_l. The coefficients of these types (1152d²-2592d+1632,36,144,576) combine into C_d+A_d|S|²+36|2S²-T|², with A_d=96(12d²-33d+26)>0, C_d=2d(192d³-864d²+1604d-1155). Thus min C_d iff S=T=0; d-th roots give witnesses for every d≥4. Positive phase coefficients give max attained exactly for all equal ν_j. For d=4,5, Newton identities and unit-root conjugacy force all minimizing ν_j to rotated regular d-gons. Binary T=d cannot cancel; ternary S=T=0 iff 3|d; quaternary iff 4|d; for d4,5 q-th-root coefficient alphabets attain iff d|q, with q^(d+1)(d-1)! ordered arrays. Sampling orders N_j≥9 avoid collisions among P^4 spatial frequencies. Independently computed exact moment by grouping P^4 Fourier coefficients for selected d=4,5 vectors: 30376 at (1,-1,1,-1), 29800 at (1,-1,i,-i), and aligned maximum 190120 for d4 and 551950 for d5; matched the closed formula. The all-d proof relies on the complete exponent-type enumeration rather than checking d≤5.

## originality

PASS

The published d=3 octahedral sum-of-squares identity and minimizers are credited. It does not cover all d≥4 or rigid d4/5 polygons, ternary/quaternary divisibility rules and q-array counts. Golay complementary arrays are multiple jointly cancelling arrays, not a sharp eighth moment of this single signed-coordinate aperture.

## value

PASS

A natural harmonic-analysis design objective—the eighth moment on a 2d-frequency antipodal aperture—has an all-dimensional exact positive-deficit law and a complete small-dimensional minimizer/alphabet classification. The precise obstruction from both power sums changes phase design beyond lower moments, with exact attainable performance bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
