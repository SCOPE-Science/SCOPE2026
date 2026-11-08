# Balanced EFX existence and its binomial threshold for identical two-value goods

## Finding

Let \(n\ge 2\) agents have the same strictly positive additive valuation. There are \(nr\) individually labeled goods, each worth either \(H\) or \(L\), with \(r\ge 1\), \(H>L>0\), and exactly \(q\in\{0,\ldots,nr\}\) high-valued goods. A *balanced allocation* assigns exactly \(r\) goods to every agent. It is *EFX* when, for every distinct agents \(i,j\) and every \(g\in A_j\),
\[
v(A_i)\ge v(A_j\setminus\{g\}).
\]

**Theorem (complete balance-versus-EFX criterion, exact enumeration, and random threshold).** A balanced EFX allocation exists if and only if
\[
H\le 2L\quad\text{or}\quad n\mid q\quad\text{or}\quad q>(r-1)n.
\tag{1}
\]
Every balanced allocation is also fractionally Pareto optimal relative to the balanced fractional-allocation polytope, so (1) is equally the criterion for simultaneous balanced EFX and constrained fPO.

In the high-contrast case \(H>2L\), the number \(N_{n,r,q}\) of EFX allocations into *labeled agent bundles* of the \(nr\) distinct goods is
\[
N_{n,r,q}=\begin{cases}
\displaystyle\frac{q!\,(nr-q)!}{(a!)^n\,((r-a)!)^n},&q=an,\ 0\le a\le r-1,\\[6pt]
\displaystyle\frac{n!\,q!}{s!\,(r!)^s\,((r-1)!)^{n-s}},&q=(r-1)n+s,\ 1\le s\le n,\\[6pt]
0,&\text{otherwise.}
\end{cases}
\tag{2}
\]
The two nonzero branches have disjoint domains as written.

If each of the \(nr\) goods independently has value \(H\) with probability \(p_n\), let \(B_n\sim\mathrm{Binomial}(nr,p_n)\) be the number of high goods. For \(H>2L\), the probability \(F_{n,r}(p_n)\) that *some* balanced EFX allocation exists is exactly
\[
F_{n,r}(p_n)=\Pr\bigl(B_n>(r-1)n\bigr)+\sum_{j=0}^{r-1}\Pr(B_n=jn).
\tag{3}
\]
For each fixed \(r\ge2\), set \(p_*=(r-1)/r\). Whenever \(p_n=p_*+\beta n^{-1/2}+o(n^{-1/2})\), where \(\beta\in\mathbb R\),
\[
\lim_{n\to\infty}F_{n,r}(p_n)
=\Phi\!\left(\frac{\beta r^{3/2}}{\sqrt{r-1}}\right),
\tag{4}
\]
with \(\Phi\) the standard normal CDF. At fixed \(0<p<p_*\), the feasibility probability decays exponentially in \(n\) except at the isolated resonances \(p=j/r\), \(1\le j\le r-2\), where
\[
F_{n,r}(p)\sim[2\pi nrp(1-p)]^{-1/2}.
\tag{5}
\]
At fixed \(p>p_*\), it tends to one exponentially fast; at \(p=p_*\), it tends to \(1/2\). If \(H\le2L\), feasibility has probability one for every realization, independently of \(p_n\).

## Assumptions and scope

Goods are distinct physical objects, though there are only two common numerical item values. Agents are labeled and all use the same additive valuation. There are no transfers or discarded goods; the cardinality constraint is exact rather than merely differing by at most one. The EFX condition quantifies over *every* good in an envied bundle; since \(L>0\), EFX and zero-inclusive EFX coincide. Constrained fPO compares to fractional reallocations that preserve all goods and each agent's fractional bundle size \(r\). Statement (4) fixes \(r\) and lets \(n\to\infty\); it does not claim a joint-growth asymptotic for \(r\).

## Proof

