# Sharp equal-radius coherent-state amplification for reciprocal exponential Fock Toeplitz products

## Finding

In the power-weighted analytic Fock space \(\mathcal F_m^2\), the largest off-diagonal normalized coherent-state matrix coefficient of a reciprocal exponential Toeplitz product has a sharp, universal leading law. For every fixed real \(m>1/2\), every nonconstant polynomial \(g(z)=a_d z^d+\cdots+a_0\) of integer degree \(1\le d<2m\), and \(a_d\ne0\), let \(T_g^{\mathrm{rec}}\) denote the Toeplitz product \(T_{e^g}T_{\overline{e^{-g}}}\) on its natural coherent-kernel domain. Put

\[
M_{m,g}(R)=\max_{|z|=|w|=R}|\langle T_g^{\mathrm{rec}}k_w,k_z\rangle|,
\qquad k_w=K_m(\cdot,w)/\sqrt{K_m(w,w)}.
\]

Then, as \(R\to\infty\),

\[
\boxed{\lim_{R\to\infty}R^{2m-2d}\log M_{m,g}(R)
=\frac{d^2|a_d|^2}{2m^2}.}
\tag{1}
\]

For *every* sequence \((z_R,w_R)\) attaining the maximum, with the principal signed separation \(\theta_R=\arg(z_R\overline{w_R})\in(-\pi,\pi]\),

\[
\boxed{\lim_{R\to\infty}R^{2m-d}|\theta_R|=\frac{d|a_d|}{m^2}.}
\tag{2}
\]

Consequently, \(M_{m,g}(R)\to1\) if \(d<m\); when \(d=m\) (necessarily an integer radial exponent), it tends to \(\exp(|a_d|^2/2)\); and when \(m<d<2m\), \(M_{m,g}(R)\) grows as \(\exp[(d^2|a_d|^2/(2m^2)+o(1))R^{2d-2m}]\). In the last regime the Toeplitz product has no bounded extension. No assertion equates \(M_{m,g}(R)\) to the operator norm. Nevertheless, at every integer radial exponent \(m=d\), boundedness of the product from the published classification and the coherent-state test imply the coefficient-only lower bound \(\|T_g^{\mathrm{rec}}\|\ge\exp(|a_d|^2/2)\), independently of all lower coefficients.

## Assumptions and scope

Fix \(m>1/2\) and define \(\mathcal F_m^2\) as the entire functions with finite squared norm

\[
\|f\|_m^2=\int_{\mathbb C}|f(z)|^2e^{-|z|^{2m}}\,dA(z).
\]

The reproducing kernel, with inner product linear in its first argument, is

\[
K_m(z,w)=\frac m\pi\sum_{n=0}^\infty
\frac{(z\overline w)^n}{\Gamma((n+1)/m)}.
\tag{3}
\]

Let \(g\) be *fixed independently of* \(R\). The condition \(d<2m\) ensures \(e^{\pm g}\in\mathcal F_m^2\), so their Toeplitz sesquilinear product is defined on coherent kernels. The symbols are generally unbounded: the result concerns matrix coefficients of that initially defined product, and makes an operator boundedness conclusion only where stated. The polynomial's constant term cancels identically.

## Proof

**1. Exact coherent-state reduction.** The reproducing property gives, for arbitrary coherent kernels in the product's domain,

\[
\langle T_{e^g}T_{\overline{e^{-g}}}k_w,k_z\rangle
=e^{g(z)-\overline{g(w)}}
\frac{K_m(z,w)}{\sqrt{K_m(z,z)K_m(w,w)}}.
\tag{4}
\]

Write \(w=Re^{i\phi}\), \(z=Re^{i(\phi+\theta)}\) with \(-\pi<\theta\le\pi\). The modulus of (4) is the product of the kernel quotient

\[
Q_m(R,\theta)=\left|\frac{K_m(R^2e^{i\theta})}{K_m(R^2)}\right|
\]

and \(\exp\Re[g(Re^{i(\phi+\theta)})-g(Re^{i\phi})]\). Thus

\[
\log M_{m,g}(R)=\max_{-\pi<\theta\le\pi}
\{\log Q_m(R,\theta)+H_R(\theta)\},
\]

where \(H_R(\theta)\) is the maximum of that real polynomial difference over \(\phi\). The maximum exists because the original two-torus is compact and the diagonal coefficient equals one.

