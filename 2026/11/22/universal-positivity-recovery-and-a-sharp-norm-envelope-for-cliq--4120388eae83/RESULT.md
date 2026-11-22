# Universal positivity recovery and a sharp norm envelope for clique-cone semigroups

## Finding
Let \(r\ge2\), let \(p_1,\ldots,p_r\) be arbitrary positive integers, and let \(N=1+\sum_i p_i\). Consider the connected unweighted graph
\[
G=K_1\vee(K_{p_1}\sqcup\cdots\sqcup K_{p_r}),
\]
with combinatorial Laplacian \(L\). Let \(\psi:[0,\infty)\to[0,\infty)\) satisfy \(\psi(0)=0\), \(\psi(1)=a>0\), and be strictly increasing on \([0,N]\). Put \(c=\psi(N)\) and define the real symmetric row-sum-one semigroup \(H(t)=\exp[-t\psi(L)]\), for every \(t\ge0\).

**Complete positivity phase:** If \(c\le Na\), all entries of \(H(t)\) are strictly positive for every \(t>0\). If \(c>Na\), there is exactly one positive \(T\) satisfying
\[
(N-1)+e^{-cT}-Ne^{-aT}=0.
\]
Then \(H(t)\) is entrywise nonnegative exactly for \(t=0\) and \(t\ge T\), is strictly positive for \(t>T\), and has negative cross-clique entries for every \(0<t<T\). **The exact positivity horizon depends only on \(N,a,c\), not on the number or sizes of cliques.**

**Sharp induced-norm envelope:** For \(c>Na\), set
\[
 D(t)=\frac{N-1+e^{-ct}-Ne^{-at}}{N(N-1)},\qquad
 t_*=\frac{\log[c/(Na)]}{c-a}.
\]
At all times,
\[
\boxed{\|H(t)\|_{\ell^1\to\ell^1}=\|H(t)\|_{\ell^\infty\to\ell^\infty}
\le1+2(N-2)[-D(t)]_+.}
\]
The upper bound is **attained at every time** precisely for graphs having at least one singleton base clique (when \(D(t)<0\)); for all partitions containing no singleton base clique the inequality is strict in \(0<t<T\). Consequently the largest possible peak over all such clique-cone graphs on \(N\) vertices equals
\[
\boxed{1+\frac{2(N-2)}{N(N-1)}
\left(Ne^{-at_*}-e^{-ct_*}-(N-1)\right),}
\]
and is attained exactly by the graphs with at least one singleton base clique. For \(c\le Na\), every induced \(\ell^1\) and \(\ell^\infty\) norm equals one at every time.

**Fractional-heat consequence:** For \(\psi(x)=x^\alpha\), \(\alpha>0\), the transition occurs exactly at \(\alpha=1\). For each fixed graph, with \(\varepsilon\downarrow0\),
\[
T_{1+\varepsilon}=\frac{2\log N}{N-1}\varepsilon+O_N(\varepsilon^2),
\qquad
\lim_{\alpha\to\infty}T_\alpha=\log\frac{N}{N-1}.
\]
The sharp, partition-optimized transient norm excess near \(\alpha=1\) is
\[
\frac{(N-2)(\log N)^2}{(N-1)^2}\varepsilon^2+O_N(\varepsilon^3).
\]
This includes arbitrarily heterogeneous windmills; singleton cliques correspond to degree-one leaves.

## Assumptions and scope
All edges have conductance one. All norms are counting-measure coordinate norms, not degree-normalized norms. Matrix functional calculus is defined by the real symmetric spectral theorem. Strict monotonicity is required only for comparisons between the spectral levels \(1,p_i+1,N\) and gives the strict extremizer statement; the positivity phase and non-strict norm envelope also hold if \(\psi\) is merely nondecreasing with \(\psi(1)>0\). There must be at least two base cliques; the one-clique case is a complete graph and is positive for every such \(\psi\), independently of the endpoint test. No assertion concerns arbitrary cones, normalized Laplacians, directed or weighted edges, or graph classes beyond the stated family.

