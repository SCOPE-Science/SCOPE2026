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

Area density in slant radius u is 2u/L^2 and azimuth is uniform. The Euclidean distance square is (u-v)^2+4q^2uv sin^2(phi/2), giving the capped arcsine in (1) with unit Jacobian to midpoint/difference coordinates. In the source proof the region x<=Cr is O(r^4) by the uniform x^2 bound. For x>=Cr the expansion through x^(-1) is uniform, and the integrated bound O(r^5/x^3) is O(r^4) because the h-range has length 2r and the x-cutoff is proportional to r. The rim upper endpoint changes the logarithmic integral only by a bounded multiplier of r^4; the cubic term comes from the linear-in-|h| part of (L-|h|/2)^2. An independent check of the entire expansion uses s=max(u,v), t=min(u,v)/s. The joint density factors as (4s^3/L^4)*(2t), and D=s*d, with d^2=(1-t)^2+4q^2t sin^2(phi/2). With J(rho)=Pr(d<=rho) and rho small at fixed q, put h=1-t, k=sqrt(rho^2-h^2)/(2q). There is no angular saturation and J(rho)=(4/pi)*integral_0^rho (1-h) arcsin(k/sqrt(1-h)) dh. The integrand expands as k(1-h/2-h^2/8)+k^3/6+O_q(rho^4), uniformly in 0<=h<=rho. The elementary half-interval integrals give J(rho)=rho^2/(2q)-rho^3/(3*pi*q)+(1-q^2)*rho^4/(64*q^3)+O_q(rho^5). Integrate J(r/s) against 4s^3/L^4: s<=Cr contributes O(r^4), the integrated Taylor error over s>=Cr is O(r^5*integral_{Cr}^L ds/s^2)=O(r^4), and the degree-four term yields 4 times its coefficient times log(L/r)/L^4. The degree-two and degree-three terms are r^2/(qL^2) and -4r^3/(3*pi*q*L^3), exactly the prescribed area and perimeter normalization. At q=1 the degree-four coefficient in J vanishes; for proper q the logarithm is positive and the prefactor after multiplying by A^2 is B=pi^2*(1-q^2)/(16q). This agrees with integrating the local curvature-square term since kappa_2=sqrt(1-q^2)/(q*s) and kappa_1=0. To take the limit defining B before knowing L, any fixed positive reference length can replace L inside the logarithm; their ratio in the limit is 1. Solving q^2+beta*q-1=0 gives the stated inverse, while area and rim alone already determine L=2A/P. The proof does not use uniformity over cone openings, the base disk, or an assumption that a smooth expansion is valid uniformly through the apex.

## originality

PASS

The unweighted cone sidewall surface-pair observable is a form of a known surface correlation function, and both leading coefficients and the local curvature-square mechanism are known in smooth settings. The increment is the singular apex-dependent coefficient and the bounded remainder after subtracting the divergent logarithm for this exact finite geometry. The older same-shape Gille logarithm concerns a different chord measure; its inaccessible full text leaves qualified priority uncertainty, not evidence of absence.

## value

PASS

The non-polynomial term distinguishes a smooth-away-from-apex developable surface from flat or fixed faceted cases after ordinary area and rim losses have been accounted for. It quantifies the effect of curvature accumulating across slant scales, giving a concrete singular surface-correlation benchmark and an alternative inverse invariant. The alternative inverse is not a claim of improved efficiency, stability or minimal data; the scientific value is the singular coefficient and its scope, not re-solving the two-parameter reconstruction already available from area and perimeter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
