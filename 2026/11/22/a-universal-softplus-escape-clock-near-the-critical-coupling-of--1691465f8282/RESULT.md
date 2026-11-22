# A universal softplus escape clock near the critical coupling of a Gaussian map

## Finding
Fix any real \(a>0\) and \(r_0>\sqrt{2}\). In the symmetrically coupled Gaussian-cubic planar map
\[
F_{a,b}(x,y)=\bigl(f_a(x)+b(y-x),\ f_a(y)+b(x-y)\bigr),\qquad
f_a(x)=ax(1-x^2)e^{-x^2},
\]
put \(b=1/2+\varepsilon\), \(\varepsilon>0\), and start at \((x_0,y_0)=(r_0,-r_0)\). For \(0<2\varepsilon<ae^{-2}\), let \(U_\varepsilon>2\) be the unique large solution of
\[
a(U_\varepsilon-1)e^{-U_\varepsilon}=2\varepsilon.
\]
For each fixed real \(t\), define the first-passage index
\[
N_\varepsilon(t)=\min\{n\geq0:\ x_n^2\geq U_\varepsilon+t\}.
\]
Then \(N_\varepsilon(t)\) is finite, and the **near-critical escape clock** has the exact universal scaling limit
\[
\boxed{\lim_{\varepsilon\downarrow0}4\varepsilon U_\varepsilon N_\varepsilon(t)=\log(1+e^t).}
\]
The limit is independent of both \(a\) and the fixed starting radius \(r_0\). Equivalently, for every fixed \(\tau>0\), the squared amplitude at discrete time \(n_\varepsilon=\lfloor\tau/(4\varepsilon U_\varepsilon)\rfloor\) satisfies
\[
\boxed{x_{n_\varepsilon}^2-U_\varepsilon\longrightarrow\log(e^\tau-1).}
\]
The large root obeys \(U_\varepsilon=L_\varepsilon+\log L_\varepsilon+o(1)\), where \(L_\varepsilon=\log(a/(2\varepsilon))\). This theorem concerns the positive detuning side only; it does not reassert the already-known classification of periodic orbits at negative detuning or the critical-boundary escape law.

## Assumptions and scope
All parameters and initial coordinates are real and the map is evaluated in exact arithmetic. The gain \(a>0\) and initial radius \(r_0>\sqrt{2}\) are independent of \(\varepsilon\), which tends to zero through positive values. The root \(U_\varepsilon\) is the root larger than 2; an additional root between 1 and 2 exists but is not the definition here. The initial condition lies on the invariant antidiagonal \(y=-x\); the claimed finite-time crossover is not a full-plane statement. In the equivalent orbit statement, \(\tau\) ranges over fixed positive values, and the convergence is not asserted at \(\tau=0\).

## Proof
**Exact reduction and root.** Oddness of \(f_a\) makes the antidiagonal invariant. Its signed coordinate obeys \(x_{n+1}=f_a(x_n)-(1+2\varepsilon)x_n\). For \(|x_n|>1\), the sign alternates and the amplitude increases strictly. Set \(u_n=x_n^2\). For all \(n\geq0\), since \(u_0=r_0^2>2\),
\[
u_{n+1}=u_n\bigl[1+h_\varepsilon(u_n)\bigr]^2,\quad
h_\varepsilon(u)=2\varepsilon+a(u-1)e^{-u},
\]
and hence \(u_{n+1}-u_n=q_\varepsilon(u_n):=u_n[2h_\varepsilon(u_n)+h_\varepsilon(u_n)^2]>0\). As \(q_\varepsilon(u)\ge4\varepsilon u\), \(u_n\to\infty\); all first-passage indices are finite once \(\varepsilon\) is sufficiently small. The scalar function \((u-1)e^{-u}\) decreases strictly from \(e^{-2}\) to zero on \((2,\infty)\), proving existence and uniqueness of \(U_\varepsilon\). Taking logarithms of its defining equation gives \(U_\varepsilon-\log(U_\varepsilon-1)=L_\varepsilon\), so \(U_\varepsilon=L_\varepsilon+\log L_\varepsilon+o(1)\).

**Exact scaled increment in the transition layer.** Fix a compact interval of \(w\) values. The root identity gives
\[
h_\varepsilon(U_\varepsilon+w)=2\varepsilon\left[1+e^{-w}\frac{U_\varepsilon+w-1}{U_\varepsilon-1}\right].
\]
It follows, uniformly on every such compact interval, that
\[
\frac{q_\varepsilon(U_\varepsilon+w)}{4\varepsilon U_\varepsilon}\longrightarrow 1+e^{-w},
\qquad \sup_{w\in I}q_\varepsilon(U_\varepsilon+w)\longrightarrow0.
\]
Thus, for each fixed \(L>0\) and \(t>-L\), the scaled number of steps from the first crossing of \(U_\varepsilon-L\) to the first crossing of \(U_\varepsilon+t\) tends to the Riemann integral
\[
\int_{-L}^t\frac{dw}{1+e^{-w}}
=\log(1+e^t)-\log(1+e^{-L}).
\]
The possible one-step overshoot at either finite layer boundary is \(o(1)\) in squared amplitude and hence changes the scaled time by \(o(1)\). These conclusions follow from summing the reciprocal of the positive scaled increments; no continuous-time approximation is assumed.

