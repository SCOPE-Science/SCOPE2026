# Independent mathematical audit

## correctness

PASS

Necessity: simultaneous positive clades of rooted trees are laminar. Sufficiency: for any labeling of a support S compatible with positive H, build the hierarchy of positive clades; negative compatible queries become proper unions of at least two, but not all, children at their least positive ancestor. The cherry-contraction avoidance lemma gives binary refinements independently at each multifurcation omitting these negative unions; hence arbitrary labels occur iff H union S is laminar. A maximal rooted binary hierarchy contains n-2 nontrivial proper clades, so VC=n-2-|H|. In an online complete binary query tree the all-positive branch cannot repeat a query and must use distinct proper clusters outside H, yielding Ldim<=n-2-|H|; static lower bound gives equality; nonbinary trees cannot beat it. EGF U=x+z(e^U-1-U), inversion gives restricted Stirling coefficients {(n+k) over k+1}_{blocks>=2}. Independently checked all 15 binary trees at n4 and 105 at n5: every laminar support shattered, face polynomials 1+10z+15z² and 1+25z+105z²+105z³. These checks are bounded.

## originality

PASS

The unconditional n-2 VC/Littlestone dimensions and abstract counting of laminar hierarchies are definitively prior work. New surviving claim is the full if-and-only-if positive/negative shattering complex, its interpretation as query faces and dimension after arbitrary compatible positive history. The older positive-branch product factorization makes the conditional scalar extension mathematically close, but it does not itself state nor establish the all-support negative-avoidance theorem.

## value

PASS

Complete shattering-complex determination for a natural phylogenetic-clade membership class specifies exactly which query families realize every binary response pattern. Conditional adaptive capacity after arbitrary positive clade histories is a useful exact learning invariant, beyond an unconditional scalar dimension; tree-query semantics and avoidance constraints have mathematical substance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
