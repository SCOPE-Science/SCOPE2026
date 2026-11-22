# Parity-separated reversible-wave clocks on finite generalized hexagons

## Finding

Let \(\Gamma\) be the point–line incidence graph of any finite generalized hexagon of equal order \((q,q)\), where \(q\ge 2\) is an integer for which the geometry exists. For every finite field \(\mathbb F_Q\), with \(Q=2^f\) and \(f\ge1\), let \(A\) be its adjacency matrix and set
\[
T(u,v)=(Au+v,u),\qquad (u,v)\in\mathbb F_Q^{N}\times\mathbb F_Q^{N},
\]
where \(N=2(q^3+1)(q^2+q+1)\) is the number of graph vertices. Then every initial state is periodic from time zero, with **exact global update order**
\[
\operatorname{ord}(T)=\begin{cases}48,&q\text{ even},\\12,&q\text{ odd}.\end{cases}
\]
Every divisor of the indicated global order actually occurs as a least temporal period. The entire labelled periodic-state and primitive-orbit census is determined exactly by the modular adjacency kernel dimensions specified below, for every such geometry and field extension.

## Assumptions and scope

A generalized hexagon of order \((q,q)\) has a bipartite point–line incidence graph of degree \(q+1\), girth twelve, and diameter six. Its distance matrices \(D_0=I,D_1=A,\ldots,D_6\) have intersection numbers
\[
(b_0,b_1,\ldots,b_5)=(q+1,q,q,q,q,q),\quad(c_1,\ldots,c_6)=(1,1,1,1,1,q+1).
\]
The statement applies to **realized geometries only**; it does not assert existence at every integer order or uniqueness of such a geometry. Computation takes place in characteristic two, but the order \(q\) of the incidence geometry need not be a power of two. The thin cycle \(C_{12}\) at \(q=1\) is a check, not part of the stated domain. All vector-space dimensions below are over \(\mathbb F_Q\).

For \(\lambda\in\{0,1\}\) put
\[
H_\lambda(j)=\dim\ker(A+\lambda I)^j,\quad H_\lambda(0)=0.
\]
Define \(r_0=5,r_1=2\) for even \(q\), and \(r_0=2,r_1=4\) for odd \(q\). Values \(H_\lambda(j)\) are constant once \(j\ge r_\lambda\). For \(1\le j\le r_\lambda\), let
\[
c_{\lambda,j}=2H_\lambda(j)-H_\lambda(j-1)-H_\lambda(j+1).
\]
These nonnegative integers are the Jordan-block counts for the adjacency eigenvalue \(\lambda\).

For each positive time \(k\), let \(e(k)=2^{\nu_2(k)}\) be the largest power of two dividing \(k\), and set
\[
E(k)=\sum_{j=1}^{r_0}c_{0,j}\min\{2j,e(k)\}
+2\mathbf{1}_{\{3\mid k\}}\sum_{j=1}^{r_1}c_{1,j}\min\{j,e(k)\}.
\]
The exact number of initial states fixed by the \(k\)-th iterate is \(Q^{E(k)}\). The number of states of **least** period \(k\), and the number of primitive temporal orbits of least period \(k\), are respectively
\[
P(k)=\sum_{d\mid k}\mu(k/d)Q^{E(d)},\qquad C(k)=P(k)/k.
\]
For \(k\) not dividing the global order, \(P(k)=0\). No additional graph-invariant inputs beyond the finitely many specified kernel dimensions are required.

## Proof

**Distance-polynomial identity.** In the binary adjacency algebra, the distance-regular recurrence is
\[
AD_i=b_{i-1}D_{i-1}+c_{i+1}D_{i+1},\quad 1\le i\le5,
\]
with \(AD_0=D_1\) and \(AD_6=b_5D_5\); bipartiteness gives no diagonal term. If \(q\) is even, then \(q+1=1\) and \(q=0\) in \(\mathbb F_Q\). Iteration gives
\[
D_2=A^2+I,\quad D_3=A^3+A,\quad D_4=A^4+A^2,\quad D_5=A^5+A^3,\quad D_6=A^6+A^4.
\]
Since \(AD_6=0\), we obtain \(A^7+A^5=0\). If \(q\) is odd, the same recurrence gives
\[
D_2=A^2,\quad D_3=A^3+A,\quad D_4=A^4,\quad D_5=A^5+A^3+A.
\]
The relation \(AD_5=D_4\) yields \(A^6+A^2=0\).

