# A flux-uniform single-band theorem for high-branching triangular cacti

## Finding

For every integer \(m\ge3\), let \(\Gamma_m\) be the infinite triangle cactus in which each vertex belongs to exactly \(m\) triangles and different triangles share at most one vertex. Put unit-magnitude Hermitian nearest-neighbor hopping on its edges, with the same oriented magnetic flux \(\phi\) around every triangular face. Write \(c=\cos\phi\). Its bounded magnetic adjacency operator \(H_{m,\phi}\) on \(\ell^2(V\Gamma_m)\) has **purely absolutely continuous spectrum supported on one closed interval for every flux**: no spectral gaps, eigenvalues, or flat bands occur.

For \(|c|<1\), the two band edges \(L_{m,c}<R_{m,c}\) are exactly the two real simple zeros of
\[
 D_{m,c}(E)=E^4+2(m-1)cE^3+(m^2-12m+9)E^2
 -18m(m-1)cE-(2m-3)^3-27(m-1)^2c^2.
\]
In particular, \(\sigma(H_{m,\phi})=[L_{m,c},R_{m,c}]\), and its density of states is strictly positive in the open interval.

At \(c=1\), this interval is \([1-\sqrt{8(m-1)},\,1+\sqrt{8(m-1)}]\); at \(c=-1\), it is the negative of that interval. At the critical branching \(m=3,c=1\), the density has the integrable singularity
\[
 \rho_{3,1}(-3+\varepsilon)\sim \frac{\sqrt2}{3\pi\sqrt\varepsilon}\quad(\varepsilon\downarrow0).
\]
By spectral reflection, \(m=3,c=-1\) has the corresponding singularity at energy \(+3\); every other band edge in this theorem has ordinary square-root vanishing. Thus branching \(m=3\) is the sharp transition from the known flux-dependent point spectrum at \(m=2\) to all-flux gaplessness and absence of point spectrum.

## Assumptions and scope

The graph is a connected, countably infinite, regular block graph of triangles with a tree-like incidence structure (no cycles of triangles); equivalently it is the Cayley graph of \(\mathbb Z_3*\cdots*\mathbb Z_3\) (\(m\) free factors), using each order-three generator and its inverse. Every vertex has degree \(2m\). Choose an orientation on each triangular block so its three positively oriented edges have coefficient \(e^{i\phi/3}\); reverse edges carry conjugate coefficients. This determines a bounded self-adjoint operator. A different gauge leaves the spectrum unchanged. The spectral density is the local spectral measure at any vertex, which is also the normalized trace spectral measure of this transitive Cayley operator. The claim covers all real \(\phi\), all integer \(m\ge3\), and the entire operator spectrum; it does not concern interacting many-body Hamiltonians.

## Proof

**Cavity identity.** Fix \(z\) in the upper half-plane and write \(h(z)\) for the diagonal self-energy contributed to a vertex by one adjacent triangular block together with its forward branches. If \(y=z-(m-1)h\), Schur complementation across the two other vertices of that triangle gives
\[
 h=\frac{2(y+c)}{y^2-1},\qquad
 y=z-(m-1)h.
\]
The outgoing resolvent of a self-adjoint subtree has negative imaginary part, hence \(\operatorname{Im}h<0\) and \(\operatorname{Im}y>0\) for \(\operatorname{Im}z>0\). Eliminating \(h\) yields the cubic
\[
 P_{m,c}(y,z)=y^3-zy^2+(2m-3)y+z+2(m-1)c=0,
\]
where the physical root is the analytic branch satisfying \(y(z)/z\to1\) at infinity. The diagonal Green function is
\[
 G(z)=\langle\delta_o,(z-H_{m,\phi})^{-1}\delta_o\rangle
 =\frac{1}{z-mh}
 =\frac{y^2-1}{y^3-3y-2c}.
\]
All identities can also be obtained as convergent upper-half-plane resolvent identities on finite-depth truncations; the physical branch is specified by the resolvent sign and infinity asymptotic, rather than by an arbitrary cubic root.

**Nondegenerate flux.** The discriminant of the cubic in \(y\) is exactly \(4D_{m,c}(E)\). Direct polynomial expansion gives
\[
 \operatorname{disc}_E(D_{m,c})=
 -16(c^2-1)(m-1)^2
 \bigl[27(m-1)^2(c^2-1)-2(m-3)^3\bigr]^3.
\]
For each \(m\ge3\) and \(|c|<1\), the right side is strictly negative. A real quartic with negative discriminant has precisely two real simple zeros; because \(D_{m,c}(0)<0\), they satisfy \(L_{m,c}<0<R_{m,c}\), and \(D<0\) exactly between them. Thus for \(E\in(L_{m,c},R_{m,c})\) the cubic has one real root and two conjugate nonreal roots. The real root \(u\) satisfies \(-1<u<1\), since
\[
 P_{m,c}(-1,E)=2(m-1)(c-1)<0,
 \qquad P_{m,c}(1,E)=2(m-1)(1+c)>0.
\]
It is a simple positive-slope crossing: \(\partial_y P(u,E)>0\). Since \(\partial_E P(u,E)=1-u^2>0\), implicit differentiation yields \(du/dE=-(1-u^2)/\partial_yP<0\). An upper-half-plane physical root cannot approach this real branch: its analytic continuation to \(E+i\eta\) would have negative imaginary part for sufficiently small positive \(\eta\), contrary to \(\operatorname{Im}y>0\). Hence the physical boundary value is the complex root with positive imaginary part throughout the open band. Because \(\operatorname{Im}h=-\operatorname{Im}y/(m-1)<0\), its Green function has strictly negative imaginary part, giving strictly positive density \(-\operatorname{Im}G(E+i0)/\pi\). Outside the closed interval the cubic roots are real; the physical boundary value is real away from isolated algebraic degeneracies, so no absolutely continuous spectral mass lies there.

