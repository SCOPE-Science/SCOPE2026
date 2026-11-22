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

# Reproduction and limits

Run `python3 verify_subsets.py` using Python 3 standard library, and compile/run `verify_rotations.cpp` with `c++ -O2 -std=c++17 verify_rotations.cpp -o verify_rotations && ./verify_rotations`.

The Python checker exhausts unordered literal subsets from all 27 length-three ternary words. At pairwise distance two it enumerates all subset sizes zero through five (including all 80,730 five-element sets), and at distance three all sizes zero through four (including all 17,550 four-element sets). It verifies maximum-size counts, symmetry orbit representatives and group-orbit closure. It obtains respectively 132 and 12 optimal labeled codebooks; symmetry-group partitions have sizes \(6,6,12\) repeated ten times, and \(2,4,6\).

The C++17 checker independently builds all eight nonconstant rotation classes and enumerates every one of their \(4^8=65,536\) omit/choose assignments. Every code is tested for all ordered splices including self-concatenation, and for aligned pairwise Hamming distances. Its full exact histograms are \((1,24,174,336,132,0,0,0,0)\) and \((1,24,66,12,0,0,0,0,0)\).

The exhaustive universe proves completeness for **this finite problem**. The computation does not certify any theorem about arbitrary alphabets, longer words, or error correction at unknown boundaries. Older-source equivalence cannot be logically excluded by automated searches; independent audit is not yet performed.
