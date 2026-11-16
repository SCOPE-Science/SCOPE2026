# Unique maximin annulus and a sharp \(1/e\) radius law for finite Hermite-band Gaussian concentration

## Finding

Fix an annular phase-space area \(s>0\) and an integer \(K\ge 2\). Among all concentric annuli of area \(s\), there is a **unique** annulus maximizing the **least** fraction of Gaussian short-time Fourier transform (STFT) energy captured from any unit signal in the first \(K+1\) Hermite modes. Its inner squared-radius parameter \(a_K(s)>0\) is the unique root of

\[
\int_0^s e^{-t}(a_K(s)+t)^K\,dt=K!(1-e^{-s}).
\]

At this optimum the two and only two least-observable normalized modes are the Gaussian \(h_0\) and the highest allowed Hermite mode \(h_K\). The exact sharp lower concentration constant is

\[
M_K(s)=(1-e^{-s})e^{-a_K(s)},
\]

and the complete space of equality signals is \(\operatorname{span}\{h_0,h_K\}\setminus\{0\}\). For each fixed \(s>0\), define

\[
J_s=\int_0^s e^{(e-1)t}\,dt
=\frac{e^{(e-1)s}-1}{e-1}.
\]

The sharp bandwidth asymptotics are

\[
a_K(s)=\frac K e+\frac{\log(2\pi K)}{2e}
+\frac1e\log\!\left(\frac{1-e^{-s}}{J_s}\right)+o_s(1)
\quad(K\to\infty),
\]

and therefore

\[
M_K(s)\sim
(1-e^{-s})\left(\frac{J_s}{1-e^{-s}}\right)^{1/e}
(2\pi K)^{-1/(2e)}e^{-K/e}.
\]

The theorem optimizes **only over single concentric annuli of fixed area**, not arbitrary domains or unions of concentric rings. The space of admissible signals is a prescribed finite Hermite band, not the full infinitely dimensional signal space.

## Assumptions and scope

Set \(\phi(t)=2^{1/4}e^{-\pi t^2}\) and use the STFT convention

\[
V_\phi f(x,\omega)=\int_\mathbb R f(t)\overline{\phi(t-x)}e^{-2\pi i\omega t}\,dt.
\]

Let \((h_j)_{j\ge0}\) be the orthonormal Hermite basis of \(L^2(\mathbb R)\) with \(h_0=\phi\). For integer \(K\ge2\), write \(\mathcal H_K=\operatorname{span}\{h_0,\ldots,h_K\}\). For real \(s>0\) and \(a\ge0\), define the concentric circular annulus (a disk when \(a=0\))

\[
\Omega_{a,s}=\{(x,\omega)\in\mathbb R^2:
 a\le\pi(x^2+\omega^2)\le a+s\}.
\]

Its ordinary planar Lebesgue area is exactly \(s\). Define the sharp restricted lower concentration constant

\[
m_K(a,s)=\inf_{f\in\mathcal H_K\setminus\{0\}}
\frac{\int_{\Omega_{a,s}}|V_\phi f|^2\,dx\,d\omega}{\|f\|_2^2}.
\]

All statements concern the usual complex Hilbert space and the Lebesgue-area normalization above. At fixed \(K,s\), the optimum is over all \(a\in[0,\infty)\).

## Proof

**1. Exact diagonalization and the finite-band minimum.** The STFT of \(h_j\) with the Gaussian analysis window has squared magnitude

\[
|V_\phi h_j(x,\omega)|^2
=\frac{\left(\pi(x^2+\omega^2)\right)^j}{j!}
 e^{-\pi(x^2+\omega^2)}.
\]

The cross terms between distinct Hermite orders integrate to zero on any radial set by their different angular Fourier factors. Thus the restricted localization Gram operator is diagonal in the specified basis, with eigenvalues

\[
\lambda_j(a,s)=\frac1{j!}\int_a^{a+s}e^{-u}u^j\,du,
\qquad j=0,\ldots,K.
\]

Consequently, \(m_K(a,s)=\min_{0\le j\le K}\lambda_j(a,s)\). The expression and diagonalization are classical (see the references); the new work below concerns the sharp *lower* band edge and its global optimization in \(a\).