Write \(d=H-L>0\), and let \(h_i\in\{0,\ldots,r\}\) be the number of high goods assigned to agent \(i\). Then
\[
v(A_i)=rL+dh_i,\qquad \sum_{i=1}^n h_i=q.
\tag{6}
\]
If target agent \(j\) has at least one low good, removing a low good is the strongest EFX test, and it is equivalent to \(d(h_j-h_i)\le L\). If target \(j\) has \(h_j=r\), all target goods are high and the strongest test is \(d(r-h_i)\le H\). These two inequalities, checked for all ordered distinct agent pairs, are exactly EFX.

First suppose \(d\le L\), equivalently \(H\le2L\). Assign high goods so that the \(h_i\)'s differ by at most one, distributing the remaining low goods to make every bundle size \(r\). Whenever the target has a low good, its high-count advantage is at most one, so \(d(h_j-h_i)\le d\le L\). When the target is entirely high, \(r-h_i\le1\), so \(d(r-h_i)\le d<H\). Thus the allocation is EFX.

Now assume \(d>L\). Choose an agent \(i\) with minimum high count \(a\). Any target \(j\) containing a low good must have \(d(h_j-a)\le L\); integrality and \(d>L\) force \(h_j=a\). Thus *every* non-all-high bundle has the same high count \(a\). If no all-high bundle exists, every agent has \(a\) high goods, so \(q=an\). If at least one all-high bundle exists but not every bundle is all-high, testing one against minimum agent \(i\) gives \(d(r-a)\le H=d+L\). Because \(d>L\) and \(r-a\) is a positive integer, this forces \(r-a=1\). Accordingly all bundles have \(r-1\) or \(r\) high goods and \(q>(r-1)n\). If every bundle is all-high, \(q=nr\), also covered. This proves necessity of (1).

For sufficiency when \(q=an\), assign exactly \(a\) high and \(r-a\) low goods to each agent. All bundles have the same total value, hence EFX. For \(q=(r-1)n+s\) with \(1\le s\le n\), assign \(r\) high goods to \(s\) agents and \(r-1\) high plus one low good to the remaining \(n-s\). A mixed bundle has utility \((r-1)H+L\), exceeding the value \((r-1)H\) of an all-high bundle after deleting any good. Between mixed bundles, utilities agree; an all-high agent has greater utility than a mixed agent, so EFX holds. These constructions exhaust the cases in (1).

For (2), in the equal-count case, assigning the \(q\) distinct high goods in groups of \(a\), and the \(nr-q\) distinct low goods in groups of \(r-a\), gives \(q!/(a!)^n\) and \((nr-q)!/((r-a)!)^n\) choices. In the upper-layer case, select \(s\) agents to take entirely high bundles, assign \(r\) distinct high goods to each and \(r-1\) to each remaining agent, and assign the \(n-s\) low goods bijectively to the mixed bundles. Multiplying the resulting multinomial counts gives the second branch. The necessity argument proves there are no uncounted types.

Every feasible balanced (possibly fractional) allocation has total utility \(\sum_i v(A_i)=\sum_g v(g)\), a fixed constant, because agents have identical valuations. An improvement of all agents with one strict improvement would increase that total, contradicting this identity. Hence each balanced allocation is constrained fPO (in fact, unconstrained fPO).

Equation (3) follows from (1), as the events \(B_n>(r-1)n\) and \(B_n=jn\) for \(0\le j\le r-1\) are disjoint. For (4), \(\mathbb E B_n=nrp_n\) and \(\operatorname{Var}B_n=nrp_n(1-p_n)\). At \(p_*=(r-1)/r\),
\[
\frac{\mathbb E B_n-(r-1)n}{\sqrt{\operatorname{Var}B_n}}
\longrightarrow \frac{\beta r^{3/2}}{\sqrt{r-1}}.
\tag{7}
\]
The triangular-array binomial central limit theorem proves the right-hand side of (4) for \(\Pr(B_n>(r-1)n)\). For each \(j\le r-2\), the event \(B_n=jn\) is separated from the limiting mean by a positive linear fraction of \(n\), so a Chernoff bound makes its probability exponentially small. The remaining event \(B_n=(r-1)n\) is \(O(n^{-1/2})\) by the local binomial central limit theorem. Thus the discrete corrections vanish in the critical window.

