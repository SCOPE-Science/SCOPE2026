# Exact frequency crossover for AdEMAMix's fast-slow momentum mixer
## Finding

AdEMAMix combines a conventional fast exponential moving average of gradients with a much slower one. The defining paper motivates this mixture by the tension between reacting to recent gradients and retaining useful information from gradients thousands of steps old. With fixed hyperparameters, that fast-slow split has an exact frequency boundary.

Consider one coordinate after the source warmup schedules for the slow decay and slow multiplier have settled. Let
\[
0\le\beta_1<\beta_3<1,
\qquad
\alpha>0.
\]
Ignoring weight decay, the two first-moment states are
\[
m_t^{(1)}
=
\beta_1m_{t-1}^{(1)}
+
(1-\beta_1)g_t,
\]
\[
m_t^{(2)}
=
\beta_3m_{t-1}^{(2)}
+
(1-\beta_3)g_t.
\]
The fast state is bias corrected in the source algorithm, while the slow state is not. Bias correction tends to one asymptotically, so for a steady harmonic input the two channels have transfer functions
\[
H_{\beta}(\omega)
=
\frac{1-\beta}
{1-\beta e^{-i\omega}}.
\]

Define the slow-to-fast steady contribution ratio
\[
R(\omega)
=
\alpha
\frac{|H_{\beta_3}(\omega)|}
{|H_{\beta_1}(\omega)|}.
\]
Since
\[
|H_{\beta}(\omega)|
=
\frac{1-\beta}
{\sqrt{1+\beta^2-2\beta\cos\omega}},
\]
we have
\[
R(\omega)^2
=
C
\frac{
1+\beta_1^2-2\beta_1\cos\omega
}{
1+\beta_3^2-2\beta_3\cos\omega
},
\]
where
\[
C
=
\left[
\frac{\alpha(1-\beta_3)}
{1-\beta_1}
\right]^2.
\]

For
\[
0\le\beta_1<\beta_3<1,
\]
the ratio
\[
R(\omega)
\]
is strictly decreasing on
\[
0<\omega<\pi.
\]
Its endpoint values are
\[
R(0)=\alpha
\]
and
\[
R(\pi)
=
\alpha
\frac{
(1-\beta_3)(1+\beta_1)
}{
(1+\beta_3)(1-\beta_1)
}.
\]

Therefore, whenever
\[
\alpha>1
\]
and
\[
R(\pi)<1,
\]
there is exactly one frequency
\[
\omega_c\in(0,\pi)
\]
at which the slow and fast EMA contributions have equal magnitude. It is given by
\[
\boxed{
\cos\omega_c
=
\frac{
1+\beta_3^2
-
C(1+\beta_1^2)
}{
2(\beta_3-C\beta_1)
}
}.
\]
The slow EMA dominates the fast EMA exactly for
\[
0\le\omega<\omega_c,
\]
while the fast EMA dominates for
\[
\omega_c<\omega\le\pi.
\]

For the values emphasized in the source paper,
\[
\beta_1=0.9,
\qquad
\beta_3=0.9999,
\]
the crossover periods
\[
T_c=\frac{2\pi}{\omega_c}
\]
are

\[
\begin{array}{c|c}
\alpha & T_c\\
\hline
4 & 16222.1866\ldots\\
5 & 12824.7126\ldots\\
8 & 7915.4454\ldots\\
10 & 6314.2386\ldots
\end{array}
\]

steps.

Thus, throughout the source's commonly used slow-momentum range, the slow EMA outweighs the fast EMA only on variations whose periods are on the scale of several thousand to more than sixteen thousand steps.

Two endpoint signals make the resulting normalized-update selectivity exact. Use a constant-magnitude gradient so that
\[
g_t^2=G^2
\]
for every \(t\). The Adam-style second moment then satisfies
\[
\widehat\nu_t=G^2
\]
exactly after bias correction, so the denominator is identical for AdEMAMix and the corresponding AdamW fast channel.

For a constant gradient,
\[
g_t=G,
\]
the fast bias-corrected first moment equals \(G\), while the slow first moment tends to \(G\). Hence the asymptotic AdEMAMix-to-AdamW normalized-update gain is
\[
1+\alpha.
\]

For the alternating gradient
\[
g_t=(-1)^{t-1}G,
\]
the fast and slow first moments have asymptotic amplitudes
\[
\frac{1-\beta_1}{1+\beta_1}|G|
\]
and
\[
\frac{1-\beta_3}{1+\beta_3}|G|,
\]
with the same alternating phase. Therefore the exact asymptotic gain relative to the fast AdamW channel is
\[
1+R(\pi).
\]

At
\[
\beta_1=0.9,
\qquad
\beta_3=0.9999,
\]
the source range
\[
\alpha=4\ \text{through}\ 10
\]
produces DC gains from
\[
5
\]
through
\[
11,
\]
but Nyquist gains only from
\[
1.0038001900\ldots
\]
through
\[
1.0095004750\ldots.
\]

The mixture is therefore sharply frequency selective: the slow channel can strongly amplify persistent low-frequency gradient structure while adding less than one percent to the alternating-gradient response at these source settings.

## Assumptions and scope

The theorem concerns source-form AdEMAMix after the schedules for \(\beta_3\) and \(\alpha\) have settled at fixed values.

Weight decay is set to zero in order to isolate the gradient-momentum mixer.

The harmonic calculation concerns the first-moment mixer. At intermediate frequencies the adaptive second moment need not be constant, so no full normalized-update transfer function is claimed there.

