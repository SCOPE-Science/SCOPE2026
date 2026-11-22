# Universal Hilbert–Schmidt-to-trace-class gain for Fock Hausdorff annihilation commutators

## Finding

Positive Hausdorff mixtures of radial dilations on the Gaussian Fock space possess a sharp hierarchy of iterated commutators with the annihilation operator. The first commutator is universally Hilbert–Schmidt; every commutator from the second onward is universally trace class, irrespective of the distribution of dilation mass near the identity. The uniform constants, the trace-class criterion for the first commutator, and the optimality of both universal ideal endpoints are explicit.

Let \(\rho\) be a finite positive Borel measure on \((0,1]\), with \(M=\rho((0,1])\), and let
\[
(H_\rho f)(z)=\int_{(0,1]} f(sz)\,d\rho(s),\qquad Df=f'.
\]
For integers \(k\ge1\), initially on polynomials define \(B_1=[D,H_\rho]\) and \(B_{k+1}=[D,B_k]\), where \([A,B]=AB-BA\). Each \(B_k\) has a unique bounded extension. With \(e_n(z)=z^n/\sqrt{n!}\), its exact action is
\[
B_k e_{j+k}=(-1)^k\sqrt{\frac{(j+k)!}{j!}}\left(\int_{(0,1]}s^j(1-s)^k\,d\rho(s)\right)e_j,\quad j\ge0,
\]
and \(B_k e_n=0\) for \(0\le n<k\). Thus the nonzero singular values, with multiplicity but not necessarily in decreasing index order, are the displayed positive weights.

The first commutator obeys the exact identity and sharp bound
\[
\boxed{\ \|B_1\|_{\mathcal S_2}^2=
\iint_{(0,1)^2}\frac{(1-s)(1-t)}{(1-st)^2}\,d\rho(s)\,d\rho(t)\ \le M^2.\ }
\]
An atom at \(s=1\) makes no contribution. Its trace-class membership is characterized precisely by
\[
\boxed{\ B_1\in\mathcal S_1\quad\Longleftrightarrow\quad
\int_{(0,1)}(1-s)^{-1/2}\,d\rho(s)<\infty.\ }
\]
For every integer \(k\ge2\),
\[
\boxed{\ B_k\in\mathcal S_1,\qquad \|B_k\|_{\mathcal S_1}\le\sqrt{k!}\,M.\ }
\]
The coefficients \(1\) in the Hilbert–Schmidt bound and \(\sqrt{k!}\) in each trace norm bound are the best possible over finite positive measures: unit point masses at \(s\downarrow0\) approach equality.

Both universal ideal thresholds are optimal. In particular, for the probability measures
\[
d\rho_\alpha(s)=\alpha(1-s)^{\alpha-1}\,ds,\qquad 0<s<1,\quad \alpha>0,
\]
the singular values are strictly decreasing in their natural order and, for every integer \(k\ge1\), satisfy
\[
\boxed{\ s_{j+1}(B_k)=\alpha\Gamma(\alpha+k)
\sqrt{\frac{(j+k)!}{j!}}\frac{\Gamma(j+1)}{\Gamma(j+\alpha+k+1)}
\sim \alpha\Gamma(\alpha+k)\,j^{-\alpha-k/2}.\ }
\]
Consequently \(B_k\in\mathcal S_p\) exactly when \(p>1/(\alpha+k/2)\). For each \(p<2\), some positive \(\rho\) gives \(B_1\notin\mathcal S_p\); for each \(p<1\), some positive \(\rho\) gives \(B_2\notin\mathcal S_p\).

## Assumptions and scope

Use the standard one-variable Gaussian Fock space
\[
\mathcal F^2=\left\{f\text{ entire}:\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}
\]
with its usual Hilbert norm. The monomials \(e_n=z^n/\sqrt{n!}\), \(n\ge0\), are an orthonormal basis. The densely defined operator \(D=d/dz\) has polynomial core and acts by \(De_n=\sqrt n\,e_{n-1}\) for \(n\ge1\), \(De_0=0\). No assertion is made about a bounded extension of \(D\) itself.

The measure \(\rho\) is nonnegative, finite, and supported on \((0,1]\); it may have an atom at one and need not have a density. This is the standard positive Fock Hausdorff class: if \(\mu\) is a positive Borel measure on \([1,\infty)\) with \(\int_{[1,\infty)}t^{-1}d\mu(t)<\infty\), then pushing \(t^{-1}d\mu(t)\) forward under \(s=1/t\) gives \(\rho\), and
\[
(H_\rho f)(z)=\int_{[1,\infty)}t^{-1}f(z/t)\,d\mu(t).
\]
Conversely every such \(\rho\) corresponds to a positive \(\mu\) under this change of variables. The statement is not extended to arbitrary signed or complex measures for the exact trace-class iff criterion. All sums use nonnegative summands, so Tonelli's theorem applies.

