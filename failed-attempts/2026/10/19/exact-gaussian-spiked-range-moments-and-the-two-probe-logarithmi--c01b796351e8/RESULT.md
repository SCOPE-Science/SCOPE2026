# Exact Gaussian spiked-range moments and the two-probe logarithmic boundary

## Finding
Let \(n\ge3\), \(1\le s<n\), \(p\ge1\) be integers, \(0<\varepsilon<1\), and \(\Omega\in\mathbb R^{n\times s}\) have independent standard real Gaussian entries. Set
\[
A_\varepsilon=\operatorname{diag}(1,\varepsilon,\ldots,\varepsilon),\qquad
P=\operatorname{proj}_{\operatorname{range}(A_\varepsilon^p\Omega)},\qquad
R=\|(I-P)A_\varepsilon\|_F^2,\quad \delta=\varepsilon^p.
\]
Put \(\nu=n-s\). Then, with independent chi-squared random variables \(D\sim\chi^2_\nu\) and \(N\sim\chi^2_s\),
\[
\boxed{R\ \stackrel d=\ \nu\varepsilon^2+(1-\varepsilon^2)U,
\qquad U=\frac{\delta^2D}{N+\delta^2D}.}
\]
Equivalently, for \(X\sim\operatorname{Beta}(\nu/2,s/2)\),
\[
U\ \stackrel d=\ \frac{\delta^2X}{1-(1-\delta^2)X}.
\]
For every real \(q>0\), the exact positive moment is
\[
\mathbb E U^q=
\delta^{2q}\frac{B(\nu/2+q,s/2)}{B(\nu/2,s/2)}
\,{}_2F_1\!\left(q,\nu/2+q;\,n/2+q;\,1-\delta^2\right).
\]
Write \(a=s/2\), \(b=\nu/2\). As \(\delta\downarrow0\), with \(n,s,q\) fixed,
\[
\mathbb E U^q\sim
\begin{cases}
\displaystyle\delta^{2q}\frac{\Gamma(b+q)\Gamma(a-q)}{\Gamma(b)\Gamma(a)},&0<q<a,\\[6pt]
\displaystyle 2\delta^s\log(1/\delta)\frac{\Gamma(b+a)}{\Gamma(b)\Gamma(a)},&q=a,\\[6pt]
\displaystyle\delta^s\frac{\Gamma(b+a)\Gamma(q-a)}{\Gamma(b)\Gamma(q)},&q>a.
\end{cases}
\]
There is also an exact sharp rare-event law: for each fixed \(0<u<1\),
\[
\boxed{\lim_{\delta\downarrow0}\delta^{-s}\Pr\{U>u\}=
\frac{\Gamma(n/2)}{\Gamma((n-s)/2)\Gamma(s/2+1)}
\left(\frac{1-u}{u}\right)^{s/2}.}
\]
In the mean-squared case \(q=1\), this becomes the **one-, two-, and at least three-probe transition**
\[
\mathbb E U\sim\begin{cases}
\displaystyle\frac{\sqrt\pi\,\Gamma(n/2)}{\Gamma((n-1)/2)}\,\delta,&s=1,\\[5pt]
(n-2)\delta^2\log(1/\delta),&s=2,\\[3pt]
\displaystyle\frac{n-s}{s-2}\,\delta^2,&3\le s<n.
\end{cases}
\]
At identical probe count, the ordinary Gaussian range finder is \(p=1\), while the **left subspace** computed by the two-pass row-aware procedure on this symmetric example is \(p=2\). For \(s=1\) the expected squared residual is asymptotic to \(\sqrt\pi\Gamma(n/2)\varepsilon/\Gamma((n-1)/2)\) in the ordinary method, but to \(\left(n-1+\sqrt\pi\Gamma(n/2)/\Gamma((n-1)/2)\right)\varepsilon^2\) in the two-pass method. For every \(s\ge2\), the two-pass method has \(\mathbb ER\sim(n-s)\varepsilon^2\), attaining the best possible rank-\(s\) Frobenius squared residual at leading order. The ordinary method has a logarithmic excess for \(s=2\) and a strictly positive proportional excess for \(s\ge3\).