The normalized-update ratios are stated only for the constant and alternating constant-magnitude inputs, where the bias-corrected second moment is exactly \(G^2\).

The analysis is one-coordinate and deterministic. It is an optimizer input-response statement, not a claim about nonlinear training dynamics, stochastic convergence, or generalization.

## Proof

For the stable scalar EMA
\[
m_t
=
\beta m_{t-1}
+
(1-\beta)g_t,
\]
substitution of the complex harmonic ansatz
\[
g_t=Ge^{i\omega t},
\qquad
m_t=H_{\beta}(\omega)Ge^{i\omega t}
\]
gives
\[
H_{\beta}(\omega)
=
\frac{1-\beta}
{1-\beta e^{-i\omega}}.
\]
Taking magnitudes gives the displayed formula for \(R(\omega)\).

Set
\[
c=\cos\omega.
\]
Apart from the positive constant \(C\),
\[
R(\omega)^2
\]
is the ratio
\[
Q(c)
=
\frac{
1+\beta_1^2-2\beta_1c
}{
1+\beta_3^2-2\beta_3c
}.
\]
Differentiating with respect to \(c\) yields
\[
Q'(c)
=
\frac{
2(\beta_3-\beta_1)(1-\beta_1\beta_3)
}{
(1+\beta_3^2-2\beta_3c)^2
}
>0.
\]
Since \(c=\cos\omega\) is strictly decreasing on \((0,\pi)\), \(R(\omega)\) is strictly decreasing there.

The endpoint values follow from
\[
|H_\beta(0)|=1
\]
and
\[
|H_\beta(\pi)|
=
\frac{1-\beta}{1+\beta}.
\]
Under
\[
R(0)>1>R(\pi),
\]
strict monotonicity gives a unique crossover. Solving
\[
R(\omega_c)^2=1
\]
for \(\cos\omega_c\) gives the displayed closed form.

For a constant-magnitude endpoint signal, the source second-moment recurrence is
\[
\nu_t
=
\beta_2\nu_{t-1}
+
(1-\beta_2)G^2.
\]
Starting from zero,
\[
\nu_t=(1-\beta_2^t)G^2,
\]
so bias correction gives
\[
\widehat\nu_t=G^2
\]
exactly.

At zero frequency, the fast bias-corrected first moment is \(G\), while the slow uncorrected EMA converges to \(G\). Their source mixture therefore tends to
\[
(1+\alpha)G.
\]

At the Nyquist frequency, the stable EMA response is real and in phase with the alternating input:
\[
H_\beta(\pi)
=
\frac{1-\beta}{1+\beta}.
\]
Thus the AdEMAMix numerator amplitude is the fast amplitude multiplied by
\[
1+
\alpha
\frac{
(1-\beta_3)(1+\beta_1)
}{
(1+\beta_3)(1-\beta_1)
}
=
1+R(\pi).
\]
The common adaptive denominator cancels in the ratio to AdamW, proving the endpoint gain formulas.

## Verification

The accompanying `verify.py` checks the analytic transfer-function ratio, strict frequency monotonicity, crossover equation, and the source-parameter crossover periods.

It also directly replays the two source first-moment recurrences and the bias-corrected second moment on constant and alternating gradients, verifying the predicted endpoint gain ratios.

The numerical checks are transcription guards. Monotonicity, uniqueness of the crossover, and both endpoint ratios are proved algebraically above.

## Relationship to prior work

Pagliardini, Ablin, and Grangier introduced AdEMAMix to resolve a specific limitation of a single gradient EMA: a single decay cannot simultaneously give large weight to the immediate past and non-negligible weight to much older gradients. Their method combines a fast EMA with a slower EMA, often using
\[
\beta_3=0.9999,
\]
and reports useful values of
\[
\alpha
\]
in the approximate range from \(4\) to \(10\). The paper emphasizes that gradients can remain useful over tens of thousands of optimization steps.

The defining paper gives the two EMA recurrences, the slow-momentum multiplier, the Adam-style second moment, and warmup schedules. It does not state a harmonic transfer-function comparison, a unique fast-slow crossover frequency, or the exact DC-versus-Nyquist gain contrast derived here.

Morwani, Vyas, Zhang, and Kakade later connected AdEMAMix and related recent optimizers to accelerated stochastic-gradient methods. Their analysis concerns optimization-equivalence structure rather than a frequency-response crossover; targeted searches of that work for frequency, alternating, and transfer formulations did not reveal an implication-equivalent result.

Related analyses of multiple-momentum and filtered-gradient optimizers have different state equations or normalization rules. In particular, a twofold-EMA denominator method can cancel momentum attenuation on an alternating signal, while AdEMAMix retains the raw-gradient Adam second moment and instead sums two first-moment channels. Those statements do not imply the fast-slow crossover here.

## Limitations

The source uses warmup schedules for \(\beta_3\) and \(\alpha\); the theorem starts after those schedules have settled.

The crossover concerns the two numerator channels, not the complete adaptive update at arbitrary frequency.

Only the zero-frequency and Nyquist normalized-update ratios exploit an exactly constant squared-gradient denominator.

The multi-thousand-step crossover periods are signal periods, not memory half-lives, and should not be interpreted as identical quantities.

## References

1. Matteo Pagliardini, Pierre Ablin, and David Grangier, “The AdEMAMix Optimizer: Better, Faster, Older,” arXiv:2409.03137v1, 2024.
2. Depen Morwani, Nikhil Vyas, Hanlin Zhang, and Sham Kakade, “Connections between Schedule-Free Optimizers, AdEMAMix, and Accelerated SGD Variants,” arXiv:2502.02431v1, 2025.
