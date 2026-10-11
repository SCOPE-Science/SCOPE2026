# An infinite fixed-square Weyl orbit of irrational Seshadri classes on \(X_9\)
## Finding
Let
\[
X=\operatorname{Bl}_{p_1,\ldots,p_9}\mathbf P^2
\]
be the blow-up at a very general ordered nine-tuple, with \(H\) the pullback of a line and \(E_i\) the exceptional classes. There is a very general point \(x\in X\) such that, for every integer \(m\ge0\),
\[
\begin{aligned}
L_m={}&(9+12m^2)H-(4m^2-4m+3)E_1-(4m^2+4m+3)E_2\\
&-(4m^2+3)(E_3+E_4+E_5)-(4m^2+2)(E_6+E_7+E_8+E_9)
\end{aligned}
\]
is a primitive ample divisor with
\[
L_m^2=20,
\qquad
\varepsilon(L_m;x)=2\sqrt5=\sqrt{L_m^2}.
\]
The classes are pairwise distinct, and their degrees in the original plane marking satisfy
\[
H\cdot L_m=9+12m^2\longrightarrow\infty.
\]

Thus the irrational Seshadri constant constructed by Laface--Ugaglia is not confined to one polarization: on one fixed very general nine-point blow-up, and simultaneously at one common very general point, it propagates along an explicit infinite affine-Weyl orbit of primitive polarizations having the same self-intersection.

## Assumptions and scope
All varieties are over \(\mathbf C\). “Very general” means outside a countable union of proper closed subsets of the relevant irreducible parameter space.

The initiating result of Laface--Ugaglia is the following. For a very general ordered nine-point blow-up
\[
X_9=\operatorname{Bl}_{p_1,\ldots,p_9}\mathbf P^2,
\]
the divisor
\[
L=9H-3(E_1+\cdots+E_5)-2(E_6+\cdots+E_9)
\]
is ample and satisfies
\[
\varepsilon(L;y)=2\sqrt5
\]
at a very general point \(y\in X_9\).

We use the standard affine Weyl action on the Picard lattice of a nine-point plane blow-up. Put
\[
\delta=3H-E_1-\cdots-E_9,
\qquad
\alpha=E_1-E_2.
\]
Then \(\delta\) is the null anticanonical root and \(\alpha^2=-2\), \(\alpha\cdot\delta=0\). Let \(T_\alpha\) be the affine Weyl translation associated with \(\alpha\).

The conclusion is simultaneous in all \(m\ge0\). No assertion is made for every point of \(X\); the common evaluation point is very general.

## Proof
Use the intersection convention
\[
H^2=1,
\qquad
E_i^2=-1,
\qquad
H\cdot E_i=E_i\cdot E_j=0\quad(i\ne j).
\]
For the Laface--Ugaglia class \(L\), direct calculation gives
\[
L\cdot\delta=4,
\qquad
L\cdot\alpha=0.
\]
The Kac formula for the affine Weyl translation is
\[
T_\alpha(\lambda)
=
\lambda+(\lambda\cdot\delta)\alpha
-
\left(
\frac12(\lambda\cdot\delta)\alpha^2+\lambda\cdot\alpha
\right)\delta.
\]
Since \(\alpha^2=-2\), it follows that
\[
T_\alpha(L)=L+4\alpha+4\delta.
\]
Also \(T_\alpha(\delta)=\delta\) and
\[
T_\alpha(\alpha)=\alpha+2\delta.
\]
Induction therefore gives
\[
T_\alpha^m(L)=L+4m\alpha+4m^2\delta
\qquad(m\ge0).
\]
Expanding this expression in the basis \(H,E_1,\ldots,E_9\) is exactly the displayed formula for \(L_m\).

The Weyl translation \(T_\alpha^m\) is an integral lattice automorphism. Hence it preserves primitivity and the intersection form. Since \(L\) is primitive and
\[
L^2=81-5\cdot9-4\cdot4=20,
\]
we obtain
\[
L_m^2=20
\]
for all \(m\). The coefficient of \(H\) is \(9+12m^2\), which is strictly increasing for \(m\ge0\), so the \(L_m\) are pairwise distinct.

It remains to establish ampleness and the Seshadri value on one fixed surface, not merely on a varying family. Standard Cremona transformations and permutations generate the affine Weyl action on the marked Picard lattice of a nine-point blow-up. Very general ordered nine-tuples are in Cremona general position, so every finite Weyl word is valid. On surfaces, the resulting pseudo-isomorphisms are actual isomorphisms between the corresponding blow-ups.

Let \(U\) be the ordered nine-point configuration space. Laface--Ugaglia's theorem holds on a very general subset \(U_{\mathrm{LU}}\subset U\). For each \(m\), choose a finite Cremona word representing the Weyl element whose pullback action is \(T_\alpha^m\); it defines a birational self-map \(w_m\) of the configuration space on a dense open set. The conditions
\[
p\in\operatorname{Dom}(w_m),
\qquad
w_m(p)\in U_{\mathrm{LU}}
\]
exclude only a countable union of proper closed subsets when imposed for all \(m\ge0\). Choose a very general configuration \(p\) satisfying them simultaneously.

