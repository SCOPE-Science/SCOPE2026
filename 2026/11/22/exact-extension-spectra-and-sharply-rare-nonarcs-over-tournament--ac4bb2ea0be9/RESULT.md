# Exact extension spectra and sharply rare nonarcs over tournament bases in the homogeneous independent-triple-free digraph

## Finding

Let \(\mathbb D\) be the countable homogeneous oriented digraph in which no three distinct vertices are pairwise nonadjacent. For any pointwise named induced tournament \(A\subset\mathbb D\) of size \(n\geq 0\), let \(T_r(n)\) be the number of complete types of ordered \(r\)-tuples of mutually distinct points outside \(A\), for \(r\geq1\). The count is independent of the orientation pattern on \(A\).

For a labelled simple graph \(H\) on \([r]\), write \(\mathcal I(H)\) for its independent sets, \(e(H)\) for its number of edges, and define the integer weight
\[
W(H)=\sum_{S\in\mathcal I(H)}2^{r-|S|}=2^r Z_H(1/2),
\]
where \(Z_H\) is the usual independence polynomial. Put \(m=\binom r2\). Then for every \(n\geq0\) and \(r\geq1\),
\[
\boxed{T_r(n)=\sum_{\substack{H\text{ labelled on }[r]\\H\text{ triangle-free}}} 2^{m-e(H)}W(H)^n.}
\]
In particular,
\[
T_1(n)=3^n,\qquad T_2(n)=2\cdot9^n+8^n,
\]
\[
T_3(n)=8\cdot27^n+12\cdot24^n+6\cdot22^n.
\]

The three largest exponential bases in the all-arity formula are exactly \(3^r\), \(8\cdot3^{r-2}\), and \(22\cdot3^{r-3}\), for \(r\ge3\), with respective coefficients \(2^m\), \(m2^{m-1}\), and \(3\binom r3 2^{m-2}\). Thus for each fixed \(r\ge4\),
\[
\begin{aligned}
T_r(n)={}&2^m3^{rn}+m2^{m-1}(8\cdot3^{r-2})^n\\
&+3\binom r3 2^{m-2}(22\cdot3^{r-3})^n
+O_r((64\cdot3^{r-4})^n).
\end{aligned}
\]
For \(r=3\), the displayed first three terms are exact, and for \(r=2\), the first two terms are exact. The bound in the remainder for \(r\ge4\) is sharp: two disjoint nonedges among the new points produce the fourth base \(64\cdot3^{r-4}\).

When types are sampled uniformly from the \(T_r(n)\) types at fixed \(r\ge2\), the probability of at least one nonadjacent pair among the new points is
\[
\boxed{\frac{\binom r2}{2}(8/9)^n+O_r((22/27)^n)}.
\]
Conditioned on having a nonadjacent pair, the new tuple has *exactly one* nonadjacent pair with probability \(1-O_r((11/12)^n)\). For \(r=2\), this conditional probability is exactly one for every \(n\).

## Assumptions and scope

An oriented digraph has at most one directed arc between two distinct vertices, and may have no arc. An \(I_3\)-free digraph forbids three distinct pairwise nonadjacent vertices. The finite \(I_3\)-free digraphs form a strong-amalgamation class, so the countable homogeneous limit \(\mathbb D\) realizes every compatible finite extension diagram. Homogeneity in the finite relational language identifies complete types over finite pointwise named bases with their induced finite diagrams. The new tuple coordinates are labelled and pairwise distinct, and none equals a base vertex. No assumption is made on the orientation pattern of the tournament base.

The asymptotic statements hold as \(n\to\infty\) with \(r\) fixed; the implicit constants may depend on \(r\). The probability distribution is uniform on logical types, not on elements of the infinite structure.

## Proof

**Finite-diagram reduction.** Any induced extension of \(A\) by \(r\) labelled vertices has an undirected *nonarc graph* \(H\) on the new vertices: \(ij\in E(H)\) exactly when the pair has no directed arc. The forbidden-triple condition implies \(H\) is triangle-free. Every other new-new pair can be oriented in either direction, giving \(2^{m-e(H)}\) choices.

For each old vertex \(a\in A\), write \(S_a\subseteq[r]\) for those new vertices nonadjacent to \(a\). Every pair in \(H\) cannot lie entirely in \(S_a\), since that would create a forbidden independent triple. Equivalently, \(S_a\) must be an independent set of \(H\). For every \(S_a\), there are exactly \(2^{r-|S_a|}\) ways of orienting the remaining old-new pairs, yielding \(W(H)\) local assignments.

These are all the conditions: a triple containing at least two old vertices contains the tournament arc joining those two vertices; triples containing one old vertex are dealt with by the condition on \(S_a\); triples consisting of three new vertices are dealt with by triangle-freeness of \(H\). Therefore the \(n\) old vertices make independent contributions \(W(H)^n\). Summing over \(H\) proves the exact formula. The extension property and homogeneity turn every finite diagram into exactly one complete tuple type.

