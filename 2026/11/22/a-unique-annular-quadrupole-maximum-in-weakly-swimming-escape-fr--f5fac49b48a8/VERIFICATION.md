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

For D,R,q>0 and a fully absorbing disk, the backward Dirichlet inverse at v=0 maps first-derivative forcing to a higher Sobolev regularity class, so the drift is a bounded perturbation after inversion and the small-v expansion is justified. The passive time gives first-order forcing rho/(2D). Substituting F=(R I_1(k rho)/I_1(kR)-rho)/(2Dq) into the second harmonic gives forcing -(F'-F/rho)/2=-Rk I_2(k rho)/(4Dq I_1(kR)); the angular Laplacian contributes -4q. Applying the radial operator to I_2(k rho) and I_2(2k rho) yields the particular solution and the regular homogeneous correction, respectively. With L=kR, z=k rho, c=I_2(L)/I_2(2L), positivity follows from strict increase of I_2(2z)/I_2(z); strictness of the derivative follows from the positive-coefficient ratio covariance with j and 4^j. The same argument on I_2'(z)/z gives strict decrease of I_2'(z)/(2I_2'(2z)) from 1/4 to below c at z=L; thus exactly one strict interior maximum. Taylor expansion gives k^4 rho²(R²-rho²)/32 for the leading Bessel bracket, with uniform remainder over the closed disk, and hence the stated H-limit and peak at R/sqrt(2). For large L, at z=L-s the derivative ratio divided by c tends to e^s/2 uniformly on bounded s; testing fixed s below and above log 2 brackets the unique root. The normalized profile e^(-s)-e^(-2s) then gives peak height R/(48D^(3/2)q^(3/2)). Independent Bessel series and bisection at R=D=1 support both regimes, including wall distances 0.7101802, 0.7040833 and 0.6990514 at L=10,20,40.

## originality

PASS

The disk model, weak-swimming backward equation and first harmonic are established, and a distinct indexed finding gives the second-order orientation average. The supported contribution is the explicit nonzero second-harmonic coefficient together with its positive single-peak classification at every q>0 and the sharp peak asymptotics. Earlier perturbative propagator methods are substantially overlapping machinery, but the inspected recursion does not give the sign, uniqueness or peak limits without additional analysis. No claim of priority for the model, radial susceptibility or perturbation scheme is supported.

## value

PASS

The second harmonic resolves directional variation that disappears in the known orientation average. The theorem identifies the unique radius of strongest quadratic directional response at every rotational diffusivity and distinguishes a true interior optimum at slow rotation from a shrinking wall layer at fast rotation, with explicit location and height constants. These are concrete checks for numerical first-passage calculations and are not obtainable from the zero-harmonic result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
