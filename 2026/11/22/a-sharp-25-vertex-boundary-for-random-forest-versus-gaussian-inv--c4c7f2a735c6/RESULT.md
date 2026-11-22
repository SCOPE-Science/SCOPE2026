# A sharp 25-vertex boundary for random-forest versus Gaussian inverse-trace variance

## Finding

Let \(G\) be any connected undirected graph with \(n\ge2\) vertices, strictly positive edge conductances, and weighted Laplacian \(L\). For every \(q>0\), the matrix \(K_q=q(qI+L)^{-1}\) has trace estimated without bias either by (i) the number \(R_q\) of roots of a \(q\)-weighted random rooted spanning forest, or (ii) the Gaussian quadratic form \(H_q=g^{\mathsf T}K_qg\) with \(g\sim N(0,I_n)\). Write \(V_F=\operatorname{Var}(R_q)\) and \(V_G=\operatorname{Var}(H_q)\).

If \(0=\lambda_1<\lambda_2\le\cdots\le\lambda_n\) are the eigenvalues of \(L\), then the **exact spectral gap certificate** is

\[
\boxed{V_G-V_F=\frac{25-n}{12}+\frac1{12}\sum_{j=2}^{n}\left(\frac{\lambda_j-5q}{\lambda_j+q}\right)^2.}
\]

Consequently the largest possible *forest-variance excess*, over all connected positively weighted graphs on \(n\) labeled vertices and all positive \(q\), is exactly

\[
\boxed{\sup_{G,q}\bigl(V_F-V_G\bigr)=\frac{n-25}{12}.}
\]

For any fixed \(q>0\), equality is attained **only** by the complete graph with uniform conductance \(5q/n\) on every edge. Thus, for \(2\le n\le24\), the forest root count has strictly smaller single-sample variance than Gaussian quadratic-form probing for every connected weighted graph and every \(q>0\). At \(n=25\), forest variance is never larger, and equality occurs exactly at the stated complete-graph weighting. At every \(n\ge26\), a nonempty open set of positive graph conductances and positive \(q\) makes the Gaussian probe strictly lower variance than the forest root count.

More precisely, on a uniform complete graph of order \(n\ge26\) whose nonzero Laplacian eigenvalue is \(\lambda=nw\), put \(x=\lambda/q\) and

\[
x_{\pm}=\frac{n-5\pm\sqrt{(n-1)(n-25)}}4.
\]

Then \(V_F>V_G\) exactly when \(x_-<x<x_+\); equality holds at the endpoints, and \(V_F<V_G\) outside that interval. At \(n=26\), \(q=1\) and \(w=5/26\), the excess is exactly \(1/12\).

## Assumptions and scope

The graph is finite, connected, undirected, and has real positive weights. Every forest is a spanning acyclic edge set with one marked root in each component. Its probability is proportional to \(q^{r}\) times the product of the edge conductances, where \(r\) is its number of roots. Gaussian probing uses one vector with independent standard normal coordinates and an exact matrix solve; the comparison is between the variances of **one draw from each method**, not between computational costs, time-to-accuracy, or a variance-reduced forest estimator. The zero eigenvalue has multiplicity one because the graph is connected. All conclusions concern variance, not concentration tails or distributional dominance.

## Proof

**Forest variance.** The rooted matrix-forest identity yields \(Z(q)=\det(qI+L)\) for the forest partition function. Differentiation of the generating function gives

\[
\mathbb E R_q=q\frac{d}{dq}\log Z(q)
=\sum_{j=1}^{n}\frac{q}{\lambda_j+q},
\qquad
V_F=q\frac{d}{dq}\mathbb E R_q
=\sum_{j=1}^{n}\frac{q\lambda_j}{(\lambda_j+q)^2}.
\]

The zero mode contributes \(1\) to the mean and \(0\) to the variance.

**Gaussian variance.** Orthogonally diagonalize \(K_q\). Since the squares of independent standard normals have variance \(2\),

\[
\mathbb E H_q=\operatorname{tr}K_q
=\mathbb E R_q,
\qquad
V_G=2\operatorname{tr}(K_q^2)
=2\sum_{j=1}^{n}\frac{q^2}{(\lambda_j+q)^2}.
\]

Its zero mode contributes exactly \(2\) to \(V_G\). Subtracting the two variance formulas and using the exact scalar identity, valid for each \(\lambda\ge0\),

