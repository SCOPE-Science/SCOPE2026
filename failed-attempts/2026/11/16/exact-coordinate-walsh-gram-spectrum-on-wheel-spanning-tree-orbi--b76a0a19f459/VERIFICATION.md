---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Reconstructed weighted matrix-tree transfer-current matrix K=E^T(3I-S-S^-1)^-1 E, Cov(I_e,I_f)=delta_ef K_ee-K_ef^2, and G=4Cov(I)+Echi Echi^T. Cyclic Green kernel g_j=(rho^j+rho^(n-j))/(sqrt5(1-rho^n)) yields finite Fourier block diagonalization, one forced null direction from sum chi_e=0, and scalar values from geometric series. Direct independent complete tree subset enumeration for n=3..8 gave tree counts 16,45,121,320,841,2205; numerical eigenvalue lists matched formulas within 1.4e-15 (support only, not universal proof). Positive small modes scale 4*pi^2/(sqrt5*n^2), noncentered mean mode contributes 2n(1-2/sqrt5)^2, giving cubic condition ratio; n=3 extra multiplicity checked. No fabricated infinite proof from finite data.

## originality

FAIL

A published 2026-11-08 SCOPE paper already gives the exact finite 2-by-2 Fourier block spectrum of the SAME uniform wheel spanning-tree indicator covariance for every rim size, including the Green kernel and all pair inclusion probabilities. The assigned coordinate Walsh Gram matrix is exactly G=4C+(1-2p)(1-2p)^T. On wheels p_e is already explicitly K_ee in that earlier proof, so its two constant mean blocks and all nonconstant Gram Fourier blocks are directly determined. The new n^3 condition asymptotic follows from that paper’s lambda_min(C)~pi^2/(sqrt5*n^2), mean spoke-minus-rim vector of norm squared 2n(1-2/sqrt5)^2, and the rank-one update; all-n closed forms simplify earlier finite Fourier-block entries. Thus the single final claim is already mathematically covered as an elementary consequence of the stronger earlier complete wheel-covariance description even though the word Walsh and the cubic coefficient do not appear there. Mere vocabulary/normalization change cannot establish O.

## value

FAIL

Sampling Walsh characters of a natural tree orbit is mathematically motivated, and the proof is correct. However the exact Gram operator is just four times the earlier completely evaluated same-object covariance plus its explicit rank-one mean term. The principal n^3 growth comes mechanically from the prior n^-2 centered gap and the elementary O(n) mean contribution. This re-expression is not a substantive new mathematical gap independent of the already available finite covariance spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
