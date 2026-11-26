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

Writing the resolvent as (1+dc)^(-1) times the positive adjacency Neumann series proves off-diagonal strict positivity for c>0 by connectedness. C=2R-I and translation invariance reduce nonnegativity to the common diagonal; the Fourier diagonal strictly falls from 1 to n^(-d)<1/2. Adding a coordinate strictly reduces the mean resolvent for c>0. The Laplace integrand factorizes; A_n(z)=I_0(z)+2 sum_{l>=1} I_{ln}(z). The Bessel ratio tends to zero at z=0 and obeys r'_m=1-r_m^2-(2m+1)r_m/z, preventing any first crossing of 1 by the negative derivative there. Termwise comparison gives the strict n ordering, and Riemann-sum convergence brackets the limiting root at every fixed d. Strict Jensen uses E Y=1 and Var(Y)=1/2 for n>=3 and for continuous angles. The one-dimensional kernel has q=e^-omega, cosh(omega)=1+1/c and diagonal (1+q^n)/[(1-q^n)sqrt(1+2c)]; at c=3/2, q=1/3 and the excess over 1/2 is epsilon/(1-epsilon) for epsilon=3^-n. Uniform derivative convergence on a compact root neighborhood first gives displacement O(epsilon); then q(c)^n=epsilon(1+O(n epsilon)) there, yielding coefficient 8. The finite 3-by-3 multiplicities for sum frequencies 0,3/2,3 are 1,4,4, giving 7c^2-c-2=0. The continuous square-lattice Haar change of variables gives the squared central-binomial moments and K in modulus convention. Independent AGM evaluation reproduced 0.5881972836856281148591326751..., and finite frequency calculations checked the radicals. For the dimension law, on compact t=dc intervals the cubic Taylor expansion and fourth moment control give Phi=1/(1+t)+t^2/[2d(1+t)^3]+O(d^-2), uniformly in n; bounded centered summands with variance 1/2 give signed third and fourth moments O(d^-2). Evaluating at fixed points around 1 first traps the root; then the derivative -1/4 at 1 and correction 1/(16d) imply t=1+1/(4d)+O(d^-2). The package's artifacts/verify.py and recorded output are corroborative finite evidence, including some floating-point checks; all strict inequalities for unbounded n,d rest on the analytic proof.

## originality

PASS

Best-of-knowledge pass for the all-dimensional periodic threshold analysis, notably the strict period comparison in every dimension and the explicit correction uniform over finite and infinite periods. The general return-diagonal test, the Bessel product heat kernel, the elliptic Green function and the entire one-dimensional threshold sequence have direct antecedents; combining the return criterion with classical lattice Green functions in low dimension is not itself a novelty claim.

## value

PASS

On a canonical family, a strict dimension-and-period comparison and uniform quantitative correction distinguish the actual all-data positivity frontier from conservative time-step rules. The uniform coefficient 1/4 quantifies how close the sharp threshold is to 1/d simultaneously even on the smallest allowed periodic grids. This is useful independently of the known fixed-chain criterion and the classical low-dimensional Green formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
