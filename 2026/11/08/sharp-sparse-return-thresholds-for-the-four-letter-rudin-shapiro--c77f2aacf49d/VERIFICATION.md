---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Reconstructed the four-letter substitution, parity rule and many-to-one binary coding. Independent recomputation found identical length-67 factor languages in substitution stages 11 and 12, each with 528 factors, and 80 length-11 factors. The exact sigma(F_L) closure lemma turns these stable finite factors into the complete infinite-word language. Recomputed all 1024 delay subsets at horizon 10 (32 qualify, minimum cardinality five) and all C(33,4)=40920 even four-subsets through delay 66; exactly {2,14,64,66} and {2,52,64,66} cover. The no-three-shift global lower bound correctly uses published binary Rudin-Shapiro Theorem 28; it is not inferred from finite enumeration. Every quantifier over the one-sided fixed point and distinct literal symbols is respected.

## originality

PASS

The published binary four-shift lower bound does not determine literal four-letter forward-equality covers; no inspected result supplies the exact horizon 10, sparsest horizon 66 and their two extremizers. The explicit infinite-word finite-language certificate is a motivated exact structural invariant.

## value

PASS

Exact finite-delay optimization for a canonical morphic four-letter word gives an intrinsically useful sharp delay-versus-sparsity tradeoff and exhaustive optimizer classification, not a numerical finite-prefix curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
