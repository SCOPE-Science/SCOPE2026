# Sharp odd–even sampling constants for Bernstein circle covariances

## Finding

Let \(f(\theta)=b_0+\sum_{m\ge1}b_m\cos(m\theta)\) be a continuous positive-semidefinite circle covariance on \([0,\pi]\), with \(b_m\ge0\) and \(\sum_m b_m<\infty\). Fix a degree \(n\ge1\) and take its ordinary Bernstein approximant \(g(\pi t)=\sum_{r=0}^n \binom nr t^r(1-t)^{n-r}f(r\pi/n)\). Put
\[
D_s=\sum_{m\ge1,\ m\equiv s\pmod 2} b_m[1-\cos(m\pi/n)],\qquad s=0,1.
\]
On the regular \(N\)-gon, let \(\lambda_N\) be the least eigenvalue of the **unnormalized** Gram matrix with entries \(g(d_{S^1}(e^{2\pi i j/N},e^{2\pi i \ell/N}))\). With \(n,f\) held fixed,
\[
\lim_{N\to\infty,\ N\ {\rm even}}N\lambda_N=2n\min(D_0,D_1),\qquad
\lim_{N\to\infty,\ N\ {\rm odd}}N\lambda_N=\frac n2(\sqrt{D_0}+\sqrt{D_1})^2.
\]
In particular, with just one active parity, odd grids still have a strictly positive inverse-grid-size lower eigenvalue scale, even though sufficiently large even grids are singular. With both masses positive, the odd constant is strictly larger unless the masses are equal. These are quantitative statements for equally spaced samples, not assertions about arbitrary designs or jointly increasing Bernstein degree.

## Proof

Let \(\beta_0=\pi^{-1}\int_0^\pi g\) and \(\beta_k=2\pi^{-1}\int_0^\pi g(\theta)\cos(k\theta)\,d\theta\) for \(k\ge1\). Set \(c_0=\beta_0\) and \(c_{\pm k}=\beta_k/2\). All \(c_k\ge0\) by the Bernstein preservation theorem of Otten, Nguyen and Watts. The endpoint derivatives of \(P(t)=g(\pi t)\) are \(P'(0)=-n(D_0+D_1)\), \(P'(1)=n(D_0-D_1)\), by the first and last differences of the sampled cosine modes. Integration by parts for the polynomial \(P\) gives
\[
c_{\pm k}=\frac{2nD_{k\bmod2}}{\pi^2 k^2}+O_{n,f}(k^{-4})\qquad(k\ge1).
\]
If \(D_s=0\) all nonconstant coefficients of parity \(s\) vanish: each positive-weight mode in that parity must be sampled as a constant, and other modes contribute only in their own parity by reflection about \(t=1/2\). These tail and vanishing statements were also given in the earlier antipodal Gram-nullity result cited below. If \(D_0>0\) then \(c_0>0\): a nonconstant even sampled mode has mean \(1/(n+1)\), obtained by summing the real parts of the powers of its nontrivial \(n\)-th root of unity from 0 through \(n\). The mean of a Bernstein image is the average of its sampled values. Odd modes have zero mean, and aliased constants have mean one.

Absolute convergence and the discrete Fourier transform give the circulant eigenvalues \(\Lambda_{N,j}=N\sum_{r\in\mathbb Z}c_{j+rN}\) for \(0\le j<N\). On any compact interior range for \(u=j/N\), the expansion of \(c_k\) gives the following profiles for \(N\Lambda_{N,j}\), with a uniform \(O(N^{-2})\) error there (sum the inverse fourth powers; write \(p=j\bmod2\)):
\[
\begin{cases}
2nD_p/\sin^2(\pi u),&N\text{ even},\\[2pt]
\dfrac n2\left(D_p/\sin^2(\pi u/2)+D_{1-p}/\cos^2(\pi u/2)\right),&N\text{ odd}.
\end{cases}
\]
Here \(\sum_{r\in\mathbb Z}(u+r)^{-2}=\pi^2/\sin^2(\pi u)\); the odd-grid profile splits that sum into even and odd \(r\) because their aliases have opposite parities. Both index parities approximate every interior fraction.

