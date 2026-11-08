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

# Reproducibility and verified limits

The program `verify_graph.py` independently enumerates near-perfect matchings on \(2k+1\) labeled vertices for \(1\le k\le5\), constructs all one-flip neighbors, and breadth-first searches every vertex reachable from the canonical matching. Its observed distance profiles have total populations \(3,15,105,945,10395\) and diameters \(1,3,4,6,7\). The same code separately enumerates every subset of the appropriate size in the triangular graphs for \(n=3,5,7,9\) and checks optimum domination counts \(3,15,105,945\), including a search for smaller dominating sets.

The separate `verify_species.py` computes the distance polynomial by a labeled-component recurrence without constructing or traversing a matching-flip graph. For \(1\le k\le12\), it checks the total count \((2k+1)!/(2^k k!)\), degree \(2k\), diameter \(\lfloor3k/2\rfloor\), and exact antipodal multiplicity. At \(1\le k\le5\), it reproduces the graph-search sphere coefficients.

Reproduce using standard Python: `python3 verify_graph.py` and `python3 verify_species.py`. Their expected outputs are embedded as `verify_graph_output.txt` and `verify_species_output.txt`.

The mathematical proof—not any finite test—establishes the enumerator for arbitrary \(k\). Historical priority and independent scholarly audit have not been independently certified. The underlying flip-distance identity is not claimed novel.
