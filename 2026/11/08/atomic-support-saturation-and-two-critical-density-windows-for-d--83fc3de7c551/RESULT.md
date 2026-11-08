# Atomic-support saturation and two critical density windows for directed simplicial cups

## Finding

Consider a finite complete directed simplicial cup with a finite nonempty color set \(A\), at least two colors, a nonempty vertex set of each color, and a fixed finite nonempty set of local proposition letters for each color. Assume that distinct vertices of the same color are never connected by a directed edge (reflexive loops at every vertex are implicit). For each vertex \(x\), its **atomic type** \(u(x)=(\chi(x),\tau_x)\) records its color and full local truth assignment. Let \(U_a\) be the realized atomic types at color \(a\), \(r_a=|U_a|\), and \(m_u\) the multiplicity of atomic type \(u\).

**Theorem A (exact modal quotient and census).** The number of classes of nonempty faces under agreement on the true/false/undefined status of **every** formula of the three-valued cup belief language is at least
\[
N_0=\prod_{a\in A}(r_a+1)-1.
\]
Equality holds **if and only if** the following first-order support-uniformity condition holds: for each ordered pair of realized types \(u,v\) on different colors, either every vertex of type \(u\) has at least one outgoing edge to a vertex of type \(v\), or no vertex of type \(u\) has such an edge. Consequently, for a fixed labeled colored vertex set with fixed local valuations, the **exact** number of directed cups attaining the minimum \(N_0\) is
\[
C(\mathbf m)=\prod_{u,v:\ \chi(u)\ne\chi(v)}\bigl(1+(2^{m_v}-1)^{m_u}\bigr).
\]
If directed edges from type \(u\) to type \(v\) occur independently with probability \(p_{uv}\), the exact probability of minimal modal quotient is
\[
Q(\mathbf m,\mathbf p)=\prod_{u,v:\ \chi(u)\ne\chi(v)}\left[(1-p_{uv})^{m_um_v}+\bigl(1-(1-p_{uv})^{m_v}\bigr)^{m_u}\right].
\]
All products are over **ordered** pairs of atomic types on distinct colors. The theorem concerns equality of three-valued modal theories, not isomorphism of faces or standard two-valued bisimulation.

**Theorem B (two sharp random thresholds).** Fix an integer \(k\ge2\). Take exactly \(n\) labeled vertices of each of \(k\) colors, make each local valuation constant within its color, include every multicolored face, and independently choose each ordered cross-color directed edge with probability \(p_n\). There are precisely \(2^k-1\) atomic face signatures. Put
\[
h_n(p)=(1-p)^{n^2}+\bigl(1-(1-p)^n\bigr)^n.
\]
Then exactly
\[
\Pr\bigl(\text{exactly }2^k-1\text{ modal face types}\bigr)=h_n(p_n)^{k(k-1)}.
\]
For any fixed \(c\ge0\), the sparse critical window \(p_n=c/n^2\) has limit \(\exp(-k(k-1)c)\). For any fixed real \(c\), the dense critical window \(p_n=(\log n+c)/n\) (for large enough \(n\)) has limit \(\exp(-k(k-1)e^{-c})\). More generally, the probability tends to zero if both \(n^2p_n\to\infty\) and \(n(1-p_n)^n\to\infty\); it tends to one if either \(n^2p_n\to0\) or \(n(1-p_n)^n\to0\). Thus there are two separated sharp transitions, with full modal-type collapse at both the very sparse and the sufficiently dense extremes.

## Assumptions and scope

A **cup** contains every nonempty face consisting of at most one vertex of each color. A directed cup is obtained by assigning all reflexive edges and arbitrary ordered edges between vertices of distinct colors. In the belief semantics used here, an atom of color \(a\) is undefined at a face without an \(a\)-vertex; Boolean connectives obey weak Kleene definedness; \(\Box_a\varphi\) at a face with \(a\)-vertex \(x\) inspects all faces \(Y\) containing \(x\) that are accessible from \(x\), is undefined if no such \(Y\) defines \(\varphi\), and is otherwise true exactly when all such defined instances are true. It is undefined at a face without color \(a\). Write \(\Diamond_a\varphi=\neg\Box_a\neg\varphi\). All statements use this precise partial-modal semantics, not an unqualified two-valued Kripke translation.

Local atomic types record all proposition letters under consideration. For the infinite ambient supply of letters, the statement applies when valuation depends on finitely many letters and all remaining letters are assigned uniformly by color/type, so distinct types are separated by a finite literal formula. Every colored vertex set is fixed in the exact labeled census; no division by automorphisms or vertex permutations is performed. Distinct colors may have different numbers of atomic types and different multiplicities.

## Proof

**Step 1 — atomic signatures.** For a nonempty face \(X\), define \(\sigma(X)\) to be the partial function that records its atomic type at each represented color. By cup completeness every selection of one type or no type at each color, other than the all-absent selection, is realized by a face. This gives \(N_0\) signatures. Different signatures are separated in three-valued truth status by a local literal: different colors yield a defined-versus-undefined distinction, while different valuations at a common color yield opposite truth values. Hence different signatures cannot be modally equivalent.

