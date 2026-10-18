# The Eq. (18) partial-scaling optimization is exactly maximum bipartition negativity

## Finding

For every finite-dimensional multipartite state \(\rho\), the trace-norm optimization over the tensor-product partial-scaling maps \(T_{\lambda}=\frac{1+\lambda}{2}I+\frac{1-\lambda}{2}T\) of Lupo–Man’ko–Marmo–Sudarshan, with \(\lambda\in[-1,1]\) on any chosen set of parties, is attained at a cube vertex and equals \(2\max_S \mathcal N_S(\rho)\), where \(S\) ranges over the corresponding partial-transpose subsets. If scaling is applied to all but one party, this is exactly twice the largest ordinary bipartition negativity. Consequently every partially scaled operator is positive whenever all corresponding subset partial transposes are positive, so the continuous scaling parameters add no detection power beyond those ordinary PPT tests.

Equivalently, let \(K\) be the set of parties on which the scaling maps are applied and define
\[
\Phi_{\boldsymbol\lambda}=\bigotimes_{j\in K}T_{\lambda_j}^{(j)}\otimes I_{K^c},
\qquad
m_\rho(\boldsymbol\lambda)=\|\Phi_{\boldsymbol\lambda}(\rho)\|_1-1.
\]
Then
\[
\max_{\boldsymbol\lambda\in[-1,1]^K}m_\rho(\boldsymbol\lambda)
=
\max_{S\subseteq K}\left(\|\rho^{\Gamma_S}\|_1-1\right)
=
2\max_{S\subseteq K}\mathcal N_S(\rho).
\]
Every maximum is attained at at least one cube vertex \(\lambda_j\in\{-1,1\}\). For a system of \(n\) parties with scaling on \(n-1\) parties, the subsets \(S\) represent all unordered bipartitions up to complementation, so the right-hand side is twice the largest bipartition negativity.

## Assumptions and scope

The statement concerns exactly the one-parameter scaling map defined in Eq. (18) of Lupo–Man’ko–Marmo–Sudarshan,
\[
T_\lambda=\frac{1+\lambda}2I+\frac{1-\lambda}2T,
\qquad -1\le\lambda\le1,
\]
and tensor products of this map on disjoint finite-dimensional subsystems. Here \(T\) denotes matrix transposition in the chosen local basis, \(\Gamma_S\) denotes partial transposition on the parties in \(S\), and
\[
\mathcal N_S(\rho)=\frac{\|\rho^{\Gamma_S}\|_1-1}2
\]
is the usual negativity across that bipartition.

No claim is made about the larger anisotropic positive-map families proposed in the source's outlook, or about arbitrary positive maps. The theorem concerns detection and the source-style trace-norm optimization for the Eq. (18) family; it does not claim that positivity under all partial transposes is sufficient for separability in dimensions where PPT entanglement exists.

## Proof

For each \(j\in K\), put
\[
a_j=\frac{1+\lambda_j}2,
\qquad
b_j=\frac{1-\lambda_j}2.
\]
Because \(\lambda_j\in[-1,1]\), one has \(a_j,b_j\ge0\) and \(a_j+b_j=1\). Tensor-product distributivity gives the exact operator identity
\[
\Phi_{\boldsymbol\lambda}(\rho)
=
\sum_{S\subseteq K}w_S(\boldsymbol\lambda)\,\rho^{\Gamma_S},
\]
where
\[
w_S(\boldsymbol\lambda)
=
\prod_{j\in S}b_j
\prod_{j\in K\setminus S}a_j.
\]
Every coefficient is nonnegative and
\[
\sum_{S\subseteq K}w_S
=
\prod_{j\in K}(a_j+b_j)=1.
\]
Thus every partially scaled operator is a convex combination of subset partial transposes.

The trace norm is convex, so
\[
\|\Phi_{\boldsymbol\lambda}(\rho)\|_1
\le
\sum_{S\subseteq K}w_S\|\rho^{\Gamma_S}\|_1
\le
\max_{S\subseteq K}\|\rho^{\Gamma_S}\|_1.
\]
Each map is trace preserving, hence every operator in this display has trace \(1\). Subtracting \(1\) gives
\[
m_\rho(\boldsymbol\lambda)
\le
\max_{S\subseteq K}\left(\|\rho^{\Gamma_S}\|_1-1\right).
\]
For any fixed subset \(S\), choose the cube vertex
\[
\lambda_j=
\begin{cases}
-1,&j\in S,\\
1,&j\notin S.
\end{cases}
\]
Then \(b_j=1\) on \(S\), \(a_j=1\) off \(S\), all other weights vanish, and
\[
\Phi_{\boldsymbol\lambda}(\rho)=\rho^{\Gamma_S}.
\]
Therefore the upper bound is attained, proving the equality and the vertex-maximization statement.

