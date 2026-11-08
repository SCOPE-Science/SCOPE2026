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

# Reproducible checks and exact scope

Run `python3 verify_desargues.py` using only the Python 3 standard library. The program builds the incidence graph of two- and three-subsets of a fixed five-set, then checks the metric by both a full graph-search computation and a direct set-intersection distance formula. It tests all 190 unordered vertex pairs and confirms the distance-pair histogram \((30,60,60,30,10)\).

For the inclusive thresholds two and three, independent complete enumerations of all 20-vertex subsets agree. The respective face vectors are \((20,90,120,30)\) and \((20,150,540,1000,960,450,80)\). Sequential vertex-toggle matchings leave precisely one critical zero-cell plus nineteen critical two-cells (threshold two), or one critical zero-cell plus one critical three-cell (threshold three). The program verifies 120 and 1599 matching pairs respectively and inspects **every** one of the 660 and 13,980 Hasse covering incidences in the two complexes. The complete reversed-matching directed Hasse graphs admit topological sorts of all 260 and 3200 nonempty faces, proving acyclicity. Additional exact mod-two boundary reductions yield reduced Betti vectors with only \(\widetilde\beta_2=19\) and only \(\widetilde\beta_3=1\), respectively.

The scale-four statement is checked via ten disjoint antipodal nonedges and a combinatorial cross-polytope face count of \(3^{10}-1=59048\) nonempty faces; its homeomorphism to \(S^9\) is a direct mathematical implication. The graph's cycle rank at scale one is eleven, and its diameter is five. The finite checker covers all thresholds for this one finite metric space and makes no assertion for larger bipartite Kneser graphs. The output log `verification_output.txt` records the expected trace, ending in `ALL_CHECKS_PASS`; the decisive evidence is the checker plus the mathematical Morse and antipodal arguments, not the log alone.

The homotopy types imply the complete reduced barcode because all nonzero reduced homology groups at consecutive integer thresholds have different degrees. Independent audit is not performed.
