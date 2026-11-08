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
# Reproducible checks

The definitions and infinite-family proof are in `RESULT.md`. The C++17 code `check_reconfig.cpp` tests \(2\le k\le5\), both \(n=k^2\) and \(n=k^2-1\). It enumerates time-ordered sources subject to source-separation inequalities; for each tuple it covers the cycle by all radius-\(k-i\) balls, constructs all legal one-coordinate moves, then exhaustively tests degrees, component sizes and counts. Its complete output is `reconfig_output.txt`; it ends with `PASS exhaustive sequence reconfiguration`.

The independent Python code `check_python_reconfig.py` tests \(2\le k\le4\), with explicit set-valued balls, Python tuples and a separate graph traversal implementation. Its output is `python_reconfig_output.txt`; it ends with `PASS independent Python graph census`. Both tests were rerun after extraction from the completed delivered package.

From the extracted directory, execute `g++ -std=c++17 -O2 check_reconfig.cpp -o check_reconfig && ./check_reconfig` and `python3 check_python_reconfig.py`. C++ tests only orders through 25, where a 64-bit mask is sufficient. These finite tests do not establish the theorem for larger \(k\); the cyclic interval and winding proof does.

For \(k=2\) the graph sizes are 4 isolated states on \(C_4\) and one six-cycle on \(C_3\). For \(k=3\), the graphs have 18 isolated states on \(C_9\) and two 24-cycles on \(C_8\). For \(k=4\), the graphs have 96 isolated states on \(C_{16}\) and six 60-cycles on \(C_{15}\). For \(k=5\), the graphs have 600 isolated states on \(C_{25}\) and 24 120-cycles on \(C_{24}\).

No independent scholarly audit has been performed. A later full-length paper on a different burning-schedule reconfiguration move model was not available for complete inspection.
