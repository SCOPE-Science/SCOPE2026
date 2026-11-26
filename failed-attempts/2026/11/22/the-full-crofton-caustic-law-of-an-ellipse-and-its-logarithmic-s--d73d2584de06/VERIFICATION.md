---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a line with unit normal n and signed offset p, put h²=a²n_x²+b²n_y². The dual conic equation gives Lambda=h²−p². For a regular parameter and p≠0 it is sufficient as well: the contact is diag(a²−Lambda,b²−Lambda)n/p, so the line is tangent there. Central lines and degenerate parameters causing exceptional contacts are null events. The total allowed (theta,p) mass is P by Cauchy's formula. Changing variables on both offset signs shows the pushforward is absolutely continuous, with density (1/P) times the integral of (h²−z)^(-1/2) over theta in [0,π) with h²>z. For z<b², all angles contribute, immediately giving the first K branch. For z>b², use h²=a²−c² sin² theta in one quadrant and substitute sin theta=(sqrt(a²−z)/c)sin v in the allowed interval; this yields the second branch with prefactor 2/(Pc). The complementary modulus squared is |eta|/(c²+|eta|) below the separatrix and eta/c² above it. The standard asymptotic of K therefore gives exactly log(16c²/|eta|)/(Pc)+o(1). K(0)=π/2 gives the upper density and linear tail. A line meeting the focal segment has |p|≤c|n_x| (equality is a null event), of total measure 4c, giving the mass ratio. The law determines b² as the unique interior point of locally unbounded essential density and a² as the upper support endpoint. In the circle h is constant, giving the stated density and tail sqrt(epsilon)/R. The independent line-coordinate proof checks the density without using the billiard equivalence; that equivalence also follows from the incidence Jacobian dℓ du on the oriented double cover.

## originality

FAIL

Waalkens–Wiersig–Dullin explicitly computed the two angular actions in §2, equations (8) and (9) of arXiv:chao-dyn/9612020. In collision coordinates these are the Crofton survival probability up to one common constant, with the parameter replaced by its affine complement. To see this, scale the semimajor axis to 1, write alpha=c/a, P'=P/a, x=z/a² and kappa²=1−x, and take unit speed (2E=1). Their angle phi is eccentric anomaly and p_phi is the canonical tangential momentum q'(phi)·v, so dphi dp_phi equals dℓ du in scaled collision coordinates. Equation (7) gives the level curve p_phi²=kappa²−alpha²cos²phi. Thus the survival set has |p_phi|≤sqrt(kappa²−alpha²cos²phi) on the allowed angles. Its oriented area is eight times the quadrant integral J of that square root over allowed angles, and total oriented mass is 2P'. Equations (8) and (9) identify J=π times the desymmetrized angular action: J=kappa E(alpha/kappa) for kappa>alpha and J=alpha[E(k)−(1−k²)K(k)] with k=kappa/alpha for kappa<alpha. Accordingly the full survival probability is 4J/P' on both sectors. Differentiation and unscaling give exactly the two proposed normalized density branches. The precise logarithmic coefficient, upper endpoint and inverse recovery are direct consequences of this known two-sector action via the standard elliptic integral limit and support. The record's probabilistic interpretation is valid but is an equivalent formulation of existing explicit formulas, not a newly determined law.

## value

FAIL

The normalization gives a clear probabilistic presentation of useful classic curves, but does not determine a new invariant or inverse phenomenon: the exact survival curve is the known angular-action curve, and both density branches and the separatrix and endpoint consequences follow by standard differentiation and limits. The formula and elementary recovery in exact data add no independently motivated unknown fact beyond that reformulation. No new statistical stability, near-circular uniform estimate, or different ensemble is analyzed in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
