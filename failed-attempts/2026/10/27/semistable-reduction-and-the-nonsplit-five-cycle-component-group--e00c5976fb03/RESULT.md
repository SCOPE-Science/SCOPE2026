# Semistable reduction and the nonsplit five-cycle component group of Bring’s genus-four Jacobian at two

## Finding
Let \(e_j\) be the elementary symmetric polynomial of degree \(j\) in five variables. Over \(\mathbb Q\), let \(C\) be the smooth genus-four complete intersection \(e_1=e_2=e_3=0\) in \(\mathbb P^4\). Write \(\mathscr C\) for the model defined by the same integral equations over \(\mathbb Z_2\). Then \(\mathscr C\) is a **regular proper semistable model**. Its special fiber has two smooth geometric rational components intersecting transversely in five distinct ordinary nodes; every node has smoothing thickness one. Geometric Frobenius fixes the five nodes and exchanges the components.

Let \(J=\operatorname{Jac}(C)\). The identity component of its Néron special fiber is a nonsplit torus of rank four, with Frobenius acting as \(-1\) on the character lattice. The geometric component group is \(\Phi_J(\overline{\mathbb F}_2)\simeq\mathbb Z/5\mathbb Z\), and Frobenius acts by inversion. Therefore
\[
 c_2(J)=\#\Phi_J(\mathbb F_2)=1,\qquad
 c_{2,\mathrm{unr.\,quadratic}}(J)=5,\qquad
 f_2(J)=4.
\]
Here \(c\) denotes a Tamagawa number and \(f_2\) the local Artin conductor exponent of the Jacobian.

## Assumptions and scope
All assertions concern the integral elementary-symmetric complete intersection, **not** an arbitrary model obtained by reducing the power-sum equations at two (whose integral equations differ at even residue characteristic). The surface \(\mathscr C\) has relative dimension one. The finite field \(\mathbb F_4\) is represented by \(\omega^2+\omega+1=0\). The Jacobian is taken over \(\mathbb Q_2\), and component groups are those of its Néron model. The unramified quadratic extension is the degree-two unramified extension of \(\mathbb Q_2\).

## Proof
**1. Geometry of the special fiber.** In the hyperplane \(e_1=0\), the reduction of \(e_2=0\) is a smooth split quadric after extending constants to \(\mathbb F_4\). For example, in five coordinates, take
\[
 E_0=(0,0,1,\omega,\omega^2),\quad E_1=(0,1,1,1,1),\quad
 E_2=(1,0,1,1,1),\quad E_3=(0,0,1,\omega^2,\omega).
\]
These vectors are hyperbolic basis vectors for the quadratic form \(e_2\), with \(e_2(E_0,E_3)=e_2(E_1,E_2)=1\) (polarized form) and all other pairings zero. The Segre parametrization is
\[
 (s:v)\times(t:u)\longmapsto s tE_0+s uE_1+v tE_2+v uE_3.
\]
Direct substitution and calculation in \(\mathbb F_4\) yield
\[
 e_3=(st^2+vu^2)(s^2t+v^2u).
\]
Each factor cuts out a smooth rational bidegree \((1,2)\), respectively \((2,1)\), curve on \(\mathbb P^1\times\mathbb P^1\), and each is embedded as a twisted cubic under the Segre map. Their intersection product is \(1\cdot1+2\cdot2=5\). Direct differentiation of the two factors confirms five reduced transverse intersections; the five points correspond to the permutations of \([0:1:1:1:1]\), all rational over \(\mathbb F_2\). The coefficientwise Frobenius square-map exchanges the two bidegree factors and hence the two components, while fixing the five nodes.