**2. Every intermediate mode is above the smaller endpoint.** Put \(p_j(u)=e^{-u}u^j/j!\). An integration by parts gives

\[
\lambda_{j+1}(a,s)-\lambda_j(a,s)
=p_{j+1}(a)-p_{j+1}(a+s).
\]

For \(a>0\), the sign of this difference is the sign of

\[
\frac{s}{\log(1+s/a)}-(j+1).
\]

The sign can change at most once as the index \(j\) increases, from nonnegative to nonpositive. Thus the finite sequence of eigenvalues rises, then falls (allowing at most one adjacent tie at the peak). Its minimum on indices \(0,\ldots,K\) is exactly

\[
m_K(a,s)=\min\{\lambda_0(a,s),\lambda_K(a,s)\}.
\]

For \(a=0\), the same identity follows because
\(\lambda_{j+1}(0,s)-\lambda_j(0,s)=-p_{j+1}(s)<0\).

**3. Unique endpoint balance.** One has \(\lambda_0(a,s)=e^{-a}(1-e^{-s})\) and

\[
\frac{\lambda_K(a,s)}{\lambda_0(a,s)}
=\frac{\int_0^s e^{-t}(a+t)^K\,dt}{K!(1-e^{-s})}.
\]

The numerator is continuous and strictly increasing in \(a\ge0\). At \(a=0\), the ratio is strictly below one because \(\lambda_K(0,s)=1-e^{-s}\sum_{j=0}^K s^j/j!<1-e^{-s}\). As \(a\to\infty\) the ratio diverges. There is therefore exactly one positive crossing \(a_K(s)\), with the displayed integral characterization. At the crossing the unimodal sequence has equal endpoint values and, because \(K\ge2\), all intermediate eigenvalues are *strictly larger*. The strictness uses the fact that the successive differences can have at most one zero and change sign only from positive to negative; an equal endpoint sequence of length at least three cannot have a repeated minimum at an interior index.

**4. The crossing is the unique global optimum.** Differentiating the eigenvalue integral with respect to the annulus translation \(a\), or using the identity above, yields

\[
\partial_a\lambda_K(a,s)=\lambda_{K-1}(a,s)-\lambda_K(a,s).
\]

At \(a=a_K(s)\) this derivative is strictly positive by the previous paragraph. Independently,

\[
\partial_a\lambda_K(a,s)=p_K(a+s)-p_K(a),
\]

which changes sign exactly once, from positive to negative, at \(a=s/(e^{s/K}-1)\). Hence \(\lambda_K\) is strictly increasing on \([0,a_K(s)]\). The function \(\lambda_0(a,s)=e^{-a}(1-e^{-s})\) is strictly decreasing for all \(a\ge0\). By the endpoint reduction, \(m_K=\lambda_K\) to the left of the crossing and \(m_K=\lambda_0\) to its right. This proves strict increase followed by strict decrease and establishes the unique global maximum, its exact value, and its two-dimensional bottom eigenspace.

**5. Sharp large-bandwidth law.** Fix \(s>0\), let \(a=a_K(s)\), and rewrite the endpoint-balance equation as

\[
\frac{a^K}{K!}\int_0^s e^{-t}\left(1+\frac{t}{a}\right)^K\,dt
=1-e^{-s}.
\]

For any fixed \(\alpha>0\), substituting \(a=\alpha K\) shows that the logarithm of the left side equals \(K(1+\log\alpha)+O_s(\log K)\), by Stirling's formula and boundedness of the short integral. Strict monotonicity then forces \(a_K(s)/K\to e^{-1}\). It follows, uniformly for \(t\in[0,s]\), that

\[
\left(1+\frac{t}{a_K(s)}\right)^K\longrightarrow e^{et},
\]

so the integral tends to \(J_s\). Taking logarithms of the balance identity and using

\[
\log K!=K\log K-K+\frac12\log(2\pi K)+o(1)
\]

therefore gives

