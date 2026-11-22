# A sharp diameter switch and rare-chord crossover for finite catenary arcs

## Finding

Let \(\Gamma_L=\{(x,\cosh x):-L\le x\le L\}\), with \(L>0\). There exists exactly one \(L_*\in(2.1,2.3)\), characterized by the equations below, at which its Euclidean diameter changes from the horizontal chord joining the endpoints to two symmetric endpoint-to-interior chords. Numerically \(L_*\approx2.195042322200679\), and the interior contact parameter at the transition is \(z_*\approx0.858743695256390\). In particular, the diameter as a function of \(L\) is continuous and has a strict derivative jump at \(L_*\).

Choose two points independently and uniformly **by arclength** on \(\Gamma_L\); let \(X_L\) be their Euclidean chord length and \(D_L=\operatorname{diam}(\Gamma_L)\). For each fixed \(L<L_*\),
\[
\Pr(D_L-X_L\le\varepsilon)\sim\frac{\coth^2 L}{4}\,\varepsilon^2.
\]
For every fixed \(L\ge L_*\), let \(z=z(L)\in(0,L)\) denote the unique interior maximizing contact, with \(z=z_*\) at equality, and put
\[
\begin{split}
D&=\sqrt{(L+z)^2+(\cosh L-\cosh z)^2},\\
A&=\frac{L+z+(\cosh L-\cosh z)\sinh L}{D},\\
B&=\frac{\cosh z\,(\cosh L-2\cosh z)}{2D},\\
\rho_L(x)&=\frac{\cosh x}{2\sinh L}.
\end{split}
\]
Then \(A,B>0\) and
\[
\Pr(D_L-X_L\le\varepsilon)\sim
\mathcal C(L)\varepsilon^{3/2},\qquad
\mathcal C(L)=\frac{16\rho_L(L)\rho_L(z)}{3A\sqrt B}.
\]
At the transition, \(\mathcal C(L_*)\approx0.209137127699404\). Thus the rare-chord exponent jumps from \(2\) to \(3/2\) at a finite, first-order switch rather than a merger of the maximizing pairs.

There is a sharp double-scaling crossover. Let \(L_\varepsilon=L_*+\lambda\varepsilon\) for fixed \(\lambda\in\mathbb R\) and define \(k=A(L_*)-2>0\) (numerically \(k\approx1.881452102681085\)). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-3/2}
\Pr(D_{L_\varepsilon}-X_{L_\varepsilon}\le\varepsilon)
=\mathcal C(L_*)\,[1+k\min(\lambda,0)]_+^{3/2},
\]
where \([t]_+=\max(t,0)\). At any fixed \(L\ge L_*\), conditional on an almost-diametral chord, one of the four ordered symmetric endpoint-to-interior contact patterns has limiting probability \(1/4\); in a selected pattern the rescaled inward endpoint distance and centered interior parameter become uniform on \(\{(u,v):u\ge0,\ u+v^2\le1\}\) after the respective scalings \(A/\varepsilon\) and \(\sqrt{B/\varepsilon}\).

## Assumptions and scope

All lengths are in the same Euclidean units and the normalized catenary is \((x,\cosh x)\). Scaling the entire curve by a positive factor scales the critical physical half-span accordingly. The two random points are independent with probability density \(\rho_L(x)\,dx\) on the parameter interval; this is arclength-uniform, not coordinate-uniform. The asymptotic limits hold as \(\varepsilon\downarrow0\) with fixed \(L\), or in the stated \(L_\varepsilon\) regime; no uniformity over all positive spans is claimed.

The exact transition is the unique solution \(L_*>0\) admitting an interior \(0<z_*<L_*\) such that
\[
( L_*+z_* )^2+(\cosh L_*-\cosh z_*)^2=4L_*^2,
\quad
(\cosh L_*-\cosh z_*)\sinh z_*=L_*+z_*.
\]

## Proof

**1. Reduction to one endpoint.** For any two parameters \(s<t\), reflect both in the vertical axis if necessary so that \(t\ge0\). If \(|s|\le t\), replacing \(t\) by \(L\) increases both the horizontal and absolute vertical separations, since \(\cosh L\ge\cosh t\ge\cosh s\). If \(|s|>t\), then \(s<0\), and replacing \(s\) by \(-L\) increases both separations, since \(\cosh L\ge\cosh s>\cosh t\). Therefore a diameter always has an endpoint at \(\pm L\). Reflecting as necessary, maximize
\[
Q_L(x)=(L+x)^2+(\cosh L-\cosh x)^2,\qquad -L\le x\le L.
\]
For \(-L\le x\le0\), its derivative is positive apart from the trivial left endpoint, so it suffices to consider \(0\le x\le L\). The endpoint option has \(Q_L(L)=4L^2\).

