# A sharp \(4/\pi\) amplification law for Fourier projection onto two opposite finite parabolas

## Finding
For every odd prime \(p\ge5\), put \(G_p=\mathbb F_p^2\) and
\[
\Gamma_p=\{(x,x^2):x\in\mathbb F_p\}\cup\{(x,-x^2):x\in\mathbb F_p\}.
\]
Let \(P_{\Gamma_p}\) be the Fourier multiplier with symbol \(1_{\Gamma_p}\) acting on complex functions on \(G_p\). Its exact \(\ell^\infty\)-operator norm is given by the following one-dimensional formula. Let \(\chi_p\) be the quadratic character modulo \(p\), let \(\Phi_p(\theta)=\cos\theta\) when \(p\equiv1\pmod4\) and \(\Phi_p(\theta)=\sin\theta\) when \(p\equiv3\pmod4\), and define
\[
B_p=\begin{cases}2(p-1)\sqrt p,&p\equiv1\pmod4,\\p-1,&p\equiv3\pmod4.\end{cases}
\]
Then
\[
\boxed{\|P_{\Gamma_p}\|_{\ell^\infty\to\ell^\infty}=\frac{3p-2+B_p+(p-1)\displaystyle\sum_{t=1}^{p-1}\left|2\sqrt p\,\chi_p(t)\Phi_p(2\pi t/p)-1\right|}{p^2}.}
\]
As \(p\to\infty\) through primes,
\[
\boxed{\|P_{\Gamma_p}\|_{\ell^\infty\to\ell^\infty}=\frac4\pi\sqrt p+O\!\left(\frac{\log p}{\sqrt p}\right).}
\]
The same equality holds for the \(\ell^1\to\ell^1\) norm, by duality. In comparison, for a single parabola \(\Delta_p=\{(x,x^2):x\in\mathbb F_p\}\),
\[
\|P_{\Delta_p}\|_{\ell^\infty\to\ell^\infty}=\frac{1+(p-1)\sqrt p}{p};\qquad \lim_{p\to\infty}\frac{\|P_{\Gamma_p}\|}{\|P_{\Delta_p}\|}=\frac4\pi.
\]
For the unitary Fourier transform on \(G_p\) with counting-measure sequence norms, the Fourier ratio of the set indicator obeys
\[
\boxed{\frac{\|\widehat{1_{\Gamma_p}}\|_1}{\|\widehat{1_{\Gamma_p}}\|_2}=\frac{2\sqrt2}{\pi}p+O(\log p).}
\]

## Assumptions and scope
All functions and operator norms are over the complex numbers; all \(\ell^r\) norms use counting measure. The group Fourier transform is \(\widehat f(\xi)=p^{-1}\sum_{z\in G_p}f(z)e^{-2\pi i\langle z,\xi\rangle/p}\) (unitary in \(\ell^2\)). Thus the multiplier operator \(P_{\Gamma_p}\) has convolution kernel \(p^{-2}K_p\), where \(K_p(u,v)=\sum_{\xi\in\Gamma_p}e^{2\pi i\langle(u,v),\xi\rangle/p}\). There is no claim for extension to composite moduli or to other configurations of conics. The asymptotic constant is universal along both residue classes modulo four.

## Proof
**1. Exact Fourier kernel.** Since the two quadratic graphs meet exactly at the origin,
\[
K_p(u,v)=\sum_{x\in\mathbb F_p}e_p(ux+vx^2)+\sum_{x\in\mathbb F_p}e_p(ux-vx^2)-1,
\]
with \(e_p(a)=\exp(2\pi i a/p)\). In the slice \(v=0\), \(K_p(0,0)=2p-1\), while \(K_p(u,0)=-1\) for every \(u\ne0\). Their sum of absolute values is \(3p-2\).

For \(v\ne0\), completion of the square and the classical quadratic Gauss sum give
\[
\sum_x e_p(vx^2+ux)=\varepsilon_p\sqrt p\,\chi_p(v)e_p\!\left(-\frac{u^2}{4v}\right),\quad
\varepsilon_p=\begin{cases}1,&p\equiv1\pmod4,\\i,&p\equiv3\pmod4.\end{cases}
\]
The second summand replaces \(v\) with \(-v\). When \(u=0\), this gives \(K_p(0,v)=2\sqrt p\chi_p(v)-1\) in the first residue class and \(K_p(0,v)=-1\) in the second. Summing over the equally numerous square and nonsquare \(v\) gives exactly \(B_p\).

When \(u\ne0\), put \(t=u^2/(4v)\). Then \(\chi_p(v)=\chi_p(t)\), because \(u^2/4\) is a square. The two conjugate Gauss phases combine to
\[
K_p(u,v)=2\sqrt p\,\chi_p(t)\Phi_p(2\pi t/p)-1.
\]
Each nonzero \(t\) corresponds to exactly \(p-1\) pairs \((u,v)\) with \(uv\ne0\). Hence summation of \(|K_p|\) over all frequency pairs proves the boxed exact formula, once the operator-norm identity in step 2 is applied.

**2. Sharp endpoint operator norm.** A translation-invariant convolution operator with kernel \(h\) has \(\ell^\infty\to\ell^\infty\) norm exactly \(\sum_z|h(z)|\): the triangle inequality proves the upper bound, and for one prescribed output location the input values can be chosen as the conjugate phases of \(h\) to attain equality. Since the multiplier kernel is \(p^{-2}K_p\), its norm is \(p^{-2}\sum_{u,v}|K_p(u,v)|\). Duality gives the same \(\ell^1\) norm.

