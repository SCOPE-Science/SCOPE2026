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

The geometric chambers correspond to the empty set and skew-line subsets: any meeting pair of (-1)-curves has a singular principal block, and a pairwise-skew subset has matrix −I. A stable support B descends as a divisor; −K+B is nef, intersects B's components trivially, and has square 3+|B|, so −K+2B realizes the support over the ground field. Independently reconstructing incidence automorphisms from the images of an ordered skew sextuple gave 51,840 permutations, 25 classes and the stated 2,764 skew subsets. Computing the set action from this reconstruction agrees in every row with the frozen Markdown, including the fixed counts and Burnside sum 414,720. The equal line profile 3^9 does give distinct chamber profiles and counts 1 vs. 13. Over extensions they differ precisely when the degree is not divisible by three; both counts reach 2,764 at multiples of three. The cycle-power count and zeta formula follow from finite orbits.

## originality

FAIL

The chamber permutation representation is an instance of the preexisting parabolic-coset mark calculation, not merely of an abstract algorithm for arbitrary finite actions. Here this reduction covers all rows, because the stabilizer of a skew subset is exactly the stabilizer of the sum of its line classes, and a vector stabilizer in the real Weyl reflection representation is parabolic. Atkinson–van Willigenburg–Pfeiffer's Corollary 1 gives each of these permutation character values directly as a parabolic mark, and their §4.4 explicitly uses the computed exceptional-type marks and identifies the E6 parabolic classes. Apply the formula to each power and use ordinary divisor inversion to recover all cycle multiplicities. The exact chamber table is not claimed to appear verbatim in that paper; the failure is mechanical prior implication through the very same coset actions. Reformatting them as Frobenius support zeta functions and the elementary descent argument do not supply a distinct core claim.

## value

FAIL

Frobenius descent of chamber supports is a well-motivated invariant, and the reference table may be convenient, but its purported decisive new exact facts are direct readouts of existing parabolic coset marks. Neither assembling those fixed counts into cycles by divisor inversion nor realizing the fixed supports via the elementary nef divisor −K+B establishes a separate, independently needed unknown mathematical invariant. The negative assessment is of the computation as a research finding, not a claim that the table has no reference utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
