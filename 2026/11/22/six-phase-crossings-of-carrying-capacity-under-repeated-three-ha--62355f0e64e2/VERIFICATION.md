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

For every fixed k, small and large positive constant vectors are strict sub- and supersolutions, using double stochasticity, slopes (2,2,4) at zero and bounded recruitment. Monotone iteration and strict subhomogeneity (scaling one positive fixed point to first contact with another gives a strict inequality) give a unique positive equilibrium; primitivity makes every nonzero orbit positive after finitely many steps, and the two monotone iterations trap it. At perfect mixing the total 3 gives x0=(2/3,1,4/3), a=(2/9,1/2,4/9) and 1−a·v=11/18. The Jacobian I−diag(a)v1ᵀ is invertible, and the positive local IFT branch is the unique positive equilibrium for D^k near P. Differentiating and summing gives aᵀ(D^k−P)x0/(1−a·v) with error O(||D^k−P||²). On the zero-sum plane 2D=I+C satisfies (I+C)^3=−I, from C^3=I and I+C+C²=0 there. Exact iteration on b=x0−(1,1,1) gives the six scaled numerators 4,−1,−5,−4,1,5 divided by 33. Since the norm error is O(4^−k), signs are eventual and strict in each specified class. With two habitats D^k−P=λ^k(I−P), λ real, so an analytic noncritical response is either locally constant or has a first nonzero monomial, giving only constant or parity signs (λ=0 is exact mixing). Independent replay: python3 /workspace/independent_checks.py 1; 27 numerical signs are diagnostic, not the proof of an onset or of infinitely many switches.

## originality

PASS

The supported increment is the fixed-D, integer-k sign sequence at equality in the perfect-mixing benchmark, including its six nonzero coefficients and dimension obstruction. The closest same-model paper expressly leaves the finite-k direction at equality unresolved. Neither a varied rate in a different family nor a rank-one optimal-bound result settles this. This is not a priority claim for the Beverton–Holt model, the implicit function theorem, or multiple biomass crossings under varied intensities.

## value

PASS

The finite-k direction matters precisely where the established limiting comparator is indecisive. An exact network with infinitely many strict sign switches despite convergence, and a sharp dimension requirement for that particular sign pattern, show a qualitative limitation of inferring benefits from fast mixing. The switches compare distinct systems and their magnitude tends to zero; no ecological field effect or oscillating trajectory is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
