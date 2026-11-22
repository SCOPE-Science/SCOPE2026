# Four-residue shattering and a homological jump for minimum total domination of cycles

## Finding
For every integer \(n\ge 3\), let \(C_n\) be the simple cycle on labelled vertices \(\mathbb Z/n\mathbb Z\). Let \(\mathcal T_n\) be **all minimum-cardinality total dominating vertex subsets** of \(C_n\): each vertex (including each selected vertex) must have a selected neighbor. Define \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\), where a vertex-query support \(S\) is shattered if every zero-one membership assignment on it occurs as the restriction of some member of \(\mathcal T_n\).

For \(m\ge2\), put
\[
Q_m(z)=\begin{cases}
1+mz,&m\text{ even},\\
1+mz+\frac{m(m-3)}2z^2,&m\text{ odd}.
\end{cases}
\]
Then the **entire shattering polynomial** has the following exact form:
\[
\boxed{\displaystyle
\Phi_n(z)=\begin{cases}
Q_n(z),&n\text{ odd},\\
Q_{n/2}(z)^2,&n\text{ even}.
\end{cases}}
\]
In particular, for every \(n\), no query support of size five is shattered. The maximum support size (VC dimension) is one for \(n=3\), four for \(n\equiv2\pmod4\) with \(n\ge10\), and two in all other cases. The scalar VC bound follows also from a prior fixed-weight-independent-set theorem and is not claimed independently new here.

**Individual-support classification.** Form the auxiliary simple graph \(H_n\) with vertex set \(\mathbb Z/n\mathbb Z\) and edges \(\{i-1,i+1\}\) for each \(i\), modulo \(n\); when \(n=4\), duplicate edges are merged. It is a step-two cycle of length \(n\) when \(n\) is odd, and two disjoint step-two cycles of length \(m=n/2\) when \(n\) is even. A support \(S\) is shattered if and only if its intersection with each component \(K\) of \(H_n\) satisfies:

- if the length of \(K\) is even, the intersection has at most one vertex;
- if the length is odd, the intersection has at most two vertices, and a two-vertex intersection is not an edge of \(K\).

Let \(\Delta_n\) be the simplicial complex of shattered supports. Its **integral homotopy type** is fully determined. Writing \(m=n/2\) in the even cases, and \(b_m=1+m(m-5)/2\) when \(m\ge5\) is odd,
\[
\boxed{\displaystyle
\Delta_n\simeq\begin{cases}
\bigvee^2 S^0,&n=3,\\
\bigvee^{1+n(n-5)/2}S^1,&n\ge5\text{ odd},\\
\bigvee^{(m-1)^2}S^1,&n\equiv0\pmod4,\\
\bigvee^{4}S^1,&n=6,\\
\bigvee^{b_m^2}S^3,&n\equiv2\pmod4,\ n\ge10.
\end{cases}}
\]
Thus the only nonzero reduced integral homology is free, in dimension zero for \(n=3\), dimension three for \(n\ge10\) congruent to two modulo four, and dimension one otherwise; the displayed multiplicities are its ranks. For example, \(\Phi_{10}(z)=1+10z+35z^2+50z^3+25z^4\) and \(\Delta_{10}\simeq S^3\), while \(\Phi_{14}(z)=1+14z+77z^2+196z^3+196z^4\) and \(\Delta_{14}\simeq\bigvee^{64}S^3\).

## Assumptions and scope
All cycles here are simple, labelled, and have at least three vertices. Total domination uses **open** neighborhoods and is distinct from ordinary (closed-neighborhood) domination. *Minimum* means minimum possible cardinality rather than inclusion-minimality. Query labels are literal membership bits; a zero label is a required exclusion. The constant coefficient one counts the empty support. The exponent of \(z\) counts queried vertices, not the cardinality of a dominating set. Topological equivalence is ordinary homotopy equivalence of the geometric realization over the integers, not only a mod-two homology calculation. The graph \(H_4\) is interpreted as a simple graph with two independent two-vertex components.

## Proof
**1. Exact reduction to maximum independent sets.** Define \(H_n\) as in the theorem. A vertex subset \(D\) is a total dominating set of \(C_n\) precisely if, for every original vertex \(i\), at least one of \(i-1\) and \(i+1\) belongs to \(D\). Equivalently, \(D\) meets every edge of \(H_n\), so \(D\) is a vertex cover of \(H_n\). A vertex cover has minimum cardinality if and only if its complement is a maximum-cardinality independent set. Thus \(\mathcal T_n\) consists exactly of the complements of maximum independent sets of \(H_n\). Complementing **every** incidence bit preserves shattered supports, because it bijectively exchanges the positive and negative labels of each requested trace.

