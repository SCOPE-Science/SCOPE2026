# Nested escape-time ellipses and a neutral-to-damped survival-area crossover in a rigid cubic flow

## Finding

Consider the planar cubic vector field
\[
\dot x=-y+x(y^2-\kappa),\qquad
\dot y=x+y(y^2-\kappa),\qquad \kappa\geq0.
\]
For each initial state \(z=(x_0,y_0)\), let \(\tau_\kappa(z)\in(0,\infty]\) be its maximal forward existence time; set \(\tau_\kappa(0)=\infty\). For \(t>0\), define the symmetric matrix
\[
Q_{\kappa,t}=2\int_0^t e^{-2\kappa s}
\begin{pmatrix}\sin^2s&\sin s\cos s\\\sin s\cos s&\cos^2s\end{pmatrix}ds.
\]
Every matrix \(Q_{\kappa,t}\) is positive definite. For every nonzero \(z\),
\[
\tau_\kappa(z)>t\quad\Longleftrightarrow\quad z^\mathsf{T}Q_{\kappa,t}z<1.
\]
Consequently the complete finite-horizon survival region is an open ellipse. In particular, write \(A_\kappa(t)\) for its Euclidean area. When \(\kappa>0\), put \(q=e^{-2\kappa t}\). Then
\[
\boxed{A_\kappa(t)=\frac{2\pi\kappa\sqrt{1+\kappa^2}}
{\sqrt{(1-q)^2-4\kappa^2q\sin^2t}}.}
\]
At \(\kappa=0\) its continuous extension is
\[
\boxed{A_0(t)=\frac{\pi}{\sqrt{t^2-\sin^2t}}.}
\]
For \(\kappa>0\), the set of initial states with infinite forward existence is a closed ellipse of area
\[
A_\kappa(\infty)=2\pi\kappa\sqrt{1+\kappa^2};
\]
its boundary is the repelling periodic orbit and its interior converges to the origin. For \(\kappa=0\), only the origin has infinite forward existence. Thus the exact finite-escape survival area
\[
S_\kappa(t)=\operatorname{Leb}_2\{z:t<\tau_\kappa(z)<\infty\}
\]
is \(A_\kappa(t)-A_\kappa(\infty)\) for \(\kappa>0\), and \(A_0(t)\) for \(\kappa=0\).

These exact formulas have a sharp three-regime consequence:
\[
\begin{aligned}
S_0(t)&=\frac{\pi}{t}+O(t^{-3})&& (t\to\infty),\\
S_\kappa(t)&=2\pi\kappa\sqrt{1+\kappa^2}\,e^{-2\kappa t}
 \bigl(1+2\kappa^2\sin^2t+O_\kappa(e^{-2\kappa t})\bigr)
 && (t\to\infty,\ \kappa>0),\\
\frac{S_\kappa(u/\kappa)}{\kappa}&\longrightarrow\frac{2\pi}{e^{2u}-1}
 &&(\kappa\downarrow0,\ u>0).
\end{aligned}
\]
The last limit is uniform when \(u\) ranges over any compact subset of \((0,\infty)\). For every fixed \(\kappa>0\), the normalized exponential survival area has distinct sharp limits:
\[
\liminf_{t\to\infty}e^{2\kappa t}S_\kappa(t)=2\pi\kappa\sqrt{1+\kappa^2},\qquad
\limsup_{t\to\infty}e^{2\kappa t}S_\kappa(t)=2\pi\kappa\sqrt{1+\kappa^2}(1+2\kappa^2).
\]
For every fixed \(\kappa\geq0\), the short-horizon area has the universal leading law
\[
A_\kappa(t)=\pi\sqrt3\,t^{-2}\bigl(1+\kappa t+O_\kappa(t^2)\bigr)
\qquad(t\downarrow0).
\]
The result is about maximal **original-physical-time existence**, not a Poincaré-compactified or rescaled time.

## Assumptions and scope

The equations are considered on the full real plane and \(\kappa\) is real and nonnegative. Every initial condition gives a unique local classical solution because the vector field is polynomial. \(\tau_\kappa(z)\) denotes the supremum of its original-time forward existence interval. \(\operatorname{Leb}_2\) means ordinary two-dimensional Euclidean Lebesgue measure, not an invariant probability. Area statements treat ellipse boundaries as measure-zero sets. The two-parameter crossover holds with \(u=\kappa t>0\) fixed while \(\kappa\) tends to zero; it is not a claim of uniformity down to \(u=0\).

## Proof

