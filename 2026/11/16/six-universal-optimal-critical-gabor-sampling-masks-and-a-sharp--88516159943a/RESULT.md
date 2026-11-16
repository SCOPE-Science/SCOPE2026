# Six universal optimal critical Gabor sampling masks and a sharp Gaussian width-uniform bound

## Finding
Let \(0<b<a\), \(g=(a,b,b)/\sqrt{a^2+2b^2}\in\mathbb C^3\), and let the nine unit Gabor atoms be \(u_{x,k}=M_kT_xg\), with \(x,k\in\mathbb Z_3\). For any three-element subset \(S\subset\mathbb Z_3^2\), put \(A(S)=\sum_{(x,k)\in S}u_{x,k}u_{x,k}^{*}\). Then
\[
\max_{|S|=3}\lambda_{\min}(A(S))
=\frac{a^2-2ab+4b^2}{a^2+2b^2}.
\]
Exactly six subsets attain the maximum: the graphs \(S=\{(x,\sigma(x)):x\in\mathbb Z_3\}\) of the six permutations \(\sigma\) of \(\mathbb Z_3\). For each such subset the complete spectrum is
\[
\left\{\frac{a^2-2ab+4b^2}{a^2+2b^2},\quad
\frac{a^2+ab+b^2}{a^2+2b^2},\quad
\frac{a^2+ab+b^2}{a^2+2b^2}\right\}.
\]

In particular, let \(g^{\lambda}\) be the normalized length-three vector obtained by periodizing and sampling \(e^{-\pi\lambda t^2}\), where \(\lambda>0\). Its six optimal sampling masks are independent of \(\lambda\), and its best three-sample lower frame bound satisfies the **sharp width-uniform inequality**
\[
\max_{|S|=3}\lambda_{\min}(A_{\lambda}(S))\ge\frac{3-\sqrt3}{2}.
\]
Equality is attained at the self-Fourier width \(\lambda=3\).

## Assumptions and scope
For coordinates \(j\in\mathbb Z_3\), define \((T_xf)(j)=f(j-x)\) and \((M_kf)(j)=\exp(2\pi ikj/3)f(j)\). Norms and eigenvalues use the standard Hermitian inner product of \(\mathbb C^3\). The analysis operator takes a signal to three Gabor inner products; its optimal lower frame bound is the least eigenvalue of \(A(S)\). Repeated time-frequency indices are excluded, and no extra weights are permitted. The result maximizes the **lower bound**, not necessarily the ratio of upper to lower frame bounds.

Define the unnormalized Gaussian samples by
\[
G_j^{\lambda}=\sum_{m\in\mathbb Z}\exp\bigl(-\pi\lambda(m+j/3)^2\bigr),\qquad j=0,1,2.
\]
Then \(G_0^{\lambda}=a_\lambda\), \(G_1^{\lambda}=G_2^{\lambda}=b_\lambda\), and \(g^{\lambda}=G^{\lambda}/\|G^{\lambda}\|_2\). The source date concerns the sampled-periodized Gaussian construction, not a claim that the present stability result was already in that source.

## Proof
Write \(s=a^2+2b^2\). Every atom has squared norm one. The three-by-three frame operator \(A(S)\) and the Gram matrix \(\Gamma(S)=(\langle u_v,u_w\rangle)_{v,w\in S}\) have the same eigenvalues.

**A repeated translation loses optimality.** If two distinct selected nodes share \(x\), their modulations differ. Their inner-product magnitude equals \((a^2-b^2)/s\), since \(1+\omega+\omega^2=0\) for \(\omega=e^{2\pi i/3}\). The smallest eigenvalue of their two-by-two Gram principal submatrix is \(1-(a^2-b^2)/s=3b^2/s\). By the Rayleigh principle, \(\lambda_{\min}(\Gamma(S))\le3b^2/s\), strictly below the proposed optimum by \((a-b)^2/s>0\).

**A repeated modulation loses optimality.** If two distinct selected nodes share \(k\), then their translations differ and their inner-product magnitude is \((2ab+b^2)/s\). The same principal-submatrix argument gives \(\lambda_{\min}(\Gamma(S))\le(a-b)^2/s\), strictly below the proposed optimum by \(3b^2/s>0\).

