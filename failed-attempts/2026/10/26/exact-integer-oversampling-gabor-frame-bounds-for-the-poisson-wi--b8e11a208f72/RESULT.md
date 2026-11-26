# Exact integer-oversampling Gabor frame bounds for the Poisson window

## Finding

For every \(w>0\) and integer \(q\ge2\), put \(g_w(t)=1/(t^2+w^2)\) and define the unit-translation, reciprocal-integer-frequency system
\[
\mathcal G_{q,w}=\{e^{2\pi i m t/q}g_w(t-n):m,n\in\mathbb Z\}\subset L^2(\mathbb R).
\]
Its **optimal** frame constants (the largest admissible lower bound and smallest admissible upper bound) are
\[
\boxed{A_q(w)=\frac{\pi^2}{w^2}\left(\tanh(\pi w)\operatorname{csch}(2\pi w/q)-\frac q2\operatorname{sech}^2(\pi w)\right)},
\]
\[
\boxed{B_q(w)=\frac{\pi^2}{w^2}\left(\coth(\pi w)\coth(2\pi w/q)+\frac q2\operatorname{csch}^2(\pi w)\right)}.
\]
Here \(\operatorname{csch}(u)=1/\sinh u\) and \(\operatorname{sech}(u)=1/\cosh u\). These expressions are strictly positive and finite for the indicated parameters. Their extremal Zak points are \((1/2,1/(2q))\) and \((0,0)\) respectively, unique modulo the natural Zak periodicities.

The explicit formulas yield two sharply distinct fixed-redundancy limits:
\[
\begin{aligned}
&w\downarrow0:\quad A_q(w)=\frac{\pi^4}{3}(q-q^{-1})+O_q(w^2),\\
&\hspace{46pt}B_q(w)\sim q w^{-4},\qquad \frac{B_q(w)}{A_q(w)}\sim\frac{3q^2}{\pi^4(q^2-1)}w^{-4};\\
&w\to\infty:\quad A_q(w)\sim\frac{2\pi^2}{w^2}e^{-2\pi w/q},\quad B_q(w)\sim\frac{\pi^2}{w^2},\quad \frac{B_q(w)}{A_q(w)}\sim\frac12e^{2\pi w/q}.
\end{aligned}
\]

## Assumptions and scope

All inner products and norms are the standard Lebesgue \(L^2(\mathbb R)\) ones, with no unit-norm normalization of \(g_w\) and with modulation \(M_\xi f(t)=e^{2\pi i\xi t}f(t)\), translation \(T_n f(t)=f(t-n)\). The statements hold for **every real** \(w>0\) and **every integer** \(q\ge2\). The asymptotic equivalents and the \(O_q(\cdot)\) estimate fix \(q\) as \(w\) varies. The result does not optimize over continuously varying lattice shapes or address noninteger density.

## Proof

**1. Frame operator as a scalar Zak multiplier.** On \([0,1]^2\), use the unitary Zak transform
\[
Zf(x,\omega)=\sum_{k\in\mathbb Z}f(x+k)e^{-2\pi i k\omega}.
\]
Because \(g_w\) decays quadratically, the series for its Zak transform converges uniformly. Write the modulation index as \(m=q\ell+j\), \(0\le j<q\). The elementary Zak covariance laws for integer translations and integer modulations, followed by two-dimensional Fourier Parseval in \((\ell,n)\), give, first for a dense class and then for every \(f\in L^2(\mathbb R)\),
\[
\sum_{m,n\in\mathbb Z}|\langle f,M_{m/q}T_ng_w\rangle|^2
=\int_0^1\int_0^1 |Zf(x,\omega)|^2 F_q(x,\omega)\,dx\,d\omega,
\]
where \(F_q(x,\omega)=\sum_{j=0}^{q-1}|Zg_w(x,\omega+j/q)|^2\). Hence the optimal frame bounds are the essential minimum and maximum of the continuous periodic multiplier \(F_q\); once \(F_q\) is positive, the system is a frame, and sharpness follows by concentrating a Zak-domain test function in arbitrarily small neighborhoods of its extremal points.

