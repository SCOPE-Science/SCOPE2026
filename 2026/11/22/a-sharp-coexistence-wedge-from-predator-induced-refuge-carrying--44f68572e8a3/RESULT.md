# A sharp coexistence wedge from predator-induced refuge carrying capacity

## Finding

Consider the spatially homogeneous reaction part of the active/hidden-prey, searching/handling-predator limit model of Bisi, Bondesan, Groppi and Soresina [1], with equal prey-state growth rates and carrying capacities, scaled to one, and refuge and handling ratios scaled to one. For arbitrary \(a,b,\mu>0\), the equations are
\[
\dot x=x-\frac{x^2(1+y^2)}{(1+y)^2}-\frac{axy}{1+x+y},\qquad
\dot y=y\left(-\mu+\frac{bx}{1+x+y}\right),\quad x,y\geq0.
\]
Here \(x\) and \(y\) are total prey and predator abundances, \(a\) is the successful-predation coefficient, \(b\) is the handling-mediated predator recruitment coefficient and \(\mu\) is predator mortality. Set \(\lambda=b/\mu-1\) and \(\lambda_c=2(\sqrt2-1)\).

**Sharp classification.** If \(0<\lambda<1\), there are two strictly positive coexistence equilibria precisely when
\[
\lambda_c<\lambda<1,\qquad
0<a<a_f(\lambda):=\frac{1+\lambda}{\lambda^2}\left(\lambda-2\sqrt{1-\lambda}\right).
\]
The lower-predator equilibrium is a hyperbolic saddle, and the upper-predator equilibrium is a locally asymptotically stable sink. The prey-only equilibrium \((1,0)\) is also a sink: coexistence therefore persists below the predator's linear invasion threshold. At \(a=a_f(\lambda)\) within this range, the two coexistence equilibria merge in a nondegenerate saddle-node; for other \(a>0\) and \(0<\lambda<1\) there are no positive equilibria. If \(\lambda=1\), exactly one positive coexistence equilibrium exists for \(0<a<2\), and none for \(a\geq2\). If \(\lambda>1\), exactly one positive coexistence equilibrium exists for every \(a>0\). If \(\lambda\leq0\), none exists. These statements give the complete positive-equilibrium count for all positive parameters.

**Exact bistability witness.** With \((a,b,\mu)=(38/81,19,10)\), all three equilibria
\[
(1,0),\quad (4/3,1/5),\quad (5/3,1/2)
\]
are exact. The first and third are sinks; the second is a saddle. This is a genuinely open parameter phenomenon, not merely a nonhyperbolic equality example.

## Assumptions and scope

The source's equations (41) and (43) for total densities \(m_X,m_Y\) define the macroscopic reaction terms. Assume \(\alpha_P=\alpha_R=K_P=K_R=1\), \(\beta=\delta=1\), and write \(c_{SP}^{H}=a\), \(c_{HE}^{HS}=b\), with predator natural mortality \(\mu\). All are strictly positive. Taking spatially constant states eliminates the divergence terms independently of the positive diffusion matrices. The claim is about the resulting autonomous two-dimensional ODE, including its spatially homogeneous equilibria, not about arbitrary spatially heterogeneous solutions or full-PDE stability.

The invasion exponent of predators at the prey-only state \((1,0)\) is \(b/2-\mu=\mu(\lambda-1)/2\). Hence the two-equilibrium wedge lies strictly below the usual linear-invasion boundary \(b=2\mu\). The nonlinear additional prey capacity follows from active and refuge fractions \(x/(1+y)\) and \(xy/(1+y)\), rather than from an externally assigned varying carrying capacity.

## Proof

**1. Exhaustive algebraic reduction.** For \(y>0\), the predator equation demands \(b x/(1+x+y)=\mu\), which is impossible if \(b\leq\mu\). Otherwise \(\lambda>0\) and this equality is equivalent to
\[
x=\frac{1+y}{\lambda}.
\]
Along this exact predator nullcline the prey equation reduces, with no omitted roots or denominator singularities, to
\[
\dot x\big|_{x=(1+y)/\lambda}=-\frac{P(y)}{\lambda^2},\quad
P(y)=y^2-B y+1-\lambda,\quad
B=\lambda-\frac{a\lambda^2}{1+\lambda}.
\]
Thus positive coexistence equilibria are in one-to-one correspondence with positive roots of the quadratic \(P\), with prey coordinate \((1+y)/\lambda\).

**2. Exact root count.** If \(\lambda>1\), the constant coefficient \(1-\lambda\) is negative, so precisely one root is positive. If \(\lambda=1\), the roots are zero and \(1-a/2\), giving the stated boundary count. For \(0<\lambda<1\), both roots are positive and distinct if and only if \(B>2\sqrt{1-\lambda}\), and coincide in one positive double root if and only if equality holds. Because \(B<\lambda\) for \(a>0\), equality or strict inequality is possible only when \(\lambda>2\sqrt{1-\lambda}\), equivalently \(\lambda>2(\sqrt2-1)\). Solving the discriminant equality for \(a\) yields the stated \(a_f(\lambda)\). At the fold \(y_f=\sqrt{1-\lambda}>0\), while elsewhere in \(0<\lambda<1\) no admissible positive root exists.

