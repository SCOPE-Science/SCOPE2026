# Exact Gaussian log-volume fluctuations for a critical cyclic Gabor basis

## Finding

For every integer \(p\ge 3\), let \(N=2p\), and give \(\mathbb C^N\) its standard Hermitian inner product. For \(k,\ell,j\in\mathbb Z_N\), write
\[
(T_k g)[j]=g[j-k],\qquad (M_\ell g)[j]=e^{2\pi i\ell j/N}g[j].
\]
Take exactly \(N\) Gabor atoms \(M_{2\ell}T_k g\), where \(0\le\ell<p\) and \(k\in\{0,1\}\). Form their square synthesis matrix \(G_p\) and its frame operator \(S_p=G_pG_p^*\). Let the entries of \(g\) be independent circular complex Gaussians of mean zero and variance \(1/(2p)\), meaning the real and imaginary parts independently have variance \(1/(4p)\).

Then \(G_p\) is invertible almost surely. With Euler's constant \(\gamma\), put
\[
\mu=1-2\gamma-\log 4,\qquad
\sigma^2=\frac{2\pi^2}{3}-3>0.
\]
The random log-volume \(H_p=\log\det S_p=2\log|\det G_p|\) obeys the **exact finite-size identities**
\[
\boxed{\mathbb E H_p=p\mu,\qquad \operatorname{Var}(H_p)=p\sigma^2}\quad(p\ge3),
\]
and the **central limit theorem**
\[
\boxed{\frac{H_p-p\mu}{\sigma\sqrt p}\ \xrightarrow[p\to\infty]{\mathrm{distribution}}\ \mathcal N(0,1).}
\]
In particular, the geometric mean of the \(2p\) positive eigenvalues of the frame operator converges in probability:
\[
\boxed{(\det S_p)^{1/(2p)}\ \xrightarrow[p\to\infty]{\mathrm{probability}}\frac12e^{(1-2\gamma)/2}=0.462845096596516\ldots.}
\]
The variance \(\sigma^2\) includes a nonzero contribution from Gaussian coordinates reused by neighboring Gabor blocks. It is therefore **not** the variance obtained by treating the blocks as independent Wishart matrices.

## Assumptions and scope

The statement holds for every integer \(p\ge3\), with a *fresh* independent complex-Gaussian window in dimension \(2p\) for each \(p\). No almost-sure coupling between dimensions is asserted. The distributional and in-probability conclusions use only the marginal law for each dimension. The modulation frequencies are precisely the even residue classes modulo \(2p\), and the two translation indices are adjacent, \(0\) and \(1\). Gaussian variance is normalized to make \(\mathbb E\|g\|_2^2=1\). The log-determinant refers to the frame operator, not to a nonlinear intensity-measurement operator.

## Proof

