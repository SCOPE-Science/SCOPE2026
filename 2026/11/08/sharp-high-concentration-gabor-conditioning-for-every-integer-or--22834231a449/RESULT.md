# Sharp high-concentration Gabor conditioning for integer-order Matérn windows

## Finding

For each fixed integer \(m\ge2\), the optimal bounds of the redundancy-two Gabor frame with the origin-normalized Matérn window defined below satisfy
\[
A_m(\lambda)\sim 4\left(\frac{(m-1)!}{(2m-2)!}\right)^2\lambda^{2m-2}e^{-\lambda},\qquad B_m(\lambda)\longrightarrow 2\qquad(\lambda\to\infty).
\]
Consequently
\[
\frac{B_m(\lambda)}{A_m(\lambda)}\sim
\frac{((2m-2)!)^2}{2((m-1)!)^2}\frac{e^\lambda}{\lambda^{2m-2}}.
\]
The minimizing time coordinate approaches \(1/2\) modulo integers. Precisely, if \(\lambda_j\to\infty\) and the Zak fibers \((x_j,\omega_j)\) satisfy \(S_{m,\lambda_j}(x_j,\omega_j)/A_m(\lambda_j)\to1\), then \(\operatorname{dist}(x_j,1/2+\mathbb Z)\to0\). This includes exact minimizers. Localization is not asserted for a vanishing **absolute** gap: the symbol can tend to zero at a fixed time coordinate away from the midpoint.

## Assumptions and scope

Let \(n=m-1\), \(\lambda>0\), and
\[
P_n(s)=\frac{n!}{(2n)!}\sum_{j=0}^{n}\frac{(2n-j)!}{(n-j)!j!}(2s)^j,
\qquad g_{m,\lambda}(t)=e^{-\lambda|t|}P_n(\lambda|t|).
\]
Then \(g_{m,\lambda}(0)=1\). The Fourier transform (with cycles per unit time) is proportional to \((\lambda^2+4\pi^2\xi^2)^{-m}\); the window is an \(m\)-fold convolution power of a symmetric Laplace density rescaled to have value one at zero, not to have integral one. Translations are \(T_kf(t)=f(t-k)\) and modulations are \(M_{j/2}f(t)=e^{\pi ijt}f(t)\). The numbers \(A_m(\lambda)\) and \(B_m(\lambda)\) are the largest lower and smallest upper constants in
\[
A_m(\lambda)\|f\|_2^2\le\sum_{j,k\in\mathbb Z}|\langle f,M_{j/2}T_k g_{m,\lambda}\rangle|^2\le B_m(\lambda)\|f\|_2^2,\qquad f\in L^2(\mathbb R).
\]

## Proof

**Zak symbol.** Write \(g=g_{m,\lambda}\) and use \(Zg(x,\omega)=\sum_{k\in\mathbb Z}g(x-k)e^{2\pi i k\omega}\), uniformly convergent on a fundamental square. The Zak transform is unitary from \(L^2(\mathbb R)\) to \(L^2([0,1]^2)\). Under this transform, translations act by \(e^{-2\pi i k\omega}\) and integer modulations act by \(e^{2\pi i q x}\); modulation by \(1/2\) additionally shifts \(\omega\) by \(-1/2\) and multiplies by \(e^{\pi i x}\). Applying Fourier Parseval separately to the even and odd modulations thus makes the frame quadratic form multiplication by
\[
S_{m,\lambda}(x,\omega)=|Zg(x,\omega)|^2+|Zg(x,\omega+1/2)|^2=2(|E|^2+|O|^2),
\]
where \(E,O\) are the even- and odd-translate sums in \(Zg(x,\omega)\), respectively. Its minimum and maximum are the optimal bounds by continuity. The reciprocal Fourier transform factors into \(m\) factors of each sign \((1\pm 2\pi i\xi/\lambda)\) up to a positive constant, so the finite-type totally positive window frame theorem also guarantees the lower bound is positive at every \(\lambda>0\) on this density-two lattice. Positivity at large \(\lambda\) follows directly below. By periodicity and evenness the time coordinate may be restricted to \([0,1/2]\).

**Window and translate estimates.** If \(a_j\) is the coefficient of \(s^j\) in \(P_n\), then \((j+1)a_{j+1}/a_j=2(n-j)/(2n-j)\le1\). Thus \(0<g(t)\le1\) and \(g\) is nonincreasing for \(t\ge0\). For \(t\) in any positive compact interval bounded away from zero,
\[
g(t)=\frac{2^nn!}{(2n)!}(\lambda t)^ne^{-\lambda t}(1+O(\lambda^{-1})).
\]
In particular \(h_\lambda:=g(1/2)\sim (n!/(2n)!)\lambda^n e^{-\lambda/2}\). All bounds here are for fixed \(m\). For any fixed positive minimal distance \(b\), the translate tails beginning at distance at least \(b\) are bounded in modulus by \(O(\lambda^n e^{-b\lambda})\) uniformly in the Zak frequency: bound the polynomial by \(C(1+\lambda t)^n\) and sum the exponential at linearly increasing distances.

