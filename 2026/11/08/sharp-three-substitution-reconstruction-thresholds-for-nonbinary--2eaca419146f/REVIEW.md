# Scientific review

## Correctness — PASS

The exact-distance sphere intersection is derived by disjoint coordinate types, with the same multiplicity sum in two forms. Substitution of the six possible center separations yields six closed expressions. A positive-coefficient comparison proves that distances \(3\) through \(6\) never maximize; the independent comparison between distances \(1\) and \(2\) yields a strict switch at \(q=3\) versus \(q\geq4\), for every \(n\geq6\). The reconstruction threshold follows from an intersection-size characterization of worst-case ambiguity. The standalone checker verifies exact enumeration and algebra for bounded parameters and is not substituted for the proof. Risks: proof applies only to the stated integer ranges, and no external formal or independent audit has been performed.

## Originality — PASS against accessible literature, with priority risk

Papadopoulou et al. (arXiv:2610.30001) treat binary fixed-weight substitutions and do not derive a nonbinary exact-three distance optimizer. Junnila et al. (arXiv:2606.09158) establish general Hamming **ball** intersection formulas, not the claimed optimized intersection of equal-radius **spheres** for all nonbinary alphabets and blocklengths. Danoyan's 2013 two-sphere work is binary. Existing Hamming-scheme intersection number formulas can compute the six quantities individually; they are credited as background, not claimed new. The new assertion is a uniform strict maximization and an exact zero-error reconstruction threshold with a ternary phase transition. Residual risk: an older paper or database could have optimized exactly these known intersection numbers; no definitive historical-priority claim is made.

## Value — PASS

A recently studied exact-weight substitution reconstruction channel makes the maximum common-output count an operationally natural quantity: it equals the precise number of distinct observations at which worst-case ambiguity stops. Extending the binary focus to all nonbinary alphabets changes the extremal geometry sharply at three symbols versus four or more, and provides an explicit all-length threshold rather than another one-parameter lookup of intersection counts. The result can inform read-budget guarantees, even though it supplies no efficient decoding method and does not solve error models of other radii.

## Closest literature and limitations

- V. Papadopoulou et al., arXiv:2610.30001 (2026); binary exact-weight substitution reconstruction.
- V. Junnila et al., arXiv:2606.09158 (2026); intersections of Hamming balls, including broader multi-center questions.
- H. Danoyan, Mathematical Problems of Computer Science 39 (2013), 119–124; binary sphere intersection formulas.
- Classical Hamming association-scheme intersection numbers are known, and earlier literature not exhaustively inspected could subsume the maximization.

Self-review: passed. Independent audit: not yet performed.
