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

The mathematical argument in `RESULT.md` proves the claim for all integers \(q\ge4\), \(a,b\ge1\). The finite experiments below check implementations and boundary conditions, not all possible parameters.

Run `python check_exhaustive.py` to enumerate labelled states directly. Run `c++ -std=c++17 -O2 check_independent.cpp -o check_independent && ./check_independent` for an independently written integer-encoded simulation and a separate event-by-event ancestry condition comparison. Their captured outputs are embedded in `check_exhaustive_output.txt` and `check_independent_output.txt`, respectively.

The Python program tests fourteen triples and directly verifies maximum extinction time and its exact population. The C++ program tests eight triples and verifies the condition \(\tau=q+2\) for *every state*, not just the aggregated formula. Neither program relies on a symbolic algebra system. Calculations are finite; the all-parameter conclusion follows from the proof and not from extrapolating any numerical sample.

Scientific limitations: only the last extinction layer is classified, not the entire extinction histogram. The public literature comparisons do not establish historical uniqueness. Independent audit status remains not performed.