On \([0,1/4]\), the nearest even translate is \(k=0\), and the remainder has distance at least \(7/4\); thus \(E=g(x)+O(\lambda^ne^{-7\lambda/4})\). In particular \(|E|\ge g(1/4)-O(\lambda^ne^{-7\lambda/4})\), so the infimum of \(S/h_\lambda^2\) there tends to infinity. On \([1/4,1/2]\) the nearest even and odd translates are at \(k=0,1\) respectively. The remainders satisfy
\[
E=g(x)+O(\lambda^ne^{-3\lambda/2}),\qquad
O=e^{2\pi i\omega}g(1-x)+O(\lambda^ne^{-5\lambda/4}).
\]
Both principal terms are at most \(g(1/4)\) in modulus, so squaring gives uniformly
\[
S_{m,\lambda}(x,\omega)=2(g(x)^2+g(1-x)^2)+o(h_\lambda^2).
\]

**Minimum and localization.** For \(t\in[1/4,3/4]\), \(g(t)^2=q_n(\lambda t)\) where \(q_n(s)=e^{-2s}P_n(s)^2\). The expression \(e^{2s}q_n''(s)\) is a polynomial with leading term \(4P_n(s)^2\) (the terms involving derivatives have lower degree), hence is positive for large \(s\). Thus \(g^2\) is convex on this interval for large \(\lambda\); Jensen gives \(g(x)^2+g(1-x)^2\ge2h_\lambda^2\). The uniform remainder bound and the larger symbol scale on \([0,1/4]\) give the lower estimate \(A_m(\lambda)\ge4h_\lambda^2-o(h_\lambda^2)\); evaluation at \(x=1/2\) gives the matching upper estimate. For any fixed \(0<\varepsilon<1/4\), on \([1/4,1/2-\varepsilon]\) the ratio \(g(x)/h_\lambda\) diverges uniformly by monotonicity and the fixed-positive-distance asymptotic. Together with the earlier estimate on \([0,1/4]\) this makes \(S/A_m(\lambda)\) diverge uniformly away from the midpoint, proving the stated relative localization. By contrast, \(x=1/4\) at any fixed \(\omega\) has \(S_{m,\lambda}(x,\omega)\to0\), and hence an absolute gap tending to zero without localization.

**Maximum.** On \([0,1/4]\) the odd translates all have distance at least \(3/4\), so \(E=g(x)+o(1)\), \(O=o(1)\) uniformly. Since \(g(x)\le1\), this gives \(S\le2+o(1)\) there. On \([1/4,1/2]\) both translate sums are \(o(1)\). At \((0,0)\) the symbol is \(2+o(1)\) since \(g(0)=1\). Thus \(B_m(\lambda)\to2\). Combining with \(A_m(\lambda)\sim4h_\lambda^2\) proves the ratio asymptotic.

## Verification

The supplied `CHECK.py` (`python CHECK.py`) checks polynomial coefficient ratios with integer-rational arithmetic and samples the two Zak sums with finite truncations for orders \(2\) through \(6\). The reported check is finite consistency evidence, not a proof of optimality, localization, or the limit for every fixed order. Those follow from the uniform estimates above.

## Relationship to prior work and limitations

Kloos and Stöckler, [Zak transforms and Gabor frames of totally positive functions and exponential B-splines](https://arxiv.org/abs/1311.7359), treat finite-type totally positive windows and quantitative near-critical-density bounds for the first-order exponential. De Dios Pont, Gröchenig, Liehr, Shafkulovska, and Taylor, [Gabor Frames of Totally Positive Functions: A Complete Characterization](https://arxiv.org/abs/2608.04992), give the general qualitative frame-set theorem. Faulhuber and Shafkulovska, [Gabor frame bound optimizations](https://arxiv.org/abs/2204.02917), optimize lattice parameters for other windows including the two-sided exponential. Ghosh and Antony Selvan, [On Gabor frames generated by B-splines, totally positive functions, and Hermite functions](https://arxiv.org/abs/2304.11322), study sufficient frame regions and existence. The exact [asymmetric two-sided exponential bound](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-sharp-redundancy-two-gabor-bounds-for-asymmetric-two-sided--400c3e36998f) gives the equal-rate first-order limit on this same lattice. The contribution here is the sharp concentration law in the higher convolution orders at the fixed lattice, not frame existence, order one, or the Zak representation.

There is no claim for varying \(m\), other lattices or window normalizations, nor for exact finite-\(\lambda\) extremal fibers. The estimates do not classify the minimizing frequency coordinate.
