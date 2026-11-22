# A four-core switch in inverse-square two-leader placement on clique coronas

## Finding

For every integer \(n\ge3\), let \(H_n=K_n\circ K_1\) be the unit-weight graph obtained by attaching one private leaf \(p_i\) to each vertex \(c_i\) of a complete graph \(K_n\). Choose exactly two perfectly pinned (noise-free) vertices \(S\). Set \(F=V(H_n)\setminus S\) and minimize the **unscaled** grounded inverse-square objective
\[
J_2(S)=\operatorname{tr}\bigl(L_{FF}(S)^{-2}\bigr),
\]
where \(L\) is the original combinatorial Laplacian (the diagonal keeps all original degrees). **Every** minimizing leader pair is of the following form, with no unlisted ties:

* At \(n=3\), exactly one core \(c_i\) and the private leaf \(p_j\) of a *different* core, \(i\ne j\). There are exactly six optimal pairs and the minimum is \(124/25\).
* At every \(n\ge4\), any two distinct core vertices \(\{c_i,c_j\}\). There are exactly \(\binom n2\) optimal pairs and
  \[
  J_2^*(n)=\frac{(n+2)(n^2+2n-6)}{n^2}.
  \]

For the *first* inverse-power objective \(J_1(S)=\operatorname{tr}(L_{FF}^{-1})\), a previously established all-budget theorem gives only the core–different-leaf pairs for every \(n\ge3\). Thus, for each \(n\ge4\), the two spectral design objectives have **disjoint** globally optimal leader sets on the same graph, with a sharp inverse-square transition at four core vertices.

## Assumptions and scope

The graph has \(2n\) vertices, every edge has conductance one, the two leaders are fixed perfectly, all followers are retained in the grounded block, and no positive-edge perturbations or leader-gain optimization are performed. Each original core has degree \(n\), each leaf has degree one. The objective is the sum of squared inverse positive eigenvalues of the follower matrix; a multiplicative physical variance factor, if introduced, does not alter its optimizer. All statements are for integers \(n\ge3\) with precisely two distinct leaders, and all inequalities at the listed boundary are strict except within each symmetry orbit.

## Proof

**1. Four orbits exhaust the design space.** Permuting the \(n\) core–leaf pairs preserves the graph. Every unordered two-leader set belongs to precisely one of the types \(CC=\{c_i,c_j\}\), \(CL_s=\{c_i,p_i\}\), \(CL_d=\{c_i,p_j\}\) for \(i\ne j\), or \(LL=\{p_i,p_j\}\) for \(i\ne j\). Therefore an exact comparison of these four grounded matrices is exhaustive.

**2. Determinants from a leaf Schur complement.** For an indeterminate \(t\), put
\[
A(t)=n+(n+2)t+t^2,\qquad B(t)=n+1+t,
\qquad D_S(t)=\det(L_{FF}(S)+tI).
\]
Let \(r\) be the number of follower cores, \(d\) the number of those follower cores whose leaves are leaders, and \(h\) the number of follower leaves whose own cores are leaders. Schur elimination of the other \(r-d\) follower leaves gives the exact identity
\[
D_S(t)=(1+t)^h A(t)^{r-d}B(t)^d
\left[1-\frac{(r-d)(1+t)}{A(t)}-\frac d{B(t)}\right].\tag{1}
\]
Indeed, among follower cores the core–core block before eliminating leaves is \((n+1+t)I-\mathbf1\mathbf1^{\mathsf T}\); each attached follower leaf contributes \(-1/(1+t)\) to its own diagonal, whereas a leaf whose core is a leader is an isolated degree-one follower. The remaining diagonal-plus-rank-one determinant is evaluated by the matrix determinant lemma. Each expression below is a polynomial even where its factored form uses a rational intermediate.

The four types respectively have \((r,h,d)=(n-2,2,0),(n-1,0,0),(n-1,1,1),(n,0,2)\), whence
\[
\begin{aligned}
D_{CC}&=(1+t)^2A^{n-3}\,[A-(n-2)(1+t)],\\
D_{CL_s}&=A^{n-2}\,[A-(n-1)(1+t)],\\
D_{CL_d}&=(1+t)A^{n-3}\,[AB-(n-2)(1+t)B-A],\\
D_{LL}&=A^{n-3}B\,[AB-(n-2)(1+t)B-2A].
\end{aligned}\tag{2}
\]
The determinant at zero is positive, since a grounded Laplacian of a connected graph with at least one pinned vertex is positive definite. Its eigenvalues are positive; logarithmic differentiation therefore gives
\[
\left.\frac{d}{dt}\log D_S(t)\right|_{t=0}=J_1(S),\qquad
-\left.\frac{d^2}{dt^2}\log D_S(t)\right|_{t=0}=J_2(S).\tag{3}
\]

