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

The complete certified finite computation is `verify.cpp` (C++17, integer-only) and its actual captured output is `expected_output.txt`. Compile and run `c++ -O3 -std=c++17 verify.cpp -o verify && ./verify` and compare exact output. The code exhausts all permitted \(t,b\) at width \(14\), obtains all permitted last-block residues by a modular inverse, counts the complement, and compares all \(8193\) shell-boundary ratios by integer cross-products.

The separate `crosscheck.py` checks the forced-prefix test directly against inverse enumeration for *every* width-3 to width-8 input, and for 200 deterministic width-14 samples. Its saved output is `crosscheck_output.txt`. Those sampled checks are supporting tests, not a substitute for exhaustive width-14 enumeration or the all-length proof.

Verified finite count: \(45362298\) excluded width-14 leading/trailing block pairs. Verified minimum: \(80469557/240599040\) at leading-block boundary index \(6493\). The proof in `RESULT.md` transforms this into the upper-density bound; the program alone would not prove the infinite conclusion.

Limitations: the local predicate may mark a pair possible even though no actual quotient realizes it, so the claimed result is only an upper bound. The density-zero conjecture remains unproved, and independent scientific audit has not been performed.
