# Fourier-edge compact Fock compositions with a sharp Schatten threshold

## Finding
For every real \(0<\lambda<1\) and \(0<a<1\), put \(\beta=1-\lambda^2\) and define the entire functions
\[
g_a(z)=\int_0^1t^{-a}e^{itz}\,dt,\qquad
\psi_{\lambda,a}(z)=e^{\beta z^2/2}g_a(z).
\]
On the classical Gaussian Fock Hilbert space \(\mathcal F^2\), the weighted composition operator
\[
(W_{\lambda,a}f)(z)=\psi_{\lambda,a}(z)f(\lambda z)
\]
is compact. More sharply, for **every** \(0<p<\infty\), its membership in the Schatten class \(S_p\) has the exact threshold
\[
\boxed{W_{\lambda,a}\in S_p\ \Longleftrightarrow\ p>\frac1{1-a}.}
\]
In particular, \(W_{\lambda,a}\) is Hilbert--Schmidt precisely when \(0<a<\tfrac12\). In that range the **exact** squared Hilbert--Schmidt norm is
\[
\boxed{\|W_{\lambda,a}\|_{S_2}^2
=2\sqrt{\frac{\pi}{2\beta}}\int_0^1t^{-2a}e^{t^2/(2\beta)}\,dt.}
\]
To quantify the failure beyond the threshold, define the finite horizontal-window Hilbert--Schmidt integral
\[
H_{\lambda,a}(R)=\frac1\pi\int_{-R}^R\int_{\mathbb R}
|g_a(x+iy)|^2e^{-2\beta y^2}\,dy\,dx\qquad (R>0).
\]
For \(a=\tfrac12\),
\[
\boxed{H_{\lambda,1/2}(R)\sim
2\sqrt{\frac\pi{2\beta}}\log R,}
\]
and for \(\tfrac12<a<1\),
\[
\boxed{H_{\lambda,a}(R)\sim
\frac{2\Gamma(1-a)^2}{\pi(2a-1)}
\sqrt{\frac\pi{2\beta}}\,R^{2a-1}.}
\]
Thus the recent question whether compact weighted composition operators must be Hilbert--Schmidt already has a negative answer on the ordinary one-variable Gaussian Fock space. The theorem concerns this concrete two-parameter family, not every radial Fock space.

## Assumptions and scope
Use Lebesgue planar measure \(dA\), and normalize
\[
\mathcal F^2=\left\{f\text{ entire}:\|f\|^2
=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}.
\]
The functions \(e_n(z)=z^n/\sqrt{n!}\), for integers \(n\ge0\), form an orthonormal basis. We take \(\lambda\) positive real; no assertion is made for a complex dilation outside that range. The exponent \(p\) ranges over every positive real number, including the quasi-Schatten range. The horizontal window is a **spatial integral**, not a finite-rank spectral cutoff.

## Proof
**1. Entire symbols and square-integrability.** Since \(0<a<1\), the function \(t\mapsto t^{-a}\) is integrable on \((0,1)\). Termwise differentiation under the integral shows that \(g_a\) is entire; more precisely, every derivative is dominated locally by \(t^{k-a}e^{|\operatorname{Im}z|}\). For \(z=x+iy\),
\[
|g_a(x+iy)|\le\frac{e^{|y|}}{1-a}.
\]
Thus \(|\psi_{\lambda,a}(z)|^2e^{-|z|^2}\) is bounded by a constant times
\[
\exp\bigl(-\lambda^2x^2-(2-\lambda^2)y^2+2|y|\bigr),
\]
which is integrable; in particular \(\psi_{\lambda,a}\in\mathcal F^2\).

**2. Compactness, with no Schatten assumption.** The weighted kernel profile simplifies **exactly** to
\[
M(x+iy):=|\psi_{\lambda,a}(x+iy)|e^{-\beta|x+iy|^2/2}
=|g_a(x+iy)|e^{-\beta y^2}.
\]
It is bounded and vanishes at infinity. To see the latter, when \(|y|\to\infty\), the Gaussian \(e^{-\beta y^2}\) dominates the elementary \(e^{|y|}\) bound. On any strip \(|y|\le Y\), the compact family of \(L^1(0,1)\) functions \(t^{-a}e^{-ty}\) has Fourier transforms tending uniformly to zero as \(|x|\to\infty\), by the Riemann--Lebesgue lemma and finite-net approximation in \(L^1\). Hence \(M\in C_0(\mathbb C)\).