\[
K\log(a_K(s))
=K\log K-K+\frac12\log(2\pi K)
+\log(1-e^{-s})-\log J_s+o_s(1).
\]

Writing \(a_K(s)=K/e+\delta_K\) first yields \(\delta_K=O_s(\log K)\), then expansion of \(K\log a_K(s)\) gives

\[
e\delta_K=\frac12\log(2\pi K)
+\log(1-e^{-s})-\log J_s+o_s(1).
\]

This is the asserted sharp radius expansion. Substituting into the exact expression for \(M_K(s)\) yields the stated asymptotic including its complete leading constant. No conclusion for \(s\) varying with \(K\) is claimed.

## Verification

The standalone program `check_annulus.py` uses only the Python standard library. It independently evaluates the radial gamma integrals with scaled Simpson quadrature, locates the balancing radius by bisection, checks that every intermediate Hermite mode lies strictly above the two worst modes, compares four off-optimal annuli for each sampled \(K,s\), checks unimodality for additional radii, and tests the sharp large-\(K\) correction.

Replay using `python3 check_annulus.py`. A successful run prints `FINITE_HERMITE_ANNULUS_PASS`. Its numerical cases are consistency checks; the infinite quantifiers, optimality, and asymptotics rest on the proof above.

## Relationship to prior work

Abreu and Speckbacher (2018) develop STFT concentration and recovery estimates using Hermite windows and local reproducing formulas. Knutsen (2019 preprint, 2020 journal) gives the relevant Gaussian Hermite diagonalization and studies largest eigenvalues on rings. Nicola and Tilli (2021 preprint, 2022 journal) establish the global **maximum** concentration inequality for Gaussian STFTs. Svela (2024) develops broad Daubechies-type diagonalization results. Nicola, Riccardi and Tilli (2025 preprint) identify the radial fixed-area annulus maximizing the **second largest** eigenvalue of the full Fock Toeplitz operator; it coincides with the \(K=1\) endpoint-balancing example, which is explicitly **not claimed as new here**.

The present theorem instead fixes a prescribed \((K+1)\)-dimensional Hermite subspace with \(K\ge2\), maximizes its **least** observable energy over annulus location, proves the exact two-mode minimizer and uniqueness for every \(K\), and determines a new large-\(K\) \(1/e\) radius and logarithmic correction. These statements are not furnished by a full-operator largest-eigenvalue estimate or a global second-eigenvalue theorem. General spectral diagonalization is a premise, not a claimed discovery.

## Limitations

The result is one-dimensional in the signal variable and uses the normalized Gaussian analysis window. It treats only circular concentric annuli with fixed area; it neither establishes optimality among all measurable sets of that area nor covers arbitrary unions of annular intervals, nonradial masks, varying area \(s=s(K)\), or other Hermite windows. Bibliographic priority remains provisional, especially regarding possible specialist finite-band concentration papers under sampling or observability terminology. An independent mathematical audit has not been performed.

## References

1. L. D. Abreu and M. Speckbacher, *Donoho–Logan large sieve principles for modulation and polyanalytic Fock spaces*, first available 2018-08-07, arXiv:1808.02258, https://arxiv.org/abs/1808.02258. Sections 1, 2.2 and 4.2.
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, first available 2019-07-01, arXiv:1907.00848; *Journal of Fourier Analysis and Applications* 26 (2020), article 47, https://doi.org/10.1007/s00041-020-09751-9. Sections 2.3, 3.1 and Appendix A.
3. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, first available 2021-06-07, arXiv:2106.03423, https://arxiv.org/abs/2106.03423. Theorem 1.1.
4. E. A. T. Svela, *Extensions of Daubechies' theorem: Reinhardt domains, Hagedorn wavepackets and mixed-state localization operators*, first available 2024-10-24, arXiv:2410.18769, https://arxiv.org/abs/2410.18769. Introduction and §3.
5. F. Nicola, F. Riccardi, and P. Tilli, *The Faber–Krahn inequality for partial sums of eigenvalues of Toeplitz operators*, first available 2025-03-10, arXiv:2503.07069, https://arxiv.org/abs/2503.07069. Theorem 1.3 and Remark 4.1.
