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

In base 3, digit-sum parity equals integer parity, so even numbers fail anti-Niven. For every initial residue r modulo 27, a concrete triple of indices among j=0..12 lies in the same quotient block of r+2j and has low-digit sums 0,1,2 modulo 3, forcing a multiple of 3 regardless of the upper quotient digit sum. Independently checked all 27 triples and all 243 r/upper-sum pairs. Any length-39 step-two progression of odds has exactly 13 multiples of 3, their quotients form 13 consecutive odds; the lemma yields gcd>=3. All 38 terms a=86699+2j, j=0..37 were independently verified as gcd(n,s3(n))=1. This is an infinite upper bound with a finite complete residue certificate, not an inference from sampled starts.

## originality

PASS

The full 2023 Blau–Harrington–Lohrey–Sosis–Wong source defines the same anti-Niven progression and proves finite lower bounds for base b=2^r+1, explicitly leaving an upper bound open. Its upper-bound hypotheses require an odd prime dividing b−1, absent for b=3, d=2. A published broader short-even-stride theorem likewise requires a prime p|b−1 with p not dividing d; for (3,2) this set is empty, so it cannot entail the 38 bound. The different Niven-divisibility literature and OEIS A064150 do not cover coprimality. Residual risk of post-2023 obscure equivalent.

## value

PASS

Provides the exact sharp first global maximum for a natural previously unresolved base-three/difference-two anti-Niven progression question, with an explicit attaining witness and a rigorous finite-state forcing lemma. The fact is an intrinsically motivated sharp cutoff, not a random tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
