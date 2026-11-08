# Scientific review: two-level autocorrelation of subset-sum profiles

## Correctness — PASS

The theorem is quantified over every odd modulus \(n\ge3\) and every finite multiset of *unit* residues. Fourier inversion gives the exact autocorrelation constants from unit Fourier magnitudes. The algebraic identity \(1+z=(1-z^2)/(1-z)\) turns the magnitude conditions into a linear logarithmic relation. For each nonprincipal even character of the unit group, its primitive conductor is a divisor of the modulus; evaluating at corresponding roots and weighting by that primitive character recovers a nonzero Gauss-sum/Dirichlet \(L(1,\chi)\) factor. Vanishing of every even character coefficient, together with the principal coefficient, forces signed multiplicities to be doubling invariant. The reverse implication is elementary. All arithmetic ranges and the empty-multiset boundary are covered. The exact-arithmetic checker exhausts binary multiplicities for small admissible moduli and tests larger moduli. Its finite tests are corroboration, not the infinite proof.

Risk: the proof relies on the classical (established, external) Dirichlet nonvanishing theorem and primitive Gauss-sum identity; it does not independently reprove those theorems.

## Originality — PASS within inspected sources

Gaitanas (2023, arXiv:2304.14141, Theorems 2.3 and 2.4) studies completely uniform nonempty subset sums and proves signed doubling-progression structure under prime-power or additional composite-modulus hypotheses. Its June 2023 correction modifies an order assumption in Theorem 2.4. The present statement instead exactly characterizes **two-level cyclic autocorrelation / Fourier-unit magnitudes** for **every odd modulus**. It includes non-equidistributed examples, so it is neither a restatement of the sufficient progression construction nor implied by the prime-power converse alone. Ciprietti–Glaudo (2023, arXiv:2301.04635v2, Section 4) establish cyclotomic-unit relationships and certain full-subset-sum reconstruction results; Proposition 4.6 assumes a special class of moduli and does not give this exact all-odd autocorrelation equivalence. Relevant mathematical-record searches and accessible historical-claim comparisons identified no full-coverage theorem.

Risk: related cyclotomic-unit or spectral literature may contain an unindexed equivalent. This is self-review, not independent certification.

## Mathematical value — PASS

The result is a natural complete characterization of a rigid autocorrelation invariant of additive subset-sum distributions. It gives a structural signed-doubling criterion for all odd moduli, sharpens the relationship between a well-studied equidistribution problem and its Fourier magnitudes, and exhibits an explicit Fourier-flat but nonuniform profile. The analytic-number-theory character transform bridges prime-power and arbitrary composite moduli. This is more than a numerical table, a normalization check, or a parameter substitution; the iff statement holds for all finite multisets and all odd moduli.

Limitations: no necessary-and-sufficient criterion for full nonempty-sum equidistribution is claimed at arbitrary composite moduli; nonunits and even moduli are outside scope.

Self-review: passed. Independent audit: not yet performed.