## Assumptions and scope
All random variables are real and all QR operations are understood in exact arithmetic. The Gaussian \(n\)-by-\(s\) sketch has full column rank almost surely; \(n>s\) guarantees the residual degrees of freedom \(\nu\) are positive. The parameter \(p\) is a positive integer and denotes the power applied to the diagonal matrix, not the rank of a postprocessed truncated SVD. The comparison \(p=2\) concerns the **range of the left factor \(Q\)** of the two-pass row-aware scheme, \(Q=\operatorname{qr}(A_\varepsilon\operatorname{qr}(A_\varepsilon^{\mathsf T}\Omega))\), which equals the range of \(A_\varepsilon^2\Omega\). The statistic is precisely \(\|A_\varepsilon-QQ^{\mathsf T}A_\varepsilon\|_F^2\), not the reconstruction residual \(\|A_\varepsilon-A_\varepsilon PP^{\mathsf T}\|_F^2\) based on the right factor, or the optional rank-one truncated-SVD residual. The optimal rank-\(s\) reference is \((n-s)\varepsilon^2\).

## Proof
Write the sketch in blocks \(\Omega=\begin{bmatrix}a\\B\end{bmatrix}\), where \(a\in\mathbb R^{1\times s}\), \(B\in\mathbb R^{(n-1)\times s}\). Almost surely \(B\) has full column rank. Put \(Y=\begin{bmatrix}a\\\delta B\end{bmatrix}\). By the Schur complement (or the matrix inversion lemma),
\[
U=1-e_1^{\mathsf T}Y(Y^{\mathsf T}Y)^{-1}Y^{\mathsf T}e_1
=\frac{\delta^2}{\delta^2+a(B^{\mathsf T}B)^{-1}a^{\mathsf T}}.
\]
Rotational invariance permits rotation of the sketch columns so that \(a=(\sqrt N,0,\ldots,0)\), where \(N=\|a\|_2^2\sim\chi_s^2\). Conditional on \(a\), the rotated \(B\) remains a matrix of independent standard normals. The inverse-Gram Schur complement identity gives
\[
\bigl((B^{\mathsf T}B)^{-1}\bigr)_{11}^{-1}
=\|(I-P_{B_{2:s}})B_1\|_2^2\ \sim\ \chi^2_{(n-1)-(s-1)}=\chi^2_{n-s},
\]
and this \(D\) is independent of \(N\). Hence \(a(B^{\mathsf T}B)^{-1}a^{\mathsf T}=N/D\), giving the exact ratio distribution. The ratio \(D/(D+N)\) is beta with parameters \((\nu/2,s/2)\).

Because \(A_\varepsilon A_\varepsilon^{\mathsf T}=\varepsilon^2I+(1-\varepsilon^2)e_1e_1^{\mathsf T}\) and \(\operatorname{tr}(I-P)=n-s\),
\[
R=\operatorname{tr}((I-P)A_\varepsilon A_\varepsilon^{\mathsf T})
=(n-s)\varepsilon^2+(1-\varepsilon^2)U.
\]
The beta density integrated against \(\bigl(\delta^2x/[1-(1-\delta^2)x]\bigr)^q\) yields the hypergeometric moment formula by Euler's integral representation, valid for every \(q>0\).