Write \(X=X_p\) and \(X_m=X_{w_m(p)}\). The lifted Cremona word is an isomorphism
\[
f_m:X\longrightarrow X_m
\]
whose pullback sends the Laface--Ugaglia divisor on \(X_m\) to \(L_m\). Since the target divisor is ample, \(L_m\) is ample on \(X\).

For each \(m\), Laface--Ugaglia's equality holds on a very general subset \(V_m\subset X_m\). Hence
\[
f_m^{-1}(V_m)\subset X
\]
is very general. The intersection
\[
\bigcap_{m\ge0}f_m^{-1}(V_m)
\]
is again very general because only countably many proper closed exceptional loci are removed. Choose \(x\) in this intersection. Isomorphism invariance of Seshadri constants gives, simultaneously for every \(m\),
\[
\varepsilon(L_m;x)
=
\varepsilon(L;f_m(x))
=2\sqrt5.
\]
Since \(L_m^2=20\), this equals the volume bound \(\sqrt{L_m^2}\), completing the proof.

## Verification
The accompanying `verify.py` checks the lattice arithmetic independently from the prose proof. It verifies the intersection form, the Kac translation and its inverse on the full basis, the closed formula
\[
T_\alpha^m(L)=L+4m\alpha+4m^2\delta,
\]
the displayed coefficients of \(L_m\), the identities
\[
L_m^2=20,
\qquad
L_m\cdot\delta=4,
\]
and the increasing plane degree \(9+12m^2\) over a finite replay range.

The finite replay is not used as a proof of the universal statement in \(m\). The universal formula is proved symbolically by induction in the preceding section. The checker also confirms that the integral translation has an integral inverse, matching the primitivity argument.

The saved output ends in `VERIFY_OK`.

## Relationship to prior work
Laface--Ugaglia prove the single explicit ample class
\[
L=9H-3(E_1+\cdots+E_5)-2(E_6+\cdots+E_9)
\]
on the very general nine-point blow-up and compute its maximal irrational Seshadri constant \(2\sqrt5\). Their paper does not formulate an affine-Weyl orbit of this class; targeted full-text checks found no discussion under “Weyl” or “infinitely”.

Alonso--Suris record the affine \(E_8^{(1)}\) Picard-lattice action for a plane blown up at nine points and the Kac formula for translations. Their work concerns birational dynamics and does not study Seshadri constants or the Laface--Ugaglia polarization.

Totaro explains that very general point configurations are in Cremona general position and that repeated standard Cremona transformations give new blow-up presentations of the same surface; in dimension two the relevant pseudo-isomorphisms are isomorphisms. This supplies the geometric passage from the lattice orbit to actual ample classes on one fixed surface, but does not contain the Seshadri calculation.

A subsequent paper by Malara--Merta--Szpond--Zieliński, first posted after the source window of the initiating result, produces an infinite series of irrational Seshadri constants by varying an odd parameter and, for the new cases, the number of blown-up points. Its first new plane case is a ten-point blow-up. It does not state the fixed-surface, fixed-square Weyl orbit above; targeted full-text checks found no “Weyl” or “same surface” formulation.

Targeted searches for the explicit coefficient sequence \(9+12m^2\), an infinite family of primitive square-
\(20\) ample classes with Seshadri constant \(2\sqrt5\), and equivalent fixed-surface Weyl-orbit formulations located no covering statement.

## Limitations
The finding concerns one explicit affine-Weyl orbit. It does not classify all primitive ample classes of square \(20\) on a very general nine-point blow-up, nor all classes attaining their volume-bound Seshadri constant.

The common point \(x\) is very general; no claim is made about a prescribed point, every point, or an effective description of the exceptional locus.

The proof uses the standard realization of affine-Weyl words by Cremona transformations on very general point configurations. It does not claim that the corresponding lattice translations arise from automorphisms preserving a fixed plane marking.

The most relevant later preprint appeared after the initiating source window and was nevertheless inspected for coverage. Because the topic is extremely recent, an unindexed note or an unstated immediate corollary observed independently by others remains a residual originality risk.

## References
1. A. Laface and L. Ugaglia, *Irrational Seshadri constants from dihedral orbits*, arXiv:2609.26521v2, 2026.
2. J. Alonso and Y. B. Suris, *Geometry of autonomous discrete Painlevé equations related to the Weyl group \(W(E_8^{(1)})\)*, arXiv:2512.18288, 2025.
3. B. Totaro, *Hilbert's 14th problem over finite fields and a conjecture on the cone of curves*, Compositio Mathematica 144 (2008), 1176--1198.
4. G. Malara, Ł. Merta, J. Szpond, and M. Zieliński, *Dihedral reflections and an infinite series of irrational Seshadri constants*, arXiv:2610.01783v1, 2026.
