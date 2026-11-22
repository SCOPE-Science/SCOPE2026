# A parabolic escape separator and a sign-changing logarithmic drift in a rational plane map

## Finding
Consider the rational map introduced by Zhang, Liu, Wei, Jiang and Bi,
\[
F_{a,b,c,d}(x,y)=\left(x+\frac{ax}{1+y^2}+b,\ y+cx+d\right).
\]
On the natural fixed-line slice \(b=d=0\), let \(a=-\lambda\) with \(0<\lambda<1\), and let \(c\ne0\). Write \(u=cx\). For every initial height \(y_0\ge0\), the positive-speed initial half-line \(u_0>0\) has three mutually exclusive regimes:

1. The orbit converges to a finite point on the fixed line \(u=0\).
2. It escapes ballistically: \(y_n/n\to u_\infty>0\).
3. It escapes *critically*: \(y_n\to+\infty\) while \(u_n\downarrow0\).

The first and second regimes are both nonempty open intervals of initial speeds; the third is a nonempty closed interval between them (not asserted to be a singleton). **Every** critical orbit has the same universal two-term law
\[
\boxed{\quad y_n^2=2\lambda n+\frac{5\lambda-2}{6}\log n+C+o(1),\quad n\to\infty,\quad}
\]
with a finite, orbit-dependent \(C\), and the sharper velocity-height relation
\[
\boxed{\quad u_n=\frac{\lambda}{y_n}+\frac{\lambda(\lambda-1)}{3y_n^3}+O(y_n^{-5}).\quad}
\]
The logarithmic correction changes sign at the *exact* coupling \(\lambda=2/5\). At that coupling \(y_n^2-(4/5)n\) converges to a finite constant, whereas for smaller/larger couplings its uncorrected residual diverges negatively/positively on every critical orbit. Sign reflection gives the corresponding result for \(y_0\le0\), \(u_0<0\).

## Assumptions and scope
The state space is real \(\mathbb R^2\), not a periodic quotient. The original parameters satisfy \(0<\lambda=-a<1\), \(b=d=0\), \(c\ne0\), and the initial conditions satisfy \(y_0\ge0\), \(cx_0>0\). The scaled dynamics is exactly
\[
y_{n+1}=y_n+u_n,\qquad u_{n+1}=u_n\left(1-\frac{\lambda}{1+y_n^2}\right).
\]
All statements are quantified over every such coupling and initial height. Critical initial speeds are proven to exist; uniqueness of the critical speed is **not** claimed. The symmetry \((u,y)\mapsto(-u,-y)\) covers the reflected half-plane.

## Proof
**1. Monotonicity and the trichotomy.** Put \(q(y)=1-\lambda/(1+y^2)\). For \(y\ge0\), \(0<q(y)<1\) and \(q\) is nondecreasing. Hence every positive-speed orbit satisfies \(u_n>0\), \(u_{n+1}<u_n\), and \(y_{n+1}>y_n\). Both limits \(u_\infty\ge0\), \(y_\infty\in[y_0,+\infty]\) exist. If \(y_\infty<\infty\), then necessarily \(u_\infty=0\). If \(u_\infty>0\), Cesàro convergence gives \(y_n/n\to u_\infty\). The only remaining case has \(y_\infty=\infty\), \(u_\infty=0\).

**2. Both open phases exist.** If \(u_0/[1-q(y_0+1)]<1\), a geometric comparison traps \(y_n\) below \(y_0+1\); this is a strict condition and gives a nonempty open set of finite-height orbits. For any state with \(Y=y_N\ge0\), \(V=u_N>0\), monotonicity of \(f(y)=1/(1+y^2)\) and the left Riemann-sum estimate give
\[
V-u_\infty=\lambda\sum_{k=N}^{\infty}(y_{k+1}-y_k)f(y_k)
\le\lambda\left[\int_Y^\infty f(t)\,dt+Vf(Y)\right].
\]
For large \(u_0\), the first step has \(y_1=y_0+u_0\to\infty\) and \(u_1=q(y_0)u_0\to\infty\), while the displayed loss bound from step one is \(O(u_0^{-1})\). Thus a nonempty open set of initial speeds has \(u_\infty>0\). More generally, both open-phase properties can be recognized by a strict inequality at some finite iterate, proving openness. Coordinatewise order preservation of \((y,u)\mapsto(y+u,q(y)u)\) on \([0,\infty)\times(0,\infty)\) implies the finite-height set is downward closed in initial speed and the positive-terminal-speed set upward closed. Their complement is therefore a nonempty closed bounded interval, all of whose orbits are critical.

