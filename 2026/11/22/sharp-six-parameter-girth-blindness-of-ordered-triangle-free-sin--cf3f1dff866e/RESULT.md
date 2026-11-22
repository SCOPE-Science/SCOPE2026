# Sharp six-parameter girth blindness of ordered triangle-free singleton-type spectra

## Finding
Let \(\mathcal H^{<}_3\) be the Fraïssé limit of finite simple triangle-free graphs with a freely chosen linear order. For an individually named finite induced ordered graph \(G\) with order \(0<1<\cdots<n-1\), let \(p\) range over complete nonalgebraic singleton types over these parameters. Write \(\ell(p)\) and \(r(p)\) for the numbers of parameters adjacent to a realization of \(p\) and lying, respectively, before and after that realization in the ambient order. Define
\[
F_G(u,v)=\sum_p u^{\ell(p)}v^{r(p)}.
\]

**Sharp reconstruction boundary.** For each \(1\le n\le5\), two triangle-free ordered parameter graphs on \(n\) vertices having equal \(F\)-polynomials have isomorphic *underlying unordered graphs*. This fails at \(n=6\), even for connected triangle-free graphs with different girths. On the ordered vertex set \(0<1<2<3<4<5\), set
\[
\begin{aligned}
E(G)&=\{04,05,12,14,15,23\},\\
E(H)&=\{04,05,12,13,15,24\}.
\end{aligned}
\]
Here \(ij\) denotes the undirected edge with endpoints \(i,j\). Both graphs are connected and triangle-free, but \(G\) has a four-cycle whereas \(H\) has no four-cycle. Nevertheless, their entire two-variable singleton-type polynomials agree:
\[
\boxed{F_G(u,v)=F_H(u,v)=7+21u+21v+22u^2+17uv+24v^2+5u^3+4u^2v+4uv^2+8v^3.}
\]

**Persistent connected obstruction.** For every integer \(t\ge0\), obtain \(G_t,H_t\) by adjoining \(t\) later-ordered, pairwise nonadjacent vertices, each adjacent to exactly the two old vertices \(3,4\). Then \(G_t,H_t\) are connected triangle-free ordered graphs of size \(6+t\) with \(F_{G_t}=F_{H_t}\), yet their numbers of (unoriented, unrooted) four-cycles are \(\binom t2+1\) and \(\binom t2\), respectively. In particular, the ordered spectrum fails to recover a four-cycle count at **every** order \(n\ge6\), even on connected triangle-free bases.

## Assumptions and scope
All graphs are finite, simple, and undirected; an order is a named binary linear-order relation, not a post hoc numbering to be forgotten in the type count. Parameters are individually named and their listed order is fixed. A nonalgebraic singleton type requires the new point to be distinct from all parameters. The types are complete types of the homogeneous ordered structure, not arbitrary independently chosen graph patterns; their equivalence with the finite graph/order patterns follows from homogeneity and the extension property. The two variables mark **adjacencies on the two sides of the new point**, not all preceding/succeeding parameters. The reconstruction statement distinguishes underlying *graph isomorphism*, which is weaker than isomorphism preserving the listed order.

## Proof
**1. Exact type-to-independent-set formula.** A new point can lie in one of the \(n+1\) gaps of the ordered parameters, indexed \(j=0,\ldots,n\), with exactly \(j\) parameters before it. Its neighborhood among the named vertices must be an independent set \(S\): otherwise the new point and an old edge within \(S\) form a triangle. Conversely, for every independent \(S\) and every gap \(j\), adding such a point creates a finite triangle-free ordered extension, which occurs over the named copy of \(G\) in the Fraïssé limit. The same pattern has one complete type by ultrahomogeneity, and infinitely many distinct realizations are possible. Thus
\[
\boxed{F_G(u,v)=\sum_{j=0}^n\ \sum_{\substack{S\subseteq\{0,\ldots,n-1\}\\S\text{ independent in }G}}u^{|S\cap[0,j)|}v^{|S\cap[j,n)|}.}\tag{1}
\]
In particular \(F_G(z,z)=(n+1)I_G(z)\), where \(I_G\) is the ordinary independence polynomial. Formula (1) makes the invariant a strict two-sided positional refinement of classical independent-set enumeration.

