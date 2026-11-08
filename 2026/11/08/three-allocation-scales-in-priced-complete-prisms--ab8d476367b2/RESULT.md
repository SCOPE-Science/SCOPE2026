# Three allocation scales in priced complete prisms

## Finding

Let \(n\ge4\), \(B>0\), and \(c>0\). Take two copies of the complete graph \(K_n\), join corresponding vertices by a perfect matching, price each within-clique edge at one unit per unit conductance, and price each matching edge at \(c\) units. Permit every edge to have its own nonnegative conductance, with total expenditure at most \(B\). Minimize the Kirchhoff index \(\mathcal K=\sum_{i<j}R_{ij}\), the sum of all pairwise effective resistances.

**Theorem.** The global minimizer exists, uses the full budget, and is unique. Every within-clique edge has the same strictly positive conductance \(a_n\), and every matching edge has the same strictly positive conductance \(b_n\). Put \(r_n=b_n/a_n\) and
\[
F_{n,c}(r)=(n-1+cr)\left(\frac{n-1}{n}+\frac{1}{2r}+\frac{n-1}{n+2r}\right).
\]
Then \(r_n\) is the unique positive root of
\[
c\left(\frac{n-1}{n}+\frac{1}{2r}+\frac{n-1}{n+2r}\right)
=(n-1+cr)\left(\frac1{2r^2}+\frac{2(n-1)}{(n+2r)^2}\right).
\]
The optimal conductances and minimum Kirchhoff index are exactly
\[
a_n=\frac{B}{n(n-1+cr_n)},\qquad b_n=r_na_n,\qquad
\mathcal K_{\min}=\frac{2n^2}{B}F_{n,c}(r_n).
\]
For each **fixed** price \(c\), the optimal ratio has the following three distinct large-network regimes:
\[
\boxed{\begin{aligned}
0<c<1:&\quad \frac{r_n}{n}\longrightarrow \frac{\sqrt{2/c-1}-1}{2},\\
c=1:&\quad \frac{r_n}{n^{2/3}}\longrightarrow \frac12,\\
c>1:&\quad \frac{r_n}{\sqrt n}\longrightarrow \frac{1}{2\sqrt{c-1}}.
\end{aligned}}
\]
The optimal fraction of total expenditure allocated to the inter-clique matching is \(\theta_n=cr_n/(n-1+cr_n)\); hence
\[
\boxed{\begin{aligned}
0<c<1:&\quad \theta_n\longrightarrow \frac{c\alpha(c)}{1+c\alpha(c)},\quad
\alpha(c)=\frac{\sqrt{2/c-1}-1}{2},\\
c=1:&\quad n^{1/3}\theta_n\longrightarrow \frac12,\\
c>1:&\quad \sqrt n\,\theta_n\longrightarrow \frac{c}{2\sqrt{c-1}}.
\end{aligned}}
\]
In particular, each finite optimum funds *all* interlayer links even though their optimal budget share vanishes at the two displayed rates for prices at or above one.

## Assumptions and scope

The graph has vertex set \(\{1,\ldots,n\}\times\{0,1\}\). Within each layer, every distinct pair is adjacent; the only between-layer edges are \((i,0)\)--\((i,1)\). Edge conductances are nonnegative real numbers, and disconnected allocations have infinite pairwise-resistance objective. There are \(n(n-1)\) within-layer edges in total and \(n\) between-layer edges. All quantifiers in the theorem are over the unrestricted individual-edge feasible set, not only over two-class symmetric allocations. The asymptotics hold for fixed \(c\) and fixed \(B\), with \(n\to\infty\); no uniform assertion is made when the price changes with \(n\).

## Proof

**1. Existence, uniqueness, and global symmetry.** Write \(N=2n\), let \(L(w)\) be the weighted Laplacian, and let \(J\) denote the all-ones \(N\)-by-\(N\) matrix. For connected conductance allocations, set \(M=L(w)+J/N\), which is positive definite. The resistance identity gives
\[
\mathcal K(w)=N\bigl(\operatorname{tr}M^{-1}-1\bigr).
\]
If \(\Delta L\ne0\) is the Laplacian variation induced by any nonzero individual-edge variation, then the second directional derivative is
\[
2N\operatorname{tr}(M^{-1}\Delta L M^{-1}\Delta L M^{-1})>0.
\]
Indeed, conjugate the middle factor with \(M^{-1/2}\); the expression is the trace of a nonzero positive-semidefinite square against a positive-definite matrix. The edge-to-Laplacian map is injective, since each individual edge is determined by its off-diagonal entry. Thus the objective is strictly convex on the connected feasible region. By compactness of the budget simplex, and divergence of effective resistance on any sequence approaching a disconnected configuration, a minimizer exists and is connected. Scaling all conductances up strictly lowers resistance, so the full budget is used. Strict convexity implies uniqueness.

Simultaneous permutations of corresponding vertices, together with interchange of the two layers, preserve both objective and costs. Uniqueness therefore forces common conductance \(a\) on every within-layer edge and common conductance \(b\) on every matching edge. Since removing either entire edge orbit disconnects the graph, both are strictly positive.