**3. Hyperbolicity and stability inside the wedge.** Let \(J\) denote the two-dimensional reaction Jacobian. At any positive equilibrium with \(0<\lambda<1\), differentiation along the exact predator nullcline gives
\[
\det J=\frac{\mu y}{(1+\lambda)(1+y)}P'(y).
\]
The lower root has \(P'(y_-)<0\), hence is a hyperbolic saddle. The upper root has \(P'(y_+)>0\), hence positive determinant. Furthermore, using the equilibrium identity to remove \(a\) gives
\[
J_{11}=-\frac{\lambda y^2-\lambda y+2y^2+2}{\lambda(1+\lambda)(1+y)},\qquad
J_{22}=-\frac{\mu\lambda y}{(1+\lambda)(1+y)}.
\]
Each positive root satisfies \(0<y<B<\lambda<1\). Thus \(\lambda y^2-\lambda y+2y^2+2>2-\lambda>0\); both diagonal entries are strictly negative. Hence the upper root has negative trace and positive determinant and is a hyperbolic sink. The Jacobian at \((1,0)\) is upper triangular with eigenvalues \(-1\) and \(\mu(\lambda-1)/2\), so it is another hyperbolic sink throughout the wedge.

**4. Nondegenerate saddle-node.** At \(a=a_f(\lambda)\) for fixed \(\lambda_c<\lambda<1\), the double root has \(P''(y_f)=2\) and \(\partial_a P(y_f)=\lambda^2 y_f/(1+\lambda)>0\). The predator-nullcline reduction is regular because \(\partial_x[\dot y/y]=b(1+y)/(1+x+y)^2>0\). The nonzero transverse Jacobian eigenvalue is the negative trace displayed above. These establish a generic one-parameter saddle-node with the two branches on the \(a<a_f\) side.

**5. Exact rational witness.** Substituting \(\lambda=9/10\) and \(a=38/81\) gives \(B=7/10\) and \(P(y)=(y-1/5)(y-1/2)\). At \((1,0)\), the trace and determinant are \(-3/2\) and \(1/2\). At \((4/3,1/5)\), they are \(-889/513\) and \(-5/19\). At \((5/3,1/2)\), they are \(-1265/513\) and \(10/19\). The three stability classifications follow exactly.

## Verification

Run `python checker.py` using Python 3's standard library. The program evaluates all three exact equilibria and their Jacobian invariants using rational arithmetic, verifies the polynomial reduction at 600 deterministic rational test points, and reports `PASS` when every assertion succeeds. These computations are supporting checks. The proof above, not finite sampling, establishes the full parameter ranges and the saddle-node classification.

## Relationship to prior work

Bisi, Bondesan, Groppi and Soresina [1] derive the prey-state-dependent carrying capacity and explicitly leave equilibria and stability of the macroscopic system for further investigation. The present result solves a sharp, biologically interpretable homogeneous-equilibrium problem for their newly derived reaction law, including a sub-invasion bistability wedge. It does not claim novelty for the generic phenomena of refuge-driven coexistence, saddle-nodes or bistability.

Conforto, Desvillettes and Soresina [2] analyze cross-diffusion with a Beddington–DeAngelis response but a prey growth term of prescribed logistic type, not the particular endogenous quadratic combination of separate active and hidden-state competition used here. Hanifah and Abadi [3] investigate a three-equation predator–prey model with independently evolving environmental carrying capacity and a fixed protection fraction; their displayed equations do not entail the two-state refuge-feedback polynomial \(P\). Desvillettes and Soresina [4] investigate related cross-diffusion and Turing patterns; the available abstract does not settle the present exact equilibrium classification. This last inaccessible full-text comparison remains a residual literature risk.

## Limitations

The claims concern spatially homogeneous equilibria and their stability against homogeneous perturbations only. Cross-diffusion may destabilize an ODE sink to spatial patterns; no such PDE mode classification, nonlinear global basin description or rigorous kinetic fast-reaction convergence is asserted. Parameters represent a mathematical model and the exact sample does not calibrate an empirical ecosystem. The general ecological mechanism of multiple stable states predates this calculation, and historical priority of the specific parameter classification still requires independent literature validation.

## References

[1] M. Bisi, A. Bondesan, M. Groppi and C. Soresina, *Mesoscopic derivation of predator-prey dynamics via diffusive fast-reaction asymptotics: cross-diffusion and fear effects*, arXiv:2611.14132v1 (first posted 2026-11-10). https://arxiv.org/abs/2611.14132

[2] F. Conforto, L. Desvillettes and C. Soresina, *About reaction-diffusion systems involving the Holling-type II and the Beddington-DeAngelis functional responses for predator-prey models*, arXiv:1712.10159v1 (2017). https://arxiv.org/html/1712.10159v1

[3] A. K. Hanifah and A. Abadi, *Efek Perlindungan Mangsa dan Daya Dukung Variabel pada Sistem Mangsa-Pemangsa dengan Fungsi Respon Beddington-DeAngelis*, Jambura Journal of Mathematics 6(1), 102–110 (2024). https://doi.org/10.37905/jjom.v6i1.24288

[4] L. Desvillettes and C. Soresina, *Non-triangular cross-diffusion systems with predator–prey reaction terms*, Ricerche di Matematica 68, 295–314 (2019). https://doi.org/10.1007/s11587-018-0403-y