For fixed \(p<p_*\), the strict upper tail is exponentially small by Chernoff's inequality, as is every lattice point \(jn\) for which \(j/r\ne p\), by the binomial large-deviation bound with rate \(D(j/r\Vert p)>0\). If \(p=j/r\), \(1\le j\le r-2\), the one lattice point at the binomial mean instead has mass asymptotic to \([2\pi nrp(1-p)]^{-1/2}\) by Stirling's formula, proving (5). For fixed \(p>p_*\), the binomial lower-tail probability \(\Pr(B_n\le(r-1)n)\) is exponentially small; at \(p=p_*\) the critical normal limit with \(\beta=0\) is \(1/2\).

## Verification

A standalone Python 3 checker `check.py` independently enumerates every feasible integer high-count profile for \(2\le n\le5\), \(1\le r\le4\), and six rational contrast choices. It directly tests the EFX pairwise inequalities, aggregates counts with multinomial weights, and compares against the classification and the high-contrast formula. It checked 34,080 high-count profiles, 936 existence instances, and 312 enumeration formulas. A separate labeled-good recursive allocation enumeration verified 38 cases for selected \((n,r)\), providing an independent route to the exact counts. All comparisons passed. These tests support the finite calculations but are not a replacement for the all-parameter proof above. No simulations are invoked to prove the asymptotic normal limit.

A minimal boundary example has two agents, two goods each, one good of value \(H\) and three of value \(L\). Balanced EFX exists when \(H\le2L\), but fails when \(H>2L\), because the recipient of two low goods still envies the mixed bundle after removal of its low good. A higher-count witness has three agents, three goods each, and four high goods of value \(3\) versus five low goods of value \(1\): neither divisibility nor the top layer applies, so no balanced EFX exists, although balanced EF1 is achievable.

## Relationship to prior work

Kawase and Mahara (2026, arXiv:2603.05956) prove balanced EF1 and fPO existence for personalized bivalued valuations and two valuation types. Cookson, Shah and Verma (2026, arXiv:2608.06325) prove balanced EF1 and fPO existence for arbitrary additive valuations. Both concern the weaker fairness criterion EF1 rather than balanced EFX. Gorantla, Marwaha and Velusamy (2022, arXiv:2202.05186) prove EFX existence for up to two types of goods without exact cardinality balance. Davidiuk and coauthors (2026, arXiv:2601.03438) establish unconstrained EFX and Pareto optimality for two good types; they do not impose exact equal-size bundles. None of the inspected relevant statements gives criterion (1), counts (2), or the random critical window (4). These comparisons concern implication between hypotheses and conclusions, not only matching keywords.

## Limitations

The theorem applies only to identical two-value positive additive valuations and exact equal-cardinality allocations; it does not assert analogous criteria for heterogeneous agents, more than two values, approximate balancedness, or chores. The probability law assumes independent item types with common probability and fixed \(r\). Exact EFX feasibility is a structural consequence of the simple valuation domain; the proof does not settle general EFX feasibility under balance. Primary-source inspection and research-record searches support an originality judgment but do not establish universal priority or rule out unindexed equivalent work. Independent audit is not claimed.

## References

1. Y. Kawase and R. Mahara, *Fair and Efficient Balanced Allocation for Indivisible Goods*, first public March 6, 2026, https://arxiv.org/abs/2603.05956.
2. B. Cookson, N. Shah and P. Verma, *Fair and Efficient Balanced Allocations for Additive Valuations*, first public August 6, 2026, https://arxiv.org/abs/2608.06325.
3. P. Gorantla, K. Marwaha and S. Velusamy, *Fair allocation of a multiset of indivisible items*, first public February 10, 2022, https://arxiv.org/abs/2202.05186.
4. V. Davidiuk, Y. Dementiev, A. Ignatiev and D. Sagunov, *EFX and PO Allocation Exists for Two Types of Goods*, first public January 6, 2026, https://arxiv.org/abs/2601.03438.
