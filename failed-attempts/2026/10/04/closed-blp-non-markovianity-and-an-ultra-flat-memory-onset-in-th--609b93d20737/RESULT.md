# Closed BLP non-Markovianity and an ultra-flat memory onset in the resonant damped Jaynes–Cummings model

## Finding

Consider the resonant zero-temperature Lorentzian damped Jaynes--Cummings model. Let
\[
\Gamma>0
\]
be the reservoir spectral width and
\[
\gamma_0>0
\]
the Markovian decay scale.

In the non-Markovian regime
\[
\gamma_0>\frac{\Gamma}{2},
\]
define
\[
\kappa=\sqrt{2\gamma_0\Gamma-\Gamma^2}.
\]
The optimized Breuer--Laine--Piilo trace distance found for the resonant amplitude-damping channel is
\[
D_{\mathrm{opt}}(t)=|b(t)|,
\]
where
\[
b(t)
=
e^{-\Gamma t/2}
\left[
\cos\!\left(\frac{\kappa t}{2}\right)
+
\frac{\Gamma}{\kappa}
\sin\!\left(\frac{\kappa t}{2}\right)
\right].
\]

The positive-information-flow maxima after the first loss of distinguishability occur exactly at
\[
t_n=\frac{2\pi n}{\kappa},
\qquad n=1,2,\ldots,
\]
and have the geometric heights
\[
\boxed{
|b(t_n)|=e^{-\pi\Gamma n/\kappa}.
}
\]

Consequently the infinite-time BLP non-Markovianity is
\[
\boxed{
\mathcal N_{\mathrm{BLP}}
=
\frac{1}{e^{\pi\Gamma/\kappa}-1}
}
\]
when
\[
\gamma_0>\frac{\Gamma}{2},
\]
and
\[
\boxed{\mathcal N_{\mathrm{BLP}}=0}
\]
when
\[
\gamma_0\le\frac{\Gamma}{2}.
\]

This gives two sharp asymptotic regimes.

First, define the distance above the Markovian boundary by
\[
\varepsilon=\frac{2\gamma_0}{\Gamma}-1.
\]
Then
\[
\mathcal N_{\mathrm{BLP}}
=
\frac{1}{e^{\pi/\sqrt{\varepsilon}}-1}
\sim
e^{-\pi/\sqrt{\varepsilon}}
\qquad
(\varepsilon\downarrow0).
\]
Thus information backflow turns on beyond all algebraic orders. If the measure is extended by zero to
\[
\varepsilon\le0,
\]
the resulting function is \(C^\infty\) at the transition and every derivative at
\[
\varepsilon=0
\]
vanishes, although the function is not analytic there.

Second, writing
\[
r=\frac{\gamma_0}{\Gamma},
\]
one has, as
\[
r\to\infty,
\]
\[
\boxed{
\mathcal N_{\mathrm{BLP}}
=
\frac{\sqrt{2r-1}}{\pi}
-\frac12
+
\frac{\pi}{12\sqrt{2r-1}}
+
O(r^{-3/2}).
}
\]

The individual information-backflow revivals therefore form an exact geometric spectrum, while the total memory measure has an ultra-flat threshold onset and square-root strong-coupling growth.

## Assumptions and scope

The result concerns the resonant Lorentzian amplitude-damping model at zero reservoir temperature and under the rotating-wave model used in the cited sources.

The BLP measure is the standard trace-distance information-backflow measure. The closed formula uses the resonant optimization theorem establishing
\[
D_{\mathrm{opt}}(t)=|b(t)|.
\]

The statement is for the infinite-time BLP measure. A finite observation window truncates the geometric revival sum.

The detuned Lorentzian model is not covered by the closed formula because its local minima generally do not vanish and its optimizing state pair is more complicated.

## Proof

In the strong-memory regime the resonant excited-state amplitude is
\[
b(t)
=
e^{-\Gamma t/2}
\left[
\cos\!\left(\frac{\kappa t}{2}\right)
+
\frac{\Gamma}{\kappa}
\sin\!\left(\frac{\kappa t}{2}\right)
\right],
\]
where
\[
\kappa=\sqrt{2\gamma_0\Gamma-\Gamma^2}.
\]

Differentiate directly:
\[
b'(t)
=
-\frac{\gamma_0\Gamma}{\kappa}
e^{-\Gamma t/2}
\sin\!\left(\frac{\kappa t}{2}\right).
\]
Hence the nonzero stationary times are exactly
\[
t_n=\frac{2\pi n}{\kappa},
\qquad n=1,2,\ldots.
\]
At these times,
\[
b(t_n)
=
(-1)^n e^{-\pi\Gamma n/\kappa},
\]
so
\[
|b(t_n)|=e^{-\pi\Gamma n/\kappa}.
\]

Between successive stationary times the amplitude has one zero. Explicitly, the zeros occur at
\[
\tau_n
=
\frac{2}{\kappa}
\left[
n\pi-\arctan\!\left(\frac{\kappa}{\Gamma}\right)
\right],
\qquad n=1,2,\ldots.
\]
Thus each positive-information-flow interval begins at a zero of the optimized trace distance and ends at the next local maximum. The contribution of the \(n\)-th revival to the BLP measure is therefore exactly
\[
e^{-\pi\Gamma n/\kappa}.
\]