Thus every maximizing triple must have three different translations and three different modulations; these are precisely the six permutation graphs. Every permutation of \(\mathbb Z_3\) has the form \(\sigma(x)=\varepsilon x+c\), where \(\varepsilon\in\{1,-1\}\) and \(c\in\mathbb Z_3\). Common modulation shifts move \(c\), and complex conjugation, because \(g\) is real, interchanges the two signs; consequently all six Gram spectra agree.

For the representative \(\{(0,0),(1,1),(2,2)\}\), direct multiplication yields the unnormalized Gram characteristic polynomial
\[
\bigl(t-(a^2-2ab+4b^2)\bigr)\bigl(t-(a^2+ab+b^2)\bigr)^2.
\]
Since their difference is \(3b(a-b)>0\), division by \(s\) gives the asserted eigenvalues and strict optimality. The preceding cases exhaust all \(\binom93=84\) possible three-point masks.

**Gaussian specialization.** Poisson summation gives
\[
a_\lambda-b_\lambda=\frac{2}{\sqrt\lambda}\sum_{n=1}^{\infty}e^{-\pi n^2/\lambda}\bigl(1-\cos(2\pi n/3)\bigr)>0,
\]
while both terms are positive. Put \(r=b_\lambda/a_\lambda\in(0,1)\). The optimized lower bound is
\[
F(r)=\frac{1-2r+4r^2}{1+2r^2},\qquad
F'(r)=\frac{2(2r^2+2r-1)}{(1+2r^2)^2}.
\]
It follows that \(F(r)\ge(3-\sqrt3)/2\), with equality precisely when \(r=(\sqrt3-1)/2\).

For \(\lambda=3\), reindexing \(G_j^3=\sum_{n\equiv j\ (\mathrm{mod}\ 3)}e^{-\pi n^2/3}\) and applying the Poisson summation formula shows that the unnormalized length-three discrete Fourier transform satisfies \(\widehat G^3=\sqrt3 G^3\). As \(G^3=(a_3,b_3,b_3)\), its zero-frequency coordinate gives \(a_3+2b_3=\sqrt3 a_3\), and hence \(b_3/a_3=(\sqrt3-1)/2\). Thus the uniform constant is attained.

## Verification
The included `CHECK.py` uses exact symbolic cyclotomic arithmetic through SymPy. It enumerates all 84 distinct three-node masks, verifies the two-way geometric partition, checks the Gram characteristic polynomial separately for each of the six optimizers, and verifies the rational optimization and radical value. A separate convergent Gaussian-series check confirms the self-dual identity numerically; the proof above, not this numerical check, establishes the identity for the infinite series. Run with `python CHECK.py` in an environment with SymPy.

## Relationship to prior work
Abreu, Balazs, Holighaus, Luef and Speckbacher (arXiv:2209.04191, version 1 of September 9, 2022) establish that every three-point discrete Gabor mask with a periodized Gaussian window is a basis in dimension three (Theorem 3). That theorem gives **existence**, not the best lower frame bound or the six optimal masks. Faulhuber and Shafkulovska (arXiv:2204.02917, April 6, 2022) optimize frame bounds for infinite rectangular-lattice Gabor systems with other windows, not arbitrary three-point finite masks. Closely related indexed findings about two-tap windows with full translation banks or three modulation channels address different operators and do not imply this minimum-eigenvalue optimization.

## Limitations
The finite-dimensional theorem concerns exactly the nine atoms on \(\mathbb Z_3^2\), with equal atom weights, and windows \(g\) of the stated symmetric positive form. It does not assert optimality in larger dimensions, for other window shapes, for off-grid sampling, or for conditioning ratios or noise models beyond the sharp least-eigenvalue guarantee. Historical priority among unindexed specialized three-dimensional Gabor-frame calculations remains subject to further verification; no independent audit is claimed.

## References
- L. D. Abreu, P. Balazs, N. Holighaus, F. Luef, M. Speckbacher, *Time-frequency analysis on flat tori and Gabor frames in finite dimensions*, arXiv:2209.04191 (first posted September 9, 2022). https://arxiv.org/abs/2209.04191
- M. Faulhuber, I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (first posted April 6, 2022). https://arxiv.org/abs/2204.02917