For detection, if every \(\rho^{\Gamma_S}\) is positive semidefinite, then every convex combination above is positive semidefinite. The contrapositive says that a nonpositive partially scaled operator can occur only if at least one corresponding partial transpose is already nonpositive. Conversely, such a partial transpose is itself one of the cube vertices.

Finally, transposing all parties maps \(\rho^{\Gamma_S}\) to \(\rho^{\Gamma_{S^c}}\), and ordinary transposition preserves singular values. Hence
\[
\|\rho^{\Gamma_S}\|_1=\|\rho^{\Gamma_{S^c}}\|_1.
\]
When scaling is applied to all but one designated party, the subsets of the scaled parties therefore give one representative of every unordered bipartition, which proves the last assertion.

## Verification

The proof is purely algebraic and has no numerical or asymptotic step. Its critical checks are: the Eq. (18) coefficients are nonnegative exactly on \([-1,1]\); tensor expansion produces weights summing exactly to \(1\); trace-norm convexity supplies the upper bound; every subset partial transpose occurs at a cube vertex; and complementation changes a partial transpose only by a full transpose, which preserves trace norm.

For the three-party map used by the source,
\[
I\otimes T_\lambda\otimes T_\mu,
\]
the expansion is explicitly
\[
a_\lambda a_\mu\rho
+b_\lambda a_\mu\rho^{\Gamma_2}
+a_\lambda b_\mu\rho^{\Gamma_3}
+b_\lambda b_\mu\rho^{\Gamma_{2,3}}.
\]
The four vertices are therefore the state itself and the three bipartition partial transposes, because \(\Gamma_{2,3}\) has the same trace norm as \(\Gamma_1\). This directly recovers, and generalizes beyond the source's examples, its observed endpoint maxima.

## Relationship to prior work

Lupo, Man’ko, Marmo, and Sudarshan define \(T_\lambda\) and explicitly observe in Eq. (18) that a single scaling map is a convex combination of identity and transposition. They consequently note that a single scaling map cannot detect PPT bound entanglement. In the multipartite section, however, they study \(I\otimes T_\lambda\otimes T_\mu\), use two-dimensional parameter phase diagrams, interpret generic parameter points as multipartite witnesses, and define a maximum over the continuous parameters. For their symmetric examples they find the maximum at partial-transpose vertices, while nonsymmetric examples are treated numerically.

The present statement proves that the vertex behavior is not an example-specific accident: for every state, every finite local dimension, and any number of Eq. (18) scaling factors, the full parameter cube is the convex hull of the subset partial transposes. Thus the source-style trace-norm optimization always collapses exactly to the finite maximum of ordinary negativities, and interior parameters never add detection power.

Vidal and Werner define the standard negativity by \(\mathcal N=(\|\rho^{T_A}\|_1-1)/2\) and prove its convexity. Their work supplies the standard interpretation of the vertex values but does not discuss the partial-scaling family or the collapse of its multipartite parameter optimization.

Targeted searches using the source title, the map formula, partial-scaling aliases, vertex maximization, convex-hull language, and the exact implication to maximum bipartition negativity did not locate a publication stating this general collapse. The closest source is the defining paper itself, whose Eq. (18) is one ingredient of the proof and whose example-specific endpoint maxima are subsumed by the theorem.

## Limitations

The result does not improve the PPT criterion and deliberately explains why the Eq. (18) partial-scaling family cannot do so. It does not address the source's later proposed anisotropic maps, indecomposable positive maps, PPT-entangled states detectable by other criteria, or whether the maximum of bipartition negativities has any preferred multipartite monotonicity property.

The originality assessment is literature-search based rather than a theorem of uniqueness. A poorly indexed note could have observed the same tensor-product convex-hull reduction. The strongest residual overlap risk is therefore a short later remark deriving the same vertex-collapse identity from Eq. (18).

## References

1. C. Lupo, V. I. Man’ko, G. Marmo, E. C. G. Sudarshan, “Partial scaling transform of multiqubit states as a criterion of separability,” arXiv:quant-ph/0509006, DOI:10.1088/0305-4470/38/48/009. First public 2005-09-01.
2. G. Vidal, R. F. Werner, “A computable measure of entanglement,” arXiv:quant-ph/0102117, DOI:10.1103/PhysRevA.65.032314. First public 2001-02-22.