**1. Reciprocal-square dynamics and the exact survival set.** For a nonzero solution, continuous polar coordinates \(x=r\cos\theta\), \(y=r\sin\theta\) give
\[
\dot\theta=1,\qquad \dot r=-\kappa r+r^3\sin^2\theta.
\]
The reciprocal squared radius \(w=r^{-2}\) therefore obeys
\[
\dot w=2\kappa w-2\sin^2(\theta_0+t).
\]
Writing \(z=(x_0,y_0)\) and \(r_0=\lVert z\rVert\), direct integration yields, throughout the maximal forward interval,
\[
w(t)=\frac{e^{2\kappa t}}{r_0^2}
\left(1-2\int_0^t e^{-2\kappa s}(x_0\sin s+y_0\cos s)^2ds\right)
=\frac{e^{2\kappa t}}{r_0^2}(1-z^\mathsf{T}Q_{\kappa,t}z).
\]
In particular
\[
r(t)=\frac{r_0e^{-\kappa t}}{\sqrt{1-z^\mathsf{T}Q_{\kappa,t}z}}.
\]
For every nonzero \(z\), the quadratic form \(z^\mathsf{T}Q_{\kappa,t}z\) is strictly increasing as a function of \(t>0\): its derivative is nonnegative, and it cannot vanish identically on any nonempty time interval because \(x_0\sin s+y_0\cos s\) is not identically zero. It starts at zero. It follows that the first equality to one is the exact finite blow-up time, with radius tending to infinity as that time is approached; if equality never occurs, the trajectory exists for all forward times. The case \(z=0\) is stationary. This proves the survival equivalence. For fixed \(t>0\), the vectors \((\sin s,\cos s)\), as \(s\) runs through \((0,t)\), span the plane, so \(Q_{\kappa,t}\) is positive definite and the survival set is a bounded open ellipse.

**2. Gram determinant and exact ellipse area.** Define
\[
D=\int_0^t e^{-2\kappa s}ds,\quad
C=\int_0^t e^{-2\kappa s}\cos(2s)ds,\quad
H=\int_0^t e^{-2\kappa s}\sin(2s)ds.
\]
Then
\[
Q_{\kappa,t}=\begin{pmatrix}D-C&H\\H&D+C\end{pmatrix},\qquad
\det Q_{\kappa,t}=D^2-C^2-H^2.
\]
For \(\kappa>0\), setting \(q=e^{-2\kappa t}\),
\[
D=\frac{1-q}{2\kappa},\qquad
C+iH=\frac{1-qe^{2it}}{2(\kappa-i)}.
\]
Taking the squared complex modulus gives
\[
\det Q_{\kappa,t}=
\frac{(1-q)^2-4\kappa^2q\sin^2t}{4\kappa^2(1+\kappa^2)}.
\]
For \(\kappa=0\), \(D=t\), \(C=\sin(2t)/2\), \(H=(1-\cos(2t))/2\), hence \(\det Q_{0,t}=t^2-\sin^2t>0\) for all \(t>0\). The Euclidean area of \(\{z:z^\mathsf{T}Qz<1\}\) is \(\pi/\sqrt{\det Q}\), proving both exact formulas.

**3. Infinite-lifetime states and subtraction of the nonescaping area.** For \(\kappa>0\), the Gram matrices increase to the finite positive-definite matrix
\[
Q_{\kappa,\infty}=2\int_0^\infty e^{-2\kappa s}
\begin{pmatrix}\sin^2s&\sin s\cos s\\\sin s\cos s&\cos^2s\end{pmatrix}ds,
\qquad \det Q_{\kappa,\infty}=\frac{1}{4\kappa^2(1+\kappa^2)}.
\]
Consequently infinite existence is equivalent to \(z^\mathsf{T}Q_{\kappa,\infty}z\leq1\). The interior has \(w(t)\) bounded below by a positive multiple of \(e^{2\kappa t}\) and tends to the origin. On the boundary, periodicity of the remaining tail integral shows the radius is a positive \(\pi\)-periodic function of the angle; with \(\dot\theta=1\) this is a nonconstant-state periodic orbit of period \(2\pi\), separating the interior from finite-time escape. It is repelling since the radial reciprocal-square difference from its periodic solution grows as \(e^{2\kappa t}\). The limiting ellipse area is the displayed \(2\pi\kappa\sqrt{1+\kappa^2}\). When \(\kappa=0\), the Gram quadratic form diverges for every nonzero \(z\) as \(t\to\infty\), and all such initial data blow up. Removing the infinite-existence ellipse from each finite-time ellipse proves the stated exact formula for \(S_\kappa(t)\).

