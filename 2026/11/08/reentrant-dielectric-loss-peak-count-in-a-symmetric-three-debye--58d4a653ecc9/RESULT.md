# Reentrant dielectric-loss peak count in a symmetric three-Debye mixture

## Finding

A sum of three elementary Debye losses can lose and then regain a central peak as their relaxation times become more widely separated. Fix a central strength \(a\) satisfying
\[
\frac12<a<\frac{4}{3\sqrt6}.
\]
The two outer components each have strength one and relaxation times \(\tau_0/r\) and \(\tau_0r\); the middle component has strength \(a\) and time \(\tau_0\), where \(\tau_0>0\) and \(r>1\). Let \(N(r;a)\) be the number of strict local maxima of the positive-frequency loss as a function of logarithmic frequency. Define \(s=(r+r^{-1})/2\), \(s_0=4a\), and let \(s_1<s_2\) be the two roots greater than 2 of
\[
a s^3-2s^2+4=0.
\]
Then \(2<s_0<s_1<\sqrt6<s_2\), and, **including all transition equalities**, the exact modal law is
\[
N(r;a)=\begin{cases}
1,&1<s\le s_0,\\
3,&s_0<s<s_1,\\
2,&s_1\le s\le s_2,\\
3,&s>s_2.
\end{cases}
\]
At \(s=s_0\), the two off-center stationary points are nonextremal shoulders; at \(s=s_1,s_2\), the center is a strict fourth-order-flat local minimum, not a maximum. Thus there is a genuine **one–three–two–three reentrance** as the common multiplicative separation \(r\) increases. No mode count above three occurs.

For example, with \(a=53/100\), the transitions occur at \(r\approx3.9893314313\), \(4.0921245101\), and \(5.4850648080\), in that order. The phenomenon concerns mathematical local maxima, not finite-resolution experimental identifiability.

## Assumptions and scope

Take independent, linear, positive-strength Debye relaxations with the complex susceptibility
\[
\chi^*(\omega)=\Delta\epsilon\left(\frac{1}{1+i\omega\tau_0/r}+\frac{a}{1+i\omega\tau_0}+\frac{1}{1+i\omega\tau_0r}\right),\qquad \omega>0,
\]
with \(\Delta\epsilon>0\), \(\tau_0>0\), and the \(a,r\) restrictions above. Define the nonnegative loss as \(\mathcal L(\omega)=-\operatorname{Im}\chi^*(\omega)\). A peak means a strict local maximum for \(\omega\in(0,\infty)\) as measured against \(\log(\omega\tau_0)\). Multiplying \(\Delta\epsilon\) or rescaling \(\tau_0\) does not alter this count. The statement does not require material-specific constitutive data, interactions between relaxations, or a claim that arbitrary observed processes have Debye shapes.

## Proof

**1. Symmetric reduction.** Put \(y=\log(\omega\tau_0)\), \(\ell=\log r\), \(s=\cosh\ell>1\), and \(c=\cosh y\ge1\). Each positive Debye loss is half a hyperbolic secant, so
\[
\frac{\mathcal L(y)}{\Delta\epsilon}
=\tfrac12\operatorname{sech}(y-\ell)+\tfrac a2\operatorname{sech}y+\tfrac12\operatorname{sech}(y+\ell)
=\frac{a}{2c}+\frac{sc}{c^2+s^2-1}=:F(c).
\]
The loss is even in \(y\), goes to zero at both infinite ends, and the map \(y\mapsto c\) is strictly increasing for \(y>0\). Differentiation, with \(z=c^2\), yields exactly
\[
F'(c)=-\frac{Q(c^2)}{2c^2(c^2+s^2-1)^2},\quad
Q(z)=(a+2s)z^2+2(s^2-1)(a-s)z+a(s^2-1)^2.
\]
The quadratic discriminant is \(4s(s-4a)(s^2-1)^2\).

**2. Creation of outer maxima.** If \(1<s<4a\), the discriminant is negative; since the leading coefficient is positive, \(Q(z)>0\), so \(F\) decreases strictly on \(c>1\), and only \(y=0\) is a maximum. At \(s=s_0=4a\),
\[
Q(z)=(a+2s)\left(z-\frac{s^2-1}{3}\right)^2.
\]
Because \(s_0>2\), the double zero lies above \(z=1\). It creates stationary shoulders but no outer extrema, so the count remains one.

For \(s>4a\), the two simple roots are positive and equal to
\[
z_\pm=\frac{(s^2-1)\bigl(s-a\pm\sqrt{s(s-4a)}\bigr)}{a+2s},\qquad 0<z_-<z_+.
\]
The vertex of \(Q\) is \(z_v=(s^2-1)(s-a)/(a+2s)\). Since \(a\le s/4\), \(z_v\ge(s^2-1)/3>1\); the quadratic is negative at its vertex. Hence \(z_+>1\) always. The off-center critical points \(y=\pm\operatorname{arcosh}\sqrt{z_+}\) are strict maxima. When \(z_->1\), the extra two points \(y=\pm\operatorname{arcosh}\sqrt{z_-}\) are strict minima and the center is a strict local maximum, giving three maxima. When \(z_-<1\), the center is a strict local minimum and there are two maxima. At \(z_-=1\), the center is still a strict local minimum, but of fourth rather than second order: near \(y=0\), \(z-1\) is positive of order \(y^2\), and \(Q(z)<0\) for \(1<z<z_+\), so \(F(\cosh y)-F(1)>0\) for all sufficiently small nonzero \(y\).

