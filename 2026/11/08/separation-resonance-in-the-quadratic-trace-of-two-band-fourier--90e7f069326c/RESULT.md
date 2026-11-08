# Separation resonance in the quadratic trace of two-band Fourier concentration

## Finding
Let \(L,W>0\), let \(c>W/2\), and let \(I=[-L/2,L/2]\). Set
\[
B_{\pm}(c)=[\pm c-W/2,\pm c+W/2],\qquad B(c)=B_-(c)\cup B_+(c).
\]
With Fourier transform \(\widehat f(\xi)=\int_{\mathbb R} f(x)e^{-2\pi i x\xi}\,dx\), let \(T_c=\mathbf1_I\mathcal F^{-1}\mathbf1_{B(c)}\mathcal F\mathbf1_I\) on \(L^2(\mathbb R)\). Its nonzero eigenvalues lie in \((0,1)\), and its quadratic spectral defect is \(D(c)=\operatorname{tr}(T_c-T_c^2)=\sum_j\lambda_j(c)(1-\lambda_j(c))\). Let \(T_0^{\mathrm{one}}\) denote the single-band operator for \([-W/2,W/2]\), and put \(D_{\infty}=2\operatorname{tr}(T_0^{\mathrm{one}}-(T_0^{\mathrm{one}})^2)\).

The exact interaction \(J(c)=(D_{\infty}-D(c))/2\) is strictly positive and has both representations
\[
J(c)=\int_{-W}^{W}(W-|h|)\frac{\sin^2(\pi L(2c+h))}{\pi^2(2c+h)^2}\,dh
=W^2\int_{-L}^{L}(L-|t|)\operatorname{sinc}^2(Wt)e^{4\pi ict}\,dt,
\]
where \(\operatorname{sinc}(y)=\sin(\pi y)/(\pi y)\), continuously extended by \(1\) at zero. In particular, \(0<D_{\infty}-D(c)\) for every finite disjoint-band spacing.

Define the explicit dimensionless resonance amplitude
\[
A(L,W)=\operatorname{sinc}^2(LW)\in[0,1).
\]
For fixed \(L,W>0\), as \(c\to\infty\),
\[
J(c)=\frac{W^2}{8\pi^2c^2}\left[1-A(L,W)\cos(4\pi Lc)\right]+O_{L,W}(c^{-3}),
\]
so the full set of subsequential limits of \(4\pi^2c^2(D_{\infty}-D(c))/W^2\) is exactly \([1-A(L,W),\,1+A(L,W)]\).

The following **complete eventual-monotonicity dichotomy** holds.