**2. Exact Zak transform.** With \(r=e^{-2\pi w}\), \(u=e^{2\pi ix}\), and \(0\le s\le1\), the Fourier transform in convention \(\widehat g(\xi)=\int g(t)e^{-2\pi i t\xi}\,dt\) is \(\widehat g_w(\xi)=(\pi/w)r^{|\xi|}\). Poisson summation and two elementary geometric series give
\[
Zg_w(x,s)=\frac\pi w e^{2\pi isx}\left(\frac{r^s}{1-ru}+\frac{r^{1-s}u^{-1}}{1-ru^{-1}}\right)
=\frac\pi w e^{2\pi isx}\frac{a_s+b_su^{-1}}{1+r^2-2r\cos(2\pi x)},
\]
where \(a_s=r^s-r^{2-s}\ge0\) and \(b_s=r^{1-s}-r^{1+s}\ge0\). The endpoint formulas agree by Zak quasi-periodicity.

**3. Exact extremization in the time coordinate.** Fix a representative \(0\le\omega\le1/q\); put \(s_j=\omega+j/q\), \(c=\cos(2\pi x)\), \(C=\sum_j(a_{s_j}^2+b_{s_j}^2)>0\), and \(E=2\sum_j a_{s_j}b_{s_j}\ge0\). The multiplier has the rational form
\[
F_q(x,\omega)=\frac{\pi^2}{w^2}\frac{C+Ec}{(1+r^2-2rc)^2}.
\]
Its derivative with respect to \(c\in[-1,1]\), apart from the positive constant, is
\[
\frac{E(1+r^2+2rc)+4rC}{(1+r^2-2rc)^3}>0.
\]
The inequality is strict because \(1+r^2+2rc\ge(1-r)^2>0\) and \(C,r>0\). Thus the global minimum occurs only at \(x=1/2\pmod1\), and the maximum only at \(x=0\pmod1\).

**4. Exact extremization in the frequency coordinate.** At the two time endpoints, simplification of the Zak transform gives
\[
\left|Zg_w(1/2,s)\right|^2=\frac{\pi^2}{w^2}\frac{(r^s-r^{1-s})^2}{(1+r)^2},\qquad
\left|Zg_w(0,s)\right|^2=\frac{\pi^2}{w^2}\frac{(r^s+r^{1-s})^2}{(1-r)^2}.
\]
For \(0\le s\le 1/q\), define
\[
H_q(s)=\sum_{j=0}^{q-1}\bigl(r^{2(s+j/q)}+r^{2-2(s+j/q)}\bigr)
=\frac{1-r^2}{1-r^{2/q}}\bigl(r^{2s}+r^{2/q-2s}\bigr).
\]
The right side is strictly convex in \(s\) and symmetric about \(s=1/(2q)\). It therefore has its **unique minimum** there, and its maximum at the identified interval endpoints \(s=0,1/q\), which are identical under the period \(1/q\). We have
\[
F_q(1/2,s)=\frac{\pi^2}{w^2}\frac{H_q(s)-2qr}{(1+r)^2},\qquad
F_q(0,s)=\frac{\pi^2}{w^2}\frac{H_q(s)+2qr}{(1-r)^2}.
\]
Consequently
\[
A_q(w)=\frac{\pi^2}{w^2}\frac{\tfrac{2(1-r^2)r^{1/q}}{1-r^{2/q}}-2qr}{(1+r)^2},\quad
B_q(w)=\frac{\pi^2}{w^2}\frac{\tfrac{(1-r^2)(1+r^{2/q})}{1-r^{2/q}}+2qr}{(1-r)^2}.
\]
Using \(r=e^{-2\pi w}\) and elementary hyperbolic identities yields the two boxed constants in the finding. For \(q\ge2\), the lower numerator is the sum
\(\sum_{j=0}^{q-1}(r^{s_j}-r^{1-s_j})^2\) at \(s_j=(j+1/2)/q\). The \(s_j\)'s are distinct, so they cannot all equal \(1/2\); hence the numerator is strictly positive. The denominator is finite. This proves existence, optimality and strict uniqueness of the two extremal fibers.

