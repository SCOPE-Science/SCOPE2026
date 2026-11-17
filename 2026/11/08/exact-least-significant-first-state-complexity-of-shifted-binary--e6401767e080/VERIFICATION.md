---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For every m>=2 and c>=0 the quotient/remainder splitting after e low bits gives the residual F_{a,b}(n)=s_2(n+a)+b mod m. Distinct a are distinguishable using n=2^h-a_big and variation of h mod m. Enumerating reachable phases by full popcount intervals above and below c mod 2^e yields exactly Q_{m,c}; for c=2^k the distinct quotient levels give m+sum_{j=1}^{k+1}min(m,j). The transition recovers correct zero-padding outputs. Infinite proof is constructive; finite checks corroborate only a bounded set.

## originality

PASS

The October 25 exact shifted parity/Thue-Morse formula covers the m=2 case, but its phase set is only {0,1}; its sharp dyadic interval bounds do not yield all higher m state counts. The new exact all-m residual classification is a motivated generalization; earlier work on MSD-first shifts and translated Thue–Morse sets does not imply it as stated. Novelty of m>=3 remains best of knowledge.

## value

PASS

An exact minimal state count for every generalized digit-sum modulus and every shift is useful for automata minimization; the higher-modulus power-of-two case reveals a triangular-to-linear phase transition not captured by the parity theorem. It is more than an isolated example or textbook renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
