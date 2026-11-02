# A nonconstant log-periodic Gaussian localization profile for Cantor annuli

## Finding

Let \(C_n(A)\) be the \(n\)-th middle-third Cantor prefractal inside \([0,A]\), retaining the left and right thirds at each step, and let \(P_{n,A}\) be Daubechies' Gaussian-window time-frequency localization operator on
\[
\Omega_{n,A}=\{(x,\omega)\in\mathbb R^2:\pi(x^2+\omega^2)\in C_n(A)\}.
\]
Write \(\lambda_0(n,A)\) for its normalized Gaussian (zeroth Hermite) Rayleigh eigenvalue, \(\delta=\log 2/\log 3\), and
\[
K(t)=\prod_{k=0}^{\infty}(1+e^{-2t3^k})
\prod_{r=1}^{\infty}\frac{1+e^{-2t/3^r}}2,\qquad
H(t)=t^\delta K(t),\quad t>0.
\]
The products converge to strictly positive values. The function \(H\) is continuously differentiable, positive, **nonconstant**, and exactly multiplicatively periodic: \(H(3t)=H(t)\) for every \(t>0\).

For every pair of positive integers \(n\) and real \(A\ge1\) with \(A<3^n\), put \(h=A/3^n\). Then the following explicit two-sided remainder estimate holds:
\[
\exp[-\eta(A,n)]\le
\frac{\lambda_0(n,A)}{(2/3)^n A^{1-\delta}H(A)}
\le\exp[\eta(A,n)],\qquad
\eta(A,n)=\frac{3A}{2\,3^n}+\frac{e^{-2A}}{1-e^{-4A}}.
\]
Consequently, for every sequence with \(A\to\infty\) and \(A/3^n\to0\),
\[
\lambda_0(n,A)=(2/3)^n A^{1-\delta}H(A)(1+o(1)),
\]
with a nonvanishing log-periodic phase factor. In particular, there is **no constant** \(c\) such that this Gaussian eigenvalue is asymptotic to \(c(2/3)^n A^{1-\delta}\) simultaneously for all such sequences. Equivalently, for any fixed \(t>0\),
\[
\lim_{m\to\infty}(3/2)^m\lambda_0(2m,t3^m)=tK(t).
\]
The assertion concerns the Gaussian eigenvalue, **not** the full operator norm.

## Assumptions and scope

The short-time Fourier transform uses the unit vector \(\phi(u)=2^{1/4}e^{-\pi u^2}\) and the convention
\[
V_\phi f(\omega,x)=\int_{\mathbb R}f(u)\overline{\phi(u-x)}e^{-2\pi i\omega u}\,du.
\]
The positive compact localization operator is \(P_{n,A}=V_\phi^*\mathbf1_{\Omega_{n,A}}V_\phi\). The Cantor set is explicitly
\[
C_n(A)=\bigcup_{\epsilon_j\in\{0,2\}}
\left[A\sum_{j=1}^n\epsilon_j3^{-j},\ A\sum_{j=1}^n\epsilon_j3^{-j}+A3^{-n}\right].
\]
Endpoints of the intervals have no effect. The exact base and alphabet are part of the theorem. No assertion is made for other alphabets, non-Gaussian windows, or complex-dimension extensions. The normalization makes the zeroth Hermite eigenvalue \(\lambda_0(n,A)=\int_{C_n(A)}e^{-s}\,ds\).

## Proof

**1. Exact product and scale separation.** Radial diagonalization of the Gaussian localization operator gives the zeroth eigenvalue displayed above (see references). Integrating \(e^{-s}\) over the disjoint Cantor intervals, or decomposing a point into independent ternary digits and an interval remainder, yields the exact identity
\[
\lambda_0(n,A)=(1-e^{-A/3^n})\prod_{j=1}^{n}(1+e^{-2A/3^j}). \tag{1}
\]
This finite product is already known; the new claim is its explicit **nonconstant leading oscillation and uniform remainder** in the simultaneous large-scale, deep-iteration regime.

Write \(A=t3^m\) with the unique integer \(m=\lfloor\log_3A\rfloor\) and \(1\le t<3\). The assumption \(A<3^n\) implies \(m<n\). Split the product at \(j=m\):
\[
\lambda_0(n,A)=h\,\frac{1-e^{-h}}h\,2^{n-m}P_m(t)Q_{n-m}(t),
\]
where
\[
P_m(t)=\prod_{k=0}^{m-1}(1+e^{-2t3^k}),\qquad
Q_{n-m}(t)=\prod_{r=1}^{n-m}\frac{1+e^{-2t/3^r}}2.
\]
The infinite products \(P_\infty(t)\) and \(Q_\infty(t)\) converge uniformly on each compact subinterval of \((0,\infty)\), since their logarithmic tails are dominated respectively by \(e^{-2t3^k}\) and \(t3^{-r}\). Their product is \(K(t)>0\).

