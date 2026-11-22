# A fixed-gap bulk–interface Schatten transition for weighted harmonic Bergman Toeplitz commutators

## Finding

Fix an integer \(d\ge1\), a weight parameter \(0<\beta<1\), and write \(\alpha=\beta-1\). On the complex harmonic Bergman space \(h^2_\alpha(\mathbb D)\), let \(T_j\) be the Toeplitz compression of multiplication by \(z^j\). Define the finite-rank commutator
\[
C_{n,d}=[T_{n+d},T_n],\qquad n=1,2,\ldots.
\]
There is a **sharp bulk–interface transition** for its Schatten masses. Put
\[
p_c=\frac1{1-\beta},\quad
G_\beta(j)=\frac{\Gamma(j+\beta+1)}{\Gamma(j+1)}\quad(j\in\mathbb N_0),
\]
and, for \(0<p<p_c\),
\[
I_{\beta,p}=2\beta^p\int_0^1
\left[t(1-t)^{\beta-1}\left(\frac{t}{2-t}\right)^{\beta/2}\right]^pdt.
\]
This integral is finite and positive. For every fixed \(p>0\), as \(n\to\infty\),
\[
\boxed{
\begin{array}{ll}
0<p<p_c:&\displaystyle n^{p-1}\|C_{n,d}\|_{\mathcal S_p}^{p}\longrightarrow d^p I_{\beta,p},\\[5pt]
p=p_c:&\displaystyle \frac{n^{\beta p}}{\log n}\|C_{n,d}\|_{\mathcal S_p}^{p}\longrightarrow2(\beta d)^p,\\[8pt]
p>p_c:&\displaystyle n^{\beta p}\|C_{n,d}\|_{\mathcal S_p}^{p}
\longrightarrow\sum_{r\in\mathbb Z}|G_\beta(|r|)-G_\beta(|d-r|)|^p.
\end{array}}
\]
The last series is absolutely convergent precisely for \(p>p_c\). Moreover, the exact leading operator-norm constant is
\[
\boxed{\displaystyle \lim_{n\to\infty}n^\beta\|C_{n,d}\|
=G_\beta(d)-G_\beta(0)>0.}
\]
In particular \(\|C_{n,d}\|\to0\), but its trace norm converges to the strictly positive number \(d I_{\beta,1}\). Each \(C_{n,d}\) is individually finite rank; the exponent \(p_c\) classifies **large-degree asymptotic mass**, not individual Schatten-class membership.

## Assumptions and scope

Take normalized planar area \(dA=\pi^{-1}dx\,dy\) on \(\mathbb D\) and the radial probability weight \(dA_\alpha=\beta(1-|z|^2)^{\beta-1}dA\), where \(0<\beta<1\). The Hilbert space \(h^2_\alpha\) consists of complex-valued harmonic functions in \(L^2(dA_\alpha)\). Let \(Q_\alpha\) be orthogonal projection onto this subspace; \(T_j=Q_\alpha M_{z^j}|_{h^2_\alpha}\). Throughout, commutators are \([A,B]=AB-BA\), \(d\) and \(\beta\) are fixed, and \(n\to\infty\). For \(0<p<1\), \(\|\cdot\|_{\mathcal S_p}^{p}\) denotes the standard Schatten quasi-norm power sum.

The monomial moments and normalized harmonic Fourier basis are
\[
\mu_j=\int_{\mathbb D}|z|^{2j}\,dA_\alpha
=\frac{\Gamma(\beta+1)\Gamma(j+1)}{\Gamma(j+\beta+1)},\quad
 e_j=\frac{z^j}{\sqrt{\mu_j}}\ (j\ge0),\quad
 e_{-j}=\frac{\bar z^{\,j}}{\sqrt{\mu_j}}\ (j\ge1).
\]
The variable \(j\) always denotes a nonnegative integer in \(\mu_j\) and \(G_\beta(j)\).

## Proof

**1. Exact singular-value reduction.** For every positive integer \(a\), angular orthogonality gives \(T_a e_j=b_a(j)e_{j+a}\), where
\[
b_a(j)=\begin{cases}
\sqrt{\mu_{j+a}/\mu_j},&j\ge0,\\
\sqrt{\mu_{-j}/\mu_{-j-a}},&j\le-a,\\
\mu_a/\sqrt{\mu_{-j}\mu_{j+a}},&-a<j<0.
\end{cases}
\]
Put \(m=n+d\), \(M=m+n\). Both ordered products agree on every \(e_j\) except \(e_{-k}\) for \(1\le k<M\). On these modes, \(C_{n,d}e_{-k}=c_{n,d}(k)e_{M-k}\), where direct substitution gives
\[
c_{n,d}(k)=\begin{cases}
\displaystyle\sqrt{\frac{\mu_{M-k}}{\mu_k}}
\left(\frac{\mu_n}{\mu_{n-k}}-\frac{\mu_m}{\mu_{m-k}}\right),&1\le k\le n,\\[8pt]
\displaystyle\mu_m\left(\frac{\sqrt{\mu_k/\mu_{M-k}}}{\mu_{k-n}}-
\frac{\sqrt{\mu_{M-k}/\mu_k}}{\mu_{m-k}}\right),&n<k<m,\\[8pt]
\displaystyle\sqrt{\frac{\mu_k}{\mu_{M-k}}}
\left(\frac{\mu_m}{\mu_{k-n}}-\frac{\mu_n}{\mu_{k-m}}\right),&m\le k<M.
\end{cases}
\]
For all these indices \(c_{n,d}(M-k)=-c_{n,d}(k)\). The inputs and outputs form orthonormal families. Thus all nonzero singular values are exactly the nonzero elements of \(\{|c_{n,d}(k)|:1\le k<M\}\), and
\[
\|C_{n,d}\|_{\mathcal S_p}^{p}=
\sum_{k=1}^{M-1}|c_{n,d}(k)|^p.
\]

