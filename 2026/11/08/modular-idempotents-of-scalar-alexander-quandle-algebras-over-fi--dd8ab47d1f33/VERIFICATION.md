---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In K[(F,+)] the original product is ρ_α(u)ρ_β(v) with ordinary multiplication on the right. The augmentation ideal I is nilpotent and each augmentation-zero idempotent lies in I^{2^j} for every j, so only the algebra zero is lost on restricting to augmentation one. Frobenius and px=0 give v^p=0 for v∈I, so 1+I is an elementary abelian p-group under ordinary multiplication. Its idempotents in the transported product are the F_p-linear kernel of ρ_α+ρ_β−1, stable under both automorphisms. The equivariant quotients of the principal-unit filtration equal I^j/I^{j+1}; Maschke applies over F_p since p does not divide |F×| and identifies 1+I noncanonically with I as an F_p[F×]-module. The basis X^x−1 for x≠0 is permuted regularly, so after scalar extension the characters t↦t^k give exactly the claimed nullity over K. This also verifies the gcd and Frobenius lower bound; the excluded F2 case is the only case where the stated parameter set is empty. The zero vector of W corresponds to the nonzero algebra idempotent e_0, so there is one additional algebra zero, not an extra point of W.

## originality

PASS

There is exact prior catalogue coverage of the prime-order base case and substantial prior coverage of prime-subfield scalars on elementary abelian groups. Credit those cases rather than a new general prime-subfield census. The supported distinct result is the exact count and nonzero-idempotent quandle for genuine extension-field scalars, including characteristic two. Their multiplication operators can have no invariant F_p-lines, and the prime-scalar eigenspace formulas and integral/ordered treatments inspected do not give this case.

## value

PASS

The result explains how a modular idempotent locus that is not a linear subspace in the original algebra becomes an explicit Alexander quandle, and counts it over every finite coefficient extension. The genuine extension-scalar range allows large differences on the same additive group (17 versus 1025 idempotents in the F16 examples) and includes characteristic two where a midpoint reduction is unavailable. The regular-character mechanism explains those differences rather than just fitting small counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
