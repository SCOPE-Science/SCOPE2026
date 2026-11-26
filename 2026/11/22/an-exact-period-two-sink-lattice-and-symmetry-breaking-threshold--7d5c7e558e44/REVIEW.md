# Independent mathematical audit

## correctness

PASS

A primitive pair cannot have equal first coordinates since the second component then forces equal second coordinates. Sort first coordinates and set d=x_1−x_0>0, s=x_0+x_1, c=(a−1)/2 and L=(a+1)/2. The second-coordinate equations fix y_0=ax_1 and y_1=ax_0, so 0<d≤1 and the two first-coordinate equations are exactly equivalent to sin(Ls)cos(cd)=0 and d=cos(Ls)sin(cd). For 0<a≤3, |c|≤1 and |sin(cd)|<d (also when c=0), so no primitive cycle. For 3<a<1+2π, 0<cd<π: the central branch requires Ls∈2πZ and c=θ/sin θ with θ=cd, strictly increasing from 1 to infinity; the only other case is cd=π/2, with cos(Ls)=π/(a−1). This gives two distinct side phases per cell above 1+π, coalescing with the central cycle at equality. Translation by (2π/(a+1))(1,a) advances the cell. On the central branch, both step derivatives are J(t) with t=cos θ; the return is J(t)². The monic polynomial λ²−(1+t)λ−at has strict Schur conditions exactly −1/a<t<0 in the claimed range. The product −a cos θ is strictly increasing for θ>π/2; it reaches 1 before θ=2π/3, where c=4π/(3√3)<π. Bisection independently checks a_*≈4.65946370392898. Neither endpoint is an exponential sink. On a noncoalescent side cycle the step cosines are v and −v, and the return has trace 1−v² and determinant −a²v². Its characteristic value at 1 is negative, forcing a real multiplier greater than 1. Finally 1−π/(a−1)=(a−1−π)/π+O((a−1−π)²), which gives the arccos phase splitting and remainder.

## originality

PASS

The system and its translation symmetry are known. The supported distinct result is the exhaustive primitive-two-cycle description in the stated positive-gain interval, including side onset, phase splitting and exact sink boundaries. The principal same-map paper gives the actual equations, fixed-point analysis and numerical attractor observations but no such census or Floquet interval. The relevant indexed two-cycle classifications use different maps with no identified reduction. The older Li et al. reference remains an explicit access risk, not evidence of coverage or grounds by itself for failure.

## value

PASS

The full real-plane classification per translation cell answers a natural first nonsingleton-orbit question for a previously studied nonlinear map. It separates existence, symmetry splitting and local exponential stability at distinct exact thresholds, reveals that two new side branches cannot be sinks, and supplies an analytic positive-gain benchmark outside the earlier numerical sweep. This is useful beyond a numerical location of a single cycle, without implying global basin or higher-period results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