## Proof
**Orthogonal spectral decomposition.** Write \(m=N-1\), and let \(J_q\) denote the all-ones \(q\)-by-\(q\) matrix. On leaf coordinates let \(B_i=J_{p_i}/p_i\) on clique \(i\), embedded by zero elsewhere, and put \(B=J_m/m\). The orthogonal spectral projections of \(L\) are the constant-mode \(P_0=J_N/N\), the apex-to-leaf contrast \(P_N\), the clique-average contrast \(P_1=\sum_iB_i-B\) (extended by zero on the apex), and \(P_{p_i+1}=I_{p_i}-B_i\) on each clique. Spectral eigenvalues are respectively \(0,N,1,p_i+1\). To check directly, \(P_N\) is the projector onto \((m,-1,\ldots,-1)\); \(P_1\) contains leaf vectors constant on each clique whose total leaf sum is zero; and a clique's zero-sum vectors have Laplacian eigenvalue \(p_i+1\). Their dimensions sum to \(N\). Coincident eigenvalues from equal-size cliques are handled by summing the indicated projections.

Put \(A=e^{-at}\), \(C=e^{-ct}\), and \(B_i(t)=e^{-\psi(p_i+1)t}\). From \(H=P_0+CP_N+AP_1+\sum_iB_i(t)P_{p_i+1}\), the apex--leaf entry is
\[
E(t)=\frac{1-C}{N}>0\quad (t>0),
\]
a leaf--leaf entry across different cliques is
\[
D(t)=\frac{m+C-NA}{Nm},
\]
and the entry between distinct leaves within clique \(i\) is
\[
W_i(t)=D(t)+\frac{A-B_i(t)}{p_i}\ge D(t).
\]
Every diagonal is strictly positive for \(t>0\), since each eigenvalue coefficient is positive and \(P_0\) contributes \(1/N\). Because \(\psi(0)=0\), every row sums to one; symmetry gives the same column sum.