**3. Asymptotic velocity-height relation.** Let \(y_n\to\infty\), \(u_n\to0\). Telescoping the velocity decrements yields
\[
u_n=\lambda\sum_{k=n}^{\infty}\frac{y_{k+1}-y_k}{1+y_k^2}.
\]
The decreasing integrand gives, writing \(I(Y)=\int_Y^\infty dt/(1+t^2)\),
\[
0\le \frac{u_n}{\lambda}-I(y_n)\le\frac{u_n}{1+y_n^2}.
\]
Consequently \(u_n=\lambda/y_n+O(y_n^{-3})\). Expand each left-Riemann excess by Taylor's theorem:
\[
\sum_{k\ge n}\left[u_k f(y_k)-\int_{y_k}^{y_k+u_k}f(t)\,dt\right]
=\frac12\sum_{k\ge n}u_k^2[-f'(y_k)]+O(y_n^{-5}).
\]
Here \(f'(y)=-2y/(1+y^2)^2\), \(f''(y)=O(y^{-4})\), \(u_k=\lambda/y_k+O(y_k^{-3})\), and \(\Delta y_k=u_k\). Comparing the positive monotone sum to its integral (step sizes \(u_k\asymp y_k^{-1}\)) gives
\[
\frac12\sum_{k\ge n}u_k^2[-f'(y_k)]=\frac{\lambda}{3y_n^3}+O(y_n^{-5}).
\]
Finally \(I(Y)=Y^{-1}-\frac13Y^{-3}+O(Y^{-5})\), so
\[
u_n=\frac{\lambda}{y_n}+\frac{\lambda(\lambda-1)}{3y_n^3}+O(y_n^{-5}).
\]

**4. Logarithmic clock.** With \(s_n=y_n^2\), direct expansion using the preceding estimate yields
\[
s_{n+1}-s_n=2y_nu_n+u_n^2
=2\lambda+\frac{\lambda(5\lambda-2)}{3s_n}+O(s_n^{-2}).
\]
Thus \(s_n=2\lambda n+O(\log n)\), whence
\[
s_{n+1}-s_n=2\lambda+\frac{5\lambda-2}{6n}+O\left(\frac{\log n}{n^2}\right).
\]
The error is summable. Summation against \(\sum_{j=1}^{n-1}j^{-1}=\log n+\gamma+o(1)\) gives a finite constant \(C\) and the claimed \(o(1)\) limit. At \(\lambda=2/5\) the harmonic term cancels exactly. This is an infinite-orbit proof, not an inference from finite computation.

## Verification
The included `verify.py` checks the rational-series cancellation exactly for several rational couplings, numerically shoots critical orbits in two noncritical and critical-log couplings, and checks the residual against the derived coefficient. Numerical tests only illustrate the theorem. They are neither used as existence proofs nor treated as exhaustive certification.

## Relationship to prior work
Zhang et al. (2022) introduce the map, its line of equilibria, and numerical attractor diagrams. Their case-I examples focus on stronger negative feedback (for instance \(a=-3\)) and do not present a critical parabolic escape family or the logarithmic coefficient above. Existing published analyses of the *same* rational map include positive-feedback ballistic scattering, and a non-equilibrium forcing regime exhibiting an exponent \(2/3\) critical trajectory. Neither statement implies the present negative-feedback, equilibrium-line \(n^{1/2}\) critical boundary. The integral comparison is classical; the claim is its exact model-specific separator, coefficient, and cancellation threshold.

## Limitations
This theorem does not prove that the critical-speed interval is a singleton; it does not classify initial states outside the indicated sign sectors, nor establish chaotic attractors or backward recurrence. Its \(O\)-constants depend on the orbit and fixed \(\lambda\), and no uniform estimate as \(\lambda\downarrow0\) or \(\lambda\uparrow1\) is claimed. Independent review remains outstanding.

## References
1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, Q.-S. Bi, *A class of two-dimensional rational maps with self-excited and hidden attractors*, Chinese Physics B 31 (2022), 030503, DOI: https://doi.org/10.1088/1674-1056/ac4025 . An accepted manuscript was publicly dated 2021-12-05.
2. *Logarithmic ballistic scattering and a uniform velocity gap in a rational planar map*, publicly indexed mathematical finding (2026-11-02): https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-logarithmic-ballistic-scattering-and-a-uniform-velocity-gap-in-a--c216a2b82ab6 . Accessible description only; full source could not be fetched for this comparison.
3. *Unique subballistic separatrix in a no-equilibrium rational planar map*, publicly indexed mathematical finding (2026-11-02): https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-subballistic-separatrix-in-a-no-equilibrium-rational-plan--a68c4d4e0fdd . Accessible description only; full source could not be fetched for this comparison.
