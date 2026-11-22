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

# Reproducibility and limits

The verification artifacts are `verify_permutations.py` and `verify_direct.py`, both standalone Python 3 standard-library programs. Execute them as `python3 verify_permutations.py` and `python3 verify_direct.py` in the same directory.

The permutation enumerator visits every one of \(q!\) possibilities for \(f\), computes \(g=c\circ f^{-1}\circ c\circ f\), and checks the precise inequality. It obtains \(0,6,160,8988\) admissible full-size codebooks for \(q=2,4,6,8\), respectively. Each accepted code is independently tested against the raw Hamming, reverse-complement and both splice conditions; direct-block examples of sizes \(8,10,12,14\) are also tested. The second checker does not use the permutation representation: it forms 32 complementary word pairs on four bases, exhausts their 496 distinct two-pair selections, and retains exactly six valid four-word codebooks. It computes two orbits of sizes two and four under the eight complement-preserving relabelings. It also checks all four two-symbol complement pairs and finds no nonempty valid code.

The exhaustive four-base search is exhaustive because every length-three word has a distinct reverse complement, and a strand-closed four-word code must be a union of two of the 32 disjoint pairs. The permutation enumeration is exhaustive for full-size codes by the proved coordinate-bijection reduction. For larger even alphabets, existence and sharp maximality are established symbolically by disjoint-block union, not by numerical sampling.

The programs do not establish novelty against unavailable papers, measure DNA synthesis or sequencing outcomes, or perform independent review. The theorem does not claim a closed formula for numbers of optimal codes at every alphabet size.
