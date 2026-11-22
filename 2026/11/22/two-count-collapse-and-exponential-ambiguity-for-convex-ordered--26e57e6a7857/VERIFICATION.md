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

# Verification of the new calculation

The standalone `verify_counts.py` uses Python standard-library integer arithmetic and enumerates all strict-order interleavings of the old parameters and a sorted run of anonymous new points. For each interleaving it independently enumerates the cut subsets determining a convex equivalence relation and retains exactly the diagrams inducing the original equivalence pattern on the old named points. Multiplication by the factorial of the new tuple arity restores all coordinate orders.

Recorded execution from the packaged program returned `PASS direct extension-diagram comparisons: 272`, `PASS inverse reconstructions: 5051`, and the four-point same-total/different-refined-channel check. The finite comparisons cover each ordered composition through six old points and each arity through three, plus arity four through four old points. The inverse reconstruction checks each admissible parameter pair through 100 old points. These are explicit finite checks only; the full proof is in `RESULT.md`.

The closed-form symbolic proof and its hypotheses were also checked directly: represented classes supply exactly \(n+k\) internal gaps; unrepresented classes occur in \(k+1\) quotient gaps as sequences of nonempty blocks; homogeneity identifies induced diagrams with complete types. The named quotient class order and the new-coordinate strict order prevent additional automorphism identifications. The logarithmic derivative, inversion, composition-fibre count, and channel moment argument do not require numerical extrapolation. Historical originality is not certified by the numerical checker.
