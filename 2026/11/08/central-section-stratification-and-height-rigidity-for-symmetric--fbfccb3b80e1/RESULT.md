# Central-section stratification and height rigidity for symmetric polygonal prisms

## Finding
Let \(B\subset\mathbb R^2\) be a fixed nondegenerate centrally symmetric convex polygon, centered at the origin, with exactly \(2m\ge6\) genuine vertices \(\pm v_1,\ldots,\pm v_m\). For \(h>0\), form the right prism \(K_h=B\times[-h,h]\). If \(U\) is uniform on the unit sphere, let \(N_h(U)\) be the number of sides of the polygon \(K_h\cap U^\perp\). All assertions concerning \(U\) hold outside a set of spherical area zero.

For \(w_\phi=(\cos\phi,\sin\phi)\), order the \(m\) numbers \(\rho_i(\phi)=|\langle v_i,w_\phi\rangle|\) as \(\rho_{(1)}(\phi)\le\cdots\le\rho_{(m)}(\phi)\), and put \(\rho_{(0)}=0\). Define \(F_h(r)=r/\sqrt{h^2+r^2}\) for \(r\ge0\). Then for every \(j=0,\ldots,m-1\), the probability contribution to the side count \(4+2j\) is exactly
\[
\frac1{2\pi}\int_0^{2\pi}\bigl[F_h(\rho_{(j+1)}(\phi))-F_h(\rho_{(j)}(\phi))\bigr] \,d\phi.
\]
There is one additional contribution to side count \(2m\), equal to
\[
\frac1{2\pi}\int_0^{2\pi}\bigl[1-F_h(\rho_{(m)}(\phi))\bigr] \,d\phi.
\]
In particular, \(N_h\) has no other positive-probability values. For **every** fixed such base \(B\), the quadrilateral probability
\[
P_4(B,h)=\frac1{2\pi}\int_0^{2\pi}\frac{\rho_{(1)}(\phi)}{\sqrt{h^2+\rho_{(1)}(\phi)^2}}\,d\phi
\]
is a strictly decreasing continuous bijection from \((0,\infty)\) onto \((0,1)\). Thus one central-section side-count probability determines the prism's height when its base is known.

For the regular hexagon of circumradius \(1\), write \(a=\sqrt{1+h^2}\). The **complete elementary law** reduces to
\[
\begin{aligned}
P_4(h)&=\frac6\pi\left[\arcsin\frac1a-\arcsin\frac{\sqrt3}{2a}\right],\\
P_8(h)&=\frac6\pi\left[2\arcsin\frac1{2a}-\arcsin\frac{\sqrt3}{2a}\right],\\
P_6(h)&=1-P_4(h)-P_8(h).
\end{aligned}
\]
In particular \(P_4\) recovers the aspect ratio explicitly: with \(\delta=\pi P_4(h)/6\in(0,\pi/6)\),
\[
h=\frac{\cos\delta-\sqrt3/2}{\sin\delta}.
\]
Moreover \(P_8(h)\) is uniquely maximized at \(h=\sqrt5/2\), and its sharp maximum is
\[
\max_{h>0}P_8(h)=\frac6\pi\left[2\arcsin\frac13-\arcsin\frac1{\sqrt3}\right]\approx0.122601719540891.
\]
For the uniform (all edges equal) regular hexagonal prism \(h=1/2\), the respective \((4,6,8)\)-side probabilities are approximately \((0.422215643550476,0.499063595191250,0.078720761258275)\).

## Assumptions and scope
The base polygon has \(2m\) distinct genuine vertices, no three consecutive collinear, positive area, and a center of symmetry at the origin; the half-height \(h\) is strictly positive. The normal is sampled with normalized rotation-invariant area on \(S^2\); \(U\) and \(-U\) give the same unoriented central plane. A plane through a vertex or edge is excluded only because it belongs to a measure-zero exceptional set. The base is held fixed, including its scale, in the height-recovery statement. No offset planes or alternative stereological sampling distributions are considered.

## Proof
**Sign changes and side counts.** Fix a generic direction \(U=(U_x,U_y,U_z)\) and let \(w=(U_x,U_y)/\sqrt{U_x^2+U_y^2}\) and \(t=h|U_z|/\sqrt{U_x^2+U_y^2}\). A vertical edge over a base vertex \(v\) crosses the central plane exactly when \(|\langle v,w\rangle|<t\). The vertices occur in \(m\) antipodal pairs, so there are exactly \(2j\) crossing vertical edges when \(t\) lies strictly between the \(j\)-th and \((j+1)\)-st ordered \(\rho\)-values, with \(\rho_{(0)}=0\).

The maximum of \(\langle v,w\rangle\) on \(B\) is \(\rho_{(m)}\) and its minimum is \(-\rho_{(m)}\). For \(0<t<\rho_{(m)}\), each of the two horizontal base faces is cut along a nondegenerate chord, crossing exactly two of its edges. Thus the section has \(4+2j\) sides. If \(t>\rho_{(m)}\), neither horizontal face is crossed, all \(2m\) vertical edges are crossed, and the section has \(2m\) sides. Since each generic edge crossing corresponds to exactly one section vertex, this gives the asserted deterministic side-count rule.

