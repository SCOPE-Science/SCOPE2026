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

Detailed balance parametrizes the whole feasible set by unnormalized flows a,b,c and the two interior row caps. A disconnected chain has SLEM 1 and is immediately excluded from equality; in the Rayleigh step one may uniformly use the smallest generalized eigenvalue on the M-orthogonal complement of constants, including zero. For 0<t≤1, q=(r,1,−1,−r), r=1+√2, has Rayleigh quotient (a+c+2b)/(r²+t)≤2t/(r²+t)=γ*. Equality forces both interior caps tight and q to be an eigenvector, hence a=c=γ*r/(r−1) and b=t−a. At that feasible candidate, the even nonzero Laplacian eigenvalue e=a(1+1/t) exceeds γ*, and the odd characteristic polynomial at e is −2ab/t². Thus γ* is the smallest nonzero Laplacian eigenvalue, and the odd trace 2+a(1−1/t)≤2 controls the negative end of the transition spectrum. For t≥1, the endpoint antisymmetric unit vector gives a square-norm lower bound 1/(1+t) plus two squared deviations from a=c=t/(1+t). At those outer flows, saturation of the norm requires the odd block squared to have zero off-diagonal entry; the odd block's positive off-diagonal therefore forces its trace zero and b=t/2. Those weights give odd block square I/(1+t) and even nonstationary eigenvalue zero. The two branches agree at one, with derivatives −1/4 and −1/(4√2), and both interior holding rates change from zero to (t−1)/(2(t+1)). Independent sample t=1/2 (replay /tmp/opencode/frozen_math_samples_a91d.py): flows 0.2697521433898179 and 0.2302478566101821, SLEM 0.8419828528814565. Frozen verify.py was inspected, not executed.

## originality

PASS

Pass the exact capacity-saturated branch 0<t<1, its proof of uniqueness without reflection restrictions, and the sharp interface with the harmonic regime. The convex SLEM formulation, uniform point and the reported t≥1 harmonic weights are not new. The strongest accessible general and exact indexed comparisons do not supply an exact low-mass branch; unavailable parts of the highly relevant path literature remain an explicit risk.

## value

PASS

The interior-mass valley makes the standard harmonic walk infeasible and creates a natural active-constraint problem. The complete explicit design, certificate excluding asymmetric ties, and the first-derivative break at the switch provide an exact benchmark for discrete-time prescribed-mass path design beyond uniform stationarity. This is not a claim about arbitrary non-log-concave mass profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
