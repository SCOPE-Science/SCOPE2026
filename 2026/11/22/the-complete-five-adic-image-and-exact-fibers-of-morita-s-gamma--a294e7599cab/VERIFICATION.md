---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The signed product over a complete length-5^k interval is 1 modulo 5^k: the unit product is −1 by inverse pairing, against the odd-length sign. This gives a well-defined map on residues by continuity and approximation by nonnegative integers. The five-step ratios on a+5t are the displayed negative products of four units. Their leading nonzero digits are c_a at λ=(2,2,1,1,1); in the restricted series 5^(−λ) log U_a the terms modulo 25 are c_a+5P_a with deg P_a≤2 (the log-square correction when λ=1 is constant after dividing by 5 and reducing modulo 5). Over 5^s consecutive inputs the constant, linear and quadratic sums are divisible by 5^s, and the integral restricted-series remainder has sum divisible by 5^(s−1), by grouping five lifts of each residue and using its 1-Lipschitz property. Hence the leading digit of the block ratio is unchanged at precision s+λ. Iterating by a unit multiple and passing to the limit gives exact branch distance valuation ν_5(t−u)+λ, including s=0 from the original ratios. Each normalized branch induces bijections modulo every 5^m, so it fills its stated ball. The centers (1,−1,1,−2,6) give the stated disjoint image union and Haar measure 11/25; the larger balls contribute one per branch and the two smaller branches five per eligible residue modulo 5^k for k≥2, including k=2. Reducing the centers yields the level-one counts. A period must be divisible by five from the nonconstant level-one pattern; on branch a=2 a nonzero input shift divisible by five changes the value with exactly the valuation of the shift, establishing least period 5^k. A fresh finite replay exhaustively checked fibers through k=6, period closure, and a shift witness; it is not the all-depth proof. The frozen script was inspected, not executed.

## originality

PASS

The supported contribution is the two-scale local distance calculation at five, with its exact image, multiplicities, and minimal period. This does not claim novelty for Morita's definition, its recurrence, local analyticity, or congruence preservation. The strongest matching accessible prior statements establish those underlying properties or image/fiber decompositions of different maps, not the asserted five-adic classification.

## value

PASS

For a standard p-adic interpolation of factorials, image and multiplicity are natural invariants: they determine solvability and counts for inverse gamma congruences at every depth. At five the first two branches contract by an extra factor, so the precise range and fibers are not consequences of generic regularity. The branch isometries identify both where inversion is possible and why the finite multiplicities differ, rather than merely tabulating small moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
