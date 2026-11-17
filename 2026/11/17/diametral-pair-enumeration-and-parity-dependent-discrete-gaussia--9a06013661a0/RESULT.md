# Diametral-pair enumeration and parity-dependent discrete Gaussian law for strong-total-cover polytopes of complete graphs

## Finding
For each integer \(n\geq3\), let \(G=K_n\) on a labelled vertex set, let \(D=V(G)\sqcup E(G)\), and let \(P_n\subseteq\mathbb R^D\) be the convex hull of the indicator vectors of its strong total covers. Write \(N=n+\binom n2\). An unordered pair of vertices of \(P_n\) is called *diametral* when its Euclidean distance equals the diameter.

**Theorem.** The diameter is \(\sqrt N\). Every diametral pair is uniquely \(\{\mathbf 1_C,\mathbf 1_{D\setminus C}\}\), with both \(C\) and its complement strong total covers. The number of unordered diametral pairs is exactly
\[
\boxed{H_n=\frac12\left(\sum_{a=0}^n\binom na2^{a(n-a)}-2n\right).}
\]
More precisely, among *ordered* choices of a diametral pair, where the first cover contains \(a\) original graph vertices, the number is
\[
\boxed{M_{n,a}=\binom na2^{a(n-a)}-n\,\mathbf 1_{\{a=1\}}-n\,\mathbf 1_{\{a=n-1\}}\quad (0\le a\le n).}
\]
Consequently \(\sum_{a=0}^nM_{n,a}=2H_n\). This equality counts the two possible orientations of each pair.

Select an ordered diametral pair uniformly and let \(A_n\) count the original graph vertices in its first cover. Put \(m=\lfloor n/2\rfloor\) and \(J_n=A_n-m\). Define
\[
\Theta_0=\sum_{j\in\mathbb Z}2^{-j^2},\qquad \Theta_1=\sum_{j\in\mathbb Z}2^{-j(j-1)}.
\]
Then the *entire integer-valued distribution*, not just its weak limit, satisfies
\[
\boxed{d_{\rm TV}\!\left(\mathcal L(J_n),\pi_{n\bmod2}\right)=O(n^{-1}),}\qquad
\pi_0(j)=\frac{2^{-j^2}}{\Theta_0},\quad
\pi_1(j)=\frac{2^{-j(j-1)}}{\Theta_1}.
\]
The implicit constant is absolute. In particular,
\[
\boxed{H_{2m}\sim\tfrac12\binom{2m}{m}2^{m^2}\Theta_0,\qquad
H_{2m+1}\sim\tfrac12\binom{2m+1}{m}2^{m(m+1)}\Theta_1.}
\]
The binomial-scale fluctuations that might have been expected from choosing original vertices collapse instead to an order-one, parity-dependent discrete Gaussian law.

## Assumptions and scope
A *strong total cover* is a set \(C\subseteq V(G)\sqcup E(G)\) such that every original vertex \(v\) belongs to \(C\) or some edge incident to \(v\) belongs to \(C\), and every original edge \(uv\) belongs to \(C\) or at least one of \(u,v\) belongs to \(C\). This is the convention of Aprile--Ferrarini, arXiv:2610.23312. The metric is the standard, *unweighted ambient Euclidean metric* on the \(N\) incidence-vector coordinates, not the graph distance in the polytope one-skeleton, a projected metric, or an inradius.

Only \(n\ge3\) is claimed. Original graph vertices and graph edges are distinct coordinates. The graph is the labelled complete graph, and all covers (not only minimum-cardinality covers) are included.

## Proof
**1. Binary extremal geometry.** All indicator vectors belong to \(\{0,1\}^N\). Every distinct binary point in a family is a vertex of its convex hull: if a convex combination equals a binary vector, each coordinate of every positively weighted term must equal that vector. Thus the vertex set of \(P_n\) consists exactly of the distinct cover indicators. Every two binary points have squared Euclidean distance equal to their Hamming distance, at most \(N\), with equality precisely when they are complementary. The set \(V(G)\) is a strong total cover (its endpoints cover every edge), as is \(E(G)\) (all vertices are incident to an edge), so the bound \(\sqrt N\) is attained. Moreover, a convex distance maximum on a polytope is attained at vertices, while the claimed classification concerns **vertex pairs**, not arbitrary pairs of points of the body.

**2. Two-color reconstruction.** Identify a binary cover with a red/blue coloring of each element of \(D\), putting the element in the first cover iff red. Both color classes are covers iff neither closed covering constraint is monochromatically deficient. At an edge \(uv\), the triple \((u,v,uv)\) must contain both colors; otherwise the monochromatic triple's opposite color fails to cover this edge. The vertex condition requires for each \(v\) that the star \(\{v\}\cup\delta(v)\) contains both colors. Fix the set \(A\) of red original vertices, of size \(a\), and its blue complement \(B\). For edges internal to \(A\), red endpoints force the edge blue. For edges internal to \(B\), blue endpoints force the edge red. Every one of the \(a(n-a)\) crossing edges can receive either color freely. This gives \(\binom na2^{a(n-a)}\) assignments satisfying **all edge constraints**.