**2. Kernel estimate with a sufficiently small remainder.** For \(m>1/2\) the standard Mittag–Leffler asymptotic expansion for \(E_{1/m,1/m}\) has exactly one dominant exponential in a fixed angular neighborhood of the positive real axis. Its full expansion, not merely a relative \(1+o(1)\) statement, has an algebraic remainder, since the coefficient at the first inverse power is \(1/\Gamma(0)=0\). Hence there exist \(\delta,c,C>0\), independent of \(R\), such that uniformly for \(|\theta|\le\delta\),

\[
\log Q_m(R,\theta)
=R^{2m}(\cos(m\theta)-1)+O(e^{-cR^{2m}}).
\tag{5}
\]

Indeed, the dominant prefactor \((R^2e^{i\theta})^{m-1}\) has modulus independent of \(\theta\); the exponentially small relative error follows by comparing the algebraic remainder with \(e^{R^{2m}\cos(m\theta)}\) for \(\cos(m\delta)>0\). The conventional sectorwise upper bounds for this same Mittag–Leffler function give, for every such fixed sufficiently small \(\delta\),

\[
\sup_{\delta\le|\theta|\le\pi}Q_m(R,\theta)
\le C e^{-cR^{2m}}.
\tag{6}
\]

The estimates are also obtained directly from the reproducing-kernel estimates in the cited Fock Toeplitz-product literature, supplemented for (5) by the classical full Mittag–Leffler expansion. For \(m\le1/2\) additional exponential branches appear in that expansion; this proof makes no statement about that regime.

**3. Polynomial angular gain.** The leading term gives exactly

\[
\max_{\phi}\Re\left[a_d R^d e^{id\phi}(e^{id\theta}-1)\right]
=2|a_d|R^d|\sin(d\theta/2)|.
\]

The remaining terms obey the *uniform* bound

\[
\left|H_R(\theta)-2|a_d|R^d|\sin(d\theta/2)|\right|
\le C_g R^{d-1}|\theta|,
\tag{7}
\]

where the right-hand side is interpreted as zero for the derivative of a constant term. Thus for sufficiently small \(|\theta|\),

\[
H_R(\theta)=d|a_d|R^d|\theta|
+O(R^{d-1}|\theta|+R^d|\theta|^3).
\tag{8}
\]

In particular \(H_R(\theta)\le C_gR^d\) globally and \(H_R(\theta)\le C_g R^d|\theta|\) near zero.

**4. Global localization.** Because \(d<2m\), (6) and \(H_R=O(R^d)\) show that no maximizing angular difference remains outside \((-\delta,\delta)\) for large \(R\): those values give a logarithm tending to minus infinity, whereas the diagonal gives zero. Decrease \(\delta\) if needed so that \(1-\cos(m\theta)\ge c_m\theta^2\). Equations (5) and (8), together with nonnegativity of the maximum, then imply that every maximizing difference satisfies

\[
|\theta_R|=O(R^{d-2m}).
\tag{9}
\]

This localization includes the delicate \(d<m\) case, where the logarithm of the maximum tends to zero: the error in (5) is exponentially small and therefore negligible even relative to a negative power of \(R\).

**5. The universal quadratic saddle.** Set \(\theta=vR^{d-2m}\), where \(v\) ranges over a bounded interval. From (5), (8), and the Taylor expansion of cosine,

\[
R^{2m-2d}\{H_R(\theta)+\log Q_m(R,\theta)\}
=d|a_d||v|-\frac{m^2v^2}{2}+o(1),
\tag{10}
\]

uniformly for bounded \(v\). The errors divide by \(R^{2d-2m}\) to give, respectively, \(O(R^{-1})\), \(O(R^{2d-4m})\), and an exponentially small term; all vanish because \(d<2m\). The continuous limiting quadratic on \(v\ge0\) has unique maximizing magnitude

\[
v_* =\frac{d|a_d|}{m^2},\qquad
\max_{v\ge0}\left(d|a_d|v-\frac{m^2v^2}{2}\right)
=\frac{d^2|a_d|^2}{2m^2}.
\]

The lower bound follows by testing the phase of the leading monomial at the angle \(v_*R^{d-2m}\); the upper bound follows from (9) and uniformity in (10). Uniqueness of the limiting maximizing magnitude proves (2), and (1) follows. The three regimes and the unbounded-extension consequence are immediate. \(\square\)

## Verification

