# Sharp one-step safety frontier and angle-dependent transient expansion for relaxed alternating projections

## Finding
Let \(U,V\) be proper, nonzero linear subspaces of a finite-dimensional real Euclidean space, let \(P_U,P_V\) denote their orthogonal projectors, let \(P=P_{U\cap V}\), and suppose the Friedrichs cosine \(c=c_F(U,V)\) satisfies \(0<c<1\). For real \(\omega\), define the relaxed alternating-projection operator \(T_\omega=(1-\omega)I+\omega P_UP_V\). Then:

1. **Exact Euclidean safety interval:** \(\|T_\omega\|_2\le1\) (equivalently, \(\|T_\omega-P\|_2\le1\)) if and only if
   \[0\le\omega\le\omega_E(c):=\frac{2+c}{1+c}.\]
   The upper endpoint is sharp for the given pair of subspaces and hence for every specified \(c\in(0,1)\).
2. **Uniquely best first step:** Over every real relaxation, \(\|T_\omega-P\|_2\ge c\), with equality if and only if \(\omega=1\). Thus spectral-rate acceleration by a fixed relaxation cannot improve the worst-case first-step Euclidean error.
3. **Sharp conflict with asymptotic tuning:** The known spectrally fastest relaxation is \(\omega_A(c)=2/(2-c^2)\), with optimized asymptotic eigenvalue modulus \(c^2/(2-c^2)\). It lies outside the one-step nonexpansive interval if and only if \(c>c_0\), where \(c_0\) is the unique real root in \((0,1)\) of
   \[c_0^3+2c_0^2-2=0,\qquad c_0=0.839286755214161\ldots .\]
   Consequently, \(\|T_{\omega_A}\|_2>1\) exactly when \(c>c_0\), it equals \(1\) at \(c=c_0\), and it is nonexpansive below the threshold.

## Assumptions and scope
The norm is the Euclidean induced operator norm. The real subspaces need not be disjoint or have equal dimensions. The fixed-point subspace \(U\cap V\) is preserved identically. The strict hypothesis \(0<c<1\) excludes the degenerate zero-Friedrichs-cosine and coincident-subspace cases. The result concerns the full map on the ambient Euclidean space, not just iterates initialized in one subspace. “Spectrally fastest” refers to the spectral radius of \(T_\omega-P\) as a function of the constant real parameter; it does not assert a minimum over varying relaxation sequences.

## Proof
**Principal-angle reduction.** By the canonical orthogonal decomposition of two subspaces, the nontrivial nonorthogonal principal-angle planes have cosines \(c_j\in(0,c]\), and on each such plane, after possibly transposing the block, the operator has matrix
\[B_j(\omega)=\begin{pmatrix}1-\omega s_j^2&0\\\omega c_j s_j&1-\omega\end{pmatrix},\qquad s_j^2=1-c_j^2.\]
The other blocks consist of identity on \(U\cap V\) and scalar \(1-\omega\) or degenerate versions with \(c_j=0\). The largest nontrivial cosine is \(c\), attained in finite dimension. Orthogonality of the decomposition also gives \(T_\omega=P\oplus(T_\omega-P)\), so \(\|T_\omega\|_2\le1\) exactly when \(\|T_\omega-P\|_2\le1\); the forward direction includes the possibility that \(P=0\).

**Safety.** Direct multiplication on a principal plane yields
\[I-B_j(\omega)^\mathsf TB_j(\omega)=\omega\begin{pmatrix}s_j^2(2-\omega)&-c_js_j(1-\omega)\\-c_js_j(1-\omega)&2-\omega\end{pmatrix}.\]
For \(\omega\notin[0,2]\), the displayed matrix cannot be positive semidefinite, as one of its diagonal entries is negative. For \(0\le\omega\le2\), positive semidefiniteness is equivalent to
\[(2-\omega)^2\ge c_j^2(1-\omega)^2,\]
because its determinant is \(\omega^2s_j^2\big((2-\omega)^2-c_j^2(1-\omega)^2\big)\). If \(0\le\omega\le1\), this is automatic; if \(1\le\omega\le2\), it is exactly \(\omega\le(2+c_j)/(1+c_j)\). The function \((2+t)/(1+t)\) is strictly decreasing for \(t\in(0,1)\), so the strongest bound comes from \(c_j=c\). The scalar blocks require only \(0\le\omega\le2\). This proves the first assertion including both endpoints.

