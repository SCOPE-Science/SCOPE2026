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

A positive admissible binary expansion is uniquely 1(1|00)*. The number of length-L words is F_L. For every nonmaximum word its last 00 tile followed only by ones determines a unique numeric successor, and a direct suffix subtraction gives gap Δ_t=2^t+2 (even t) or 2^t+1 (odd t). Prefixes of length L-t-2 number F_(L-t-2) and sum to F_L-1: all within-layer gaps accounted for, including t=0,1 both giving gap3. Boundary gaps alternate 1 and2; summing Fibonacci counts across dyadic layers and taking ratios gives masses 1/φ at3 and φ^(-(t+2)) at t>=2. Independently enumerated complete layer gaps up to L=16.

## originality

PASS

A060142 encodes the SAME Baum–Sweet support under recurrence x→2x+1,4x and a known Fibonacci counting structure; these are explicitly credited. The last-zero-pair numerical successor classification, exact list of adjacent gaps, multiplicities and limiting probability law were not found in inspected database passages or semantic published records. An unindexed first-difference representation, composition-to-odd-parts argument or original paper might already imply them.

## value

PASS

Gaps between successive ones in the classical sparse Baum–Sweet automatic set are a natural return-time observable. The full gap spectrum, Fibonacci multiplicities and dyadic limiting frequencies are nontrivial infinite combinatorial statistics, not a renaming of known membership/size formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
