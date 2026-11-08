# Exact tail-optimal random probing of a two-level quantum transition

## Finding

**Theorem (universal sharp late-tail probing rate).** Let a closed two-level system have distinct Hamiltonian energies with angular-frequency gap \(\omega>0\). Fix two orthogonal normalized states \(\lvert0\rangle,\lvert1\rangle\), and assume the Hamiltonian couples them: \(\langle0\rvert H\lvert1\rangle\ne0\). Write
\[
p=\frac{4\lvert\langle0\rvert H\lvert1\rangle\rvert^2}{\hbar^2\omega^2}\in(0,1].
\]
Conduct independent rank-one projective measurements of \(\lvert1\rangle\) at the points of a rate-\(r>0\) Poisson process. Stop at the first affirmative result. Consider either the **transition** experiment (initial state \(\lvert0\rangle\)) or the **return** experiment (initial state \(\lvert1\rangle\)); each unsuccessful measurement projects the state to \(\lvert0\rangle\).

For either experiment, the first-detection survival probability has a strictly positive exponential leading term at long times,
\[
\Pr(T_r>t)\sim C_r e^{-\rho(r)t},\qquad C_r>0.
\]
There is exactly one \(r>0\) maximizing its exponential decay rate \(\rho(r)\), equivalently minimizing the slowest exponential tail time \(\rho(r)^{-1}\). **The same rate is optimal for both experiments** and is exactly
\[
\boxed{\frac{r_{\mathrm{tail}}}{\omega}=
\frac{4-p}{2\sqrt{2(2-p)}},\quad
\frac{\rho(r_{\mathrm{tail}})}{\omega}=
\frac{p}{2\sqrt{2(2-p)}}.}
\]
In the transition experiment the unique mean-detection-time optimum is \(r_{\mathrm{mean}}=\omega\), so the tail optimum lies strictly higher, with the sharp universal comparison
\[
\boxed{\left(\frac{r_{\mathrm{tail}}}{r_{\mathrm{mean}}}\right)^2-1=\frac{p^2}{8(2-p)},\qquad
1<\frac{r_{\mathrm{tail}}}{r_{\mathrm{mean}}}\le\frac{3}{2\sqrt2}.}
\]
Equality in the upper bound holds exactly at \(p=1\) (zero detuning); the lower bound is a nonattained infimum as \(p\downarrow0\). In the return experiment the mean detection time is \(2/r\) and has no finite optimum, **even though its late-time exponential tail has the same unique finite optimum**.

## Assumptions and scope

The Poisson measurement epochs are exogenous, independent and have exponential gaps of rate \(r\). The detector is the fixed projector \(\lvert1\rangle\langle1\rvert\); the state continues unitary evolution under time-independent Hermitian \(H\) between probes, with instantaneous ideal projective collapse on failure. There are no additional state resets, environmental dephasing, detection inefficiencies or time-varying controls. The ensemble averages include the random intervals and quantum measurement outcomes. The model is two-dimensional, and the transition amplitude is nonzero (\(p>0\)).

Because the energy gap is \(\hbar\omega\), unmeasured evolution through time \(t\) has transition probability
\[
q(t)=\lvert\langle1\rvert e^{-iHt/\hbar}\lvert0\rangle\rvert^2=p\sin^2(\omega t/2).
\]
The normalization \(p\le1\) follows from diagonalizing a two-by-two Hermitian matrix. For a matrix with off-diagonal coupling \(h\) and diagonal detuning \(\Delta\), \(\hbar\omega=\sqrt{4\lvert h\rvert^2+\Delta^2}\) and \(p=4\lvert h\rvert^2/(4\lvert h\rvert^2+\Delta^2)\). All times and rates in the theorem are dimensional (not dimensionless physical times).

## Proof

