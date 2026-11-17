# Almost-periodic homogenization and sharp spectral profiles of compact Aluthge shifts

## Finding

Fix \(0<t<1\), \(\beta>0\), and a real uniformly Bohr-almost-periodic sequence \(f:\mathbb Z\to\mathbb R\), with Bohr mean \(m\). On \(\ell^2(\mathbb N_0)\), let \(W e_j=w_j e_{j+1}\) with positive weights
\[
w_j=(j+1)^{-\beta}\exp(f(j)),\qquad j\ge0.
\]
Write \(W_n=\Delta_t^n(W)\), \(C=e^m\), \(S_n\sim\operatorname{Bin}(n,t)\), and
\[
\delta_n=\sup_{j\ge0}\left|\mathbb E f(j+S_n)-m\right|.
\]
Then \(\delta_n\to0\). In particular, for every \(n\ge1\) and \(j\ge0\), with \(D_{n,j}=j+nt+1\), the actual positive weight \(w_j^{(n)}\) satisfies the **uniform all-index expansion**
\[
\log w_j^{(n)}
=m-\beta\log D_{n,j}
+\frac{\beta nt(1-t)}{2D_{n,j}^{2}}
+O_{\beta,t}(n^{-2})+\varepsilon_{n,j},
\qquad |\varepsilon_{n,j}|\le\delta_n.
\]
The remainder is uniform for all \(j\ge0\); its implicit constant does not depend on \(f\). Consequently, for some \(K_{\beta,t}\), simultaneously for **every** rank \(j\ge0\),
\[
 e^{-\delta_n-K_{\beta,t}/n}\,C D_{n,j}^{-\beta}
\le s_{j+1}(W_n)
\le e^{\delta_n+K_{\beta,t}/n}\,C D_{n,j}^{-\beta}.
\]
Thus \(\|W_n\|\sim C t^{-\beta}n^{-\beta}\), and, for every \(p>0\) with \(\beta p>1\),
\[
\|W_n\|_{\mathcal S_p}^{p}
\sim\frac{C^p t^{1-\beta p}}{\beta p-1}n^{1-\beta p},\qquad
\frac{\|W_n\|_{\mathcal S_p}^{p}}{\|W_n\|^p}
\sim\frac{tn}{\beta p-1}.
\]
For \(0<\theta<1\), the normalized singular-value count satisfies
\[
\frac1n\#\{j\ge1:s_j(W_n)>\theta\|W_n\|\}
\longrightarrow t\big(\theta^{-1/\beta}-1\big).
\]
The same all-index envelope applies to nonperiodic quasiperiodic modulations, which generally are not regularly varying. There is no polynomial convergence rate uniformly over this class: indeed **one fixed** real uniformly almost-periodic \(f\) exists for which, for every \(a>0\),
\[
\left|\frac{n^{\beta}\|W_n\|}{C t^{-\beta}}-1\right|
\ne O(n^{-a}).
\]
For each finite \(n\), \(W_n\in\mathcal S_p\) if and only if \(\beta p>1\).

## Assumptions and scope

The Hilbert space is complex and separable. Uniform Bohr almost periodicity means uniform approximation on \(\mathbb Z\) by finite trigonometric polynomials \(\sum_{r=1}^R a_r e^{i\theta_r j}\). The Bohr mean retains only the constant frequency. The strict positivity of the weights makes every logarithm well-defined. Parameters \(t\) and \(\beta\) are fixed, and constants may depend on them. The singular values are indexed from one. No smoothness, periodicity, or eventual monotonicity of \(f\) is assumed.

## Proof

**Exact Aluthge reduction.** For a strictly positive unilateral weighted shift, its generalized Aluthge transform has weights \(w_j^{1-t}w_{j+1}^{t}\). Iteration gives the already known binomial identity
\[
\log w_j^{(n)}=\mathbb E\log w_{j+S_n}
=-\beta\mathbb E\log(j+S_n+1)+\mathbb E f(j+S_n).
\]
This identity is not claimed as new.

**Uniform almost-periodic mixing.** The averaging operator \(P_tg(j)=(1-t)g(j)+tg(j+1)\) acts on a Fourier mode \(e^{i\theta j}\) by multiplication by \(1-t+t e^{i\theta}\). Every nonconstant mode has multiplier of modulus strictly less than one. Therefore \(P_t^nf\) tends uniformly to the Bohr mean \(m\) for trigonometric polynomials. The operators \(P_t^n\) have sup-norm at most one. Uniform approximation of \(f\) by trigonometric polynomials extends the conclusion to all uniformly almost-periodic \(f\), proving \(\delta_n\to0\).

