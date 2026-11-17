# An opposite-phase obstruction and exact period-four energy bands on complete graphs

## Finding

Consider synchronous parallel chip-firing on the labelled simple graph \(K_n\), for any integer \(n\ge4\), with nonnegative integral chips and firing threshold \(n-1\). Let \(H_n(z)\) count **initially periodic configurations of least temporal period four**, weighted by their conserved total number of chips (each temporal state counted once).

For \(r\ge1\), put \([r]_z=\sum_{j=0}^{r-1}z^j\). For every positive ordered quadruple \(\mathbf a=(a_0,a_1,a_2,a_3)\) with \(\sum a_i=n\), set
\[
B(\mathbf a)=n(n-1)-\sum_{0\le i<j\le3}a_i a_j,
\qquad
Q_{\mathbf a}(z)=\prod_{j=0}^3[a_{j-1}]_z^{a_j},
\]
where subscripts of \(\mathbf a\) are cyclic modulo four. Define
\[
P_n(z)=\sum_{\substack{a_0,a_1,a_2,a_3\ge1\\a_0+a_1+a_2+a_3=n}}
\frac{n!}{a_0!a_1!a_2!a_3!}\,z^{B(\mathbf a)}Q_{\mathbf a}(z).
\]
Then the exact mass polynomial is
\[
\boxed{H_n(z)=P_n(z)+z^{n(2n-3)}P_n(z^{-1}).}
\]
The support is **exactly two full integer intervals**:
\[
\boxed{[L_n,U_n]\ \cup\ [n(2n-3)-U_n,\ n(2n-3)-L_n],}
\]
with
\[
\boxed{L_n=n(n-1)-\left\lfloor\frac{3n^2}{8}\right\rfloor,
\qquad U_n=(n-1)(n-2).}
\]
Every integer in the two displayed intervals occurs, and no other total is supported. In particular, the high band begins at \(n^2-2\), and the two bands are separated by exactly \(3n-5\) unsupported integer chip totals.

The number of configurations at the **upper edge of the low-energy band** (and, by reflection, the lower edge of the high-energy band) is
\[
\boxed{[z^{U_n}]H_n(z)=4n(n-1)(2^{n-2}-n)+24\mathbf1_{n=4}.}
\]
At the opposite edge, write \(n=4q+r\) with \(q\ge1\) and \(0\le r<4\). Then
\[
\boxed{[z^{L_n}]H_n(z)=\binom4r\frac{n!}{(q+1)!^r q!^{4-r}}.}
\]
The total number of primitive four-orbits equals \(H_n(1)/4\), where
\[
H_n(1)=2\sum_{\substack{a_0,a_1,a_2,a_3\ge1\\\sum a_i=n}}
\frac{n!}{\prod_{i=0}^3a_i!}\prod_{j=0}^3a_{j-1}^{a_j}.
\]

## Assumptions and scope

Each of the \(n\) labelled vertices begins with a nonnegative integer chip count. Every vertex whose count is at least \(n-1\) fires one chip to every other vertex simultaneously. The map is iterated without a sink, dissipation, or chip additions. *Initially primitive period four* means the fourth update returns the initial state and no smaller positive update does. The result counts initial states already on a four-cycle, not their transient attraction basins. A four-cycle requires \(n\ge4\); there are none on \(K_3\).

## Proof

Let \(x_v(t)\) be the chips at vertex \(v\) before step \(t\), let \(f_v(t)=\mathbf1\{x_v(t)\ge n-1\}\), and put \(R_t=\sum_v f_v(t)\). The exact update is
\[
x_v(t+1)=x_v(t)+R_t-nf_v(t).
\]
If the configuration returns after four steps, summing the updates gives
\(n\sum_{t=0}^3f_v(t)=\sum_{t=0}^3R_t\) for every vertex; consequently every vertex fires the same number \(h\) of times in the four steps. For \(h=0\) or \(h=4\), the state is fixed. If \(h=2\), the no-clumpy-periodic-firing-pattern theorem of Jiang, Scully and Zhang (2012; Theorem 6.2) excludes all four-bit sequences containing both adjacent zeros and adjacent ones. The only remaining two-fire words are the alternating strings `1010` and `0101`. They imply \(R_t+R_{t+1}=n\) for every \(t\); summing the update over any two steps returns every vertex to its previous chip count, so such states have period at most two. Thus primitive period four has exactly \(h=1\) or \(h=3\).

