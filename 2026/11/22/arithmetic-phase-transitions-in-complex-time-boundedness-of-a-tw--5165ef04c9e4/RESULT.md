# Arithmetic phase transitions in complex-time boundedness of a two-rate Gaussian semigroup

## Finding
Let \(1<p<\infty\), \(p\ne2\), and let \(a,b>0\). Define \(\kappa_p=\tan(\arccos|1-2/p|)\), and consider the positive anisotropic Ornstein–Uhlenbeck generator
\[
L_{a,b}=a(-\partial_x^2+x\partial_x)+b(-\partial_y^2+y\partial_y)
\]
on \(L^p(\mathbb R^2,\gamma_1\otimes\gamma_1)\), where \(\gamma_1\) is standard Gaussian probability measure. Its Hermite-polynomial complex-time family is bounded (indeed contractive) precisely on
\[
\mathcal B_{a,b}=\{t+is:\ |\sin(as)|\le\kappa_p\sinh(at),\quad |\sin(bs)|\le\kappa_p\sinh(bt)\}.
\]
The bounded holomorphy domain is \(\operatorname{int}\mathcal B_{a,b}\).

For \(t>0\), define the *imaginary-time admissibility density*
\[
d_{a,b}(t)=\lim_{R\to\infty}\frac1R\big|\{s\in[0,R]:t+is\in\mathcal B_{a,b}\}\big|,
\]
where vertical bars denote Lebesgue length. The limit exists for every pair of rates.

**Incommensurable rates.** If \(a/b\notin\mathbb Q\), then for every \(t>0\)
\[
d_{a,b}(t)=\prod_{c\in\{a,b\}}\frac2\pi\arcsin\!\big(\min\{1,\kappa_p\sinh(ct)\}\big),
\]
and, in particular,
\[
d_{a,b}(t)\sim\frac{4\kappa_p^2ab}{\pi^2}t^2\quad(t\downarrow0).
\]
Put \(t_c=c^{-1}\operatorname{arsinh}(1/\kappa_p)\). If \(a<b\), every horizontal section \(\{s:t+is\in\mathcal B_{a,b}\}\) has **no nonzero translational period** for \(0<t<t_b\), has fundamental period \(\pi/a\) for \(t_b\le t<t_a\), and equals all of \(\mathbb R\) for \(t\ge t_a\). In particular, the full two-dimensional boundedness set has no nonzero imaginary translational period.

**Commensurable rates.** If \(a=m\lambda\), \(b=n\lambda\) with coprime positive integers \(m,n\), then the sections have period \(\pi/\lambda\), and for every sufficiently small positive \(t\),
\[
d_{a,b}(t)=\frac{2\lambda}{\pi}\min\!\left\{\frac{\arcsin(\kappa_p\sinh(at))}{a},\frac{\arcsin(\kappa_p\sinh(bt))}{b}\right\}
\sim\frac{2\kappa_p\lambda}{\pi}t.
\]
Thus the short-real-time density exponent is **two** for irrational rate ratios and **one** for rational rate ratios, even though each individual one-dimensional Gaussian semigroup has periodic complex-time boundedness.

## Assumptions and scope
All rates are fixed and positive, and \(1<p<\infty\) with \(p\ne2\). The space uses the product standard Gaussian invariant probability measure. Complex-time operators are initially defined on the dense Hermite-polynomial span by multiplying the basis element of bidegree \((j,k)\) by \(e^{-z(aj+bk)}\). The boundedness domain refers to extension of that family to all of \(L^p\); no assumption is made that the complex-time family is bounded off this domain. The quantity \(d_{a,b}(t)\) is an asymptotic density in imaginary time, *not* an operator norm. For the rational formula, the sufficiently small interval can be made explicit: take \(t>0\) with \(\kappa_p\sinh(at)<1\), \(\kappa_p\sinh(bt)<1\), and
\[
\frac{\arcsin(\kappa_p\sinh(at))}{a}+\frac{\arcsin(\kappa_p\sinh(bt))}{b}<\frac\pi{mn\lambda}.
\]

## Proof
1. Let \(U_p(w)\) be the one-dimensional complex Ornstein–Uhlenbeck Hermite multiplier. Epperson's precise boundedness theorem says that \(U_p(w)\) extends boundedly if and only if \(|\sin(\operatorname{Im}w)|\le\kappa_p\sinh(\operatorname{Re}w)\), and in that event its norm is exactly one. On products of Hermite polynomials, \(e^{-zL_{a,b}}=U_p(az)\otimes U_p(bz)\). When both factors are bounded, their tensor action on \(L^p\) is a contraction by Fubini; it fixes constants, so its norm equals one. If a factor is unbounded, restricting the putative two-variable bounded extension to functions constant in the other coordinate would make that factor bounded, a contradiction. This gives exactly \(\mathcal B_{a,b}\). On its interior both factors admit locally bounded holomorphic extensions and hence so does the product; no larger open bounded-holomorphy domain is possible.

