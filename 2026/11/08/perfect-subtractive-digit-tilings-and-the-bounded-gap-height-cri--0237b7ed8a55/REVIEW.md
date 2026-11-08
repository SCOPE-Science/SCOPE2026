# Scientific assessment

## Correctness — PASS

The single claim concerns perfect subtractive digit tilings and an if-and-only-if threshold for linear witness height. Base-\(q\) residues force every permissible signed digit, proving injection. Iterated floor or ceiling division reaches the terminal states \(0,1\) or \(0,-1\); the opposite-sign support clears the remaining nonzero state exactly when that support is infinite. Bounded gaps give an explicit digit-length bound and therefore height at most \(1+q^{R+1}|n|\); arbitrarily long monochromatic runs give exact witnesses whose height ratio grows as \(q^r\). Mechanical partitions have exact digit-position counts \(\lfloor\alpha N\rfloor\), hence the claimed power-law counting bounds. All quantifiers, translations and endpoints are explicit. The supplied exact-integer checker passed; its finite evidence was not used to infer the infinite theorem.

## Originality — PASS (historical-priority qualified)

The closest direct source is Example 2.1 of Ding–Kiss–Niu–Pach–Sándor (arXiv:2610.40489v1), which already constructs the binary digit pairs and proves the **at-most-one** assertion. That pre-existing injection is expressly excluded from the originality claim. The new proposed contribution is the complete-signed-integer coverage criterion and, most importantly, the sharp if-and-only-if bounded-gap characterization of linear-size witnesses for arbitrary positional supports and fixed bases. This height distinction is not implied by the injection: arbitrarily long one-sided runs force unbounded witness inflation. Primary comparisons covered signed numeral expansions (Heuberger–Kropf–Prodinger), general inverse linear-form representation (Hegarty), and single-set bi-bases (Xiong–Tang). Relevant mathematical research-record searches and accessible prior claim fields found no covering equivalent. Because positional digit methods are classical, an unindexed equivalent remains a genuine priority risk.

## Mathematical value — PASS

Difference-set work under complementary polynomial density constraints raises the distinction between a sparse representation function and genuine coverage. This theorem establishes the exact universal-coverage boundary and identifies the necessary-and-sufficient structural condition under which the unique witnesses can be found without unbounded size inflation. The explicit counterexamples make the threshold sharp; balanced supports simultaneously realize every exponent \(0<\alpha<1\), exact multiplicity one, and linear representation height. These are structural classification facts for an infinite natural family, not a narrow numerical improvement or a restatement of injectivity.

## Closest work and limitations

Ding et al. (2026) provides the original binary injection and density setting; this must not be relabeled as novel. Heuberger et al. (2015/2017) covers classical uniform signed digit alphabets, without the arbitrary two-sign support and witness-height classification located here. Hegarty (2007) and Xiong–Tang (2014) treat different base-set conditions. The classification is restricted to positional digit sets with fixed base and does not determine optimal linear constants, all possible perfect difference pairs, or asymptotically constant-normalized counting functions. Historical priority requires independent scrutiny.

Self-review: passed. Independent audit: not yet performed.
