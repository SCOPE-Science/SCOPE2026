# Exact four-node positivity phase diagram for centered convection-diffusion theta stepping

## Finding
For the standard centered method-of-lines discretization of one-dimensional periodic convection-diffusion on **four** equally spaced sites, the following gives the complete strictly positive-step range in the advection-dominated regime, including a sharp second-order Crank–Nicolson cutoff.

Let \(a>0\) be the centered convection coefficient and \(0<d<a\) the centered diffusion coefficient. Set \(\kappa=d/a\in(0,1)\). Let \(S\) cyclically shift the four coordinates, and define
\[
A=(d+a)S+(d-a)S^{-1}-2dI,\qquad
M_{\theta,h}=(I-\theta hA)^{-1}(I+(1-\theta)hA).
\]
Here \(\theta\in[0,1]\) and \(h>0\). A completed step preserves nonnegative vectors precisely when \(M_{\theta,h}\) is entrywise nonnegative. For \(\theta>0\), put \(t=a\theta h\) and
\[
F_\kappa(t)=(1+2\kappa t)^2+4t^2,\qquad
R_\kappa(t)=\frac14\left(1+\frac1{1+4\kappa t}+\frac{2(1+2\kappa t)}{F_\kappa(t)}\right),
\]
\[
t_*(\kappa)=\frac{\kappa(1-\kappa)+\sqrt{\kappa(1-\kappa^2)}}{2\kappa(1+\kappa^2)},
\quad
\theta_*(\kappa)=1-R_\kappa(t_*(\kappa)).
\]
**Exact criterion:**
\[
M_{\theta,h}\ge0 \ \Longleftrightarrow\ 
\theta>0,\quad t\ge t_*(\kappa),\quad \theta\ge 1-R_\kappa(t).
\]
For \(\theta=0\) no positive step works. The function \(R_\kappa\) decreases strictly from \(1\) to \(1/4\). Thus \(0<\theta_*<3/4\), and the complete phase diagram is:

1. \(0\le\theta<\theta_*\): no positive timestep.
2. \(\theta=\theta_*\): exactly one timestep, \(a\theta h=t_*\).
3. \(\theta_*<\theta<3/4\): exactly one closed, nondegenerate interval \(t_*\le a\theta h\le t^{\rm up}_\theta\), where \(R_\kappa(t^{\rm up}_\theta)=1-\theta\).
4. \(3/4\le\theta\le1\): precisely the half-line \(a\theta h\ge t_*\).

In particular the **Crank–Nicolson** choice \(\theta=1/2\) admits a positive timestep if and only if
\[
\boxed{\kappa\ge\sqrt2-1}\qquad(0<\kappa<1).
\]
At equality, the only permitted step satisfies \(a h=1+\sqrt2/2\); the update kernel at that point, up to reversing cyclic orientation, is \( (0,2-\sqrt2,\sqrt2-1,0)\). For \(\sqrt2-1<\kappa<1\), the admissible Crank–Nicolson steps form a nondegenerate bounded interval. For \(0<\kappa<\sqrt2-1\) no strictly positive Crank–Nicolson step preserves nonnegativity. The critical ratio is below the standard spatial monotonicity threshold \(\kappa=1\).

The pure-advection limit is singular: \(t_*(\kappa)\sim (2\sqrt\kappa)^{-1}\) as \(\kappa\downarrow0\), and \(\theta_*(\kappa)\to1/2\), whereas at \(\kappa=0\) every finite positive step fails for every \(\theta\in[0,1]\).

## Assumptions and scope
Take four periodic sites with a uniform positive spacing \(\Delta x\). For the PDE \(u_t=v u_x+\nu u_{xx}\) with constants \(v,\nu>0\), the coefficients are \(a=v/(2\Delta x)\) and \(d=\nu/(\Delta x)^2\). The domain \(0<\kappa<1\) corresponds to convection-dominated centered spatial differencing (cell Péclet number \(v\Delta x/\nu>2\)), so the semidiscrete matrix has a negative off-diagonal entry. The theorem concerns the completed theta step, not intermediate-stage values, accuracy, or continuous-time positivity of the semidiscretization. Both endpoints of each admissible timestep interval are included.

## Proof
Write \(Q(t)=(I-\theta hA)^{-1}=(I-(t/a)A)^{-1}\) for \(\theta>0\). The four Fourier eigenvalues of \(A/a\) are \(0,-4\kappa,-2\kappa+2i,-2\kappa-2i\). Inverting gives the four circulant kernel coefficients, up to interchanging the clockwise and counterclockwise neighbors:
\[
q_0=R_\kappa(t),\quad
q_2=\frac14\left(1+\frac1{1+4\kappa t}-\frac{2(1+2\kappa t)}{F_\kappa(t)}\right),
\]
\[
q_{\rm good}=\frac14\left(1-\frac1{1+4\kappa t}+\frac{4t}{F_\kappa(t)}\right),\quad
q_{\rm bad}=\frac14\left(1-\frac1{1+4\kappa t}-\frac{4t}{F_\kappa(t)}\right).
\]
The good neighbor is positive for \(t>0\). Since \(F_\kappa(t)>(1+2\kappa t)^2\) and the function \(x\mapsto1/x\) is strictly convex, \(2(1+2\kappa t)/F_\kappa(t)<2/(1+2\kappa t)<1+1/(1+4\kappa t)\); hence \(q_2>0\). The remaining neighbor satisfies the exact sign identity
\[
q_{\rm bad}=\frac{t P_\kappa(t)}{(1+4\kappa t)F_\kappa(t)},\qquad
P_\kappa(t)=4\kappa(1+\kappa^2)t^2-4\kappa(1-\kappa)t+\kappa-1.
\]
The quadratic has positive leading coefficient and negative constant term, hence exactly one positive root; the quadratic formula gives \(t_*(\kappa)\). Therefore all resolvent off-diagonals are nonnegative exactly for \(t\ge t_*\).