**Direction distribution.** The azimuth \(\phi\) of \((U_x,U_y)\) is uniform on \([0,2\pi)\), independent of \(|U_z|\), which is uniform on \([0,1]\). Hence
\[
\Pr(t<r\mid\phi)=\Pr\left(\frac{h|U_z|}{\sqrt{1-U_z^2}}<r\right)=\frac r{\sqrt{h^2+r^2}}=F_h(r).
\]
Taking the conditional probabilities of successive \(\rho\)-intervals proves the complete integral law, including the extra terminal interval.

**Height rigidity.** For \(m\ge3\), the terminal interval has side count \(2m\ge6\), and no other interval except \(j=0\) has four sides. Thus \(P_4(B,h)\) is exactly the stated integral. The smallest \(\rho\)-value is positive except at finitely many azimuths (one perpendicular direction pair for each vertex pair). For almost every \(\phi\), its integrand is continuous and strictly decreasing in \(h\), converging to \(1\) as \(h\downarrow0\) and to \(0\) as \(h\to\infty\). Dominated convergence proves the asserted strict continuous bijection.

**Regular hexagon.** Symmetry reduces the azimuth to \(0\le\phi\le\pi/6\) with density \(6/\pi\). On this interval the ordered projections are
\[
\rho_{(1)}=\cos(\pi/3+\phi),\quad \rho_{(2)}=\cos(\pi/3-\phi),\quad\rho_{(3)}=\cos\phi.
\]
Therefore \(P_4\) is the average of \(F_h(\rho_{(1)})\) and \(P_8\) is the average of \(F_h(\rho_{(3)})-F_h(\rho_{(2)})\). The identity
\[
\int\frac{\cos\alpha}{\sqrt{h^2+\cos^2\alpha}}\,d\alpha
=\arcsin\frac{\sin\alpha}{\sqrt{1+h^2}}+C
\]
yields the three displayed formulas. The inverse relation follows by writing \(\delta=\arcsin(1/a)-\arcsin(\sqrt3/(2a))\), taking sines, and solving for \(h>0\).

To maximize \(P_8\), put \(x=1/\sqrt{1+h^2}\in(0,1)\) and \(g(x)=2\arcsin(x/2)-\arcsin(\sqrt3 x/2)\). Then
\[
g'(x)=\frac1{\sqrt{1-x^2/4}}-\frac{\sqrt3/2}{\sqrt{1-3x^2/4}}.
\]
Both denominators are positive, so comparison of squares gives \(g'(x)>0\) for \(x<2/3\) and \(g'(x)<0\) for \(x>2/3\). The unique maximizing value is \(x=2/3\), equivalently \(h=\sqrt5/2\). Substitution gives the sharp maximum. This completes the proof.

## Verification
A separate executable program, `geometry_hex_prism_check.py`, compares the deterministic edge-crossing count to the ordered-projection count for 350,000 fixed-seed normal directions in each of 15 prism configurations, including regular six- and eight-gonal bases and a nonsymmetric-metric centrally symmetric hexagon. It independently integrates the general law over 30,000 azimuths, compares the regular-hexagon formulas with those integrals and simulated frequencies, checks explicit height recovery, and tests the extremum. Run using Python with NumPy installed: `python geometry_hex_prism_check.py`. These finite computations corroborate but are not used to prove the universal statements or exact optimization.

## Relationship to prior work
Voss (1982) developed an integral-geometric treatment of polygon frequencies in random planar sections of polyhedra. Ohser and Mücklich (1995) considered inversion of size–shape distributions from stereological sections of random regular prisms. These established geometric-stereology problems motivate the current central, orientation-only conditional law, but the full texts were not available for decisive line-by-line comparison. Their random cutting-plane ensembles generally have offset degrees of freedom that are absent here; no claim that the present formula is implied or excluded by those articles is made from abstracts alone.

Hartley, Pellicer, and Williams (2012) studied geometric/combinatorial prism and antiprism families through minimal regular abstract covers, not random central section probabilities. Finch (2012) examined random planar **projections** of other polytopes; projection vertex counts are not central-section side counts. The contribution here is the order-statistic stratification for arbitrary centrally symmetric polygonal bases, the resulting universally height-identifying quadrilateral statistic, and the closed hexagonal-prism law with its unique octagon optimum. These particular conclusions were not located in the examined accessible works, but historical priority is not independently established.

## Limitations
The formulas require a fixed, centered, centrally symmetric polygonal base and central-plane sampling; an unknown base generally prevents height inference from one probability. The inversion is exact in the population model, not a claim about finite-sample estimation error. The full texts of Voss (1982) and Ohser–Mücklich (1995) were unavailable for complete priority checking. The result has not undergone an independent mathematical audit.

## References
1. M. I. Hartley, D. Pellicer, G. Williams, *Minimal covers of the prisms and antiprisms*, arXiv:1206.6119v1, first posted 2012-06-26; primary MSC 51M20. https://arxiv.org/abs/1206.6119
2. K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy 128 (1982), 111–120, DOI: 10.1111/j.1365-2818.1982.tb00443.x.
3. J. Ohser, F. Mücklich, *Stereology for some classes of polyhedrons*, Advances in Applied Probability 27 (1995), 384–396, DOI: 10.2307/1427832.
4. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, 2012-03-12. https://arxiv.org/abs/1203.2464
