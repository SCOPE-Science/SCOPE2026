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

For every dyadic side length n_i, the cyclic shift module k[x_i]/(x_i^{n_i}-1) has x_i+x_i^{-1}=x_i^{-1}(x_i+1)^2 and therefore exactly two nilpotent Jordan chains of size h_i=n_i/2. After tensoring all d independent sides, the orthogonal-neighbor operator is multiplication by w=sum t_i on 2^d copies of B=k[t_i]/(t_i^{h_i}). Select maximal h_k=H and change variables t_k=w+sum others; characteristic-two Frobenius gives t_k^H=w^H since other h_i divide H. Thus A has exactly N/H copies of J_H(0). The two-layer reversible F satisfies F^2+I=diag(A,A)F, F^{2H}=I, and ker(F+I) is isomorphic to ker A; with c=N/H blocks in dimension 2N, all unipotent blocks have length L=2H. This proves exact fixed and primitive periods for all d>=3 over GF(2^f), not a finite experimental extrapolation. Independent full physical neighbor-matrix check on a 4x4x4 torus verified spatial rank 32, F order 4, and fixed dimensions 32,64,128.

## originality

PASS

Martin–Odlyzko–Wolfram describes general multidimensional additive cellular automata and second-order rules, but its cited Theorem 4.8 period bound assumes circumferences prime to the characteristic, specifically excluding these dyadic hypertori. Earlier exact 1D reversible and 2D first-order cyclic cases are related and credited, but do not state the all-d two-time-level uniform Jordan similarity and complete orbit census. The polynomial change-of-variable proof supplies the substantive higher-dimensional specialization.

## value

PASS

Complete Jordan similarity, maximum clock, fixed spaces and every primitive-orbit population for a natural reversible nearest-neighbor wave on arbitrary high-dimensional dyadic tori yield a structural classification far beyond sample simulations. The uniform dependence on the *largest* circumference rather than the spatial dimension is a motivated spectral dynamical fact of possible independent use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