**2. Exact six-point witness.** Both edge sets displayed above contain six edges and induce connected graphs. In \(G\), vertices \(0,4,1,5\) form a four-cycle. In \(H\), the unique cycle on the six original vertices is \(0,4,2,1,5,0\), a five-cycle; vertex \(3\) is pendant. The independent-set polynomials agree, \(I_G(z)=I_H(z)=1+6z+9z^2+3z^3\). Direct finite evaluation of (1), more informatively by each gap, yields identical gap polynomials at \(j=0,1,3,5,6\) and
\[
\begin{aligned}
F_{G,j=2}-F_{H,j=2}&=u^2v-uv^2,\\
F_{G,j=4}-F_{H,j=4}&=-u^2v+uv^2.
\end{aligned}\tag{2}
\]
They cancel exactly upon summing over all gaps; the common polynomial is as displayed in the finding. This is an exact integer calculation and is independently reproduced by the bundled checker.

**3. First-order completeness.** For each \(1\le n\le5\), enumerate all \(2^{\binom n2}\) adjacency masks on \(n\) ordered vertices, discard masks containing a triangle, and compute (1) as an integer coefficient vector. The resulting numbers of triangle-free labelled masks are respectively \(1,2,7,41,388\), with \(1,2,7,36,337\) distinct coefficient vectors. In each polynomial fiber, compute a canonical **unlabelled** graph code by taking the lexicographically least adjacency edge list over all \(n!\) vertex permutations. Every fiber has a single canonical code. These finite procedures are exhaustive, not samples: every simple graph on the fixed ordered vertex set has exactly one adjacency mask, every simple triangle-free mask passes the explicit triangle test, and the permutation minimum is an exact isomorphism test. The included standard-library program supplies the full reproducible exhaustive certificate. The six-point pair in step 2 establishes sharpness.

**4. An all-order twin-extension lemma.** Suppose two ordered graphs \(A,B\) on the same ordered vertex set satisfy \(F_A=F_B\), and for some common vertex subset \(W\), the graphs induced on the complement \(V\setminus W\) are identical (as ordered graphs). Append any number of new last vertices that are mutually nonadjacent and adjacent precisely to the old set \(W\). Then the resulting ordered type polynomials still coincide, provided the extensions are in the triangle-free class. Indeed split the old independent sets in (1) according to whether they meet \(W\). If they avoid \(W\), the contributions for all new gaps and all choices among the appended vertices agree term-by-term, since the old induced graphs on \(V\setminus W\) agree. If they meet \(W\), no appended vertex may lie in the extension neighborhood. For any old gap, the total difference over these sets is the old difference \(F_A-F_B\), because the avoid-\(W\) contribution cancels; hence summing old gaps gives zero. For each new gap all old parameters lie before the new point, so the difference is the one-variable polynomial of old independent sets meeting \(W\). That difference is zero as well: \(I_A=I_B\) follows from \(F_A(z,z)=F_B(z,z)\), and \(I_{A-W}=I_{B-W}\) follows from equality of the induced complements. This proves the lemma for every number of appended vertices.

Apply the lemma to \(A=G,B=H,W=\{3,4\}\). The induced graph on \(\{0,1,2,5\}\) has exactly the three edges \(05,12,15\) in either case. Moreover \(3\) and \(4\) are nonadjacent, so the enlarged graphs are triangle-free. Both are connected because the original graphs are connected and each new vertex has two old neighbors.

**5. Four-cycle separation at every size.** In either original graph the neighborhoods of \(3\) and \(4\) are disjoint: they are \(\{2\}\) and \(\{0,1\}\) in \(G\), and \(\{1\}\) and \(\{0,2\}\) in \(H\). Consequently no four-cycle contains exactly one appended vertex. Any four-cycle containing appended vertices must use exactly two of them with the common old neighbors \(3,4\), giving precisely \(\binom t2\) cycles in either enlarged graph. The old graphs contribute one four-cycle in \(G\) and zero in \(H\), proving the claimed counts and nonisomorphism for every \(t\ge0\).

