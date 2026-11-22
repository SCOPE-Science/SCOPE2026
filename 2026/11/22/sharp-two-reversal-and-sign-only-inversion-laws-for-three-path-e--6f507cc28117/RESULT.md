# Sharp two-reversal and sign-only inversion laws for three-path estuarine salinity attenuation

## Finding

**Theorem (complete positive-discharge phase diagram and threshold-only inverse).** Consider an idealized two-branch estuarine junction. For river discharge \(Q\geq0\), let the uncoupled junction salinities be
\[
S_A(Q)=a e^{-\alpha Q}+c e^{-\gamma Q},\qquad
S_B(Q)=b e^{-\beta Q},
\]
with \(a,b,c>0\) and \(0<\alpha<\beta<\gamma\). Assume the signed weak-overspill diagnostic is \(T(Q)=K(Q)[S_A(Q)-S_B(Q)]\), with an arbitrary strictly positive \(K(Q)\). The direction of \(T\), rather than its magnitude, is the observable of interest. Define
\[
p=\beta-\alpha>0,\quad q=\gamma-\beta>0,\quad
H(Q)=a e^{pQ}+c e^{-qQ},\quad H_0=a+c.
\]
If \(cq>ap\), also define
\[
Q_*={\log(cq/(ap))\over p+q}>0,\qquad
B_*=a e^{pQ_*}+c e^{-qQ_*}<H_0.
\]
The signed overspill reverses direction **twice for strictly positive discharge** if and only if
\[
\boxed{cq>ap\quad\text{and}\quad B_*<b<a+c.}
\]
In that regime there are exactly two simple thresholds \(0<Q_-<Q_*<Q_+\), with signs positive, negative, positive as \(Q\) increases through them. Outside this regime there cannot be two positive-discharge reversals. All boundary cases are classified below.

Furthermore, if \(p,q\) are calibrated, the *two threshold positions alone*, without any measurement of overspill magnitude, uniquely recover the **relative** pathway amplitudes \(a/b\) and \(c/b\). Write
\[
U_\pm=e^{pQ_\pm},\qquad V_\pm=e^{-qQ_\pm},\qquad
D=U_+V_- -U_-V_+>0.
\]
Then
\[
\boxed{{a\over b}={V_- -V_+\over D},\qquad
{c\over b}={U_+-U_-\over D}.}
\]
Every pair \(0<Q_-<Q_+\) is realized by exactly one pair of strictly positive relative amplitudes with the calibrated rates. In contrast, one crossing supplies only one linear constraint and does not determine both amplitude ratios. The common absolute salinity scale remains unidentifiable from directions alone.

At the lower two-reversal boundary, let \(b=B_*+\varepsilon\), with \(\varepsilon\downarrow0\) and \(cq>ap\) fixed. Define \(t=\sqrt{2\varepsilon/(pqB_*)}\). The two thresholds satisfy the sharp fold laws
\[
Q_\pm=Q_*\pm t-{p-q\over6}t^2+O(t^3),\qquad
Q_+-Q_-=2t+O(t^3).
\]
In the special equal-gap case \(p=q\), the midpoint identity \((Q_-+Q_+)/2=Q_*\) holds **exactly** throughout the two-reversal regime. The two-threshold inverse becomes ill-conditioned as the thresholds merge because \(D\) vanishes linearly with \(Q_+-Q_-\).

## Assumptions and scope

The model concerns steady independent positive salt contributions of **two** transport pathways reaching one channel and **one** pathway reaching the other. Each individual pathway has an exponential discharge-attenuation law with constant positive rate, representing a stylized passive advection–diffusion balance with fixed geometry and mixing. It is not the nonlinear hydrodynamic model of any particular river. River discharge is the parameter \(Q\geq0\); its units must be chosen consistently with the reciprocal units of the attenuation rates. All amplitudes have compatible salinity units. The factors \(K(Q)\) may depend on discharge but must be strictly positive at every discharge under discussion. The sign convention is positive for the first branch's uncoupled salinity exceeding the second's.

The three rates are ordered as written; if the one-path branch's rate is not strictly between the other two, the relative salinity difference is monotone after division by its strictly positive exponential factor and **at most one** positive-discharge reversal is possible. Likewise, if each branch has a single exponential mode, at most one positive reversal is possible. These are minimal pathway-complexity statements, not claims about arbitrary three-dimensional estuarine dynamics.

