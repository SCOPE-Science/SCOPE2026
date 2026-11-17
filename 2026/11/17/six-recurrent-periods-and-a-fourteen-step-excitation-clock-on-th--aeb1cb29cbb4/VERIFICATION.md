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

# Verification

The executable `verify_heawood4.py` recompiles the two supplied C++17 sources, runs them as full-state enumerators, compares their \((\tau,p)\) tables with the included CSV, verifies that all population counts sum to \(4^{14}=268435456\), and checks the exact recurrent population \(3753\). Successful replay occurred before release; the finite procedure may require multiple gigabytes of memory and a native C++ compiler.

The two proof implementations classify functional graphs by different algorithms: forward trajectory tracing and reverse indegree elimination. This distinction checks the exact state-space accounting but does not constitute independent external peer review. Only the indicated graph and local transition rule were checked; no claim is made about every possible graph or every number of colors. The source, all finite census records, and a replay command are included.
