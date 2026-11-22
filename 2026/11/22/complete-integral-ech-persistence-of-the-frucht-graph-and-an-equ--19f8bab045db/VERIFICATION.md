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

# Verification details

Run `python3 VERIFY.py` with Python 3's standard library. All data are included in the file and the computation does not retrieve external dependencies. The companion `VERIFY_OUTPUT.json` records the deterministic output.

The calculation exhausts all 4095 nonempty graph vertex subsets at integer thresholds zero through five. Graph distances are independently checked by breadth-first search and Floyd–Warshall. Every oriented Hasse edge is covered by a topological-sort acyclicity check. Integral Morse boundary coefficients are computed using oriented simplex incidence signs and unit pivots. Independent raw simplicial mod-two elimination confirms each Betti signature.

The only nonzero positive-degree interstage map is the split surjection of rank three from degree-one homology at scale one to scale two. A determinant-one minor explicitly ensures an integral splitting. Three signed tetrahedra provide a bounding chain for the scale-two degree-two generator at scale three. Two single signed four-simplices bound the scale-three degree-three generators at scale four. Each asserted bounding chain is directly checked to have exactly the lifted source boundary; projections also give zero. The scale-five nerve is the full simplex.

Exactness is finite for the fixed Frucht graph. This does not validate unrelated graph classes or independently certify originality. No independent mathematical audit has been performed.
