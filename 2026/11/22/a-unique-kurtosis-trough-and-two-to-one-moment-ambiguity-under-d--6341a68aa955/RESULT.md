# A unique kurtosis trough and two-to-one moment ambiguity under dichotomous-acceleration resetting

## Finding

Consider a force that randomly switches between two opposite accelerations and whose particle position, velocity, and force sign are jointly restarted at independent Poisson times. The stationary position excess kurtosis has a **unique strict interior minimum** as the reset/force-switch ratio changes, crossing below and then above the complete-reset Gaussian-acceleration value. This creates an interval of **two-to-one inverse ambiguity**: two different switching rates and suitably chosen acceleration magnitudes give the same stationary second and fourth position moments at any fixed reset rate.

Precisely, with \(z=r/\gamma>0\), let \(K(z)=\mathbb E[X^4]/(\mathbb E[X^2])^2-3\). Then

\[
K(z)=\frac{3(608+1184z+810z^2+201z^3)}{(z+2)(3z+4)^2}.
\]

The unique global minimizer \(z_*\) is the unique positive root of

\[
6z^3+15z^2+6z-4=0,
\quad z_*=0.339462271566093694\ldots,
\]

and \(K(z_*)=56.5770470882562612\ldots\). Write

\[
z_c=\frac{\sqrt{249}-3}{15}=0.851982255870633336\ldots.
\]

Then \(K(z)<57\) exactly for \(0<z<z_c\), equals \(57\) at \(z=z_c\), and is greater than \(57\) for \(z>z_c\). Its boundary limits are \(\lim_{z\downarrow0}K(z)=57\) and \(\lim_{z\to\infty}K(z)=67\). Every value \(k\) with \(K(z_*)<k<57\) is assumed at exactly two different positive ratios \(z\), on opposite sides of \(z_*\).

## Assumptions and scope

All parameters \(a,\gamma,r\) are strictly positive. Between resets, the position \(X\), velocity \(V\), and acceleration sign \(S\in\{-1,+1\}\) evolve according to

\[
\dot X=V,\qquad \dot V=aS,
\]

with \(S\) changing sign at the independent exponential rate \(\gamma\). At Poisson times of rate \(r\), the entire state is reset to \((X,V)=(0,0)\), and an independent uniform sign \(S\) is drawn. A full excursion restarts independently after each reset. The statement concerns the unique stationary distribution of the Markov process and the *excess* kurtosis, defined by subtracting three from the normalized fourth central moment. The stationary position is symmetric, so central and raw even moments agree.

## Proof

**1. Stationarity and moment existence.** Independent complete resets produce a regenerative stationary law: draw \(T\sim\mathrm{Exp}(r)\), independently start a fresh symmetric telegraph sign at time zero, and run the unreset dynamics for time \(T\). Within a reset-free interval, \(|V(T)|\le aT\) and \(|X(T)|\le aT^2/2\). Hence every stationary polynomial moment exists and the regenerative law is unique: the probability of avoiding a reset for a time interval of length \(t\) is \(e^{-rt}\), erasing all prior state dependence.

**2. Closed moment recursion.** Put \(M_{i,j,k}=\mathbb E[X^iV^jS^k]\), for nonnegative integers \(i,j\), with \(k\in\{0,1\}\). For positive weighted degree \(2i+j>0\), the stationary generator identity, including both sign switches and complete resetting, is

\[
(r+2\gamma k)M_{i,j,k}
=iM_{i-1,j+1,k}+ajM_{i,j-1,1-k},
\]

where a term multiplied by zero is omitted. The base values are \(M_{0,0,0}=1\), \(M_{0,0,1}=0\). Both terms on the right strictly decrease weighted degree, so induction is exact for all moments. In particular,

\[
\begin{aligned}
m_2:=\mathbb E[X^2]
&=\frac{2a^2(4\gamma+3r)}{r^3(r+2\gamma)^2},\\
m_4:=\mathbb E[X^4]
&=\frac{24a^4(320\gamma^3+624\gamma^2r+426\gamma r^2+105r^3)}{r^6(r+2\gamma)^5}.
\end{aligned}
\]

A separate reconstruction uses the four-time telegraph correlation: for ordered times \(s_1\le s_2\le s_3\le s_4\),

\[
\mathbb E[S(s_1)S(s_2)S(s_3)S(s_4)]
=e^{-2\gamma[(s_2-s_1)+(s_4-s_3)]}.
\]

With \(X(T)=a\int_0^T(T-s)S(s)\,ds\), integration over the exponential age and the four ordered times gives

\[
\begin{aligned}
m_4=24a^4\int_{[0,\infty)^4}&
 e^{-(r+2\gamma)(u_1+u_3)-r(u_2+u_4)}\\
&\cdot(u_1+u_2+u_3+u_4)(u_2+u_3+u_4)
(u_3+u_4)u_4\,d\boldsymbol u .
\end{aligned}
\]

(The initial ordered-time translation integral cancels the leading factor \(r\) in the reset-age density.) This explicitly convergent integral evaluates to the displayed \(m_4\) independently of the generator recurrence. The analogous two-time integral evaluates to \(m_2\). See `CHECKER.py` for reproducible exact polynomial integration and recurrence calculations.

