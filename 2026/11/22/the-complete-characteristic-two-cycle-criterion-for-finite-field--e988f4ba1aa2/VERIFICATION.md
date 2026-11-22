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

# Reproducible verification

Run `python3 verify_structure_graph.py` from the extracted directory. This uses only the Python standard library and prints `STRUCTURE_GRAPH_VERIFY_OK` on success.

The script independently checks polynomial irreducibility for each of eight fields, exact field addition and multiplication, all directed cycles in dimensions \(1\) through \(8\), the eight-step \(\mathbb F_{16}\) witness, and selected orbits of \(g(x)=x+x^2\). In these eight examples the full graphs have respectively \(2,4,9,17,33,70,139,265\) weak components. These values are finite checks, not generalized claims about component counts.

The proof of the infinite result instead uses the trace-zero space in an odd-degree subfield and the fixed eight-cycle in the degree-four subfield. These cover every \(m\ge3\). For \(m=1,2\), the short exhaustive algebraic case analysis in RESULT.md is sufficient and is separately checked computationally.

No independent audit or external certification has been performed.
