# Exact graph-ball residuals for GMRES on radially weighted grounded trees

## Finding
Let \(T\) be a finite rooted tree of height \(H\ge1\), with a positive integer \(b_j\) of children at every level-\(j\) vertex, for \(0\le j<H\). Give each edge between levels \(j\) and \(j+1\) an arbitrary common positive conductance \(w_j\). Ground every leaf with a common positive killing conductance \(\kappa\). Let \(A=L_w+\kappa\operatorname{diag}(\mathbf1_{S_H})\), where \(S_j\) denotes the vertices at distance \(j\) from the root. Starting unrestarted Euclidean GMRES at \(x_0=0\) for \(Ax=e_{\mathrm{root}}\), its exact residual vectors are
\[
r_k=\frac{1}{B_k}\mathbf1_{S_0\cup\cdots\cup S_k},\qquad
\|r_k\|_2^2=\frac1{B_k},\qquad
B_k=\sum_{j=0}^k\prod_{i=0}^{j-1}b_i,\qquad 0\le k\le H,
\]
where the empty product equals one. The next iteration is exact: \(r_{H+1}=0\); none of the preceding residuals vanishes. Thus the entire nonterminal GMRES residual curve, and indeed every nonterminal residual vector, is **independent of all edge conductances and the positive grounding conductance**. Its squared norm is exactly the reciprocal of the number of vertices in the corresponding rooted ball.

As a regular-tree specialization, for \(d\ge3\), \(b_0=d\) and \(b_j=d-1\) for \(1\le j<H\) give
\[
\|r_k\|_2^2=\left(1+d\frac{(d-1)^k-1}{d-2}\right)^{-1},\qquad 0\le k\le H.
\]
For \(d=2\) the same specialization gives \(\|r_k\|_2^2=(2k+1)^{-1}\). Hence branching produces exponential rather than algebraic preterminal decay. For any fixed tree and layer weights, letting \(\kappa\downarrow0\) makes the condition number of \(A\) diverge, while this entire finite residual history remains exactly unchanged.

## Assumptions and scope
The tree includes exactly the vertex levels \(S_0,\ldots,S_H\), with \(S_0\) consisting of the root and \(|S_j|=\prod_{i=0}^{j-1}b_i\). All \(b_i\) are positive integers; all \(w_i\) and \(\kappa\) are positive real numbers. The weighted combinatorial Laplacian acts by \((L_w f)(v)=\sum_{u\sim v}w_{uv}(f(v)-f(u))\), and only leaves receive the additional diagonal killing. Thus \(A\) is symmetric positive definite: its quadratic form is \(\sum_{\{u,v\}}w_{uv}(x_u-x_v)^2+\kappa\sum_{v\in S_H}x_v^2>0\) for each nonzero \(x\). GMRES means exact arithmetic, no restart, no preconditioner, and Euclidean residual minimization over \(\mathcal K_k(A,e_{\mathrm{root}})\).

The statement is about residuals, not relative solution error. The positive grounding hypothesis ensures invertibility and exact termination at iteration \(H+1\). The layer-homogeneity hypotheses are essential for the radial Krylov-space argument; no claim is made for arbitrary weighted trees without level symmetry.

## Proof
**1. Radial Krylov characterization.** Write \(s_j=\mathbf1_{S_j}\), and let \(\mathcal R_j=\operatorname{span}\{s_0,\dots,s_j\}\). The operator \(A\) maps level-constant vectors to level-constant vectors, because both branching and weights depend only on level and the leaf killing is uniform. Moreover, \(As_j\) belongs to \(\mathcal R_{j+1}\), and for \(j<H\) its coefficient on \(s_{j+1}\) is \(-w_j\ne0\). By induction the vectors \(e_{\mathrm{root}},Ae_{\mathrm{root}},\ldots,A^{k-1}e_{\mathrm{root}}\) are triangular with nonzero newly reached shell coefficients. Therefore
\[
\mathcal K_k(A,e_{\mathrm{root}})=\mathcal R_{k-1},\qquad 1\le k\le H+1.
\]
In particular, \(A\mathcal K_k\subseteq\mathcal R_k\). Since \(A\) is injective, this image has dimension \(k\).

**2. The unique orthogonal residual direction.** For \(0\le k\le H\), put \(u_k=s_0+\cdots+s_k\), the indicator of the rooted ball. Its weighted Laplacian is zero at every vertex in levels \(0,\ldots,k-1\), since it is locally constant there. The same is true for the killing term, since all killed vertices lie in \(S_H\). Thus \(Au_k\perp\mathcal R_{k-1}\). By symmetry, \(u_k\perp A\mathcal K_k\). For \(k\ge1\), the orthogonal complement of the \(k\)-dimensional subspace \(A\mathcal K_k\) within the \((k+1)\)-dimensional \(\mathcal R_k\) is therefore exactly \(\operatorname{span}\{u_k\}\). The right-hand side \(e_{\mathrm{root}}\) belongs to \(\mathcal R_k\), so its minimum-residual projection is
\[
r_k=\frac{\langle e_{\mathrm{root}},u_k\rangle}{\langle u_k,u_k\rangle}u_k=\frac{1}{B_k}u_k.
\]
For \(k=0\), the same identity is simply the initial residual \(e_{\mathrm{root}}\). Taking squared norms gives \(\|r_k\|_2^2=1/B_k\) and proves strict nontermination through \(k=H\).

