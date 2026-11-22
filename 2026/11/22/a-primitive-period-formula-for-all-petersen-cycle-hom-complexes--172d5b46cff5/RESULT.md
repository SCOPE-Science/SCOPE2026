# A primitive-period formula for all Petersen cycle-Hom complexes

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, \(C_n\) the simple cycle with \(n\ge3\), and \(\operatorname{Hom}(C_n,P)\) the ordinary polyhedral graph-Hom complex. Let \(B\) be the \(30\times30\) nonbacktracking matrix indexed by directed edges of \(P\): \(B_{(a,b),(b,c)}=1\) when \(c\ne a\), otherwise zero. Write \(T_j=\operatorname{tr}(B^j)\), and define nonnegative integers \(p_j\) by
\[
T_j=\sum_{d\mid j}d p_d,\qquad
p_j=\frac1j\sum_{e\mid j}\mu(e)T_{j/e}.
\]
Here \(p_j\) counts primitive *oriented* cyclic nonbacktracking necklaces of length \(j\), without identifying reversal. Define
\[
Q_n=\begin{cases}
\displaystyle\sum_{\substack{d\ge1\\d\,\mathrm{odd}}}
p_d\left\lfloor\frac{\lfloor(n-2)/d\rfloor+1}{2}\right\rfloor,&n\text{ odd},\\[6pt]
\displaystyle 2\sum_{\substack{d\ge1\\d\,\mathrm{even}}}p_d\left\lfloor\frac{n-2}{d}\right\rfloor
+\sum_{\substack{d\ge1\\d\,\mathrm{odd}}}p_d\left\lfloor\frac{n-2}{2d}\right\rfloor,&n\text{ even}.
\end{cases}
\]
(All displayed sums are finite.) Then, for every \(n\ge3\),
\[
\operatorname{Hom}(C_n,P)\simeq
\left(\coprod^{T_n}\{\mathrm{pt}\}\right)
\sqcup\left(\coprod^{Q_n}S^1\right)
\sqcup\begin{cases}|P\times K_2|,&n\text{ even},\\\varnothing,&n\text{ odd}.
\end{cases}
\]
In particular the even null-homotopic component is a wedge of eleven circles, while the formula distinguishes the multiplicity-one contribution of odd-primitive-period even powers from the multiplicity-two contribution of even primitive periods. The homotopy equivalence is integral. The formula is a *uniform enumeration* beyond, and does not reprove, the square-free-target component-type theorems.

The first new values beyond the small-cycle classifications are: \((T_{10},Q_{10})=(1320,100)\), \((T_{12},Q_{12})=(3360,364)\), and \((T_{13},Q_{13})=(7800,304)\). In the case \(n=12\), the \(264\) circles whose reduced length is ten consist of \(240\) circles from primitive length-ten necklaces and \(24\) circles from twice-traversed primitive pentagons; the latter are *not* doubled.

## Assumptions and scope
The target is the ten-vertex graph whose vertices are two-element subsets of \(\{0,1,2,3,4\}\), adjacent exactly when disjoint. It is connected, cubic, nonbipartite and has no triangles or four-cycles. The source is a simple cycle, so \(n\ge3\); \(n=3\) gives the empty complex. A graph-Hom vertex is a cyclic length-\(n\) walk in \(P\). The geometric realization of the polyhedral Hom complex, rather than a reconfiguration graph alone, is classified. A cyclic word and its reverse are distinct unless equal under a cyclic shift; no unproved equivalence between either pair is assumed.

## Proof
**1. Lifts and reduction.** Fix the universal covering tree \(T\longrightarrow P\), whose degree is three. A homomorphism \(C_n\to P\) lifts to a walk \(u:\mathbb Z\to T\) satisfying \(u(i+n)=g u(i)\) for a deck transformation \(g\). Different choices of lift conjugate \(g\); thus its conjugacy class, represented by a cyclically reduced closed edge-word, is invariant under Hom moves. Write \(\ell(g)\) for the translation length of a nontrivial \(g\). A walk of length \(n\) from \(u(0)\) to \(g u(0)\) exists only when \(n\ge\ell(g)\) and \(n\equiv\ell(g)\pmod2\). Conversely, walking once along the translation axis and inserting \((n-\ell(g))/2\) immediate reversals constructs such a map. For \(g=1\), an even \(n\) is necessary and sufficient.

**2. The parity-lift lemma.** For fixed \(g\ne1\) and \(n>\ell(g)\) with matching parity, the graph of \(g\)-equivariant length-\(n\) walks in \(T\), with edges changing one vertex while retaining its two neighbors, has precisely two connected components, distinguished by the bipartition color of \(u(0)\). To prove connectedness within each parity, consider the axis \(A_g\). At a vertex of maximal positive distance from the axis on an off-axis excursion, both adjacent walk vertices are its unique parent toward the axis. Replacing that tip by the grandparent (distance at least two) or, at distance one, by an axis neighbor decreases the number or depth of off-axis visits. Repeating gives an axis-valued walk. Axis-valued walks correspond to \(n\) symbols \(+1,-1\) with net sum \(\ell(g)\). A local Hom move swaps neighboring opposite symbols, hence arbitrarily permutes their locations. Since \(n>\ell(g)\), both symbol types occur; bringing a reversal to the cyclic seam permits changing \(u(0)\) by two axis steps. Therefore all axis walks with the same bipartition color connect. Every move changes a vertex by distance two, so opposite parity cannot connect. The argument works with all three neighbors of a tree vertex and does not require the image to remain on the axis during the initial reduction.

