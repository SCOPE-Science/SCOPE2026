---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS: Spatial Parseval gives S²+2Σ_h|B_h(t)|². For fixed positive lag h, the time-frequency difference between indices m+r and m is 3hr(2m+h+r)>0, so continuous t integration drops all off-diagonal terms; uniform N-sampling retains exactly N-divisible differences. Pairing conjugates gives the factor 4 and correct coefficient ordering, including signed possible defect. N|3hr(2m+h+r) reduces exactly to t|2m+h+r, with t=(N/gcd(N,3))/gcd(N/gcd(N,3),hr); solvability and bounded least solution are necessary and sufficient. Taking all a_n=1 detects any alias; magnitude Cauchy–Schwarz proves C=2−1/K iff alias-free. For p>=2K−3 all positive factors are too small; for p<2K−3, p=2,3 use (h,r,m)=(1,1,0), p>=5 use (1,2,(p−3)/2); K<=3 exceptions handled. Independent direct Gaussian-integer frequency quadruple enumeration reproduced the complete signed defect in 261 (K,N) cases, K=1..9 and N=1..29. Proof itself covers infinite parameters.

## originality

PASS

PASS on best available primary and published comparisons: earlier Oct11 quadratic dispersion sampling has off-diagonal differences 2hr independent of m and divisor optimization; it does not imply the cubic nontranslation-invariant 3hr(2m+h+r) congruence or prime p>=2K−3 threshold. Classical KdV/Airy continuous restriction and aliasing motivate the observable but do not furnish this arbitrary-complex-coefficient N-grid uniform equality criterion. Searches found no prior same-scope cubic sampling theorem; that does not prove universal priority.

## value

PASS

PASS: The exact sample count needed to preserve a nonlinear Fourier fourth moment is a natural measurement/alias-avoidance invariant of a dispersive flow. The complete modular criterion gives a finite arithmetic algorithm for all composite grids, and the sharp prime threshold depends on cubic rather than quadratic dispersion. It captures both signed quadrature error and a sharp norm transition and is a structural finite-sampling theorem, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
