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

The proof reduces the infection rule to a root-graph degree-sum update and classifies every four-edge root graph that can activate in its first round. The two surviving types have explicit round-by-round closure and a counted replacement graph. This is an all-order mathematical argument for every integer \(n\geq5\).

Two distinct executable verifiers were run. Compile `verify_line_graph.cpp` with `c++ -O2 -std=c++17 verify_line_graph.cpp -o verify_line_graph` and run `./verify_line_graph`; it exhausts every four-initial-vertex subset at orders \(5\) through \(10\) using the explicit line graph's adjacency. Run `python3 verify_root_graph.py`; it checks root-graph degree sums and independently generated path-family masks, complete enumeration through order \(8\), and all replacement-neighbor edges and connected components. The count pairs at orders \(5,6,7,8\) are respectively \((60,0)\), \((360,90)\), \((1260,630)\), and \((3360,2520)\), with first coordinate the path type. Both verifiers must print PASS without exceptions. The finite enumerations cannot establish the all-order theorem by themselves.

No Lean, expert certification, or external independent scholarly audit was performed. The 2021 same-object article's full text was not obtained, so its unpublished-in-abstract optimizer details remain a literature-priority uncertainty.
