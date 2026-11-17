# A cubic-logarithmic pole-containment transition for three random spherical-cap vertices

## Finding

Let \(N=(0,0,1)\), let \(0<\alpha<\pi\), and let \(V_1,V_2,V_3\) be independent uniform-surface-area points in the closed spherical cap \(K_\alpha=\{v\in S^2:v\cdot N\ge\cos\alpha\}\). Write \(P_\alpha=S^2\cap\operatorname{pos}\{V_1,V_2,V_3\}\), the spherical convex hull, and \(p(\alpha)=\Pr(N\in P_\alpha)\). The following assertions hold.

1. For every \(0<\alpha\le\pi/2\), \(p(\alpha)=1/4\).
2. With \(h=-\cos\alpha\downarrow0\) from the *larger-than-hemisphere* side,
   \[
   \lim_{h\downarrow0}\frac{1/4-p(\arccos(-h))}{h^3\log(1/h)}=\frac4{\pi^2}.
   \]
   Equivalently, with \(\delta=\alpha-\pi/2\downarrow0\), \(p(\pi/2+\delta)=1/4-(4/\pi^2)\delta^3\log(1/\delta)+o(\delta^3\log(1/\delta))\).
3. A more precise marked law identifies the configurations causing this loss. Let \(E_h\) be the event that the three projected azimuths enclose the planar origin but the spherical convex hull misses \(N\). On \(E_h\), write \(J_h\) for the index of the smallest complementary gap \(b_i\) defined in the proof, \(T_h\) for the number of sampled vertices with negative height, and \(U_h=\log(1/\min_i b_i)/\log(1/h)\). Conditional on \(E_h\), the triple \((J_h,T_h,U_h)\) converges weakly to independent variables: \(J\) uniform on three indices, \(\Pr(T=1)=1/4\), \(\Pr(T=2)=3/4\), and \(U\) uniform on \((0,1)\). In particular \(\Pr(T_h=3\mid E_h)\to0\). The particular cyclic indexing of the three \(b_i\)'s is immaterial.

## Assumptions and scope

The surface-area sampling measure is normalized on the spherical cap, including caps strictly larger than a hemisphere. The spherical hull means the positive conic hull intersected with \(S^2\), not the Euclidean convex hull of the three vertices. The vertices are almost surely distinct and in general position. Every asymptotic is for exactly three vertices on \(S^2\); no higher-dimensional or growing-sample assertion is made. For \(\alpha\le\pi/2\), the fixed pole is in the sample cap, and the positive hull is contained in its hemisphere.

## Proof

**1. Exact coordinates and the flat hemispherical plateau.** Write \(V_i=(\sqrt{1-z_i^2}\cos\phi_i,\sqrt{1-z_i^2}\sin\phi_i,z_i)\). Surface-area uniformity means that the azimuths \(\phi_i\) are independent uniform angles and the heights \(z_i\) are independent uniform variables on \([\cos\alpha,1]\), independently of the azimuths. For three cyclically sorted azimuths, let \(g_1,g_2,g_3\) be their successive counterclockwise gaps, summing to \(2\pi\). Their positive horizontal vectors span the planar origin precisely when every \(g_i<\pi\), an event of probability \(1/4\) (the complementary semicircle event has probability \(3/4\)). In that event put \(b_i=\pi-g_i\), so \(b_i>0\), \(b_1+b_2+b_3=\pi\). The vector of positive coefficients in the horizontal null relation is, up to common normalization and a cyclic permutation, \((a_i/\sqrt{1-z_i^2})_{i=1}^3\), where \(a_i=\sin b_i\). Consequently the pole lies in the positive cone precisely when
\[
\sum_{i=1}^3 a_i q(z_i)>0,\qquad q(z)=\frac z{\sqrt{1-z^2}}.
\]
Equalities have probability zero. Conditional on the azimuthal enclosing event, the \((b_1,b_2)\) pair has constant density \(2/\pi^2\) on \(\mathcal B=\{b_1,b_2>0:b_1+b_2<\pi\}\). Unconditionally its density on this triangle is \(1/(2\pi^2)\). For caps no larger than a hemisphere all \(z_i\) are positive almost surely, so exactly the enclosing azimuths produce pole containment and \(p=1/4\).

