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

A complete uniform proof and its exact assumptions are supplied in `RESULT.md`. The checker `verify.cpp` exhaustively constructs each permitted base for orders \(4\) through \(12\), enumerates every binary new-vertex orientation vector, checks each candidate for a nontrivial module by enumeration of every subset, and verifies the necessary-and-sufficient bit test and stated counts. In total it checks 458720 cases. Run `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify` in the extracted package directory.

The separately written `verify.py` uses Python subsets of vertex labels, tests every new-point orientation through order eight, compares with the claimed piecewise formula and checks the global sum. Run `python3 verify.py`. It checks 80 pairs of possible reversal endpoints.

Observed successful output for both commands is given in `CHECKS.txt`. Exhaustive finite computation is supporting evidence; the proof establishes the claim for all orders. Original 1972 one-point-extension full text was not accessible and publication priority remains uncertain. No independent mathematical audit has been conducted.
