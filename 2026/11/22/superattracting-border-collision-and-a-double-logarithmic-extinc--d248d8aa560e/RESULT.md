# Superattracting border collision and a double-logarithmic first-passage clock in a dispersal map

## Finding

For the sign-triggered one-species dispersal map of Morozov, Almutairi, Petrovskii and Lai at gain \(\mu=2\), an attracting prime-two cycle meets the switch at \(\varepsilon_*=(\sqrt5-1)/2\). The limiting two-step multiplier is zero. At the threshold, an open trapped interval has a two-point weak empirical limit that is not invariant under the discontinuous map. Above the threshold, the initial state \(x_0=3/5\) first reaches the switch or crosses below it at an even iterate, with first-passage time
\[
\tau(\varepsilon)=2\log_2\log\frac{1}{\varepsilon-\varepsilon_*}+O(1)
\qquad(\varepsilon\downarrow\varepsilon_*^+).
\]
A strict crossing leads to exponential decay to zero. An exact hit at the switch remains there; the formula counts both outcomes and is not a uniform time-to-extinction statement.

More precisely, put \(r=2(1+\varepsilon)\), \(r_*=1+\sqrt5\), \(U_r=1-1/r\) and \(c_r=(1+\sqrt{1-2/r})/2\). For \(3<r<r_*\), every orbit started in \((1/2,c_r)\) except \(U_r\) approaches by parity the attracting cycle
\[
x_\pm(r)=\frac{r+1\pm\sqrt{(r-3)(r+1)}}{2r}.
\]
For \(r=r_*\), every initial point in \((1/2,r_*/4)\) except \(U_{r_*}\) converges by parity to the two endpoints, and the empirical measures converge weakly to \(\nu_*=(\delta_{1/2}+\delta_{r_*/4})/2\). For \(r_*<r\le13/4\), every initial point in \((1/2,1)\) except \(U_r\) reaches \([0,1/2]\).

## Assumptions and scope

On \([0,1]\), use \(F(x)=2x(1-x)\), \(\operatorname{sgn}(0)=0\), and \(1/2<\varepsilon\le5/8\). The map is
\[
H_\varepsilon(x)=\max\{0,F(x)[1+\varepsilon\operatorname{sgn}(x-F(x))]\}.
\]
For \(0<x<1/2\) the map equals \((4-r)x(1-x)\); for \(1/2<x<1\) it equals \(f_r(x)=rx(1-x)\). The endpoints map to zero, and the actual switch value is \(H_\varepsilon(1/2)=1/2\), not \(f_r(1/2)\). The time is \(\tau(\varepsilon)=\min\{n\ge1:H_\varepsilon^n(3/5)\le1/2\}\); the inner logarithm is natural. Parameters and trajectories are considered in real arithmetic.

## Proof

**Branch geometry.** The sign follows from \(x-F(x)=x(2x-1)\). Strictly lower states stay lower and decay at least geometrically since \(0<4-r<1\). On the right, \(f_r\) decreases and \(f_r(c_r)=1/2\). The maximum right extension value \(r/4\) lies below \(c_r\) for \(3<r<r_*\), equals it at \(r_*\), and lies above it for \(r_*<r\le13/4\). Indeed \(f_r(r/4)-1/2=-(r-2)(r^2-2r-4)/16\), and \(r/4\) lies in the decreasing range. Thus \((1/2,c_r)\) is invariant for \(3<r\le r_*\).

**Cycle and critical limit.** The smooth return factors as
\[
 f_r^{\circ2}(x)-x=-x(rx-r+1)(r^2x^2-r(r+1)x+r+1).
\]
The two quadratic roots satisfy \(x_-<U_r<x_+\) for \(r>3\). At a quadratic root, the quadratic relation gives \(f_r(x)=(r+1)/r-x\), so the roots are exchanged. For \(3<r<r_*\), \(x_->1/2\) because \(\sqrt{(r-3)(r+1)}<1\). Then \(f_r(x_+)=x_->1/2\) implies \(x_+<c_r\). The multiplier \(f_r'(x_-)f_r'(x_+)=-r^2+2r+4\) lies in \((0,1)\), while the squared multiplier at \(U_r\) is \((r-2)^2>1\). In the invariant interval \(f_r^2\) is increasing, so any even subsequence is monotone and converges to a fixed point of the smooth return in the closure. Below threshold neither endpoint is a fixed point of that extension. An orbit distinct from \(U_r\) cannot converge to it: the return expands near it and \(f_r\) is injective on the right. Hence the even limit is a cycle coordinate and the odd limit is the other one.

At \(r=r_*\), the two roots are \(1/2\) and \(r_*/4=c_{r_*}\). The same argument on the open trap gives parity convergence to the endpoints, since the branch extension governs each iterate there. Weak empirical convergence follows by taking averages of continuous test functions on the even and odd subsequences. Both endpoints map to \(1/2\) under the actual map, so \((H_{\varepsilon_*})_*\nu_*=\delta_{1/2}\ne\nu_*\).

**Above the threshold.** An orbit that always stays strictly right must stay in \((1/2,c_r)\), since its next state stays right as well. The smooth return is increasing on that interval, as a composition of decreasing branches at arguments strictly above \(1/2\). The even subsequence converges in the closure to a root of \(f_r^2(x)-x\). It cannot converge to \(0\) or \(x_-<1/2\), and if it converged to \(x_+\), the odd subsequence would tend to \(x_-<1/2\). The remaining candidate is \(U_r\); repulsion and injectivity again exclude convergence except from \(U_r\) itself. Thus all other right starting points reach \([0,1/2]\) in finite time. Exact hits are fixed by the sign convention.