\[
\frac{q(2q-\lambda)}{(\lambda+q)^2}
=\frac{(\lambda-5q)^2}{12(\lambda+q)^2}-\frac1{12},
\]

proves the displayed spectral certificate and sharp upper bound on \(V_F-V_G\).

**Equality and graph structure.** Equality in the bound requires \(\lambda_2=\cdots=\lambda_n=5q\). Because a connected Laplacian's nullspace is the span of the all-ones vector, its spectral resolution then forces \(L=5q(I-\mathbf{1}\mathbf{1}^{\mathsf T}/n)\). The off-diagonal entries are all \(-5q/n\), hence the graph must be the equally weighted complete graph. Conversely this graph has precisely that spectrum. The upper bound is therefore attained and the vertex threshold follows.

**Complete-graph crossover window.** For the complete graph with edge weight \(w\), the eigenvalues are \(0\) and \(nw\), the latter repeated \(n-1\) times. Substitution gives

\[
V_F-V_G=\frac{(n-1)(x-2)-2(x+1)^2}{(x+1)^2}
=\frac{-2x^2+(n-5)x-2n}{(x+1)^2}.
\]

Its numerator has discriminant \((n-1)(n-25)\). For \(n\ge26\), both roots \(x_-\) and \(x_+\) are positive, and the concave quadratic is positive exactly between them. At \(x=5\) it yields the global maximum \((n-25)/12\). Continuity of the inverse and of both variance formulas in the graph weights and \(q\) makes the strict advantage stable under sufficiently small positive perturbations of the complete-graph conductances.

## Verification

The included `verify.py` performs independent rational-arithmetic calculations of the gap for complete graphs and of the spectral decomposition for several additional exact spectra. It verifies the scalar square certificate, the sharp \(n=24,25,26\) boundary cases, explicit finite complete-graph windows, complete-graph binomial root counts, and direct rooted-forest enumeration on several small weighted trees. These finite calculations supplement, but do not replace, the analytic argument for arbitrary graph size and positive weights. Run `python3 verify.py` using the standard Python library.

## Relationship to prior work

Barthelmé, Tremblay, Gaudillière, Avena and Amblard (2019) introduce the random-forest root estimator, write its general spectral variance and compare it with Gaussian Girard probing. These known identities are the starting point here. The contribution claimed is their *sharp all-graphs extremal variance-gap optimization*, the exact 25-to-26-vertex threshold and the equality/crossover classification, not the estimators, the spectral variance identities, or the scalar Gaussian fourth moment. Pilavcı, Amblard, Barthelmé and Tremblay (2022) study control variates, stratification and empirical runtime comparisons, not this exact minimax threshold. The derivation is short because a general variance formula is already available; this is a priority risk, and independent mathematical and literature verification has not been performed.

## Limitations

A smaller per-sample variance need not mean less computation, as forest generation and Gaussian linear solves have different costs. This theorem does not compare Rademacher-sign probes, normalized or deflated Gaussian probes, variance-reduced forests, multiple correlated samples, or run-time efficiency. The graph restriction is essential to the rooted-forest interpretation, although the algebraic spectral certificate applies to any positive-semidefinite matrix with one zero eigenvalue. A corresponding theorem or equivalent extremal inequality could be present in literature not found in the search; no independent audit is claimed.

## References

1. S. Barthelmé, N. Tremblay, A. Gaudillière, L. Avena, and P.-O. Amblard, *Estimating the inverse trace using random forests on graphs*, first publicly posted May 6, 2019, arXiv:1905.02086. https://arxiv.org/abs/1905.02086 ; conference full text https://www.gretsi.fr/data/colloque/pdf/2019_tremblay412.pdf .
2. Y. Y. Pilavcı, P.-O. Amblard, S. Barthelmé, and N. Tremblay, *Variance Reduction for Inverse Trace Estimation via Random Spanning Forests*, first publicly posted June 15, 2022, arXiv:2206.07421. https://arxiv.org/abs/2206.07421 ; conference full text https://gretsi.fr/data/colloque/pdf/2022_pilavci804.pdf .
3. M. F. Hutchinson, *A stochastic estimator of the trace of the influence matrix for Laplacian smoothing splines*, Communications in Statistics—Simulation and Computation (1989). Referenced for the classical probing construction, not for the extremal threshold.