2. Fix \(t>0\) and define \(u_c=\min\{1,\kappa_p\sinh(ct)\}\) and \(I_c=\{\theta\bmod\pi:|\sin\theta|\le u_c\}\). Each circle window has normalized Haar measure \(2\arcsin(u_c)/\pi\). If \(a/b\notin\mathbb Q\), the line \(s\mapsto(as,bs)\bmod\pi\) is uniformly distributed in the two-torus. Since the boundary of each \(I_c\) has Haar measure zero, the long-time average of the characteristic function of \(I_a\times I_b\) equals its Haar measure, proving the product formula. Expanding \(\sinh(ct)=ct+O(t^3)\) and \(\arcsin u=u+O(u^3)\) gives the stated quadratic coefficient.

3. Suppose \(a<b\) and the ratio is irrational. For \(0<t<t_b\), both windows have positive measure strictly between zero and one. If \(\tau\) is a translational period of the horizontal section, the torus characteristic function of \(I_a\times I_b\) is invariant almost everywhere under translation by \((a\tau,b\tau)\bmod\pi\): this follows from density of the line and continuity of the characteristic function away from its boundary. Integrating in each torus coordinate shows that both proper circle windows are separately invariant under the respective translations. Such a symmetric proper interval \(I_c\) has no nontrivial circle translational stabilizer, so \(a\tau,b\tau\in\pi\mathbb Z\); irrationality forces \(\tau=0\). At \(t\ge t_b\), the \(b\)-window is the full circle, leaving only the \(a\)-window until \(t=t_a\). Its least positive period is \(\pi/a\). At \(t\ge t_a\) both conditions are automatic. Since global vertical periodicity would imply periodicity of every section, no nonzero global period exists.

4. If \(a=m\lambda\), \(b=n\lambda\), both sine conditions have common period \(\pi/\lambda\), so the asymptotic density is the normalized measure of one period. Within one period the zero sets of the two sine functions intersect only at the common endpoints, because \(m,n\) are coprime. Distinct (noncommon) zeros of the two functions have separation at least \(\pi/(mn\lambda)\). For sufficiently small \(t\), allowed neighborhoods of the respective zero sets have half-widths \(\delta_a=\arcsin(\kappa_p\sinh(at))/a\) and \(\delta_b=\arcsin(\kappa_p\sinh(bt))/b\), with \(\delta_a+\delta_b<\pi/(mn\lambda)\). There can then be no intersection around distinct zeros. Exactly one common zero occurs per fundamental period, and its allowed intersection has total length \(2\min\{\delta_a,\delta_b\}\). Divide by \(\pi/\lambda\) to obtain the exact rational formula. Taylor expansion yields the linear coefficient.

## Verification
The operator-domain reduction is a direct application of the cited one-variable theorem and Fubini, not a finite-computation inference. The density proof uses uniform distribution on the two-torus and explicitly handles indicator discontinuities by their measure-zero boundaries. The period proof uses a product-window stabilizer argument. The rational exact formula is valid only under the displayed separation and unsaturation conditions. A standalone finite diagnostic script, `check_geometry.py`, compares the formulas with deterministic imaginary-time sampling; its numerical output is not part of the infinite proof.

## Relationship to prior work
Epperson's 1989 boundedness theorem, as recalled and used in Perelmuter's 2026 paper, already determines the entire one-rate boundedness region. Perelmuter proves a periodic covariance principle and applies it to isotropic Ornstein–Uhlenbeck semigroups and other operators. The factorization of this anisotropic generator into two one-dimensional semigroups, and hence the set intersection description, are elementary consequences of existing results and are **not claimed as new**. The distinct contribution is the complete imaginary-time slice period transition together with its exact asymptotic density and sharp rational–irrational small-real-time exponent for one natural two-rate operator.

## Limitations
This does not determine exact norms outside the bounded region (there is no bounded operator there), finite-interval discrepancy rates, or robustness of the arithmetic density law under non-diagonal drift perturbations. The dependence on arithmetic resonance is an infinite-imaginary-time phenomenon: the limits in long imaginary time and in the rate ratio need not commute. Exact priority beyond the inspected literature and indexed records is not independently certified.

## References
- M. A. Perelmuter, *Semigroups with periodic complex-time boundedness and holomorphy regions*, arXiv:2611.15455v1 (11 November 2026), https://arxiv.org/html/2611.15455v1.
- J. B. Epperson, *The hypercontractive approach to exactly bounding an operator with complex Gaussian kernel*, Journal of Functional Analysis 87 (1989), 1–30.
- S. Janson, *On complex hypercontractivity*, Journal of Functional Analysis 151 (1997), 270–280.
- J. van Neerven and P. Portal, *Weyl calculus with respect to the Gaussian measure and restricted \(L^p\)-\(L^q\) boundedness of the Ornstein–Uhlenbeck semigroup in complex time*, https://fa.ewi.tudelft.nl/~neerven/publications/papers/Gaussian-Weyl.pdf.