**Unique first-step optimum.** The first column of the transposed principal block has squared norm
\[\|B_j(\omega)e_1\|_2^2=1-\omega(2-\omega)(1-c_j^2)=c_j^2+(1-c_j^2)(\omega-1)^2.\]
The original block and its transpose have the same spectral norm. Taking \(c_j=c\) gives \(\|T_\omega-P\|_2\ge\sqrt{c^2+(1-c^2)(\omega-1)^2}\ge c\), with strict inequality if \(\omega\ne1\). At \(\omega=1\), the canonical blocks have norm \(c_j\), while the scalar blocks vanish, giving \(\|P_UP_V-P\|_2=c\). This proves assertion two globally, not just among nonexpansive parameters.

**Asymptotic-versus-first-step threshold.** The eigenvalues on the nontrivial plane are \(1-\omega(1-c_j^2)\) and \(1-\omega\), so for \(\omega\in(0,2)\) the maximum nonfixed eigenvalue modulus is \(\max\{|1-\omega(1-c^2)|,|1-\omega|\}\). The two terms balance uniquely at \(\omega_A=2/(2-c^2)\), giving \(c^2/(2-c^2)\), in agreement with the existing asymptotic-rate theorem. Comparing the two exact parameters gives
\[\omega_A-\omega_E=\frac{c^3+2c^2-2}{(2-c^2)(1+c)}.\]
The cubic is strictly increasing on \((0,1)\), negative at zero and positive at one; hence it has precisely one root there. The safety equivalence already proved completes the third assertion.

## Verification
The standalone script `verify.py` uses exact rational arithmetic to check the two-by-two block identity, every entry of its Gram defect, the determinant factorization, the sharp interval endpoints and the cubic comparison for 24 distinct rational principal-angle instances generated by Pythagorean triples. It completes 5,064 exact rational checks. These are supplementary reproducibility checks; the infinite-dimensional-parameter theorem follows from the analytic argument above, not finite sampling. The source’s block representation and asymptotic optimum were checked directly against the cited primary text.

## Relationship to prior work
Bauschke, Bello Cruz, Nghia, Phan and Wang (first public arXiv version July 2, 2014; later journal article) prove the spectral-rate-optimizing relaxation for exactly the operator \(T_\omega\), and give its principal-angle block decomposition in their Theorem 3.6 and formula (48). Their claimed spectral optimum is **prior work**, not a new claim here. The present finding instead evaluates the sharp **one-step Euclidean nonexpansivity** interval, proves the unrelaxed step uniquely minimizes the operator norm, and locates the exact cubic angle at which the already-known spectral optimizer violates that safety interval. These comparisons operate on identical operators and conventions, not just similarly named methods.

Cegielski and Suchocka (2008) study the *different* projected relaxation \(P_A\big(x+\lambda(P_AP_Bx-x)\big)\) for convex sets; its outer projector makes its claims nonidentical. Only the accessible abstract, not its full text, was inspected, leaving a residual priority risk. Further equivalent unindexed treatments could also exist.

## Limitations
The statement is about full-space **single-step** Euclidean operator norm and fixed constant relaxation; it does not assert monotonicity of every individual iterate, a bound for every power, improved finite-time performance in a narrower initialization subspace, or any benefit for nonconvex projections. The established asymptotic-rate formula is inherited from the identified 2014 source and is clearly separated from the new one-step and angular-frontier statements. The source comparison is not a proof of absolute publication novelty. Independent mathematical review has not been performed.

## References
1. H. H. Bauschke, J. Y. Bello Cruz, T. T. A. Nghia, H. M. Phan and X. Wang, *Optimal rates of convergence of matrices with applications*, arXiv:1407.0671v1 (public July 2, 2014), especially Theorem 3.6 and formula (48); https://arxiv.org/pdf/1407.0671v1.
2. H. H. Bauschke, J. Y. Bello Cruz, T. T. A. Nghia, H. M. Phan and X. Wang, *Optimal Rates of Linear Convergence of Relaxed Alternating Projections and Generalized Douglas–Rachford Methods for Two Subspaces*, Numerical Algorithms 73 (2016), 33–76, DOI:10.1007/s11075-015-0085-4; author-hosted full text https://cdn.blot.im/folder/v-3cffc543/blog_ae8712159a464c2587bb10e2e0b396cc/Files/papers/098.pdf.
3. A. Cegielski and A. Suchocka, *Relaxed Alternating Projection Methods*, SIAM J. Optim. 19 (2008), 1093–1106, DOI:10.1137/070698750.
