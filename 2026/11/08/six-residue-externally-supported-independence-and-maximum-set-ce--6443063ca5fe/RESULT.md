# Six-residue externally supported independence and maximum-set census of circular ladders

## Finding
Let \(L_n=C_n\square K_2\) be the labelled circular ladder with \(n\ge3\) columns. An *externally supported independent set* (ESI set) is an independent vertex set \(B\) for which every vertex of \(N(B)\) has a neighbor in \(V(L_n)\setminus N[B]\). Write \(\alpha_{\mathrm{es}}(L_n)\) for its maximum cardinality and \(m_n\) for the number of labelled ESI sets attaining that cardinality.

For \(n=6q+r\), \(0\le r\le5\), the exact values are
\[
\begin{array}{c|rrrrrr}
r&0&1&2&3&4&5\\\hline
\alpha_{\mathrm{es}}(L_n)&4q&4q&4q+1&4q+1&4q+2&4q+2\\
m_n&6&2n&2n&2n^2/3&n(n+5)/3&n(n-2)(n+7)/9
\end{array}
\]
where only entries with \(n\ge3\) are asserted. Equivalently,
\[
\alpha_{\mathrm{es}}(L_n)=\lfloor 2n/3\rfloor-\mathbf1_{\{n\equiv3,5\pmod6\}}.
\]
Thus the regular-graph upper bound is missed by one exactly in two of the six congruence classes. In particular, for every positive multiple of six there are exactly six maximizing ESI sets, whereas the other residue classes have multiplicities growing linearly, quadratically, or cubically.

For every \(n\ge7\), the *entire* cardinality polynomial \(E_n(z)=\sum_{B\text{ ESI in }L_n}z^{|B|}\) is given by \(E_n(z)=\operatorname{tr}(T(z)^n)\), where the finite labelled transition matrix \(T(z)\) is specified in the proof and constructed reproducibly in `verify.py`. Its recurrent portion has exactly \(117\) states and \(241\) directed transitions. The exceptional short polynomials are
\[
\begin{aligned}
E_3(z)&=1+6z,\\
E_4(z)&=1+8z+12z^2,\\
E_5(z)&=1+10z+20z^2,\\
E_6(z)&=1+12z+36z^2+28z^3+6z^4.
\end{aligned}
\]

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The cycle \(C_n\) has distinct columns indexed by \(\mathbb Z/n\mathbb Z\), with \(n\ge3\). Each column of \(L_n\) has two vertices \((i,0)\), \((i,1)\), joined by a rung; equal-row vertices in adjacent columns are joined by cycle edges. The empty set is ESI. Two ESI sets are counted separately when they differ as subsets of the labelled vertex set, including when related by a graph automorphism. The counts \(m_n\) enumerate *sets*, not auxiliary witnesses.

## Proof
**Local encoding.** Because every rung is an edge, an independent set selects at most one vertex per column. Encode column \(i\) by a symbol \(s_i\in\{-1,0,1\}\): \(-1\) means no selected vertex, and \(0\) or \(1\) specifies the selected row. For every integer index \(i\), a block \((s_{i-3},\ldots,s_{i+3})\) of seven symbols is declared admissible precisely when (a) no two consecutive symbols are equal and nonnegative; and (b) for each of the two vertices in its middle column, if that vertex has a selected neighbor, at least one of its three neighbors is unselected and has no selected neighbor. The latter test uses at most three columns on either side of the middle, so it is entirely determined by the seven-symbol block. For \(n\ge7\) the cyclic word encodes an ESI set **if and only if** every seven-consecutive-symbol block is admissible. This is a local equivalence, not a heuristic approximation.

Form the de Bruijn digraph whose vertices are all \(3^6=729\) six-symbol words; a seven-symbol admissible block gives one arc from its first six symbols to its last six. The arc has weight \(w=1\) if its last symbol is selected and \(w=0\) otherwise. A cyclic word of length \(n\ge7\) corresponds bijectively to a rooted closed walk of length \(n\); the total weight is \(|B|\). All closed walks lie in strongly connected components containing a directed cycle. Exact enumeration of the local rule gives \(429\) arcs in the full digraph and a unique cyclic strongly connected component with \(117\) states and \(241\) arcs. Thus the polynomial transfer formula follows, with \(T(z)_{ab}=\sum_{a\to b}z^{w(a,b)}\) on those \(117\) states.

**Nonnegative deficit transfer.** Assign an integer potential \(h\) on the recurrent states satisfying \(h(b)\ge h(a)+3w(a,b)-2\) for every arc. Such a potential exists: initialize every potential to zero and repeatedly relax along all arcs by this inequality; the exact finite computation stabilizes and returns \(57\) zero, \(40\) one, and \(20\) two potentials, with every inequality checked. Define the new arc cost
\[
c(a,b)=2-3w(a,b)+h(b)-h(a)\ge0.
\]
Among the \(241\) arcs, the costs \(0,1,2\) occur \(144,40,57\) times respectively. For a closed walk of length \(n\), potential differences telescope, so its total cost equals
\[
d=2n-3|B|.
\]
In particular, all ESI sets on these prisms satisfy \(3|B|\le2n\), and the nonnegative deficit is congruent to \(2n\) modulo three.

