# A sharp dimension–alphabet dependence phase diagram for two-step Hamming random graphs

## Finding

For integers \(q\ge2\), \(d\ge1\), and \(n\ge3\), independently sample \(n\) uniform words from \(\{0,\ldots,q-1\}^d\), **with replacement**, and join two different sampled vertices exactly when their words have Hamming distance one or two. Let \(D_1,D_2\) be the degrees of a specified pair conditional on the pair being an edge, and \(M_n\) the total number of edges. The complete two-vertex edge-conditioned probability generating function, a strict sign phase diagram for \(\operatorname{Cov}(D_1,D_2\mid 12\in E)\), and the exact sign of the third cumulant of \(M_n\) are given below.

Put \(b=q-1\), \(N=q^d\), \(A=db+\binom d2 b^2\), \(p=A/N\), and
\[
c_1=(d-1)b^2+db-1,\qquad c_2=b^2+2(d-1)b-1,
\]
\[
B=db\,c_1+\binom d2b^2c_2,\qquad
\Delta=\frac{B}{AN}-\frac{A^2}{N^2}=\frac{NB-A^3}{AN^2}.
\]
The term containing \(c_2\) is absent for \(d=1\). Define
\[
F_h(s,t)=1-2p+\frac{c_h}{N}+\left(p-\frac{c_h}{N}\right)(s+t)+\frac{c_h}{N}st.
\]
Then for all \(s,t\in\mathbb C\),
\[
\mathbb E[s^{D_1-1}t^{D_2-1}\mid 12\in E]
=\frac{db}{A}F_1(s,t)^{n-2}+\frac{\binom d2b^2}{A}F_2(s,t)^{n-2}.
\]
In particular each conditional marginal is \(1+\operatorname{Bin}(n-2,p)\), while
\[
\boxed{\operatorname{Cov}(D_1,D_2\mid 12\in E)=(n-2)\Delta.}
\]
The strict sign classification is
\[
\boxed{
\Delta>0\ \Longleftrightarrow\quad
(q=2,\ d\ge5)\ \text{or}\ (q=3,\ d\ge4)\ \text{or}\ (q\ge4,\ d\ge3).
}
\]
For all other allowed \((q,d)\), \(\Delta<0\); it is never zero. Thus the first positive-dependence dimension is five for binary words, four for ternary words, and three for every larger alphabet.

All two distinct edge indicators are pairwise independent, and every collection of edge indicators indexed by a forest is jointly independent. Yet each labelled triangle has centered third edge moment \(p\Delta\). Consequently
\[
\boxed{\kappa_3(M_n)=\binom n2 p(1-p)(1-2p)+6\binom n3p\Delta.}
\]
Its sign is positive precisely in the positive-\(\Delta\) cases, **except** \((q,d,n)=(4,3,3)\), where it is negative; it is strictly negative otherwise, with no zero cases. At \((q,d)=(4,3)\), the exact formula is
\[
\kappa_3(M_n)=\frac{9n(n-1)(5n-17)}{4096},
\]
so the unique sample-size sign reversal occurs between three and four vertices.

## Assumptions and scope

The \(n\) latent words are iid and may repeat. Vertex labels remain distinct even when their latent words coincide; coincident words have Hamming distance zero and no edge. Connection is deterministic given labels, with permitted distances exactly one and two (not zero). The alphabet is symmetric, not assumed binary; \(q,d,n\) are integers in the indicated ranges. All probabilities and cumulants refer to the finite-sample labelled graph, not an asymptotic random-graph limit. The conditional distribution is defined because \(0<p<1\) throughout the parameter range. The words' coordinate alphabets have the same size \(q\).

## Proof

