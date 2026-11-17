---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The digit recursion f_d(2t)=f_d(t) and f_d(2t+1)=f_d(t) XOR [t≡2^(d-1)-1] is exact. Its state S=(f(t),f(t+1),t mod2^(d-1)) admits finite appended-digit maps, and a proved two-block identity reduces every possible factor up to length 2^(d+1) to reachable states and residues. Inspected check_factors.py constructs all 14/24 reachable states, verifies closed backward access and stationary rational weights, exhaustively checks every residue and even length, and checks absence at the next even length. Cropping both ends proves no longer factor is possible. Markov primitivity and exact rational aggregation prove natural starting-position densities; direct prefix enumeration independently corroborates the finite lists.

## originality

PASS

Earlier all-one-pattern parity sequence work concerns subsequence complexity, ordinary factor complexity and maximal constant-letter runs. The same-date Resultary exact constant-run census does not fix factors under simultaneous reversal plus bitwise complement and does not determine each reverse-complement factor density. No stronger exact antipalindromic spectrum was found by the targeted search.

## value

PASS

The complete classification of involution-fixed factors of two concrete natural automatic sequences, together with exact frequencies and sharp last allowable lengths 14/30, is a motivated and reproducible finite-state structural invariant; these are not merely counts of ordinary constant runs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
