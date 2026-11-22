# Exact random-graph law and connectivity window for three-nilpotent semigroups

## Finding
Fix disjoint labeled finite sets \(A\) and \(B\), where \(|A|=r\ge2\), \(|B|=b\ge2\), and designate \(0\in B\). Assume \(b-1\le r^2\). Choose uniformly from all semigroup multiplications on \(A\sqcup B\) for which \(S^3=\{0\}\), \(S^2=B\), and \(A=S\setminus S^2\). Let \(G_S\) be the graph on \(A\) in which distinct vertices are adjacent precisely when their products commute.

Put \(m=\binom r2\). For any *particular labeled graph* \(H\) on \(A\) with \(k\) edges, the exact probability is
\[
\Pr(G_S=H)=\frac{F_{r,b}(k)}{D_{r,b}},
\quad F_{r,b}(k)=\sum_{j=0}^{b-1}(-1)^j\binom{b-1}{j}(b-j)^{r+k}\big((b-j)(b-j-1)\big)^{m-k},
\]
\[
D_{r,b}=\sum_{j=0}^{b-1}(-1)^j\binom{b-1}{j}(b-j)^{r^2}.
\]
Here \(0^0=1\) for the finite counting convention. In particular, the law is uniform among graphs with the same number of edges.

Writing \(\mathcal G_{r,p}\) for the independent-edge Erdős–Rényi graph with \(p=1/b\), the total-variation distance satisfies
\[
d_{\mathrm{TV}}(\mathcal L(G_S),\mathcal L(\mathcal G_{r,1/b}))\le(b-1)(1-1/b)^{r^2}.
\]
The standard commuting graph \(\Gamma(S)\), defined on the noncentral elements, is obtained from \(G_S\) by deleting its universal vertices (vertices adjacent to all other vertices). Thus the probability that \(\Gamma(S)\) is exactly \(G_S\) on all \(r\) generators is at least
\[
1-(b-1)(1-1/b)^{r^2}-r b^{-(r-1)}.
\]

For every fixed real \(c\), let \(b=b_r=\lfloor r/(\log r+c)\rfloor\) for sufficiently large integers \(r\), and choose \(S\) as above. Then the *ordinary noncentral commuting graph* has the sharp connectivity law
\[
\boxed{\lim_{r\to\infty}\Pr(\Gamma(S)\text{ is connected})=\exp(-e^{-c}).}
\]
Finally, every inclusion-maximal commutative subsemigroup is exactly \(B\cup C\), where \(C\) is an inclusion-maximal clique of \(G_S\), and its largest possible cardinality is \(b+\omega(G_S)\).

## Assumptions and scope
Every semigroup considered is labeled and has a distinguished zero. The two subsets \(A=S\setminus S^2\) and \(B=S^2\) are fixed as labeled sets; isomorphism classes are *not* sampled uniformly. The algebraic nilpotency degree is exactly three because \(S^2\neq\{0\}\) and \(S^3=\{0\}\). The connectivity limit uses natural logarithms and the regime \(b_r\asymp r/\log r\). Nothing is asserted about arbitrary mixtures of the parameters \(r,b\) or uniform sampling over unlabelled isomorphism classes.

## Proof
**1. Canonical multiplication tables.** Every multiplication in the stated family is uniquely determined by a function \(\psi:A\times A\to B\) via \(xy=\psi(x,y)\) if \(x,y\in A\), and \(xy=0\) otherwise. All triple products vanish, so associativity holds automatically. Moreover \(S^2=B\) exactly when every member of \(B\setminus\{0\}\) occurs in \(\operatorname{im}\psi\). Hence the uniform semigroup law is that of \(r^2\) independent uniform \(B\)-valued entries conditioned on this coverage event \(E\). Inclusion–exclusion yields \(|E|=D_{r,b}\) tables.

**2. Exact graph counts.** A diagonal entry \(\psi(x,x)\) is unconstrained by \(G_S\). For each of the \(k\) commuting unordered pairs, the two oppositely ordered entries must be equal, giving \(t\) assignments when the available label set has size \(t\). For each of the remaining \(m-k\) pairs, the entries must differ, giving \(t(t-1)\) assignments. The \(r\) diagonal entries supply \(t^r\). To force every one of the \(b-1\) nonzero labels to appear, apply inclusion–exclusion, removing \(j\) of them and putting \(t=b-j\). This gives exactly \(F_{r,b}(k)\). Summation over all graphs yields \(D_{r,b}\), as \(t+t(t-1)=t^2\) per unordered pair.

**3. Coupling and center.** Without coverage conditioning, the equality events \(\psi(x,y)=\psi(y,x)\) for distinct unordered pairs are independent and each has probability \(1/b\). Thus \(G_S\) is obtained by conditioning the exact Erdős–Rényi model on \(E\). Total variation cannot increase when passing from tables to their graphs, and the distance between a law and its conditioning on \(E\) is \(\Pr(E^c)\). The union bound gives \(\Pr(E^c)\le(b-1)(1-1/b)^{r^2}\). Every element of \(B\) commutes with everything; a member of \(A\) is central exactly when its graph vertex is universal. In the unconditioned independent-edge graph the union bound for universal vertices gives \(r b^{-(r-1)}\). The displayed lower probability follows by the same coupling.