**The remote entrance takes negligible scaled time.** Put \(q_0(u)=2au(u-1)e^{-u}\). For \(u>2\), \(q_\varepsilon(u)\ge q_0(u)\), and \(q_0\) is strictly decreasing on \([4,\infty)\). Choose a fixed \(M>\max\{u_0,10\}\) large enough that \(q_0(u)\le1/4\) and \(a(u-1)e^{-u}\le1/16\) for \(u\ge M\). The number of steps required to cross \(M\) is bounded independently of \(\varepsilon\), by the strict positivity of \(q_0\) on the fixed finite interval. For any fixed \(L>0\), when \(\varepsilon\) is small and \(u\in[M,U_\varepsilon-L]\), we have \(q_\varepsilon(u)<1\) (because \(u\varepsilon\to0\) uniformly on this interval, and \(u(u-1)e^{-u}\) is small for large \(M\)). Consequently the overshoot at \(U_\varepsilon-L\) is at most 1. For each step beginning at \(v\ge M\), decreasingness of \(q_0\) gives
\[
1\le\int_v^{v+q_\varepsilon(v)}\frac{ds}{q_0(s)}.
\]
Summation, with a constant independent of \(\varepsilon\), yields
\[
N_\varepsilon(-L)\le C+\int_M^{U_\varepsilon-L+1}\frac{e^s}{2as(s-1)}\,ds.
\]
As \(U_\varepsilon\to\infty\), the integral is asymptotic to \(e^{U_\varepsilon-L+1}/[2a(U_\varepsilon-L+1)(U_\varepsilon-L)]\). Using \(4\varepsilon U_\varepsilon=2aU_\varepsilon(U_\varepsilon-1)e^{-U_\varepsilon}\) shows
\[
\limsup_{\varepsilon\downarrow0}4\varepsilon U_\varepsilon N_\varepsilon(-L)\le e^{1-L}.
\]
The right side vanishes when \(L\to\infty\).

**The limit and its inverse.** Add the remote entrance estimate to the transition-layer Riemann sum. Taking \(\varepsilon\downarrow0\) first, then \(L\to\infty\), traps the total scaled first-passage time at \(\log(1+e^t)\), proving the boxed first limit. The limiting function is strictly increasing, continuous, and ranges over \((0,\infty)\), so the monotonicity of \(u_n\) and vanishing transition-layer step sizes imply inversion of the first-passage limit: at scaled time \(\tau>0\), the centered squared amplitude converges to \(\log(e^\tau-1)\). The floor in \(n_\varepsilon\) changes scaled time by at most \(4\varepsilon U_\varepsilon\to0\).

## Verification
The self-contained `verify.py` checks the exact antidiagonal recurrence against direct two-coordinate iteration, the defining root identity, the scaled layer increment against its limiting vector field, and convergence trends for several decreasing positive detunings. These finite checks are diagnostics; the limit for every real \(a>0\), fixed \(r_0>\sqrt2\), and fixed \(t\) is established solely by the analytic proof. Run with `python3 verify.py` using the Python standard library.

## Relationship to prior work
Soula, Jahanshahi, Al-Barakati and Moroz [1] introduced the Gaussian-cubic coupled map and investigated its numerical bifurcations, synchronization and basin topology. A later exact analysis [2] proves the sharp compact-absorption boundary and the logarithmic escape law *at* \(b=1/2\). A separate finite-orbit classification [3] already identifies the large antipodal period-two branch for \(b<1/2\). These previously established statements are not claimed as new here. The current theorem concerns the **different double limit** of positive detuning \(b-1/2=\varepsilon\downarrow0\) and first-passage time \(n\asymp(\varepsilon\log(1/\varepsilon))^{-1}\), identifying the entire nontrivial crossover profile rather than only the static threshold or a fixed-parameter orbit.

## Limitations
The results hold on the exact invariant antidiagonal for a fixed starting radius. They do not establish the same universal profile for arbitrary off-antidiagonal initial conditions, for parameter-dependent initial radii, or at the limiting initial time \(\tau=0\). The asymptotic does not supply finite-\(\varepsilon\) error constants. The literature investigation cannot guarantee priority against unindexed or inaccessible equivalent works. Numerical checks do not constitute an infinite proof or independent validation.

## References
[1] Y. Soula, H. Jahanshahi, A. A. Al-Barakati and I. Moroz, *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps*, Mathematics 11 (2023), 1517; first published 21 March 2023; DOI 10.3390/math11061517; https://www.mdpi.com/2227-7390/11/6/1517.

[2] *A sharp global boundedness interval and logarithmic critical escape in a coupled Gaussian map* (2026), public mathematical finding, identifier f463338d3c52. Its complete theorem and proof were compared with the new claim.

[3] *Bistable coexistence and an exact antidiagonal basin separator in a coupled Gaussian map* (2026), related mathematical analysis, identifier 483979a4-5fcf-47cd-ac80-e1a8fb37478a; the previously established large-cycle asymptotic is not reused as the present finding.