**Sharp minimal polynomials.** There exist graph vertices at every distance up to six. For distance \(j\le5\) the unique shortest path implies that \(A^j\) has nonzero entries at distance \(j\), whereas all lower powers vanish there. For even \(q\), vertices at distance six are connected by exactly \(q+1\) shortest paths, an odd number, so the same holds at distance six. Consequently the first six powers are linearly independent if \(q\) is odd, and the first seven if \(q\) is even. The displayed annihilating polynomials have exactly these degrees, so the **exact** modular adjacency minimal polynomials are
\[
m_A(X)=\begin{cases}X^5(X+1)^2,&q\text{ even},\\ X^2(X+1)^4,&q\text{ odd}.\end{cases}
\]
In particular both eigenvalues and both maximum Jordan exponents truly occur; the statement does not rely on an unjustified semisimplicity assumption.

**Passage to the two-level wave.** The inverse is \(T^{-1}(x,y)=(y,x+Ay)\). On an adjacency Jordan block \(J_j(0)\), the wave has one unipotent Jordan block of length \(2j\). Indeed, \(T^2+I=AT\) and \(\dim\ker(T+I)=\dim\ker A=1\) on that block. On an adjacency block \(J_j(1)\), the wave is a cyclic block with characteristic polynomial \((Z^2+Z+1)^j\), because \(T^2+T+I=(A+I)T\), \(T+I\) is invertible on this primary component, and its first cyclotomic kernel has dimension two. This remains valid if the quadratic splits in the chosen field extension.

A length-\(2j\) unipotent block has order \(2^{\lceil\log_2(2j)\rceil}\); a \((Z^2+Z+1)^j\) primary block has order \(3\cdot2^{\lceil\log_2 j\rceil}\). The sharp maximum block lengths above therefore give \(\operatorname{lcm}(16,6)=48\) in even order and \(\operatorname{lcm}(4,12)=12\) in odd order. The largest primary blocks supply vectors of all their subordinate power-of-two or three-times-power-of-two periods; direct sums supply their least common multiples. Hence each divisor of the exact order occurs.

**Orbit census.** For any positive \(k\), the root \(Z=1\) occurs in \(Z^k+1\) with multiplicity \(e(k)\), and a primitive cubic root occurs with the same multiplicity precisely when \(3\mid k\). Taking nullities on the described primary blocks gives \(E(k)\), hence \(|\operatorname{Fix}(T^k)|=Q^{E(k)}\). Möbius inversion and division by the orbit length yield \(P(k)\) and \(C(k)\).

## Verification

The standalone scripts `check_distance_algebra.py` and `check_wave.py` use only Python's standard library. Invoke `python3 check_distance_algebra.py` and `python3 check_wave.py` from the directory containing these files. The first checks both binary distance-algebra recurrences and their exact annihilator degrees. The second independently constructs bit-packed binary matrices, checks the direct twelve-cycle adjacency, checks faithful cyclic algebra models of both modular adjacency polynomials, and compares all iterate fixed-space dimensions with the claimed Jordan formulas through the respective global periods. The test sizes are \(12\), \(7\), and \(6\) adjacency coordinates, with respectively \(12\), \(48\), and \(12\) exact fixed-space comparisons. The cyclic models are **not** falsely presented as actual generalized hexagons: the infinite-family proof is the preceding distance-recursion argument.

## Relationship to prior work

The generalized-hexagon incidence axioms, the Benson graph and the degree/girth/diameter statements are standard, as documented in Exoo–Jajcay's *Dynamic Cage Survey* (initial public version 2008; the relevant 2013 text is §2.2.3). Vlasov establishes the general reversible second-order cellular-automaton construction, not these incidence-specific modular minimal polynomials or global periods. Jazaeri's *Distance-regular graphs admitting a perfect 1-code*, §4.2, gives the exact generalized-hexagon intersection array and studies codes in line graphs rather than the two-time-level wave. Earlier reversible-wave classifications for projective planes, generalized quadrangles and partial geometries concern different incidence axioms: hexagon incidence graphs have diameter six and girth twelve, whereas those families do not provide a covering hexagon assertion. The key new claim here is the exact hexagon parity clock and Jordan-kernel orbit formula, not the graph parameters or reversibility itself.

## Limitations

The theorem covers equal-order finite generalized hexagons, not unequal-order generalized polygons or arbitrary distance-regular graphs. Orbit-count inputs may vary across nonisomorphic geometries with the same order; universal values for every individual Jordan multiplicity are not asserted. The proof is mathematical, supported but not replaced by finite algebra tests. Independent external mathematical audit has not yet been performed, and a previously unindexed equivalent dynamical classification cannot be excluded absolutely.

## References

1. G. Exoo and R. Jajcay, *Dynamic Cage Survey*, Electronic Journal of Combinatorics, Dynamic Surveys DS16, first published 2008-09-29, revised 2013-07-26, §2.2.3. https://doi.org/10.37236/37
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first submitted 2013-11-18, §3. https://arxiv.org/abs/1311.4297
3. M. Jazaeri, *Distance-regular graphs admitting a perfect 1-code*, arXiv:2301.06593, first submitted 2023-01-16, §4.2. https://arxiv.org/abs/2301.06593