**Uniform logarithmic expansion.** Put \(D=j+nt+1\), \(X=S_n-nt\), and \(\sigma^2=nt(1-t)\). On \(|X|\le nt/2\), Taylor's theorem gives \(\log(D+X)=\log D+X/D-X^2/(2D^2)+X^3/(3D^3)+O(|X|^4/D^4)\), with an error uniform in \(j\ge0\) because \(D\ge nt\). Binomial moments satisfy \(\mathbb EX=0\), \(\mathbb EX^2=\sigma^2\), \(\mathbb EX^3=O_t(n)\), and \(\mathbb EX^4=O_t(n^2)\). The omitted event has exponentially small probability, and \(\log(j+S_n+1)\), compared with \(\log D\), grows no faster than \(O_t(\log(n+1))\) there, uniformly in \(j\). Consequently
\[
\mathbb E\log(j+S_n+1)
=\log D-\frac{nt(1-t)}{2D^2}+O_t(n^{-2})
\]
uniformly for all \(j\ge0\). This proves the weight expansion.

**Ordered spectrum and Schatten asymptotics.** Each singular value of a weighted unilateral shift is an absolute weight, arranged decreasingly. A coordinatewise multiplicative comparison with the decreasing sequence \(C(j+nt+1)^{-\beta}\) remains valid after decreasing rearrangement; this proves the global spectral envelope. Integral comparison gives
\[
\sum_{j\ge0}(j+nt+1)^{-\beta p}
\sim\frac{(nt)^{1-\beta p}}{\beta p-1}
\]
when \(\beta p>1\). The global envelope transfers this to the Schatten sum and yields the operator norm. The counting formula follows by solving \(((nt+1)/(j+nt+1))^\beta>\theta\) and controlling multiplicative errors \(e^{\pm\delta_n+O(1/n)}\). Since \(\exp(f(j))\) stays between two positive constants and each binomial logarithmic average preserves the polynomial tail order for finite \(n\), Schatten membership is exactly equivalent to \(\beta p>1\).

**A fixed example with arbitrarily slow polynomial comparison.** Define on all integers
\[
f(j)=\sum_{k=1}^{\infty}2^{-k}\cos(2\pi\alpha_kj),
\qquad \alpha_k=2^{-4^k},
\]
a uniformly convergent almost-periodic series of Bohr mean \(m=0\). Put \(n_k=2^{3\cdot4^{k-1}}\) for \(k\ge2\). For frequencies with index less than \(k\), the binomial multipliers decay like \(\exp(-c_t n_k\alpha_{k-1}^2)\), hence vanish; for frequencies with index at least \(k\), their phases remain uniformly near zero since \(n_k\alpha_k=2^{-4^{k-1}}\to0\). Therefore
\[
(P_t^{n_k}f)(0)=(1+o(1))\sum_{\ell\ge k}2^{-\ell}
=(1+o(1))2^{1-k}.
\]
The uniform logarithmic expansion at \(j=0\) implies
\[
\frac{n_k^{\beta}\|W_{n_k}\|}{t^{-\beta}}
\ge1+(1+o(1))2^{1-k}.
\]
Because \(n_k\) grows superexponentially in \(k\), the normalized norm error cannot be \(O(n^{-a})\) for any \(a>0\). This shows why a quantitative mixing hypothesis is essential for rates, although the universal spectral law remains valid.

## Verification

The accompanying standalone `CHECK.py` replays the exact binomial weighted-shift formula on a nonconstant three-periodic modulation and an irrational-frequency modulation. It checks the coordinatewise logarithmic expansion, the decay of Fourier modes, and multiplicative spectral envelopes for finite parameter samples. These diagnostics do not substitute for the uniform-in-rank proof or the infinite almost-periodic construction.

## Relationship to prior work

Stanković's 2026 compact-operator theorem establishes singular-value convergence and an exact binomial identity for iterated weighted shifts, but gives no macroscopic or uniform all-index spectral rate in the presence of nonperiodic almost-periodic modulation. The published 2026 regular-variation profile for monotone polynomial weights does not cover these generally oscillatory weights: a nonconstant almost-periodic perturbation typically prevents regular variation. The 2026 cyclic-induced-Aluthge rate theorem concerns finite-period strictly positive bilateral shifts and their convergence to a constant noncompact shift; it does not provide a spectral distribution of compact almost-periodically modulated shifts or the fixed almost-periodic no-polynomial-rate example. Standard finite Fourier mixing explains each trigonometric frequency; the novel comparison here concerns its uniform transfer through polynomial decay, ordered infinite singular spectra, and arbitrary almost-periodic modulations. This literature comparison cannot prove absolute priority.

## Limitations

The theorem is restricted to positive compact unilateral weighted shifts with a power-decaying envelope and uniformly Bohr-almost-periodic log modulation. The all-index remainder is qualitative in its almost-periodic component; no general rate follows without spectral separation. The fixed slow example shows failure of every polynomial rate, not a prescribed arbitrary convergence profile. It does not address general compact operators or nonalmost-periodic perturbations. Independent validation has not been performed.

## References

- H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728v1, first submitted 2026-11-05; Proposition 5.8 and equation (9). https://arxiv.org/html/2611.07728v1
- *A universal sharp nonlinear spectral rate for cyclic induced Aluthge means*, publicly available mathematical result (2026-11-02); see its complete RESULT.md at https://github.com/published-finding corpus/2026 .
- J. Antezana, E. Pujals, and D. Stojanoff, *The iterated Aluthge transforms of a matrix converge*, Advances in Mathematics 226 (2011), 1591–1620; https://doi.org/10.1016/j.aim.2010.08.012 .