**First-passage scale from \(3/5\).** Let \(u_k=H_\varepsilon^{2k}(3/5)-1/2\) up to and including the first nonpositive return, and set
\[
\Delta(r)=\frac{(r-2)(r^2-2r-4)}{16},\qquad C(r)=r^2(r/2-1).
\]
Starting at \(u_0=1/10\), whenever \(0<u_k\le1/10\), the intervening odd state is \(r(1/4-u_k^2)\ge (6/25)r>1/2\). Expansion of the return therefore gives
\[
u_{k+1}=-\Delta+u_k^2(C-r^3u_k^2).
\]
For \(r_*<r\le13/4\), \(0<\Delta\le5/1024\) by monotonicity of the positive factors and evaluation at \(13/4\). For \(0\le u\le1/10\), \(6\le C-r^3u^2\le7\): \(C\) increases from \(2+2\sqrt5\) to \(845/128\), and the subtracted term is at most \((13/4)^3/100\). Thus a still-positive return is at most \((7/10)u_k\), maintaining the premises at each step. The first nonpositive index \(K\) is finite (the upper recurrence would otherwise eventually force negativity), and \(\tau=2K\).

Iteration of the upper bound \(u_{k+1}\le7u_k^2\) while positive gives \(u_k\le(7/10)^{2^k}/7\). Take \(m_+=\lceil\log_2(\log(1/\Delta)/\log(10/7))\rceil\). If \(K>m_+\), then \(u_{m_+}\le\Delta/7\) and \(u_{m_++1}\le\Delta^2/7-\Delta<0\). Thus \(K\le m_++1\).

For the other direction set \(w_k=(3/10)^{2^k}/3\) and \(m_-=\lfloor\log_2(\log(1/\Delta)/(4\log(10/3)))\rfloor\). For \(0\le k\le m_-\) one has \(w_k\ge\Delta^{1/4}/3\ge\sqrt{\Delta/3}\), using \(\Delta<1/9\). If \(u_k\ge w_k\), then \(u_{k+1}\ge6u_k^2-\Delta\ge3u_k^2\ge w_{k+1}\). Starting from \(u_0=w_0\) gives \(K>m_-\) for small \(\Delta\). Hence \(K=\log_2\log(1/\Delta)+O(1)\). Since \(\Delta'(r_*)=(5-\sqrt5)/8>0\) and \(r-r_*=2(\varepsilon-\varepsilon_*)\), this proves the claimed time law. At the threshold the recurrence has \(\Delta=0\), and the bounds by pure squaring give doubly exponential approach from this initial point.

The possibility of exact hits cannot be removed by restricting to a smaller right neighborhood of \(r_*\). Let \(U_j(r)=f_r^{2j}(3/5)-1/2\) denote polynomial iterates of the smooth extension, distinct from the fixed-point notation \(U_r\) above. On \([r_*,13/4]\), all \(U_j(r_*)>0\) by critical trapping. For every sufficiently large integer \(N\), the minimum of the first \(N\) return values is nonpositive at \(13/4\), since a first hit or crossing occurs there and agrees with the smooth extension. Let \(r_N\) be the least parameter where that minimum is nonpositive. Then \(r_N>r_*\) and the minimum is zero by continuity. If \(U_j(r_N)=0\) for some \(j<N\), then \(U_{j+1}(r_N)=-\Delta(r_N)<0\), a contradiction. The earlier returns are therefore positive, the intervening odd states are right-branch states by the bounds above, and the actual orbit first lands exactly at the switch at time \(2N\). For each fixed \(r>r_*\) in the range there is a finite first passage, hence \(r_N\le r\) for all large \(N\); this proves \(r_N\to r_*\).

## Verification

The companion `verify_critical_dispersal.py` checks the return identity, factorization, two-cycle multipliers, critical contacts and selected constants by symbolic algebra, and compares finite exact-rational iterates. Its high-precision parameter probes are finite diagnostics. The branch, first-passage and exact-contact conclusions use the analytic inequalities and continuity arguments above, not an extrapolation from those probes.

## Relationship to prior work and limitations

Morozov et al. introduce the sign-triggered dispersal map. The generic logarithmic ghost law is associated with a nonzero contraction slope (Sections 2.1 and 3.1, Table 1); the return here has zero slope and a quadratic leading term. Virtual period-two collisions with zero limiting multiplier are also known for an additively shifted discontinuous logistic map (Krishnan Nair and Nandakumaran). The distinction here is the explicit border, limiting measure and fixed-initial-condition first-passage law for the multiplicatively modified dispersal map. A basin-selection finding for the same model addresses a different parameter range (Resultary identifier `dafee39a2bfd`); a noninvariant two-point ghost is also the subject of a discontinuous power-map finding (`3ab687079720`). These comparisons are not a universal historical priority claim. In particular, the full 1993 sectional-discontinuity paper was not assessed.

The time law concerns the fixed initial condition \(3/5\) at gain \(\mu=2\) and the given switch convention. It makes no assertion about ensemble-average lifetimes, other gains, noisy or rounded dynamics, or biological extinction times. Strict crossings are followed by asymptotic decay to zero; equality yields no such decay.

## References

1. A. Yu. Morozov, D. Almutairi, S. V. Petrovskii, and Y.-C. Lai, “Long transients in discontinuous time-discrete models of population dynamics,” *Chaos, Solitons & Fractals* **174** (2023), 113707. https://doi.org/10.1016/j.chaos.2023.113707
2. P. R. Krishnan Nair and V. M. Nandakumaran, “Existence of multiple attractors and the nature of bifurcations in a discontinuous logistic map,” *Pramana* **51** (1998), 377–385.
3. B. L. Tan and T. T. Chia, “Properties of a logistic map with a sectional discontinuity,” *Physical Review E* **47** (1993), 3087–3098. https://doi.org/10.1103/PhysRevE.47.3087
