# Scientific review: sharp two-phase Markov–Bernstein constant for damped conjugate modes

## Correctness — PASS

The statement is a complete all-parameter theorem for real two-mode damped oscillations, plus equality of the real and complex-span constants. Translation invariance reduces the derivative norm to initial velocity; real-phase parametrization is exhaustive; the first damped critical point and time-zero endpoint exhaust the possible supremum contacts. The strictly decreasing function \(e^{ru}(\cos u-r\sin u)\) gives exactly one denominator-switching point. Its two branch objectives are respectively single-peaked and strictly decreasing, establishing uniqueness of the optimal phase. The transition equation is strictly increasing in damping ratio. Explicit normalized extremizers attain the constant in both regimes. Implicit differentiation proves the claimed curvature jump; the large-damping limit follows from a unique limiting transcendental root.

The standalone `check.py`, run from the same extracted package, passed 174,116 phase/trajectory probes, 58 parameter configurations, and five separate coefficient-phase optimizations, including critical and asymptotic tests. These finite checks are supplementary and are not offered as proof of the continuous maximization.

## Originality — PASS, with priority limits

The closest identified literature is V. Yu. Protasov (arXiv:2209.12250, first submission 2022-09-25), which formulates and studies general exponential-polynomial Markov–Bernstein constants, proves results for real exponent systems, and reduces complex cases to convex extremal problems. It does not evaluate the one-pair underdamped two-mode constant, determine the unique active-contact threshold, or state the \(C^1\)-but-not-\(C^2\) phase boundary. V. Yu. Protasov and R. Kamalov (arXiv:2403.16330, first submission 2024-03-24) develop constrained approximation methods and report a numerical complex-exponential example with *three* modes, rather than the analytic two-mode formula. The Borwein–Erdélyi exponential-sum comparison concerns different, real exponent configurations. Database comparisons found related damped-oscillator sampling and approximation records but not a statement implying the proposed constant or threshold. Theoretical methods for constrained approximation do not themselves tabulate this closed scalar classification.

The absence of a matching search hit is not a uniqueness proof. An older exact two-dimensional complex-exponent computation, possibly in the dynamical-systems or Chebyshev approximation literature, remains a priority risk. The 1996 exponential-sum source was assessed through available bibliographic/abstract excerpts, not a complete readable paper.

## Value — PASS

The object is the minimal underdamped real ODE solution space, where the derivative inequality is exactly the largest allowable initial velocity of a trajectory uniformly confined to a scalar amplitude bound. The theorem identifies a genuine geometric switch between a single interior active constraint and endpoint/interior equioscillation. This switch produces a precisely determined threshold and a second-order regularity defect in the sharp constant, not a mere numerical constant for an arbitrary parameter slice. The repeated-real-root strong-damping limit connects the oscillatory and Laguerre-type Markov problems. These quantitative features make the exact answer useful as a benchmark for constrained approximation and linear-ODE bounds.

## Scope and limitations

No general comparison theorem for arbitrary nonreal spectra is proved. Higher derivatives, multiple conjugate pairs, and different exponential decay rates remain outside this result. All parameter-wide statements rely on the analytic proof, not the numerical checker. Historical priority and independent mathematical review remain open.

Self-review: passed. Independent audit: not yet performed.
