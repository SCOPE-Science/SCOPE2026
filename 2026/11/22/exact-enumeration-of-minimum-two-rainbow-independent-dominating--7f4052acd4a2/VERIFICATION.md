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

# Reproducibility and proof checks

The following certificate programs and their exact output files accompany the theorem; all outputs were reproduced directly from their corresponding included source files.

- `transfer_certificate.py`: verifies the entire finite local transition universe of \(35\) compatible states, \(70\) directed legal arcs, and reduced-cost histogram \(46\) zero, \(24\) one. Uses exact symbolic integer arithmetic to obtain the characteristic polynomial and the \(12\)- and \(4\)-state recurrent-block factors; matches all traces through length \(40\). Requires SymPy.
- `direct_bruteforce.cpp`: exhaustively enumerates every vertex labeling for \(3\le n\le7\), testing independent positive color classes and the two-neighbour condition with no transfer-table shortcuts. Requires a C++17 compiler.
- `independent_dp.py`: counts feasible assignments independently from local three-column feasibility and outputs the complete number and minimum count for \(3\le n\le11\). Requires Python 3.

The independent direct exhaustive test for \(n=7\) examines all \(3^{14}=4,782,969\) vertex labelings and obtains minimum weight \(7\) with \(112\) minimizers. The full symbolic certificate supplies the infinite proof; tests on finite lengths do not alone imply the all-length claim. A separate external independent audit has not been performed.
