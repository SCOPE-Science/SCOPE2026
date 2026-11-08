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

# Verification of the exact three-deck classification

The proof is self-contained in `RESULT.md`; this file documents executable finite cross-checks. Run `python verify_deck3.py` using Python 3 and only the standard library.

The checker enumerates every word with three ones at each length \(3\le n\le19\), totaling 4,845 source words. For each length, it groups the complete eight-entry scattered length-three deck and checks that the fibers are singleton or doubleton, every doubleton comprises exactly the two words prescribed by the involution, and every singleton has no legal partner. It confirms 370 doubleton classes in the tested range and exact equality to the finite double sum and quasipolynomial at every tested length.

For each word through length 16, an independent slow checker explicitly visits every strictly increasing triple of positions and matches its deck to a dynamic subsequence counter. The checker also evaluates 250 seeded words at lengths from 20 to 400; 62 have admissible partners, each verified against the dynamic deck, and checks equality between the double-sum and quasipolynomial counts through length 400. Finally it checks the shortest collision, `1000110` and `0110001`, at length 7.

These finite tests corroborate, but cannot establish by themselves, the all-length result. The infinite correctness argument is Steps 1–3 of `RESULT.md`, which prove exhaustive necessity, sufficient equality of all deck coordinates, uniqueness of the partner and a bijective collision count.

The reference conjecture is from Chrisnata et al., *On the Number of Distinct \(k\)-Decks: Enumeration and Bounds*, DOI:10.3934/amc.2021032, Section 5.3; the printed conjecture and its finite checks are prior work. Independent validation of this proof has not been performed.
