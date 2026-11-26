# Independent mathematical audit

## correctness

PASS

The cover of token edges by q(2q−1) lifted triangles is an edge partition: the moved parent edge determines its petal and the common token determines the external-token lift or the within-petal lift. The hub–leaf coloring lifted by pair parity saturates every triangle; maximum cuts are therefore exactly the colorings with no monochromatic lifted triangle. Fix the two hub-token colors per petal. The within-petal color has one completion for a pure hub pair, two for a mixed pair. Each cross-petal 2×2 array is independent and must obey its two row and two column forbidden-constant constraints. For two equal pure states the array has no zero row/column after color symmetry (2 permutation, 4 three-one, 1 all-one); opposite pure states force exactly the two permutations. Pure/mixed has 9 row-admissible arrays and subtracts 1+4−1 invalid arrays; mixed/mixed has 9 and subtracts 2+2−1, giving 5 and 6. Grouping hub states gives mixed site weight 4 and the displayed multinomial sum. The 1/2 quotient is free color reversal, not a quotient by petal permutations. For the asymptotic, the two all-equal pure states contribute 2 to the ordered normalized sum. A positive fraction of mixed petals, or positive fractions of both pure types as in the proof, incurs an exp(−Ω(q²)) penalty against the exp(O(q)) total site weights. Otherwise a pure majority with d defects contributes at most binom(q,d)8^d(5/7)^(dq/2) for either color. Summing over d≥1 tends to zero by the binomial bound. This proves both asymptotic and uniform-optimum concentration. Independent direct enumeration fixing one token color gave (value, count)=(2,3),(12,97),(30,17239) for q=1,2,3; a separate hub-completion sum matched the six listed counts, not a substitute for the asymptotic proof.

## originality

PASS

The scalar cut value and the underlying triangle-lift method are covered. Pass only the distinct optimizer multiplicity and concentration: exact local weights and all-q evaluation of the nonmonochromatic-coloring count, and dominant-state asymptotics. The most closely matched inspected records concern distinct hosts or the scalar value. The assigned record's own catalogue hit is not independent corroboration.

## value

PASS

A natural frustrated graph family already has an accessible scalar optimum; the labelled maximum-cut multiplicity measures an independent feature. The exact solution captures a large number of optimal cross-petal colorings together with strong concentration on a single unordered hub pattern, information not given by the cut value. This is an all-parameter ground-configuration benchmark, not a small-instance rerun.

The dated certificate retains the supplied scientific assessment, sources and limitations.