For \(h=1\), let phase class \(A_j\) contain the vertices firing uniquely at time \(j\), and put \(a_j=|A_j|\) and \(p_j=\sum_{i<j}a_i\). Directly imposing firing and waiting thresholds in all four temporal rows yields the necessary-and-sufficient integer intervals
\[
\boxed{x_v(0)\in[n-1-p_j,\ n-2-p_j+a_{j-1}]\quad(v\in A_j),}
\]
with cyclic \(a_{-1}=a_3\). For example, a phase-zero vertex fires initially, then waits, requiring \(n-1\le x_v(0)\le n-2+a_3\). A phase-one vertex first waits and then fires, requiring \(n-1-a_0\le x_v(0)\le n-2\); the later waiting inequalities are weaker. Phase two and three follow analogously by using the partial firing sums. In each case the interval contains precisely \(a_{j-1}\) integers. An occupied phase must therefore have a nonempty predecessor phase; around a four-cycle this forces **all four phase classes to be nonempty**. Conversely, each positive ordered quadruple and each independent choice of chip counts inside these intervals realizes exactly its prescribed firing pattern. Each vertex fires once, so the update formula guarantees return after four steps; the nonconstant firing pattern and per-vertex count exclude smaller period.

The minimum total for a fixed phase quadruple is
\[
\sum_j a_j(n-1-p_j)=n(n-1)-\sum_{i<j}a_i a_j=B(\mathbf a),
\]
and the independent ranges contribute \(\prod_j[a_{j-1}]_z^{a_j}\). There are \(n!/\prod a_j!\) assignments of labelled vertices to the ordered classes. This proves the displayed \(P_n(z)\). Within any given quadruple, the available totals fill every integer from \(B(\mathbf a)\) to
\[
U(\mathbf a)=B(\mathbf a)+\sum_j a_j(a_{j-1}-1)=n(n-2)-(a_0a_2+a_1a_3).
\]
In particular, these states lie in the box \([0,2n-3]^n\). Complementation \(x_v\mapsto2n-3-x_v\) therefore preserves nonnegativity, interchanges firing and waiting, and commutes with the update. It bijects \(h=1\) and \(h=3\) four-cycles and sends total \(E\) to \(n(2n-3)-E\). Hence the stated \(H_n(z)\).

The smallest possible \(B(\mathbf a)\) is obtained by minimizing \(\sum a_j^2\), since \(B=(n^2+\sum a_j^2)/2-n\). Balanced positive quadruples give \(L_n=n(n-1)-\lfloor3n^2/8\rfloor\). Also \(a_0a_2\ge a_0+a_2-1\) and \(a_1a_3\ge a_1+a_3-1\) for positive integers, so \(U(\mathbf a)\le(n-1)(n-2)\), with equality exactly when at least one of \(a_0,a_2\) and at least one of \(a_1,a_3\) equals one.

To rule out holes between the two extreme totals, consider the connected graph of positive quadruples of sum \(n\), with an edge for moving a single unit from one part into another while keeping all parts positive. If a move transfers one from part \(i\) to part \(j\), the lower endpoints differ by \(a_j-a_i+1\). For an upward move, this is at most \(a_j-1\), while the original interval width is \(U(\mathbf a)-B(\mathbf a)=\sum_k a_k(a_{k-1}-1)\ge a_{j+1}(a_j-1)\ge a_j-1\). Thus the two consecutive quadruple-intervals overlap. For a downward move, apply the same argument to its reverse. Every neighboring pair of intervals intersects; connectivity implies their union is one integer interval, from \(L_n\) through \(U_n\). Its reflection yields the second band. Since \(n(2n-3)-U_n=n^2-2>U_n\), these bands are disjoint with \(3n-5\) missing integers.