For the sharp asymptotics put \(a=s/2\), \(b=\nu/2\) and use the independent gamma densities of \(N,D\). If \(q<a\), the family \(\delta^{-2q}U^q=(D/(N+\delta^2D))^q\) is dominated by \((D/N)^q\), whose mean factors into gamma moments, and dominated convergence gives the first case. If \(q>a\), condition on \(D=d\), scale \(N=\delta^2dt\), and use the bound \(e^{-\delta^2dt/2}\le1\). The remaining beta integral is \(\int_0^\infty t^{a-1}(1+t)^{-q}dt=B(a,q-a)\); the \(D^a\) expectation supplies the displayed coefficient. At \(q=a\) the same scaled integral diverges logarithmically at infinity; splitting at \(t=1\) and \(t=1/\delta^2\) gives \(2\log(1/\delta)+O(1+|\log D|)\). Since \(\mathbb E[D^a(1+|\log D|)]<\infty\), integration gives the sharp middle coefficient. Finally, for fixed \(0<u<1\), \(U>u\) is equivalent to \(N<\delta^2D(1-u)/u\); the chi-square CDF at zero, \(\Pr\{N<z\}\sim z^a/(2^a\Gamma(a+1))\), together with dominated convergence and the finite \(a\)-moment of \(D\), yields the rare-event law. Inserting \(q=1\) and \(\delta=\varepsilon^p\) proves every stated comparison. No simulation or finite enumeration is used to infer an infinite statement.

## Verification
The included standalone `verify.py` uses exact SymPy rational matrices and 75-digit mpmath hypergeometric and incomplete-beta evaluations. It reconstructed \(P\) from \(Y\) for dimensions \(3\) through \(6\), all admissible sketch sizes, multiple nonsingular integer Gaussian-sample surrogates, two rational spike values and three powers; checked the Schur-complement and squared-loss identities; tested representatives of every asymptotic moment regime, the rare-event coefficient, and finite-noise upper/lower bounds. It passed 957 assertions at the time of packaging. Reproduce with `python verify.py` after installing the versions in `requirements.txt`. Algebraic certificates and the written proof, not the finite checker, establish the universal result.

## Relationship to prior work
Palitta and Portaro, arXiv:2408.04503, Algorithms 2.1 and 3.1, construct the standard and row-aware Gaussian ranges, while their Theorems 2.1 and 3.1 provide expected **norm upper bounds** primarily under target-rank/oversampling restrictions. Their Algorithm 3.1 constructs the left subspace in the stated way; that construction is prior work, not part of the novelty claim. Saibaba (arXiv:1804.02614) analyzes randomized subspace iteration and deterministic/probabilistic bounds on canonical angles and unitarily invariant approximation errors. Gu (arXiv:1408.2208) likewise develops subspace-iteration error bounds, including heavy-tail-sensitive Gaussian estimates. Diouane and collaborators (arXiv:2206.08793) give general error-analysis bounds. The result here specializes to a structured one-spike spectrum but yields an **exact distribution, the full moment threshold, the critical two-probe logarithmic constant, and the fixed-threshold rare-event coefficient** rather than a general worst-case bound. The one-probe heavy-tail mechanism is related to existing inverse-chi-square and rank-one sketch calculations; no novelty is claimed for that mechanism in isolation.

## Limitations
The theorem is for a fixed-dimensional, real, Gaussian, equal-tail-spike diagonal model; it does not give a uniform-in-dimension limit, extend automatically to generic spectra, or cover finite-precision orthogonalization and rank-one post-truncation. It quantifies the quality of the left *range*, not the paper's distinct final SVD output. A generalized gamma/inverse-Wishart reformulation may have appeared in literature not indexed or inspected; independent priority assessment remains open.

## References
1. D. Palitta and S. Portaro, *Row-aware Randomized SVD with applications*, arXiv:2408.04503, first posted 8 August 2024; version 4 (31 July 2025), Algorithms 2.1/3.1 and Theorems 2.1/3.1, https://arxiv.org/abs/2408.04503 .
2. A. K. Saibaba, *Randomized subspace iteration: Analysis of canonical angles and unitarily invariant norms*, arXiv:1804.02614, 2018, https://arxiv.org/abs/1804.02614 .
3. M. Gu, *Subspace Iteration Randomization and Singular Value Problems*, arXiv:1408.2208, 2014, https://arxiv.org/abs/1408.2208 .
4. Y. Diouane and collaborators, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793, 2022, https://arxiv.org/abs/2206.08793 .