**4. Asymptotic and crossover analysis.** At \(\kappa=0\), expand
\(A_0(t)=\pi t^{-1}(1-\sin^2t/t^2)^{-1/2}\) as \(t\to\infty\). For fixed \(\kappa>0\), set \(B(t)=1+2\kappa^2\sin^2t\); the area formula becomes
\[
A_\kappa(t)=A_\kappa(\infty)
\bigl(1-2e^{-2\kappa t}B(t)+e^{-4\kappa t}\bigr)^{-1/2}.
\]
The Taylor expansion \((1+h)^{-1/2}=1-h/2+O(h^2)\), uniform because \(B(t)\) is bounded, produces the oscillatory exponential term. The extremal subsequences \(t=j\pi\) and \(t=(j+1/2)\pi\) give the sharp liminf and limsup. For the crossover, replace \(t\) by \(u/\kappa\) and divide \(S_\kappa\) by \(\kappa\):
\[
\frac{S_\kappa(u/\kappa)}{\kappa}=
2\pi\sqrt{1+\kappa^2}\left[
\frac{1}{\sqrt{(1-e^{-2u})^2-4\kappa^2e^{-2u}\sin^2(u/\kappa)}}-1\right].
\]
On compact positive \(u\)-intervals the squared-sine term is uniformly \(O(\kappa^2)\) and \(1-e^{-2u}\) stays bounded away from zero, yielding the stated uniform limit. Finally, direct Taylor integration of the entries of \(Q_{\kappa,t}\) gives \(\det Q_{\kappa,t}=(t^4/3)(1-2\kappa t+O_\kappa(t^2))\) as \(t\downarrow0\); its inverse square root gives the short-horizon law.

## Verification

The accompanying standalone script `check_lifetime.py` evaluates the quadratic Gram entries both by elementary trigonometric-exponential formulas and by independent Simpson quadrature, verifies their determinants and ellipse areas at several parameters, and checks the small-time, large-time and crossover limits numerically. These finite diagnostics test the algebra only: the infinite-time and all-initial-data statements rest on the analytic proof above. Run `python3 check_lifetime.py` from the extracted directory with the Python standard library.

## Relationship to prior work

Llibre's 2024 paper and its July 24, 2024 preprint study the rigid homogeneous family, include exactly this \(P(x,y)=y^2\) cubic system and establish a general explicit polar initial-value formula, which is **used rather than claimed anew here**. Gasull and Torregrosa's 2004/2005 rigid-system existence theorem and Gasull--Prohens--Torregrosa's 2005 cubic classification also concern periodic orbits and phase portraits. Neither of the inspected scientific statements supplies an exact two-dimensional area of initial states remaining finite through an arbitrary physical horizon, its oscillatory exponential factor, or the neutral-damping crossover. Those are the novel quantitative observables claimed here, despite their having a derivation from the established radial representation. Related recent exact escape-area laws for different dynamical systems do not imply these formulas for this vector field.

## Limitations

The theorem makes no claim about random invariant measures, parameter perturbations that change the polynomial's homogeneous form, negative \(\kappa\), or numerical stability of discretizations. This is a rigorous special-family space-time area identity; general rigid systems need not have elliptical lifetime levels. The original source's explicit formula is prior art, and the novelty assessment is confined to the new area/crossover observable, not to the solvability of the differential equation. The possibility of a separate prior treatment of the same area observable outside inspected sources remains a publication-priority risk. Independent validation has not been performed.

## References

1. J. Llibre, *Rigid Polynomial Differential Systems with Homogeneous Nonlinearities*, Preprints.org, first public version posted 2024-07-24, DOI: 10.20944/preprints202407.1946.v1; peer-reviewed version in *Mathematics* **12** (2024), 2806, DOI: 10.3390/math12182806. The model, published polar reduction, and Proposition 5 were inspected.
2. A. Gasull and J. Torregrosa, *Exact number of limit cycles for a family of rigid systems*, *Proc. Amer. Math. Soc.* **133** (2005), 751–758, electronically published 2004-10-07, DOI: 10.1090/S0002-9939-04-07542-2.
3. A. Gasull, R. Prohens, and J. Torregrosa, *Limit cycles for rigid cubic systems*, *J. Math. Anal. Appl.* **303** (2005), 391–404, DOI: 10.1016/j.jmaa.2004.07.030.
