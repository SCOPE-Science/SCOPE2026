# The quadratic-étale graph state sum for binary orthogonality varieties

## Finding

Let \(k\) be a field of characteristic different from two. Let \(G=(V,E)\) be any finite simple graph with \(n=|V|\) and let \((W,B)\) be a nondegenerate two-dimensional symmetric bilinear space over \(k\). Write \(X_G(B)\) for the **reduced** closed subvariety of \(W^V\) defined by \(B(v_i,v_j)=0\) for all edges \(\{i,j\}\in E\). Let \(S_B\) be the degree-two finite étale \(k\)-scheme of isotropic lines in \(\mathbb P(W)\), and let \(\mathbb L=[\mathbb A^1_k]\) in \(K_0(\operatorname{Var}_k)\).

For each subset \(U\subseteq V\), let \(b(U)\) and \(c(U)\) be the numbers of bipartite and nonbipartite connected components of the **induced graph** \(G[U]\), respectively. Isolated vertices count as bipartite components. For the empty subset, both numbers are zero. Then the following graph-state-sum formula holds **over every such field**:

\[
\boxed{[X_G(B)]=\sum_{U\subseteq V}(\mathbb L-1)^{|U|}(\mathbb L+1)^{b(U)}[S_B]^{c(U)}.}
\]

The virtual quadratic-étale class \(\eta_B=[S_B]-1\) satisfies \(\eta_B^2=1\) in \(K_0(\operatorname{Var}_k)\). Define the integral graph polynomial

\[
F_G(T,E)=\sum_{U\subseteq V}(T-1)^{|U|}(T+1)^{b(U)}(1+E)^{c(U)},
\]

and reduce it modulo \(E^2-1\), obtaining uniquely \(F_G(T,E)\equiv A_G(T)+E C_G(T)\) with \(A_G,C_G\in\mathbb Z[T]\). Then \([X_G(B)]=A_G(\mathbb L)+\eta_B C_G(\mathbb L)\). Thus all these motives depend on the quadratic space only through its isotropic-line étale algebra.

When \(k=\mathbb F_q\) with \(q\) odd, let \(\epsilon=\chi_q(-\det B)\in\{1,-1\}\), which is independent of the chosen basis. For every integer \(r\ge1\), setting \(Q=q^r\), we obtain the exact point count

\[
\boxed{\#X_G(B)(\mathbb F_{q^r})=A_G(Q)+\epsilon^r C_G(Q)
=\sum_{U\subseteq V}(Q-1)^{|U|}(Q+1)^{b(U)}(1+\epsilon^r)^{c(U)}.}
\]

If \(A_G(T)=\sum_j\alpha_jT^j\) and \(C_G(T)=\sum_j\gamma_jT^j\), the Hasse–Weil zeta function is the finite product

\[
\boxed{Z(X_G(B),z)=\prod_{j=0}^{2n}(1-q^jz)^{-\alpha_j}(1-\epsilon q^jz)^{-\gamma_j}.}
\]

All exponents are integral, and negative exponents are permitted in this rational-function expression.

In particular, for the complete graph on \(h\ge3\) vertices, put

\[
\begin{aligned}
A_h(T)&=T^h+hT(T-1)+\binom h2 T(T-1)^2,\\
C_h(T)&=T^h-1-h(T-1)-\binom h2(T-1)^2.
\end{aligned}
\]