At \(L_n\), only balanced quadruples contribute, and all chip counts must be at their lower endpoints. There are \(\binom4r\) balanced ordered compositions, each with multinomial count \(n!/((q+1)!^rq!^{4-r})\). At \(U_n\), all chip counts must be at their upper endpoints and one from each opposite phase pair must be singleton. Count vertex-to-phase surjections with this restriction by inclusion-exclusion: the four choices of one designated singleton from each opposite pair contribute \(4n(n-1)(2^{n-2}-2)\); subtract the four cases with three designated singleton groups, each of size \(n(n-1)(n-2)\); add back all four singleton groups, possible only at \(n=4\), contributing \(24\). The result is \(4n(n-1)(2^{n-2}-n)+24\mathbf1_{n=4}\). The complement gives the reflected coefficients. Finally, setting \(z=1\) counts all states; dividing by four counts primitive orbits.

## Verification

The independent program `verify_exhaustive.py` directly updates every chip vector in the confined box \(\{0,\ldots,2n-3\}^n\) for \(n=3,4,5,6\), tests genuine least period four, and checks support, symmetry and the sharp upper-low-band coefficient. It finds respectively \(0\), \(48\), \(960\), \(17280\) primitive-four states. The second program `verify_phases.py` separately enumerates every one-fire phase assignment for \(4\le n\le8\), intersects the four firing/waiting inequalities for every vertex, and compares all integer mass coefficients to the independent phase-multinomial expression. It checks the full support and the two edge coefficient formulas at each size. Both actual programs and their output files accompany this result. These finite checks supplement, rather than replace, the all-length proof.

## Relationship to prior work

Levine's complete-graph chip-firing theory (arXiv:0811.2800, first public 2008-11-17) establishes activity/period relations and a middle period-two staircase. Its convention includes one loop per vertex and threshold \(n\); adding one chip per vertex conjugates the dynamics used here to that convention, so **the change of convention is not a novelty claim**. Jiang (arXiv:1003.0943) establishes period-length constructions and general complement lemmas. Jiang, Scully and Zhang (arXiv:1211.6786) establish the nonclumpy firing-pattern restriction used above. A published exact primitive-three mass enumeration for complete graphs (2026) gives a three-phase multinomial formula and simpler middle-stair endpoint counts. Neither it nor these earlier general results states this four-phase opposite-pair obstruction, the exact \(3n-5\)-mass gap, or the isolated \(n=4\) endpoint multiplicity correction. Those new four-specific conclusions do not follow numerically or by changing the labels of the three-phase formula.

## Limitations

The theorem concerns configurations **already** in primitive temporal four-cycles on labelled simple complete graphs, not their attraction basins, nonrecurrent inputs, or cycles of other periods. It uses the published nonclumpy-firing-pattern theorem as an external lemma; the attached checkers provide finite supporting tests but not a replacement all-graph proof of that lemma. Historic priority cannot be guaranteed against unindexed or inaccessible previous work. Independent mathematical audit has not been performed.

## References

1. L. Levine, *Parallel chip-firing on the complete graph: Devil's staircase and Poincaré rotation number*, arXiv:0811.2800 (first public 2008-11-17), https://arxiv.org/abs/0811.2800.
2. T.-Y. Jiang, *On the period lengths of the parallel chip-firing game*, arXiv:1003.0943 (first public 2010-03-04), https://arxiv.org/abs/1003.0943.
3. T.-Y. Jiang, Z. Scully, and Y. X. Zhang, *Motors and impossible firing patterns in the parallel chip-firing game*, arXiv:1211.6786 (first public 2012-11-29), https://arxiv.org/abs/1211.6786.
4. *Exact primitive-three chip-firing energy bands on complete graphs*, published mathematical result (2026), https://github.com/published-finding corpus/2026.
