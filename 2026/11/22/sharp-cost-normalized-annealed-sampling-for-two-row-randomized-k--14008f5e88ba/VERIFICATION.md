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

For two independent real unit row normals in the plane, after one projection the error lies on the line for the last completed row, and a switch multiplies squared norm by c². In the indexing of the update at RESULT.md:37, v_i(k) must use I_{k−1}, not I_k as printed at line 42. Conditioning on that last completed draw gives exactly the displayed positive transfer matrix, trace 1 and determinant (1−c⁴)p(1−p). For 0<p,c<1 every nonzero deterministic start has nonzero first-step mass, so the Perron root controls its annealed squared-error exponent. Endpoint F=0 is the continuous extension and is also the robust worst-start exponent of a pure law, not the actual exponent for an exceptional pure-law start solved in one projection; the initialization-wise theorem is scoped to interior p. For T=b+(a−b)p and N=−log Λ, the stationary numerator G=N′T−(a−b)N satisfies G′=TN″. The sign of N″ is opposite to c⁴(1+2s)−s³, increasing as p increases up to 1/2. Thus G either decreases or increases then decreases, with opposite endpoint signs, and F strictly decreases to the right of 1/2. The elasticity zh′(z)/h(z) for h(z)=−log[(1+√(1−4z))/2] exceeds 1 and is strictly increasing (its log-scale derivative is the variance of the index under the positive power-series weights). At p_0=√b/(√a+√b) this makes G positive; at fixed p<1/2 it moves the unique zero upward as 1−c⁴ increases. Compact uniform convergence yields the two endpoint optimizer and optimum limits: the leading near-parallel quotient is p(1−p)/T, and the limiting near-orthogonal objective uses Λ=max(p,1−p) with its cusp maximum at 1/2. In the stationary condition write u=1−2p, d=1−c⁴. It gives u/s=(a−b)N(1+s)/(2dT)→χ; s²=c⁴+du² then yields u/c²→χ/√(1−χ²). Equal prices follow by direct symmetry and maximization of p(1−p). Independent bisection of G on (0,1/2) at a=9,b=1 gave p_*=0.48667832, 0.41835517, 0.31365360 and 0.26455780 for c=0.2,0.5,0.8,0.95; it corroborates but does not prove the all-parameter claims. The frozen verifier and verification notes were inspected, not executed. The objective is exponent per expected update cost, not wall-clock-budget or quenched decay.

## originality

PASS

Credit the exact iteration-wise MSE transfer framework to prior work. The supported distinct addition is the static iid optimizer of the long-run annealed exponent per expected heterogeneous row cost, its strict ordering and interval, and its singular endpoint asymptotics. The closest work-priced laws have different objectives or admissible samplers.

## value

PASS

Two rows with different deterministic prices are a natural benchmark for the difference between per-update and expected-work performance. The exact optimizer shows why neither fair nor square-root-price sampling is optimal in the interior, and the coherence ordering and near-orthogonal c² layer quantify when the choice changes. These are usable exact facts about the stated criterion, not runtime-budget recommendations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