**4. Connectivity window.** For \(b_r=\lfloor r/(\log r+c)\rfloor\), set \(p_r=1/b_r\). Then \(rp_r=\log r+c+o(1)\), \(p_r\to0\), and the coverage-failure and universal-vertex bounds in step 3 tend to zero. It remains to derive the limiting connectivity probability of \(\mathcal G_{r,p_r}\). Let \(X\) count its isolated vertices. For each fixed integer \(h\ge1\), the factorial moment is
\[
\mathbb E (X)_h=(r)_h(1-p_r)^{h(r-h)+\binom h2}\longrightarrow e^{-hc}.
\]
The factorial-moment criterion therefore gives \(X\Rightarrow\operatorname{Poisson}(e^{-c})\), so \(\Pr(X=0)\to\exp(-e^{-c})\).

If the graph is disconnected but has no isolated vertices, it has a connected component of size \(k\) for some \(2\le k\le r/2\). A specified set of \(k\) vertices supports a connected induced graph only if it contains one of its \(k^{k-2}\) spanning trees. Therefore the probability of this event is bounded by
\[
\sum_{k=2}^{\lfloor r/2\rfloor}\binom rk k^{k-2}p_r^{k-1}(1-p_r)^{k(r-k)}.
\]
For \(2\le k\le r/(\log r)^2\), the inequalities \(\binom rk\le(er/k)^k\) and \((1-p_r)^{r-k}\le C/r\), with \(C\) independent of \(r,k\), bound the corresponding summand by \((eC)^k p_r^{k-1}/k^2\). Their sum is \(O(p_r)=o(1)\). For \(r/(\log r)^2<k\le r/2\), discard the spanning-tree factor and bound by \(\binom rk(1-p_r)^{k(r-k)}\le (e(\log r)^2)^k\exp[-p_rkr/2]\le r^{-k/3}\) for sufficiently large \(r\); this sum also tends to zero. Hence connectivity and absence of isolated vertices agree with probability \(1-o(1)\), proving the claimed limit for the semigroup commuting graph.

**5. Commutative subsemigroups.** The ideal \(B\) annihilates the entire semigroup. Adjoining all of \(B\) to any commutative subsemigroup preserves both closure and commutativity. Any remaining set of generators is pairwise commuting exactly when it is a clique of \(G_S\); products of generators already lie in \(B\). The assertion about maximal commutative subsemigroups follows.

## Verification
Run `python3 check_graph_law.py` from the same directory. The checker independently enumerates all \(B\)-valued tables for seven small parameter pairs, retains those for which every nonzero label occurs, constructs the graph from actual ordered products, and compares every labeled graph frequency to the alternating-sum formula. It also independently checks maximal commuting-subsemigroup sizes against clique numbers. The recorded output is in `CHECK_OUTPUT.txt`. These finite checks are diagnostic: the all-parameter statements are proved above, not inferred from enumeration.

## Relationship to prior work
Distler and Mitchell (2012, Section 3) give the canonical presentation and exact counts of degree-three nilpotent semigroups, but not the labeled commuting-graph probability law or its sharp connectivity window. Dolinka, FitzGerald and Mitchell (2024, Sections 1–2) refine the enumeration via partial partitions and analyze rigidity; their canonical tables are exactly the antecedent used here. Araújo, Kinyon and Konieczny (2010) formulate commuting graphs for semigroups and examine path lengths. Bauer and Greenfeld (2016/2017, Proposition 3) show realizability of arbitrary star-free graphs by nilpotent semigroups, rather than describing the probabilistic distribution of these graphs under fixed \(S^2\)-size. The standard Erdős–Rényi connectivity phenomenon supplies the probabilistic precedent; the present work proves its applicability to a natural uniformly labeled semigroup ensemble despite its product-surjectivity conditioning.

## Limitations
The probability model fixes the labeled generating set and product ideal; it is not the distribution of a uniform isomorphism class. The first two canonical multiplication-table constructions are established prior art. The novelty assessment concerns the exact conditional labeled-graph law and the semigroup connectivity threshold, not the classical random-graph limit in isolation. Prior independent verification has not been performed, and older literature may contain an unindexed equivalent probabilistic formulation. The asymptotic does not address a different law obtained by varying \(|S^2|\) without conditioning.

## References
1. A. Distler and J. D. Mitchell, *The number of nilpotent semigroups of degree 3*, preprint dated 2012-01-17, https://arxiv.org/abs/1201.3529 , *Electronic Journal of Combinatorics* 19(2) (2012), P51.
2. I. Dolinka, D. G. FitzGerald and J. D. Mitchell, *Semirigidity and the enumeration of nilpotent semigroups of index three*, preprint dated 2024-11-01, https://arxiv.org/abs/2411.00466 .
3. J. Araújo, M. Kinyon and J. Konieczny, *Minimal paths in the commuting graphs of semigroups*, preprint dated 2010-03-14, https://arxiv.org/abs/1003.2809 .
4. T. Bauer and B. Greenfeld, *Commuting graphs of boundedly generated semigroups*, *European Journal of Combinatorics* 56 (2016), 40–45; preprint dated 2017-10-14, https://arxiv.org/abs/1710.05250 .
5. P. A. Grillet, *Counting Semigroups*, *Communications in Algebra* 43(2) (2015), 574–596, https://doi.org/10.1080/00927872.2013.790036 (abstract accessed; complete text not available for comparison).
