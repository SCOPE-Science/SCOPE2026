# Sharp two-variable quantifier-rank threshold for successor-only finite directed paths

## Finding
For each positive integer \(n\), let \(P_n\) be the structure on \(\{1,\ldots,n\}\) with \(S(i,j)\) iff \(j=i+1\). For \(q\ge2\), two such structures agree on **every** two-variable first-order sentence of quantifier rank at most \(q\) exactly when
\[
n=m<2q,\quad\text{or}\quad n,m\ge2q.
\]
At rank one all nonempty directed paths agree. Thus the number of rank-\(q\) theories represented by nonempty directed paths is precisely \(2q\), for \(q\ge2\). For \(n<m\), the least distinguishing rank is \(2\) when \(n=1\), and \(\lceil(n+1)/2\rceil\) when \(n\ge2\).

## Assumptions and scope
The only nonlogical predicate is the directed binary successor relation \(S\). Equality is available. Formulas use just two **reusable** variable symbols, for instance \(x,y\), arbitrary Boolean connectives and first-order quantifiers. Quantifier rank counts nested quantifiers. There is no order \(<\), endpoint constant, extra label, counting quantifier or unrestricted third variable. All paths are finite, nonempty, loopless, and have the orientation shown above. The conclusion is equivalence on rank-bounded **sentences**, not equivalence of arbitrary assigned pairs of free variables.

## Proof
**1. The recursive unary-type invariant.** A unary rank-\(r\) type means the set of all formulas of quantifier rank at most \(r\) with at most one free variable that hold at a specified vertex; the comparison includes closed formulas. For every \(r\ge1\), simultaneously across all \(P_n\) with \(n\ge2r+2\), these types are indexed by exactly the following positions:
\[
L_i: i+1\quad (0\le i<r),\qquad R_i:n-i\quad (0\le i<r),\qquad C:r+1\le j\le n-r.
\]
All occurrences of a label across all qualifying paths have the same unary rank-\(r\) type, and distinct labels have distinct types.

For \(r=1\), \(\exists y\,S(y,x)\) and \(\exists y\,S(x,y)\) distinguish the two endpoints from the interior; their truth values characterize the three classes uniformly for \(n\ge4\).

Assume the assertion at \(r\). Fix \(n\ge2r+4\). Any two-variable formula with free variables among \(x,y\) and rank at most \(r\), once quantified over \(y\), is determined by: the rank-\(r\) unary type of the retained variable; the truth values of rank-\(r\) closed formulas; and, for each rank-\(r\) unary type \(T\), whether the second vertex occurs in each of the four mutually exclusive relative positions
\[
y=x,\quad S(x,y),\quad S(y,x),\quad y\ne x\wedge\neg S(x,y)\wedge\neg S(y,x).
\]
This follows by structural induction on two-variable syntax: quantifying either variable leaves at most one free variable; Boolean combinations and atoms cannot record any further binary information beyond equality and directed adjacency. Consequently the displayed unary type and four-way occurrence data characterize unary types at rank \(r+1\). One may equivalently construct their finite characteristic formulas by induction.

Each old boundary color \(L_i,R_i\), for \(0\le i<r\), occurs exactly once. Its relative position to \(x\) depends solely on whether \(x\) lies among the first or last \(r+1\) points or lies in the remaining central block. The old central color occurs on the interval from \(r+1\) through \(n-r\), which has at least four points. Relative to any \(x\), that interval always contains a vertex different from and nonadjacent to \(x\), since at most three positions are excluded. Its immediate-predecessor and immediate-successor occurrence flags depend only on the same new location classes. Thus the rank-\(r+1\) type is constant within and across the \(2(r+1)+1\) asserted new classes. Old boundary classes remain distinguishable by their old formulas; the newly exposed left position \(r+1\) is identified by the presence of a predecessor of old type \(L_{r-1}\), and similarly the newly exposed right position has a successor of old type \(R_{r-1}\). Neither is identified with the new center or each other. This completes the induction.

A closed two-variable sentence of rank at most \(q\) is a Boolean combination of existential or universal closures of unary formulas of rank at most \(q-1\) (including lower-rank closed subformulas). By the unary invariant with \(r=q-1\), every path of size at least \(2q\) realizes exactly the same collection of such unary types. Hence all paths of size at least \(2q\) satisfy the same rank-\(q\) sentences. All nonempty paths agree at rank one, because a rank-one sentence can only assert existence or universality of a quantifier-free unary property; here \(S(x,x)\) is always false and equality reflexive.

