---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For m>=2 unit-row scalar least squares with uniform singleton residual updates, errors e=x-x*, s_i=storedResidual_i-(x*-b_i) evolve as e'=(1-mα)e+mα(s_i-mean(s)), s_i'=e. Their exact exchangeable second-moment closure on (Ee²,Ee t,Et²,EV) has displayed 4x4 matrix and characteristic-one factor det(I-M)=-2α/m² P_m(α), P=m(m-1)(2m-1)α²-(m-2)(2m-1)α-2. The positive covariance map is permutation-equivariant; averaging a nonzero PSD Perron eigenmatrix preserves its nonzero trace, so the four-dimensional moment restriction has the full radius. Spectral perturbation at α=0 gives derivative -2m, no crossing before unique positive P root, and determinant sign gives real eigenvalue >1 beyond. Reachable original states Y0=(1,1_m), Y1=(c,1_m), Y2,i=(c²,1_m+(c-1)e_i) span R^(m+1), proving the original nonzero least-squares solution also has sharp necessity. x*=0 initially exact zero is acknowledged. Checked bounded symbolic matrix and finite-word verification script; analytic PSD and span arguments establish infinite-horizon statements.

## originality

PASS

The full 2026-11-08 two-row imbalanced-sampling theorem already covers m=2 uniform α=1/sqrt3 as a special case, and that portion is credited. Its cubic probability-dependent two-row covariance system does not cover all m>=3 identical-row trackers or the initialized-state nondecay proof. Xie–Qi–Han source sufficient step 1/[m(m+4)] and JacSketch/SAGA equivalence do not imply necessity and sharp m-dependent root. The all-m uniform classification is best-knowledge new with explicit unresolved older specialized SAGA risk; authorized access to source full text was blocked.

## value

PASS

An exact m-dependent stability frontier of a natural residual-tracking/SAGA method on maximally coherent rank-one linear least squares supplies a rigorous necessary-versus-sufficient calibration missing from existing bounds. The full four-moment reduction, failure at the sharp endpoint, and actual initialized-state necessity are nonroutine structural facts applicable to every m, and quantify the growing factor-m conservatism of standard sufficient step rules. Not a trivial m=2 substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