**1. Renewal transforms from the measurement rule.** Let \(s\ge0\), \(L=r+s\), and define
\[
A(s)=\int_0^\infty re^{-Lt}q(t)\,dt
=\frac{pr\omega^2}{2L(L^2+\omega^2)},\qquad
B(s)=\frac rL-A(s).
\]
For the transition experiment a successful first probe has transform \(A\), while after a failed probe the state is again \(\lvert0\rangle\) and the attempt restarts independently. Thus the first-detection Laplace transform is
\[
\widehat f_{\mathrm{tr}}(s)=A+B\widehat f_{\mathrm{tr}}
=\frac{pr\omega^2}{2s^3+4rs^2+2(r^2+\omega^2)s+pr\omega^2}.
\tag{1}
\]
For the return experiment the *first* probe succeeds with probability \(1-q(t)\); after a failed first probe the state is \(\lvert0\rangle\), and subsequent attempts follow the transition experiment. Hence
\[
\widehat f_{\mathrm{ret}}(s)=B(s)+A(s)\widehat f_{\mathrm{tr}}(s).
\tag{2}
\]
These are proper first-detection transforms since each equals one at \(s=0\). Differentiating at zero gives \(\mathbb ET_{\mathrm{tr}}=2(r^2+\omega^2)/(pr\omega^2)\) and \(\mathbb ET_{\mathrm{ret}}=2/r\).

**2. Unique dominant real pole and positive tail coefficient.** Introduce \(x=r/\omega>0\) and let \(y=\rho/\omega\). The zeros \(s=-\omega y\) of the cubic denominator in (1) satisfy
\[
G(y;x,p)=2y[(x-y)^2+1]-px=0.
\tag{3}
\]
The discriminant of this cubic, divided by four, equals
\[
-27p^2x^2+8px^4+72px^2-16x^4-32x^2-16.
\]
It is strictly increasing in \(p\in(0,1]\), because its \(p\)-derivative is \(x^2(8x^2+72-54p)>0\). At \(p=1\) it equals \(-8x^4+13x^2-16<0\), as the quadratic \(8u^2-13u+16\) has negative discriminant and positive leading coefficient. Consequently for every permitted parameter the cubic has exactly one real root and one nonreal conjugate pair. Because \(G(0)=-px<0\) and \(G(x/2)=x(1-p+x^2/4)>0\), that real root \(y\) lies in \((0,x/2)\).

The two nonreal roots have real part \(x-y/2>y\), since the sum of the three roots of (3) is \(2x\). Therefore the real pole \(s=-\omega y\) is strictly closest to the origin. Its residue in (1) is positive, because the derivative of the cubic \(G\) with respect to \(y\) at its sole real root is strictly positive (it equals twice the squared distance to either nonreal root). Thus its exponential appears with positive amplitude in the transition density and survival tail. Equation (2) has the same leading pole: its factor \(A(s)\) is strictly positive at \(s=-\omega y\), since \(r-\omega y>r/2\); any extra pole at \(s=-r\) decays faster. Integration of the positive leading density term establishes the asserted positive leading survival coefficient in both experiments. The detection time is *not* deterministically bounded above.

**3. Sharp optimization.** For each \(x>0\), let \(y(x)\) denote the unique real solution of (3). Its derivative satisfies
\[
\frac{dy}{dx}=-\frac{4y(x-y)-p}{2[(x-y)^2+1]-4y(x-y)}.
\]
The denominator is strictly positive at the real root by the preceding discriminant argument. Stationarity is therefore equivalent to \(p=4y(x-y)\). Combining this with (3) eliminates \(p\) and gives \(x^2-y^2=1\). Put \(u=x-y\in(0,1)\). Then \(x+y=1/u\) and \(p=2(1-u^2)\), so necessarily \(u=\sqrt{1-p/2}\), yielding the unique stationary pair
\[
x_* =\frac{4-p}{2\sqrt{2(2-p)}},\qquad
y_* =\frac{p}{2\sqrt{2(2-p)}}.
\]
Conversely this pair satisfies (3) and the derivative condition, and \(0<y_*<x_*/2\). As \(x\downarrow0\) one has \(y<x/2\to0\). As \(x\to\infty\), equation (3) and \(x-y>x/2\) give \(0<y\le2p/x\to0\). Thus the *only* stationary point is the strict global maximum of \(y(x)\). This proves uniqueness for both protocols.

