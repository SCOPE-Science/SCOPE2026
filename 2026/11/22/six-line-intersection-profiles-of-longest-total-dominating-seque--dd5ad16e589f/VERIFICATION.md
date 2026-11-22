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

# Reproduction and limits

Both independent checkers are contained in this package as `verify.py` and `verify.cpp` and require no external data. Run `python3 verify.py` and `g++ -O3 -std=c++17 verify.cpp -o verifier && ./verifier`.

The Python checker uses a finite-field multiplication table and a last-choice deletion recurrence; the C++17 checker uses polynomial reduction and forward additions. Both enumerate every one of the \(2^{21}\) possible selected-point sets, check the incidence design, and independently assert the maximum legal length, exact ordered and unordered maximal counts, reachable-support count, and six line-intersection signature populations. The supplied coordinate witness directly realizes the ten-step bound. The incidence-graph consequences then follow from shore separation and the interleaving formula.

These finite computations establish the claim for the Desarguesian order-four plane only; they do not imply an all-order theorem or independently establish publication priority. The checks are ordinary executable mathematical verification, not a third-party independent audit.
