# Two exact resolution thresholds for four geometric Debye relaxations

## Finding

Fix a reference time \(\tau_0>0\), a component dielectric strength \(\Delta\varepsilon>0\), and a common adjacent time ratio \(r>1\). Four uncoupled Debye processes have times \(\tau_0r^{-3/2}\), \(\tau_0r^{-1/2}\), \(\tau_0r^{1/2}\), and \(\tau_0r^{3/2}\). Their positive-frequency loss is

\[
L_r(\omega)=\Delta\varepsilon\sum_{j\in\{-3,-1,1,3\}}\frac{\omega\tau_0r^{j/2}}{1+(\omega\tau_0r^{j/2})^2},\qquad \omega>0.
\]

Define the polynomials

\[
C(h)=h^3-11h^2+40h-52
\]

and

\[
T(h)=h^7-16h^6+75h^5-66h^4-393h^3-300h^2-35h-34.
\]

There is exactly one root \(h_1\in(5,6)\) of \(C\) with \(h_1>3\), and exactly one root \(h_2\in(9,10)\) of \(T\) with \(h_2>3\). Set

\[
r_j=\frac{h_j-1+\sqrt{(h_j-1)^2-4}}2\quad(j=1,2).
\]

The resulting thresholds are \(r_1\approx4.068825013808844\) and \(r_2\approx8.021044889128009\). The number of **strict local maxima** of \(L_r\) on the entire positive-frequency axis is exactly

\[
\begin{cases}
1,&1<r\le r_1,\\
2,&r_1<r\le r_2,\\
4,&r>r_2.
\end{cases}
\]

At \(r=r_1\), the unique central peak is quartically flat. At \(r=r_2\), two additional symmetric stationary shoulders are present but are not extrema. Away from the thresholds, all extrema are nondegenerate. No three-peak regime exists in this family.

More precisely, put \(h=r+1+r^{-1}\), \(p=(h-3)/4\), and

\[
Q_h(v)=(1-v)(v+h^2)^2+(h-2)(h^2-v)(v+1)^2.
\]

For every simple real root \(v>1/p\) of \(Q_h\), the noncentral stationary logarithmic frequencies are

\[
s=\pm\operatorname{arcosh}\sqrt{pv},\qquad s=\log(\omega\tau_0).
\]

For \(r_1<r<r_2\), the central frequency is a minimum and the single symmetric noncentral pair consists of maxima. For \(r>r_2\), the three positive stationary locations in increasing order are an inner maximum, an intervening minimum and an outer maximum, with a central minimum at \(s=0\). At large separation \(a=\log r\), the four maxima approach \(s=\pm a/2\) and \(s=\pm3a/2\), and the three minima approach \(s=0,\pm a\). Every minimum has asymptotic loss \(L_r\sim2\Delta\varepsilon/\sqrt r\), whereas every peak approaches \(\Delta\varepsilon/2\).

## Assumptions and scope

The response is the sum of exactly four **independent, linear, ideal Debye terms**, all with equal positive dielectric strength. The relaxation times are in a geometric progression with a fixed positive ratio greater than one. The loss is defined per positive angular frequency, and the number of maxima is counted with respect to frequency (equivalently to its increasing logarithm). No assumption about observation noise or instrumental resolution is made.

## Proof

Write \(a=\log r>0\) and \(s=\log(\omega\tau_0)\). Since \(e^x/(1+e^{2x})=1/(2\cosh x)\), the normalized loss is the even function

\[
F_r(s)=\frac{L_r(e^s/\tau_0)}{\Delta\varepsilon}
=\frac12\sum_{j\in\{-3,-1,1,3\}}\operatorname{sech}(s+ja/2).
\]

Let \(u=\cosh(a/2)\), \(z=\cosh s\ge1\), and \(h=4u^2-1=r+1+r^{-1}\). The identity

\[
\frac12\bigl(\operatorname{sech}(s-b)+\operatorname{sech}(s+b)\bigr)
=\frac{z\cosh b}{z^2+\sinh^2b}
\]

and the triple-angle relation \(\cosh(3a/2)=u(h-2)\) show that

\[
F_r(s)=u z\left(\frac1{z^2+p}+\frac{h-2}{z^2+ph^2}\right),
\qquad p=\sinh^2(a/2)=\frac{h-3}{4}>0.
\]

In particular, \(\sinh^2(3a/2)=ph^2\). Set \(v=z^2/p\). Direct differentiation gives

\[
\frac{dF_r}{ds}=
\frac{u\,p^3\,\sinh s}{(z^2+p)^2(z^2+ph^2)^2}\,Q_h(v).
\]

For \(s>0\), the prefactor is strictly positive and the physical domain is \(v>v_0=1/p=4/(h-3)\). The cubic \(Q_h\) has negative leading coefficient \(1-h\). Its discriminant factors **exactly** as

\[
\operatorname{disc}_v Q_h=(h-2)(h-1)^4(h+1)^2T(h),
\]

and the sign at the domain boundary is determined by

\[
Q_h(v_0)=\frac{(h-2)(h-1)(h+1)^2}{(h-3)^3}C(h).
\]

All factors displayed outside \(C\) and \(T\) are positive for \(h>3\). Substituting \(h=z_0+3\) into \(C\) gives \(z_0(z_0-1)^2-4\). It is strictly below zero for \(0<z_0\le1\) and strictly increases from \(-4\) to infinity for \(z_0>1\). Hence \(C\) has exactly one root \(h_1>3\), and the signs \(C(5)<0<C(6)\) locate it in \((5,6)\).

For the second polynomial,

