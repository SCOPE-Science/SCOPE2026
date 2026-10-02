# Pairwise incidence rigidity for transitive hypersurface families

## Result

Let \(n\ge 2\), let \(M^{n+1}\) be a smooth manifold, and let
\[
\mathscr Z=\{\Sigma_\sigma:\sigma\in P\}
\]
be an unoriented transitive family of closed embedded hypersurfaces in the sense of Martins: the Legendrian lifts of the members form a smooth locally trivial foliation of the hyperplane Grassmann bundle, so every pair \((x,\Pi)\) of a point and an unoriented tangent hyperplane lies on a unique member of the family.

Then the family has the following pairwise-incidence rigidity.

**Theorem.** For every two distinct parameters \(\sigma,\tau\in P\):

1. \(\Sigma_\sigma\) and \(\Sigma_\tau\) intersect, and their intersection is transverse.
2. If the family is in the spherical alternative of the topological classification, then
   \[
   \Sigma_\sigma\cap\Sigma_\tau\cong S^{n-1},
   \]
   and this intersection is smoothly isotopic inside \(\Sigma_\sigma\cong S^n\) to an equator.
3. If the family is in the real-projective alternative, then
   \[
   \Sigma_\sigma\cap\Sigma_\tau\cong \mathbb{RP}^{\,n-1},
   \]
   and this intersection is smoothly isotopic inside
   \(\Sigma_\sigma\cong\mathbb{RP}^{\,n}\) to a projective hyperplane.

More globally, for fixed \(\sigma\) define
\[
\mathcal I_\sigma=
\{(x,\tau)\in \Sigma_\sigma\times(P\setminus\{\sigma\}):
x\in\Sigma_\tau\}.
\]
The projection
\[
\pi_\sigma:\mathcal I_\sigma\longrightarrow P\setminus\{\sigma\},
\qquad (x,\tau)\longmapsto\tau,
\]
is a proper surjective smooth submersion. Hence it is a smooth locally trivial fiber bundle. Its fiber is \(S^{n-1}\) in the spherical case and
\(\mathbb{RP}^{\,n-1}\) in the projective case.

Consequently, in a hypersurface Zoll manifold of dimension \(n+1\ge3\), every two distinct Zoll minimal hypersurfaces meet transversely in one connected standard codimension-two submanifold. In dimension three, every two distinct Zoll minimal surfaces meet in exactly one embedded circle.

The theorem is purely differential-topological: minimality is needed only for the Zoll corollary, not for the incidence statement.

## Proof

### 1. Distinct members are automatically transverse wherever they meet

Suppose \(x\in\Sigma_\sigma\cap\Sigma_\tau\) and the two tangent hyperplanes agree:
\[
T_x\Sigma_\sigma=T_x\Sigma_\tau=\Pi.
\]
By the defining uniqueness property of an unoriented transitive family, there is exactly one member whose Legendrian lift contains \((x,\Pi)\). Therefore \(\sigma=\tau\). Hence distinct members can never be tangent at an intersection.

### 2. The infinitesimal family gives a complete first-jet system

Fix \(\sigma\) and write \(\Sigma=\Sigma_\sigma\). The double-fibration description of a transitive family identifies every
\(\zeta\in T_\sigma P\) with a normal variation section
\[
s_\zeta\in\Gamma(N\Sigma).
\]
At every \(x\in\Sigma\), the map
\[
J_x:T_\sigma P\longrightarrow
N_x\Sigma\oplus (T_x^*\Sigma\otimes N_x\Sigma),
\qquad
\zeta\longmapsto
\bigl(s_\zeta(x),\nabla s_\zeta(x)\bigr)
\tag{1}
\]
is an isomorphism.

This can be seen directly from the transitive-family local product structure. In local graph coordinates around \((x,T_x\Sigma)\) in the hyperplane Grassmann bundle, a nearby hypersurface is determined to first order transverse to the reference Legendrian leaf by its normal height and its tangent-hyperplane variation, i.e. by the value and differential of its normal graphing section. Both sides of (1) have dimension \(n+1\), and the uniqueness of the leaf through a point-hyperplane pair makes this first-jet map nonsingular.

