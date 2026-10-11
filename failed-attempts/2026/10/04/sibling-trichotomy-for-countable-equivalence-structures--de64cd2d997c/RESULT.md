# Sibling trichotomy for countable equivalence structures

## Finding

For a countable structure \(\mathcal A=(A,E)\) whose only nonlogical symbol is an equivalence relation, let \(\operatorname{sib}(\mathcal A)\) be the number of isomorphism types of countable structures bi-embeddable with \(\mathcal A\). Then
\[
\operatorname{sib}(\mathcal A)\in\{1,\aleph_0,2^{\aleph_0}\}.
\]
More precisely:

1. \(\operatorname{sib}(\mathcal A)=1\) exactly when only finitely many \(E\)-classes are nonsingletons.
2. \(\operatorname{sib}(\mathcal A)=\aleph_0\) exactly when \(\mathcal A\) has finitely many infinite classes, its finite class sizes are bounded, and it has infinitely many finite nonsingleton classes.
3. \(\operatorname{sib}(\mathcal A)=2^{\aleph_0}\) exactly when \(\mathcal A\) has infinitely many infinite classes or its finite class sizes are unbounded.

Thus Thomassé's \(1/\aleph_0/2^{\aleph_0}\) sibling trichotomy has an explicit class-size criterion for all countable equivalence structures.

## Assumptions and scope

An embedding of equivalence structures preserves both \(E\) and non-\(E\), so distinct source classes must go to distinct target classes, and a source class of size \(n\) can only go into a target class of size at least \(n\). An infinite source class can only go into an infinite target class.

For \(n\geq 1\), write \(c_n(\mathcal A)\in\mathbb N\cup\{\aleph_0\}\) for the number of \(E\)-classes of size exactly \(n\), and write \(c_\infty(\mathcal A)\in\mathbb N\cup\{\aleph_0\}\) for the number of infinite classes. “Finite class sizes are bounded” means that some finite \(K\) bounds the size of every finite class.

The statement concerns countable structures and ordinary relational embeddings. No computability assumption is used in the proof.

## Proof

First suppose \(c_\infty(\mathcal A)=r<\aleph_0\) and the finite class sizes are bounded. Define
\[
k(\mathcal A)=\max\{n\geq 1:c_n(\mathcal A)=\aleph_0\},
\]
with \(k(\mathcal A)=0\) if the displayed set is empty.

We claim that for any countable \(\mathcal B\) in the same bounded regime,
\[
\mathcal A\approx\mathcal B
\]
if and only if
\[
c_\infty(\mathcal A)=c_\infty(\mathcal B),\qquad
k(\mathcal A)=k(\mathcal B)=k,
\]
and \(c_n(\mathcal A)=c_n(\mathcal B)\) for every \(n>k\); when \(k=0\), equality is required for every finite \(n\).

For necessity, mutual embeddings give opposite injections between the finite sets of infinite classes, so their cardinalities agree. If \(k(\mathcal A)>k(\mathcal B)\), then infinitely many classes of size at least \(k(\mathcal A)\) in \(\mathcal A\) would have to map to distinct classes of at least that size in \(\mathcal B\), forcing some finite size at least \(k(\mathcal A)\) to occur infinitely often in \(\mathcal B\), a contradiction. Symmetry gives equality of the two \(k\)'s. Once the equally many infinite classes are matched, every embedding uses all infinite target classes for infinite source classes. For each \(t>k\), the number of finite classes of size at least \(t\) is finite, and mutual embeddings force these finite tail counts to be equal. Descending from the common finite size bound recovers \(c_n(\mathcal A)=c_n(\mathcal B)\) for all \(n>k\). If \(k=0\), this applies to every finite \(n\).

For sufficiency, match the infinite classes bijectively and match the finitely many classes of each size \(n>k\) exactly. If \(k>0\), enumerate all remaining finite source classes; each has size at most \(k\), so map them injectively into distinct target classes among the \(\aleph_0\) many classes of size \(k\). Do this in both directions. If \(k=0\), the exact finite multiplicities already give an isomorphism.

Hence, in the bounded regime with finitely many infinite classes, the sibling isomorphism types are parametrized only by
\[
(c_1,\ldots,c_{k-1})\in(\mathbb N\cup\{\aleph_0\})^{k-1}.
\]
If \(k\leq 1\), this parameter tuple is empty, so there is exactly one sibling. The condition \(k\leq 1\) here is equivalent to having only finitely many nonsingleton classes. If \(k\geq 2\), there are countably many possible finite tuples and infinitely many are realized, for example by varying \(c_1\); thus there are exactly \(\aleph_0\) siblings.