For any \(f\in\mathcal F^2\), change variables in the Fock norm to obtain
\[
\|W_{\lambda,a}f\|^2
=\frac1\pi\int_{\mathbb C}M(z)^2|f(\lambda z)|^2
 e^{-\lambda^2|z|^2}\,dA(z)
\le\lambda^{-2}\|M\|_\infty^2\|f\|^2.
\]
The same bound, restricted to \(|z|>R\), tends to zero in operator norm as \(R\to\infty\). On \(|z|\le R\), the map \(f\mapsto\mathbf1_{|z|\le R}\psi_{\lambda,a}(z)f(\lambda z)\) into the weighted planar \(L^2\) space is compact: bounded sets of Fock functions have uniformly bounded derivatives on compact sets by the reproducing kernel, and thus compactly convergent subsequences. Therefore \(W_{\lambda,a}\) is a norm limit of compact maps into weighted \(L^2\); since every output is entire and the Fock space is closed in that space, it is a compact operator \(\mathcal F^2\to\mathcal F^2\).

**3. Sharp Schatten threshold.** Dao Yuan Du's published Gaussian Fock Schatten criterion [2, Theorem 2.3], for a bounded weighted composition operator, states that membership in \(S_p\), for any \(p>0\), is equivalent to integrability of
\[
|\psi(z)|^p\exp\left(\frac p2\bigl(|\phi(z)|^2-|z|^2\bigr)\right).
\]
All its assumptions hold by steps 1--2, with \(\phi(z)=\lambda z\). Substitution gives precisely
\[
I_p=\int_{\mathbb R^2}|g_a(x+iy)|^p e^{-p\beta y^2}\,dx\,dy.
\]
We evaluate its convergence, rather than simply invoking the criterion as an answer. For fixed \(y\), the power singularity at \(t=0\) gives the uniform-on-bounded-strips Fourier asymptotic
\[
g_a(x+iy)=\Gamma(1-a)
\exp\left(\operatorname{sgn}(x)\frac{\pi i(1-a)}2\right)
|x|^{a-1}+O_Y(|x|^{-1}),\quad |y|\le Y,\ |x|\to\infty.
\]
Indeed, compare the integral with the classical oscillatory Mellin integral over \((0,\infty)\). Replacing \(e^{-ty}\) by one creates an integral whose integrand vanishes at \(t=0\) to order \(1-a>0\); one integration by parts gives the stated error, uniformly for bounded \(y\). The discarded tail \(t>1\) is \(O(|x|^{-1})\) by integration by parts in the oscillatory sense. An elementary split at \(t=|x|^{-1}\), followed by integration by parts on the remainder, also gives the global bound
\[
|g_a(x+iy)|\le C_a(1+|y|)e^{|y|}|x|^{a-1},\qquad |x|\ge1.
\]
The asymptotic supplies a positive lower bound of order \(|x|^{a-1}\) on every fixed finite strip for large \(|x|\), while the global bound is integrable in \(y\) against \(e^{-p\beta y^2}\) to the required power. Therefore
\[
I_p<\infty\quad\Longleftrightarrow\quad
\int_1^\infty x^{-p(1-a)}\,dx<\infty
\quad\Longleftrightarrow\quad p>\frac1{1-a}.
\]
At equality, the integral diverges logarithmically. This proves the full Schatten classification.

**4. Exact Hilbert--Schmidt norm.** The orthonormal basis and monotone convergence give the *identity of extended nonnegative quantities*
\[
\begin{aligned}
\|W_{\lambda,a}\|_{S_2}^2
&=\sum_{n=0}^\infty\frac1\pi\int_\mathbb C
|\psi_{\lambda,a}(z)|^2\frac{|\lambda z|^{2n}}{n!}e^{-|z|^2}\,dA(z)\\
&=\frac1\pi\int_{\mathbb R^2}|g_a(x+iy)|^2e^{-2\beta y^2}\,dx\,dy.
\end{aligned}
\]
If \(a<\tfrac12\), Plancherel with the convention \(\widehat h(x)=\int_\mathbb R h(t)e^{ixt}dt\) yields
\[
\int_{\mathbb R}|g_a(x+iy)|^2\,dx
=2\pi\int_0^1t^{-2a}e^{-2ty}\,dt.
\]
Tonelli and completion of the square evaluate the remaining Gaussian integral as
\[
\int_\mathbb R e^{-2\beta y^2-2ty}\,dy
=\sqrt{\frac\pi{2\beta}}\,e^{t^2/(2\beta)}.
\]
This proves the exact formula; for \(a\ge\tfrac12\), step 3 already shows divergence.

