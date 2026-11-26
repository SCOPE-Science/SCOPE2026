---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification

The accompanying finite checker `CHECK.py` reconstructs gaps by additive reachability for the classified multiplicities for genera 1 through 90. It compares the run through \(g\) with the remainder formula and checks the finite histograms and numerator. The frozen verification reports these checks passing.

An additional bounded check (`python3 check_by_reflectiveness.py`) uses only the definition of reflectiveness: for \(g=1,\ldots,14\), choose one gap from each pair \(\{i,i+g\}\), \(0\le i<g\), force \(0\) to be a nongap, and retain exactly the candidates whose nongaps are closed under addition below \(2g\). The genus bound \(F\le2g-1\) justifies that finite window. Directly scan the consecutive gap run containing \(g\); for \(g=12\) the histogram is \(\{1:1,2:2,3:1,4:1,5:1,12:1\}\). All tested histograms agree with the formula. These checks verify finite normalization and boundary conventions only. The interval comparison and moment calculations in the proof establish the limiting conclusions.