**2. Exact spectral reduction.** For orbitwise conductances the Laplacian is
\[
L=aL(K_n)\otimes I_2+bI_n\otimes L(K_2).
\]
Because the factor Laplacians commute in the tensor representation, the spectrum consists of \(0\) once, \(2b\) once, \(na\) with multiplicity \(n-1\), and \(na+2b\) with multiplicity \(n-1\). Kirchhoff's spectral identity now yields
\[
\mathcal K=2n\left(\frac1{2b}+\frac{n-1}{na}+\frac{n-1}{na+2b}\right).
\]
The exact budget is \(n(n-1)a+ncb=B\). Substituting \(r=b/a>0\) gives the \(a_n,b_n\) expressions and \(\mathcal K=(2n^2/B)F_{n,c}(r)\). Differentiation gives the displayed root equation. Both extremes \(r\downarrow0\) and \(r\to\infty\) make \(F\) diverge. The budget line parameterized by \(a=B/[n(n-1+cr)]\) is a bijection of an open interval with \(r>0\), and strict convexity of the original objective restricted to this affine budget line implies a single stationary point. Hence this is the unique positive root and the global minimizer.

**3. Three asymptotic scales.** Differentiating explicitly gives
\[
F'_{n,c}(r)=c\left(\frac{n-1}{n}+\frac1{2r}+\frac{n-1}{n+2r}\right)
-(n-1+cr)\left(\frac1{2r^2}+\frac{2(n-1)}{(n+2r)^2}\right).
\]
When \(0<c<1\), for every fixed \(t>0\), direct division by powers of \(n\) shows
\[
F'_{n,c}(nt)\longrightarrow
\frac{2(2ct^2+2ct+c-1)}{(1+2t)^2}.
\]
The numerator has precisely one positive root, \(\alpha(c)=(\sqrt{2/c-1}-1)/2\), with a negative sign below and positive above it.

At \(c=1\), cancellation of the leading terms and expansion of the rational factors, again for fixed \(t>0\), gives
\[
n^{1/3}F'_{n,1}(t n^{2/3})\longrightarrow 4t-\frac1{2t^2},
\]
which changes sign only at \(t=1/2\).

At \(c>1\), the corresponding fixed-\(t\) limit is
\[
F'_{n,c}(t\sqrt n)\longrightarrow 2(c-1)-\frac1{2t^2},
\]
whose unique positive zero is \(t=1/[2\sqrt{c-1}]\). In each case, for arbitrary fixed \(t_-\) below and \(t_+\) above the limiting zero, these limits ensure \(F'<0\) at the lower trial point and \(F'>0\) at the upper trial point for all sufficiently large \(n\). The uniqueness of the finite-\(n\) zero traps \(r_n\) between those trial points. Sending \(t_-\) and \(t_+\) to the limiting zero proves all three limits. Substitution into \(\theta_n=cr_n/(n-1+cr_n)\) gives the three budget-fraction limits.

## Verification

Run `python3 verify.py` with the Python standard library. The script constructs the full \(2n\)-vertex Laplacian and exactly inverts \(L+J/(2n)\) over rational numbers for selected positive conductances. It tests the spectral Kirchhoff formula, checks rational signs around numerical approximations of the unique positive root, verifies the exact budget identity, and checks the large-network constants numerically. The extracted script produced `VERIFY_OK 202`. These finite tests check implementation and algebraic identities in samples; they do not certify the infinite-family asymptotics, whose proof is given above.

## Relationship to prior work

Ghosh, Boyd, and Saberi formulate and establish the convex effective-resistance minimization problem for weighted graphs, including wheel networks and a barbell consisting of two cliques joined by *one* edge. Their general framework covers this problem as an optimization task; their studied barbell has different connectivity, and its allocation formulas do not imply the three asymptotic regimes above. Boyd's dated 2006 lecture identifies inverse positive Laplacian eigenvalue sums as total resistance and develops general convexity and symmetry methods. The particular graph here has a *perfect matching* of interlayer connections, so its interlayer spectrum and investment behavior differ from the one-edge barbell. Published work on resistance of graph Cartesian products provides structural context, but fixed-weight product identities alone do not optimize conductance under two prices.

## Limitations

The proof is for two identical complete layers with precisely the corresponding-vertex matching; it does not cover arbitrary two-layer graphs, incomplete interlayer matching, nonuniform individual prices, or price sequences varying with network size. The formula for the finite optimum is an implicit but uniquely solvable scalar equation, not a radical closed form. The 2006 talk is day-dated August 29; the related resistance-minimization work had an earlier **July 2006** conference version whose precise first public release *day* could not be verified. The recorded date therefore identifies the earliest verified day-precise relevant public source, not a claimed first publication of the entire general framework. A broad literature search and detailed primary-source comparison reduce but do not eliminate the risk of an equivalent unindexed theorem. No independent mathematical audit has been performed.

## References

1. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, International Congress of Mathematicians presentation, Madrid, August 29, 2006. https://web.stanford.edu/~boyd/papers/pdf/icm06_talk.pdf (especially slide 5).
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66, DOI: 10.1137/050645452. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf (especially Sections 2, 5.2, and the barbell example on pp. 60–61). An earlier conference version appeared July 2006.
