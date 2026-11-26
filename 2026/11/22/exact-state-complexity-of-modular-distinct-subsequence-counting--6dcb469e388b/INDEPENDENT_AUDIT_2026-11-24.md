# Independent mathematical audit

## correctness

PASS

Each new ending-in-c subsequence is the unique concatenation of an old subsequence and c; old words ending in c are already included in this set. The shifted ending counts obey the two shear recurrences and the count including empty is x+y-1, giving acceptance x+y=1. The legal blocks 0 and 10 generate the same finite group as the two shears (inverse is a positive power). Over a prime-power residue ring a primitive column has a unit coordinate; eliminate the other by a shear, using a signed swap if necessary. A remaining unit diagonal diag(d,d^-1) is the product E12(d)E21(-d^-1)E12(d)E12(-1)E21(1)E12(-1). CRT combines the local elementary coefficients, and every elementary shear is a power of the corresponding unit shear. Thus the group is all SL2 over the residue ring; Bezout completion gives transitivity on primitive columns and rows. The last-zero and last-one layers are both reachable, by legal blocks and an appended 1 respectively. For distinct vectors in either fixed layer, after sending the first to (1,0), test with row (1,0) if the other's first coordinate differs from 1, otherwise (1,1); pull back and realize the row via a legal suffix, prepending 0 and absorbing its matrix when starting in the last-one layer. Cross-layer states are separated by starting the suffix with 10 and then taking the desired group element; the last-one layer goes to the sink immediately. The sink is reachable by 11 and is the only state with no accepting continuation. Prime-wise counting gives J2(m) per layer. This handles all m>=2, including m=2 and nonfields. Independent bounded replay `python3 /tmp/opencode/modular-review.py` used backward state-pair distinguishability for m=2..10 and verified 2,295 cases by direct subsequence-word sets including empty. Frozen checker.py was inspected, not run; the algebra, not the finite check, establishes the all-moduli result.

## originality

PASS

The contribution is the exact legal-input quotient with the adjacent-one prohibition, not the coprime-pair encoding or unrestricted count. The closest Resultary records genuinely overlap on either the unrestricted statistic or the same constraint for a different statistic; none inspected establishes the claim. No relative priority is inferred from their common date.

## value

PASS

11 avoidance is the elementary nontrivial binary run restriction, and the question asks exactly how it changes the modular state complexity for a natural word statistic. The result demonstrates both that no arithmetic states are lost and that the entire live layer is duplicated without any collapse, across composite as well as prime moduli. The legal-block lemma and same-/cross-layer separators explain why; the formula is a reusable exact baseline rather than a product bound or a handful of modular examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
