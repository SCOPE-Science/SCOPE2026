# Long-step mass polarization in optimized recursive gradient schedules
## Finding

For normalized gradient descent on a \(1\)-smooth convex objective, let
\[
h^{(N)}=(h_0,\ldots,h_{N-2})
\]
be any optimized basic \(s\)-composable schedule with \(N\ge2\) leaves. The recent recursive-composition analysis gives the exact scalar value
\[
U_N=N^p\Phi(\{\log_2N\}),
\qquad
p=\log_2(1+\sqrt2),
\]
with \(\Phi\) positive, one-periodic, and nonconstant, and the \(s\)-composable interface gives
\[
\frac1{U_N}
=
\frac1{1+\sum_i h_i}
=
\prod_i(h_i-1).
\]

Define the total normalized stepsize mass
\[
H_N=\sum_i h_i=U_N-1,
\]
the mass carried by long steps
\[
M_N=\sum_{h_i>2} h_i,
\]
and the excess above the classical one-step descent ceiling
\[
\Omega_N=\sum_i (h_i-2)_+.
\]

Then every inserted step satisfies
\[
h_i>1,
\]
but every nonempty optimized schedule also contains at least one step satisfying
\[
h_i<2.
\]

At the same time,
\[
1-\frac{2(N-1)}{H_N}
\le
\frac{M_N}{H_N}
\le1
\]
and
\[
1-\frac{2(N-1)}{H_N}
\le
\frac{\Omega_N}{H_N}
\le1.
\]
Because
\[
H_N=N^p\Phi(\{\log_2N\})-1
\]
and the phase has a strictly positive minimum, both ratios converge to one uniformly as \(N\to\infty\). Their deficits are
\[
O(N^{1-p}).
\]

Finally,
\[
\max_i h_i
\ge
\frac{H_N}{N-1}
=
\frac{N^p\Phi(\{\log_2N\})-1}{N-1}.
\]
Thus the largest normalized step is forced to diverge at least on the scale
\[
N^{p-1},
\]
with the same dyadic phase in the lower bound. Along dyadic horizons, where \(\Phi(0)=1\),
\[
\max_i h_i
\ge
N^{p-1}(1+o(1)).
\]

The optimized recursive schedules therefore have a necessary mass-polarization structure: a sub-\(2\) short-step anchor survives at every finite horizon, while asymptotically almost all cumulative stepsize mass is carried by steps above \(2\), and almost all cumulative mass remains even after subtracting \(2\) from every long step.

## Assumptions and scope

The claim concerns the optimized basic \(s\)-composable family generated recursively from the empty schedule by the \(s\)-join. The horizon convention is that \(N\) leaves correspond to \(N-1\) gradient steps.

The normalized step \(h_i\) corresponds to the physical step \(h_i/L\) on an \(L\)-smooth objective. Therefore the threshold \(h_i=2\) is exactly the usual one-step descent boundary \(2/L\).

The result uses the exact phase law for the optimized OBS-S scalar \(U_N\). It does not claim that every accelerated predetermined schedule has the same mass profile, nor does it classify how many long steps occur.

## Proof

The \(s\)-join of two positive-rate schedules inserts
\[
\mu(\alpha,\beta)
=
1+
\frac{
\sqrt{\alpha^2+6\alpha\beta+\beta^2}-(\alpha+\beta)
}{
2\alpha\beta
},
\qquad
\alpha,\beta>0.
\]
Since
\[
\alpha^2+6\alpha\beta+\beta^2
-
(\alpha+\beta)^2
=
4\alpha\beta>0,
\]
the square root is strictly larger than \(\alpha+\beta\). Hence every recursively inserted step satisfies
\[
\mu(\alpha,\beta)>1.
\]
Starting from the empty schedule proves
\[
h_i>1
\]
for every step in every basic \(s\)-composable schedule.

For an \(s\)-composable schedule with rate \(\eta\), the certificate interface contains the exact sum-product identity
\[
\eta
=
\frac1{1+\sum_i h_i}
=
\prod_i(h_i-1).
\]
For an optimized OBS-S schedule,
\[
\eta=\frac1{U_N},
\]
and for \(N\ge2\) one has \(U_N>1\). Therefore
\[
\prod_i(h_i-1)<1.
\]
All factors are positive. If every step satisfied \(h_i\ge2\), then every factor would satisfy \(h_i-1\ge1\), forcing the product to be at least one, a contradiction. Hence at least one step has
\[
1<h_i<2.
\]