Here \(\mathcal S_p\) denotes the singular-value Schatten ideal for \(p>0\); \(\mathcal S_2\) and \(\mathcal S_1\) are respectively the Hilbert–Schmidt and trace ideals. The criterion for \(B_1\) integrates only over \((0,1)\); any atom at \(s=1\) is annihilated by commutation.

## Proof

**1. Exact commutator and singular-value system.** Each radial dilation \(C_s f(z)=f(sz)\) is a contraction for \(0<s\le1\), with \(C_se_n=s^ne_n\). Because \(\rho\) is finite, \(H_\rho=\int C_s\,d\rho(s)\) is bounded, diagonal and positive. Induction using \(De_n=\sqrt n\,e_{n-1}\) gives
\[
\operatorname{ad}_D^k(C_s)e_{j+k}=(-1)^k\sqrt{(j+k)!/j!}\,(1-s)^ks^j e_j.
\]
The induction is an identity on the common polynomial core; integrating a finite sum is legitimate. Thus the stated formula follows. The images of distinct basis vectors \(e_{j+k}\) are orthogonal, so the displayed coefficients, in absolute value, comprise the complete nonzero singular-value multiset whenever the extension is compact. The estimates below prove this compactness.

**2. Sharp first Hilbert–Schmidt bound.** For \(k=1\), the squares of the coefficients are \((j+1)[\int_{(0,1)}(1-s)s^j\,d\rho(s)]^2\). By Tonelli,
\[
\sum_{j=0}^\infty(j+1)\iint (1-s)(1-t)(st)^j\,d\rho(s)d\rho(t)
=\iint_{(0,1)^2}\frac{(1-s)(1-t)}{(1-st)^2}\,d\rho(s)d\rho(t).
\]
The restriction to \((0,1)^2\) disposes of the harmless atom at \(s=1\). For \(0<s,t<1\), \(1-st\ge\max\{1-s,1-t\}\ge\sqrt{(1-s)(1-t)}\), hence the kernel is at most one. Therefore \(\|B_1\|_2\le M\). A unit atom \(\rho=\delta_s\) has
\[
\|B_1\|_2=(1-s)\left(\sum_{j\ge0}(j+1)s^{2j}\right)^{1/2}=\frac1{1+s},
\]
which tends to one as \(s\downarrow0\). This also proves sharpness without positing an actual point mass at excluded \(s=0\).

**3. Exact trace-class boundary at first order.** The trace norm of this one-step backward weighted shift is the sum of its nonnegative weights, so
\[
\|B_1\|_1=\int_{(0,1)}(1-s)\sum_{j\ge0}\sqrt{j+1}\,s^j\,d\rho(s),
\]
allowing \(+\infty\). Set \(\Phi(s)=(1-s)\sum_{j\ge0}\sqrt{j+1}s^j\). The sum is continuous and positive away from one. Standard integral comparison (or Riemann sums with \(s=e^{-h}\), \(h\downarrow0\)) yields
\[
\lim_{s\uparrow1}\sqrt{1-s}\,\Phi(s)=\Gamma(3/2)=\frac{\sqrt\pi}{2}.
\]
Indeed \(h^{3/2}\sum_{j\ge0}\sqrt{j+1}\,e^{-hj}\to\int_0^\infty u^{1/2}e^{-u}du\), and \((1-e^{-h})/h\to1\). Thus \(\Phi(s)\) is comparable to \((1-s)^{-1/2}\) over \((0,1)\). Tonelli gives the exact iff criterion. An atom at one yields zero, not an infinite contribution.

**4. Uniform trace-class regularization at all higher orders.** For \(k\ge2\) and \(j\ge0\),
\[
\sqrt{\frac{(j+k)!}{j!}}\le\sqrt{k!}\binom{j+k-1}{k-1}.
\]
At \(j=0\) this is equality. If true at \(j\), the ratio of successive left sides is \(\sqrt{(j+k+1)/(j+1)}\) and that of the binomial right sides is \((j+k)/(j+1)\). The required ratio inequality follows from
\[
(j+k)^2-(j+k+1)(j+1)=(k-2)j+k^2-k-1>0
\]
for every integer \(k\ge2\), \(j\ge0\). Consequently, by Tonelli and the negative-binomial identity,
\[
\begin{aligned}
\|B_k\|_1&=\int_{(0,1)}(1-s)^k\sum_{j\ge0}\sqrt{\frac{(j+k)!}{j!}}s^j\,d\rho(s)\\
&\le\sqrt{k!}\int_{(0,1)}(1-s)^k\sum_{j\ge0}\binom{j+k-1}{k-1}s^j\,d\rho(s)\\
&=\sqrt{k!}\,\rho((0,1))\le\sqrt{k!}M.
\end{aligned}
\]
The atom at \(s=1\) gives no commutator. Dominated convergence in the displayed scalar integrand shows that \(\rho=\delta_s\) with \(s\downarrow0\) makes \(\|B_k\|_1\to\sqrt{k!}\). In particular, every \(B_k\) is trace class, hence compact and bounded; the earlier first-order Hilbert–Schmidt bound establishes the same extension property for \(B_1\).