In particular, for every nonzero \(\zeta\), the section \(s_\zeta\) is transverse to the zero section: if both \(s_\zeta(x)\) and \(\nabla s_\zeta(x)\) vanished, (1) would imply \(\zeta=0\).

### 3. The nearby intersection is a standard hyperplane section

First assume \(N\Sigma\) is trivial. Choose a unit normal \(\nu\), a basis
\(\zeta_0,\ldots,\zeta_n\) of \(T_\sigma P\), and write
\[
s_{\zeta_i}=f_i\nu.
\]
Set
\[
F=(f_0,\ldots,f_n):\Sigma\to\mathbb R^{n+1},
\qquad
\Psi=\frac{F}{|F|}:\Sigma\to S^n.
\]
The first-jet isomorphism (1) implies that \(F\) never vanishes and that
\(d\Psi\) has rank \(n\) everywhere. Thus \(\Psi\) is a local diffeomorphism.
By Martins' topological classification, in the two-sided case
\(\Sigma\cong S^n\). Since \(n\ge2\), compactness and simple connectedness of
\(S^n\) imply that \(\Psi\) is a diffeomorphism.

For
\[
\zeta=\sum_{i=0}^n a_i\zeta_i\ne0,
\]
the zero set of \(s_\zeta\) is therefore
\[
\Psi^{-1}\{y\in S^n:\langle a,y\rangle=0\}\cong S^{n-1}.
\tag{2}
\]
Moreover it is smoothly isotopic in \(\Sigma\) to an equator.

Now suppose \(N\Sigma\) is nontrivial. Its unit-normal cover
\(q:\widetilde\Sigma\to\Sigma\) is the connected double cover. In the
projective alternative, \(\Sigma\cong\mathbb{RP}^n\), so
\(\widetilde\Sigma\cong S^n\). Trivialize \(q^*N\Sigma\) by the tautological
unit normal \(\nu\) and write
\[
q^*s_{\zeta_i}=f_i\nu.
\]
The same first-jet argument gives a diffeomorphism
\(\Psi:\widetilde\Sigma\to S^n\). The deck involution reverses \(\nu\), hence
\[
f_i\circ\iota=-f_i,\qquad
\Psi\circ\iota=-\Psi.
\]
Thus \(\Psi\) descends to a diffeomorphism
\[
\bar\Psi:\Sigma\longrightarrow\mathbb{RP}^n.
\]
For every nonzero \(\zeta\), the zero set of \(s_\zeta\) is the quotient of a
great \(S^{n-1}\) by the antipodal map, so
\[
s_\zeta^{-1}(0)\cong\mathbb{RP}^{\,n-1},
\tag{3}
\]
isotopic to a projective hyperplane.

