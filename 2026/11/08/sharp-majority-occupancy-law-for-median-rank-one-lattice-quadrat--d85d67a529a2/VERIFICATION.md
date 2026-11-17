---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Character orthogonality yields Q_{p,z}(f_c)=sqrt(2)c_S and exactly uniform independent slopes S for nonzero prime generators. A positive median of height v forces at least q distinct coefficients >=v; Cauchy norm gives v<=1/sqrt(q), matched by setting the q most occupied coefficients equal. Multinomial law and disjoint majority-class binomial tail are exact; top d=s/2 occupancies always cover a majority and strong law gives eventual q=d. Binomial large deviations on (d-1)-subsets provide -1/2 log(1-4/s^2). For a fixed half-class Fourier function the Bernoulli median event is exactly 1/2. Small sample occupancy enumeration corroborates rather than proves the asymptotic statements.

## originality

PASS

Goda and L’Ecuyer study construction-free median lattice integration with weighted Korobov norm high-probability upper bounds; here the p-dependent Fourier-slope L2 unit ball gives a different exact worst-case functional and probability law. Related median Fourier coefficient-approximation work has a different target and risk. No exact occupancy theorem in inspected references.

## value

PASS

Exact realized worst-case nonlinear median error and its finite-sample/large-sample occupancy law on a naturally occurring Fourier aliasing subspace give an informative sharp boundary for independent-generator median quadrature; the result is not claimed for smoothness-normalized Korobov balls.

The dated certificate retains the supplied scientific assessment, sources and limitations.
