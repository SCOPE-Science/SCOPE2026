# Exact Sobolev widths from discontinuous affine splines and a sharp mesh law

## Finding

For every integer \(N\ge1\) and any strictly increasing partition \(\pi=(t_0,\ldots,t_N)\) of \([0,1]\), write \(h_j=t_j-t_{j-1}>0\) and \(H=\max_j h_j\). Let \(V_\pi\subset L^2(0,1)\) be the discontinuous piecewise-affine space, with dimension \(2N\), and let \(P_\pi\) be its orthogonal projection. Then the following *sharp derivative-seminorm error law* holds, over real or complex functions:

\[
\sup_{f\in H^1(0,1),\ \|f'\|_2>0}
\frac{\|f-P_\pi f\|_2}{\|f'\|_2}=\frac{H}{2\pi}.
\]

All its nonconstant extremizers are exactly the functions

\[
f(x)=c+\sum_{j:\,h_j=H}a_j
\left[\cos\left(\frac{2\pi(x-t_{j-1})}{H}\right)-1\right]
\mathbf1_{[t_{j-1},t_j]}(x),
\qquad \sum_j|a_j|>0,
\]

with arbitrary complex (or real) coefficients \(a_j,c\). The endpoint values match, so these functions belong to \(H^1(0,1)\).

For the uniform \(N\)-cell partition, let \(B^1=\{f\in H^1(0,1):\|f\|_{H^1}\le1\}\), with \(\|f\|_{H^1}^2=\|f\|_2^2+\|f'\|_2^2\). Then

\[
\sup_{f\in B^1}\inf_{v\in V_\pi}\|f-v\|_2
=\frac1{\sqrt{1+(2\pi N)^2}}
=d_{2N}(B^1;L^2(0,1)).
\]

Thus the uniform discontinuous affine space is exactly (not only asymptotically) Kolmogorov-width optimal at every even dimension. Among nonzero functions, the only extremizers of the normalized full-\(H^1\) ratio are scalar multiples of \(\cos(2\pi Nx)\). For any nonuniform mesh, the derivative-seminorm error exceeds the uniform value since \(H>1/N\).

## Assumptions and scope

All partitions have finite, strictly positive cell lengths. Functions are in the standard one-dimensional Sobolev space \(H^1(0,1)\), which has continuous representatives. The approximation error is in \(L^2\), and the local approximation is an independent least-squares affine polynomial on each cell. The full-norm width is over *all* \(2N\)-dimensional subspaces of \(L^2(0,1)\), not only polynomial spaces. No endpoint boundary conditions are imposed. The statements hold for real and complex Hilbert spaces.

## Proof

**Step 1: A sharp one-cell lemma.** On \((0,1)\), denote by \(Q\) the \(L^2\)-orthogonal projection onto \(\operatorname{span}\{1,t\}\). We show

\[
\|g-Qg\|_2^2\le\frac1{4\pi^2}\|g'\|_2^2,
\]

with equality precisely for \(g(t)=c+a\cos(2\pi t)\). Expand \(g=a_0+\sum_{n\ge1}a_ne_n\) in the Neumann cosine basis \(e_n=\sqrt2\cos(n\pi t)\). Parseval (including the derivative form for \(H^1\)) yields

\[
\|g'\|_2^2=\pi^2\sum_{n\ge1}n^2|a_n|^2.
\]

The normalized affine direction orthogonal to constants is \(\ell(t)=\sqrt{12}(t-1/2)\), and its cosine coefficients are

\[
v_n=\langle e_n,\ell\rangle
=\frac{\sqrt{24}((-1)^n-1)}{(n\pi)^2},
\qquad
\sum_{n\ge1}|v_n|^2=1.
\]

Consequently

\[
\|g-Qg\|_2^2=\sum_{n\ge1}|a_n|^2-\left|\sum_{n\ge1}v_na_n\right|^2.
\]

For even indices \(v_n=0\), and \(1-n^2/4\le0\), with equality only at \(n=2\). For the odd sector, put \(q=|v_1|^2=96/\pi^4\), \(Z=\sum_{n\ge3,\,n\text{ odd}}v_na_n\), and

\[
B=\sum_{n\ge3,\,n\text{ odd}}\left(\frac{n^2}{4}-1\right)|a_n|^2,
\quad
C=\sum_{n\ge3,\,n\text{ odd}}\frac{|v_n|^2}{n^2/4-1}.
\]

Cauchy--Schwarz gives \(|Z|^2\le BC\), while \(0<C\le\frac45(1-q)\). Minimizing in \(Z\) gives

\[
|v_1a_1+Z|^2+B\ge\frac{q}{1+C}|a_1|^2
\ge\frac{5q}{9-4q}|a_1|^2
>\frac34|a_1|^2,
\]

where the strict last inequality follows from \(q>27/32\) (for example \(\pi^2<10\) suffices). Thus the odd sector is strictly below the proposed sharp quotient unless all its coefficients vanish. Only the even \(n=2\) mode survives equality, establishing the lemma for arbitrary real or complex \(H^1\) functions, including infinite Fourier series (all sums converge by Cauchy--Schwarz and Parseval).

**Step 2: Arbitrary mesh and all seminorm extremizers.** Affine scaling of the one-cell lemma gives

\[
\|f-P_\pi f\|_{L^2(t_{j-1},t_j)}^2
\le\frac{h_j^2}{4\pi^2}\|f'\|_{L^2(t_{j-1},t_j)}^2.
\]

Summing yields the upper bound \(H/(2\pi)\). On any maximal cell, the continuous function equal there to \(\cos(2\pi(x-t_{j-1})/H)-1\) and zero elsewhere attains equality. Equality in every summed step forces \(f\) to be constant on shorter cells and to be a constant plus a first full cosine cycle on each maximal cell. Continuity at cell endpoints forces all endpoint levels to equal one common \(c\). This is exactly the displayed family of extremizers.

**Step 3: Full-norm optimality at uniform meshes.** Orthogonality gives \(\|f\|_2^2=\|P_\pi f\|_2^2+\|f-P_\pi f\|_2^2\). Combining it with the seminorm inequality gives the universal full-norm bound

\[
\frac{\|f-P_\pi f\|_2}{\sqrt{\|f\|_2^2+\|f'\|_2^2}}
\le\frac1{\sqrt{1+(2\pi/H)^2}}.
\]

For the uniform mesh, \(f(x)=\cos(2\pi Nx)\) is orthogonal on *each* cell both to constants and to the local affine coordinate; it has \(\|f'\|_2=2\pi N\|f\|_2\). Hence it reaches the bound. Equality additionally requires \(P_\pi f=0\), so Step 2 and continuity force all local cosine amplitudes to agree, giving exactly scalar multiples of this global cosine. If a mesh is nonuniform, the bound is strict for every nonzero function: on a shorter cell equality requires a constant, while \(P_\pi f=0\) makes it zero; equality and continuity then propagate zero amplitude through all maximal-cell blocks. The compact embedding \(H^1\hookrightarrow L^2\) ensures the operator norm is attained, so this pointwise strictness is also strict at the supremum.

**Step 4: The width comparison.** The compact embedding \(H^1(0,1)\hookrightarrow L^2(0,1)\) has singular functions \(1,\sqrt2\cos(j\pi x)\), for \(j\ge1\), with singular values \((1+j^2\pi^2)^{-1/2}\). Thus the \(n\)-width of its unit ball equals \((1+n^2\pi^2)^{-1/2}\). Taking \(n=2N\) agrees exactly with Step 3, proving uniform-mesh global optimality.

## Verification

The standalone \(\texttt{check.py}\) independently tests the cosine moment formula and strict odd-frequency certificate, the finite-mode inequality for thousands of random real vectors, sharp equality at the second cosine, uniform-cell orthogonality, full-norm ratios, and supported maximal-cell witnesses on random positive meshes. A successful finite check is supplementary only; the proof above establishes the infinite-dimensional assertion. Run with \(\texttt{python check.py}\) using Python 3 and NumPy.

## Relationship to prior work

Yang and Zhang (2026) investigate the \(L^2\) sup-inf and Kolmogorov widths of spline spaces of degree \(k\) and continuity \(\mu\). Their Theorems A and B isolate an exceptional \(\nu=k-\mu=2\) regime for \(k>s-1\). The case \(s=1\), \(k=1\), \(\mu=-1\) is that regime. Their numerical and asymptotic analysis does not assert the exact finite-\(N\) identity proved here, nor its arbitrary-mesh equality classification. Floater and Sande discuss optimal spline spaces with prescribed boundary conditions and different smoothness setups. Classical sharp-width theory includes optimal spaces but does not, in the materials inspected, imply this specific uniform discontinuous-affine and all-mesh theorem. The Neumann spectrum and Poincaré methods used in the proof are classical; novelty is asserted only for their exact combined consequence in this setting.

## Limitations

This result concerns \(s=1\), degree-one discontinuous splines and \(L^2\) error only. It does not establish that uniform meshes uniquely minimize the *full-norm* approximation error among nonuniform partitions; strictness of an upper envelope alone cannot establish that. The derivative-seminorm assertion and its mesh-minimizing property are exact. Earlier equivalent formulations in the extensive classical \(n\)-width and approximation literature remain a publication-priority risk, and no independent audit has been performed.

## References

- P. Yang and Z. Zhang, *How good are spline spaces for the Kolmogorov \(n\)-width of a Sobolev ball?*, arXiv:2611.10371v1, submitted 7 November 2026. https://arxiv.org/html/2611.10371v1
- M. S. Floater and E. Sande, *Optimal spline spaces for \(L^2\) \(n\)-width problems with boundary conditions*, arXiv:1709.02710 (2017). https://arxiv.org/abs/1709.02710
- A. Pinkus, *\(n\)-Widths of Sobolev spaces in \(L^p\)*, Constructive Approximation 1 (1985), 15–62. https://doi.org/10.1007/BF01890021
- A. A. Melkman and C. A. Micchelli, *Spline spaces are optimal for \(L^2\) \(n\)-width*, Illinois Journal of Mathematics 22 (1978). Classical optimal-spline precedent.