**Step 2 — modal homogeneity from support uniformity.** Write \(S_x\) for the set of atomic types on other colors to which \(x\) has an outgoing edge. The hypothesis means \(S_x\) depends only on \(u(x)\). The set of signatures of directed faces \(Y\) accessible from \(x\) is then exactly the set of signatures that contain \(u(x)\) at color \(\chi(x)\) and, independently at each other color, select either no type or one of the types in \(S_x\). The independence of selections is the decisive use of cup completeness: all multicolored subsets are faces, without further adjacency restrictions between vertices within \(Y\). Thus two source vertices of the same atomic type have precisely the same set of accessible face signatures. A structural induction over formulas proves that the three-valued status of every formula at \(X\) depends only on \(\sigma(X)\). For \(\Box_a\), the existence of a *defined* successor and the truth of *all defined* successors both depend only on this accessible-signature set, completing the induction. Therefore exactly \(N_0\) modal face types occur.

**Step 3 — necessity via modal observation.** Suppose \(x,x'\) have the same atomic type \(u\), but \(x\) has an outgoing edge to a vertex of target type \(v\) of another color \(b\), while \(x'\) has none. Let \(\lambda_v\) be the conjunction of all signed local letters describing \(v\). Its three-valued status is true exactly on faces with a \(b\)-vertex of type \(v\), false on faces with a different \(b\)-type, and undefined on faces lacking \(b\). The formula \(\Diamond_{\chi(u)}\lambda_v\) is true at singleton face \(\{x\}\), because one accessible face containing the desired target exists, but is false or undefined at \(\{x'\}\). These singleton faces have the same atomic signature but different modal theories. Thus the minimum quotient size forces uniform support.

**Step 4 — exact counting.** A block of directed edges from \(m_u\) sources of type \(u\) to \(m_v\) targets of type \(v\), with different colors, is an arbitrary \(m_u\)-by-\(m_v\) Boolean matrix. Uniform row support means either the unique all-zero matrix or a matrix with every row nonzero. There are \((2^{m_v}-1)^{m_u}\) latter matrices, disjoint from the zero matrix. Edge blocks of distinct ordered type pairs are independent, yielding the product for \(C(\mathbf m)\). With Bernoulli probability \(p_{uv}\), the first class has probability \((1-p_{uv})^{m_um_v}\), while each nonzero row has probability \(1-(1-p_{uv})^{m_v}\); product factorization yields \(Q(\mathbf m,\mathbf p)\).

**Step 5 — random phase diagram.** Under one atomic type per color, each of the \(k(k-1)\) ordered color blocks has \(n^2\) independently chosen edges and the same homogeneous-support probability \(h_n(p)\). At \(p=c/n^2\), the all-zero block probability tends to \(e^{-c}\), and the all-row-nonempty probability tends to zero, yielding the sparse limit. At \(p=(\log n+c)/n\), the one-row-empty probability is \((1-p)^n=e^{-c}/n+o(1/n)\); thus the probability that every row is nonempty tends to \(e^{-e^{-c}}\), whereas the all-zero contribution vanishes. Multiplying the independent color blocks establishes both limits. Finally, \((1-p)^{n^2}\le e^{-n^2p}\) and \([1-(1-p)^n]^n\le e^{-n(1-p)^n}\) imply the zero limit under the two stated divergences. The corresponding one-sided lower bounds (all edges absent or all rows having a neighbor) give the two sufficient conditions for the one limit.

## Verification

The standalone `checker.py` uses only the Python standard library. It builds every possible face of small cups, evaluates atoms, negation, weak conjunction, and nested belief operators with undefinedness, exhaustively enumerates all directed cross-color edge sets for several two- and three-color examples, and compares the observed homogeneous-support counts against the product formula. It checks the distinguishing diamond formulas and compares the exact independent-edge probability with direct rational-weight enumeration at three edge probabilities. Execution should print `ALL_CHECKS_OK`. These finite tests check implementation and boundary cases; the all-formula and asymptotic conclusions follow from the proof, not from extrapolation of finite tests.

## Relationship to prior work

The directed cup construction, its three-valued belief semantics, and its relational representation come from van Ditmarsch, Gomes, Randrianomentsoa and Studer's 2026 work *Unbelievably Complex*. Those are foundations here, not claimed innovations. Earlier work on bisimulation for impure simplicial complexes studies the standard knowledge setting on a different class of complexes and establishes a Hennessy–Milner result. It neither supplies the fixed-valuation **exact count of three-valued cup modal-type saturation** nor the two separated random directed-edge windows. The present theorem is a combinatorial and probabilistic classification for those already-defined cup models, rather than a new logic or a general bisimulation theorem.

## Limitations

This classification is specific to complete cups: in arbitrary directed simplicial complexes, independence of selecting compatible target types can fail, invalidating the sufficiency step and the census. The exact formula counts labeled vertex-and-valuation configurations, not unlabeled structures. The probabilistic phase theorem fixes the color count as \(n\to\infty\), and assumes independent ordered cross-color arrows. Outside these assumptions no phase diagram is asserted. The modal quotient criterion assumes the local language separates atomic types and treats undefinedness as observable in modal status. General prior work on modal reduction and random directed relations might contain broader tools implying parts of this classification; historical priority remains open to external verification.

## References

1. H. van Ditmarsch, D. Gomes, R. Randrianomentsoa and T. Studer, *Unbelievably Complex*, arXiv:2610.35106v1, first submitted 26 October 2026. https://arxiv.org/abs/2610.35106
2. M. Bílková, H. van Ditmarsch, R. Kuznets and R. Randrianomentsoa, *Bisimulation for Impure Simplicial Complexes*, arXiv:2406.16785v1, first submitted 24 June 2024. https://arxiv.org/abs/2406.16785
3. T. Bolander and A. Burigana, *Better Bounded Bisimulation Contractions*, arXiv:2405.00480, 2024. https://arxiv.org/abs/2405.00480