The theta update has the identity \(M_{\theta,h}=\theta^{-1}\bigl(Q(t)-(1-\theta)I\bigr)\). Consequently, its nonnegativity adds exactly one diagonal requirement \(q_0=R_\kappa(t)\ge1-\theta\). Every nonzero Fourier mode has a strictly decreasing real resolvent contribution: \((1+4\kappa t)^{-1}\) decreases and
\[
\frac{d}{dt}\frac{1+2\kappa t}{F_\kappa(t)}
=-\frac{2\kappa(1+2\kappa t)^2+8t+8\kappa t^2}{F_\kappa(t)^2}<0.
\]
Thus \(R_\kappa(t)\) decreases strictly from \(1\) to \(1/4\), giving all four branches of the phase diagram. For \(\theta=0\) the explicit update has a negative neighbor \(h(d-a)\), so none works.

For Crank–Nicolson, the unique interval is nonempty exactly when \(R_\kappa(t_*)\ge1/2\). On the root of \(P_\kappa\), substitute \(\kappa F_\kappa(t_*)=1+4\kappa t_*\) to obtain
\[
R_\kappa(t_*)=\frac{(1+\kappa)(1+2\kappa t_*)}{2(1+4\kappa t_*)}.
\]
Therefore \(R_\kappa(t_*)\ge1/2\) is equivalent to \(t_*\le[2(1-\kappa)]^{-1}\). Because \(P_\kappa\) has exactly one positive root and is negative before it, this is equivalent to \(P_\kappa([2(1-\kappa)]^{-1})\ge0\). Direct substitution yields
\[
P_\kappa\!\left(\frac1{2(1-\kappa)}\right)
=\frac{\kappa^2+2\kappa-1}{(1-\kappa)^2}.
\]
The unique root in \((0,1)\) is \(\sqrt2-1\). At equality \(t_*=(2+\sqrt2)/4\), so \(a h=2t_*=1+\sqrt2/2\). Finally the closed form for \(t_*\), together with \(R_\kappa\), gives the stated singular limits.

## Verification
Run `python verify.py` with Python 3 and SymPy. The script checks symbolic resolvent identities, the sharp critical algebraic point, the polynomial boundary relation, 320 exact-rational comparisons with direct four-by-four matrix inversion and exact Crank–Nicolson interval witnesses. The exact proof above, not finite enumeration, establishes all positive real parameters. As an example, at \(\kappa=1/2\), Crank–Nicolson works precisely for \(a h\in[2(1+\sqrt6)/5,\,2u]\), where \(u\approx0.8052200399\) is the unique positive root of \(5u^3-2u-1=0\).

## Relationship to prior work
Hadjimichael, Ketcheson and Lóczi (arXiv:2105.07403v1, Theorem 1(i)) prove that the centered pure-advection theta step cannot preserve nonnegativity on any even periodic grid. The present result instead adds a strictly positive diffusion coefficient and exactly resolves the first nontrivial even grid, including a singular zero-diffusion limit and the second-order cutoff. Fekete, Ketcheson and Lóczi (arXiv:1610.00228v1, Section 6) analyze centered spatial discretizations with explicit Runge–Kutta methods, rather than this implicit theta-step positivity phase. Other work on monotone convection-diffusion discretizations introduces characteristic procedures or positivity limiters rather than proving positivity reentry of this unmodified centered theta matrix. None of these distinctions alone establishes exhaustive historical priority.

## Limitations
The sharp phase diagram is for four periodic sites with constant coefficients and \(0<d<a\). It is not asserted for arbitrary grid counts, nonuniform meshes, nonperiodic boundaries, or variable coefficients. This is a positivity statement, not a recommendation to take very large timesteps: spatial accuracy and time accuracy may be poor even when the completed numerical step is nonnegative. No independent validation or exhaustive historical-priority certification has been performed.

## References
1. Y. Hadjimichael, D. I. Ketcheson, L. Lóczi, *Positivity preservation of implicit discretizations of the advection equation*, arXiv:2105.07403v1 (first public 2021-05-16), https://arxiv.org/abs/2105.07403.
2. I. Fekete, D. I. Ketcheson, L. Lóczi, *Positivity for convective semi-discretizations*, arXiv:1610.00228 (first public 2016-10-02), https://arxiv.org/abs/1610.00228.
3. X. Li, K. Fu, *Positive and Conservative Characteristic Block-Centered Finite Difference Methods for Convection Dominated Diffusion Equations*, Adv. Appl. Math. Mech. 14 (2022), 1087–1110, https://doi.org/10.4208/aamm.OA-2021-0051 (distinct scheme; abstract consulted).
4. MSC2020 classification 65M06, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=65Mxx.
