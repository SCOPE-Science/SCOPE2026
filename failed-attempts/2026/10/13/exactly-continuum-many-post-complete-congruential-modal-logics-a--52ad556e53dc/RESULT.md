# Exactly continuum many Post-complete congruential modal logics are neighborhood-unsound
## Finding
In the standard countable one-operator propositional modal language, the class of C-Post complete congruential modal logics that are neighborhood-unsound has cardinality exactly \(2^{\aleph_0}\).

More concretely, let \(\mathfrak A\) be the Boolean algebra of finite and cofinite subsets of \(\omega\), let \(\operatorname{At}(\mathfrak A)\) be its atoms, and let \(\operatorname{Mid}(\mathfrak A)\) be its elements other than atoms, zero, and one. For every bijection \(f:\operatorname{Mid}(\mathfrak A)\to\operatorname{At}(\mathfrak A)\), Krawczyk defines a modal algebra \(\mathfrak A_f\). His construction gives pairwise distinct minimal varieties \(\mathsf V(\mathfrak A_f)\), and the corresponding logics \(\tau_V(\mathsf V(\mathfrak A_f))\) are neighborhood-unsound. The family of such bijections has size exactly \(2^{\aleph_0}\), so the construction already realizes continuum many distinct neighborhood-unsound C-Post complete logics. Fritz’s theorem that the total number of C-Post complete congruential modal logics is \(2^{\aleph_0}\) gives the reverse inequality.

## Assumptions and scope
The language is the countable propositional modal language with one unary modal operator used in the cited work. “C-Post complete” means Post complete inside the lattice of congruential modal logics. “Neighborhood-unsound” means that no neighborhood frame validates the logic.

The result concerns the cardinality of the unsound C-Post complete subclass. It does not determine the exact cardinality of the neighborhood-complete C-Post complete subclass.

## Proof
Krawczyk takes \(\mathfrak A\) to be the Boolean algebra of finite and cofinite subsets of \(\omega\). Its atoms are the singletons, so \(\operatorname{At}(\mathfrak A)\) is countably infinite. The same source states that \(\operatorname{Mid}(\mathfrak A)\) is countable and in bijective correspondence with \(\operatorname{At}(\mathfrak A)\); hence it too is countably infinite.

Let
\[
\operatorname{Bij}=\{f:\operatorname{Mid}(\mathfrak A)\to\operatorname{At}(\mathfrak A): f\text{ is a bijection}\}.
\]
After choosing enumerations of the two countably infinite sets, \(\operatorname{Bij}\) is identified with the permutations of \(\omega\). Therefore \(\lvert\operatorname{Bij}\rvert=2^{\aleph_0}\): the upper bound follows because each permutation is a subset of \(\omega\times\omega\), while the lower bound follows by assigning to each subset \(S\subseteq\omega\) the permutation that swaps \(2n\) and \(2n+1\) exactly when \(n\in S\).

Krawczyk’s fundamental theorem states that \(\mathsf V(\mathfrak A_f)\) is minimal for every \(f\in\operatorname{Bij}\), and that \(f\ne g\) implies \(\mathsf V(\mathfrak A_f)\ne\mathsf V(\mathfrak A_g)\). Under the algebraic correspondence used there, each such minimal nontrivial variety yields a C-Post complete congruential modal logic. The same paper proves that no neighborhood frame validates \(\tau_V(\mathsf V(\mathfrak A_f))\). Thus the map
\[
f\longmapsto\tau_V(\mathsf V(\mathfrak A_f))
\]
is injective into the class of neighborhood-unsound C-Post complete congruential modal logics. This gives a lower bound of \(2^{\aleph_0}\).

Finally, Fritz’s cardinality theorem, reproduced as Theorem 3.1 in Krawczyk’s paper, states that there are exactly \(2^{\aleph_0}\) C-Post complete congruential modal logics altogether. Hence the unsound subclass has cardinality at most \(2^{\aleph_0}\), proving equality.

## Verification
The critical source statements were checked in the full open-access article: the finite-cofinite base algebra and its atom/middle sets; the definition of the bijection index set; pairwise distinctness and minimality of the generated varieties; the theorem that no frame validates the corresponding logic; and the reproduced Fritz theorem giving the total continuum upper bound.

The only added calculation is \(\lvert\operatorname{Bij}\rvert=2^{\aleph_0}\), verified by the explicit injection from \(\mathcal P(\omega)\) into pair-swapping permutations and the graph-of-a-function upper bound into \(\mathcal P(\omega\times\omega)\).

## Relationship to prior work
Fritz asked how many C-Post complete congruential modal logics fail to be the logic of a class of neighborhood frames. Krawczyk’s 2026 paper answers the existence side strongly by constructing an uncountable family of neighborhood-unsound examples, but states the size of the constructed family only as uncountable. The index set actually has cardinality continuum, and the paper proves that distinct indices give distinct varieties. Combining that exact lower bound with Fritz’s exact continuum upper bound for all C-Post complete congruential modal logics closes the cardinality question for the neighborhood-unsound subclass.

A companion 2026 preprint of Gyenis and Krawczyk concerns the neighborhood-complete side and proves an uncountable lower bound there; it does not provide a stronger statement that subsumes the exact unsound-side cardinality established here.

## Limitations
The theorem does not compute the exact number of neighborhood-complete C-Post complete congruential modal logics. It also does not distinguish the constructed unsound logics by finer syntactic or proof-theoretic invariants. The exact-cardinality conclusion depends on the standard countable modal language used in the cited sources.

## References
Krzysztof Aleksander Krawczyk, “Maximal Neighborhood Unsound Congruential Modal Logics,” *The Review of Symbolic Logic*, published online 30 September 2026, DOI 10.1017/S1755020326101294.

Peter Fritz, “Post Completeness in Congruential Modal Logics,” *Advances in Modal Logic* 11 (2016), 288–301.

Zalán Gyenis and Krzysztof Krawczyk, “Uncountably many maximally consistent neighborhood complete congruential modal logics,” arXiv:2609.04508 (2026).
