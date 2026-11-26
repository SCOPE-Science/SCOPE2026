---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In odd characteristic the parity-preserving theta torsor of a smooth plane quartic is equivariantly identified with quadratic refinements of its 2-torsion Weil pairing. Labeling a refinement by Q_0+B(a,·) gives parity Q_0(a) and affine triple-sum index a+b+c. Thus the unordered seven-sets with all even triple sums are exactly the specified heptads. A set is fixed by Frob^d iff its orbit length under Frob divides d; the least such positive d over all sets is the shortest cycle. I wrote an independent NumPy enumeration: construct the heptads by preserving the triple condition at each adjunction, enumerate ordered symplectic bases by choosing a symplectic pair and a basis of its complement, compute actual conjugacy orbits by conjugating with eight transvections (verified their orbit of one direction gives all 63, hence generates all transvections), and evaluate the three permutations per class. The probe gave 288 heptads and 23,040 bases with a fixed first vector. The full run gave 1,451,520 matrices in 30 actual classes, all 30 frozen profiles matched as a multiset, and the eight totals agreed exactly. The unique minimum-12 class has size 120,960 and profiles odd 1¹·3¹·12², even 6²·12², heptad 12²⁴. Its order is 12 from the heptad cycle and the symplectic theta action; its centralizer is 12. The ATLAS order-12 rows have centralizers 24, 24, 12, identifying it as 12C. The enumeration uses no assumed partition by paired theta signatures. This proves the asserted abstract spectrum and the necessary universal bound for curves, not the geometric sharpness of 12.

## originality

FAIL

The exact aggregate list was not located verbatim. Its whole abstract content is nevertheless mechanically determined by prior explicit action data: the ATLAS standard-generator actions and standard words for all class representatives (and equivalently all three permutation characters identified by Bergvall together with standard class data). This supplies more than an abstract existence theorem for an action. Computing a cycle minimum by reading the cycles of each of 30 specified permutations, and summing their printed class weights, leaves no new mathematical invariant to determine beyond that routine evaluation. Geometric realizability, which could distinguish an arithmetic theorem from the table, is explicitly not supplied.

## value

FAIL

The least extension degree is a natural question and the evaluated summary is convenient reference data. Here, however, its complete abstract answer and exceptional comparison are routine extractions of already specified small permutation data, and the transfer to curves neither realizes the exceptional class nor eliminates it geometrically. The independent computation is an effective correctness check, not a distinct substantive contribution beyond that extraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