When \(n=\ell(g)\), the lifted walk must be a geodesic on the axis. Such walks have no backtrack; because \(P\) has no four-cycle, there is no alternative color at a single source vertex. Every such projected homomorphism is isolated. Conversely, any nonbacktracking cyclic walk has this form, so the number of isolated components is exactly \(T_n\).

**3. Primitive-root parity and component count.** A nonidentity deck element \(g\) has a unique primitive root \(h\) up to inversion of an oriented generator, with \(g=h^m\), and its centralizer in the free deck group is \(\langle h\rangle\). Let \(d=\ell(h)\). Then \(\ell(g)=md\), and conjugacy classes of \(g\) correspond to primitive oriented cyclic necklaces of period \(d\), together with \(m\). The centralizer translates \(A_g\) by \(d\), so it exchanges the two parity-lift components exactly when \(d\) is odd. Thus one projected Hom component occurs for each \((h,m)\) with \(d\) odd, and two for \(d\) even, provided \(md\le n-2\) and \(md\equiv n\pmod2\). If \(n\) is odd then \(d,m\) must both be odd. If \(n\) is even and \(d\) odd, then \(m\) must be even; if \(d\) even, every positive \(m\) works. Counting admissible multipliers yields exactly the two floor-sum formulas for \(Q_n\).

**4. Topological types, not just components.** By the contractibility theorem for equivariant lifts into the universal tree of a square-free target (Matsushita, Theorem 1.4; independently Fujii--Kimura--Nozaki), each connected lift-component is contractible. For \(g\ne1\) and \(n>\ell(g)\), the centralizer stabilizing a parity lift-component is \(\langle h\rangle\) when \(d\) is even and \(\langle h^2\rangle\) when \(d\) is odd. Both are infinite cyclic and act freely, so the corresponding projected component is a \(K(\mathbb Z,1)\), hence is homotopy equivalent to \(S^1\). The \(g=1\) sector, possible only for even \(n\), gives one connected component homotopy equivalent to the connected bipartite double cover \(|P\times K_2|\), by the square-free-target theorem (Fujii--Kimura--Nozaki, Theorem 1.2, or Matsushita, Proposition 5.10). Since that cover has twenty vertices and thirty edges, it is \(\bigvee^{11}S^1\). This completes the classification.

**5. Exact necklace arithmetic.** The directed nonbacktracking transition matrix \(B\) has a closed walk for each marked cyclic nonbacktracking word. Every primitive necklace of period \(d\) contributes exactly \(d\) marked walks to \(T_j\) whenever \(d\mid j\). Hence \(T_j=\sum_{d\mid j}dp_d\), and Möbius inversion gives the displayed formula. In particular, the Ihara--Bass determinant for the cubic Petersen graph gives
\[
\det(I-tB)=(1-t^2)^5(1-3t+2t^2)(1-t+2t^2)^5(1+2t+2t^2)^4,
\]
so \(T_j\) is computable without enumerating Hom vertices for arbitrary \(j\). This determinant identity also follows by direct elimination on the explicitly defined thirty-state matrix.

## Verification
The standalone Python-standard-library script `verify.py` defines \(P\) from two-element subsets of five symbols and \(B\) from directed nonbacktracking edges, computes \(T_j,p_j,Q_n\) using exact integers, independently enumerates all closed length-\(n\) graph walks and every single-coordinate recoloring edge, and compares complete component distributions for \(3\le n\le12\). Its optional `--extended` option also exhaustively checks \(n=13\). In its standard run it reports \(Q_{10}=100\), \(Q_{11}=64\), \(Q_{12}=364\), including the period-dividing-length correction at \(n=12\). The integer and reconfiguration tests do *not* certify the infinite normal-form lemma or the geometric Hom homotopy type; those rely on the proof above and the cited square-free-target theorems. The output `verification_output.txt` is the actual standard execution transcript of the standalone checker, included for reproducibility only.

## Relationship to prior work
The square-free-codomain Hom theorems of Fujii--Kimura--Nozaki and Matsushita already establish that the possible component homotopy types are points, circles, and the relevant double cover, and give algorithms for individual components. Wrochna provides a general reconfiguration-decision algorithm. These are essential inputs, not newly claimed discoveries. The contribution here is a *single uniform closed formula for all cycle lengths* of the Petersen target, via a primitive-necklace count and the explicit period-parity correction. Accessible previous Petersen calculations report particular lengths \(5,7,8,9,11\), not an infinite-length formula. The arithmetic specialization from the general square-free setting must not be confused with a proof that earlier algorithms cannot compute these values instance by instance.

## Limitations
No claim is made for nonsquare-free targets, equivariant homology representations, the exact cell structures of circle components, or integrality of an equivariant decomposition. The formula is an integral homotopy classification, not a homeomorphism classification. The broad square-free reconfiguration work could make its uniform enumeration conceptually less remote than first appears, and overlooked unindexed explicit generating functions remain a publication-priority risk. The proof relies on the published contraction theorem for lifted Hom complexes; the checker separately validates only bounded instances. Independent audit has not been performed.

## References
1. S. Fujii, K. Kimura and Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039, initially public 2024-12-26, https://arxiv.org/abs/2412.19039.
2. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144, initially public 2024-12-26, https://arxiv.org/abs/2412.19144.
3. M. Wrochna, *Homomorphism Reconfiguration via Homotopy*, SIAM Journal on Discrete Mathematics 34 (2020), 328--350, https://doi.org/10.1137/17M1122578.
4. H. Bass, *The Ihara--Selberg zeta function of a tree lattice*, International Journal of Mathematics 3 (1992), 717--797 (Ihara--Bass determinant formula).
