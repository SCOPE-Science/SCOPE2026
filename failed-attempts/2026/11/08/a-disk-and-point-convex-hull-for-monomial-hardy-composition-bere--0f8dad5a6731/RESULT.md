# A disk-and-point convex hull for monomial Hardy composition Berezin ranges

## Finding

For every integer \(m\ge2\), let \(C_m:H^2(\mathbb D)\to H^2(\mathbb D)\) be the composition isometry \((C_mf)(z)=f(z^m)\), and let \(\mathcal B_m\) be its Berezin range with respect to the normalized Szegő kernels. Write \(R_m=1/(m+1)\) and \(D_m=\{w\in\mathbb C:|w-R_m|\le R_m\}\). Then the **exact closed convex hull** is

\[
\boxed{\overline{\operatorname{conv}}\mathcal B_m=\operatorname{conv}\bigl(\{1\}\cup D_m\bigr).}
\]

Its support function, measured in the direction \(e^{i\vartheta}\), is
\[
h_m(\vartheta)=\max\left\{\cos\vartheta,\frac{1+\cos\vartheta}{m+1}\right\}.
\]
The boundary consists of the two straight tangent segments joining \(1\) to
\[
t_\pm=\frac1m\pm i\frac{\sqrt{m^2-1}}{m(m+1)},
\]
and the **major** arc of \(\partial D_m\) connecting those tangent points through zero. Its area and perimeter are respectively
\[
A_m=\frac{\pi-\arccos(1/m)+\sqrt{m^2-1}}{(m+1)^2},
\quad
P_m=2\sqrt{\frac{m-1}{m+1}}+\frac{2\bigl(\pi-\arccos(1/m)\bigr)}{m+1}.
\]
Moreover, among the boundary points of this closed convex hull, **only \(1\) actually belongs to \(\mathcal B_m\)**.

## Assumptions and scope

Here \(H^2(\mathbb D)\) is the standard complex Hardy Hilbert space with orthonormal monomials \(1,z,z^2,\dots\); its normalized Szegő kernel is \(k_z(w)=(1-|z|^2)^{1/2}/(1-\overline z w)\). We use the convention \(\widetilde T(z)=\langle Tk_z,k_z\rangle\), so
\[
\mathcal B_m=\left\{\frac{1-|z|^2}{1-\overline z z^m}:|z|<1\right\}.
\]
The result concerns the **closed convex hull**, not the precise (nonconvex) Berezin range itself, and assumes integer \(m\ge2\). The case \(m=1\) is the identity and has singleton range \(\{1\}\).

## Proof

**Step 1: an exact pencil of circles.** Write \(z=re^{i\theta}\) with \(0<r<1\). Because \(m-1\) is a positive integer, \(e^{i(m-1)\theta}\) traverses the full unit circle. Hence the set of Berezin values at radius \(r\) is exactly the circle traced by
\[
\frac{1-r^2}{1-r^{m+1}e^{i\phi}},\qquad 0\le\phi<2\pi.
\]
A direct Möbius-circle computation gives its (real) center and radius:
\[
c(r)=\frac{1-r^2}{1-r^{2m+2}},\qquad
\rho(r)=\frac{(1-r^2)r^{m+1}}{1-r^{2m+2}}.
\]
Let \(B_r=\{w:|w-c(r)|\le\rho(r)\}\) be the filled disk. The Berezin range is contained in the union of these disks and the point \(1\). (Its circle boundaries suffice for the convex-hull calculation.)

**Step 2: a sharp universal disk containment.** Set
\[
\alpha(r)=c(r)-\rho(r)=\frac{1-r^2}{1+r^{m+1}}\in(0,1).
\]
The disk \(E_r=\alpha(r)+(1-\alpha(r))D_m\) belongs to the convex set \(K_m=\operatorname{conv}(\{1\}\cup D_m)\). Its leftmost point is \(\alpha(r)\), its radius is \((1-\alpha(r))/(m+1)\), and \(B_r\) shares that same leftmost point. The inclusion \(B_r\subseteq E_r\) is therefore equivalent to
\[
(m+1)\rho(r)\le1-\alpha(r).
\]
After substitution and clearing strictly positive denominators, the last inequality is **exactly**
\[
\sum_{j=0}^{m-1}r^{2j}\ge m r^{m-1}.
\]
This follows from the arithmetic–geometric mean inequality applied to the \(m\) positive numbers \(1,r^2,\dots,r^{2m-2}\). It is **strict** for \(0<r<1\) and \(m\ge2\). Thus every Berezin value belongs to \(K_m\), so
\[
\overline{\operatorname{conv}}\mathcal B_m\subseteq K_m.
\]