**5. Width degeneration and conditioning.** With \(t=2\pi w\), expand \(\tanh(t/2)=t/2-t^3/24+O(t^5)\), \(\operatorname{csch}(t/q)=q/t-t/(6q)+O_q(t^3)\), and \(\operatorname{sech}^2(t/2)=1-t^2/4+O(t^4)\). The bracket in \(A_q\) is \(t^2(q-q^{-1})/12+O_q(t^4)\). Similarly the bracket in \(B_q\) is \(4q/t^2+O_q(1)\). This proves the narrow-window constants. As \(t\to\infty\), the first bracket is \(2e^{-t/q}(1+o(1))\), since the subtracted correction is of order \(e^{-t}\) and \(q\ge2\); the second bracket is \(1+o(1)\). This proves the wide-window constants and their ratios.

## Verification

A standalone standard-library Python checker (`verify.py`) computes independent direct Zak series, the rational-geometric Zak formula, exact multiplier endpoints, the hyperbolic closed forms and asymptotic ratios at multiple nontrivial widths and oversampling factors. The checker prints `CHECK_OK` when its finite floating-point consistency tests pass. These checks are supplements: the statements for all \(q\) and all \(w\) follow from the exact algebra and inequalities above, not from enumeration or numerical extrapolation.

## Relationship to prior work

Belov, Kulikov and Lyubarskii (2021) proved qualitative Gabor-frame theorems for rational Herglotz windows. Semenov (first arXiv version 2025-10-29) constructed near-critical universal frequency sets for broad rational-window classes, but did not give this Poisson window's sharp spectral constants. Faulhuber and Shafkulovska (2022) determined frame-bound optimizers at integer density for several other windows (Gaussian, hyperbolic secant and exponential families). Belov, Kulikov and Lyubarskii (2022) analyzed the one-pole Cauchy window \(1/(t-iw)\), not the even two-pole window \(1/(t^2+w^2)\); their stated bounds are estimates. Belov and Semenov (2026-10-21) obtained a frame-set criterion for arbitrary semi-regular frequency sets for **this same Poisson window**, but its inspected argument establishes qualitative existence and comparability, not the exact optimal constants at all integer oversampling levels. The novelty claimed here is limited to the specific exact sharp bounds, extremal locations and width-asymptotic coefficients, not the general frame-set criterion or the Zak diagonalization method.

## Limitations

The precise spectral constants are proved only for unit translations and integer frequency oversampling, not noninteger densities or arbitrary irregular configurations. Width asymptotics hold for fixed \(q\); no uniform large-\(q\) remainder is claimed. The historical-priority assessment cannot exclude unindexed earlier exact calculations: Janssen's 1996 paper on Weyl–Heisenberg frame bounds was located bibliographically but its full text was not accessible. No claim of independent review or mathematical certification is made.

## References

1. A. V. Semenov, *Universal frame set for rational functions*, arXiv:2510.25930, first public 2025-10-29, https://arxiv.org/abs/2510.25930.
2. Yu. Belov, A. Kulikov and Yu. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959, https://arxiv.org/abs/2103.08959.
3. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, https://arxiv.org/abs/2204.02917.
4. Yu. Belov, A. Kulikov and Yu. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915, https://arxiv.org/abs/2212.08915.
5. Yu. Belov and A. V. Semenov, *Irregular Gabor Frames for the Poisson Kernel*, arXiv:2610.30037, first public 2026-10-21, https://arxiv.org/abs/2610.30037. Included solely as a close coverage comparison, not as the motivating source whose first public date determines the present study.
6. A. J. E. M. Janssen, *Some Weyl–Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, https://nuhagphp.univie.ac.at/janssen/data/p071.pdf (bibliographic comparison only; full text unavailable).