**2. Exact integral for the loss.** For \(\alpha>\pi/2\), put \(h=-\cos\alpha\in(0,1)\). Let \(a_i=\sin b_i\) and define
\[
\mathcal V_h(a)=\int_{[-h,1]^3}\mathbf1\!\left\{\sum_{i=1}^3a_iq(z_i)<0\right\}\,dz_1dz_2dz_3.
\]
The loss \(\Delta(h)=1/4-p(\arccos(-h))\) satisfies the exact identity
\[
\Delta(h)=\frac1{2\pi^2(1+h)^3}\int_{\mathcal B}\mathcal V_h(\sin b_1,\sin b_2,\sin b_3)\,db_1db_2.
\tag{1}
\]
This identity is an exact finite integral for each \(0<h<1\).

**3. Local simplex volume and the logarithmic boundary singularity.** Put \(A=a_1+a_2+a_3\) and \(m=\min_i a_i\). For \(m\ge h^\gamma\) with a fixed \(0<\gamma<1\), all coordinates contributing to the integrand of \(\mathcal V_h\) satisfy \(\max_i(z_i)_+=O(hA/m)=O(h^{1-\gamma})\). This follows from \(q(z)\ge z\) for \(z\ge0\) and \(q(z)\ge z-O(h^3)\) for \(-h\le z<0\). On that domain \(q(z)=z(1+o(1))\) uniformly for positive \(z\), and the relative correction on negative \(z\) is \(O(h^2)\). Sandwiching between the corresponding affine halfspaces, and translating \(w_i=z_i+h\), gives uniformly
\[
\mathcal V_h(a)=(1+o(1))\operatorname{vol}\{w_i\ge0:\sum_i a_iw_i<hA\}
=(1+o(1))\frac{h^3 A^3}{6a_1a_2a_3}.
\tag{2}
\]
The region in the middle is a three-dimensional simplex with the displayed volume; the upper bounds \(z_i\le1\) are inactive in this range.

For \(b_k=t\downarrow0\) with the other variable \(b_i\to\beta\in(0,\pi)\), the third is \(\pi-t-\beta\). Thus \(a_k\sim t\), \(a_i,a_j\to\sin\beta\), and
\[
\frac{A^3}{6a_1a_2a_3}\sim\frac{4\sin\beta}{3t}.
\tag{3}
\]
The three boundary sides of \(\mathcal B\) yield, for the region \(m\ge h^\gamma\),
\[
\int_{\mathcal B\cap\{m\ge h^\gamma\}}\frac{A^3}{6a_1a_2a_3}\,db_1db_2
=8\gamma\log(1/h)+O_\gamma(1),
\tag{4}
\]
because \(3\cdot(4/3)\int_0^\pi\sin\beta\,d\beta=8\). At corners the edge coefficient tends to zero, so no extra leading logarithm arises.

For completeness, the neglected thin boundary is controlled as follows. The three positive numbers \(a_i=\sin b_i\) are proportional to the sides of a Euclidean triangle with angles \(b_i\); hence the two largest are comparable, and \(A\) is bounded by a universal multiple of either. For all sufficiently small \(h\), the implication
\[
\sum_i a_iq(z_i)<0\quad\Longrightarrow\quad
\sum_i a_i(z_i+h)<hA(1+Ch^2)
\tag{5}
\]
follows from \(q(z)\ge z-Ch^3\) for \(-h\le z\le1\). Therefore \(\mathcal V_h(a)\le C h^3/m\) when \(m\ge h\), by the enclosing simplex volume. When \(m<h\), the two coordinates associated with the larger coefficients range over intervals of length at most \(Ch\), while the remaining coordinate has length at most \(1+h\), giving \(\mathcal V_h(a)\le Ch^2\). The angular region \(m<h\) has area \(O(h)\), and the integral of \(1/m\) over \(h\le m<h^\gamma\) is \(O((1-\gamma)\log(1/h)+1)\). Thus its contribution is at most \(C h^3[(1-\gamma)\log(1/h)+1]\). Combining with (2)--(4), first letting \(h\downarrow0\), then \(\gamma\uparrow1\), proves the coefficient in assertion 2.

