# Review of exact two-layer metric-circle covering radii

## Correctness (PASS)

The exact theorem covers every \(L,s>0\) and \(N\ge1\) with intrinsic circle distance and centers restricted to the two-point product. For \(r<s\), the projected sheet arcs are disjoint by layer and demand at least \(\lceil L/(2r)\rceil\) centers each. For \(r\ge s\), projecting to each sheet and comparing total arc lengths yields \(L\le2rN-2s\lceil N/2\rceil\). These exclude radii below both branches. Explicit separate-sheet equispacing realizes one branch. The alternating cyclic construction, with a single short-short gap for odd \(N\), realizes the other branch; gap lengths sum to \(L\) exactly. The boundary \(N=1\) is treated separately. The attached exact-fraction checker passes 7,200 sets of construction and strict smaller-radius tests, independently of the proof's universal quantifiers.

## Originality (PASS, provisional)

Cieliebak--Cieliebak (2026), arXiv:2611.15599v1, formulate a general conjectural covering inequality and prove several restricted cases, including graph-theoretic cycle results. They do not give a continuous two-layer intrinsic-circle \(N\)-center formula. Allagan (2026), arXiv:2601.03488v1, studies finite prism graph domination and counts, not continuous-circle products or variable real separation. Public research records concerning intrinsic multipath graph nets and metric-ladder distance moments concern different geometries and invariants. Searches for alias formulations such as circular prism covering, a circle times two-point metric, and parity transition returned no equivalent formula. Priority is not independently certified; unindexed older covering literature remains a risk.

## Mathematical value (PASS)

The claim is a complete natural two-parameter \(N\)-center classification for the simplest non-tree continuous-by-discrete product. The formula distinguishes the mixed-sheet and independent-sheet phases and exhibits a sharp separation threshold with an odd-even slope effect. It supplies a concrete exact model for the recently proposed metric-product covering program, rather than an isolated example or numerical improvement. It does not solve that program's general conjecture.

## Independent status and limits

The tests use finitely many rational parameters, while the proof handles arbitrary real parameters. Only explicit optimizers, not a classification of all optimizers, are asserted. Primary-source and public-record searches support but cannot certify global publication priority.

Self-review: passed. Independent audit: not yet performed.
