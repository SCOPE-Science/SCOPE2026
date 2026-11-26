---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

After unitary rotations assume positive real rho and nonnegative beta. The weighted change of variables proves boundedness at beta≤c; testing coherent states on the equality ray in the would-be Gaussian exponent proves unboundedness for c<beta<1, and the constant polynomial is not sent into Fock space for beta≥1. An independent check uses the real Segal–Bargmann transform on A=T*T. Write u=rho², D=1−beta+u, E=1+beta−u, delta=(c−beta)/D, kappa=(1+beta+u)/E. Gaussian integration gives the real kernel (pi D E)^(-1/2) exp[−delta ((s+t)/2)²−kappa(s−t)²/4]. Its Weyl symbol is C exp[−delta x²−xi²/kappa] with C=2/sqrt((1+u)²−beta²). In the strict region, unitary dilation gives symbol C exp[−tau(x²+xi²)] for tau=sqrt(delta/kappa) in (0,1), whose Hermite eigenvalues are C/(1+tau) times ((1−tau)/(1+tau))^n. The ratio is the smaller quadratic root r in the finding and C/(1+tau)=sqrt(r)/rho. At beta=c, delta=0, kappa=1/c, C=1/rho; Fourier transform gives exactly the claimed heat multiplier for A and its square root gives the modulus. The multiplier has two monotone branches, each smooth with nonzero derivative away from zero frequency; every spectral measure is absolutely continuous, and all neighborhoods below the norm endpoint have infinite-dimensional spectral subspaces. This gives the approximation numbers and noncompactness. Since 1−r is asymptotic to sqrt(2c epsilon)/rho, the Schatten coefficient is also correct. Frozen finite checks were inspected, not run, and are unnecessary for the completeness or continuous-spectrum arguments.

## originality

FAIL

The critical modulus and norm endpoint are exactly covered by a distinct indexed result. The compact formula, including its explicit ratio and prefactor, follows by the elementary Weyl-symbol conversion and dilation in the correctness check and the old exact Gaussian quantization formula. The remaining Schatten claims are a geometric sum and its expansion. This is a statement-and-implication comparison; directory dates do not establish priority for the equivalent critical result.

## value

FAIL

The singular-spectrum transition is a natural problem, but the submission combines a direct Gaussian normal-form specialization with a fully overlapping critical result. Neither the Schatten geometric sum nor its elementary prefactor expansion is a separate unknown exact invariant. No standalone surviving result requiring a repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
