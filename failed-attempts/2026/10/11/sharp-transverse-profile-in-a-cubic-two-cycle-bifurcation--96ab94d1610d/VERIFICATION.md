---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For the stated cubic P,Q, exact Cartesian-to-polar algebra gives rdot=r(1-r^2)(a+sin(theta)cos(theta)) and theta-dot=r^2(a+sin(theta)cos(theta))-sin(theta)^2. With phi=-theta and w=r^-2-1 this becomes wphi=2Psi_a*w*(1+w)/(G_a-w sin(phi)^2), Psi_a=a-sin(phi)cos(phi), G_a=Psi_a-sin(phi)^2. At a0=-1/4, G0<=-3/4+1/sqrt(2)<0, so angle phi strictly increases in physical time on a uniform annulus for |delta| small; analytic one-turn return is valid. Linear coefficient L_a=2Psi_a/G_a and exact integral yield log P_a'(0)=2pi-pi(2a+1)/sqrt(a^2-a-1/4), zero at a0, first a derivative -32pi. Quadratic scalar coefficient is B_a=2(Psi_a/G_a)^2, giving P_a0(w)=w+C*w^2+O(w^3), C=int_0^{2pi} B_0(phi)E(phi)dphi>0, E=exp(int L0) periodic and positive. Thus multiplicity exactly two and at neutrality P(w)-w=Cw^2+..., attracting on w<0 (r>1) and repelling w>0 (r<1). Analytic factorization P_a(w)-w=w H(a,w) and IFT give unique other small root w_a(0)=(32pi/C)delta+O(delta^2); first variational flow gives w_a(phi)=(32pi/C)delta E(phi)+O(delta^2) uniformly. r=(1+w)^(-1/2) yields r_a=1-(16pi/C)delta E+O(delta^2); return derivatives are 1-32pi delta+O(delta^2) on circle and 1+32pi delta+O(delta^2) on companion. Strict orientation and nonvanishing angular speed map roots to genuine periodic orbits. Valid only for sufficiently small |delta| and local tubular annulus. Independent symbolic polar/trig-derivative checks and DOP853 integration give C=26.802930537964, section slope=3.750745269159, and first-order branch/root checks for +/-delta. Numerical checks only corroborate the analytic proof.

## originality

FAIL

The published all-profile polar theorem assumes ds/dt=2s(1-s)U(theta), dtheta/dt=sU(theta)-V(theta), C^2 periodic U,V, U not identically zero, and nonzero angular speed in an annulus. Here U(theta)=a+sin(theta)cos(theta) and V(theta)=sin(theta)^2 satisfy those hypotheses around a0=-1/4, s=1: at s=1, U-V<=-3/4+1/sqrt(2)<0. At neutrality its universal quadratic return coefficient in q=s-1 is K=(1/2) integral_0^{-2pi} A(theta)^2 h(theta)dtheta, A=-2U/(U-V), h=exp(integral A). After phi=-theta, h(-phi)=E(phi) and K=-integral_0^{2pi} 2(Psi0/G0)^2 E dphi=-C. The change w=1/s-1=-q+O(q^2) makes the quadratic coefficient +C. Its general circle multiplier is M(a)=exp(integral_0^{-2pi} A_a dtheta). The elementary trigonometric integral for this U,V gives log M(a)=2pi-pi(2a+1)/sqrt(a^2-a-1/4) and derivative -32pi at a0. Standard analytic implicit function theory applied to the simple root after factoring P_a(w)-w=w[(M(a)-1)+Cw+O(delta*w,w^2)] forces w_a(0)=(32pi/C)delta+O(delta^2), and linear flow dependence gives w_a(phi)=(32pi/C)delta E(phi)+O(delta^2) and the two stated multiplier slopes. Hence the entire quantitative claim is a short, explicitly calculable special case/corollary of the published general coefficient formula, rather than a structurally new theorem. The general paper and this record have the same UTC publication date; priority ordering within that date has not been established, so no unverified earlier-hour assertion is made.

## value

PASS

The coalescence of two limit cycles at the invariant unit circle of a classical cubic planar system is a natural, non-arbitrary bifurcation problem. The leading angular displacement E(phi) with positive normalization C and section coefficient 3.750745269, together with matched sharp Floquet slopes, quantify both how a companion cycle separates in physical space and how its stability changes. These are meaningful model-specific continuation/validation benchmarks beyond a bare qualitative count and may matter to researchers studying explicit bifurcation geometry. Their intrinsic usefulness is distinct from originality: a prior general coefficient formula makes this particular calculation an already-covered specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
