# Exact three-phase two-cycle census in an axially symmetric quadratic diffeomorphism

## Finding
Let the quadratic polynomial diffeomorphism of \(\mathbb R^3\) be
\[
T(x,y,z)=\bigl(y,\;\nu_1x+\nu_2y+yz,\;\nu_3z-y^2\bigr),
\]
with \(\nu_1<1\), \(\nu_1\ne0\), \(0<\nu_3<1\), and unrestricted \(\nu_2\in\mathbb R\). Set \(c=1-\nu_1>0\) and
\[
\nu_2^{\mathrm{sb}}=\frac{2c\nu_3}{1-\nu_3}.
\]
The number \(N_2\) of *distinct primitive period-two orbits* in the whole real phase space (orbits, not points) is exactly
\[
N_2=\begin{cases}
0,&\nu_2\le -c,\\
1,&-c<\nu_2\le\nu_2^{\mathrm{sb}},\\
3,&\nu_2>\nu_2^{\mathrm{sb}}.
\end{cases}
\]
The single orbit present for \(\nu_2>-c\) is invariant as an orbit under the axial symmetry \((x,y,z)\mapsto(-x,-y,z)\). At \(\nu_2^{\mathrm{sb}}\), exactly two additional symmetry-exchanged period-two orbits appear; at equality they coincide with the original orbit and hence do not add to the count. On either new orbit, if \((a,b)\) are the first two coordinates at a point, then the *exact symmetry-breaking amplitude* obeys
\[
(a+b)^2=\frac{1-\nu_3^2}{\nu_3}\bigl(\nu_2-\nu_2^{\mathrm{sb}}\bigr).
\]
The fixed-point symmetry-breaking threshold, already present in the source bifurcation picture, is \(\nu_2=c\). It precedes, coincides with, or follows the new primitive-two threshold precisely when \(\nu_3>1/3\), \(\nu_3=1/3\), or \(\nu_3<1/3\), respectively. In particular, when \(0<\nu_3<1/3\) and \(\nu_2^{\mathrm{sb}}<\nu_2\le c\), all three primitive two-cycles coexist with only the origin as a fixed point.

## Assumptions and scope
All variables and parameters are real. A primitive two-cycle is a set \(\{P,T(P)\}\) with \(T^2(P)=P\) and \(T(P)\ne P\); two choices of starting point on one orbit count once. The restrictions \(\nu_1\ne0\) and \(\nu_3>0\) keep the Jacobian \(-\nu_1\nu_3\) nonzero. The ranges of \(\nu_1\), \(\nu_2\), and \(\nu_3\) are exactly those above, with no bounded-domain or genericity exclusions.

For \(\nu_2>-c\), choose \(a>0\) with \(a^2=(1-\nu_3)(c+\nu_2)\). The original primitive two-cycle is
\[
\bigl\{(a,-a,-c-\nu_2),(-a,a,-c-\nu_2)\bigr\}.
\]
For \(\nu_2>\nu_2^{\mathrm{sb}}\), let
\[
S=\frac{(1-\nu_3^2)\nu_2}{\nu_3},\quad D=c(1+\nu_3),\quad
r_\pm=\frac{S\pm\sqrt{S^2-4D^2}}2.
\]
Both \(r_\pm\) are positive and unequal. Two further primitive two-cycles are obtained from \((a,b)=(\sqrt{r_+},-D/\sqrt{r_+})\) and its axial reflection \((-a,-b)\). For either choice, define
\[
z=-\frac{a^2+\nu_3b^2}{1-\nu_3^2},\qquad
w=-\frac{b^2+\nu_3a^2}{1-\nu_3^2}.
\]
Then the corresponding cycle is precisely \(\{(a,b,z),(b,a,w)\}\).

## Proof
Any point of a two-cycle must have successive first two coordinates \((a,b)\) and \((b,a)\), because the first coordinate of \(T\) is its previous second coordinate. If the third coordinates are \(z,w\), the two-cycle equations reduce exactly to
\[
ca=b(\nu_2+z),\quad cb=a(\nu_2+w),\quad
w=\nu_3z-b^2,\quad z=\nu_3w-a^2.
\]
Since \(0<\nu_3<1\), the final two equations uniquely give the values of \(z,w\) stated above. Subtracting the first equation multiplied by \(a\) from the second multiplied by \(b\), or directly rearranging, yields
\[
(a^2-b^2)\left(c+\frac{ab}{1+\nu_3}\right)=0.
\]
This factorization exhausts *all* real solutions, including the axes and collision cases.