**Excluding hidden singular spectrum.** The finite set of branch points and poles is the only possible support of a singular component of the algebraic Cauchy transform; any singular-continuous measure supported on a finite set vanishes. For atoms, realize \(H_{m,\phi}\) as the free sum of \(m\) triangle operators in the group von Neumann algebra of \(\mathbb Z_3^{*m}\). Each summand has spectral law
\[
 \nu_\phi=\frac13\sum_{j=0}^{2}\delta_{2\cos((\phi+2\pi j)/3)}.
\]
For \(|c|<1\), every atom has mass \(1/3\), while at \(c=\pm1\) the largest mass is \(2/3\). The standard atom theorem for additive free convolution states that an atom of an \(m\)-fold free sum requires constituent atom masses adding to more than \(m-1\). Here the sum is at most \(2m/3\le m-1\) for \(m\ge3\), so no atoms occur. This also excludes isolated point spectrum for the vertex-transitive group operator: the root spectral measure has full spectral support because the diagonal matrix elements of every nonzero spectral projection cannot all vanish.

**Endpoint flux.** At \(c=1\) the cubic factors:
\[
 P_{m,1}(y,E)=(y+1)\bigl[y^2-(E+1)y+E+2m-2\bigr].
\]
The physical branch is the quadratic one, since it behaves like \(E\) at infinity. Its discriminant \((E-1)^2-8(m-1)\) gives the stated single interval. On this branch \(G=(y-1)/((y-2)(y+1))\). At \(m=3\), the lower band edge is \(E=-3\) and \(y=-1\); expanding \(y=-1+\varepsilon/2+i\sqrt{2\varepsilon}+O(\varepsilon^{3/2})\) gives the stated \(\sqrt{2}/(3\pi)\) density constant. For \(m>3\), neither quadratic band-edge root equals \(-1\), and the ordinary square-root law follows; the upper edge is regular for every \(m\ge3\). Finally, changing every hopping sign sends \(c\) to \(-c\) and reflects the spectrum, establishing the \(c=-1\) cases. The no-atom argument continues to apply at both endpoint fluxes.

## Verification

The included `verify.py` is a standard-library-only exact arithmetic checker. It verifies the cubic discriminant polynomial for a rational grid of \(m\), \(c\), and \(E\), the endpoint-flux factorization, and the first nine return moments of the \(m=3,c=1\) model in two independent ways: formal cavity expansion and closed walks in the equivalent six-neighbor Cayley graph of the free group on two generators. The output is `VERIFY_OK`. The displayed symbolic discriminant factorization and infinite-domain spectral conclusions are proven analytically above, not inferred from the finite checks.

## Relationship to prior work

Mosseri, Vogeler and Vidal derive the flux-dependent triangular Husimi cactus spectrum for **two** triangles meeting at each vertex; this is the immediate lower-branching comparison and has flat-band behavior at special flux. Lux and Prodan analyze spectral properties of Cayley-graph Hamiltonians and show connectedness of spectra for scalar self-adjoint group-algebra operators on the free group; this already implies the *gapless-only* part of the three-triangle case under the equivalent free-group Cayley description, but does not give these all-branching explicit endpoints, absolute continuity, or transition-edge asymptotics. The published three-atom free-convolution-power calculation with measure \((\delta_{-1}+\delta_0+\delta_1)/3\) covers our \(c=0\) specialization after scaling; it does not include the other magnetic fluxes. Earlier nonmagnetic Husimi-cactus densities studied by Thorpe, Weaire and Alben include five- and six-gon cacti; those results do not furnish this magnetic triangle classification. The free-convolution atom criterion is standard and credited rather than claimed as new.

## Limitations

The theorem assumes exactly identical unit hoppings and identical triangular fluxes on a homogeneous treelike triangle cactus. It does not treat unequal flux, onsite disorder, finite cactus boundary effects, or interacting models. The interval edges are given by an exact quartic rather than radicals for general flux. The previously published free-group gaplessness argument already covers one subcase; the published symmetric three-atom free-power law covers another. Closely related older nonmagnetic densities and possible poorly indexed magnetic-cactus calculations remain residual overlap risks. No independent audit has been performed.

## References

1. F. R. Lux and E. Prodan, *Spectral and Combinatorial Aspects of Cayley-Crystals*, arXiv:2212.10329 (first posted 2022-12-20), especially the free-group spectral-connectedness discussion.
2. R. Mosseri, R. Vogeler, and J. Vidal, *Aharonov-Bohm cages, flat bands, and gap labeling in hyperbolic tilings*, arXiv:2206.04543 (first posted 2022-06-08), triangular Husimi cactus discussion.
3. M. F. Thorpe, D. Weaire, and R. Alben, *Electronic Properties of an Amorphous Solid. III. The Cohesive Energy and the Density of States*, Physical Review B 7 (1973), 3777–3786, Section III.A.
4. *Three-point free convolution powers: no interior one-third cusp zero*, published mathematical record 2026/9/14/SCOPE007, specifically its three-point uniform-law calculation.
5. S. T. Belinschi, H. Bercovici, and C. W. Ho, *On the Support of Free Convolutions*, arXiv:2408.06573; general free-convolution support context (not a coverage theorem for the present discrete atomic inputs).
