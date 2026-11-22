---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Subtracting phase equations in tau=gt yields x_prime=G(y-x)-G(y), y_prime=G(y-x)-G(x). With Q=-sin+(r/3)sin3, H=Q(y-x)-Q(y)+Q(x) satisfies canonical Hamiltonian equations, as independently checked symbolically. Let u=cos s: G(s)=F_r(u)=4ru³-(1+3r)u. Its derivative 12ru²-(1+3r) is <=0 and only isolated zeroes for -1/3<=r<=1/9, so F_r is strictly decreasing and equilibrium equalities reduce to cos x=cos y=cos(y-x), giving only sync and two splay. Three invariant collision circles bound two triangular disks; H=0 on each boundary and H=±3sqrt3/2 at the unique nondegenerate splay extremum in each disk, Jacobian determinant9/4, trace0. Absence of other critical points and regular-level isotopy imply every nonzero intermediate level is a closed nonstationary periodic orbit. On a collision arc, d_prime=G(d)-G(0)>0; Taylor expansion independently gives (1-9r)d²/2+O(d⁴), and at r=1/9 exact factorization (4/9)(cos d-1)²(cos d+2)=d⁴/3+O(d⁶), yielding the respective inverse-time and cube-root clocks. For r>1/9 the factor (cos d-1)[4r(cos²d+cos d)+r-1] gives cos d=(-1+r^-1/2)/2 and 2 pair clusters per collision circle. This is an all-parameter analytic proof; finite trajectory checks only corroborate.

## originality

PASS

Best-of-knowledge PASS. Ashwin–Bick–Burylko (2016) §4.1 already give a first integral and qualitative periodic islands for any even three-oscillator coupling; these ingredients are fully credited, not claimed new. An earlier Resultary conservative three-oscillator ring paper gives the fundamental cosine r=0 energy-period asymptotic, which does not entail the uniform sharp third-harmonic interval, critical r=1/9 collision-clock exponent, or emergence of six pair-cluster equilibria. No inspected primary or published theorem implies all these parameter-dependent thresholds.

## value

PASS

The sharp perturbation threshold for a structurally meaningful third Fourier harmonic in a natural conservative phase triad controls when the simple two-annulus portrait breaks. The exact change from d(t)~t^-1 to d(t)~t^-1/3 and its leading coefficient is a motivated nonlinear dynamical boundary phenomenon, not a relabeling of known integrability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