Let \(C(t)\) be the \(117\)-by-\(117\) adjacency matrix whose arc \(a\to b\) contributes \(t^{c(a,b)}\), and let \(D(x,t)=\det(I-xC(t))\). Direct exact finite integer arithmetic, with all states and arcs generated from the explicit local predicate above, establishes the full polynomial congruence
\[
\boxed{D(x,t)\equiv 1-x^6-2x^2t-(x+x^4+x^7)t^2+x^5t^4\pmod{t^5}.}
\]
This is a **finite algebraic certificate**, not an extrapolation from small \(n\). To reproduce it, `verify.py` computes \(p_j(t)=\operatorname{tr}(C(t)^j)\bmod t^5\) for every \(1\le j\le117\) by integer dynamic programming. It then applies the Newton identity \(kD_k(t)=-\sum_{j=1}^kp_j(t)D_{k-j}(t)\) to every coefficient \(D_k(t)\) of \(x^k\) in the determinant, for \(1\le k\le117\). Since its degree in \(x\) is at most \(117\), checking **all** those coefficients proves the displayed congruence for every power of \(x\). The verifier uses arbitrary-precision integers, checks each exact division, and compares the resulting complete finite coefficient support.

**Extraction of all maximizing sets.** The formal matrix identity
\[
-\log D(x,t)=\sum_{n\ge1}\frac{x^n}{n}\operatorname{tr}(C(t)^n)
\]
implies that the number of ESI sets with \(d=2n-3|B|\) is \([x^nt^d]\bigl(-x\partial_x\log D(x,t)\bigr)\) for \(n\ge7\). Put \(U=1-x^6\), \(P=2x^2\), \(Q=x+x^4+x^7\), and \(R=x^5\). For deficits at most four, the coefficients of \(-\log D\) are exactly
\[
\begin{aligned}
H_0&=-\log U,&H_1&=P/U,\\
H_2&=Q/U+P^2/(2U^2),&H_3&=PQ/U^2+P^3/(3U^3),\\
H_4&=-R/U+Q^2/(2U^2)+P^2Q/U^3+P^4/(4U^4).
\end{aligned}
\]
Here \([t^d](-\log D)=H_d\). Since \((1-x^6)^{-j}=\sum_{q\ge0}\binom{q+j-1}{j-1}x^{6q}\), the coefficient \([x^n]xH_d'(x)\) is explicit in each residue class. The least nonzero eligible deficit is \(d=0,2,1,3,2,4\), respectively, as \(n\equiv0,1,2,3,4,5\pmod6\). In the fourth residue class, deficit zero is impossible because \(H_0\) has support only at multiples of six; in the sixth, deficit one is impossible because \(H_1\) has support only at lengths congruent to two modulo six. The congruence \(d\equiv2n\pmod3\) excludes all other smaller deficits. These coefficient calculations give the claimed maxima and the six displayed multiplicity formulas. For \(n=3,4,5,6\), direct exact enumeration of all \(3^n\) column assignments yields the four explicit polynomials above, with the same maximum and multiplicity formulas. This completes the proof for every \(n\ge3\).

## Verification
Run `python3 verify.py` using Python 3 and no third-party modules. It independently reconstructs the admissible seven-column transition graph and its cyclic strongly connected component; checks the integer potential inequalities and their complete cost distribution; computes the complete determinant congruence modulo \(t^5\) using exact Newton identities up to characteristic degree \(117\); and separately enumerates ESI subsets directly in the graph for \(3\le n\le11\). The direct enumeration compares both maximum size and number of maximizers, and for \(7\le n\le11\) compares all low-deficit transfer traces against separate graph-neighborhood tests. The expected terminal line is `VERIFY_OK`. The finite determinant calculation, not the small-graph sampling, carries the unlimited-\(n\) proof.

## Relationship to prior work
Božović, Peterin, Roux and Tepeh introduced ESI sets and derived exact ESI numbers for paths, cycles, wheels, fans, and complete bipartite graphs in arXiv:2606.22972 (first submitted June 22, 2026). Their Corollary 14 gives the general cubic-graph bound \(\alpha_{\mathrm{es}}(L_n)\le2n/3\), but their results do not supply the exact six-residue prism law, its two strict-deficit classes, the full transfer enumerator, or the maximum-set multiplicities. Brešar and collaborators studied the *minimum isolation number* on prisms and other graph products in arXiv:2508.16338; that is a different optimization problem and does not directly fix how many ESI sets of maximum size a prism has. These distinctions concern mathematical implications, not title similarity. No claim of absolute historical priority is made.

## Limitations
The closed formulas concern the ordinary two-layer circular ladder, not arbitrary cylinders, all cubic graphs, or the ordinary isolation number. The full cardinality polynomial has an exact finite transfer description rather than a closed coefficient expression. The computationally certified lemma is finite and exhaustively reproducible; it does not constitute independent mathematical audit. Unindexed or inaccessible equivalent prior results remain a historical-priority risk, and the accessible abstract of arXiv:2508.16338 was not a full-manuscript inspection.

## References
- D. Božović, I. Peterin, A. Roux, A. Tepeh, *On externally supported independence number of graphs*, arXiv:2606.22972v1, June 22, 2026. https://arxiv.org/abs/2606.22972 . Relevant material: definition, Proposition 6, Proposition 13 and Corollary 14.
- B. Brešar, T. Dravec, D. P. Johnston, K. Kuenzel, D. F. Rall, A. Tepeh, *Isolation number: Cartesian and lexicographic products and generalized Sierpiński graphs*, arXiv:2508.16338v1, August 22, 2025. https://arxiv.org/abs/2508.16338 . Distinct parameter: minimum isolation number.
- Y. Caro, A. Hansberg, *Partial domination—the isolation number of a graph*, Filomat 31 (2017), 3925–3944. https://doi.org/10.2298/FIL1712925C . Background on isolation, not the present maximum-set census.
