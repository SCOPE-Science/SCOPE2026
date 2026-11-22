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

# Verification of the graph-quandle retraction rank formula

The proof in `RESULT.md` is the mathematical basis of the unbounded theorem. The accompanying `verify_graph_quandle.py` independently reconstructs the operation table and tests `f(f(x)) == f(x)` and `f(s_x(y)) == s_{f(x)}(f(y))` on every pair of elements.

The program checks \(K_2\), \(P_3\), \(K_3\) by unrestricted exhaustive enumeration of *all* functions on their respective four- and six-point sets. It checks \(P_4\), \(C_4\), \(K_4\), the paw graph and \(K_{1,3}\) by exhaustive enumeration of every map preserving the natural two-point component partition, without imposing the derived common-slope or false-twin normal forms. The predicted polynomial is computed separately by enumerating independent subsets and equal-neighborhood classes. The output must end with `GRAPH_QUANDLE_RETRACTION_RANK_VERIFIED`.

The eight tested output polynomials in ascending order of their displayed degree are: \(K_2:4T+T^4\); \(P_3:6T+8T^2+4T^4+T^6\); \(K_3:6T+T^6\); \(P_4:8T+48T^2+T^8\); \(C_4:8T+32T^2+16T^4+8T^6+T^8\); \(K_4:8T+T^8\); paw: \(8T+32T^2+T^8\); \(K_{1,3}:8T+48T^2+24T^3+12T^4+12T^6+T^8\).

The tests do not exhaust all graphs, all vertex counts, all endomorphisms outside the tested sizes, or disconnected graphs. In particular, no runtime failure is interpreted as nonexistence or mathematical impossibility. No independent mathematical audit has been performed.