Summing the geometric series gives
\[
\mathcal N_{\mathrm{BLP}}
=
\sum_{n=1}^{\infty}
e^{-\pi\Gamma n/\kappa}
=
\frac{1}{e^{\pi\Gamma/\kappa}-1}.
\]

For
\[
\gamma_0<\frac{\Gamma}{2},
\]
the source amplitude is the corresponding hyperbolic expression and decreases monotonically. At the boundary
\[
\gamma_0=\frac{\Gamma}{2},
\]
the limiting amplitude is
\[
b(t)=e^{-\Gamma t/2}\left(1+\frac{\Gamma t}{2}\right),
\]
whose magnitude is also monotone decreasing. Hence the BLP measure is zero throughout the closed Markovian side.

Now write
\[
\varepsilon=\frac{2\gamma_0}{\Gamma}-1.
\]
Then
\[
\kappa=\Gamma\sqrt{\varepsilon},
\]
and therefore
\[
\mathcal N_{\mathrm{BLP}}
=
\frac{e^{-\pi/\sqrt{\varepsilon}}}
{1-e^{-\pi/\sqrt{\varepsilon}}}
\sim
e^{-\pi/\sqrt{\varepsilon}}.
\]
The standard estimate that every derivative of
\[
e^{-c/\sqrt{\varepsilon}}
\]
is a polynomial in inverse powers of \(\varepsilon\) times the same exponential shows that all right derivatives tend to zero. Matching to the zero function on the Markovian side proves the \(C^\infty\) flatness statement.

Finally set
\[
s=\sqrt{2r-1},
\qquad
r=\frac{\gamma_0}{\Gamma}.
\]
The Bernoulli expansion
\[
\frac{1}{e^x-1}
=
\frac1x-\frac12+\frac{x}{12}+O(x^3)
\]
with
\[
x=\frac{\pi}{s}
\]
gives
\[
\mathcal N_{\mathrm{BLP}}
=
\frac{s}{\pi}
-\frac12
+
\frac{\pi}{12s}
+
O(s^{-3}),
\]
which is the stated strong-coupling expansion.

## Verification

`verify_blp_lorentzian.py` checks the analytic derivative identity, the exact stationary-point heights, the geometric summation, and the two asymptotic regimes.

For a deterministic set of coupling ratios above threshold, it compares the closed form with a long finite sum of revival maxima.

It also verifies numerically that the normalized threshold ratio
\[
\mathcal N_{\mathrm{BLP}}e^{\pi/\sqrt{\varepsilon}}
\]
approaches \(1\), and that the three-term strong-coupling expansion has the predicted error decay.

The numerical replay is supplementary. The all-parameter formula follows from the analytic proof.

## Relationship to prior work

Breuer, Laine, and Piilo introduced the trace-distance non-Markovianity measure and illustrated it on the damped Jaynes--Cummings model.

Xu, Yang, and Feng then treated the resonant Lorentzian reservoir analytically. They showed that the optimized trace distance is
\[
|b(t)|,
\]
identified the zero minima, and wrote the non-Markovianity as the sum of the local maxima of \(|b(t)|\). Their paper evaluates the measure numerically as the spectral width varies.

He, Zou, Li, and Shao later rederived the resonant optimizing state pair within a more general amplitude-damping optimization framework. Their resonant discussion again identifies each interval contribution with the corresponding local maximum but does not state the closed geometric sum or its threshold asymptotics.

The result here closes that remaining elementary but structurally useful step: the local maxima themselves form an exact geometric progression. This exposes the nonanalytic scale of the memory onset and the strong-coupling growth law, neither of which is stated in the inspected source papers.

Targeted searches for the exact closed form, its equivalent exponential parameterization, the threshold law
\[
e^{-\pi/\sqrt{\varepsilon}},
\]
and an “essential” or “beyond-all-orders” onset did not locate a covering result.

## Limitations

The formula is specific to exact resonance. For nonzero detuning the trace-distance minima need not vanish, and the BLP optimization is not reduced to the same geometric series.

The strong-coupling asymptotic is a mathematical statement about the exact Lorentzian model; physical validity of all microscopic approximations at arbitrarily large coupling is not asserted.

The \(C^\infty\) flatness concerns the BLP measure as a function of the dimensionless coupling distance
\[
\varepsilon=2\gamma_0/\Gamma-1.
\]
It does not imply that all dynamical observables are equally flat at the Markovian boundary.

A residual literature risk remains because later reviews and application papers often reuse this canonical model, and an equivalent closed sum may have appeared without being indexed by the targeted searches.

## References

1. H.-P. Breuer, E.-M. Laine, and J. Piilo, “Measure for the Degree of Non-Markovian Behavior of Quantum Processes in Open Systems,” arXiv:0908.0238, first public 3 August 2009; *Physical Review Letters* 103 (2009), 210401, DOI: 10.1103/PhysRevLett.103.210401.
2. Z. Y. Xu, W. L. Yang, and M. Feng, “Proposed method for direct measurement of non-Markovian character of the qubits coupled to bosonic reservoirs,” arXiv:0912.2879, first public 15 December 2009; *Physical Review A* 81 (2010), 044105, DOI: 10.1103/PhysRevA.81.044105.
3. Z. He, J. Zou, L. Li, and B. Shao, “An effective method of calculating the non-Markovianity \(\mathcal N\) for single channel open systems,” arXiv:1012.4328, first public 20 December 2010; *Physical Review A* 83 (2011), 012108, DOI: 10.1103/PhysRevA.83.012108.
