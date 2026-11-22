# Superattracting border collision and a double-logarithmic extinction clock in a dispersal map

## Finding

For the sign-triggered one-species dispersal map of Morozov, Almutairi, Petrovskii and Lai, the gain \(\mu=2\) has a sharp border loss of an attracting prime-two cycle at the golden-ratio dispersal strength
\[
\varepsilon_*=(\sqrt5-1)/2.
\]
The switch is unusually degenerate: the limiting two-step multiplier is zero, not a positive contraction factor. At the threshold the lost cycle persists as a *nonstationary weak empirical limit* on a trapped open interval. For \(\varepsilon>\varepsilon_*\), the initial state \(x_0=3/5\) escapes that ghost and enters the extinction branch after a first-passage time satisfying
\[
\boxed{\tau(\varepsilon)=2\log_2\!\log\frac1{\varepsilon-\varepsilon_*}+O(1)}
\quad(\varepsilon\downarrow\varepsilon_*^+).
\]
The coefficient \(2\) is exact; the double logarithm is genuinely slower than the generic logarithmic discontinuous-ghost law described for nonzero return slope in the originating study.

More precisely, put \(r=2(1+\varepsilon)\), \(r_*=1+\sqrt5\), and \(c_r=(1+\sqrt{1-2/r})/2\). For \(3<r<r_*\), every orbit started in \((1/2,c_r)\) except the repelling right-branch fixed point \(U_r=1-1/r\) approaches the attracting prime-two cycle
\[
x_\pm(r)=\frac{r+1\pm\sqrt{(r-3)(r+1)}}{2r}.
\]
For \(r=r_*\), every orbit in \((1/2,r_*/4)\), again except \(U_{r_*}\), converges by parity to the pair \(\{1/2,r_*/4\}\), and its empirical measure converges weakly to
\[
\nu_*=(\delta_{1/2}+\delta_{r_*/4})/2,
\]
which is **not invariant** under the actual discontinuous map. For \(r_*<r\le13/4\), every right-branch orbit other than the fixed point \(U_r\) eventually reaches \([0,1/2]\); a strict landing below \(1/2\) then tends exponentially to extinction. The first such landing from \(x_0=3/5\) is at an even iterate and has the displayed double-logarithmic asymptotic.

## Assumptions and scope

The phase space is \([0,1]\); take \(\operatorname{sgn}(0)=0\), \(F(x)=2x(1-x)\), and
\[
H_\varepsilon(x)=\max\{0,F(x)[1+\varepsilon\operatorname{sgn}(x-F(x))]\},\quad 1/2<\varepsilon\le5/8.
\]
The maximum is inactive on \([0,1]\). At \(0<x<1/2\), \(H_\varepsilon(x)=(4-r)x(1-x)\); at \(1/2<x<1\), \(H_\varepsilon(x)=r x(1-x)\). Exactly at \(x=1/2\), the map gives \(H_\varepsilon(1/2)=1/2\). At the endpoints \(0,1\) it gives zero. We call \(f_r(x)=rx(1-x)\) the smooth right-branch extension and never substitute it for the true map at the switch. The interval \((1/2,c_r)\) is relevant when \(3<r\le r_*\); for \(r>r_*\) we discuss all starting states in \((1/2,1)\). The fixed initial condition for the escape statement is \(x_0=3/5\), and
\[
\tau(r)=\min\{n\ge1:H_\varepsilon^n(3/5)\le1/2\}.
\]
The limit concerns real arithmetic, the stated zero-sign convention and \(\varepsilon\downarrow\varepsilon_*\) from above. The logarithm inside the formula is natural; \(\log_2\) is base two.

## Proof

**1. Branch geometry and exact border.** The identity \(x-F(x)=x(2x-1)\) gives the branches. Since \(4-r<1\) for \(3<r\le13/4\), every strictly lower-branch state stays strictly lower and tends exponentially to zero. On the right, \(f_r\) is strictly decreasing, and \(f_r(c_r)=1/2\). For \(3<r<r_*\), the inequality \(r/4<c_r\) follows from \(r^2(4-r)>8\), equivalently \(r<1+\sqrt5\). Therefore \(f_r((1/2,c_r))\subset(1/2,c_r)\). At \(r=r_*\), the interval \((1/2,c_{r_*})=(1/2,r_*/4)\) is likewise mapped into itself: its smooth endpoint images are exchanged. Above \(r_*\), the same endpoint inequality reverses, so right-branch excursions can exit below the switch.