Choose a smooth curve \(\tau(t)\) in \(P\) with
\(\tau(0)=\sigma\) and \(\tau'(0)=\zeta\ne0\). In a tubular neighborhood of
\(\Sigma\), the nearby member \(\Sigma_{\tau(t)}\) is the normal graph of a
section \(u_t\) with
\[
u_0=0,\qquad
t^{-1}u_t\longrightarrow s_\zeta
\quad\text{in }C^1.
\]
Because \(s_\zeta\) is transverse to the zero section, the implicit function
theorem implies that, for all sufficiently small nonzero \(t\),
\[
\Sigma\cap\Sigma_{\tau(t)}=u_t^{-1}(0)
\]
is a smooth submanifold isotopic to the zero set in (2) or (3). Thus at least
one nearby parameter gives a nonempty standard intersection.

### 4. The total pair-incidence relation is a proper submersion

Let
\[
\mathcal U=\{(x,\tau)\in M\times P:x\in\Sigma_\tau\}
\]
be the universal incidence hypersurface. The local triviality in the
definition of a transitive family makes \(\mathcal U\) smooth. By Step 1,
for every \(\tau\ne\sigma\), \(\Sigma_\tau\) is transverse to
\(\Sigma_\sigma\) at every common point. Hence
\[
\mathcal I_\sigma=
\mathcal U\cap
\bigl(\Sigma_\sigma\times(P\setminus\{\sigma\})\bigr)
\]
is smooth, and the projection
\(\pi_\sigma:\mathcal I_\sigma\to P\setminus\{\sigma\}\) is a submersion.
Indeed, in a local defining equation for \(\Sigma_\tau\), transversality says
that the derivative in the \(\Sigma_\sigma\)-direction is nonzero, which
allows one to solve for the single incidence equation for an arbitrary
parameter velocity.

The map \(\pi_\sigma\) is proper. If
\(K\subset P\setminus\{\sigma\}\) is compact, the universal family over \(K\)
is a compact fiber bundle because its fibers are the closed hypersurfaces
\(\Sigma_\tau\); hence
\(\pi_\sigma^{-1}(K)\) is closed in a compact set.

A submersion has open image and a proper map has closed image. The parameter
space \(P\) is a connected smooth manifold of dimension \(n+1\), so
\(P\setminus\{\sigma\}\) is connected for \(n\ge2\). Step 3 shows that the
image of \(\pi_\sigma\) is nonempty. Therefore
\[
\pi_\sigma(\mathcal I_\sigma)=P\setminus\{\sigma\}.
\]
This proves that every distinct pair intersects.

By Ehresmann's theorem, the proper surjective submersion \(\pi_\sigma\) is a
smooth locally trivial bundle. Since its base is connected, all fibers are
diffeomorphic to the nearby standard fiber from Step 3. Pulling the bundle
back along a path in \(P\setminus\{\sigma\}\) also gives an isotopy of the
fibers inside \(\Sigma_\sigma\). This proves all assertions.

## Context and originality boundary

Martins proved that a smooth manifold admitting an unoriented transitive
family of closed embedded hypersurfaces is diffeomorphic to a sphere or a
real projective space, with members diffeomorphic respectively to spheres or
projective spaces, and developed the double-fibration and normal-variation
machinery used above. A hypersurface Zoll family is an unoriented transitive
family whose members are minimal.

The new point here is the global **pairwise incidence** conclusion. The
topology of each individual member does not by itself control how two
embedded members meet: arbitrary embedded spheres or projective
hypersurfaces can have disconnected or otherwise nonstandard intersections.
The argument combines the first-jet rigidity of the transitive family near
one parameter with a proper-submersion continuation over the punctured
parameter space, ruling out both disjoint pairs and topology changes in the
pairwise intersection.

To the best of our knowledge, searches for pairwise intersections, incidence
bundles, transverse intersections, and equivalent formulations for
hypersurface Zoll/transitive families did not locate this theorem. The
closest current sources classify the ambient and member topology or construct
Zoll families. The motivating Martins preprint is extremely recent, so a
later revision or an unindexed parallel observation remains a genuine
originality risk.

## Limitations

- The statement assumes an **unoriented** transitive family of **closed embedded**
  hypersurfaces and \(n\ge2\). It does not apply to arbitrary oriented
  transitive families; for example, standard oriented families such as small
  geodesic spheres can have disjoint members.
- The result is pairwise only. No claim is made about simultaneous
  intersections of three or more family members.
- No quantitative lower bound for intersection angles or other metric
  stability estimate is obtained.
- The theorem classifies the topology and isotopy type of pair intersections,
  not their intrinsic or extrinsic geometry.
- The low-dimensional \(n=1\) case is not included here.

## References

1. G. Martins, *Topological and spectral rigidity of hypersurface Zoll manifolds*, arXiv:2609.20689v1 (2026). https://arxiv.org/abs/2609.20689
2. L. Ambrozio, F. C. Marques, A. Neves, *Riemannian metrics on the sphere with Zoll families of minimal hypersurfaces*, J. Differential Geom. (2025), arXiv:2112.01448. https://arxiv.org/abs/2112.01448
3. L. Ambrozio, D. Guajardo, *Equivariant constructions of spheres with Zoll families of minimal spheres*, Adv. Math. (2026), arXiv:2501.16032. https://arxiv.org/abs/2501.16032
4. J. A. Gálvez, P. Mira, *Uniqueness of immersed spheres in three-manifolds*, J. Differential Geom. 116 (2020), arXiv:1603.07153. https://arxiv.org/abs/1603.07153