**4. Comparison with mean optimization.** The transition mean from step 1 is uniquely minimized at \(r=\omega\), whereas the return mean \(2/r\) is strictly decreasing. Direct algebra shows \(x_*^2-1=p^2/[8(2-p)]\), which is positive for every permitted \(p\). It increases strictly with \(p\in(0,1]\), yielding the sharp lower and upper bounds and equality conditions in the theorem. At zero detuning \(p=1\) the exact optimal tail rate is \(r_{\mathrm{tail}}=3\omega/(2\sqrt2)\), with \(\rho_*=\omega/(2\sqrt2)\).

## Verification

`verify.py` uses only the Python standard library. Run `python3 verify.py` from the extracted package. It computes rational no-click density-matrix resolvents independently of the renewal argument for transition and return preparations, exactly compares both with the rational transforms (1) and (2), and checks the analytic optimizer and pole ordering at representative parameter points. It also checks the sign of the discriminant on a parameter mesh. A successful local run returned 448 assertions and the resonant rates \(r_{\mathrm{tail}}/\omega=1.06066017177982\) and \(\rho_*/\omega=0.353553390593274\). Finite mesh evaluations are **not** used to infer infinite-parameter uniqueness: that is proved above.

## Relationship to prior work

Kulkarni and Majumdar (arXiv:2305.15123, first publicly available 2023-05-24), especially Secs. 4 and 5, develop the general two-level random-probing renewal transform and the resonant Jaynes–Cummings survival law. They explicitly identify an optimal late-tail time scale that differs from the mean-optimal rate and study its existence graphically; these foundations are credited here. The present mathematical claim is the **exact, globally unique closed-form tail optimizer**, its *full nonzero-detuning dependence* for every two-level Hamiltonian, and the sharp universal comparison with the transition mean optimum, valid for both return and transition experiments. The full cubic transform (1) is implicit in their formulas, and no independent priority claim is made for it.

Kessler, Barkai and Ziegler (arXiv:2012.01763, Secs. 2–4 and Appendix B) provide a general random-measurement renewal formalism and mean/second-moment results, including the two-level model. Ziegler, Barkai and Kessler (arXiv:2012.15182, Secs. I–III and VI) establish quantization of the mean first-detected return time. Neither inspected discussion supplies the exact detuning-dependent late-tail optimizer claimed here. The previously published general methods can yield the result by further analysis, so priority of implicit coverage needs human verification.

## Limitations

The theorem concerns the asymptotic exponential **rate**, not a hard maximum detection time, a fixed finite quantile, or the complete first-detection distribution. A tail-optimal setting need not minimize a finite-time mean. The coupling parameter \(p=0\) is excluded: transition detection then has probability zero, and return detection changes character discontinuously. Arbitrary nonexponential measurement intervals, imperfect measurements, multilevel dark states, and added dephasing are outside the theorem. The mathematical result is self-contained but does not certify publication novelty or experimental utility. Related published formulas may imply it without listing the optimizing constants.

## References

1. M. Kulkarni and S. N. Majumdar, *First detection probability in quantum resetting via random projective measurements*, arXiv:2305.15123 (first version 2023-05-24), https://arxiv.org/abs/2305.15123.
2. D. A. Kessler, E. Barkai and K. Ziegler, *The first detection time of a quantum state under random probing*, arXiv:2012.01763 (2020), https://arxiv.org/abs/2012.01763.
3. K. Ziegler, E. Barkai and D. A. Kessler, *Randomly repeated measurements on quantum systems: Correlations and topological invariants of the quantum evolution*, arXiv:2012.15182 (2020), https://arxiv.org/abs/2012.15182.
