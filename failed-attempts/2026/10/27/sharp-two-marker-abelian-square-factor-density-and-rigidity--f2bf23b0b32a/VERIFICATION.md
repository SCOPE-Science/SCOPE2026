---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The parity of the total number of ones permits only zero or two; the zero-only count is floor(max(a,b,c)/2). Each distinct two-one factor is encoded uniquely by its outer gaps (i,k), and its halves contain one one each iff i+k≡b mod 2 and |i−k|≤b. The alternating row and column sums give the stated rectangle parity term. In the corner i−k>b put i=k+b+2r, r≥1; counting all k≥0 and removing k≥c+1 gives H(a−b)−H(a−b−c−1), and the other corner is disjoint and symmetric. This also covers zero gaps and the word 11. Uniform row parity and area comparison incurs O(a+b+c+1) error. With s=a+b+c and a≤c, for b≤a and h=c−a the strip-area deficit from s²/8 is 2(b−s/4)²+[h²−(h−b)₊²]/2. For b>a and a>0, area ≤ac<a(s−2a)≤s²/8, with zero area if a=0. Hence the unique positive-sum maximizing proportions are (3/8,1/4,3/8). Continuity and compactness give rigidity for all asymptotically maximizing sequences, not just exact maximizers. For gaps (3t,2t,3t), summing even-difference diagonals gives 4t²+3t+1 two-one factors, to which floor(3t/2) must be added; padding outer zeros gives the lower bound at intermediate lengths. A separate direct substring enumeration on all 2197 triples with 0≤a,b,c≤12 corroborated the formula; the supplied scripts were inspected, not executed. Neither the enumeration nor the Finding claims a finite maximum formula.

## originality

FAIL

Two indexed comparators jointly give the actual discrete count and all continuous extremal information, not merely matching parameters: 9387a2a4a9ec supplies the exact parity-band identity and a uniform count-to-area comparison for exactly two ones, including zero gaps; 8655f359bb67 supplies the same continuous band's global bound and unique positive-area equality proportions, the identical explicit lower witness, and the sharp coefficient on a covering run-restricted class. Closed-form summation of the two parity corners and the compactness corollary do not leave a distinct result. This decision is about available mathematical coverage, not chronological priority.

## value

FAIL

The fixed-weight extremal problem and rigid near-maximizing ratios constitute a natural mathematical question. In the presence of the indexed exact discrete formula, uniform continuous reduction, unique maximizing area point and identical witness, the remaining finite simplification and rigidity corollary are routine, not a new independently useful invariant or mechanism. No genuine surviving repair is identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
