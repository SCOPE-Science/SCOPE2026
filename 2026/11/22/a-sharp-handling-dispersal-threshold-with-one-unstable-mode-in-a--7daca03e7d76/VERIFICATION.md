---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In Bisi et al.'s isotropic model (Remark 7), β=δ=1 gives the four stated population fractions. Summing the two separate competition squares gives x²(1+y²)/(1+y)², and weighting the fractions by the four listed mobilities gives the two displayed flux potentials; all ecological coefficients are strictly positive. At (1,1) the reaction vanishes, with J entries 1/150, −151/300, 1/50, −1/100, and flux derivative D entries 1, −99/200, 2w/9−1/450, 2w/9+7/900. Both trace and determinant of D are positive. The Neumann Laplacian on (0,2π) has q=n²/4 with simple nonconstant harmonics. The matrix J−qD has strictly negative trace −[3+(907+200w)q]/900 and determinant P_w(q)=[601q²+105q+900+wq(29900q−10200)]/90000. The decomposition independently proves positivity for every q≥1 and w>0; at q=0 the determinant is 1/100. At q=1/4 it is (15421−10900w)/1440000. Therefore the first harmonic alone passes from stable to one simple zero and then to one positive real eigenvalue, with negative companion at and above the crossing. At w=893/200 the two diagonal entries of D are 1 and the determinant of the first modal matrix is −4433/192000. With cross terms deleted, D=I and J−qI shifts both eigenvalues of the stable J to the left. The evidence establishes linear spectral classification on this habitat only. I inspected the frozen verification and rational dual-number script without executing it; the positivity decomposition is an all-mode check independent of the script's finite cases.

## originality

PASS

The ecological closure, cross-diffusion mechanism, and general modal trace–determinant test are prior. The additional result is a positive-parameter, exact first-mode threshold along a whole one-mobility family in this separate-competition model, including the equal-effective-diagonal comparison; no exact covering result was established. The inaccessible 2019 full text remains a material but not decisive priority risk.

## value

PASS

Handling diffusivity is an independently adjustable movement parameter in the underlying model. The exact threshold and the separation of the entire remaining Neumann spectrum give a controlled example of how only that mobility triggers a linear instability. The equal-diagonal comparison gives a concrete failure of a diagonal-contrast diagnostic in the same family. The constants are a constructed witness, not a prediction of nonlinear patterns or an empirical calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