**Positivity and the unique transition.** Different cliques exist, so \(D\) is a realized entry. Its derivative is
\[
D'(t)=\frac{Na e^{-at}-c e^{-ct}}{N(N-1)}.
\]
If \(c\le Na\), then \(c\ge a\) and \(D'(t)>0\) for all \(t>0\), so \(D(t)>0\) for \(t>0\). If \(c>Na\), the derivative changes sign exactly once at \(t_*\): it is negative before \(t_*\) and positive after. Since \(D(0)=0\), \(D(t_*)<0\), and \(D(t)\to1/N\), there is exactly one positive zero \(T>t_*\). The formulas for \(E,W_i\) and positive diagonals imply the stated entire-matrix sign phase, including strict positivity beyond \(T\).

**Norm and extremality.** A real row summing to one has absolute row sum equal to one plus twice its total negative-entry mass. For a leaf of clique \(i\), the negative-entry mass is exactly
\[
(N-1-p_i)[-D(t)]_++(p_i-1)[-W_i(t)]_+.
\]
The apex row has no negative entries. Because \(W_i\ge D\), the displayed mass is at most \((N-2)[-D]_+\). A singleton clique has one leaf with all \(N-2\) other leaves outside its clique, hence attains this bound. If no clique is singleton, then \(p_i>1\) and strict increase of \(\psi\) gives \(W_i>D\) for \(t>0\), producing strict inequality whenever \(D<0\). For \(c>Na\), \(D\) is minimized uniquely at \(t_*\), giving the sharp peak formula; if no clique is singleton, compactness of \([0,T]\) and strict inequality inside yield a strictly smaller global peak. Equality of column and row maxima follows by symmetry. For \(c\le Na\), positivity and stochastic rows give norm one.

**Fractional limits.** For \(\psi(x)=x^\alpha\), put \(\delta=N^\alpha-N\). At \(\alpha=1+\varepsilon\), \(\delta=N\log N\,\varepsilon+O_N(\varepsilon^2)\). Near the positive root, Taylor expansion of the scalar equation \(m+e^{-N^\alpha t}-Ne^{-t}=0\), after factoring its known zero at \(t=0\), gives \(T=2\delta/[N(N-1)]+O_N(\delta^2)\). Hence the displayed linear law. Also \(t_*\sim\delta/[N(N-1)]\) and \(-D(t_*)=\delta^2/[2N^2(N-1)^2]+O_N(\delta^3)\), yielding the quadratic peak law. Finally \(T_\alpha\) increases with \(c=N^\alpha\), since \(\partial_cD=-t e^{-ct}/[N(N-1)]<0\) while \(D'_t(T)>0\). It remains below \(\log[N/(N-1)]\), where \(D>0\), and for any smaller positive \(t\), \(D(t)\) tends to \(((N-1)-Ne^{-t})/[N(N-1)]<0\). This proves its stated limit.

## Verification
The supplied `verify.py` independently constructs each graph Laplacian and diagonalizes it numerically for all ordered clique partitions through ten total vertices, comparing complete matrix kernels, exact row norms, and the phase and peak formulas at seven strictly increasing generator functions. A separate exact-rational branch verifies all stated spectral projector resolutions and orthogonality for every ordered partition of eight leaves. It passed 956 exact projector checks, 17,570 matrix-and-norm comparisons, 3,514 phase tests, and 1,506 peak-bound tests. Reproduce with Python 3, NumPy and SciPy: `python3 verify.py`. These finite checks are diagnostic only; the all-parameter statements follow from the preceding proof.

## Relationship to prior work
Daners and Glück (2018) establish general sufficient conditions for uniform eventual positivity; these do not give a topology-specific necessary-and-sufficient positivity test or exact recovery time. Benzi, Bertaccini, Durastante and Simunec (2019) formulate fractional network dynamics, primarily in the positive-power range; they do not give the asserted all-increasing-generator phase diagram on clique cones. Kling (2023) and Kooij (2019) establish the relevant clique-coalescence and windmill Laplacian spectral structure but not sharp semigroup entry positivity and induced-norm extremality.

A published result, *Convex spectral filters on heterogeneous clique windmills have an exact apex-positivity criterion* (2026), derives the same leaf projector entry formulas for convex filters. It proves positivity from \(f(Nt)\le1\) under global convexity of \(f\). In the new non-positive regimes \(c>Na\), the filter \(f(x)=e^{-t\psi(x)}\) generally fails this convexity requirement (for example \(\psi(x)=x^\alpha\), \(\alpha>1\), is concave near zero after exponentiation). That theorem's convex hypothesis excludes the recovery phenomenon and the sharp all-topology norm envelope here; the shared spectral decomposition is antecedent, not claimed as novel. A published complete-multipartite fractional-heat theorem (2026) already includes the star case; the new claim concerns the exact same positivity transition across **all** heterogeneous clique cones and the extremal comparison of their induced norms. A separate windmill Gauss–Legendre rational-step theorem covers a different non-semigroup filter. The contribution is not the graph spectrum, the existing convex-filter formula, or star-specific fractional diffusion, but the complete nonconvex semigroup phase and topology-uniform sharp amplification envelope.

## Limitations
Strict monotonicity of the generator and the unweighted clique-cone geometry are essential to the strict extremizer classification. The extremal norm is for induced counting \(\ell^1\) and \(\ell^\infty\), not an exact spectral norm or a uniform theorem for arbitrary graph joins. Finite checks do not establish universal algebraic identities; these are proved analytically. The source comparison does not certify historical priority against inaccessible or unindexed papers, and independent mathematical validation has not been performed.

## References
1. D. Daners and J. Glück, *A criterion for the uniform eventual positivity of operator semigroups*, arXiv:1801.05179 (first public 2018-01-16), https://arxiv.org/abs/1801.05179.
2. M. Benzi, D. Bertaccini, F. Durastante and I. Simunec, *Nonlocal network dynamics via fractional graph Laplacians*, arXiv:1912.07288 (first public 2019-12-16), https://arxiv.org/abs/1912.07288.
3. G. Kling, *On the uniqueness of the Laplacian spectra of coalescence of complete graphs*, Open Journal of Discrete Applied Mathematics 6 (2023), 25–39 (published 2023-04-30), https://doi.org/10.30538/psrp-odam2023.0082.
4. R. Kooij, *On generalized windmill graphs*, Linear Algebra Appl. 565 (2019), 25–46, https://doi.org/10.1016/j.laa.2018.11.025.
5. *Convex spectral filters on heterogeneous clique windmills have an exact apex-positivity criterion* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-convex-spectral-filters-on-heterogeneous-clique-windmills-have-a--c55885b0d081.
6. *A sharp positivity transition for fractional graph heat on complete multipartite networks* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1.
7. *A sharp Gauss–Legendre positivity horizon on windmill graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-gauss-legendre-positivity-horizon-on-windmill-graphs--a8ca5b261d22.