If \(a=0\), the forced red edges give every blue vertex a red incident edge, since \(n\ge3\); if \(a=n\), the analogous statement holds. If \(2\le a\le n-2\), each red vertex has a blue edge to another red vertex, and each blue vertex has a red edge to another blue vertex, so every vertex constraint is automatic. If \(a=1\), the only obstruction is that the unique red vertex sees *no* blue crossing edge: of its \(2^{n-1}\) possibilities precisely one is excluded, for each of \(n\) choices of its position. All other vertices have forced red edges among their blue peers because \(n\ge3\). The case \(a=n-1\) is symmetric. Therefore the claimed \(M_{n,a}\) holds for every \(a\). Each complementary unordered pair gives two red-first assignments, proving the exact formula for \(H_n\). This also gives a complete, non-overlapping combinatorial classification of diametral pairs, not just a count.

**3. Concentration about a balanced vertex partition.** Put \(m=\lfloor n/2\rfloor\), \(a=m+j\), and normalize all counts by \(T_n=\binom nm2^{\lfloor n^2/4\rfloor}\). Define \(b_{n,j}=\binom n{m+j}/\binom nm\) for allowable \(j\), and zero outside. For \(n=2m\) the normalized uncorrected weight equals \(b_{n,j}2^{-j^2}\). For \(n=2m+1\) it equals \(b_{n,j}2^{-j(j-1)}\). In both cases \(0\le b_{n,j}\le1\).

For even \(n\) and \(j\ge0\), symmetry and the exact product
\[
 b_{2m,j}=\prod_{r=1}^j\frac{m-r+1}{m+r}
\]
show \(0\le 1-b_{2m,j}\le j^2/m\) for \(j\le m\), using \(1-\prod(1-u_r)\le\sum u_r\) and \((2r-1)/(m+r)\le2r/m\). The same holds for negative \(j\). For odd \(n\), the symmetry \(b_{2m+1,j}=b_{2m+1,1-j}\) and, for \(j\ge1\),
\[
 b_{2m+1,j}=\prod_{r=2}^j\frac{m+2-r}{m+r}
\]
show \(1-b_{2m+1,j}\le j(j-1)/m\) in range, extended to negative \(j\) by symmetry. The uncorrected normalized mass functions are therefore \(O(m^{-1})\) away in \(\ell^1(\mathbb Z)\) from the corresponding theta weights: sum the bounds against the convergent series \(\sum_j(1+j^2)2^{-j^2}\) or \(\sum_j(1+j^2)2^{-j(j-1)}\). The missing out-of-range theta tails decay as \(2^{-\Omega(m^2)}\). The two correction terms in \(M_{n,a}\) have combined unnormalized mass \(2n/T_n=o(1/m)\). Hence the total unnormalized \(\ell^1\) error is \(O(m^{-1})\). The theta normalizers are fixed positive constants, so dividing by total mass preserves this rate in total variation. Since \(m\asymp n\), this is \(O(n^{-1})\), proving both parity laws. Summing the same normalized weights without taking probabilities yields the stated asymptotics for \(H_n\). ∎

## Verification
The standalone `verify.py` uses Python's standard library only. It independently enumerates every binary cover and its complement for \(n=3,4,5\); the exact ordered counts are respectively \((1,9,9,1)\), \((1,28,96,28,1)\), and \((1,75,640,640,75,1)\), giving \(10\), \(77\), and \(716\) unordered diameter pairs. It also checks algebraic symmetry and integrality through \(n=100\) and evaluates finite-sample total-variation errors against truncated theta series for each parity. The all-dimensional count and the \(O(n^{-1})\) limit are established analytically above; these checks are not exhaustive for arbitrary \(n\).

Reproduce from a directory containing the accompanying file by running `python3 verify.py`. No source-code generation or external data download is required.

## Relationship to prior work
Aprile and Ferrarini introduce strong total covers and their polytope, and establish its relation to domination in incidence graphs; those definitions and the equivalence are prior work. In their publicly available full text, the geometric development focuses on inequalities and facet descriptions, including special cactus graphs, rather than ambient Euclidean diametral-pair enumeration. The elementary \(\sqrt N\) upper bound for binary points is not claimed as a novel general principle. The distinctive results asserted here concern the *complete-pair enumerator*, the exceptional singleton obstructions, and their non-binomial, parity-dependent limiting law. Counting pairs of complementary dominating sets in the incidence graph is an equivalent phrasing; an existing formula for such partitions could imply the new count despite different terminology.

## Limitations
This theorem applies only to the indicated complete-graph family, standard binary cover realization, and Euclidean vertex-pair diameter. It does not determine facet inequalities, a graph-skeleton diameter, the full ambient metric distribution among all vertices, or sharp conclusions for other graph families. The originality assessment is based on inspected accessible literature and targeted record searches; historical priority is provisional, since a result indexed under complementary dominating-set partitions, domatic colorings, or Boolean covering arrays could already imply some conclusions. No independent mathematical audit has been performed.

## References
1. M. Aprile and L. Ferrarini, *The Strong Total Cover Problem*, arXiv:2610.23312, first public submission 2026-10-16. https://arxiv.org/abs/2610.23312 . Full HTML manuscript consulted (sections 1, 2.1, 4 and 5).
2. Bibliography on dominating-set polytopes and incidence graphs cited in Aprile--Ferrarini, especially the discussion of Proposition 3 and the polyhedral results; these motivate the reduction but do not supply the enumerator derived here.
