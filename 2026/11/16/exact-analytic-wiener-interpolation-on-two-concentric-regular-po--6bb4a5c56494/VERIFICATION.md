---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Cyclic averaging f(omega z) projects any competitor onto degrees divisible by n without increasing its ℓ1 norm; equality in ℓ1 forces all optimal coefficients outside this residue class to vanish. For 0<u<v<1, D_k=uv^k-vu^k>0 and the feasible trinomials F_k=1-P_k t+Q_k t^k attain norm 1+L_k. For a minimizing k, lambda=-(v^k+v)/D_k and mu=(u^k+u)/D_k define h_j=lambda*u^j+mu*v^j with h1=-1, hk=1; feasible F_j for each j≥2 and L_k≤L_j imply h_j≤1. The two-exponential curve h(t) increases then decreases to 0, giving h_j≥-1 for every j≥1, a valid ALL-degree dual certificate rather than a finite enumeration. Equality forces support {1,k}, or {1,k,k+1} at a unique adjacent tie; vanishing equations make the minimizer a trinomial or convex segment. The real extension L(t) has derivative controlled by strictly increasing G(x)=x^(eta+1)+(1+eta)vx-eta*u, proving unique continuous trough and at most adjacent integer minimizers. Direct L2-L3=(u+v+uv-1)/[uv(u+v)] yields first transition, and stationary-root asymptotics give k=log(1/(1-v))/log(1/u)+O_u(1), norm→2/u. Independently evaluated rational samples include exact tie u=1/5,v=2/3 (norm 15), and u=4/5,v=9/10 (index 9). These checks only corroborate the analytic certificate.

## originality

PASS

Abakumov–Chalendar–Poltoratski sharp moment duality (Theorem 3.1) covers endpoint p=1 in abstract form, but not the computed 2-radius dual extremizer, sparse equality family, adjacent ties or escape-of-degree transition. Cheng–Mashreghi–Ross Proposition 6.3 is restricted to p in (1,infinity), excluding the nonsmooth ℓ1 endpoint. No inspected record gives a table of exact two-positive-radius values. The claim requires independent all-degree certificate and discrete one-valley analysis, so it is not a mere restatement of general moment duality.

## value

PASS

A natural finite zero-geometry problem in the analytic Wiener algebra has an explicit sharp norm and all minimizers, with genuinely nontrivial degree-transition structure and an outer-boundary asymptotic. This computes a motivated endpoint extremal invariant left implicit by general duality, not an arbitrary coefficient slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