Now suppose \(c_\infty(\mathcal A)=r<\aleph_0\) but finite class sizes are unbounded. Any bi-embeddable copy must have the same \(r\) infinite classes and unbounded finite class sizes. Conversely, any two countable equivalence structures with the same finite number \(r\) of infinite classes and unbounded finite class sizes are bi-embeddable: match the infinite classes, then greedily send the enumerated finite source classes to distinct target finite classes of sufficiently large size. Unboundedness leaves a sufficiently large unused target class at every finite stage. There are \(2^{\aleph_0}\) nonisomorphic structures in this bi-embeddability class: for each \(X\subseteq\mathbb N\), take \(r\) infinite classes and, for every \(m\geq1\), take \(1+\mathbf 1_X(m)\) classes of size \(2m\). Distinct \(X\)'s give distinct class-size multiplicities. Since there are at most \(2^{\aleph_0}\) countable structures up to isomorphism, the sibling number is exactly \(2^{\aleph_0}\).

Finally suppose \(c_\infty(\mathcal A)=\aleph_0\). Every countable equivalence structure with \(\aleph_0\) infinite classes is bi-embeddable with \(\mathcal A\): enumerate all source classes and send them injectively into distinct infinite target classes. There are \(2^{\aleph_0}\) nonisomorphic such structures, obtained for example by choosing, independently for each \(n\geq1\), whether to add one finite class of size \(n\) to \(\aleph_0\) infinite classes. Again the continuum upper bound is automatic for countable structures.

These cases are exhaustive and give the three stated criteria.

## Verification

The proof was checked case-by-case against the class-size behavior forced by embeddings. In particular, the bounded case isolates the largest finite size occurring infinitely often and shows exactly which lower multiplicities can be absorbed; the unbounded and infinitely-many-infinite-class cases supply explicit continuum families of pairwise nonisomorphic siblings.

No finite computation is used as a substitute for the infinite argument.

## Relationship to prior work

Bazhenov, Fokina, Rossegger, and San Mauro classify bi-embeddability behavior of countable equivalence structures in computable-structure-theoretic terms. Their 2017 preprint explicitly notes that any two equivalence structures with unbounded character and the same number of infinite classes are bi-embeddable, and gives detailed bounded-character criteria in the computably bi-embeddably categorical regime. Fokina, Rossegger, and San Mauro later introduced and studied “b.e. triviality,” meaning that a bi-embeddability type contains only one isomorphism type. Laflamme, Pouzet, Sauer, and Woodrow study sibling counts for \(\aleph_0\)-categorical structures, while Braunfeld and Laskowski study sibling-count trichotomies through universal theories.

The exact three-way class-size criterion above was not located in those sources or in the database searches described in the accompanying review. It packages the equivalence-structure embedding classification into a complete sibling-count theorem rather than a computability classification.

## Limitations

The result is specific to pure equivalence relations and ordinary embeddings. Adding labels, functions, orders, or extra relations can change sibling counts. The originality search covered the most directly relevant modern bi-embeddability and sibling literature but is not a proof that no older or differently phrased source contains the same corollary.

## References

1. N. Bazhenov, E. Fokina, D. Rossegger, L. San Mauro, “Degrees of bi-embeddable categoricity of equivalence structures,” arXiv:1710.10927 (first public version 2017-10-30); *Archive for Mathematical Logic* 58 (2019), 543–563, DOI 10.1007/s00153-018-0650-3.
2. E. Fokina, D. Rossegger, L. San Mauro, “Bi-embeddability spectra and bases of spectra,” *Mathematical Logic Quarterly* 65 (2019), 228–236, DOI 10.1002/malq.201800056.
3. C. Laflamme, M. Pouzet, N. Sauer, R. Woodrow, “Siblings of an \(\aleph_0\)-categorical relational structure,” arXiv:1811.04185; *Contributions to Discrete Mathematics* 16 (2021).
4. S. Braunfeld, M. C. Laskowski, “Counting siblings in universal theories,” arXiv:1910.11230; *Journal of Symbolic Logic* 87 (2022), DOI 10.1017/jsl.2022.3.
5. E. Fokina, T. Kötzing, L. San Mauro, “Limit Learning Equivalence Structures,” arXiv:1902.08006; PMLR 98 (2019), 383–403.
