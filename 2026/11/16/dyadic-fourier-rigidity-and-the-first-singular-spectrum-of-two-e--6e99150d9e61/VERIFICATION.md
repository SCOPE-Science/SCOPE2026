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
The finite exact-integer checker is `check_two_matchings.cpp`, compiled and executed with `g++ -O3 -std=c++17 check_two_matchings.cpp -o check_two_matchings && ./check_two_matchings`. It enumerates all \(2^{27}\) frequency representatives with one edge fixed positive, doubles all multiplicities by a proved global-sign symmetry, compares complete signed histograms obtained from different recurrence states, and checks 2,048 direct signed matching sums.

Required success header: `TWO_EDGE_MATCHINGS_K8_PASS total=268435456 zeros=20467680 rank=247967776 min_nonzero=2 max=210 levels=84`. All 84 resulting signed histogram rows are in `walsh_histogram_n8.csv` and must agree exactly. Checked Parseval sum: \(56{,}371{,}445{,}760\). The finite certificate does not prove assertions for other graph orders; their proofs are symbolic in `RESULT.md`.

Independent mathematical audit and external validation were not performed. The full rank and pseudoinverse norm are asserted only for \(n=8\); the congruence and gcd theorem is valid for \(n\ge4\). No lower bound for all other singular orders and no sharp endpoint projection norm is asserted.
