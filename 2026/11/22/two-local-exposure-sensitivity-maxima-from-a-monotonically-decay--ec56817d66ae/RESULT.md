# Two local exposure-sensitivity maxima from a monotonically decaying two-timescale stellar transient

## Finding
For a post-peak transient with two positive exponential cooling components, a background-noise-limited exposure score can have two separate strict local maxima, even though the instantaneous source flux is strictly decreasing. Two is the sharp universal maximum for this two-component model; a one-component exponential permits only one maximum.

Precisely, fix \(a,b,\lambda,\mu>0\) with \(\lambda<\mu\) and define
\[
I(t)=a e^{-\lambda t}+b e^{-\mu t},\qquad
E(T)=\int_0^T I(t)\,dt=\frac a\lambda(1-e^{-\lambda T})+\frac b\mu(1-e^{-\mu T}),\qquad
S(T)=\frac{E(T)}{\sqrt T}\quad(T>0).
\]
Then \(S\) has at most two strict local maxima. This bound is realized by \(a=1\), \(b=5\), \(\lambda=1\), \(\mu=30\). For every positive single-exponential model, \(S\) has exactly one strict local maximum.

## Assumptions and scope
The observation starts at the decay onset and integrates the full positive excess signal \(I\); the background variance is proportional to exposure duration and dominates the source shot noise. The source is deterministic and the noise scale is constant, so maximizing the dimensionless score \(E(T)/\sqrt T\) suffices. There is no dead time, read-noise term, telescope overhead, random start-time error, additional peak or source variability. Units of the two decay rates are reciprocal units of time. This statement classifies possible *local* maxima, not their observational attainability with a particular instrument.

## Proof
Let
\[
N(T)=2T I(T)-E(T),\qquad S'(T)=\frac{N(T)}{2T^{3/2}}.
\]
Note \(N(0)=0\), \(N(T)=(a+b)T+O(T^2)>0\) near zero and \(N(T)\to-a/\lambda-b/\mu<0\) as \(T\to\infty\). We claim that \(N\) has at most three distinct positive zeros.

Differentiating gives
\[
N'(T)=a(1-2\lambda T)e^{-\lambda T}+b(1-2\mu T)e^{-\mu T}.
\]
Put \(d=\mu-\lambda>0\) and multiply by \(e^{\lambda T}\), leaving
\[
F(T)=e^{\lambda T}N'(T)=a(1-2\lambda T)+b(1-2\mu T)e^{-dT}.
\]
Its second derivative is
\[
F''(T)=b d e^{-dT}\bigl(d+4\mu-2\mu dT\bigr).
\]
It has exactly one zero over the real line, hence at most one zero on \((0,\infty)\). If \(F\) had four distinct positive zeros, repeated Rolle arguments would force \(F''\) to have at least two distinct positive zeros, a contradiction. Thus \(N'\) has at most three distinct positive zeros. If \(N\) had four distinct positive zeros, its zero at \(T=0\) would, by Rolle, force at least four distinct positive zeros of \(N'\); impossible. Hence \(N\) has at most three distinct positive zeros. Four alternating derivative signs would require four extrema, but four local extrema need at least four distinct positive critical points; so two strict maxima are the maximum possible (a third would require at least five positive critical points between their intervening minima). The same zero bound rules out a third maximum in any degenerate tangency scenario.

For the claimed sharp example, \(I(T)=e^{-T}+5e^{-30T}\), \(E(T)=7/6-e^{-T}-e^{-30T}/6\), and
\[
N(T)=(2T+1)e^{-T}+(10T+1/6)e^{-30T}-7/6.
\]
Exact rational interval bounds obtained from alternating Taylor polynomials imply
\[
N(1/20)>0,\qquad N(1/8)<0,\qquad N(1/3)>0,\qquad N(1)<0.
\]
By continuity, the three disjoint intervening intervals each contain at least one zero. The proved bound forces exactly one in each interval, with the indicated sign changes; they are respectively a strict maximum, a strict minimum and a strict maximum of \(S\). In particular, the count of local maxima equals two and the upper bound is sharp.

For a single exponential \(I(T)=a e^{-\lambda T}\), the derivative \(N'(T)=a e^{-\lambda T}(1-2\lambda T)\) is positive before \(T=1/(2\lambda)\) and negative thereafter. Since \(N(0)=0\) and \(N(\infty)=-a/\lambda\), \(N\) crosses zero exactly once at positive \(T\), which is the unique strict local (and global) maximum of \(S\).

## Verification
Run `python checker.py` with Python's standard library. It evaluates four rigorously enclosing *rational* intervals for \(N\) at the exact specified times, using alternating Taylor sums for \(e^{-x/128}\) at truncation degrees 16 and 17, raised to the 128th power. The upper-minus-lower widths are below \(10^{-35}\) for the four checks and all signs have margins exceeding \(0.02\). The exact inequalities are certificates for the explicit example; the universal upper bound follows from the analytic Rolle argument, not numerical sampling.

## Relationship to prior work
Davenport and colleagues (2014) provide a two-exponential astronomical flare decay template, including their equation (4), and an analysis of observational time profiles; that paper treats morphological fitting rather than maximizing the exposure score defined here. Bruno and colleagues (2024) discuss flare morphology and the importance of observing cadence; their accessible abstract does not assert an exposure-optimization classification. Williams and Rovnyak (2014) analyze an optimal acquisition duration for a monoexponential signal under noise, a relevant one-component antecedent. The exponential-polynomial zero bound and Rolle's theorem are standard analytic tools and are *not* claimed as original. The delimited result assessed here is the exact two-local-maximum ceiling together with a positive two-mode realization under the stated exposure functional. An exact universal literature-priority claim is not made.

## Limitations
The explicit witness is mathematical and is not a fit to the real stellar flares described by the cited papers; it demonstrates possibility, not typicality. The noise formula excludes source shot noise and read noise, and actual instruments have finite cadence and overheads. The 2024 motivating article was accessible at abstract level, not in full text. The mathematical upper bound does not extend by this proof to arbitrary multi-peak flare profiles or time-varying backgrounds. External independent validation and exhaustive historical priority review have not been performed.

## References
1. Davenport et al. (2014), *Kepler Flares II: The Temporal Morphology of White-Light Flares on GJ 1243*, https://arxiv.org/html/1411.3723v1 , especially Section III.2 and Equation (4).
2. Bruno et al. (2024), *Detailed cool star flare morphology with CHEOPS and TESS*, first publicly posted 2024-03-25, https://arxiv.org/abs/2403.17065 .
3. Williams and Rovnyak (2014), *A Closed-Form Solution for the Optimal Time Evolution of an Exponentially Decaying Signal with Thermal Noise*, https://digitalcommons.bucknell.edu/fac_journ/867/ .