**2. Sharp separation.** Write \(L_{-1}(z)=R_{-1}(z)=\bot\), and for \(j\ge0\) let \(L_j(z)\) and \(R_j(z)\) express that the distance to the left and right endpoint is at most \(j\), respectively. Explicitly,
\[
L_0(z):=\neg\exists w\,S(w,z),\qquad R_0(z):=\neg\exists w\,S(z,w),
\]
\[
L_{j+1}(z):=L_j(z)\vee\exists w\,(S(w,z)\wedge L_j(w)),
\]
with the symmetric rule for \(R_{j+1}\). Nested quantified variables alternate the two permitted variable names, so these are valid two-variable formulas; their rank is \(j+1\). Let
\[
\Theta_{a,b}:=\exists x\,\forall y\,[x=y\vee S(x,y)\vee S(y,x)\vee L_a(y)\vee R_b(y)]
\]
for \(a,b\ge-1\). Here the false predicates indexed by \(-1\) are omitted. Since a vertex covers a three-point closed successor neighborhood, the sentence holds on \(P_n\) exactly when the part not already covered by its first \(a+1\) and last \(b+1\) vertices has at most three points, namely precisely when \(n\le a+b+5\). Its rank is at most \(\max\{2,a+3,b+3\}\) for nonnegative indices, with omitted terms contributing no rank.

For each cutoff \(3\le t\le2q-1\), choose \(-1\le a,b\le q-3\) with \(a+b=t-5\). Such a choice exists, and then \(\Theta_{a,b}\) has rank at most \(q\) and holds exactly on sizes \(n\le t\). The cutoffs \(n\le1\) and \(n\le2\) are expressed at rank two by \(\exists x\forall y\,(x=y)\) and \(\exists x\forall y\,(x=y\vee S(x,y))\), respectively. Thus each size below \(2q\) has its own rank-\(q\) theory and is separated from all larger sizes. Combining the two directions yields the exact classification. For \(n\ge2\), the first rank at which \(n<2q\) is \(\lceil(n+1)/2\rceil\), giving the asserted least distinguishing rank.

## Verification
An independent finite exact type-refinement checker accompanies this report as `checker.py`. It starts with the unique rank-zero unary type and iterates all realized relative-position/unary-color pairs to obtain the next unary type. The collection of rank-\((q-1)\) unary types determines rank-\(q\) sentence equivalence. Running it for all \(1\le n\le22\) and \(1\le q\le6\) recovered singleton sizes below \(2q\) and a common class above. A separately implemented exhaustive two-pebble EF game check covered smaller sizes through rank four. These finite computations check the invariant but are not used in place of the quantified induction proof.

## Relationship to prior work
Jeż, Michaliszyn and Witkowski (2026) address the finite satisfiability of two-variable logic with any number of independent successor relations and possible additional predicates; their primary object is algorithmic decidability and model-size bounds, rather than the exact rank theory of a single pure directed path. Weis and Immerman's ranker analysis (2009) treats the richer signature including an independent total order \(<\); that larger language does not yield the present pure-successor collapse. A separately published rank-\(q\) classification of finite directed paths for unrestricted first-order logic reaches \(2^q\), whereas the two-variable fragment here collapses at \(2q\). The additional two-variable restriction therefore has a concrete sharp quantitative effect.

## Limitations
The statement is restricted to pure directed successor paths. The conclusion need not hold after adding \(<\), labels, counting quantifiers, additional successor relations, or branching. Priority beyond inspected literature and indexed records is not guaranteed; older two-pebble game/word-language papers may contain an equivalent observation.

## References
1. A. Jeż, J. Michaliszyn, P. Witkowski, “Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors,” arXiv:2610.19943v1 (first posted 2026-10-14), https://arxiv.org/abs/2610.19943.
2. P. Weis and N. Immerman, “Structure Theorem and Strict Alternation Hierarchy for FO² on Words,” arXiv:0907.0616 (2009), https://arxiv.org/abs/0907.0616.
3. “Exact quantifier-rank threshold for finite directed paths,” published published-finding corpus record 2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112.
