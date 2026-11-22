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

# Reproducibility

The theorem's support characterization is proved for every integer \(n\geq0\) using explicit extension constructions, reversal/complement symmetries, and a finite-state generating function. The scripts independently test finite instances and are not presented as infinite certificates.

Run:

```sh
python3 verify_binary_trigrams.py
c++ -std=c++17 -O2 verify_binary_trigrams.cpp -o verify_binary_trigrams
./verify_binary_trigrams
```

`python_check.txt` and `cpp_check.txt` record observed output from actual runs on the accompanying source files. Python enumerates every word and query support for all eight forbidden length-three patterns for lengths zero through nine. C++17 independently enumerates the same trace relationship for lengths zero through eleven. Both check coefficient formulas and the shattering-extremality equality for each pattern and length.

The rational generating functions and all-order extensions have mathematical proofs in `RESULT.md`. Only these finite computational domains have been machine tested. No independent mathematical audit has been conducted.
