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

# Finite proof verification

Run `python3 verify_exhaustive.py` from the directory containing this file. The program builds all binary words at each length \(1\le n\le12\), partitions them under reverse complement, filters internally overlapping orbits, builds their pairwise compatibility graph, and uses an exact tie-preserving maximal-clique recursion to report both maximum weight and number of maximizing cliques. For every maximal-weight witness it can extract, it checks reverse-complement closure and all proper prefix–suffix comparisons word-by-word.

Independently compile and run `g++ -O3 -std=c++17 verify_independent.cpp -o verifier && ./verifier`. This implementation uses integer-bit encoding and pivoted Bron–Kerbosch enumeration, unlike the first program's direct string comparisons and nonpivot enumeration. Their outputs agree at every tested length; at \(n=12\), each returns maximum \(42\) and exactly \(1134\) maximizing codebooks. The C++ implementation processes \(80\) valid orbit vertices and visits \(2048\) recursion nodes; Python visits \(5,210,780\) nodes. These node counts are implementation-specific, not external scientific results.

The explicit length-\(12\) list in `RESULT.md` consists of \(42\) distinct binary words; direct tests confirm closure under reverse complement and no proper prefix/suffix overlaps between any ordered pair. The code-to-clique bijection together with complete finite maximal-clique enumeration proves the stated closed finite range, including all optimizer counts, not an infinite extrapolation. No external independent audit or publication-priority certification has been performed.