**3. Termination and geometric rates.** For \(k=H+1\), the Krylov space equals the full radial space \(\mathcal R_H\); invertibility and invariance imply \(e_{\mathrm{root}}\in A\mathcal R_H\), so the residual is zero. The shell count for the stated regular trees is \(|S_0|=1\) and \(|S_j|=d(d-1)^{j-1}\) for \(j\ge1\). Summing the geometric series yields the displayed formulas, including the \(d=2\) limit.

**4. Arbitrarily bad conditioning with identical residual history.** Fix the tree and weights, vary only \(\kappa>0\), and write \(N=|T|\). The unit constant vector in the Rayleigh quotient gives \(\lambda_{\min}(A)\le\kappa |S_H|/N\), while a root-coordinate Rayleigh quotient gives \(\lambda_{\max}(A)\ge b_0w_0>0\). Thus
\[
\operatorname{cond}_2(A)\ge \frac{Nb_0w_0}{\kappa |S_H|}\longrightarrow\infty
\]
as \(\kappa\downarrow0\). Nevertheless every \(r_k\) for \(k\le H\) is independent of \(\kappa\), as established above.

## Verification
The standalone standard-library Python script `verify.py` constructs the actual full grounded matrices for varying branching patterns and positive layer weights, computes the GMRES residuals from exact rational Krylov Gram projections, and compares the entire vectors against the ball-indicator formula. It also checks exact termination and the regular-tree shell-count identities. Running `python3 verify.py` passed 10,602 exact rational/integer assertions across 879 weighted grounded trees. These finite checks test implementation and boundaries; the proof establishes all allowed heights, branching counts and positive real weights.

## Relationship to prior work
Saad and Schultz introduced GMRES and its residual-minimization characterization (1986). Titley-Peloquin, Pestana and Wathen (first online publication July 25, 2013) developed right-hand-side-sensitive GMRES bounds and a spectral weighted least-squares representation. Li and Zhang's 2007 technical report, subsequently published in 2009, treats tridiagonal Toeplitz systems including canonical endpoint data and exact residual expressions. These are general or one-dimensional precedents; the present result determines a full graph-ball residual vector on radially weighted, arbitrarily branching grounded trees and identifies its conductance independence. The published work titled *Exact GMRES boundary-layer profiles for discrete-affine Poisson data* classifies harmonic boundary forcing on one-dimensional Dirichlet paths, not localized root forcing on trees. Another published analysis, *Sharp endpoint growth and depth profile of Green operators on complete branching trees*, concerns norms of a centered graph pseudoinverse, not finite GMRES residuals. Closely related special cases could conceivably be implicit in other Jacobi, Lanczos or MINRES literature; publication priority remains provisional.

## Limitations
The universality holds in exact arithmetic only and makes no claim about finite-precision attainable residuals, preconditioning, restarts, nonsymmetric operators, off-root forcing or arbitrary nonradial weights. It does not assert that the solution error is independent of conditioning. The theorem is mathematically self-contained, but independent validation and a complete historical literature census have not been performed.

## References
1. Y. Saad and M. H. Schultz, *GMRES: A Generalized Minimal Residual Algorithm for Solving Nonsymmetric Linear Systems*, SIAM Journal on Scientific and Statistical Computing 7 (1986), 856–869, https://doi.org/10.1137/0907058.
2. D. Titley-Peloquin, J. Pestana and A. J. Wathen, *GMRES convergence bounds that depend on the right-hand-side vector*, first online publication July 25, 2013, https://doi.org/10.1093/imanum/drt025. Accepted manuscript: https://ora.ox.ac.uk/objects/uuid%3A682cdddf-e26c-4540-bb82-37ab23d09648.
3. R.-C. Li and W. Zhang, *The Rate of Convergence of GMRES on a Tridiagonal Toeplitz Linear System*, technical report 2007-12 (February 2007), https://cdn.prod.web.uta.edu/-/media/project/website/science/mathematics/documents/preprint/2007/rep2007_12.pdf.
4. *Exact GMRES boundary-layer profiles for discrete-affine Poisson data*, published research report (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-gmres-boundary-layer-profiles-for-discrete-affine-poisson--1e34f70ca04d.
5. *Sharp endpoint growth and depth profile of Green operators on complete branching trees*, published research report (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-endpoint-growth-and-depth-profile-of-green-operators-on-co--0277c139a872.