## Verification
Run `python3 verify.py` in the directory of the extracted files. It needs only the Python standard library. The checker implements the finite graph enumeration, exact triangle criterion, coefficient-by-coefficient type spectrum, graph canonicalization by all vertex permutations, the explicit witness and the all-order construction at the seven tested sizes \(t=0,\ldots,6\). It separately checks the gap cancellations in (2), the common independence polynomial and exact four-cycle counts. Its recorded output is in `verification_output.txt` and ends in `VERIFY_OK`.

The finite checker proves the finite cutoff through exhaustive explicit loops, but only *tests* the first seven cases of the infinite family; the argument in steps 4 and 5 proves the extension for all \(t\ge0\). Its output is not a replacement for the stated all-order reasoning.

## Relationship to prior work
Henson's 1971 homogeneous clique-free graphs and Conant's 2014 treatment of their complete types supply the fundamental extension framework; the finite-type admissibility rule is prior. Adding an unrestricted linear order produces the corresponding classical homogeneous ordered expansion. The ordinary independence polynomial is also classical, and our identity \(F_G(z,z)=(n+1)I_G(z)\) explicitly acknowledges this specialization. The 2003 paper of Levit and Mandrescu, Oboudi's 2013 work, and the full-text 2018 independence-equivalence paper of Beaton, Brown and Cameron concern ordinary independence-polynomial roots, orderings of graphs by real-root comparison, or classical independence equivalence; they do not give the positional two-sided invariant, its sharp six-point obstruction, or the infinite connected twin-extension family. Here the phrase “ordering on graphs” in Oboudi is an ordering of graphs by a polynomial comparison, **not** an ordered-graph relation in a Fraïssé structure.

Two publicly available Henson type-enumeration notes give, respectively, the classical independent-neighborhood specialization with exact-counting complexity and a Cartesian-product formula for higher arities in the *unordered* homogeneous triangle-free graph. Their mathematical statements were inspected in full. Neither handles a freely ordered base, insertion gaps, two-sided positional grading, or graph reconstruction from that grading. The 2018 independence-equivalence discussion is a close comparison but its one-variable equality is strictly weaker: changing only the vertex order can change \(F\) without changing \(I\). A literal and semantic search for positional independence cut sums, ordered homogeneous triangle-free type polynomials, and girth-blind six-point collisions did not locate a covering theorem. These searches do not establish historical uniqueness; an unindexed equivalent remains a possibility.

## Limitations
The cutoff theorem is computationally exhaustive **only through five named vertices**; the first witness and the infinite family do not classify all later collisions. The theorem concerns finite ordered triangle-free bases, complete nonalgebraic singleton types and a specific bivariate adjacency grading. No claim is made for higher-arity types, other homogeneous graph classes or full type spaces. The nonisomorphism conclusion concerns underlying unordered graphs; a collision between different ordered presentations of an isomorphic graph already occurs at smaller sizes. The independent-set relation and standard homogeneous-extension facts are not claimed as original. An unindexed earlier positional-polynomial result remains possible.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* 38 (1971), 69–83, DOI: 10.2140/pjm.1971.38.69.
2. G. Conant, “Forking and dividing in Henson graphs,” first public arXiv submission 2014-01-08, arXiv:1401.1570, https://arxiv.org/html/1401.1570v1.
3. V. E. Levit and E. Mandrescu, “On the roots of independence polynomials of almost all very well-covered graphs,” first arXiv submission 2003-05-15, arXiv:math/0305227, https://arxiv.org/abs/math/0305227.
4. M. R. Oboudi, “On the largest real root of independence polynomials of graphs, an ordering on graphs, and starlike trees,” first arXiv submission 2013-03-13, arXiv:1303.3222, https://arxiv.org/abs/1303.3222.
5. I. Beaton, J. I. Brown and B. Cameron, “Independence equivalence classes of paths and cycles,” first arXiv submission 2018-10-12, arXiv:1810.05317, https://arxiv.org/abs/1810.05317.
6. “Exact finite-parameter 1-type counting in Henson graphs is #P-complete,” publicly available mathematics note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650.
7. “Higher-arity Henson type enumeration and exact-counting hardness,” publicly available mathematics note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-higher-arity-henson-type-enumeration-and-exact-counting-hardness--141a441755d6.
