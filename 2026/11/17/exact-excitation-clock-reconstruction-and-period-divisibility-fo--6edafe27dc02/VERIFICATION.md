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

The proof uses the maximum-walk representation established in Gravner–Lyu–Sivakoff, arXiv:1610.07320 (Lemma 1, Section 3). The new finite-time relation is obtained from an explicit three-to-one edge-weight coboundary and a two-unit endpoint-potential range, so it has no extrapolation step from small computations.

Run `python3 verify_clock_quotient.py` to replay direct event counts and independently computed walk maxima on all simple labelled graphs with at most four vertices. Output is `verify_clock_quotient.out`. Run `c++ -O3 -std=c++17 verify_period_divisibility.cpp -o verify_period_divisibility && ./verify_period_divisibility` to exhaustively compute functional-graph periods for all simple labelled graphs with at most six vertices. Output is `verify_period_divisibility.out`. All source and output bytes are included in the same record.

Correctness limits: the two programs prove only finite instances; the all-graph result rests on the mathematical proof. The cited maximum-walk theorem is an independently published mathematical input, not an independently conducted audit of the new transfer theorem. Historical priority and other thresholds or alphabets are not verified.
