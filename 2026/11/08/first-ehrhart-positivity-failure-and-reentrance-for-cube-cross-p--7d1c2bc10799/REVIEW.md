# Scientific assessment

## Correctness — PASS
The join is a lattice polytope of dimension \(p+q+1\). Lattice slices give an exact integer-point convolution; the standard cube and cross-polytope generating functions yield \(h^*(z)=A_p(z)(1+z)^q\). Expanding the binomial-basis expression yields integral scaled coefficients. The full finite ranges in the claim are enumerated without omissions, from \(p+q=2\) through \(17\) and the four specified fixed-cube cases. The complete `verify.py` script reproduces all exact signs and fractions. Independent direct counts agree in 2,122 instances. The enumeration is a complete proof for the bounded statement, not a sample used to prove an unbounded assertion. Risk: software/arithmetic implementation not externally certified.

## Originality — PASS, provisional
The exact family-specific first-failure dimension, two exceptional pairs and nonmonotone reentrant fixed-cube profile were compared by mathematical-record searches and primary literature. Liu–Tao–Xin (2026, arXiv:2606.18794) proves general nonpreservation under joins; only its abstract was accessible, so a same-family result hidden in the full text is an unresolved priority risk. Liu (2026, arXiv:2610.06338) gives broad operation formulas; abstract only. Liu–Tsuchiya (2018, arXiv:1806.08403, Section 3) gives the numerator product for ordinal sums of antichains and lists negative cases around \((7,7)\), while also covering some Ehrhart-equivalent objects with one small factor. Its inspected text does not list or imply the complete reported cube–cross parameter census. Ferroni–Morales–Panova (2026) provides general order-polytope context, not the specified family classification. Mathematical-record matches on Cartesian log-concavity and cube–cross intersections concern distinct operations. No global priority certification is claimed.

## Mathematical value — PASS
The two factors separately have positive Ehrhart coefficients, yet their canonical join first fails positivity at a natural exact ambient-dimension cutoff. The exhaustive two-parameter boundary and the reentrance when the second factor gains dimensions are independently motivated geometry: they expose the limitations of preservation heuristics and a nonmonotone sign mechanism for a canonical regular-polytope pairing. A bounded complete classification with unusual reentrance is substantively informative, not a routine isolated coefficient recomputation.

## Residual limitations
No general classification above dimension 18 and no independent audit. A plausible 2026 paper's unavailable full text remains a genuine priority uncertainty. The calculations are fully reproducible but have not been externally independently verified.

Self-review: passed. Independent audit: not yet performed.