**4. Marked configurations.** To resolve signs, consider the boundary side \(b_k=t\ll1\). In the logarithmically contributing window \(h\ll t\ll1\), write \(s=\sin\beta\) for the common first-order value of \(a_i,a_j\). For exactly two negative heights (indices \(i,j\)) and one positive height (index \(k\)), integrate \(z_i=-hu\), \(z_j=-hv\) and the allowable positive \(z_k\); the contribution is
\[
\mathcal V_{2,k}(a)\sim\frac{h^3s}{t}\int_0^1\!\int_0^1(u+v)\,du\,dv=\frac{h^3s}{t}.
\tag{6}
\]
For exactly one negative height at \(i\), the other nonexceptional positive height is \(z_j=hv\) with \(0\le v<u\), while \(z_k\) fills the remaining interval. This gives
\[
\mathcal V_{1,i}(a)\sim\frac{h^3s}{t}\int_0^1\!\int_0^u(u-v)\,dv\,du=\frac{h^3s}{6t}.
\tag{7}
\]
The analogous contribution for a negative height at \(j\) is equal. The other sign patterns do not carry the \(1/t\) singularity on this edge. Hence the logarithmic coefficient splits as \(1:(1/6+1/6)=3:1\) between two and one negative heights, respectively. The event of three negative heights has probability at most \(h^3/[4(1+h)^3]\), which is negligible against \(h^3\log(1/h)\).

By symmetry, all three choices of the vanishing gap have equal mass. For any \(0<u<v<1\), restricting \(t=\min b_i\) to \([h^v,h^u]\) multiplies each edge's leading logarithmic integral by \(v-u\). The same uniform approximations used above hold on every such fixed logarithmic band; the thin-region estimates control the endpoints. Thus the joint conditional law of the gap index, number of negative heights, and logarithmic gap scale converges to the product law stated in assertion 3. This is weak convergence of the marked triple, not a claim of total-variation convergence of the unscaled original configuration.

## Verification

The independently implemented Cartesian determinant test uses three direct random three-dimensional surface points and checks the signed horizontal determinants plus vertical weighted sum. It agrees with five-dimensional scrambled-Sobol integration of (1) with no geometric determinant calculations in common. The quadrature gives \(\Delta(0.10)\approx0.00137297\), \(\Delta(0.05)\approx0.00022747\), and \(\Delta(0.02)\approx0.0000186758\). A two-scale numerical slope for \(\Delta(h)/h^3\) between \(h=0.0002\) and \(h=0.00002\) is approximately \(0.390\), approaching the predicted asymptotic slope \(4/\pi^2\approx0.405285\) as the scales shrink and quadrature is refined. At finite \(h\), convergence is slowed by a nonzero cubic correction. The exact proof relies on the above comparison bounds, not on numerical evidence. Run `python check_cap.py` with the versions in `requirements.txt` or compatible later versions.

## Relationship to prior work

The \(1/4\) hemispherical pole-containment plateau is already known (and is also an elementary planar semicircle consequence); it is included solely to normalize the new beyond-hemisphere transition. Wendel's classical theorem determines hemisphere separability for centrally symmetric samples, rather than the fixed-pole inclusion probability for three points sampled from an enlarged spherical cap. Bárány--Hug--Reitzner--Schneider (2015) investigate spherical hulls of independent points in a hemisphere, especially face counts and approximation as the number of points grows, and motivate the sharp hemispherical boundary. Bürgisser--Cucker--Lotz (2010) consider *covering the entire sphere by randomly centered caps* rather than the fixed-pole containment event for three points sampled inside one cap. Their coverage formula neither states nor directly implies the local cubic-logarithmic transition or its marked sign-and-gap mechanism. None of these observations asserts that every possible historical source has been exhausted.

## Limitations

The result concerns only three independent uniform-area samples on \(S^2\), a cap centered at the target pole, and the one-sided regime from above a hemisphere. The logarithmic asymptotic is a limit, not a finite-error bound with an explicit rate. The sign/gap statement is weak convergence. Numerical tests are finite checks, not an infinite proof or independent certification. Historical priority remains subject to further source investigation.

## References

1. I. Bárány, D. Hug, M. Reitzner, R. Schneider, *Random points in halfspheres*, first public preprint 18 May 2015, arXiv:1505.04672v1, https://arxiv.org/abs/1505.04672.
2. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica **11** (1962), 109--112, https://doi.org/10.7146/math.scand.a-10655.
3. P. Bürgisser, F. Cucker, M. Lotz, *Coverage processes on spheres and condition numbers for linear programming*, Annals of Probability **38** (2010), 570--604, original arXiv:0712.2816, https://arxiv.org/abs/0712.2816.