**3. Main term and character cancellation.** Let \(\theta_t=2\pi t/p\) and \(a_t=2\sqrt p\,\chi_p(t)\Phi_p(\theta_t)\). The sampled function \(|\Phi_p|\) has bounded total variation and integral \(4\) over one period, so
\[
\sum_{t=1}^{p-1}|\Phi_p(\theta_t)|=\frac{2p}{\pi}+O(1).
\]
The number of sampled indices with \(|a_t|\le1\) is \(O(\sqrt p)\): the sine or cosine has only two simple zeros on a period, and their \(O(p^{-1/2})\)-neighborhoods contain \(O(\sqrt p)\) grid points. For \(|a_t|>1\), the identity \(|a_t-1|=|a_t|-\operatorname{sgn}(a_t)\) is exact; for the remaining indices the discrepancy has absolute value at most two. Therefore
\[
\sum_{t=1}^{p-1}|a_t-1|=2\sqrt p\sum_{t=1}^{p-1}|\Phi_p(\theta_t)|-\sum_{t=1}^{p-1}\chi_p(t)\operatorname{sgn}(\Phi_p(\theta_t))+O(\sqrt p).
\]
The sign function is constant on a bounded number of intervals of residues, because sine and cosine have two sign changes per period. For any interval \(I\subset\mathbb F_p\), Fourier completion and the quadratic Gauss estimate give
\[
\left|\sum_{t\in I}\chi_p(t)\right|\le\frac{\sqrt p}{p}\sum_{r=1}^{p-1}\left|\sum_{t\in I}e_p(rt)\right|=O(\sqrt p\log p).
\]
The final estimate uses the geometric-series bound \(|\sum_{t\in I}e_p(rt)|\le\min(|I|,p/(2\min(r,p-r)))\). Thus the signed-character term is \(O(\sqrt p\log p)\), and
\[
\sum_{t=1}^{p-1}|a_t-1|=\frac4\pi p^{3/2}+O(\sqrt p\log p).
\]
Inserting this into the exact formula, and using \(B_p=O(p^{3/2})\), proves the stated operator-norm asymptotic, with the error \(O(\log p/\sqrt p)\).

**4. Single parabola and Fourier ratio.** The Fourier kernel for the single parabola equals \(p\) at \((0,0)\), is zero on \((u\ne0,v=0)\), and has modulus \(\sqrt p\) at all \(p(p-1)\) positions with \(v\ne0\). Dividing its \(\ell^1\) sum by \(p^2\) gives \((1+(p-1)\sqrt p)/p\) and the ratio limit. Finally \(|\Gamma_p|=2p-1\), Plancherel gives \(\|\widehat{1_{\Gamma_p}}\|_2=\sqrt{2p-1}\), while its \(\ell^1\) norm is \(p\|P_{\Gamma_p}\|\). This proves the Fourier-ratio identity and asymptotic.

## Verification
The standalone `CHECK.py` directly sums the \(p^2\) unnormalized Fourier coefficients of the two-branch indicator, without using Gauss-sum identities, and compares the resulting endpoint norm against the independently evaluated one-dimensional character formula. It also checks the single-parabola norm and counting-measure Fourier-ratio normalization at several primes. This finite numerical check is illustrative only: the proof above applies to every odd prime \(p\ge5\). The asymptotic error term uses the classical incomplete-character-sum bound proved in step 3, not finite extrapolation.

## Relationship to prior work
Iosevich, Li and Yu (2026, arXiv:2609.25404v1) introduce the Fourier ratio for finite spectral synthesis and calculate exact synthesis constants for affine-transitive single paraboloids (Sections 4–6); their Section 2 explicitly relates the indicator Fourier algebra norm to the ratio. The present result concerns the singular reducible union of two *opposite* parabolas, which is not a single affine-transitive paraboloid, and determines an explicit endpoint projection norm and a universal interference factor \(4/\pi\). The Gauss-sum evaluation itself is classical. Li (2026, arXiv:2609.16030v1) studies sparse finite-parabola zero-set rigidity rather than this full-indicator Fourier algebra norm. Gilbert and Rzeszotnik (2010) calculate unrestricted finite-group Fourier-transform mapping norms, not norms of this specific spectral projection. See the named references.

## Limitations
The result is for odd prime fields only; it neither settles general conic unions nor determines any sharp weighted spectral-synthesis constants for the union. The Fourier ratio here is for the indicator, not for arbitrary weights on \(\Gamma_p\). The finite exact formula still involves a length-\(p-1\) sum. An earlier equivalent formula hidden under the terms *idempotent norm*, *Fourier algebra norm*, or *paired quadratic Gauss sums* cannot be excluded; no claim of independent publication-priority certification is made.

## References
- A. Iosevich, Z. Li, and K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404v1, first posted 2026-09-21, especially Sections 2, 4, 5 and 8. https://arxiv.org/abs/2609.25404
- D. Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030v1, first posted 2026-09-11. https://arxiv.org/abs/2609.16030
- J. Gilbert and Z. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Annales de l'Institut Fourier 60 (2010), 1317–1346. https://doi.org/10.5802/aif.2556
- Standard quadratic Gauss evaluation and completion-of-sums/Pólya–Vinogradov estimate for quadratic characters, as proved in abbreviated form in the proof above.
