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

# Verification of the Jordan multiplicity census

The proof relies on the explicit multiplication table and the four-case principal-ideal rank formula; the finite checker is auxiliary. Running `python3 connected_sum_checker.py` builds independent multiplication matrices, calculates all power ranks by field elimination, and compares each radical element against the derived rank profile and then compares the complete Jordan partition histograms. The output in `connected_sum_checker_output.txt` is captured from an actual replay.

Exhaustive configurations: \(q=2\) at \((a,b)=(2,2),(2,3),(3,3),(3,4)\); \(q=3\) at \((2,2),(3,3),(3,4)\); \(q=4\) at \((2,2),(2,3)\); \(q=5\) at \((2,2),(3,3)\); \(q=7,9\) each at \((2,2)\). The checks include extension fields, cancellation and noncancellation strata, and the possibility of characteristic two. A finite enumeration does not establish the theorem for untested dimensions or fields; the full proof is in `RESULT.md`.

Originality comparisons rely on inspected relevant passages of four cited articles and mathematical searches. Independent mathematical validation or publication-priority certification has not been performed.