**2. Thickness one and regularity of the total model.** At the special point \([0:1:1:1:1]\), work in the chart where the last coordinate is one, and set
\[
 x_2=1+u,\quad x_3=1+v,\quad x_4=1+w,\quad x_1=-4-u-v-w,\quad x_5=1.
\]
Writing \(q=e_2\) and \(g=e_3\), substitution gives
\[
 q(0,0,w)=-w^2-5w-10,\qquad
 g(0,0,w)=-3w^2-15w-20=3q(0,0,w)+10.
\]
The derivative \(\partial q/\partial w\) is odd at the closed point, so the formal implicit-function theorem solves \(q=0\) for a unique \(w=w(u,v)\) in \(\mathbb Z_2[[u,v]]\) with even constant term. Consequently \(g(0,0,w(0,0))=10\). Because the closed point is an ordinary node of the special fiber, the coefficients of the linear terms in the two remaining parameters are divisible by two. Thus \(g(u,v,w(u,v))\equiv 2\pmod{(2,u,v)^2}\). The equation has a nonzero class in the cotangent space of the regular local three-dimensional ambient \(\mathbb Z_2[[u,v]]\), so its quotient is a regular two-dimensional local ring. Every other node is carried to this one by a permutation of the five coordinates. Away from these five points the special fiber is smooth, so the total model is smooth over \(\mathbb Z_2\) there. The reduced nodal special fiber is nonzero and is a Cartier divisor; flatness follows, and the local equation has thickness one because the total space is regular. Projectivity gives properness.

**3. Néron component group and conductor.** The geometric dual graph has two vertices joined by five parallel edges. Its first homology has rank \(5-2+1=4\). Both components are rational, so the Jacobian has entirely toric semistable reduction of dimension four. The graph Jacobian, equivalently the cokernel of the reduced graph Laplacian \((5)\), is \(\mathbb Z/5\mathbb Z\). Frobenius reverses the two vertices and fixes every edge, hence acts by minus one on graph cycles and on the component group. As two is invertible modulo five, \((\mathbb Z/5\mathbb Z)^{\mathrm{Frob}=1}=0\), which implies \(c_2=1\). Over the unramified quadratic extension Frobenius becomes trivial, so the Tamagawa number becomes five. Finally, the conductor exponent of a semistable Jacobian equals the dimension of its toric part, here four. These are the standard graph-theoretic Néron component-group and semistable conductor formulas.

## Verification
The accompanying standalone `verify.py` recomputes the \(\mathbb F_4\) Segre factorization using exact four-element field arithmetic, counts the five intersections, verifies the local integer identities for \(q\) and \(g\), and checks the Laplacian determinant and Frobenius invariant subgroup. Reproduce using `python3 verify.py`; no external Python dependencies are needed. These finite checks support the explicit geometric computations; regularity and the local Néron conclusion are justified by the arguments above, not by point counts alone.

## Relationship to prior work
The genus-four Bring curve and its classical complex geometry are established in Edge (1978) and Braden–Northover (2012); neither the curve's existence nor its automorphism group is claimed as new. Standard semistable-curve, graph-Jacobian, and Néron-model results supply the passage from a regular thickness-one model to the component group. The present claim concerns the specific integral model at residue characteristic two, its thickness-one local structure and the resulting nonsplit local component-group arithmetic. The later work of Braden–Disney-Hogg (2024) treats other descriptions of Bring's curve, rather than the explicit Néron component calculation asserted here.

## Limitations
This result concerns the chosen integral elementary-symmetric \(\mathbb Z_2\) model and its Jacobian. It does not compute global rational points, a global Mordell–Weil group, or the complete conductor away from two. Known geometric special-fiber decompositions alone do not prove thickness one; the integral local calculation is essential. A previously published equivalent Néron-model calculation under a different integral presentation remains a historical-priority risk. Independent verification has not been performed.

## References
- H. W. Braden and T. P. Northover, *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*, SIGMA **8** (2012), arXiv:1206.6004, DOI 10.3842/SIGMA.2012.065 (first posted 2012-06-26).
- W. L. Edge, *Bring's curve*, J. London Math. Soc. (2) **18** (1978), 539–545, DOI 10.1112/jlms/s2-18.3.539.
- H. W. Braden and L. Disney-Hogg, *Bring's curve: old and new*, European J. Math. **10** (2024), DOI 10.1007/s40879-023-00706-0.
- Bosch, Lütkebohmert and Raynaud, *Néron Models*, Springer (1990): component groups of Jacobians of semistable curves and the graph pairing.