A standalone, standard-library-only script `verify.py` evaluates finite Mittag–Leffler kernel sums after positive coefficient normalization, checks exact Gaussian normalization, and compares the predicted angle and exponent with selected finite-radius examples. Running it returns `FINITE_CHECKS_OK 44`. These tests are *not* infinite proofs, do not exhaust all parameter choices, and are subordinate to steps 1–5.

For a completely exact normalization check, take \(m=d=1\), \(g(z)=az\) and let \(A=|a|\). The kernel is \(K_1(z,w)=\pi^{-1}e^{z\overline w}\), so the maximum angular objective is

\[
\max_{0\le s\le1}\{2ARs-2R^2s^2\}
=A^2/2\quad\text{whenever } R\ge A/2,
\]

where \(s=|\sin(\theta/2)|\). This agrees with the limiting coefficient and verifies the factor \(1/2\) independently of asymptotic kernel analysis. Moreover, for this Gaussian normalization, \(T_{e^{az}}T_{\overline{e^{-az}}}f(z)=e^{az}f(z-\overline a)\). Completing the square in the Fock integral gives the exact full operator norm \(e^{|a|^2/2}\); thus the large-radius equal-circle coherent-state maximum asymptotically captures that Gaussian norm exactly. This exact Gaussian identity is classical and is not proposed as an independent new result.

## Relationship to prior work

Bommier-Hato, Youssfi, and Zhu proved the qualitative reciprocal-polynomial boundedness classification for \(m\ge1\), and explicitly introduced the normalized two-kernel Toeplitz product coefficient in their proof (their Lemma 3 and equations (3)–(7)). Their later Lemma 12 gives a lower estimate for a **different**, squared Berezin-transform product, with coefficient \(d^2|a_d|^2/m^2\), rather than an exact global equal-radius two-coherent maximum. Those statements and their kernel estimates are essential cited premises, not claimed as new. Cho–Park–Zhu established the classical Gaussian boundedness criterion. Virtanen surveys Toeplitz product formulas on standard analytic spaces, and Hagger treats semiclassical product expansions for a different symbol class.

The assessed addition is the exact universal coefficient and asymptotically necessary maximizing separation for the coherent-state *two-point* statistic, simultaneously on the decaying, critical and growing sides (including \(1/2<m<1\)). The Gaussian exact identity is a known check, not a novelty claim. A direct equality for the all-radii operator norm, or a new version of the existing boundedness classification, is not asserted.

## Limitations

The exponent \(m>1/2\) and strict inequality \(d<2m\) are essential to the stated single-exponential kernel argument; the multibranch and borderline integrability cases are not classified. The polynomial and its leading coefficient must remain fixed as \(R\) varies. The theorem determines only equal-radius normalized kernel coefficients, not the full operator norm, essential norm or singular-value distribution. The source comparison cannot exclude unindexed older formulas disguised as coherent-state or saddle-point asymptotics. Independent mathematical audit has not been performed.

## References

1. H. Bommier-Hato, E. H. Youssfi and K. Zhu, *Sarason's Toeplitz product problem for a class of Fock spaces*, Bulletin des Sciences Mathématiques **141** (2017), 408–442, DOI: 10.1016/j.bulsci.2017.03.002. Lawful text: https://arxiv.org/html/2004.04094v1 (public preprint posted 8 April 2020).
2. H. R. Cho, J.-D. Park and K. Zhu, *Products of Toeplitz operators on the Fock space*, Proc. Amer. Math. Soc. **142** (2014), 2483–2489, DOI: 10.1090/S0002-9939-2014-12110-1.
3. J. A. Virtanen, *On the product formula for Toeplitz and related operators*, https://arxiv.org/html/2205.12345v1 (24 May 2022).
4. R. Hagger, *A product expansion for Toeplitz operators on the Fock space*, Proc. Amer. Math. Soc. **147** (2019), 4823–4833, https://arxiv.org/abs/1808.10376.
5. A. Erdélyi et al., *Higher Transcendental Functions*, vol. III, §18.1, classical Mittag–Leffler sector expansions; as cited in Reference 1.
6. D. Biolek, R. Garrappa, F. Mainardi and M. Popolizio, *Derivatives of Mittag-Leffler functions: theory, computation and applications*, Nonlinear Dynamics **113** (2025), 34389–34403, DOI: 10.1007/s11071-025-11682-3; see Section 4, Proposition 6 for the sectorwise exponential-plus-algebraic expansion used in step 2.
