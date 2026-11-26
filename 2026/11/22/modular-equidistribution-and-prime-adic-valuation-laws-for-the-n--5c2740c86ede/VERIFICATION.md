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

The two parity-dependent digit matrix rows follow from the normalized Z[√2] recurrence; determinant one preserves primitivity. At even parity, digit 0 and digit 2 provide lower-by-2 and upper-by-1 transvections. At 2^k an upper, then lower, then upper word produces (t+s(2t+1),2t+1) from (0,1), giving every admissible pair since the second coordinate is a unit. At each odd prime power the transvections give the primitive orbit by elimination. Choose exponents by CRT to isolate any one local factor; negative powers are realizable by positive powers on the finite state space. Digit 1 carries the full even layer bijectively onto the odd layer. The three digit permutations give uniform stationarity, the orbit gives irreducibility, and the digit-0 loop at the seed gives aperiodicity. Aligned ternary suffix blocks give the power saving on ordinary prefixes (take an exponential contraction factor greater than 1/3 when summing the geometric errors). CRT and counting second coordinates yield the stated marginals, and differences of divisibility tails give the valuation laws and independence at finitely many primes. The mod-2 return probabilities follow from diagonal projections of weights 1/4,1/4,1/2 at eigenvalues 3,−1,1 of the digit-count matrix. Fresh independent checks matched 2187 digit states and all orbits at 2≤m≤12; exact parity counts through L=5 were 1,1,3,7,21,61.

## originality

PASS

Credit the normalization's defining recurrence to Northshield, the reversal symmetry to Spiegelhofer, and the primitive-pair Markov-chain method and odd-prime-power marginal analogue to the literature on classical Stern. The supported new contribution is the normalized Northshield all-modulus state support and its law, notably the distinct 2-adic factor and exact complete-block parity count. The valuation formulas are consequences of the new joint law, not separate priority claims.

## value

PASS

This is a complete, fixed-modulus distribution on a natural ternary rational-enumeration sequence. It identifies a systematic 2-adic bias that differs from the familiar binary model and recovers exact parity counts before taking limits. The orbit support and the bias, rather than the standard convergence argument, give the scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