## Proof

**1. Reduction and classification.** Factor out the positive term \(K(Q)e^{-\beta Q}\):
\[
T(Q)=K(Q)e^{-\beta Q}[H(Q)-b].
\]
Now \(H'(Q)=ap e^{pQ}-cq e^{-qQ}\) and \(H''(Q)=ap^2e^{pQ}+cq^2e^{-qQ}>0\). Thus \(H'\) is strictly increasing. If \(cq\le ap\), \(H'\ge0\) on \(Q\ge0\), strictly positive for \(Q>0\), and \(H\) starts at \(H_0\) and increases to infinity. This yields no strictly positive zero for \(b\le H_0\) and exactly one simple strictly positive zero for \(b>H_0\); if \(b=H_0\), its only zero is the excluded boundary \(Q=0\).

If \(cq>ap\), the unique minimum of \(H\) on the nonnegative axis is attained at \(Q_*>0\), with \(B_*<H_0\). Its range on \([0,Q_*]\) decreases strictly from \(H_0\) to \(B_*\); on \([Q_*,\infty)\) it increases strictly from \(B_*\) to infinity. Consequently: \(b<B_*\) gives no zero; \(b=B_*\) gives one tangential positive zero with no direction reversal; \(B_*<b<H_0\) gives two simple positive zeros; \(b=H_0\) gives a zero at \(Q=0\) plus exactly one simple positive zero; and \(b>H_0\) gives exactly one simple positive zero. This is exhaustive and includes equality boundaries. When two roots exist, strict convexity gives the stated sign order.

If \(\beta\le\alpha\), division by \(e^{-\beta Q}\) yields \(a e^{-(\alpha-\beta)Q}+c e^{-(\gamma-\beta)Q}-b\), a nonincreasing, and except degenerate equalities strictly decreasing, function. If \(\beta\ge\gamma\), both exponentials in the corresponding bracket are nondecreasing. Hence rates that do not interlace cannot produce two reversals. In a two-pathway total model, the analogous bracket has one exponential term and a constant, also giving at most one reversal.

**2. Inverse identification and realizability.** At each threshold, division by \(b>0\) gives
\[
(a/b)U_-+(c/b)V_-=1,\qquad
(a/b)U_++(c/b)V_+=1.
\]
Since \(Q_+>Q_-\), \(U_+>U_-\) and \(V_->V_+\). The determinant \(D=U_+V_- -U_-V_+>0\), and Cramer's rule gives the displayed, strictly positive solution. Conversely, for any distinct strictly positive proposed thresholds, these positive coefficients solve the equations. Strict convexity makes the two solutions the only zeros and forces the intervening minimum and the positive–negative–positive direction pattern; because the first root is positive, the value at zero must exceed the root level. Thus every ordered threshold pair is realizable and the pair of amplitude ratios is unique. With only one threshold, one linear equation leaves a positive open line segment of ratio pairs; unknown common scaling is not resolved even with two thresholds.

**3. Fold and conditioning.** At the minimum, set \(A=a e^{pQ_*}\) and \(C=c e^{-qQ_*}\). The stationary equation gives \(pA=qC\). It follows exactly that \(H''(Q_*)=pq(A+C)=pqB_*\) and \(H'''(Q_*)=pq(p-q)B_*\). Taylor expansion yields
\[
H(Q_*+x)=B_*+{pqB_*\over2}x^2+{pq(p-q)B_*\over6}x^3+O(x^4).
\]
Solving the local equation \(H(Q_*+x)=B_*+\varepsilon\) on its two strictly monotone sides by Taylor inversion gives \(x=\pm t-(p-q)t^2/6+O(t^3)\), hence the fold laws. If \(p=q\), stationarity gives \(a e^{pQ_*}=c e^{-pQ_*}\), so \(H(Q_*+x)=2\sqrt{ac}\cosh(px)\) is exactly even, implying exact midpoint symmetry. Finally,
\[
D=e^{pQ_- -qQ_+}\left(e^{(p+q)(Q_+-Q_-)}-1\right),
\]
which is strictly positive and tends to zero linearly with the gap \(Q_+-Q_-\). Thus the two-equation coefficient recovery has a diverging inverse-matrix norm as the thresholds coalesce. No stochastic noise amplification claim is made without a noise model.

## Verification

An exact illustrative case is \((\alpha,\beta,\gamma)=(1,2,3)\), \((a,b,c)=(1,9/2,4)\). Here \(p=q=1\), \(Q_*=\log2\), \(B_*=4\), and \(H_0=5\). The two thresholds are
\[
Q_\pm=\log\left({9\pm\sqrt{17}\over4}\right)
=0.198214257465\ldots,\ 1.188080103654\ldots .
\]
They give an exact sign pattern \(+,-,+\). A standalone standard-library Python checker, `check.py`, checks the phase classification over 5,000 deterministic pseudorandom admissible settings, inversions in 212 two-threshold cases, exact witness identities, and five small-fold comparisons. Execute `python3 check.py` next to this document. The theorem is proved analytically; finite numerical checks do not certify its infinite quantifiers or historical priority.

## Relationship to prior work

Biemond, de Swart and Dijkstra (2023) derive a signed salt-overspill proxy proportional to the difference between separate-channel junction salinities, where the depth-averaged currents in both seawards channels flow toward the sea and overspill is small relative to downstream salt transport. Their physical model is more sophisticated: it uses channel geometry, hydrodynamic exchange and diffusive regimes, and its single-channel estimates can select the *larger* of two separate limits; it does **not** assert the additive three-path exponential model used here. Their work supplies the motivating observable, not this theorem. Cai and colleagues (2023) study spatial salinity-profile inference from salinity measurements and do not address directional-switch-only recovery of pathway amplitudes. Dijkstra and colleagues (2023) model stochastic salinity-intrusion statistics, not this phase diagram. Classical generalized Descartes/zero-count principles already bound zeros of a short exponential sum; merely observing that there are at most two roots is **not** claimed as original. Chauveau and colleagues (1996) also study recovering *signed exponential mixtures from complete functions or finite noisy measurements*; their accessible abstract does not establish inversion specifically from two **zero positions alone**, and the full text was not available for a decisive comparison. The assessed contribution is the discharge-constrained amplitude window, sharp fold geometry and minimal sign-only inverse *in this explicitly motivated salt-proxy class*.

## Limitations

The theorem does not establish empirical existence of two reversals, validate constant attenuation rates, determine absolute salinity scale, identify uncalibrated decay rates, or handle noisy discharge thresholds. It does not apply directly when one of the channel-averaged mean currents points upstream, when the overspill coefficient changes sign, when exchange/diffusion processes interact non-additively, or when salinities are controlled by changing tides, channel geometry, nonstationarity or stratification. Even when two switches are mathematically present, the inverse matrix is ill-conditioned near coalescence. Classical mathematical priority for more abstract formulations may be broader than the directly inspected sources. No independent verification has been performed.

## References

1. Biemond, B., de Swart, H. E., and Dijkstra, H. A. (2023), *Mechanisms of Salt Overspill at Estuarine Network Junctions Explained With an Idealized Model*, Journal of Geophysical Research: Oceans 128, e2023JC019630. First published 9 March 2023. https://doi.org/10.1029/2023JC019630
2. Cai, H., Li, B., Gu, J., Zhao, T., and Garel, E. (2023), *Extension of the general unit hydrograph theory for the spread of salinity in estuaries*, Ocean Science 19, 603–614. https://doi.org/10.5194/os-19-603-2023
3. Dijkstra, H. A., Biemond, B., Lee, J., and de Swart, H. E. (2023), *Explaining the Statistical Properties of Salt Intrusion in Estuaries Using a Stochastic Dynamical Modeling Approach*, Water Resources Research 59, e2023WR034454. https://doi.org/10.1029/2023WR034454
4. Jameson, G. J. O. (2006), *Counting zeros of generalised polynomials: Descartes’ rule of signs and Laguerre’s extensions*, Mathematical Gazette 90(518), 223–234. https://doi.org/10.1017/S0025557200179628
5. Chauveau, D., Martin, C. F., van Rooij, A. C. M., and Ruymgaart, F. H. (1996), *Discrete signed mixtures of exponentials*, Communications in Statistics: Stochastic Models 12(2), 245–263. https://doi.org/10.1080/15326349608807383 (abstract available; full article not inspected)