**2. Macroscopic bulk profile.** The continuous moment extension obeys
\[
\frac{\mu_x}{\mu_{x-k}}\sim\left(\frac{x-k}{x}\right)^\beta
\quad\text{if }x,k,x-k\to\infty\text{ proportionally}.
\]
For \(1\le k\le n\) define \(F_x(k)=\mu_x/\mu_{x-k}\) for real \(x\ge k\). With \(\psi\) the digamma function,
\[
F_x'(k)=F_x(k)\bigl[q_\beta(x-k)-q_\beta(x)\bigr],\quad
q_\beta(y)=\psi(y+\beta+1)-\psi(y+1).
\]
Since \(q_\beta(y)=\beta/y+O_\beta(y^{-2})\) at infinity, the fundamental theorem of calculus applied to \(F_n(k)-F_{n+d}(k)\) gives, uniformly on compact subsets of \(0<t<1\),
\[
\frac nd c_{n,d}(\lfloor nt\rfloor)\longrightarrow
-\beta t(1-t)^{\beta-1}\left(\frac{t}{2-t}\right)^{\beta/2}.
\]
The exact antisymmetry from step 1 supplies the reflected positive profile on \(1<t<2\). Define \(H_\beta(t)=\beta t(1-t)^{\beta-1}(t/(2-t))^{\beta/2}\) for \(0<t<1\). Then the bulk magnitude is \(dH_\beta(t)/n\) to first order on the left and its reflection on the right.