The step-two edges have one cyclic orbit if \(n\) is odd, and two parity orbits if \(n\) is even. These are, respectively, \(C_n\) and \(C_m\sqcup C_m\) where \(m=n/2\), with \(C_2\) interpreted as a single edge for \(m=2\). For a disjoint union the maximum independent sets are independent products of the maximum independent sets of components. A support is shattered by a Cartesian product concept family exactly when its restriction to every component is shattered. This reduces the result to a single auxiliary cycle and gives the square in the even case.

**2. Maximum independent-set traces on an even auxiliary cycle.** A cycle of even length \(m\ge4\) has exactly two maximum independent sets, the two alternating color classes. The same holds for the single edge at \(m=2\). The two incidence vectors differ at every coordinate, so each singleton is shattered, but no two-coordinate support is (two concepts cannot realize four patterns). Its shattering complex is \(m\) isolated vertices, with polynomial \(1+mz\).

**3. Maximum independent-set traces on an odd auxiliary cycle.** Let \(m=2k+1\ge3\). A maximum independent set has exactly \(k\) vertices. Its cyclic incidence word has no \(11\), and exactly \(m-2k=1\) cyclic edge of type \(00\): each selected vertex is incident with two distinct edges, no edge meets two selected vertices, and the remaining edges are precisely \(00\). Conversely any cyclic word with no \(11\) and one \(00\) has exactly \(k\) ones. Such words exist (and have exactly \(m\) rotations), so this characterizes every maximum independent set.

Every singleton is shattered by rotation. Two adjacent vertices cannot both receive label one, so an auxiliary edge is not shattered. Conversely, let \(u,v\) be nonadjacent. The two oriented arcs between them have lengths at least two, with odd total \(m\). Fix any prescribed endpoint bits \(a,b\). For an arc of length \(L\), the number \(c\) of its \(00\) edges satisfies \(c\equiv L-(a\oplus b)\pmod2\), since all other edges change the bit. Because the arc lengths sum to odd \(m\), exactly one arc needs odd \(c\) and one needs even \(c\). Build the even-parity arc by alternation (no \(00\)), and the odd-parity arc by taking a length-\(L-1\) alternating word from \(a\) to \(b\) and doubling one zero to insert precisely one \(00\). This insertion is always possible because \(L\ge2\) and an alternating word with at least one edge contains a zero. The resulting whole cycle has no \(11\), exactly one \(00\), and the prescribed query bits. Thus every nonadjacent pair is shattered.

No three distinct vertices can be shattered. Take any three queried vertices in cyclic order, with successive positive arc lengths \(L_1,L_2,L_3\). Choose requested bits so that \(L_i-(a_i\oplus a_{i+1})\) is **odd for all three arcs** (cyclic indices). Such bits exist: the XOR of the three target edge differences \(L_i-1\pmod2\) vanishes because \(\sum_i L_i=m\) is odd. Any extending word would then have at least one \(00\) edge in each arc, contradicting the exact global count of one. Every larger support contains a nonshattered triple. The shattered supports are therefore the empty set, all \(m\) vertices, and the \(\binom m2-m=m(m-3)/2\) nonedges. This proves the odd formula and its exact support criterion, including the triangle case where the pair coefficient is zero.

**4. Product enumeration and the VC boundary.** By step 1 a support splits independently between the two auxiliary cycles when \(n\) is even, so its face polynomial is the product of the corresponding \(Q_m\)'s. This is the stated four-residue law and the support criterion. Taking the degree yields the claimed VC values, with the vanishing quadratic coefficient at \(m=3\) producing the exceptional case \(n=6\). For \(n=3\), the odd formula also has zero quadratic coefficient. In all cases the degree is at most four.

**5. Integral homotopy.** The shattered-support complex of a single even auxiliary cycle is the discrete complex on \(m\) points and is homotopy equivalent to \(\bigvee^{m-1}S^0\). For an odd auxiliary cycle of order \(m=3\), it is three isolated points, or \(\bigvee^2S^0\). For odd \(m\ge5\), its simplices are exactly the vertices and the nonedges of that cycle: it is the graph \(\overline{C_m}\). This graph is connected (for \(m=5\) it is another pentagon; for larger odd \(m\) each vertex is adjacent to all but its two cyclic neighbors). It has \(m(m-3)/2\) edges and \(m\) vertices, so it is homotopy equivalent to a wedge of \(1+m(m-5)/2\) circles, by collapsing a spanning tree.

