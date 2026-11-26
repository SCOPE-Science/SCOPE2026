# Independent mathematical audit

## correctness

PASS

For a triangle, its three cyclic gaps must each be at most 2 or at least n−2. When n≥7 they cannot all be at most 2, so one is n−2 and the other two are 1. This identifies the complex with tight triple-cycle independence. Kim–Kim explicitly use mod two in §1; their Theorem 3.1 with k=3 gives the stated unique degree, and universal coefficients bound rational Betti numbers in that degree and kill the others. For augmentation, each chosen vertex orbit contributes a sign −1; the trace is (−1)^(d_n+1) times the weighted orbit assignments. Rotations repeat a bit word of length gcd(n,j); even for lengths 1 and 2 the periodic no-111 condition is encoded by closed walks of the stated two-bit transfer, whose spectrum is 0,1,i,−i. The identity trace gives rank, not an inference of torsion-freeness from mod two. A reflected word reduces to a path with two endpoint pairs forbidden from being 11: a fixed vertex is flanked by two copies of its neighbor bit, and an exchanged pair is flanked by its next inward bit. The remaining restrictions are exactly internal no-111. The weighted path count with the given start/end vectors has F(2)=F(3)=−1 and satisfies F(l+2)=−F(l) by the stated annihilation and Cayley–Hamilton. The three lengths and the prefactor give the traces in all four residue classes, including n=7 and the two even reflection axes. Averaging is not needed to identify the stated modules: the traces match the rational line and quarter-turn plane on every group element. Independent replay: python3 /workspace/review-evidence/reproduce.py 4, log /workspace/review-evidence/4.txt; graph triangles and 230 direct signed characters for 7≤n≤16, and independently built augmented mod-two boundary ranks through n=13. Finite checks corroborate the proof but do not establish general concentration. The supplied verifier and stored output were inspected, not executed.

## originality

FAIL

Exact source comparison with the distinct indexed tight triple-cycle noncover result, 2c98e1a11ba7, shows full coverage via reversible equivariant Alexander duality with ambient permutation sign. It treats n≥6, hence covers every frozen n≥7 as a character assertion about the equivalent dual object. This does not establish priority or dependence; its path date is later. The ordinary independence/homotopy literature alone would not determine the action.

## value

FAIL

The quarter-turn plane and alternating line are meaningful distinctions from ordinary Betti numbers. But the frozen scope adds no mathematical information to the exact indexed equivariant dual character: multiplication by one explicit sign and relabeling the homological degree recovers every case. No further genuinely distinct invariant is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