**3. Uniform interface domination.** The same digamma difference is positive and bounded by \(C_\beta/(y+1)\) for \(y\ge0\). Standard two-sided gamma-ratio bounds give
\[
0<F_x(k)\le C_\beta\left(\frac{x-k+1}{x+1}\right)^\beta.
\]
Integrating \(F_x'\) over \([n,n+d]\), using \(k=n-r\), and observing \(\sqrt{\mu_{M-k}/\mu_k}\le C\) proves
\[
|c_{n,d}(n-r)|\le C_{\beta,d}\,n^{-\beta}(1+r)^{\beta-1}\qquad(0\le r<n).
\]
The finitely many middle indices \(n<k<m\) satisfy \(|c_{n,d}(k)|\le C_{\beta,d}n^{-\beta}\) directly. Reflecting \(k\mapsto M-k\), we conclude the global estimate
\[
\boxed{\quad |c_{n,d}(n+r)|\le C_{\beta,d}n^{-\beta}
(1+|r|)^{\beta-1},\quad 1-n\le r\le n+d-1.\quad}
\]
At \(p<p_c\), summing this bound over \(|r|\le\varepsilon n\) shows that the rescaled Schatten mass of the interface is at most \(C\varepsilon^{1-p(1-\beta)}\), plus a term tending to zero. Away from the interface, the bulk profile from step 2 is uniformly valid. Riemann sums, followed by \(\varepsilon\downarrow0\), give exactly the first regime and its integral \(I_{\beta,p}\).

**4. Microscopic gamma interface and the upper Schatten regime.** For each fixed signed integer \(r\), the exact three-case formula in step 1 and \(\mu_{n+a}\sim\Gamma(\beta+1)n^{-\beta}\) give
\[
\boxed{\quad n^\beta c_{n,d}(n+r)\longrightarrow
B_{\beta,d}(r)=G_\beta(|r|)-G_\beta(|d-r|).\quad}
\]
Using the gamma ratio expansion and the fixed finite difference of \(G_\beta\),
\[
|B_{\beta,d}(r)|\sim\beta d|r|^{\beta-1}\quad(|r|\to\infty).
\]
The domination from step 3 is summable after taking the \(p\)-th power precisely if \(p>p_c\). Dominated convergence for series then gives the third regime.

For \(p=p_c\), in the intermediate zone \(R\le |r|\le\varepsilon n\) with \(R\gg d\) and \(\varepsilon\ll1\), the gamma expansion of the exact coefficient is uniform and gives
\[
n^\beta|c_{n,d}(n+r)|
=\beta d|r|^{\beta-1}\bigl(1+O_{\beta,d}(R^{-1}+\varepsilon)\bigr).
\]
At the critical exponent, its \(p\)-th power is \((\beta d)^p/|r|\) to this relative precision. Each of the two sides contributes \((\beta d)^p\log n\) after the \(n^{\beta p}\) scaling; the finitely many central modes and the macroscopic \(|r|\ge\varepsilon n\) region contribute only \(O_{\beta,d,p,\varepsilon}(1)\) to that scaling. Let \(n\to\infty\), then \(R\to\infty\), and \(\varepsilon\downarrow0\), proving the middle regime with coefficient \(2(\beta d)^p\).

**5. Sharp operator norm.** The first forward difference of \(G_\beta\) is
\[
G_\beta(j+1)-G_\beta(j)=\frac{\beta G_\beta(j)}{j+1}>0.
\]
Its ratio at successive indices is \((j+\beta+1)/(j+2)<1\); hence \(G_\beta\) is strictly increasing and discretely concave. For any integer \(r\), the two indices \(|r|\) and \(|d-r|\) differ by at most \(d\), so strict concavity yields
\[
|B_{\beta,d}(r)|\le G_\beta(d)-G_\beta(0),
\]
with equality at \(r=0,d\). The uniform bound from step 3 makes \(n^\beta|c_{n,d}(n+r)|\to0\) uniformly as \(|r|\to\infty\), independently of \(n\). Consequently the fixed-interface convergence in step 4 also determines the limiting supremum, yielding the claimed operator-norm constant.

Finally \(1<p_c\), so the first regime at \(p=1\) implies \(\|C_{n,d}\|_{\mathcal S_1}\to dI_{\beta,1}>0\), while the norm limit implies \(\|C_{n,d}\|\to0\).

## Verification

The included self-contained `CHECKER.py` computes the action of each Toeplitz factor on the harmonic Fourier basis separately and compares the resulting two-step difference with the three-branch singular-value formula. It tests four weight parameters, all \(1\le n\le35\), gaps \(1\le d\le8\), and every possibly nonzero input mode, including the reflected antisymmetry. It also checks selected microscopic gamma-interface and norm asymptotics numerically. Run `python3 CHECKER.py`; the finite diagnostic reports `NEAR_DIAGONAL_HARMONIC_BERGMAN_DIAGNOSTIC_OK 88784`. These finite assertions do not establish the asymptotic theorem; steps 2–5 give the required analytic argument.

## Relationship to prior work

Cui–Huang–Lu–Zu [1] classify finite-rank and compact Toeplitz commutators on the unweighted harmonic Bergman disk; Dong–Zhou [2] give exact canonical forms for quasihomogeneous unweighted commutators. We claim neither finite rank nor the existence of coefficient formulas as new. The published weighted two-degree spectral law [3] treats degrees with a ratio tending to a strictly larger-than-one constant and expressly excludes ratios tending to one. Its macroscopic positive singular-value distribution is therefore not the present vanishing fixed-gap limit. The published high-degree bulk–boundary theorem [4] treats \([T_z,T_{z^m}]\), with one degree fixed; its critical exponent and boundary modes are different. In this work **both degrees grow and their positive difference remains fixed**. The sharp gamma-interface law, the critical exponent \(1/(1-\beta)\), and the nonzero limiting trace norm require a separate uniform analysis of the coalescing transition region.

## Limitations

The asymptotics require a fixed positive integer degree gap and a fixed radial beta parameter \(0<\beta<1\). The theorem does not claim arbitrary varying degree gaps, parameters outside this interval, or general nonmonomial symbols. The infinite series in the upper regime need not have a simpler elementary closed form. Each individual commutator is finite rank. Primary-text comparison supports a best-knowledge novelty assessment but cannot rule out unindexed equivalent results or a future human assessment finding stronger existing coverage. Independent verification has not been performed.

## References

[1] P. Cui, Z. Huang, Y. Lu, and C. Zu, *Finite-rank and compact Toeplitz commutators on the harmonic Bergman space*, arXiv:2611.08988 (first posted 2026-11-06, updated 2026-11-18), Sections 1–4, https://arxiv.org/html/2611.08988.

[2] X.-T. Dong and Z.-H. Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213 (first posted 2014-11-02), Section 4 and Remark 4.8, https://arxiv.org/html/1411.0213v3.

[3] *A weighted two-degree spectral law for finite-rank harmonic Bergman Toeplitz commutators* (public research record, 2026-11-17), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-weighted-two-degree-spectral-law-for-finite-rank-harmonic-berg--e8a619449e4a.

[4] *A bulk–boundary Schatten transition for high-degree harmonic Bergman Toeplitz commutators* (public research record, 2026-11-17), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-bulk-boundary-schatten-transition-for-high-degree-harmonic-ber--5ef517e809cb.
