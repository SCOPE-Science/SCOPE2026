---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The actual weighted border polynomial identity gives rho(w)=1/2 exactly when P_w(lambda)=0, for a simple Perron root lambda in (1,2). The characteristic polynomial H_w=(x-2)sum_{j in borders}x^(j-1)+1 is monic and has constant coefficient ±1. Hence lambda is an algebraic unit and no positive power lambda^d can be rational: both lambda^d and its inverse would be rational algebraic integers, forcing lambda^d=1. One nonzero monomial cannot vanish; cancellation of exactly two nonzero monomials requires rational lambda^(ell-j). This proves the restricted equivalence, not the unrestricted conjecture. Independently compared weighted border derivative to prefix-automaton Perron frequencies for all 426 eligible binary words of lengths 4..8. Finite checks merely corroborate the proof.

## originality

FAIL

A direct stronger earlier result decisively covers this restricted final claim: the Lean file D5/S1/Words/Forbidden/BonaMagaRicheyHalfFrequency.lean defines ∀ nonempty binary w, Tendsto (rho w) (1/2) ↔ BalancedBorders w, formally proving the unrestricted Bóna–Maga–Richey conjecture. Its Git commit 534f00cd36b29974a6f47bf08f4147886764dd3c is dated 2026-10-08T05:53:50Z, before the assigned 2026-11-02 record. The assigned theorem for words with ≥2 of each symbol and ≤2 unbalanced borders is a strict special case: its rho limit and theorem premises match the earlier statement. Correctness of the shorter algebraic-unit proof does not make the scientific claim original.

## value

FAIL

The numerical restriction to at most two unbalanced borders was a motivated intermediate target in the original conjecture, but the complete half-frequency conjecture had already been resolved before this record. The record offers an elegant short special-case algebraic-unit proof but no separate, demonstrated unknown invariant, sharp new bound, or new method theorem once the stronger result is available. For the final research claim, the special case is already subsumed; correct/reproducible exposition is not a new valuable mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
