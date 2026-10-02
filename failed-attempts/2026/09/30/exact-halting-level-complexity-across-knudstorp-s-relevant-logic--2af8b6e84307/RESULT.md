# Exact halting-level complexity across Knudstorp's relevant-logic interval
## Finding
Let \(\mathcal L\) be the positive relevant language generated from propositional variables by \(\to,\land,\lor\). For every recursively enumerable set of formulas \(L\) satisfying
\[
\mathsf{TWJ}^{+}\subseteq L\subseteq
\mathrm{Log}(\mathcal P_{\mathrm{fin}}(\mathbb N),\cup,\varnothing),
\]
the membership problem for \(L\) is \(\Sigma^0_1\)-complete under computable many-one reductions. Equivalently, its complement is \(\Pi^0_1\)-complete.

Consequently the exact classification applies to each of
\[
\mathsf{TWJ}^{+},\ \mathsf C^{+},\ \mathsf T^{+},\ \mathsf E^{+},\
\mathsf R^{+},\ \mathsf S,\ \mathsf{SetFr},
\]
all of which are recursively enumerable and lie in the interval identified by Knudstorp.

## Assumptions and scope
Tile sets, formulas, and proofs are represented by any standard effective finite coding. Completeness is with respect to computable many-one reductions.

For a finite Wang tile set \(\mathcal W\), write \(\mathrm{NTILE}\) for the set of \(\mathcal W\) that do not tile \(\mathbb Z^2\). Knudstorp effectively associates to each \(\mathcal W\) a formula \(\psi_{\mathcal W}\in\mathcal L\) and proves, uniformly for every \(L\) in the displayed interval,
\[
\psi_{\mathcal W}\notin L
\quad\Longleftrightarrow\quad
\mathcal W\text{ tiles }\mathbb Z^2.
\]
Thus
\[
\mathcal W\in\mathrm{NTILE}
\quad\Longleftrightarrow\quad
\psi_{\mathcal W}\in L.
\]

The result classifies only recursively enumerable members of the interval. It does not assert that an arbitrary set of formulas between the two endpoints is recursively enumerable.

## Proof
First, \(\mathrm{NTILE}\) is recursively enumerable. Knudstorp records the equivalence
\[
\mathcal W\text{ tiles }\mathbb Z^2
\quad\Longleftrightarrow\quad
(\forall k\in\mathbb N)\,
\mathcal W\text{ tiles the finite octant }\mathbb O(k).
\]
For fixed finite \(\mathcal W\) and \(k\), whether \(\mathcal W\) tiles \(\mathbb O(k)\) is decidable by exhaustive search because both the region and the tile set are finite. Hence
\[
\mathcal W\in\mathrm{NTILE}
\quad\Longleftrightarrow\quad
(\exists k\in\mathbb N)\,
\mathcal W\text{ does not tile }\mathbb O(k),
\]
which gives a semidecision procedure for \(\mathrm{NTILE}\).

Second, \(\mathrm{NTILE}\) is recursively-enumerable-hard. Knudstorp explicitly invokes Berger's effective construction: from a Turing machine \(T\), one obtains a finite Wang tile set \(\mathcal W_T\) such that
\[
T\text{ halts}
\quad\Longleftrightarrow\quad
\mathcal W_T\in\mathrm{NTILE}.
\]
Thus the halting problem many-one reduces to \(\mathrm{NTILE}\). Together with recursive enumerability, this proves that \(\mathrm{NTILE}\) is \(\Sigma^0_1\)-complete.

Now fix a recursively enumerable \(L\) in Knudstorp's interval. His reduction is effective in \(\mathcal W\) and satisfies
\[
\mathcal W\in\mathrm{NTILE}
\quad\Longleftrightarrow\quad
\psi_{\mathcal W}\in L.
\]
Therefore
\[
\mathrm{NTILE}\leq_m L.
\]
Since \(L\) itself is recursively enumerable, \(L\in\Sigma^0_1\); hence \(L\) is \(\Sigma^0_1\)-complete.

Finally, if a set is \(\Sigma^0_1\)-complete under computable many-one reductions, then its complement is \(\Pi^0_1\)-complete: complementing both the source and target preserves the same reduction map. Therefore \(\mathcal L\setminus L\) is \(\Pi^0_1\)-complete.

Knudstorp states that \(\mathsf S\) is recursively enumerable and, separately, that \(\mathsf{TWJ}^{+},\mathsf C^{+},\mathsf T^{+},\mathsf E^{+},\mathsf R^{+}\), and \(\mathsf{SetFr}\) are recursively enumerable. He also places all seven systems in the interval above. The classification therefore applies to each named logic.

## Verification
The direction of the reduction was checked explicitly. Knudstorp proves
\[
\psi_{\mathcal W}\notin L
\quad\Longleftrightarrow\quad
\mathcal W\text{ tiles }\mathbb Z^2,
\]
so non-tiling, rather than tiling, reduces to theoremhood. This is the direction needed for \(\Sigma^0_1\)-hardness of \(L\).

The upper bound on non-tiling does not rely merely on classical undecidability. It follows from the finite-octant characterization: failure on one finite octant is a finite, decidable witness. The hardness direction likewise uses an effective halting-to-non-tiling construction, not only the statement that the domino problem is undecidable.

The endpoint and named-system hypotheses were checked against the source: the effective interval theorem includes all seven listed systems, and the source explicitly records their recursive enumerability.

## Relationship to prior work
Knudstorp proves undecidability throughout the interval and records recursive enumerability for the named relevant logics. He also derives consequences such as failure of the finite model property and proof-theoretic independence phenomena. The source does not state the resulting \(\Sigma^0_1\)-completeness classification.

The additional step here is to combine two ingredients already visible in the reduction architecture: finite octants make non-tiling recursively enumerable, while Berger's machine simulation makes non-tiling recursively-enumerable-hard. Since Knudstorp's formula map sends non-tiling exactly to membership in every logic in the interval, any recursively enumerable logic in the interval inherits exact halting-level completeness.

Targeted searches for the exact arithmetical-hierarchy formulation and for recursively-enumerable completeness of these positive relevant logics did not locate a stronger or equivalent published statement. The closest literature located was Knudstorp's undecidability theorem itself and the classical domino-problem construction on which its hardness direction rests.

## Limitations
This is a complexity sharpening extracted from a recent undecidability reduction, not a new tiling encoding or a new axiomatization.

The conclusion is conditional on recursive enumerability for an arbitrary intermediate \(L\). The interval contains set-theoretically many intermediate sets of formulas, and no claim is made that all are recursively enumerable.

The result gives the exact first arithmetical-hierarchy level for theoremhood and non-theoremhood, but it does not provide useful quantitative bounds on proof length, enumeration delay, or the size blow-up of the reduction beyond computability.

No claim is made here about richer signatures unless their theorem sets and the relevant effective embedding are separately verified.

## References
Søren Brinck Knudstorp, “Undecidability in Relevant Logic,” arXiv:2605.29880v1, first public version 2026-05-28.

Robert Berger, “The Undecidability of the Domino Problem,” Memoirs of the American Mathematical Society 66, 1966.
