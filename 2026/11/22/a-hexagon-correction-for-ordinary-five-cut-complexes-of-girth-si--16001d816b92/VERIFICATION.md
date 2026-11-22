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

# Verification of the hexagon-correction theorem

Execute `python3 verify.py` in a directory containing the included program. It uses only the Python 3 standard library and reconstructs every test graph from explicitly listed edges, not from an external graph database. The included `verification_output.txt` is the recorded standard output of a successful run. Run `python3 independent_mod2.py` from the same directory for a separate, direct mod-two simplicial-chain computation of the ordinary cut complexes; the corresponding recorded output is `mod2_output.txt`.

The program checks that each test graph has no cycle of length three, four, or five; enumerates all connected induced five-sets and induced six-cycles; compares the membership of every six-set in the Alexander dual with the induced-hexagon test; excludes every seven-set from the dual; exhaustively checks each disconnected four-set's set of connected five-extensions; verifies free faces for connected five-sets outside hexagons; and constructs a rooted spanning-tree removal sequence for the six faces surrounding every hexagon. Its exact counts include Heawood \((c_5,h_6,B)=(252,28,491)\), Möbius–Kantor \((288,24,1101)\), and Pappus \((324,18,2074)\). A theta graph explicitly tests intersecting hexagons.

The global statement is mathematically established by Steps 1–5 of `RESULT.md`: the connector lemma, a uniform elementary-collapse scheme, integral Euler/Hurewicz/Whitehead reasoning, and combinatorial Alexander duality. No finite test is used to infer validity for unbounded graphs. The provided checks do not prove shellability, graph automorphism modules, or smaller-order cases.