Then \([X_{K_h}(B)]=A_h(\mathbb L)+\eta_B C_h(\mathbb L)\) and \(\#X_{K_h}(B)(\mathbb F_{q^r})=A_h(q^r)+\epsilon^rC_h(q^r)\). For \(h\ge4\), the split and nonsplit counts have different polynomial growth degrees: \(h\) and three, respectively. This is a Galois-sensitive distinction not determined by the abstract geometric component dimensions alone.

## Assumptions and scope

The graph is finite and simple; every vector, including zero, is admitted. All orthogonality equations are imposed only along graph edges. The quadratic form is nondegenerate and the characteristic is not two. The class concerns the **reduced variety** underlying the common zero set, not a claim about an arbitrary scheme structure in characteristic two. The motivic equality is in the ordinary Grothendieck ring of reduced, separated varieties of finite type over \(k\); it is not merely an equality of point-counting functions. Finite-field counts and zeta functions apply to the reductions over finite fields of odd cardinality.

## Proof

**Step 1: The projective orthogonality involution.** Each nonzero vector \(v\in W\) determines a line \([v]\in\mathbb P(W)\). Nondegeneracy of \(B\) gives an algebraic involution \(\iota:\mathbb P(W)\to\mathbb P(W)\), sending a line to its orthogonal complement. The fixed scheme \(S_B\) is exactly the zero locus of the nondegenerate binary quadratic form \(B(v,v)\). Its discriminant is \(-4\det B\), up to a square, so \(S_B\) is finite étale of degree two in characteristic different from two.

**Step 2: Stratification by nonzero support.** Partition the reduced variety disjointly into locally closed subsets \(X_U\), indexed by \(U\subseteq V\), on which \(v_i\ne0\) precisely for \(i\in U\). If \(\{i,j\}\) is an edge in \(G[U]\), then \([v_j]=\iota([v_i])\). In a connected component, a chosen root line propagates uniquely along walks. If the component is bipartite, all walks from the root to any vertex have the same parity and every root line in \(\mathbb P(W)\) is allowed; the vertices in the two color classes use the root line and its perpendicular. If the component is nonbipartite, an odd closed walk forces the root line to be fixed by \(\iota\), so it lies in \(S_B\); conversely any isotropic line works and all vector lines in that component coincide. These arguments remain valid for isolated vertices, which contribute one free line in \(\mathbb P(W)\).

**Step 3: Class of a support stratum.** The projective line assignments for \(G[U]\) form

\[
Y_U\cong(\mathbb P^1_k)^{b(U)}\times_k S_B^{c(U)}.
\]

Over this base, for each \(i\in U\), the permitted nonzero vector is a nonzero point of the corresponding tautological line subbundle of the trivial rank-two bundle. Therefore \(X_U\to Y_U\) is a Zariski-locally-trivial \((\mathbb G_m)^{|U|}\)-bundle (a product of punctured line bundles), so

\[
[X_U]=(\mathbb L-1)^{|U|}(\mathbb L+1)^{b(U)}[S_B]^{c(U)}.
\]

Summing all disjoint support strata proves the motivic equality.

**Step 4: Quadratic étale reduction.** A degree-two finite étale scheme has a canonical two-sheeted Galois action; its fibre square satisfies \(S_B\times_k S_B\cong S_B\sqcup S_B\). Consequently \([S_B]^2=2[S_B]\), and \(\eta_B^2=([S_B]-1)^2=1\). Substituting \([S_B]=1+\eta_B\) into the state sum produces the unique remainder \(A_G(\mathbb L)+\eta_B C_G(\mathbb L)\).

**Step 5: Arithmetic and zeta.** For \(B\) over \(\mathbb F_q\), the two geometric isotropic lines are individually Frobenius-fixed in the split case \(\epsilon=1\), and Frobenius interchanges them in the nonsplit case \(\epsilon=-1\). Thus \(\#S_B(\mathbb F_{q^r})=1+\epsilon^r\). Counting each support stratum gives the displayed formula. The equality \(\log Z=\sum_{r\ge1}\#X(\mathbb F_{q^r})z^r/r\) and the identity \(-\log(1-\lambda z)=\sum_{r\ge1}\lambda^r z^r/r\) give the zeta product coefficient by coefficient. Terms of degree greater than \(2n\) cannot occur because \(|U|+b(U)\le2n\).

**Step 6: Complete-graph specialization.** For \(G=K_h\), induced subgraphs on zero, one, and two vertices are bipartite; on three or more vertices they are connected and nonbipartite. Accordingly the state sum is

\[
1+h(\mathbb L^2-1)+\binom h2(\mathbb L^2-1)(\mathbb L-1)
+[S_B]\sum_{t=3}^h\binom ht(\mathbb L-1)^t.
\]

The binomial identity for \(\sum_{t=3}^h\binom ht(T-1)^t\) gives \(A_h(T),C_h(T)\) above. When \(h\ge4\), the leading \(q^h\) terms add in the split case and cancel in the nonsplit case. The nonsplit formula has leading term \(\binom h2q^3\); no higher power survives because the remaining terms arise from support sizes at most two. This completes the proof.

## Verification

The companion Python script `verify_graph_frames.py` enumerates every vector assignment over prime fields of cardinality \(3,5,7\) for a selection of 57 labeled graphs with at most four vertices, and verifies the state sum by independent graph-component calculations. It also checks the complete-graph polynomial specialization for 380 choices of parameters and splitting signs. The extracted script reports `DIRECT_LABELED_GRAPH_ENUMERATIONS_OK 57` and `COMPLETE_GRAPH_SPECIALIZATION_OK 380`. These are reproducibility checks of finite cases, not a substitute for the all-graph, all-field proof.

## Relationship to prior work

Xie's 2026 study of off-diagonal Gram maps motivates exact analysis of the zero fibres and their arithmetic. Herzog–Macchia–Saeedi Madani–Welker (2014) previously established radicality and prime decompositions of binary orthogonal-representation ideals for arbitrary graphs; these results are **not** claimed as new. Hoang–Kahle (2020) gave Hilbert–Poincaré series and related homological invariants for complete-graph parity binomial edge ideals. Casabella–Sammartano (2025) described irreducible components of more general orthogonal-frame varieties. The present claim is the quadratic-étale **motivic state sum for every graph** and the split/nonsplit **point-count and zeta formulas**; a component classification or Hilbert series alone is not such an arithmetic formula. Relevant publications have been inspected for direct coverage, but historical priority is not certified.

## Limitations

The equality concerns reduced varieties and nondegenerate binary symmetric forms over fields of characteristic not two. It does not count solutions to nonzero Gram targets, higher-dimensional quadratic spaces, nilpotent jets, or integral points over finite local rings. The identity does not resolve full scheme-theoretic singularities or arbitrary graph-primary-decomposition questions. The formula is derived by elementary support stratification; an equivalent historical statement under alternative graph-polynomial terminology remains an originality risk. Independent mathematical validation has not been performed.

## References

- Y. Xie, *Sharp FRS and singularity thresholds for off-diagonal Gram maps*, arXiv:2610.02585v1 (first posted 2026-10-01), https://arxiv.org/html/2610.02585v1.
- J. Herzog, A. Macchia, S. Saeedi Madani, V. Welker, *On the ideal of orthogonal representations of a graph in R2*, arXiv:1411.3674v1 (2014), https://arxiv.org/pdf/1411.3674.
- D. T. Hoang and T. Kahle, *Hilbert–Poincaré series of parity binomial edge ideals and permanental ideals of complete graphs*, Collectanea Mathematica (online 2020), https://doi.org/10.1007/s13348-020-00294-2.
- L. Casabella and A. Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058v1 (first posted 2025-12-31), https://arxiv.org/pdf/2512.25058.
