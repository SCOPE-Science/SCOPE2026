# Resonant monotonicity of sine-kernel coupling between two unequal intervals

## Finding
Fix three real parameters \(a,b,W>0\) with \(a\ne b\). For a center separation \(D>(a+b)/2\), put
\[
A_D=[-a/2,a/2]\cup[D-b/2,D+b/2]
\]
and let \(S_D=\mathbf 1_{A_D}P_{[-W,W]}\mathbf 1_{A_D}\), where \(P_{[-W,W]}\) is the orthogonal Fourier multiplier by the indicator of \([-W,W]\), using \(\widehat f(\xi)=\int_\mathbb R f(x)e^{-ix\xi}\,dx\) and inverse factor \(1/(2\pi)\). Define the quadratic transition defect \(\mathcal D(D)=\operatorname{tr}(S_D-S_D^2)\). Let \(\mathcal D_a\) and \(\mathcal D_b\) be the corresponding defects for the isolated intervals of lengths \(a\) and \(b\).

The interaction \(J(D)=(\mathcal D_a+\mathcal D_b-\mathcal D(D))/2\) is positive and exactly equals
\[
J(D)=\frac{1}{\pi^2}\int_{-a/2}^{a/2}\int_{-b/2}^{b/2}
\frac{\sin^2(W(D+v-u))}{(D+v-u)^2}\,dv\,du.
\]
Put \(B=\sin(Wa)\sin(Wb)/W^2\), and \(B'=\left.\frac{d}{dt}\left(4\sin(at/2)\sin(bt/2)/t^2\right)\right|_{t=2W}\). Then, as \(D\to\infty\) with \(a,b,W\) fixed,
\[
J(D)=\frac{ab-B\cos(2WD)}{2\pi^2D^2}+O_{a,b,W}(D^{-3}),
\]
\[
J'(D)=\frac{WB\sin(2WD)}{\pi^2D^2}
+\frac{-ab+(B+2WB')\cos(2WD)}{\pi^2D^3}
+O_{a,b,W}(D^{-4}).
\]
In particular, the complete set of accumulation points of \(D^2J(D)\) is
\[
\left[\frac{ab-|B|}{2\pi^2},\frac{ab+|B|}{2\pi^2}\right].
\]
The following is an exact classification, **including the unequal-width mixed-resonance case**:

* If \(\sin(Wa)\sin(Wb)\ne0\), the interaction has, beyond some finite separation, exactly one stationary point near each \(D_k=k\pi/(2W)\), with \(D_k^*=D_k+O_{a,b,W}(k^{-1})\). These alternate strictly between maxima and minima. Thus \(\mathcal D(D)\) is not eventually monotone.
* If \(\sin(Wa)\sin(Wb)=0\), then \(J'(D)<0\) for all sufficiently large \(D\), and \(\mathcal D(D)\) increases strictly to \(\mathcal D_a+\mathcal D_b\). **A resonance in either one of the two unequal interval lengths is sufficient**; it need not occur in both.

The same statements hold under time-frequency duality for two unequal disjoint frequency bands observed on one centered time interval, with the parameters rescaled consistently with the Fourier convention. The equal-width specialization is included only as a consistency check, not as an originality claim.

## Assumptions and scope
All intervals are measurable intervals of positive finite length, and \(D>(a+b)/2\) ensures disjointness. The band is symmetric and has positive half-width \(W\); \(a,b,W\) remain fixed as \(D\to\infty\). The principal claim concerns \(a\ne b\); no finite uniform threshold as \(\sin(Wa)\sin(Wb)\to0\) is asserted. The defect is the summed quantity \(\sum_j\lambda_j(1-\lambda_j)\) for the nonzero eigenvalues of the positive trace-class contraction \(S_D\). No result about the ordering of individual eigenvalues is implied.

## Proof
**Trace decomposition and normalization.** The frequency projection has convolution kernel \(K_W(x-y)=\sin(W(x-y))/(\pi(x-y))\), with value \(W/\pi\) at zero. The restricted operator \(S_D\) is a positive trace-class contraction, since it factors as the product of a Hilbert–Schmidt time-frequency restriction and its adjoint. Its first trace is \(W(a+b)/\pi\); the separated diagonal blocks are unitarily translates of the respective one-interval operators. Since \(\operatorname{tr}(S_D^2)=\int_{A_D^2}|K_W(x-y)|^2\,dx\,dy\), splitting that integral into two diagonal and two off-diagonal rectangles gives \(\mathcal D(D)=\mathcal D_a+\mathcal D_b-2J(D)\). The integrand is nonnegative and not almost everywhere zero, proving \(J(D)>0\).

**The Fourier moment and the sharp oscillatory envelope.** Let \(s=v-u\), \(\theta=2WD\), and define
\[
F(t)=\int_{-a/2}^{a/2}\int_{-b/2}^{b/2}e^{it(v-u)}\,dv\,du
=\frac{4\sin(at/2)\sin(bt/2)}{t^2}.
\]
The function \(F\) is real and even, and \(F(2W)=B\). Because \(|s|\le(a+b)/2\), the expansion \((D+s)^{-2}=D^{-2}+O(D^{-3})\) is uniform, including upon taking one or two derivatives with respect to \(D\) after differentiating the exact integrand. The identity \(\sin^2 z=(1-\cos(2z))/2\), together with the real and even moment \(F\), gives the first displayed expansion. Along sequences satisfying \(\cos(2WD)\to\pm1\), and indeed any prescribed cosine limit in \([-1,1]\), it gives every value of the claimed sharp cluster interval, with no others.

**Derivative through cubic order.** Differentiation under the compact double integral gives
\[
J'(D)=\frac1{\pi^2}\iint
\left\{\frac{W\sin(2W(D+s))}{(D+s)^2}
-\frac{1-\cos(2W(D+s))}{(D+s)^3}\right\}\,dv\,du.
\]
For \(|s|\le(a+b)/2\), uniformly
\[(D+s)^{-2}=D^{-2}-2sD^{-3}+O(D^{-4}),\qquad (D+s)^{-3}=D^{-3}+O(D^{-4}).\]
Evenness yields \(\iint\sin(\theta+2Ws)=B\sin\theta\) and \(\iint s\sin(\theta+2Ws)=-F'(2W)\cos\theta\). Substitution proves the stated two-order derivative expansion. Differentiating the exact compact integral one more time yields
\[
J''(D)=\frac{2W^2 B}{\pi^2 D^2}\cos(2WD)+O_{a,b,W}(D^{-3}).
\]
If \(B\ne0\), the leading sine changes sign at successive half-periods. On every sufficiently large fixed small phase-neighborhood of \(k\pi\), the leading cosine in \(J''\) has constant nonzero sign, forcing at most one stationary point; sign change of \(J'\) at the neighborhood endpoints ensures existence. Outside these neighborhoods \(|\sin\theta|\) has a uniform positive lower bound, so no further stationary points occur. The derivative expansion gives displacement \(O(k^{-1})\). The signs of \(J''\) alternate, establishing strict alternating extrema.

**The exact resonance boundary.** The condition \(B=0\) means \(\sin(Wa)=0\) or \(\sin(Wb)=0\). In the first case, differentiating \(F\) explicitly gives
\[
2WF'(2W)=\frac{a\cos(Wa)\sin(Wb)}{W},
\]
so \(|2WF'(2W)|\le a|\sin(Wb)|/W<ab\), by the strict inequality \(|\sin z|<z\) for every \(z>0\). The second case is symmetric; if both sine factors vanish, then \(F'(2W)=0\). Therefore \(\delta=ab-|2WF'(2W)|>0\). The derivative expansion becomes
\[
J'(D)=\frac{-ab+2WF'(2W)\cos(2WD)}{\pi^2D^3}+O(D^{-4})
\le-\frac{\delta}{\pi^2D^3}+O(D^{-4})<0
\]
for all sufficiently large \(D\), uniformly over the phase. This proves the opposite implication and finishes the classification. Finally, \(J(D)\to0\) from the first expansion, proving convergence of the defect to the separate-interval sum.

## Verification
The executable `check.py` uses SymPy to independently differentiate the exact two-interval Fourier moment; one-dimensional SciPy quadrature of the overlap density to check the exact integral and its derivative against numerical finite differences; four parameter families to compare both asymptotic expansions; two nonresonant families to bracket alternating stationary points; and singly and doubly resonant families to verify eventual negative derivatives at sampled separations. Running `python check.py` from a directory containing the script yields `SINE_TWO_WINDOW_CHECKS_PASS 132` in the stated Python/SciPy/SymPy environment. These finite tests are supplementary only: the uniform expansions, strict inequalities, existence and uniqueness of all sufficiently late stationary points are proved analytically above.

## Relationship to prior work
Azimifard, arXiv:2609.14946, September 14, 2026, develops componentwise time-frequency concentration bounds and exact general trace-defect/cross-boundary identities. Those identities support the starting integral but do not give the two-unequal-interval resonance condition or the complete eventual-monotonicity classification; the relevant introductory, separation, and Section 8 material was inspected. The public November 8, 2026 record *Separation resonance in the quadratic trace of two-band Fourier concentration* determines the **equal-width** two-band case. Under Fourier duality, its quantitative trace result is covered by the \(a=b\) specialization of our formulas; that specialization is not new. Its equal-width assumption does not imply the present asymmetric fact that resonance of either interval alone suppresses every sufficiently late oscillation. SenGupta et al., *J. Fourier Anal. Appl.* 18 (2012), examine symmetric disjoint bandpass intervals and eigenvalue methods and explicitly discuss limits of their treatment for nonsymmetric intervals. No directly covering asymmetric asymptotic/monotonicity theorem was located in the material inspected. A previously unindexed derivation from the general trace identity remains a bibliographic risk.

## Limitations
The result is about the quadratic spectral defect and off-diagonal Hilbert–Schmidt interaction, not the norm or individual eigenvalues of the concentration operator. It treats one contiguous frequency band and two unequal spatial intervals (equivalently two unequal frequency bands and a single spatial interval), with all widths held fixed. It gives no uniform separation threshold near resonance, no higher Schatten-moment estimate, and no inverse reconstruction theorem. The expansion is elementary once the trace interaction is isolated; older analysis of general multiband prolate operators could contain an equivalent result. Independent validation has not been performed.

## References
1. A. Azimifard, *Componentwise and Measure-Sensitive Bounds for One-Dimensional Time-Frequency Localization*, arXiv:2609.14946, first published September 14, 2026, https://arxiv.org/abs/2609.14946.
2. *Separation resonance in the quadratic trace of two-band Fourier concentration*, public mathematical record of November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-separation-resonance-in-the-quadratic-trace-of-two-band-fourier--90e7f069326c.
3. I. SenGupta, B. Sun, W. Jiang, G. Chen, M. C. Mariani, *Concentration Problems for Bandpass Filters in Communication Theory over Disjoint Frequency Intervals and Numerical Solutions*, *Journal of Fourier Analysis and Applications* **18** (2012), 182–210, https://doi.org/10.1007/s00041-011-9197-y.
4. A. Azimifard, *Entropy-type traces and moment expansions for the sine-kernel time-band limiting operator*, arXiv:2608.17338, first published August 18, 2026, https://arxiv.org/abs/2608.17338.