**2. Stable cycle below the threshold.** Direct algebra factors the second iterate:
\[
f_r^{\circ2}(x)-x=-x(rx-r+1)\bigl(r^2x^2-r(r+1)x+r+1\bigr).
\]
For \(3<r<r_*\), the quadratic roots are precisely \(x_-(r),x_+(r)\) above; both belong to \((1/2,c_r)\), and \(x_-<U_r<x_+\). Their two-step multiplier is \(m(r)=-r^2+2r+4\in(0,1)\), whereas \((f_r'(U_r))^2=(r-2)^2>1\). On the forward-invariant interval \(f_r\) is decreasing, hence \(f_r^2\) is increasing. Its even iterates are monotone after the first iterate, bounded, and converge to a fixed point of \(f_r^2\). The fixed point \(U_r\) is repelling and cannot be the limit of any distinct right-branch orbit, because the branch is injective and expands in a neighborhood of \(U_r\). Thus every other point in the interval converges by parity to the attractive two-cycle. All of these statements concern the *actual* map since no iterate reaches the switch.

**3. Critical ghost, not a periodic orbit.** At \(r=r_*\), the two cycle coordinates meet the interval endpoints: \(x_-(r_*)=1/2\), \(x_+(r_*)=r_*/4=c_{r_*}\). They satisfy \(f_{r_*}(1/2)=r_*/4\) and \(f_{r_*}(r_*/4)=1/2\), but **not** \(H_{\varepsilon_*}(1/2)=r_*/4\): the actual switch is fixed. The monotone second-iterate argument shows that points below \(U_{r_*}\) in the open trap have even iterates tending to \(1/2\) and odd iterates to \(r_*/4\); the parity is reversed for points above \(U_{r_*}\). Consequently their empirical measures tend to \(\nu_*\). As \(H_{\varepsilon_*}(1/2)=H_{\varepsilon_*}(r_*/4)=1/2\), one has \((H_{\varepsilon_*})_*\nu_*=\delta_{1/2}\ne\nu_*\). This proves the claimed nonstationarity without asserting that the map lacks all invariant measures; in fact it has fixed points.

**4. Escape and extinction above the border.** For \(r_*<r\le13/4\), if an orbit remained in \((1/2,1)\) for all times, its even subsequence would be monotone under the increasing continuous right return \(f_r^2\), and hence converge to one of its fixed points. By the exact factorization these are \(0,U_r,x_-(r),x_+(r)\). Here \(x_-(r)<1/2\), and \(f_r(x_+(r))=x_-(r)<1/2\), so the two-cycle is incompatible with remaining right; zero is likewise impossible. A limiting endpoint \(1/2\) is impossible since \(f_r^2(1/2)<1/2\). Therefore the only possible eternally right orbit is \(U_r\), which is repelling and whose unique right preimage is itself. Every other right starting state has a finite iterate in \([0,1/2]\). Strict entry below the switch implies exponential extinction by Step 1; an exact landing at the switch instead remains there. This distinction matters at the discontinuity.

**5. The exact two-step normal form.** For the particular initial state \(3/5\), write \(u_k=H_\varepsilon^{2k}(3/5)-1/2\) until the first nonpositive \(u_k\). Each preceding \(u_k\) lies in \((0,1/10]\), and the intermediate odd iterate is \(r(1/4-u_k^2)>1/2\). Direct expansion, therefore using the correct branch twice, gives
\[
u_{k+1}=-\Delta(r)+u_k^2\bigl(C(r)-r^3u_k^2\bigr),
\]
where
\[
\Delta(r)=\frac{(r-2)(r^2-2r-4)}{16},\qquad C(r)=r^2(r/2-1).
\]
For \(r_*<r\le13/4\), \(0<\Delta\le5/1024\), and for \(0\le u\le1/10\) the **uniform exact bounds**
\[
6\le C(r)-r^3u^2\le7
\]
hold. Indeed \(C\) increases on this interval and \(C(r_*)=2+2\sqrt5\), while \(r^3u^2\le(13/4)^3/100\), giving the lower bound; \(C(13/4)=845/128<7\) gives the upper bound. Consequently \(u_{k+1}\le7u_k^2-\Delta\le(7/10)u_k\) while it remains positive, and the first nonpositive index \(K\) is finite. The first threshold crossing occurs exactly at \(\tau(r)=2K\).

**6. Matching double-logarithmic bounds.** While all earlier even iterates are positive,
\[
u_k\le \frac17\left(\frac7{10}\right)^{2^k}.
\]
Choose \(m_+=\left\lceil\log_2(\log(1/\Delta)/\log(10/7))\right\rceil\). If \(K>m_+\), then \(u_{m_+}\le\Delta/7\) and the next recurrence gives \(u_{m_++1}\le\Delta^2/7-\Delta<0\); hence \(K\le m_++1\). For the matching lower bound let
\[
m_- =\left\lfloor\log_2\left(\frac{\log(1/\Delta)}{4\log(10/3)}\right)\right\rfloor.
\]
Set \(w_k=\frac13(3/10)^{2^k}\). Since \(\Delta\le5/1024<1/9\), for \(k\le m_-\) one has \(w_k\ge\Delta^{1/4}/3\ge\sqrt{\Delta/3}\). Inductively \(u_k\ge w_k>0\) for these indices: if \(u_k\ge w_k\), then \(u_k\ge\sqrt{\Delta/3}\) and \(u_{k+1}\ge6u_k^2-\Delta\ge3u_k^2\ge3w_k^2=w_{k+1}\). Thus \(K>m_-\). Together,
\[
K=\log_2\log(1/\Delta)+O(1).
\]
Finally \(\Delta(r_*)=0\) and \(\Delta'(r_*)=(5-\sqrt5)/8>0\), while \(r-r_*=2(\varepsilon-\varepsilon_*)\). Therefore \(\Delta\asymp\varepsilon-\varepsilon_*\) and the claimed coefficient \(2\) follows. The bounds are rigorous for arbitrary real parameter values, not inferred from sampled iterates. At the threshold itself \(\Delta=0\), and the same quadratic comparison shows doubly exponential approach to the two virtual endpoints.

## Verification

The standalone `verify_critical_dispersal.py` requires Python 3 and SymPy (mpmath is used for optional diagnostics). From the package directory run `python verify_critical_dispersal.py`. It verifies the exact factorization, two-step polynomial identity, critical contacts, derivative and rational parameter bounds symbolically, plus checks sample rational iterates independently and seven high-precision first-passage examples. The proof of the all-real-parameter theorem is the analytic argument above; the finite diagnostics do not substitute for the quantifiers. Crucial comparison inequalities are simple exact algebraic bounds, not floating-point interval claims.

## Relationship to prior work

Morozov et al. (2023), Section 2.1, introduce exactly this sign-triggered density-dispersal map. Their Table 1 and Section 3.1 describe a logarithmic transient lifetime near a generic discontinuous ghost and explicitly assume a locally linear two-step return with \(0<K<1\); the present critical return has \(K=0\) and a *different* first-passage scale. Their Appendix A analyzes separate three-step trapping inequalities; neither gives this exact golden-ratio two-cycle border or its double-logarithmic exit law.

Krishnan Nair and Nandakumaran (1998) already established the **general mechanism** of a virtual period-two orbit meeting a central discontinuity, including its zero multiplier, for an **additively shifted** piecewise logistic map. We do not claim that mechanism is new. Their right branch has the form \(4\lambda x(1-x)-C\), whereas the present right branch is \(r x(1-x)\) and the left branch has a different multiplier. Their analysis of virtual cycles and precision-dependent recurrence does not give the stated fixed-initial-condition parameter-detuning double-logarithmic extinction clock.

A published 2026 analysis of the **same Morozov model** at \(\mu=2\) classifies \(0<\varepsilon<1/2\), a disjoint range in which right-branch fixed points rather than the present collapsing prime-two cycle govern the dynamics. A separate published 2026 theorem on a discontinuous power-map family shows nonstationary ghost empirical limits, but with different functions, conditions and no present double-logarithmic clock. The broad mechanisms are credited; the claimed extension is the exact boundary and sharp transient exponent for the 2023 dispersal map.

## Limitations

The explicit first-passage asymptotic is for the single initial condition \(x_0=3/5\), not an ensemble-averaged transient lifetime. Its critical rate is special to \(\mu=2\), the stated sign convention and \(\varepsilon\downarrow\varepsilon_*\); no claim is made for other growth gains, noisy parameters, machine-rounded trajectories, or a different switch value. An exact threshold hit settles at \(1/2\), not extinction. Classical superattracting iteration explains the mathematical mechanism; novelty is claimed only for the explicitly computed parameter threshold and quantified full-map transition. The full 1993 sectional-discontinuity article could not be inspected through lawful open access; the accessible abstract and the full 1998 related study were checked, leaving some literature-priority uncertainty. This is a self-review, not independent validation.

## References

1. A. Yu. Morozov, D. Almutairi, S. V. Petrovskii, and Y.-C. Lai, “Long transients in discontinuous time-discrete models of population dynamics,” *Chaos, Solitons & Fractals* **174** (2023), 113707. First verified online date 2023-07-12. https://doi.org/10.1016/j.chaos.2023.113707; lawful full text https://chaos1.la.asu.edu/~ylai1/papers/CSF_2023_MAPL.pdf.
2. P. R. Krishnan Nair and V. M. Nandakumaran, “Existence of multiple attractors and the nature of bifurcations in a discontinuous logistic map,” *Pramana* **51** (1998), 377–385. Full text https://webfiles.amrita.edu/2017/06/existence-of-multiple-attractors-and-the-nature-of-bifurcations-in-a-discontinuous-logistic-map.pdf.
3. B. L. Tan and T. T. Chia, “Properties of a logistic map with a sectional discontinuity,” *Physical Review E* **47** (1993), 3087–3098. https://doi.org/10.1103/PhysRevE.47.3087 (abstract available; full text not inspected).
4. “Exact basin selection and fractional-power response at a discontinuous logistic border,” published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-basin-selection-and-fractional-power-response-at-a-discont--dafee39a2bfd.
5. “An attracting two-cycle disappears into a nonstationary ghost at a discontinuity,” published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-an-attracting-two-cycle-disappears-into-a-nonstationary-ghost-at--3ab687079720.