For both masses positive, no edge subsequence can contain minimizing indices. Indeed, by reflection it is enough to consider \(j/N\to0\). If \(j\to\infty\), the single \(r=0\) term gives a divergent lower bound of order \((N/j)^2\). If \(j\) stays bounded, the nonnegative sum gives the same divergence via a positive \(c_j\). To verify strict positivity for a fixed \(j>0\) of an active parity, reduce a contributing frequency to a folded representative \(1\le m\le n\) modulo \(2n\). In the matching-parity regime \(j\ge m\), Otten–Nguyen–Watts, Proposition 2.3 and Lemma 3.2, give an Abel sum whose sine partial sums are \(\sin^2(\ell\vartheta)/\sin\vartheta\), \(\vartheta=m\pi/(2n)\), and whose weights decrease strictly; the first partial sum is positive (also in the one-term case). For \(j<m\), their Proposition 3.1 gives a positive multiple of \(\int_0^1 w(u)\sin(bu)\,du\), where \(b=j\pi/2\), \(w=(1-u)^{n-1}\cosh(au)\), and \(0\le a=b\cot\vartheta\le n-1\). The weight has \(w'<0\) on \((0,1)\); integration by parts against \((1-\cos(bu))/b\) makes this integral strictly positive. This is a strictness refinement of the source's nonnegativity argument. For \(j=0\), use \(c_0>0\) as above. The even profile now minimizes at \(u=1/2\) in the smaller-mass parity. The odd profile uses \(\min_{0<x<1}(A/x+B/(1-x))=(\sqrt A+\sqrt B)^2\) for positive \(A,B\), with \(x=\sin^2(\pi u/2)\).

With a single positive mass \(D\), sufficiently large even grids have a nonzero index in the inactive parity, giving an exactly zero eigenvalue. For odd grids interior limits are at least \(nD/2\). At an edge, reduce to \(j/N\to0\) by reflection: if \(j\) has active parity, the preceding single-term argument gives divergence (if \(j=0\) then the even parity is active and \(c_0>0\)). If \(j\) has inactive parity, only odd \(r\) contribute apart from a possible nonnegative constant term at \(j=0\). All these odd aliases have absolute index at least \(N-j\). The tail expansion thus applies uniformly to their entire sum, giving limit \(nD/2\) for that part. Choose inactive indices with \(j\to\infty\) and \(j/N\to0\) to attain this limit without a constant term. When both masses are zero, \(g\) is constant, so \(\lambda_N=0\) for \(N\ge2\).

## Prior results and scope of the contribution

- M. Otten, N. Nguyen and T. W. Watts, [*Preservation of Positive-Definiteness by Bernstein Operators on the Circle*](https://arxiv.org/abs/2608.04836), arXiv:2608.04836 (2026), establishes positive-semidefinite preservation. The coefficient identities and sign arguments above use their Propositions 2.3 and 3.1 and Lemmas 3.2–3.3.
- [*Complete antipodal Gram-nullity geometry for Bernstein circle covariances*](https://github.com/Resultary/2026/blob/main/2026/11/16/SCOPE-complete-antipodal-gram-nullity-geometry-for-bernstein-circle-co--30f205ea35ee/RESULT.md), 2026-11-16, gives the exact nullity on arbitrary distinct sets and the criterion for strict positive definiteness on all such sets. The cyclic rank classification follows by taking the number of antipodal pairs to be zero on odd grids and \(N/2\) on even grids. Those ranks, the strict positive-definiteness criterion, and the endpoint tail are not asserted as new here. The new comparison assessed here is the two sharp least-eigenvalue limits, not priority over every possible source.

For illustration, \(n=2\) and \(f(\theta)=1+\cos\theta+\cos(2\theta)\) give \((D_0,D_1)=(2,1)\), hence scaled limits \(4\) and \((1+\sqrt2)^2\) through even and odd grids. The accompanying finite checker illustrates this mixed example and the coefficient identities; the proof, rather than those finite checks, gives the sharp limits.