**3. Arithmetic of the two center transitions.** The exact boundary identity is
\[
Q(1)=s\bigl(a s^3-2s^2+4\bigr)
=s^4\left(a-\frac{2(s^2-2)}{s^3}\right).
\]
Write \(a_0(s)=2(s^2-2)/s^3\). On \((2,\infty)\) it increases from \(1/2\) to its unique maximum \(4/(3\sqrt6)\) at \(s=\sqrt6\), then decreases to zero. Therefore each allowed \(a\) gives exactly two roots \(2<s_1<\sqrt6<s_2\) with \(a_0(s_j)=a\). Moreover \(s_0=4a<\sqrt6\) and
\[
a-a_0(s_0)=\frac{(s_0^2-4)^2}{4s_0^3}>0,
\]
so \(s_0<s_1\). Since \(z_+>1\) for \(s>s_0\), the sign of \(Q(1)\) decides whether \(z_-\) is above or below one. In \((s_0,s_1)\cup(s_2,\infty)\), \(Q(1)>0\), so \(z_->1\); in \((s_1,s_2)\), \(Q(1)<0\), so \(z_-<1\). At the endpoints \(z_-=1\). Combining these cases proves the four intervals, their sharp endpoints, and the exhaustive maximum count. The monotone relation \(r=s+\sqrt{s^2-1}\) transfers them to frequency-separation ratios. \(\square\)

## Verification

The accompanying `verify.py` uses only the Python standard library. It checks the quadratic-discriminant transition and onset double root with exact rational arithmetic at \(a=53/100\), independently samples the **original three-term Debye derivative** across 30,000 positive log-frequency points at each of four representative parameter choices, and matches the stationary-point formula to those crossings. It additionally compares the independent direct Debye sum against the symmetric rational reduction at 42 frequency/spacing samples, and numerically locates both positive roots of the exact center-transition cubic. Run `python3 verify.py`. These finite computations corroborate the derivation; the infinite-family conclusion is proved in the preceding algebra, not inferred from sampling.

For \(a=53/100\), using \(s=2.1,2.13,2.3,4\) respectively produces \(1,3,2,3\) local maxima. The analytic transition values are approximately \(s_0=2.12\), \(s_1=2.16824817555\), \(s_2=2.83368902976\).

## Relationship to prior work

Debye spectral components and their superposition are established tools, not new physical laws. Bauer, Michl, Lunkenheimer and Loidl (2014; arXiv:1404.3972), fully inspected in its open preprint, study three experimentally distinct relaxations in 1-propanol: the Debye, structural alpha and beta processes. The latter two are **not** modeled as three identical Debye-shape components in that paper; the present tunable symmetric three-Debye peak-count phase diagram is not derived there. Nguyen et al. (2023; arXiv:2305.19560) explicitly use a *sum of three Debye components* (their equation (2)) for water; inspection of the relevant text and figure shows fitted spectra, not the equal-outer-strength, geometric-time, exact reentrant modal classification. Earlier multiterm and relaxation-distribution literature contains the building blocks and could contain an equivalent unindexed mode-count result.

The novelty asserted here is only the **exact reentrant four-regime classification in the indicated continuous central-strength interval**, including the two fourth-order-flat transition endpoints. Neither the elementary Debye formula nor the existence of three relaxation processes is claimed as new. A separate earlier analysis of four equally strong, geometrically spaced Debye components gives a different, non-reentrant count and does not imply the present three-component unequal-strength conclusion.

## Limitations

All three constituents are independent ideal Debye relaxations with equal outer strengths and geometrically spaced times. Real alpha/beta relaxations may be broadened and asymmetric, and conductivity, noise, interactions and finite instrument resolution can alter observed peaks. We classify strict mathematical *local* maxima, not global peak ordering, finite-resolution resolvability, or the possibility of realizing the exact parameter ratios in a particular substance. The theorem does not provide an exhaustive mode-count phase portrait for central strengths outside \((1/2,4/(3\sqrt6))\). Historical priority is provisional: the full text of the plausible older multiterm-dispersion work of Hurt (1985) was not accessible, and unindexed results in hyperbolic-secant-mixture theory could imply this special case. No independent scientific audit has been conducted.

## References

1. T. Bauer, M. Michl, P. Lunkenheimer and A. Loidl, *Nonlinear dielectric response of Debye, alpha, and beta relaxation in 1-propanol*, arXiv:1404.3972, first public 2014-04-15. https://arxiv.org/abs/1404.3972
2. N. Q. Vinh et al., *Correlation between Macroscopic and Microscopic Relaxation Dynamics of Water: Evidence for Two Liquid Forms*, arXiv:2305.19560 (2023), especially equation (2) and figure 3. https://arxiv.org/abs/2305.19560
3. W. D. Hurt, *Multiterm Debye dispersion relations for permittivity of muscle*, IEEE Transactions on Biomedical Engineering (1985), DOI:10.1109/TBME.1985.325629; abstract available, full text not inspected. https://doi.org/10.1109/TBME.1985.325629
4. C. J. Dias, *Determination of a distribution of relaxation frequencies based on experimental relaxational data*, Physical Review B 53 (1996), 14212, DOI:10.1103/PhysRevB.53.14212; abstract inspected. https://doi.org/10.1103/PhysRevB.53.14212
