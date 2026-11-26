# Independent mathematical audit

## correctness

PASS

With u=cx and p=uy, multiplication of the two updates gives p'−1=(p−1)(1+p/(1+y²)). Hence the sign classes and the invariant equality are exact. Below the curve, if y were unbounded, the decrease in p for y≥1 would be at least (1−p₀)/2 times the increment in log y, contradicting bounded p. For finite limit Y, uₙ is bounded by u₀qⁿ, with q=Y²/(1+Y²); summability of log(q(yₙ)/q) gives the positive limiting prefactor and summing uₙ gives the stated tail for Y−yₙ. On the curve sₙ=yₙ² obeys Δsₙ=2+1/sₙ. First sₙ=2n+O(log n), then Δ(sₙ−2n−log(n)/2)=O(log(n)/n²), giving the constant and error. Above the curve, Δ(y²)≥2p₀, so y grows without bound. If u had zero limit, its telescoping decrement sum is a left Riemann sum for ∫ from yₙ to ∞ of (1+t²)⁻¹, with error at most uₙ/(1+yₙ²); this forces pₙ→1, impossible. For v=lim uₙ>0, yₙ/n→v and summing the same decrements first gives uₙ−v=O(1/n), then yₙ=vn+O(log n). The summand is consequently 1/(vk²)+O(log(k)/k³); summing it and then subtracting the harmonic drift from y proves both displayed errors. Strict y-increase excludes periodic orbits. Replay: frozen RESULT.md §§1–5, lines 39–101. VERIFICATION.md and verify.py were inspected, not executed; the floating-point checks cannot certify the separatrix or infinite-time limits.

## originality

PASS

The supported distinct result is the exact endpoint invariant and global hyperbolic partition, including the quantitative laws on its three identified regions. The nearby parabolic study recovers the limiting critical log coefficient by the same type of Riemann-sum estimate and is substantial mathematical overlap, but does not identify the exact endpoint critical initial conditions. No priority is inferred from same-day dating. The originating article remains an explicit outstanding primary-source risk.

## value

PASS

For an existing dynamical family at an equilibrium-line parameter, local stability does not answer which positive initial states converge to that line and which escape. The explicit all-state separator answers that question without shooting or asymptotic parameter fitting and identifies a distinct critical motion, with quantitative convergence and scattering on its two sides. Even relative to the nearby parabolic model the endpoint's exact basin test is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