**1. Common-neighbor counts.** The graph on the \(N=q^d\) possible latent words is regular of degree \(A\). There are \(db\) neighbors at distance one and \(\binom d2b^2\) at distance two from a fixed word. For two words at distance one, partition common neighbors according to whether their distinguishing coordinate equals neither endpoint value, or one of the two endpoint values, and whether exactly one additional coordinate changes. The disjoint classes have sizes \(b-1\), \(2(d-1)b\), and \((b-1)(d-1)b\), giving \(c_1=(d-1)b^2+db-1\). At distance two, the disjoint classes of common neighbors have sizes \(2\) (one endpoint value in each distinguishing coordinate), \(4(b-1)\) (one new value), \((b-1)^2\) (two new values), and \(2(d-2)b\) (a mixed endpoint choice and one extra changed coordinate). Their sum is \(c_2=b^2+2(d-1)b-1\). Both counts can equivalently be checked by intersecting two Hamming balls of radii one or two and removing the centers.

**2. Conditional joint law.** The directed pair \((X_1,X_2)\), conditional on adjacency, has distance one with probability \(db/A\) and distance two with probability \(\binom d2b^2/A\). For a third independent word, conditional on this distance \(h\), the two incident-edge indicators have probabilities \(c_h/N\) for \((1,1)\), \(p-c_h/N\) for each of \((1,0),(0,1)\), and \(1-2p+c_h/N\) for \((0,0)\). All \(n-2\) other independent labels give iid copies of this pair conditional on \(X_1,X_2\). Homogeneity makes these probabilities depend only on the distance, proving the asserted mixture of generating functions. The covariance is \((n-2)(B/(AN)-p^2)\), as claimed.

**3. Strict sign classification.** Let \(S_d=NB-A^3\). Direct expansion gives \(S_1=-b\), \(S_2=-b(b+2)\), and
\[
S_3=3b(b+1)^3(b^3-3b^2+2b-1).
\]
The last factor is negative at \(b=1,2\), and at \(b=3+u\) it equals \(u^3+6u^2+11u+5>0\) for every integer \(u\ge0\). Also \(S_4\vert_{b=1}=-40\). These are precisely the proposed negative cases.

For the infinite positive cases note \(c_1-c_2=(d-2)b(b-1)\ge0\) when \(d\ge2\), so \(B/A\ge c_2\). It suffices to prove \(L_d=Nc_2/A^2>1\). For fixed \(b\ge1\), \(L_d\) is strictly increasing for every \(d\ge3\). Indeed, \(L_{d+1}>L_d\) is equivalent to
\[
(b+1)c_2(d+1)A_d^2-c_2(d)A_{d+1}^2>0,
\]
where \(A_d=db+\binom d2b^2\) and \(c_2(d)=b^2+2(d-1)b-1\). On writing \(d=t+3\), \(b=u+1\) with \(t,u\ge0\), **four times** the expression is \(b^2\sum_{j=0}^{5}C_j(t)u^j\), where
\[
\begin{aligned}
C_0&=2(t+1)^2(t+4)^3,\\
C_1&=8(t+3)^2(t+4)(t^2+4t+2),\\
C_2&=12t^5+169t^4+926t^3+2425t^2+2928t+1184,\\
C_3&=(t+3)(8t^4+91t^3+373t^2+632t+344),\\
C_4&=(t+3)^2(2t^3+19t^2+52t+40),\\
C_5&=(t+2)^2(t+3)^2.
\end{aligned}
\]
Each coefficient is strictly positive on \(t\ge0\). For \(d=3,b\ge4\), the lower-bound numerator \(Nc_2-A^2\) factors as \((b+1)^2(b^3-4b^2+3b-1)\); at \(b=4+u\) its cubic factor is \(u^3+8u^2+19u+11>0\). The remaining base cases \(d=4,b\ge2\) and \(d=5,b\ge1\) follow from the respective positive-coefficient expansions of \(Nc_2-A^2\) after substituting \(b=2+u\) and \(b=1+u\):
\[
\begin{aligned}
&u^6+22u^5+153u^4+492u^3+803u^2+638u+191,\\
&u^7+20u^6+148u^5+460u^4+700u^3+547u^2+210u+31.
\end{aligned}
\]
(The first line has leading coefficient \(1\) after substitution; both expansions are directly checkable.) Along with the direct positive case \((d,b)=(3,3)\) from \(S_3\), monotonicity covers all remaining dimensions. Thus \(\Delta\) is never zero and has the asserted signs.