**3. Unique minimum and Gaussian comparison.** Substitution and cancellation give the rational expression for \(K\). Direct differentiation yields

\[
K'(z)=\frac{192(6z^3+15z^2+6z-4)}{(z+2)^2(3z+4)^3}.
\]

The derivative of the numerator cubic is \(18z^2+30z+6>0\) for every \(z>0\); its value at zero is \(-4\), and it tends to infinity. Thus there is exactly one positive root and the derivative of \(K\) changes from negative to positive there. For comparison with the complete-reset *Gaussian-white-acceleration* case, whose stationary position is an exponential-age mixture of centered Gaussians of conditional variance \(2DT^3/3\), direct integration gives \(\mathbb E[X^2]=4D/r^3\) and \(\mathbb E[X^4]=960D^2/r^6\), hence Gaussian-acceleration **excess** kurtosis \(57\). The exact difference

\[
K(z)-57=\frac{6z(15z^2+6z-16)}{(z+2)(3z+4)^2}
\]

has precisely the asserted positive crossing. The leading terms of the rational expression yield the two endpoint limits, and strict monotonicity on each side of \(z_*\) proves the two-preimage statement.

**4. Inverse ambiguity at fixed reset frequency.** Fix \(r>0\), a desired position variance \(M>0\), and any \(k\in(K(z_*),57)\). Choose its two unique preimages \(z_-<z_*<z_+<z_c\) and set \(\gamma_\pm=r/z_\pm\). Define the corresponding positive accelerations by

\[
a_\pm^2=\frac{M r^3(r+2\gamma_\pm)^2}{2(4\gamma_\pm+3r)}.
\]

Both physical parameter triples yield \(\mathbb E[X^2]=M\) and \(\mathbb E[X^4]=(k+3)M^2\), while their switching rates are different. The claim is an ambiguity of **these two moments**, not an equality of full stationary distributions or time-dependent observations.

## Verification

`CHECKER.py` is a standalone Python 3 / SymPy checker. It reconstructs \(m_2\) and \(m_4\) from a triangular generator recursion, then independently evaluates the two-point and four-point telegraph integrals; it checks the exact kurtosis formula, derivative, Gaussian comparison, endpoint limits, and unique positive critical root. The computations use exact symbolic rational algebra except for reporting numerical root approximations. The sign/uniqueness arguments and regenerative existence statement are analytical proof steps, not conclusions drawn from numerical root finding.

Run `python CHECKER.py` with SymPy installed. No finite simulation or numerical truncation is used to justify an infinite-time or all-parameter assertion.

## Relationship to prior work

Santra, Ajgaonkar and Basu (arXiv:2304.11378; first posted 2023-04-22) study *unreset* dichotomous acceleration. They derive a general time-Laplace moment representation and explicitly compute the second moment, from which the present restarted stationary second moment can also be obtained by renewal integration. This prior second-moment formula is **not claimed new**. Their analyzed trajectory, moment, and appendix sections do not state the complete-reset stationary fourth-moment kurtosis diagram or the two-to-one inverse ambiguity. Their general higher-moment representation is an applicable starting point, and therefore the underlying moment calculation alone is not treated as the contribution.

Singh (arXiv:2007.05576) studies complete and partial resetting of Gaussian-white-noise acceleration; that distinct force law provides the kurtosis-\(57\) benchmark and general renewal principle, but not the finite-telegraph-switching phase diagram. Montero, Palassini and Masoliver (arXiv:2312.13968) analyze level crossings for reset inertial random processes, not the specific all-rate stationary kurtosis/inverse fold. The assessable novelty is the **strictly unique nonmonotonicity, its exact Gaussian crossing, and the resulting moment-identifiability fold**.

## Limitations

The statements require strictly positive independent Poisson reset and sign-flip rates, equal-magnitude opposite accelerations, simultaneous complete position/velocity resetting, and an independently redrawn symmetric force sign. They do not treat partial resetting, heavy-tailed waiting times, asymmetric telegraph forces, or non-Poisson clocks. The two-to-one inverse construction concerns matching two moments only and not full-law indistinguishability. The Gaussian comparison is to a distinct white-noise-driven random acceleration with its own force intensity, not to a claim that the models have identical stationary laws. A close result in a broader unindexed work could affect publication priority; no independent external audit has been performed.

## References

1. I. Santra, D. Ajgaonkar and U. Basu, *Dichotomous acceleration process in one dimension: Position fluctuations*, first public preprint 2023-04-22, arXiv:2304.11378v1. https://arxiv.org/abs/2304.11378
2. P. Singh, *Random acceleration process under stochastic resetting*, preprint 2020-07-10, arXiv:2007.05576v1. https://arxiv.org/abs/2007.05576
3. M. Montero, M. Palassini and J. Masoliver, *The effect of stochastic resettings on the counting of level crossings for inertial random processes*, arXiv:2312.13968v1. https://arxiv.org/abs/2312.13968