* If \(LW\in\mathbb N\), then \(J(c)=W^2/(8\pi^2c^2)+O_{L,W}(c^{-4})\) and \(J'(c)=-W^2/(4\pi^2c^3)+O_{L,W}(c^{-4})<0\) for all sufficiently large \(c\). Hence \(D(c)\) is eventually strictly increasing toward \(D_{\infty}\).
* If \(LW\notin\mathbb N\), then \(J'(c)=LW^2A(L,W)\sin(4\pi Lc)/(2\pi c^2)+O_{L,W}(c^{-3})\). For all sufficiently large integers \(k\), \(J'\) has exactly one zero \(c_k=k/(4L)+O_{L,W}(k^{-1})\) near \(k/(4L)\), and no other sufficiently large zeros. The extrema alternate: even \(k\) give strict local minima of \(J\), and odd \(k\) strict local maxima. Thus neither \(J(c)\) nor \(D(c)\) is eventually monotone.

The integer/noninteger boundary concerns the time-bandwidth product of an individual band, not an integer quantization of the center frequency. The leading inverse-square interaction persists in both regimes; only its order-leading oscillation vanishes at integer product.

## Assumptions and scope
The time and frequency domains are real intervals with Lebesgue measure, the two frequency bands have the same fixed positive width \(W\), their centers are \(\pm c\), and their disjointness is \(2c>W\). All asymptotic statements keep \(L,W\) fixed. The operator is the ordinary continuous Fourier concentration operator, not a Gabor or Gaussian localization operator. The eigenvalues are counted with multiplicity.

## Proof
**1. Trace and interaction.** Write \(T_c=T_-+T_+\), with \(T_\pm=\mathbf1_I\mathcal F^{-1}\mathbf1_{B_\pm(c)}\mathcal F\mathbf1_I\). Bounded spatial and frequency domains make these positive trace-class contractions. Each \(T_\pm\) is a modulation conjugate of \(T_0^{\mathrm{one}}\), so \(\operatorname{tr}T_c=2LW\), \(\operatorname{tr}(T_\pm^2)=\operatorname{tr}((T_0^{\mathrm{one}})^2)\), and
\[
\operatorname{tr}(T_c^2)=2\operatorname{tr}((T_0^{\mathrm{one}})^2)+2\operatorname{tr}(T_-T_+).
\]
Plancherel and Tonelli give
\[
\operatorname{tr}(T_-T_+)=\int_{B_-}\!\int_{B_+}\left|\widehat{\mathbf1_I}(\eta-\xi)\right|^2\,d\eta\,d\xi.
\]
The Fourier transform of \(\mathbf1_I\) is \(L\operatorname{sinc}(L\zeta)\). Changing variables \(\eta-\xi=2c+h\) yields the first exact formula. Its integrand is nonnegative and not almost everywhere zero, so \(J>0\). Alternatively, multiply the two modulated sinc kernels on \(I\times I\), then integrate over differences \(t=x-y\); this gives the second formula. These identities prove \(D(c)=D_\infty-2J(c)\). The strict spectral bounds \(\lambda_j(c)<1\) follow because no nonzero function can be simultaneously compactly supported in time and exactly bandlimited; the Hilbert–Schmidt/trace-class argument gives summability of the defect.

**2. Sharp first asymptotic and its complete cluster set.** Put \(\tau(h)=(W-|h|)\mathbf1_{[-W,W]}(h)\) and \(\theta=4\pi Lc\). The triangle-function Fourier identity is
\[
\int\tau(h)\,dh=W^2,\quad \int\tau(h)\cos(2\pi Lh)\,dh=W^2\operatorname{sinc}^2(LW),\quad \int\tau(h)\sin(2\pi Lh)\,dh=0.
\]
For \(c>W\), \((2c+h)^{-2}=(4c^2)^{-1}+O_W(c^{-3})\) uniformly on the fixed integration domain. Apply \(\sin^2 y=(1-\cos(2y))/2\) and these three triangle identities to get the claimed uniform \(O_{L,W}(c^{-3})\) expansion. Since \(c\) is real and unbounded, \(\cos(4\pi Lc)\) assumes every value in \([-1,1]\) along sequences tending to infinity. This proves the exact cluster interval.

**3. Differentiability and the noninteger oscillation.** For \(2c>W\), differentiating under the compact integral is valid. The exact derivative is
\[
J'(c)=\int_{-W}^W\!\tau(h)\left[\frac{2L\sin(2\pi L(2c+h))}{\pi(2c+h)^2}-\frac{4\sin^2(\pi L(2c+h))}{\pi^2(2c+h)^3}\right]dh.
\]
The triangle identity immediately yields the derivative asymptotic in the finding; differentiating once more yields
\[
J''(c)=\frac{2L^2W^2 A(L,W)}{c^2}\cos(4\pi Lc)+O_{L,W}(c^{-3}).
\]
For \(A>0\), choose disjoint fixed small phase-neighborhoods of \(k\pi\). Outside those neighborhoods the sign of \(J'\) agrees with \(\sin\theta\) for large \(c\); inside each neighborhood the sign of \(J''\) is that of \((-1)^k\), so \(J'\) has exactly one simple zero there. From the derivative estimate, its displacement in \(c\) from \(k/(4L)\) is \(O(k^{-1})\). Its extremum type follows from \(J''\). As \(L,W>0\), \(A=0\) is equivalent to \(LW\in\mathbb N\).

**4. Integer resonance.** Let \(F(s)=W^2\operatorname{sinc}^2(Ws)\). The first and second Fourier moments of \(\tau\) satisfy \(F(L)=\int\tau(h)\cos(2\pi Lh)dh\) and \(F'(L)=-2\pi\int h\tau(h)\sin(2\pi Lh)dh\). For integer \(LW\), both \(F(L)\) and \(F'(L)\) vanish. Expand \((2c+h)^{-2}\) through its term linear in \(h\); the constant term contributes \(W^2/(8\pi^2c^2)\), the first-order term vanishes by evenness together with \(F'(L)=0\), and the remainder is \(O(c^{-4})\). In the exact derivative formula above, its oscillatory first bracket has no terms of orders \(c^{-2}\) or \(c^{-3}\) by the same two vanishing Fourier moments; the nonoscillatory second bracket contributes \(-W^2/(4\pi^2c^3)\) with remainder \(O(c^{-4})\). The derivative is therefore strictly negative for all sufficiently large \(c\).

## Verification
The standalone script `check.py` evaluates the independent time-domain and frequency-domain integrals using numerical quadrature, differentiates the frequency representation numerically, compares both with the exact differentiated formula, and checks the asymptotic and derivative sign examples for integer and noninteger time-bandwidth products. Run `python check.py` with Python 3 and SciPy. It prints `TWO_BAND_TRACE_CHECKS_PASS 117` when all tests pass. These finite tests support the identities; all quantified statements and eventual properties follow from the proof above, not from the tests.

## Relationship to prior work
Marceca–Romero–Speckbacher (arXiv:2301.11685, first public January 27, 2023) establish threshold-robust concentration-eigenvalue bounds for general domains, including nonconvex geometry, and use trace defect as a spectral deviation tool. They do not provide the fixed-time, large-separation interaction coefficient or its integer-product dichotomy in the inspected main results and trace discussion. Israel–Mayeli (arXiv:2301.09616, first public January 23, 2023) investigate eigenvalue distribution under growing dilations and higher-dimensional geometric assumptions, a different regime. Lakey–Hogan (SampTA 2013, pp. 532–535) give multiband prolate matrix methods and a bandpass example, but not the asymptotic decay and eventual monotonicity characterization developed here. SenGupta–Sun–Jiang–Chen–Mariani (Journal of Fourier Analysis and Applications 18 (2012), 182–210) study these bandpass concentration operators; its abstract and bibliographic record were accessible, but its full text was not, so possible implicit or explicit earlier coverage there remains an unresolved historical-priority risk. This work is a fixed-geometry exact quadratic trace result, not a pointwise spectral-eigenvalue ordering theorem.

## Limitations
Only two equal-width symmetric frequency intervals and one time interval are treated. The theorem does not characterize individual eigenvalues, optimizing signals, higher Schatten moments, asymmetric bands, or varying time and bandwidth scales. The thresholds for eventual behavior depend on fixed \(L,W\), and no uniform near-integer estimate is asserted. The result is internally checked but has not received independent mathematical validation. Earlier bandpass-operator literature may contain an equivalent result under different terminology.

## References
1. F. Marceca, J. L. Romero, M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685 (2023), https://arxiv.org/abs/2301.11685.
2. A. Israel, A. Mayeli, *On the Eigenvalue Distribution of Spatio-Spectral Limiting Operators in Higher Dimensions*, arXiv:2301.09616 (2023), https://arxiv.org/abs/2301.09616.
3. J. Lakey, J. A. Hogan, *Sampling aspects of approximately time-limited multiband and bandpass signals*, SampTA 2013, pp. 532–535, https://new.eurasip.org/Proceedings/Ext/SampTA2013/papers/p532-lakey.pdf.
4. I. SenGupta, B. Sun, W. Jiang, G. Chen, M. C. Mariani, *Concentration Problems for Bandpass Filters in Communication Theory over Disjoint Frequency Intervals and Numerical Solutions*, J. Fourier Anal. Appl. 18 (2012), 182–210, https://doi.org/10.1007/s00041-011-9197-y.
