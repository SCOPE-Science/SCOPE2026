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

# Reproduction and verification scope

Run `python3 verify_local.py` with Python 3 to reconstruct the four possible interior deletion changes, the six possible adjacent changes, all sixteen boundary-envelope counts, the seventeen indexed witness pairs, and the sixty-four limiting boundary cases. The supplied `verify_local.out` records the actual passing output.

Run `c++ -std=c++17 -O2 direct_histogram.cpp -o direct_histogram && ./direct_histogram` to enumerate all input words of lengths two through thirteen and all pairs of deleted positions, using literal reconstructed words and freshly computed adjacent-pair histograms. `direct_histogram.out` records the actual output. The executable checks each computed maximum against the declared sequence, exits nonzero upon disagreement, and reports witness counts as well as one representative word.

The upper bound for arbitrary length is **not** inferred from the finite word enumeration. It follows from the finite exhaustive set of local changes, with the fixed-boundary table as a checkable short certificate. The explicit length-thirteen family preserves the stated seventeen local changes under arbitrary run extension, proving all-length sharpness. The limiting probabilities follow from the count of all sixty-four fixed boundary triples and from the elementary disjoint-block occurrence bound. Finite source-length enumeration is used only to establish the first-attainment threshold and smaller-length values.

The programs require a C++17 compiler and Python 3 standard library. No external software, network, or private paths are needed. Historical priority assessment of one inaccessible motivating preprint and independent scientific audit remain open.
