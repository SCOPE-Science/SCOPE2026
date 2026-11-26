---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The original antipodal-pair claim at r=1/2, a=−1/4, c=1 is false if it refers to positivity of the whole pair: 4/5 tests only the antisymmetric vector. For u=b cos(2x), the eigenvalues of the antipodal Gram matrix are (p+q)(a+(c+u)/μ) and (p−q)(a+μ(c+u)), with p=P_r(0), q=P_r(π). Requiring both yields |b|≤min(c+μa,c+a/μ)=11/16 in the example. In particular b=4/5 and x=π/2 give eigenvalue −3/10. The complete corrected result derives both eigenvalues; 67/100 still satisfies every antipodal test and violates the full PSD bound. Independent exact evaluation recovers the indicated eight-site energy −1217/1275 and minimum diagonal 6/25. The main theorem survives unchanged: direct Fourier expansion gives even/odd Jacobi sectors, and approximating trigonometric-polynomial densities by atomic measures proves necessity on all weighted finitely supported Fourier vectors. The repaired odd-sector argument uses a positive eigenvector supported with geometric tails of ratio r and the sum-of-squares ground-state identity; sign alternation gives the opposite extremum. The even-sector bulk bottom is h−|b|; an attractive defect −cδ yields h−sqrt(b²+c²δ²) by matching the unique decaying solution on the two tails and the origin, and a nonattractive defect cannot lower the bottom. The diagonal b=0 case gives the same formula. At odd equality an antipodal antisymmetric vector is null (or the b=h=0 kernel is constant). At strict odd margin a possible even zero mode has ratio |t|<r per step of two indices, so its unweighted even Fourier sequence tends to zero despite F_0≠0. Cesàro orthogonality rules this out for finite atomic measures, including the b=0 constant-Fourier-mode nullspace. Fourier uniqueness excludes the zero sequence for a nonzero distinct-site vector. This checks the repaired theorem, example, and endpoints without a finite-to-infinite extrapolation.

## originality

PASS

The repaired result credits two exact overlaps: the earlier c=0 sum-angle harmonic model and the same-day b=0 stationary finite-knot classification. The latter is exact present coverage of the stationary slice, not evidence of any within-day ordering. The supported distinct claim is the full sharp mixed nonstationary cone and its strict even-sector boundary, not either specialization, the general Fourier framework, or the elementary corrected antipodal bound.

## value

PASS

The full criterion distinguishes two genuinely different obstructions for a natural radial-plus-nonstationary covariance model. It explains why strict positivity on every finite set can persist at a sharp operator boundary and supplies a finite negative witness just outside the admissible region which passes all antipodal tests. The corrected example strengthens the interpretation without changing the theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