For disjoint ground sets the shattered-support complex of the product concept family is their **simplicial join**. The join of wedges of spheres is a wedge of spheres of the sum of dimensions plus one; this follows from \(X*Y\simeq\Sigma(X\wedge Y)\) for based CW complexes and the distributivity of the smash product over finite wedges. For the two equal components of \(H_n\), apply this to the discrete or connected graph models above. The ranks are \((m-1)^2\), \(2^2=4\), and \(b_m^2\) in the three even cases, and the odd cases retain their single-component type. All equivalences are integral homotopy equivalences, proving the full topological classification.

## Verification
Run `python verify_min_total_cycles.py` using a standard Python 3 interpreter. The checker independently enumerates all minimum-cardinality total dominating sets from the original cyclic open-neighborhood condition at orders \(3\le n\le20\) (not from the auxiliary-cycle description). It then exhaustively compares every membership trace on every support of size at most five with the theorem's structural criterion, checks all asserted polynomial coefficients, rules out six-query shattered supports through order fifteen, and independently tests reduced Euler characteristics in eleven representative orders. Its output ends with `MINIMUM_TOTAL_DOMINATION_CYCLE_PASS 93592 60 11` (93,592 trace checks, 60 coefficient checks, 11 Euler checks). The proof in the preceding section, not this finite check, establishes the statements for all orders and integral homotopy.

## Relationship to prior work
Beaton, Brown and Cameron (2018) study independence polynomials and equivalence classes of cycles, including coefficients of maximum independent sets. Their results concern counts of independent sets, not coordinate-support trace shattering or the topology of this shattering complex. Bahadır, Ekim and Gözüpek (2020) develop structural theory of minimal total dominating sets and well-totally-dominated graphs; Alikhani and Jafari (2021) study total domination polynomials, their equivalence classes, and unimodality. These graph domination results motivate the natural optimum family but do not calculate its complete Boolean shattering profile.

Two particularly close published results were examined at theorem/proof level: *Fixed-weight cyclic independent sets: a one-logarithm online boundary effect* already proves the scalar VC dimension for every fixed-weight independent-set family on a cycle; for the maximum-weight case it subsumes the **scalar** VC values for each auxiliary component here. The paper explicitly does not claim an all-coefficient shattering polynomial. *Complete shattering polynomial and forbidden-gap law for maximal independent sets of cycles* treats **all inclusion-maximal** independent sets, a genuinely larger family for most odd cycle lengths, so its trace theorem does not imply the optimum-only trace formula or the join topology. The present claim is restricted to the exact shattering polynomial, explicit face criterion, and homotopy type of the optimum **total dominating** class, not the known total domination number, optimizer count, or scalar VC bound.

## Limitations
Historical priority has not been independently established. Equivalent results might be indexed as vertex-cover traces, maximum independent-set shattering, extremal cyclic words, or simplicial joins. The formulation concerns ordinary finite simple cycles and only their minimum-total-dominating-set concept classes; it asserts neither a theorem for arbitrary graphs nor an exact Littlestone dimension. Direct experiments through twenty vertices are finite corroboration and not an infinite correctness certificate. No independent mathematical audit has been performed.

## References
1. I. Beaton, J. I. Brown and B. Cameron, *Independence Equivalence Classes of Paths and Cycles*, arXiv:1810.05317v1, first public 2018-10-12, https://arxiv.org/abs/1810.05317.
2. S. Bahadır, T. Ekim and D. Gözüpek, *Well-Totally-Dominated Graphs*, arXiv:2010.02341v1, first public 2020-10-05, https://arxiv.org/abs/2010.02341.
3. S. Alikhani and N. Jafari, *More on total domination polynomial and \(\mathcal D_t\)-equivalence classes of some graphs*, arXiv:2106.06702v1, first public 2021-06-12, https://arxiv.org/abs/2106.06702.
4. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, first public 2021-09-10, https://arxiv.org/abs/2109.04805.
5. *Fixed-weight cyclic independent sets: a one-logarithm online boundary effect*, published 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-fixed-weight-cyclic-independent-sets-a-one-logarithm-online-boun--253357213fec/RESULT.md.
6. *Complete shattering polynomial and forbidden-gap law for maximal independent sets of cycles*, published 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-shattering-polynomial-and-forbidden-gap-law-for-maximal--4d0afc364bee/RESULT.md.
