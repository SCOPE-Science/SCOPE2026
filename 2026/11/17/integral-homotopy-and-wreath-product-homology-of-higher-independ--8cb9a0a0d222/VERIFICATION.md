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

# Verification record

The theorem is proved symbolically in `RESULT.md`: center deletion/link and mapping cone, the acyclic simplex-skeleton element matching, natural integral augmentation-chain identification, and the Koszul-signed join Künneth map. Its unrestricted conclusions are not inferred from finite tests.

## Exact executable checks

Run `python3 verify.py` from this directory, using Python 3 standard library only. The recorded expected stdout is in `verification_output.txt`, ending with the exact marker `WINDMILL_HIGHER_INDEPENDENCE_FINITE_CHECKS_PASS`.

The script checks all \(7{,}552\) vertex subsets of nine small windmills by independently constructing their graph adjacency and induced connected components, then compares them to the independent blade/center face predicate. There are \(3{,}519\) actual faces across those cases, including empty faces. Exact bitset Gaussian elimination computes reduced simplicial boundary ranks over \(\mathbb F_2\), with augmentation at degree zero. The predicted integral wedge ranks match the resulting mod-two Betti numbers.

The same nine cases undergo 528 exact signed reduced Lefschetz tests for explicit automorphisms, using the sign of the permutation induced on each invariant simplex. Character targets are calculated from exterior powers of augmentation modules and the Koszul sign for blade permutations. An additional 2,520 group-element character evaluations across three complete automorphism groups verify that the invariant multiplicity of each proposed module is exactly zero.

Representative examples: \((n,q,r)=(2,4,3)\) yields \(\widetilde\beta_2=21\), \(\widetilde\beta_5=1\); \((2,5,3)\) yields \(\widetilde\beta_2=36\), \(\widetilde\beta_5=16\); and \((3,3,2)\) yields \(\widetilde\beta_1=8\), \(\widetilde\beta_5=1\). Finite mod-two computations alone cannot establish integral torsion-freeness, homotopy equivalence, or the unrestricted statement; those conclusions follow from the displayed independent proof.

## Scope of validation

Scientific correctness, originality and value have received self-review. No independent scientific validation has been performed. No equivariant homotopy decomposition or integral homology classification of the orbit space is asserted.