**5. Sharpness of the ideal endpoints.** For \(d\rho_\alpha=\alpha(1-s)^{\alpha-1}ds\), direct beta integration gives
\[
\int_0^1s^j(1-s)^k\,d\rho_\alpha(s)
=\alpha\frac{\Gamma(j+1)\Gamma(\alpha+k)}{\Gamma(j+\alpha+k+1)}.
\]
The ratio of consecutive nonzero singular weights is
\[
\frac{\beta_{j+1,k}}{\beta_{j,k}}
=\frac{\sqrt{(j+1)(j+k+1)}}{j+\alpha+k+1}<1,
\]
so these weights are already in decreasing singular-value order. Applying the gamma-ratio asymptotic \(\Gamma(j+a)/\Gamma(j+b)\sim j^{a-b}\) yields
\[
s_{j+1}(B_k)\sim\alpha\Gamma(\alpha+k)j^{-\alpha-k/2}.
\]
The positive sequence is in \(\ell^p\) exactly for \(p(\alpha+k/2)>1\). For any proposed improvement \(p<2\) of the universal first-order Hilbert–Schmidt conclusion, choose \(0<\alpha\le1/p-1/2\). For any proposed improvement \(p<1\) of the universal second-order trace conclusion, choose \(0<\alpha\le1/p-1\). The respective \(\mathcal S_p\) membership then fails. These are strict endpoint failures, not numerical extrapolations.

## Verification

The standalone finite-arithmetic checker `checker.py` reproduces the polynomial-core commutator formula with rational atomic measures, including an atom at \(s=1\), and with beta measures of integer shape. It also compares the exact Hilbert–Schmidt integral identity to long finite singular-weight sums, tests the higher-order trace bounds on a finite atomic mixture, and checks gamma-ratio asymptotics. In the packaged execution it passed 2704 exact-rational matrix-entry assertions and supplementary numerical checks. No finite test is offered as a replacement for the infinite-series, Tonelli or gamma-ratio arguments above.

Reproduction with Python 3: `python checker.py`. The checker uses only Python's standard library. Every claim is also proved in the preceding section; no external code or numerical certificate is a premise of the theorem.

## Relationship to prior work

Galanopoulos and Stylogiannis (arXiv:2008.06684, first public 15 August 2020) identify Fock Hausdorff operators with coefficient multipliers and characterize Schatten membership of the original multipliers. Blasco and Galbis (arXiv:2310.01059, first public 2 October 2023) develop their boundedness, compactness and summing behavior. These results supply the standard operator family and moment representation but do not state the annihilation-commutator trace-ideal hierarchy, its sharp measure-uniform constants, or the first-commutator trace criterion.

Alpay, Cerejeiras, Kähler and Kling (arXiv:2208.03394, first public 5 August 2022) develop an algebra of weighted-shift commutators in Fock-type spaces. Their shift algebra is related to the elementary core calculation here, but their studied commutators are different and the inspected source does not supply the moment-measure uniform Hilbert–Schmidt-to-trace-class bounds. None of the three sources is claimed to exclude all earlier spectral or moment theory; in particular, equivalent formulations through completely monotone sequences and general weighted-shift ideals are a priority risk.

## Limitations

The trace-class iff condition uses positivity of the measure; cancellation for signed or complex measures can change it. The proof is for one-variable Gaussian Fock space with the standard annihilation operator. General weighted Fock spaces, higher dimensions and unbounded Hausdorff measures outside the integrability assumption are not covered. The result is a self-review, not an independently validated publication or a proof of global historical priority. The numerical checker verifies finite identities and approximations only.

## References

- P. Galanopoulos and G. Stylogiannis, *Hausdorff operators on Fock spaces*, arXiv:2008.06684, initial posting 15 August 2020. https://arxiv.org/abs/2008.06684
- Ó. Blasco and A. Galbis, *Boundedness and compactness of Hausdorff operators on Fock spaces*, arXiv:2310.01059, initial posting 2 October 2023. https://arxiv.org/abs/2310.01059
- D. Alpay, P. Cerejeiras, U. Kähler and T. Kling, *Commutators on Fock spaces*, arXiv:2208.03394, initial posting 5 August 2022. https://arxiv.org/abs/2208.03394
