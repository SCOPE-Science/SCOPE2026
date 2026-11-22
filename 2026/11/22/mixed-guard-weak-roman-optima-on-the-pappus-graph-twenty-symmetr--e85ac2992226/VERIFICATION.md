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

# Reproducibility

For the eighteen-vertex affine Pappus incidence graph, run `python3 verify_affine.py`. It constructs the point-line incidence network, exhaustively tests all singleton/double support pairs of weight at most eight, constructs all 216 graph automorphisms with an exhaustive \(9!\) exclusion of extra shore-preserving symmetries, partitions the 2691 minima into 20 orbits, and calculates all jump/slide shortest paths. It asserts the 2691 minimum count, three weight-type counts, both full edge counts, graph connectedness, radius/diameter and eccentricity histograms.

Run `c++ -O3 -std=c++17 verify_ternary.cpp -o verify_ternary && ./verify_ternary`. The independent program uses another standard Pappus numbering, tests every ternary labelling (skipping expensive validity checks above weight eight), and separately simulates the one-attack response condition. It confirms no successful function below weight eight and exactly 1755, 882 and 54 successes with zero, one and two double labels.

`orbit_representatives.tsv` records all twenty orbit representatives in affine point/line indexing, with one-based multiplicities of each orbit and explicit lists of label-one and label-two vertices. No external scientific data or software package is required.

## Limits

The algorithms constitute an exhaustive finite proof for this specified graph and rule, not a claim about other graphs, unbounded sizes or independent external audit. Historical originality beyond the inspected material is not certified. No prior result is being revalidated.
