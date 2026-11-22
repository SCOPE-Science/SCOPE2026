---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification scope

The included C++17 source reconstructs arithmetic in six finite rings, counts each ordered pair of trace-zero matrices by its literal commutator, and separates the first operands into quadratic-residue classes of their determinants. It compares the two derived formulas for all targets, and checks global sums and nonsplit-image omissions. The captured output records success for all six cases. The two characteristic-three length-three tests each enumerate 387420489 ordered pairs, and comparison is exact integer arithmetic, with no sampling.

The proof supplies the universal statement through a free-rank-one adjoint kernel, a primitive orthogonality equation over the chain ring, and the complete binary/degenerate-plane quadratic-form counts over its odd residue field. Exhaustive small rings do not replace that proof. The result does not cover characteristic two or impose a single fixed numerical determinant; the first operand is restricted to a quadratic-type class.