In the first case, \(a^2=b^2\). If \(a=b\), the solved third-coordinate equations imply \(z=w\), so the point is fixed rather than primitive two-periodic. If \(a=-b\), \(a\ne0\), the equations give \(a^2=(1-\nu_3)(c+\nu_2)\). Thus exactly one primitive two-cycle in this case exists if and only if \(\nu_2>-c\). At equality it collapses to the fixed origin.

In the remaining case, \(ab=-c(1+\nu_3)=-D\). The first two equations, after division by nonzero \(a,b\) and addition, give
\[
a^2+b^2=\frac{(1-\nu_3^2)\nu_2}{\nu_3}=S.
\]
The two positive squares \(a^2,b^2\) must be roots of \(u^2-Su+D^2=0\). Existence requires \(S\ge2D\), i.e. \(\nu_2\ge \nu_2^{\mathrm{sb}}\). If equality holds, \(a^2=b^2=D\), and \(ab=-D\) forces \(a=-b\), yielding the *already counted* antisymmetric cycle. When the inequality is strict, \(r_+\ne r_-\), yielding the two stated cycles: the sign of \(a\) determines one of two axial-reflection partners, while exchanging \(a\) with \(b\) merely rotates a cycle in time. Because \(ab<0\) and \(a^2\ne b^2\), neither new cycle is fixed or coincides with the other or with the antisymmetric cycle. The formulas solve every original equation, so there are exactly two additional cycles, and the enumeration is exhaustive.

On the latter branch, \((a+b)^2=S+2ab=S-2D\), which is the claimed exact square-root onset. Finally, the source fixed-point threshold is also obtained directly from \(a=b\): nonzero fixed points satisfy \(a^2=(1-\nu_3)(\nu_2-c)\), so exist exactly if \(\nu_2>c\). The difference between thresholds is
\[
\nu_2^{\mathrm{sb}}-c=\frac{c(3\nu_3-1)}{1-\nu_3},
\]
proving the ordering assertion.

## Verification
The accompanying standalone `verify.py` checks the exact factorization, the threshold and amplitude identities, the fixed and antipodal branches, two exact rational three-orbit witnesses, and the equality case using SymPy. At \((\nu_1,\nu_3,\nu_2)=(1/2,1/2,25/24)\), the non-antipodal two-cycle point with first two coordinates \((1,-3/4)\) has third coordinate \(-41/24\), and its image has coordinates \((-3/4,1,-17/12)\); the reflected pair gives the other new cycle. Here \(\nu_2^{\mathrm{sb}}=1\), so this is strictly beyond the sharp threshold. A second rational witness, \((\nu_1,\nu_3,\nu_2)=(-1/2,1/4,61/60)\), has an off-antipodal cycle through \((3/2,-5/4,-169/60)\) and its axial reflection; since \(1<61/60<3/2=c\), the origin is the *only* fixed point while all three primitive two-cycles exist. Symbolic proof, not sampling, establishes the universal count.

To reproduce from the supplied package, run `python verify.py` with a Python 3 environment containing `sympy`. The expected terminal line is `ALL_CHECKS_PASSED`.

## Relationship to prior work
The quadratic map and axial symmetry are from Gonchenko and Gonchenko's 2023 study, with extended normal-form and bifurcation discussion in their 2024 paper. In particular, their period-doubling and fixed-point pitchfork descriptions are prior work, as is the fixed-point threshold \(\nu_2=c\). The contribution here is the exhaustive *global real* prime-two census, the distinct second symmetry-breaking threshold \(\nu_2^{\mathrm{sb}}\), the exact two-orbit onset, and the exchange of ordering at \(\nu_3=1/3\). General periodic-orbit analyses of other quadratic maps do not imply the parameter inequalities for this particular three-dimensional normal form.

## Limitations
The classification is for \(T_-\) on \(\nu_1<1\), \(\nu_1\ne0\), \(0<\nu_3<1\), with no assertion for the excluded boundary values, negative \(\nu_3\), higher periods, basins, or periodic-orbit stability. It does not claim classification of chaotic attractors. The original 2023 paper was available for abstract-level comparison but not complete primary-text comparison; publication priority therefore retains that stated uncertainty. The 2024 follow-up was compared via extensive accessible indexed sections, not an independently downloaded complete PDF. Independent audit has not been performed.

## References
- Sergey Gonchenko and Aleksandr Gonchenko, *On discrete Lorenz-like attractors in three-dimensional maps with axial symmetry*, Chaos **33** (2023), 123104, DOI: 10.1063/5.0172243. Public online date observed: 2023-12-04.
- Sergey Gonchenko and Aleksandr Gonchenko, *Discrete Lorenz attractors of new types in three-dimensional maps with axial symmetry*, Partial Differential Equations in Applied Mathematics **11** (2024), 100904, DOI: 10.1016/j.padiff.2024.100904 (open access).