**4. Triangle moments and the third cumulant.** For any forest of distinct edges, successively integrate over a leaf's uniform latent label; its incident edge has conditional probability exactly \(p\) regardless of the other endpoint. This proves joint independence along forests. In a labelled triangle, the first two edges have probability \(p^2\) and the three-edge probability is \(pB/(AN)\). Therefore the triple centered product is \(p(B/(AN)-p^2)=p\Delta\). Multilinearity of the third cumulant of \(M_n\) leaves only individual-edge Bernoulli third cumulants and the six permutations of each triangle's three distinct edges; contributions involving two repetitions and one different edge vanish by pairwise independence. This proves the formula.

In every negative-\(\Delta\) regime, \(p\ge1/2\); both terms in the cumulant formula are then nonpositive, and the triangle term is strictly negative. In all positive-\(\Delta\) regimes except \((q,d)=(4,3)\), \(p\le1/2\), making the cumulant strictly positive. To verify these comparisons, use \(p=d b[2+(d-1)b]/[2(b+1)^d]\), which strictly decreases in \(d\ge3\), together with \(p(2,5)=15/32\), \(p(3,4)=32/81\), and \(p(q,3)=3(q-1)/q^2\le12/25\) for \(q\ge5\). The exceptional \(q=4,d=3\) has \(p=9/16\), \(\Delta=5/256\); substitution gives \(\kappa_3(M_n)=9n(n-1)(5n-17)/4096\), yielding the stated one-step reversal.

## Verification

The accompanying standalone Python file `checker.py` uses only the standard library and integer or rational arithmetic. Execute `python3 checker.py` from the directory containing the extracted file. It independently enumerates ambient Hamming-neighbor intersections, all finite labelled graphs for selected parameters, the complete edge-conditioned degree pair distribution, and the edge-count third cumulant; it checks the sign classification on a larger finite parameter grid. The checker reports **3,149 exact assertions passed**. The infinite-dimensional classification does not follow from those finite tests: its proof uses the explicit positive polynomial certificates above.

## Relationship to prior work

The random algebraic graph framework of Bangachev and Bresler [2] includes random labelled samples from finite abelian groups with symmetric connection functions, and its Fourier formula for expected signed triangles covers the general moment identity used in Step 4 when specialized to the binary group. Thus neither the general signed-triangle identity nor the idea of counting signed triangles is claimed as new. Liu and Rácz [1] study signed-triangle detection in spherical latent-space random graphs, a different connection model. Adamaszek and Adams [3] study deterministic Vietoris–Rips complexes of hypercube graphs, not conditional random-sample degree laws. The contribution assessed here is the **complete explicit q-ary dimension–alphabet sign classification**, joint finite edge-conditioned degree law, and the resulting all-parameter skewness classification with its unique three-vertex exception. Standard Hamming intersection numbers underlie the calculation and are not claimed original.

## Limitations

The result treats a fixed radius set \(\{1,2\}\), not arbitrary thresholds or nonuniform latent labels. Repeat labels are explicitly permitted. The edge-degree correlation conditional on adjacency is not the same as the empirical assortativity coefficient in a single realization. The third cumulant establishes a skewness sign, not a stochastic ordering or a distributional approximation. Numerical enumeration proves only the finite instances checked. A broad algebraic-graph Fourier framework already contains general signed-triangle moment expressions, so priority is claimed only for the specialized sharp phase and joint-law classifications. Earlier specialized results under other terminology remain a literature-priority risk; independent verification has not been performed.

## References

[1] S. Liu and M. Z. Rácz, “Phase transition in noisy high-dimensional random geometric graphs,” first public 28 March 2021, https://arxiv.org/abs/2103.15249 (especially the signed-triangle arguments).

[2] K. Bangachev and G. Bresler, “Random Algebraic Graphs and Their Convergence to Erdős–Rényi,” first public May 2023, https://arxiv.org/abs/2305.04802 (Sections 1.3, 2 and 6, particularly signed-triangle and finite-group coverage).

[3] M. Adamaszek and H. Adams, “On Vietoris–Rips complexes of hypercube graphs,” first public March 2021, https://arxiv.org/abs/2103.01040 (deterministic Hamming graph powers).