**Step 3: no envelope point is redundant.** At \(z=0\), the Berezin value is \(1\). As \(r\uparrow1\), the circle centers and radii in Step 1 both tend to \(1/(m+1)\). Each point of \(\partial D_m\) is consequently a limit of Berezin values (choose the corresponding phase \(\phi\) in Step 1). Because the closed convex hull contains \(1\) and \(\partial D_m\), it contains \(K_m\). This proves equality.

**Step 4: all boundary points and geometric invariants.** The support function of a convex hull is the maximum of its constituents' support functions. Those of \(\{1\}\) and \(D_m\) are \(\cos\vartheta\) and \(R_m(1+\cos\vartheta)\). These cross exactly when \(\cos\vartheta=1/m\). The two tangent points are obtained by intersecting \(\partial D_m\) with the corresponding supporting lines through \(1\): their real part is \(1/m\) and imaginary parts are \(\pm\sqrt{m^2-1}/[m(m+1)]\). The common tangent length is \(\sqrt{(m-1)/(m+1)}\). With \(\gamma=\arccos(1/m)\), the visible circular arc has central angle \(2\pi-2\gamma\). Adding the two tangent lengths yields \(P_m\). Adding the tangent triangle's area to the disk's area and subtracting the obscured circular segment gives
\[
A_m=\pi R_m^2+(1-1/m)\frac{\sqrt{m^2-1}}{m(m+1)}-R_m^2\bigl(\gamma-\sin\gamma\cos\gamma\bigr),
\]
which simplifies to the formula in the finding.

**Step 5: attained boundary.** Because the inequality in Step 2 is strict, \(B_r\) is strictly smaller than the internally tangent disk \(E_r\) except at their common leftmost point \(\alpha(r)\). That point is in the **interior** of \(K_m\) for every \(\alpha(r)\in(0,1)\). Consequently \(B_r\subset\operatorname{int}K_m\) for \(0<r<1\). The only remaining Berezin value, from \(r=0\), is \(1\in\partial K_m\). Thus \(\mathcal B_m\cap\partial K_m=\{1\}\).

## Verification

The attached standalone `checks.py` evaluates the circle-center, containment, support, tangent, and area identities for integer orders \(2\le m\le30\) and radial samples. Its tests are **diagnostic only**; Steps 1–5 prove the universal statement for every integer \(m\ge2\). The inequalities use exact algebra and AM–GM, not any numerical extrapolation. No computer-assisted nonstandard lemma is required.

## Relationship to prior work

Bourdon, Le, and Thompson (arXiv:2610.17634v1) give the general Hardy composition-operator Berezin-transform formula, prove general boundary/corner properties, and in Proposition 3.7 describe circular images for symbols of the form \(z\psi(z^n)\) with a linear-fractional \(\psi\). Taking \(\psi(z)=z\) obtains the circle structure in Step 1, **which is prior work rather than a claimed discovery**. Their inspected statements do not identify the sharp convex envelope of the monomial family, the AM–GM disk dominance, the tangent transition, or its exact area/perimeter. The present claim is those additional conclusions, not the underlying circle identity.

Cowen and Felder (arXiv:2109.12095) study convexity of Hardy composition-operator Berezin ranges, especially automorphisms and linear symbols. Augustine, Garayev, and Shankar (arXiv:2302.12547) address other Hardy composition-operator and finite-rank configurations. Neither inspected text gives this all-degree monomial convex-hull classification. The overlap assessment also considered publicly indexed records on monomial composition operators, which concern other invariants. Absence from these searches is not proof of publication novelty.

## Limitations

This is a result for the **standard Hardy space** and the special monomial symbols \(z^m\). It does not establish the corresponding envelope for arbitrary nonlinear selfmaps, finite Blaschke products, weighted Hardy spaces, Bergman spaces, or the exact nonconvex range \(\mathcal B_m\) itself. Published equivalent formulations under other terminology may exist and would require independent priority checking. Independent audit is not performed.

## References

1. P. S. Bourdon, T. Le, D. Thompson, *Berezin Ranges of Composition Operators on \(H^2\)*, arXiv:2610.17634v1, 13 October 2026, especially Proposition 3.7 and Theorem 3.11; https://arxiv.org/html/2610.17634v1.
2. C. C. Cowen, C. Felder, *Convexity of the Berezin Range*, arXiv:2109.12095v1; https://arxiv.org/pdf/2109.12095.
3. A. Augustine, M. Garayev, P. Shankar, *Composition operators, convexity of their Berezin range*, arXiv:2302.12547v1; https://arxiv.org/pdf/2302.12547.