**1. Exact block factorization.** Put \(\xi=\sqrt{2p}\,g\), so the coordinates of \(\xi\) are independent standard circular complex Gaussians. Group the physical coordinates into pairs \(\{a,a+p\}\), for \(a=0,\ldots,p-1\). The modulation sum is
\[
\sum_{\ell=0}^{p-1}e^{2\pi i(2\ell)(j-j')/(2p)}
=p\,\mathbf 1_{j\equiv j'\pmod p}.
\]
Consequently, a fixed permutation turns \(S_p\) into a direct sum of \(p\) Hermitian matrices of order two. Define independent Gaussian column vectors
\[
V_a=\begin{pmatrix}\xi_a\\\xi_{a+p}\end{pmatrix},\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The blocks are exactly
\[
B_a=\frac12(V_aV_a^*+W_aW_a^*),\qquad
W_a=\begin{cases}V_{a-1},&a\ge1,\\JV_{p-1},&a=0.\end{cases}
\]
The swap \(J\) at the cyclic boundary is essential: omitting it produces a different finite Gabor system. The two-by-two Gram determinant identity yields
\[
\det B_a=\frac14|\det[V_a,W_a]|^2,
\qquad
\det S_p=4^{-p}\prod_{a=0}^{p-1}|\det[V_a,W_a]|^2.
\]
Each factor is strictly positive almost surely, since conditional on one nonzero Gaussian vector the other is independent with an absolutely continuous law. Hence the system is a basis almost surely.

**2. Radial and angular decomposition.** Write \(V_a=R_a^{1/2}U_a\), where \(R_a=\|V_a\|_2^2\) has the Gamma distribution with shape two and scale one, and \(U_a\) is Haar-uniform on the unit sphere of \(\mathbb C^2\). All radii are independent of all directions, and the pairs are independent across \(a\). Define \(D_a=|\det[U_a,\widetilde U_{a-1}]|^2\), with \(\widetilde U_{a-1}=U_{a-1}\) for \(a\ge1\) and \(\widetilde U_{p-1}=JU_{p-1}\) at \(a=0\). Then
\[
H_p=-p\log4+2\sum_{a=0}^{p-1}\log R_a+
\sum_{a=0}^{p-1}\log D_a.
\tag{1}
\]
For fixed unit \(u\in\mathbb C^2\) and independent Haar-uniform unit \(U\),
\[
|\det[U,u]|^2=1-|\langle U,u\rangle|^2
\]
is uniformly distributed on \((0,1)\). Thus every \(D_a\) is uniform on \((0,1)\). Moreover, \(\log D_a\) and \(\log D_b\) are uncorrelated whenever \(a\ne b\). For disjoint edges this is independence; for adjacent edges, condition on their shared direction. The two remaining directions are independent, and each conditional angular distribution is uniform, independent of the conditioned direction. This argument also covers the edge containing \(J\), since \(J\) is unitary. For \(p\ge3\), every pair of different edges is either disjoint or shares precisely one direction.

**3. Exact moments.** The standard Gamma log-moment identities give
\[
\mathbb E\log R_a=\psi(2)=1-\gamma,
\qquad
\operatorname{Var}(\log R_a)=\psi_1(2)=\frac{\pi^2}{6}-1.
\]
Since \(D_a\) is uniform on \((0,1)\),
\[
\mathbb E\log D_a=-1,\qquad
\operatorname{Var}(\log D_a)=1.
\]
The radial terms are independent and also independent of the angular terms. The angular logarithms are pairwise uncorrelated, though not asserted jointly independent around the entire cycle. Therefore (1) gives, exactly for each \(p\ge3\),
\[
\mathbb E H_p=p[-\log4+2(1-\gamma)-1]=p\mu,
\]
\[
\operatorname{Var}(H_p)
=4p\left(\frac{\pi^2}{6}-1\right)+p
=p\left(\frac{2\pi^2}{3}-3\right).
\]

**4. Gaussian fluctuations.** On the nonboundary edges define
\[
X_a=\log|\det[V_a,V_{a-1}]|^2,\qquad 1\le a<p.
\]
The variables \(X_a\) form a stationary one-dependent sequence, since each depends only on two consecutive independent Gaussian vectors. Their common mean is \(1-2\gamma\). Their variance is \(2\psi_1(2)+1\), and their adjacent covariance is \(\psi_1(2)\); hence the long-run variance is
\[
[2\psi_1(2)+1]+2\psi_1(2)=\sigma^2.
\]
Every logarithmic moment is finite. The standard central limit theorem for stationary one-dependent sequences therefore applies to \(\sum_{a=1}^{p-1}(X_a-\mathbb EX_a)\). The single boundary term \(\log|\det[V_0,JV_{p-1}]|^2\), after centering, has a distribution not depending on \(p\) and finite second moment, so divided by \(\sqrt p\) it vanishes in probability. Slutsky's theorem proves the displayed central limit theorem. Finally the exact variance implies \((H_p-p\mu)/p\to0\) in probability, by Chebyshev's inequality, proving the geometric-mean limit.

## Verification

Run `python CHECK.py` with NumPy installed. The included checker constructs the original full Gabor matrix, computes its Gram log-determinant, and compares it against the independently assembled two-by-two determinant factorization over 250 seeded finite instances. It also performs two seeded Monte Carlo sanity checks for the exact first and second moments. The recorded outcome was `GAUSSIAN_CYCLIC_GABOR_VOLUME_CHECKS_PASSED 254`. The exact identities and the infinite-size central limit theorem are proved above; finite sampling is not offered as proof of either probabilistic statement.

## Relationship to prior work

Asipchuk, De Carli, and Rodriguez [1] establish general explicit block equivalence for finite Gabor systems with a subgroup of modulations or translations. This provides the appropriate structural context; the present two-translation random-window law obtains an exact log-determinant and a fluctuation variance, which their stated results do not give. Salanevich [2] investigates extreme singular values of random time-frequency structured matrices, and Salanevich and Strachan [3] establish random Gabor frame-bound and erasure-robustness estimates. Neither inspected work supplies the stated deterministic local determinant factorization combined with its full exact Gaussian log-volume moments and central limit theorem. Classical Gaussian polar decomposition, Gamma log-moments, and the one-dependent central limit theorem are used as known facts, not presented as new.

## Limitations

The result measures logarithmic frame volume (the product of squared singular values). It is not a bound on the smallest singular value, condition number, or worst-case reconstruction error. The distribution is complex Gaussian, not real Gaussian or fixed-modulus random phase. The exact variance uses the two-translation, half-modulation geometry; more general time-frequency masks may produce other dependence ranges. Pairwise uncorrelated angular variables are not claimed jointly independent. The theorem makes no assertion of novelty for the underlying general block-diagonalization or for the classical one-dependent central limit theorem. No independent publication-priority assessment has been carried out.

## References

[1] O. Asipchuk, L. De Carli, and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, first submitted 2026-05-15. https://arxiv.org/html/2605.16139v2

[2] P. Salanevich, *Extreme Singular Values of Random Time-Frequency Structured Matrices*, arXiv:1902.01062 (2019). https://arxiv.org/html/1902.01062v1

[3] P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325 (2025). https://arxiv.org/html/2509.01325v1