**The leading exponential bases.** If \(H\) is edgeless, then \(W(H)=3^r\), and its coefficient is \(2^m\). If \(H\) has exactly one edge, then precisely the assignments giving state zero to both endpoints are forbidden; hence \(W(H)=8\cdot3^{r-2}\). There are \(m\) choices of that edge, each with coefficient \(2^{m-1}\).

If \(H\) has at least two edges, select any two. For adjacent edges the number of allowed ternary states on their three vertices is \(27-3-3+1=22\), so \(W(H)\leq22\cdot3^{r-3}\). For disjoint edges the corresponding number is \(8^2=64\), so \(W(H)\leq64\cdot3^{r-4}\), strictly smaller than \(22\cdot3^{r-3}\). Equality at the third base requires exactly two adjacent edges: every further edge removes a formerly allowed zero-state pattern. There are \(3\binom r3\) two-edge paths on \([r]\), and their orientations contribute \(2^{m-2}\) each.

For \(r\ge4\), all other graphs have weight at most \(64\cdot3^{r-4}\). For two edges, the only remaining case is two disjoint edges. With three or more edges, choose a three-edge subgraph: it is either a three-edge star, a four-vertex path, a two-edge path plus a disjoint edge, or a three-edge matching (up to isolated vertices); their respective ternary-assignment weights are \(62\cdot3^{r-4}\), \(60\cdot3^{r-4}\), \(176\cdot3^{r-5}\), and \(512\cdot3^{r-6}\), all smaller than \(64\cdot3^{r-4}\). Adding edges cannot increase the weight. Since there are finitely many labelled graphs for fixed \(r\), the claimed error term follows, and is sharp because a two-edge matching has weight \(64\cdot3^{r-4}\).

**Rare nonarcs.** The edgeless \(H\) contribution is exactly \(2^m3^{rn}\); all other contributions count types with at least one nonarc. Dividing their sum by \(T_r(n)\) and using the first two bases yields the stated probability, because \((8/9)^2=64/81<22/27\). The total contribution from graphs with at least two nonarcs is \(O_r((22\cdot3^{r-3})^n)\), while the contribution from graphs with exactly one nonarc is \(m2^{m-1}(8\cdot3^{r-2})^n\). Their ratio is \(O_r((11/12)^n)\). This proves the conditional statement.

## Verification

The standalone `verify.py` checks the triangle-free graph sum, including the exact weight multiplicities for \(r=1,2,3\) and the leading three weights for \(r=3,4,5\). It independently enumerates all ternary directed/nonarc edge assignments extending fixed tournament bases in every tested case with \(nr+\binom r2\le12\), namely the small cases printed by the verifier, and confirms both independent routes agree. The recorded output is in `verification_output.txt`. This finite enumeration checks the formulas but is not a substitute for the all-size proof above.

## Relationship to prior work

Aranda's 2015 preprint and the deposited 2013 thesis establish the existence and extension framework of the homogeneous \(I_3\)-free digraph, and classify the asymptotically typical *unconditioned* labelled \(I_3\)-free digraph as a bitournament. The original counting proof uses a local eight-choice bound for a specified nonarc pair; that bound is consistent with the \(r=2\) term above but neither states nor implies the complete fixed-new-arity type-spectrum decomposition and its three exponential layers without an additional finite-diagram analysis. The present theorem instead fixes \(r\), names a growing tournament base, and samples uniformly among extension types.

The hard-core independence polynomial \(Z_H\) is established terminology; the novelty claim is not the polynomial itself but its exact role as a transfer weight for this model-theoretic orbit spectrum and the sharp local asymptotics. No assertion of historical uniqueness is made.

## Limitations

The result is specific to *tournament* parameter bases, though it counts all arities of distinct new vertices. It does not establish the same formula over arbitrary finite \(I_3\)-free parameter digraphs, and the asymptotic errors are not uniform when the arity grows with \(n\). It counts finite logical types rather than probabilities of choosing vertices from an infinite set. Earlier equivalent enumeration under another terminology remains a historical-priority risk.

## References

- Andrés Aranda López, *Omega-categorical simple theories*, University of Leeds PhD thesis (2013), deposited publicly 21 January 2015. https://etheses.whiterose.ac.uk/id/eprint/7838/
- Andrés Aranda, *Asymptotic Enumeration of \(I_3\)-free Digraphs* (2015), arXiv:1505.00235, especially Definition 1.1, Remark 1.2, Proposition 1.3, and Theorem 2.1. https://arxiv.org/abs/1505.00235
- Andreas Galanis, Qi Ge, Daniel Štefankovič, Eric Vigoda and Linji Yang, *Improved Inapproximability Results for Counting Independent Sets in the Hard-Core Model*, initial arXiv submission May 2011, arXiv:1105.5131, for the independence-polynomial terminology. https://arxiv.org/abs/1105.5131
