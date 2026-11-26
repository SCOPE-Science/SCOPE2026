---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A simplex is precisely a triple-family of support size ≤n−3. A fixed r-vertex simplex with o induced orbits contributes (−1)^(o−1) to reduced Lefschetz, also correctly counting the empty face as −1. On the Boolean set of cycles the unrestricted supported-family weight sum is one on stable subsets of size ≤2 and zero otherwise. Inverting gives (−1)^c(1−a+binom(a,2)−b); taking complements of sizes 0,1,2 gives the checked polynomial with the stated sign after converting the Lefschetz trace in degree n−6. Independently, the support map from nonempty faces onto subsets of ranks 3 through n−3 has the order-preserving section U↦binom(U,3), with section after support pointwise ≥identity. These maps commute with relabeling; this gives the same homology representation on the rank-selected order complex. I enumerated fixed-chain contributions there on every conjugacy class for n=7,8,9,10 (15,22,30,42 classes), reproducing the polynomial. For the Pieri sum, λ=(n−k,ν) has k≤4 and first row ≥3, bigger than any input μ first row (≤2), so interlacing depends only on the tail ν. Checking all tails of sizes 0 through 4 gives coefficient one at (1,1,1,1), (2,1,1), (2,2) and zero at the rest, proving stabilization across the full range. Evaluating the small induced characters gives 1−2a+4 binom(a,2)−2b−6 binom(a,3)+2ab+6 binom(a,4)−2 binom(a,2)b+2 binom(b,2), exactly the untwisted polynomial. Sign twist conjugates the three partitions. Neither trivial nor sign appears, so no A_n fixed vectors occur. The frozen checker was inspected, not run, and the finite corroboration is not used as a universal proof.

## originality

FAIL

A distinct indexed Result gives exactly the full rational character of the same ordinary open triple complex in all the claimed degrees and throughout a larger parameter range, by the same fixed-face/Möbius calculation. Rational S_n modules are determined by their characteristic-zero characters, so the explicit labels do not escape this coverage. There is also a direct reduction to Solomon's general rank-selected Boolean representation theorem and a bounded ribbon/Pieri expansion. The exact catalogue match has a later displayed date; this is not an inference about priority or independence.

## value

FAIL

The symmetry of a natural neighborhood complex is a worthwhile invariant, but the full character is already explicitly covered. The multiplicity-free labels add no new independent information and are mechanically obtainable by standard ribbon/Pieri expansion. The original proof's central fixed-point calculation also overlaps, and the record supplies no additional structural theorem beyond that exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