**2. Normalization and sharp remainder.** Because \(3^\delta=2\), a direct calculation gives
\[
h2^{n-m}K(t)=(2/3)^n A^{1-\delta}H(t).
\]
Also
\[
0\le-\log\frac{1-e^{-h}}h\le h,
\quad 0\le\log\frac{P_\infty(t)}{P_m(t)}
\le\frac{e^{-2A}}{1-e^{-4A}},
\quad 0\le\log\frac{Q_{n-m}(t)}{Q_\infty(t)}\le\frac h2.
\]
The first bound follows by writing \((1-e^{-h})/h=\int_0^1e^{-hu}\,du\). The second follows from \(\log(1+v)\le v\) and the fact that consecutive omitted exponents increase at least by \(4A\). The third follows from \(e^{-u}\le(1+e^{-2u})/2\le1\) and summing a geometric series in \(u=t3^{-r}\). Taking logarithms gives the stated two-sided remainder with \(\eta(A,n)\). As \(A\to\infty\) and \(h\to0\), the error tends to zero.

**3. Exact periodicity.** Shifting indices in the absolutely convergent products gives \(K(3t)=K(t)/2\). Thus \(H(3t)=3^\delta H(t)/2=H(t)\), and \(H(A)=H(t)\) for \(A=t3^m\). Termwise differentiation of the locally normally convergent logarithmic products gives
\[
\frac{d\log H(t)}{d\log t}=\delta-
\sum_{k\in\mathbb Z}\frac{2t3^k}{1+e^{2t3^k}}. \tag{2}
\]
This series converges absolutely and locally uniformly, including its first derivative.

**4. Rigorous nonconstancy.** At \(t=1\), retain only the eight positive terms indexed by \(-6\le k\le1\) in (2). They satisfy
\[
\sum_{k=-6}^{1}\frac{2\,3^k}{1+e^{2\,3^k}}>\frac{631}{1000}>
\frac{\log2}{\log3}=\delta. \tag{3}
\]
For a reproducible *exact-rational* verification of the first strict inequality, use \(x_k=2\,3^k\) and, for each \(0<x_k\le6\), the rational exponential upper bound
\[
U_{36}(x)=\sum_{j=0}^{36}\frac{x^j}{j!}
+\frac{x^{37}}{37!}\frac1{1-x/38}.
\]
Indeed \(e^x\le U_{36}(x)\) by a geometric bound on the positive Taylor tail. Replacing each denominator \(1+e^{x_k}\) by \(1+U_{36}(x_k)\), exact fraction arithmetic still yields a sum greater than \(631/1000\). The second strict inequality in (3) is the elementary integer inequality \(2^{1000}<3^{631}\). The included standalone checker executes these rational comparisons without trusting floating-point output. Therefore the logarithmic derivative at \(t=1\) is strictly negative: \(H\) cannot be constant. Taking \(n=2m\) and \(A=t3^m\) for two fixed values of \(t\) with different \(H(t)\) proves the absence of a phase-independent leading constant.

## Verification

Run `python3 CHECK.py` from the directory containing that complete file. It establishes the exact-rational inequality (3), tests the finite ternary-digit integral against (1) for multiple small iterates, tests the quantitative finite-size remainder, and checks numerical approximations of \(H(3t)=H(t)\). The last checks are diagnostics only; the infinite assertion and uniform error are proved above. A recorded successful execution is in `CHECK_OUTPUT.txt`.

## Relationship to prior work

Knutsen's 2019 preprint and 2020 article derive radial Hermite diagonalization, the exact finite Cantor product (1), and operator-norm estimates **up to multiplicative constants**. Knutsen's 2021 sequel treats general bases and alphabets, including comparable asymptotics and in certain configurations Gaussian extremizers. Abreu, Mouayn, and Voigtlaender's 2022 preprint concerns the distinct hyperbolic Bergman/analytic-wavelet realization and likewise gives norm estimates at the order-of-magnitude scale. In those inspected texts the present exact periodic leading profile, nonconstancy, and remainder for the middle-third Gaussian eigenvalue are not stated. The present result is specifically a refinement of a known exact product, not a claim to have discovered its diagonalization or finite-n value.

## Limitations

The known estimate \(\lambda_0\le\|P_{n,A}\|\le2\lambda_0\) does not identify the operator norm. It is **not proved** that the operator norm inherits the same oscillatory factor or that the Gaussian is always extremal. The result does not improve the power-law exponent for the norm, does not determine other Hermite eigenvalues, and gives no independent priority certification. Periodic scaling is a classical phenomenon in self-similar Laplace transforms, so an equivalent general theorem in older fractal-asymptotic literature remains a concrete priority risk. The phase modulation is small but rigorously nonzero; no claim of optimal experimental significance is made.

## References

1. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, arXiv:1907.00848, first posted 2019-07-01. Published as *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, J. Fourier Anal. Appl. **26**, 47 (2020), DOI: 10.1007/s00041-020-09751-9. Full article: https://link.springer.com/article/10.1007/s00041-020-09751-9 .
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets II*, arXiv:2104.10976, first posted 2021-04-22. https://arxiv.org/abs/2104.10976 .
3. L. D. Abreu, Z. Mouayn, F. Voigtlaender, *A fractal uncertainty principle for Bergman spaces and analytic wavelets*, arXiv:2201.11705, first posted 2022-01-27. https://arxiv.org/abs/2201.11705 .
4. I. Daubechies, *Time-frequency localization operators: A geometric phase space approach*, IEEE Trans. Inf. Theory **34** (1988), 605–612.