**3. Exact inverse-square orbit costs.** Applying (3) term-by-term to (2) produces
\[
\begin{aligned}
J_2(CC)&=\frac{(n+2)(n^2+2n-6)}{n^2},\\
J_2(CL_s)&=\frac{(n-1)(n^2+8n+8)}{n^2},\\
J_2(CL_d)&=\frac{n^5+11n^4+14n^3-20n^2-56n-48}{n^2(n+2)^2},\\
J_2(LL)&=\frac{n^6+4n^5+2n^4-6n^3-18n^2-26n-12}{n^2(n+1)^2}.
\end{aligned}\tag{4}
\]
All denominators are positive for \(n\ge3\). Subtracting gives four explicit comparison certificates:
\[
\begin{aligned}
J_2(CC)-J_2(CL_d)&=-\frac{3n^2-4n-16}{(n+2)^2},\\
J_2(CL_s)-J_2(CC)&=\frac{3n^2+2n+4}{n^2}>0,\\
J_2(LL)-J_2(CC)&=\frac{n^4+3n^3-4n^2-13n-6}{(n+1)^2}>0,\\
J_2(CL_s)-J_2(CL_d)&=\frac{2(9n^3+20n^2+12n+8)}{n^2(n+2)^2}>0.
\end{aligned}\tag{5}
\]
The quartic numerator in the third line is positive because putting \(n=x+3\), \(x\ge0\), transforms it to \(x^4+15x^3+77x^2+152x+81\). Finally, \(3n^2-4n-16=-1\) at \(n=3\), whereas it is positive and strictly increasing for integers \(n\ge4\) (already \(16\) at \(n=4\)). Thus \(CL_d\) strictly wins when \(n=3\), and \(CC\) strictly wins for every \(n\ge4\). This comparison covers all four types, completing the unrestricted classification. The minimum at \(n=3\) follows by inserting \(n=3\) into (4); orbit sizes follow from core-pair permutations.

**4. Exact contrast with first inverse power.** The same determinant derivatives give
\[
J_1(CC)=\frac{n^2+3n-6}{n},\qquad
J_1(CL_d)=\frac{n^3+5n^2-2n-12}{n(n+2)},
\]
and hence \(J_1(CC)-J_1(CL_d)=2/(n+2)>0\). The all-budget first-power classification in reference [3], specialized to a budget of two, establishes that \(CL_d\) strictly beats the other two types as well for every \(n\ge3\) (its threshold polynomial at budget two is \(-2n^3+8n+4<0\)). Thus the two problems have disjoint optimizers for every \(n\ge4\). The differing conclusion is not an implication of that earlier first-power theorem.

## Verification

The standalone `verify.py` uses SymPy for *exact* symbolic logarithmic derivatives and rational polynomial comparisons, and independently constructs each full grounded Laplacian by its edge list. It checks the exact inverse and squared-inverse traces of all two-leader sets exhaustively for \(3\le n\le6\), then one representative of each orbit for \(n=7,8\). It also compares the characteristic polynomial with (2) in the exhaustive range. A successful replay reports 162 exact grounded-matrix comparisons together with the symbolic identities and all tested optimality classes. All-size conclusions come from (1)–(5), not from finite enumeration.

## Relationship to prior work

Lin, Fardad and Jovanović [1] define the noise-free inverse-trace leader-allocation problem and develop optimization relaxations; the full text's formulation and algorithmic examples do not classify squared-inverse two-leader optima on clique coronas. Patterson and Bamieh [2] develop second-order spectral coherence for ungrounded fractal networks, including the reciprocal-square Laplacian sum, rather than optimizing grounded leader pairs on this graph.

The closest same-graph prior result [3] proves a **different functional**, the first inverse trace \(\operatorname{tr}(L_{FF}^{-1})\), at all leader budgets. Its proof and exact occupancy formula imply the first-power location types quoted above, but not (4), (5), or the switch to two core leaders. A separate same-graph finite-gain result [4] optimizes \(\operatorname{tr}[(L+\kappa\operatorname{diag}(\mathbf1_S))^{-1}]\) for \(\kappa>0\); this is neither the squared grounded inverse nor its all-size minimizing classification. Finally, Du et al. [5] investigate ungrounded first-order coherence and Laplacian polynomials of weighted coronas, not leader optimization of inverse-squared grounded Laplacians. These are comparisons of mathematical statements, not title-based exclusions.

## Limitations

The exact theorem does not cover other core graphs, nonuniform conductances or follower noise variances, nonperfect leaders, three or more leaders, or arbitrary spectral order. The interpretation as second-order performance depends on the chosen noise and feedback normalization; the unscaled matrix objective is unambiguous. Symbolic computations and finite full-matrix replay support the algebra, but only the presented proof establishes the infinite-size statement. Literature search cannot establish absolute publication priority: an unindexed equivalent result or an uninspected specialization of a broader theorem remains possible. Independent mathematical audit has not been performed.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, first public posting 2013-02-03, arXiv:1302.0450v1, full accessible text https://arxiv.org/html/1302.0450v2 (especially Section 2.1 and Section 4).
2. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, first public posting 2013-10-09, arXiv:1310.2592v1, full text https://arxiv.org/html/1310.2592v1 (especially Sections II-B and IV and appendices).
3. *A sharp all-budget leader transition on complete-clique coronas*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-sharp-all-budget-leader-transition-on-complete-clique-coronas--9b274a4d27c1/RESULT.md (full theorem and proof, first inverse-power criterion).
4. *Exact two-leader gain transition on complete-graph coronas*, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-exact-two-leader-gain-transition-on-complete-graph-coronas--17423e28b87e/RESULT.md (finite-gain first inverse power).
5. W. Du, J. Zhu, H. Gao, and X. Li, *Consensus analysis of the weighted corona networks*, *Frontiers in Physics* 10 (2022), https://doi.org/10.3389/fphy.2022.948247 (Sections 3–6, first-order ungrounded network coherence).
