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

Frobenius makes linear changes valid in the truncated algebra, and Jordan ranks are unchanged by extending the field. In odd characteristic the three nonzero quadratic ranks reduce to z², xy, xy+z². The first two split into monomial chains by parity or by exponent difference. For the third, the tensor calculation can be recovered in R=k[t]/(t^p) with primitive action t=X+Y. A J_p factor gives a free tensor product, by changing variables from X,Y to t,Y, using Y^p=0. For 2≤b<p, multiplication on k[X,Y]/(X²,Y^b) has two blocks and (X+Y)^b=bXY^(b−1)≠0, yielding lengths b+1,b−1. The resulting J_2 recurrence gives the short-range tensor rule by induction up to a+b=p+1 (intermediate lengths are at most p−1). For a≤b<p and a+b>p+1, tensor the exact sequence 0→J_(p−b)→J_p→J_b→0 with J_a. The middle term is free; elementary divisors of an inclusion into a free R-module replace each nonfree kernel block of length l with a quotient block of length p−l. The short-range calculation of J_a⊞J_(p−b) then gives lengths b−a+2i−1 for 1≤i≤p−b, with a+b−p free blocks by dimension. Thus for fixed b and j<p the contributing a form the indicated step-two interval, with cardinality min(b,p−b,j,p−j). Both split lengths (p±1)/2 give min(j,p−j). The xy chain multiplicities give 4 min(j,p−j), and the remaining dimension gives (p²+1)/2 length-p blocks, different from p at rank two. The rank counts follow by choosing a radical and a nondegenerate form on its quotient: symmetric 2×2 matrices have exactly q² singular members (ac=b², split on a=0), leaving q²(q−1) nonsingular ones; subtract the lower ranks from q⁶ for rank three. For a lift, at each degree d≥3 write its current correction as a sum of the invertible gradient's linear forms times degree-(d−1) terms. The resulting near-identity substitution descends because every maximal-ideal element has pth power zero, is invertible by the filtration, and cancels that degree only, terminating at 3(p−1). Taking its inverse gives the stated direction φ(Q)=f. The number of lifts per form is q^(p³−10) by dimensions. I inspected the supplied checker.py and recorded checker_output.txt, without executing them. A separate direct check formed the columns of each (xy+z²)^t by binomial expansions truncated at exponent p, took ranks mod p, and second-differenced them; it agreed at p=3,7,11 (at p=11 the ranks from t=0 to 11 were 1331,1150,973,804,647,506,385,284,199,126,61,0). Neither diagnostic is used to extrapolate to all primes or extension fields.

## originality

PASS

The distinct contribution is the complete rank-stratified three-variable regular-multiplication classification, with an explicit all-odd-prime rank-three partition and its extension to the full nonsingular quadratic-leading stratum. Do not credit the modular tensor rule, symmetric-matrix rank counts, binary partitions, or the formal Morse method as new. The lower-rank cases and much of the computational machinery are already covered. The inspected evidence does not establish prior equivalent coverage of the ternary classification.

## value

PASS

The quadratic layer is a natural six-dimensional coefficient space in the regular representation. The result identifies exactly what its regular multiplication remembers (quadratic rank), makes the full-rank versus rank-two projective-block jump quantitative, and gives the entire Jordan type and size of the nonsingular quadratic-leading stratum. This is a reusable structural classification, not a tabulation at isolated primes or merely an application of the block rule to one pair of lengths. It does not address degenerate lifts, characteristic two or general modules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
