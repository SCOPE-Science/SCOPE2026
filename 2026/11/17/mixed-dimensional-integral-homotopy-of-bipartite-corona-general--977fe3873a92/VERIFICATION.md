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
# Mathematical verification
The theoretical proof is the four-stage graph-distance/cover/join/edge-attachment argument in `RESULT.md`. Its crucial domains are all \(a,b\ge2\), all geodesic triples, and no additions of two- or higher-dimensional faces beyond the stated subcomplexes. It does not rely on numerical extrapolation.

The standalone `verify_corona_gp.py` uses graph adjacency, BFS geodesics and complete simplicial enumeration rather than assuming the proposed face classification. For six pairs \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\), the complete enumerated face sets agree **exactly** with an independently coded classification, and all mod-two reduced Betti ranks match the integral wedge prediction. In particular, for \((2,3)\) the nonzero reduced Betti numbers are \(11\) in degree one, \(2\) in degree two and \(1\) in degree three; for \((3,3)\) the corresponding degrees are one and three, with ranks \(15\) and \(4\). See `verification_output.txt` for complete observed face counts and exact boundary ranks.

Command: `python3 verify_corona_gp.py`. The program depends only on the standard Python library and prints `CORONA_GENERAL_POSITION_COMPLETE_INDEPENDENT_ENUMERATION_PASS` on success. The recorded output is from an actual run of this complete program. These checks cannot establish an unbounded integer theorem or independent mathematical audit; the general result follows from the proof.