**2. At most one interior competitor.** Define
\[
H_L(x)=(\cosh L-\cosh x)\sinh x-(L+x).
\]
Then \(Q_L'(x)=-2H_L(x)\) and
\[
H_L'(x)=\cosh x\,(\cosh L-2\cosh x).
\]
Thus \(H_L\) increases and then decreases (or decreases throughout); it begins at \(-L\) and ends at \(-2L\). Consequently, \(Q_L\) has at most one interior local maximum, necessarily the smaller of two possible positive roots of \(H_L=0\). At that root, \(\cosh L>2\cosh x\), so the maximum is strictly nondegenerate.

**3. Existence, strict uniqueness, and first-order character of the switch.** Write \(x=rL\) with \(0\le r<1\). The interior chord exceeds the endpoint chord exactly when
\[
\frac{\cosh L-\cosh(rL)}{L}>\sqrt{4-(1+r)^2}.
\]
For each fixed \(r<1\), the left side is strictly increasing from zero to infinity in \(L\): its power series has positive coefficients \((1-r^{2j})L^{2j-1}/(2j)!\). Thus each \(r<1\) has exactly one crossing length. These lengths tend to infinity as \(r\uparrow1\) (the left side is \(O(1-r)\) at fixed \(L\), whereas the right side is of order \(\sqrt{1-r}\)). Their infimum is attained. It cannot occur at \(r=0\): at the crossing for \(r=0\), the derivative with respect to \(r\) of the squared-chord excess is strictly positive. Therefore the first contact occurs for an interior \(r_*\in(0,1)\), necessarily at the unique interior local maximum from Step 2. Strict increase in \(L\) for every fixed \(r\) proves that this switch happens exactly once, with no second phase change.

At the tie, \(Q_L(z_*)=4L_*^2\) and \(H_L(z_*)=0\). Let \(I(L)=\sqrt{Q_L(z(L))}\) be the interior local-maximum length. The envelope theorem gives \(I'(L_*)=A_*\), whereas the endpoint length has derivative \(2\). Strict increase of the normalized squared-chord excess in Step 3 at the minimizing \(r_*\) gives \(A_*>2\); hence \(D_L=2L\) below and \(D_L=I(L)\) above, with a strict derivative jump \(k=A_*-2\). The two symmetric interior pairs persist at the transition and are separate from the endpoint pair.

**4. Local integration and limiting marks.** The arclength speed is \(\sqrt{1+\sinh^2x}=\cosh x\), giving the stated density. Below the switch the unique unordered maximizing pair is \((-L,L)\), and for the inward coordinate deviations \(u,v\ge0\),
\[
2L-\|\gamma(-L+u)-\gamma(L-v)\|=u+v+O((u+v)^2).
\]
There are two ordered neighborhoods. The triangle \(\{u,v\ge0:u+v\le\varepsilon\}\) has area \(\varepsilon^2/2\), giving \(\rho_L(L)^2\varepsilon^2\).

At and above the switch, the four ordered neighborhoods correspond to \((-L,z),(z,-L),(L,-z),(-z,L)\). Near \((-L,z)\), for endpoint inward perturbation \(u\ge0\) and interior perturbation \(v\in\mathbb R\),
\[
D-\|\gamma(-L+u)-\gamma(z+v)\|
=A u+Bv^2+O(u^2+|u v|+|v|^3).
\]
Here \(A>0\), and \(B>0\) follows from \(Q_L''(z)=2\cosh z(2\cosh z-\cosh L)<0\). The limiting region \(\{u\ge0:A u+Bv^2\le\varepsilon\}\) has area \(4\varepsilon^{3/2}/(3A\sqrt B)\). Multiplying by the local density and the four symmetric ordered patterns yields \(\mathcal C(L)\), while the same change of variables proves the uniform-region conditional law. At equality, the endpoint pair gives only an \(O(\varepsilon^2)\) term and is negligible at the \(\varepsilon^{3/2}\) scale.

**5. Transition window.** The two competing maximal chord lengths differ by
\[
I(L)-2L=k(L-L_*)+O((L-L_*)^2).
\]
For \(L=L_*+\lambda\varepsilon\), the local interior maximum lies below the global diameter by \(\max\{0,-k\lambda\varepsilon\}+O(\varepsilon^2)\). Substituting its remaining deficit allowance into the Step 4 local volume, and observing that the endpoint neighborhoods contribute only \(O(\varepsilon^2)\), proves the stated crossover for every fixed \(\lambda\).

## Verification

The included `checker.py` uses Python's standard library. It bisects the exact contact equations, compares globally predicted diameters with a dense sample of candidate chords at several spans, checks signs on both sides of the transition, and compares finite-tolerance arclength-weighted chord-tail quadratures to both asymptotic regimes. Run `python3 checker.py`. These checks are diagnostic finite computations; the proof of all quantifiers is analytic in Steps 1–5.

## Relationship to prior work

Rojas (2014) describes the catenary parametrization and its variational origin, but does not give a two-point Euclidean diameter phase diagram. Coll and Harrison (2014) study constant volume-to-area and area-to-arclength ratios for catenaries and their higher-dimensional analogues, not maximal chord pairs or rare random distances. The present result uses the classical catenary and basic arclength formula as inputs; it does **not** claim them as new. Literature searches included the exact shape, equivalent farthest-point/diametral-chord wording, and random arclength-chord tails. Closely related published random-chord laws for polygons, cylinders, and convex boundaries use different objects or sampling measures and do not directly imply the specific two-branch catenary threshold and crossover.

## Limitations

The finding concerns finite **symmetric** catenary arcs, not nonsymmetric spans, general hanging chains with nonuniform density, arbitrary graph curves, nor intrinsic along-curve distance. The numeric constants are floating-point evaluations of exact implicit definitions, not independently certified decimal enclosures. Broad historical literature coverage is incomplete; the theorem has had only self-review and no independent mathematical audit.

## References

1. R. Rojas, *The straight line, the catenary, the brachistochrone, the circle, and Fermat*, arXiv:1401.2660, first public 2014-01-12, https://arxiv.org/abs/1401.2660.
2. V. Coll and M. Harrison, *Two Generalizations of a Property of the Catenary*, American Mathematical Monthly 121 (2014), 109–119, https://doi.org/10.4169/amer.math.monthly.121.02.109.
3. E. M. Horsburgh, *An Approximate Formula for the Length of an Arc of a Suspended Rope*, Proceedings of the Edinburgh Mathematical Society 36 (1917), 94–95, https://doi.org/10.1017/S0013091500035264 (arc-length approximation, not a diameter theorem).
