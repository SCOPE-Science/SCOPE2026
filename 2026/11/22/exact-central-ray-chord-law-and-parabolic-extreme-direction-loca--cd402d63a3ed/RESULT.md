# Sharp conditional localization of nearly longest central chords in the Steinmetz bicylinder

## Finding

Let \(K=\{(x,y,z):x^2+z^2\le1,\ y^2+z^2\le1\}\), let \(U\) be uniform on \(S^2\), and let \(L\) be the length of the whole chord through the origin in direction \(U\). For \(0<h<1\), set \(\ell(h)=2\sqrt{2/(1+h)}\). Conditional on \(L>\ell(h)\), write \(J\) for the index of the closest diagonal azimuth \(\phi_J=\pi/4+J\pi/2\), \(0\le J\le3\); put \(q=\phi-\phi_J\) with \(|q|<\pi/4\). Let \(\mu_h\) be the conditional law of \((J,q/h,U_z/\sqrt h)\).

The mark \(J\) is exactly uniform and independent of the other two coordinates. The unmarked coordinates are uniform on the domain
\[
D_h=\{(a,b): |b|<1,\ |a|<w_h(b)\},\qquad
w_h(b)=\frac1{2h}\arcsin\frac{h(1-b^2)}{1-hb^2}.
\]
These domains contain the limiting parabola-bounded region \(D=\{(a,b):2|a|+b^2<1\}\), of area \(4/3\). Write \(\mu_0\) for uniform marking and independent uniform area on \(D\), with unmarked density \(3/4\). In the convention \(d_{\rm TV}(\mu,\nu)=\sup_E|\mu(E)-\nu(E)|\), the exact distance and its sharp first term are
\[
d_h=d_{\rm TV}(\mu_h,\mu_0)=1-\frac{4/3}{|D_h|}
=\frac h5+O(h^2)\qquad(h\downarrow0).
\]
For each \(h>0\), the full discrepancy is given by the exact mixture \(\mu_h=(1-d_h)\mu_0+d_h\rho_h\), where \(\rho_h\) has uniform mark and is uniform in area on the excess shell \(D_h\setminus D\). As \(h\downarrow0\), \(\rho_h\) converges weakly to the following marked boundary law: take independent \(J\) uniform on the four marks, \(S\) uniform on \(\{-1,1\}\), and \(B\) with density \(\tfrac{15}{4}b^2(1-b^2)\mathbf1_{(-1,1)}(b)\). The limiting vector is \((J,S(1-B^2)/2,B)\).

## Assumptions and scope

These probabilities use the center-pinned Haar direction, with the direction vector recorded on the sphere (hence four oriented marks), not a random affine line. Only the fixed solid formed by equal-radius orthogonal cylinders sharing a center is treated. The parameter \(h\) is dimensionless; lengths rescale with a common cylinder radius. The statement concerns the conditional spatial law and its approximation error, not historical priority for the scalar law of \(L\).

## Proof

Writing \(T=\min(|U_x|,|U_y|)\), both cylinder inequalities give \(L=2/\sqrt{1-T^2}\). In a diagonal azimuth sector write
\[
U=(\sqrt{1-z^2}\cos(\phi_J+q),\sqrt{1-z^2}\sin(\phi_J+q),z),\qquad |q|<\pi/4.
\]
Then \(1-2T^2=z^2+(1-z^2)|\sin 2q|\). Thus \(L>\ell(h)\) if and only if \(z^2+(1-z^2)|\sin 2q|<h\). The event lies off the sector boundaries and poles for \(h<1\). Put \(q=ha\) and \(z=\sqrt h\,b\). Necessarily \(|b|<1\); in the given sector, monotonicity of sine for \(2|q|\in[0,\pi/2)\) gives exactly \(|a|<w_h(b)\). The argument of the inverse sine is between zero and \(h\), because \((1-b^2)/(1-hb^2)\le1\). Spherical area is \(d\phi\,dz\), hence the rescaled density on each sector is constant with Jacobian \(h^{3/2}\). The domains agree on all four sectors, giving uniform independent marking.

Let \(w_0(b)=(1-b^2)/2\). The inequality \(\arcsin x\ge x\) on \([0,1]\) and \(1-hb^2\le1\) show \(w_h\ge w_0\). The area excess is positive for \(h>0\), and on \([-1,1]\) as \(h\downarrow0\), uniformly,
\[
w_h(b)=w_0(b)+\tfrac h2 b^2(1-b^2)+O(h^2).
\]
Indeed, expand \((1-hb^2)^{-1}\) uniformly, and use \(\arcsin x=x+O(x^3)\) for \(0\le x\le h\). Integration gives
\[
|D_h|=2\int_{-1}^1 w_h(b)\,db=\frac43+\frac4{15}h+O(h^2).
\]
For normalized uniform measures on nested sets the larger-set law is a mixture of the smaller-set law and the uniform excess law, which are mutually singular. The mixture coefficient is attained as the TV discrepancy of the excess event; the uniform independent mark leaves it unchanged. This proves the exact distance and the sharp term.

Finally, under the shell law the height \(b\) has density \(2(w_h(b)-w_0(b))/(|D_h|-4/3)\) on \((-1,1)\); this converges uniformly there to \((15/4)b^2(1-b^2)\). Conditional on this height, the sign is uniform, and the magnitude is uniform between \(w_0(b)\) and \(w_h(b)\). The uniform bound \(w_h-w_0=O(h)\) forces that magnitude to approach \(w_0(b)\). Testing with bounded continuous functions (all the supports for small \(h\) lie in one compact set) proves the stated weak limit. The shell limit is not a TV limit to a boundary-supported measure.

## Relationship to prior work

The scalar survival probability is the sum of four equal spherical cap-intersection areas, divided by \(4\pi\). Mazonka, *Solid Angle of Conical Surfaces, Polyhedral Cones, and Intersecting Spherical Caps*, [arXiv:1205.1396](https://arxiv.org/abs/1205.1396), §4.3, gives general formulas for these areas. The pair-overlap kernel in [*Exact Haar central-chord law of rectangular boxes and its singularity thresholds*](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-haar-central-chord-law-of-rectangular-boxes-and-its-singul--04bd972e6d48) directly evaluates this survival probability at equal coordinate thresholds and already gives the scalar \(3/2\)-power lens onset. Its local shrinking-triangle calculation is a related leading-order geometry, not the exact conditional excess distribution derived here. A [strictly unequal-radii bicylinder result](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-isotropic-central-chord-law-and-contact-transition-for-an--6836a26dd40d) also describes shrinking wedges and gives scalar endpoint laws and a different contact label. The present result concerns how the full conditional law deviates from its parabolic limit, in a specific azimuth-height normalization; the shell law is not specified by scalar area alone.

## Verification

Run `python3 verify_localization.py` with the standard library. The script checks the exact conditional domain against the radial condition at a bounded grid of directions. Numerical quadrature checks the rescaled area against the scalar cap-overlap formula and corroborates the sharp TV coefficient and the shell height limit via its second moment. The analytic proof, not these finite checks, establishes the statements over the full parameter range.
