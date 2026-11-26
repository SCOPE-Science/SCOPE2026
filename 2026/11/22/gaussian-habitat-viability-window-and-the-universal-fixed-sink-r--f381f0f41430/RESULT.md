# The order-1/n boundary-density correction for a fixed number of sinks in dense random graphs

## Finding

Let \(G_n\sim G(n,p)\) with \(p\in(0,1)\) fixed, and delete the rows and columns of a deterministic set of \(s\ge1\) vertices from the full combinatorial Laplacian, with \(s\) fixed. Write \(m=n-s\), \(\xi_n\) for the smallest eigenvalue of the grounded Laplacian, and \(B_n\) for the number of cross edges between the retained and removed sets. Then
\[
m\left(\frac{B_n}{m}-\xi_n\right)\xrightarrow{\mathbb P}s(1-p).
\]
The quantity resolved here is the order-\(1/m\) relaxation below the *random observed* boundary density, not the fluctuation of the density around its expectation. The positive coefficient separates the constant-vector approximation from the true minimum even though they agree at the coarser Gaussian fluctuation scale.

## Proof

Let \(L_H\) be the Laplacian of the induced graph on the retained vertices. The grounded Laplacian is \(L_H+Z\), with \(Z=\operatorname{diag}(z_i)\) and \(z_i\) independent \(\operatorname{Binomial}(s,p)\) counts of sink neighbors. These counts are independent of \(L_H\), and \(B_n=\sum_i z_i\). Put \(e=m^{-1/2}\mathbf1\), \(Q=I-ee^{\mathsf T}\), \(\bar z=B_n/m\), and \(b=QZe\). The Rayleigh principle gives \(0\le\xi_n\le \bar z\le s\), and the law of large numbers gives
\[
\|b\|^2=m^{-1}\sum_i(z_i-\bar z)^2\xrightarrow{\mathbb P}sp(1-p).
\]

The centered internal Laplacian is \(E_m=L_H-p(mI-\mathbf1\mathbf1^{\mathsf T})\). In its edge-sum representation, the independent summands are \((A_{ij}-p)(e_i-e_j)(e_i-e_j)^{\mathsf T}\), where the \(e_i\) are coordinate unit vectors. Each has operator norm at most 2 and the sum of their second moments is \(2p(1-p)(mI-\mathbf1\mathbf1^{\mathsf T})\). Self-adjoint matrix Bernstein therefore gives \(\|E_m\|=O_{\mathbb P}(\sqrt{m\log m})\). In particular, the restriction of \(L_H\) to \(e^\perp\) has least eigenvalue greater than \(s\) with probability tending to one.

On this event a minimizing eigenvector has nonzero component along \(e\): the Rayleigh quotient of every vector in \(e^\perp\) exceeds \(s\), whereas \(\xi_n\le s\). Eliminating its component in \(e^\perp\) gives the exact Schur identity
\[
\bar z-\xi_n=b^{\mathsf T}(QL_HQ+QZQ-\xi_n I_{e^\perp})^{-1}b.
\]
The inverse is taken on \(e^\perp\). The internal term on that space is \(pmI_{e^\perp}+O_{\mathbb P}(\sqrt{m\log m})\), in operator norm, and both \(QZQ\) and \(\xi_n I\) are bounded by \(s\). The inverse is consequently \((pm)^{-1}(I_{e^\perp}+O_{\mathbb P}(\sqrt{\log m/m}))\). Thus \(m(\bar z-\xi_n)=\|b\|^2/p+o_{\mathbb P}(1)\), proving the limit. For a finite deterministic graph whose retained Laplacian has gap \(g>s\), the same Schur argument gives \(0\le\bar z-\xi_n\le s^2/(g-s)\).

## Gaussian window as a consequence, and relation to prior work

The coefficient theorem gives \(\bar z-\xi_n=O_{\mathbb P}(1/m)\), so the binomial CLT for \(B_n\sim\operatorname{Binomial}(sm,p)\) gives \(\sqrt n(\xi_n-sp)\Rightarrow N(0,sp(1-p))\). By continuity of the limiting law, for each fixed \(a\in\mathbb R\),
\[
\Pr(\xi_n<sp+a/\sqrt n)\longrightarrow \Phi(a/\sqrt{sp(1-p)}),
\]
where \(\Phi\) is the standard normal CDF. The window describes strict positive *linear* invasion for reproduction-to-diffusion ratio \(sp+a/\sqrt n\); it is not a finite-population persistence result.

The Gaussian window is not the originality claim. Pirani and Sundaram [1, Theorem 3] give the earlier leading approximation \(\xi_n\sim sp\); their earlier estimates in the same paper also imply the window without the coefficient theorem. In their notation normalize the positive principal eigenvector \(x\) by \(\max_i x_i=1\), and write \(x=\gamma\mathbf1+d\) with \(d\perp\mathbf1\). Their Eq. (9), using the dense retained-graph gap of order \(m\) and \(B_n\le sm\), yields \(\|d\|_2=O_{\mathbb P}(m^{-1/2})\) and hence \(\gamma=1+O_{\mathbb P}(m^{-1/2})\). Summing the eigenvector equation gives \(\xi_n=\bar z+z^{\mathsf T}d/(m\gamma)\); since \(\|z\|_2\le s\sqrt m\), this is \(\bar z+O_{\mathbb P}(m^{-1})\). The same binomial CLT now applies. This gap bound does not identify the coefficient: the proof above uses operator-norm concentration around \(pmI\) on the whole orthogonal subspace to evaluate the quadratic form to leading order. Apollonio, Tora and Vergni [2] give related viability bounds and concentration results but not this order-\(1/m\) coefficient in the fixed-sink, fixed-density regime. The accessible abstract of [3] concerns related spectral persistence bounds; its full text was not reviewed.

## Verification and limits

The accompanying frozen `check_fixed_sink.py` (Python, NumPy, SciPy) illustrates the deterministic bracket, Schur identity, and the bias and fluctuation scales in sampled graphs. These are finite diagnostics, not proof of the limit. For example, for the retained graph \(K_5\) and boundary degrees \((0,1,2,1,0)\), the smallest eigenvalue solves \(2/(5-\xi)+2/(6-\xi)+1/(7-\xi)=1\) below 5, giving \(\xi\approx0.694102470667\) and \(\bar z-\xi\approx0.105897529333\). No sparse, growing-sink, or network-adaptive sink regime is covered. Priority is bounded by the literature reviewed.

## References

1. M. Pirani and S. Sundaram, *On the Smallest Eigenvalue of Grounded Laplacian Matrices*, arXiv:1406.2271v2, Lemma 1 and Sections III–V, https://arxiv.org/html/1406.2271v2.
2. N. Apollonio, V. Tora and D. Vergni, *The Critical Patch Size Problem in Random Graphs*, arXiv:2604.00624v1, https://arxiv.org/html/2604.00624v1.
3. V. Tora and D. Vergni, *The critical patch size problem on networks*, Mathematical Biosciences 399 (2026), 109749, https://doi.org/10.1016/j.mbs.2026.109749.
4. J. A. Tropp, *User-friendly tail bounds for sums of random matrices*, Foundations of Computational Mathematics 12 (2012), 389–434, https://arxiv.org/abs/1004.4389.
