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

# Reproducibility and limits

The embedded programs are self-contained and use distinct descriptions of the configuration space.

Run `python3 verification/verify_gaps.py`: it enumerates every nonnegative slack composition of total \(s\le2\), constructs labelled independent sets from gap words, directly applies legal cyclic slides, and verifies state counts, degrees, component counts, edge and triangle counts, and all triangle-incidence multiplicities for \(6\le N\le74\). Its successful completion prints `GAP_RECONSTRUCTION_PASS`.

Run `g++ -std=c++17 -O2 verification/verify_direct.cpp -o verify_direct && ./verify_direct`: it generates every size-\(m\) subset of \(\mathbb Z/N\mathbb Z\), checks independence using direct circular distances, generates legal slides from the original edge rule, and verifies the predicted counts and connectivity for \(6\le N\le26\). Its successful completion prints `DIRECT_ENUMERATION_PASS`.

These enumerations corroborate the cyclic-gap proof but cover finite ranges only. The proof of the theorem for every \(N\ge6\) is contained in `RESULT.md`. No independent audit has been performed.