\[
T(z_0+3)=z_0^7+5z_0^6-24z_0^5-156z_0^4-240z_0^3
-1488z_0^2-7424z_0-10048.
\]

Its nonzero coefficients have exactly one sign change in descending order. Descartes' rule, together with \(T(9)<0<T(10)\), shows that \(T\) has exactly one real root \(h_2>3\), lying in \((9,10)\). Thus \(3<h_1<h_2\), the cubic has one real simple root for \(3<h<h_2\), and three simple real roots for \(h>h_2\). At \(h=h_2\), its discriminant vanishes. This is a double root, not a triple one: the derivative cubic's quadratic discriminant is

\[
4(h-1)^2\bigl(h^4-9h^3+2h^2+27h+19\bigr)>0\qquad(h\ge9).
\]

For \(h<h_2\), the unique real cubic root is below \(v_0\) if \(h<h_1\), is exactly \(v_0\) if \(h=h_1\), and is above \(v_0\) if \(h_1<h<h_2\); this follows from \(Q_h(v_0)\)'s sign and the negative leading coefficient. For \(h>h_2\), **all three** roots lie above \(v_0\). To prove that last assertion without relying on a plotted root locus, observe that at the exact rational sample \(h=10\), the signs of \(Q_{10}\) at \(v=4/7,2,20,80\) alternate \(+,-,+,-\). Thus all three roots lie in \((4/7,2)\), \((2,20)\), and \((20,80)\), all above the physical lower boundary \(v_0=4/7\). The number of physical roots cannot change throughout the connected interval \(h>h_2\): the discriminant is nonzero and \(Q_h(v_0)\ne0\), so no root can collide or enter through the boundary. At \(h=h_2\), the limiting double root is also inside the physical domain.

The derivative signs now prove the peak count. For \(h<h_1\), the derivative is negative on \(s>0\), giving only the central maximum. At \(h=h_1\), the boundary root yields \(F_r'(s)\) proportional to a negative multiple of \(s^3\) near zero, hence a flat but strict central maximum. For \(h_1<h<h_2\), the derivative is first positive and then negative, giving one maximum on each side of a central minimum. At \(h=h_2\), the double root produces stationary nonextremal shoulders. For \(h>h_2\), the derivative alternates \(+,-,+,-\) as \(s>0\) crosses the three roots, giving two maxima and one additional minimum on each side, alongside the minimum at the origin. Strictness and nondegeneracy outside the critical values follow from simple roots and the nonzero boundary curvature.

Finally, as \(a\to\infty\), each of the four translates of \(\operatorname{sech}\) has one separated maximum near its own center. Near the midpoint between adjacent centers, the two neighboring exponential tails contribute \(2e^{-a/2}\cosh y\) in a local midpoint coordinate \(y\), while the other translates contribute smaller terms. This gives minima at \(s=0,\pm a+o(1)\) and loss \(2\Delta\varepsilon e^{-a/2}(1+o(1))\); peaks tend to \(\Delta\varepsilon/2\). No claim is made about an experimental finite-resolution threshold.

## Verification

Run `python verify.py` with Python 3, `sympy` and `mpmath` installed. The standalone checker validates the exact derivative numerator, two polynomial identities, discriminant, isolating brackets and rational witness signs; it also compares roots of the cubic with derivatives of the original four-term physical loss over representative ratios, and checks the high-separation asymptotics. The current checker reports `VERIFY_OK checks=81`, \(r_1\approx4.068825013808844\), and \(r_2\approx8.021044889128009\). Those tests supplement, rather than replace, the parameter-uniform proof above.

## Relationship to prior work

Standard dielectric response theory allows sums or distributions of Debye relaxation processes. Ribeiro and Vieira (2003) discuss the phenomenological sum model and its limitations, including omitted interactions between relaxors. Dean, Démery, Parsegian and Podgornik (2012) explicitly formulate finite sums of Debye terms and study a distinct thermal-force relaxation observable; Jakobsen, Maggi, Christensen and Dyre (2008) investigate experimentally overlapping dielectric and shear-mechanical relaxations. Clegg and Robinson (2012) study fitting multipole Debye models. These establish physical motivation and the underlying constitutive law, not the two exact algebraic resolution thresholds proved here in the material examined. A three-process symmetric geometric model has a different single-threshold stationary equation; the four-process theorem here has an additional noncentral saddle-node transition, including a genuine two-peak window. A broader unexamined specialist treatment might still contain the result.

## Limitations

The result is a theorem for an ideal four-component response with equal amplitudes and equal logarithmic spacing, not for arbitrary multipole fits, component coupling, fractional/non-Debye lineshapes, temperature-dependent strengths, experimental noise, or instrumental peak-resolving capability. The detailed historical-priority assessment remains provisional.

## References

- J. L. Ribeiro and L. G. Vieira, *The factorized form for dielectric relaxation* (first published online 2003-11-19), https://doi.org/10.1140/epjb/e2003-00313-2.
- B. Jakobsen, C. Maggi, T. Christensen and J. C. Dyre, *Investigation of the shear-mechanical and dielectric relaxation processes in two mono-alcohols close to the glass transition* (first public arXiv version, 2008-05-29), https://arxiv.org/abs/0805.4519.
- D. S. Dean, V. Démery, V. A. Parsegian and R. Podgornik, *Out of equilibrium thermal Casimir effect in a model polarizable material* (first public arXiv version, 2012-01-02), https://arxiv.org/abs/1201.0547.
- J. Clegg and M. P. Robinson, *A genetic algorithm for optimizing multi-pole Debye models of tissue dielectric properties* (2012), https://pubmed.ncbi.nlm.nih.gov/22975629/.