Now
\[
H_N=\sum_i h_i=U_N-1.
\]
The mass not carried by long steps is bounded by
\[
H_N-M_N
=
\sum_{h_i\le2}h_i
\le
2(N-1).
\]
Thus
\[
M_N\ge H_N-2(N-1),
\]
which gives the stated lower bound after division by \(H_N\).

Likewise, for every step,
\[
h_i\le2+(h_i-2)_+.
\]
Summing gives
\[
H_N\le2(N-1)+\Omega_N,
\]
hence
\[
\Omega_N\ge H_N-2(N-1).
\]
The upper bounds
\[
M_N\le H_N,
\qquad
\Omega_N\le H_N
\]
are immediate from positivity.

The recent phase theorem gives
\[
U_N=N^p\Phi(\{\log_2N\}),
\]
where
\[
0<\phi_*:=\min_t\Phi(t).
\]
Consequently
\[
H_N\ge \phi_*N^p-1.
\]
Since \(p>1\),
\[
\frac{2(N-1)}{H_N}
\le
\frac{2(N-1)}{\phi_*N^p-1}
=
O(N^{1-p}),
\]
uniformly over the dyadic phase. This proves both mass-ratio limits.

Finally, one of the \(N-1\) positive steps is at least their average:
\[
\max_i h_i
\ge
\frac{H_N}{N-1}.
\]
Substitution of the exact phase law yields the claimed lower bound and the \(N^{p-1}\) growth scale.

## Verification

The standalone script `artifacts/verify_mass_polarization.py` recursively constructs balanced OBS-S schedules from the source join formula for a range of horizons. It verifies the sum-product identity numerically, checks that every generated step exceeds \(1\), checks that every nonempty schedule contains a step below \(2\), and evaluates the long-step and overshoot mass bounds.

The computation is a finite replay only. The all-horizon claim follows from the join formula, exact sum-product identity, and source phase theorem.

## Relationship to prior work

Liu, Chen, Jiang, and Wang prove balanced optimality for the symmetric recursive constructions and derive the exact log-periodic law
\[
U_N=N^p\Phi(\{\log_2N\}).
\]
Their paper emphasizes that carefully organized long steps enable acceleration and gives the exact total stepsize through the scalar identity \(U_N=1+\sum_i h_i\). It does not state the mass-polarization consequence above: a persistent sub-\(2\) step together with asymptotically unit long-step and overshoot mass fractions and a phase-sensitive lower bound on the largest step.

Grimmer, Shu, and Wang introduced \(s\)-composability, its sum-product interface, and the recursive \(s\)-join. Their composition theory generates optimized schedules of every length and proves accelerated rates, but the inspected full text does not formulate the long-step mass fraction or the forced simultaneous presence of a sub-\(2\) step and a diverging largest step.

Earlier long-step gradient-descent work proves acceleration by deliberately using steps beyond the classical interval \((0,2)\), including increasingly large nonperiodic steps. It establishes that long steps can accelerate convergence, but it does not imply the exact OBS-S mass balance because it predates the all-horizon phase law.

Targeted searches using \(s\)-composability, cumulative long-step mass, overshoot above \(2\), maximum-step growth, and short-step-anchor aliases found no statement equivalent to this polarization law.

## Limitations

The finding is structural rather than a new convergence-rate exponent: the rate and phase law are inputs from the recent source.

The bound on the largest step is a necessary lower bound, not an exact asymptotic for the maximum. The result also does not determine the number or locations of long steps.

Only the optimized basic \(s\)-composable family is claimed. Other predetermined schedules may realize acceleration through different mass distributions.

## References

1. Y. Liu, K. Chen, R. Jiang, T. Wang, *Optimal Recursive Composition and Dyadic Phase Laws for Gradient Descent with Predetermined Stepsizes*, arXiv:2609.11788v1, 2026.
2. B. Grimmer, K. Shu, A. L. Wang, *Composing Optimized Stepsize Schedules for Gradient Descent*, Mathematics of Operations Research, 2025, DOI: 10.1287/moor.2024.0764; arXiv:2410.16249.
3. B. Grimmer, K. Shu, A. L. Wang, *Provably Faster Gradient Descent via Long Steps*, SIAM Journal on Optimization 34(3), 2024, DOI: 10.1137/23M1588408; arXiv:2309.09961.