**5. Sharp divergence in horizontal windows.** The Fourier-edge asymptotic and the global Gaussian-dominated bound from step 3 imply, by dominated convergence in \(y\),
\[
\int_\mathbb R |g_a(x+iy)|^2e^{-2\beta y^2}\,dy
\sim \Gamma(1-a)^2\sqrt{\frac\pi{2\beta}}\,|x|^{2a-2}
\quad (|x|\to\infty).
\]
Integrating the two symmetric tails, using \(\Gamma(1/2)^2=\pi\), gives exactly the asserted logarithmic and power laws for \(H_{\lambda,a}(R)\). The finite interval in \(x\) has finite contribution for all \(a\in(0,1)\). All limiting operations are justified by the displayed integrable bounds.

## Verification
The proof is analytic and requires no finite enumeration. Its central identities are independently checkable from the normalizations given here: (i) the Fock basis identity \(\sum_{n\ge0}|\lambda z|^{2n}/n!=e^{\lambda^2|z|^2}\); (ii) the Gaussian identity after completing the square; (iii) the Fourier Mellin coefficient \(\Gamma(1-a)e^{\pm i\pi(1-a)/2}\); (iv) the two integrals \(\int_1^R x^{-1}dx=\log R\) and \(\int_1^R x^{2a-2}dx=(R^{2a-1}-1)/(2a-1)\). The cited Schatten criterion is applied only after boundedness and compactness have been proved directly. No numerical test is used as an infinite-dimensional proof.

## Relationship to prior work
Barik, Sen and Paul [1] proved general boundedness, compactness, and Hilbert--Schmidt criteria for radial weighted Fock spaces; their Section 7 Question 7.1 asks whether compactness forces Hilbert--Schmidt membership. Their Section 6 examples compare different radial weights but do not present a compact non-Hilbert--Schmidt example on the Gaussian Fock space. The construction above supplies a negative answer within the classical case, with a full Schatten membership threshold and exact logarithmic/power divergence constants.

Du [2, Theorem 2.3] had already given the general Gaussian Fock Schatten test; it is a *prior premise*, and the present theorem is not a new general test. The nontrivial additional work is the explicitly entire Fourier-edge weight, the compactness proof, the exact threshold and quantified critical growth. Mengestie and Takele [3] provide related integral/Schatten criteria for other Fock-type weights, not the stated explicit phase diagram. Other classical weighted-composition and Fourier constructions may conceivably imply an equivalent example; publication priority has not been independently determined.

## Limitations
The negative answer is established for \(m=2\), \(\alpha=1\) and the particular positive-real dilation and Fourier-edge family. It does not decide the corresponding compact-versus-Hilbert--Schmidt implication separately at every other \(m>0\), does not identify the actual singular-value asymptotics, and does not establish optimality among all possible weights. \(H_{\lambda,a}(R)\) is a spatially truncated integral, **not** a Schatten partial sum, so its divergence must not be interpreted as a singular-value counting law. The use of the earlier general Schatten theorem is explicitly acknowledged. Independent validation and independent publication-priority certification have not been performed.

## References
[1] S. Barik, A. Sen, K. Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170, first public July 19, 2026, especially Theorems 1.1--1.4, Section 6 and Question 7.1. https://arxiv.org/abs/2607.17170

[2] D. Y. Du, *Schatten Class Weighted Composition Operators on the Fock Space*, International Journal of Mathematical Analysis **5** (2011), 625--630, especially Theorem 2.3. https://www.m-hikari.com/ijma/ijma-2011/ijma-13-16-2011/duIJMA13-16-2011.pdf

[3] T. Mengestie and M. H. Takele, *Integral and Weighted Composition Operators on Fock-type Spaces* (2023), especially Schatten-integrability criteria for generalized Fock-type weights. https://doi.org/10.1007/s40840-023-01476-4 The weights and detailed asymptotics considered here are distinct.
