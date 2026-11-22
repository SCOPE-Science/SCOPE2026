# Full symmetric singular-fiber monodromy for index-three K3 genus-one pencils

## Finding

Let \(V=H^0(\mathbb P^2_{\mathbb C},\mathcal O(3))\), and let \(\mathcal U\) be the nonempty Zariski-open locus of triples \((F,G,H)\in V^3\) for which
\[
S_{F,G,H}=\{s^2F(x)+2stG(x)+t^2H(x)=0\}\subset \mathbb P^1_{[s:t]}\times\mathbb P^2_x
\]
is smooth and the projection \(\pi:S_{F,G,H}\to\mathbb P^1\) has only distinct, irreducible nodal singular fibers. The locus \(\mathcal U\) exists by the proof below. On every member of \(\mathcal U\), the fibration has exactly \(24\) singular fibers, all of Kodaira type \(I_1\). The finite étale degree-\(24\) cover of \(\mathcal U\) whose points mark one singular-fiber parameter has **geometric monodromy group \(S_{24}\)**. Equivalently, for \(30\) algebraically independent rational coefficients of \(F,G,H\), the degree-\(24\) binary polynomial
\[
D_{F,G,H}(s,t)=\operatorname{Disc}_{\mathbb P^2}(s^2F+2stG+t^2H)
\]
has splitting-field Galois group \(S_{24}\) over their rational-function field. Here the ternary-cubic discriminant is taken with its ordinary reduced normalization; nonzero scalar multiples have the same roots and group.

For a *very general* such surface, \(\operatorname{Pic}(S)=\mathbb Z e\oplus\mathbb Z h\), with Gram matrix \(\bigl(\begin{smallmatrix}0&3\\3&2\end{smallmatrix}\bigr)\). Both nef isotropic classes \(e\) and \(e'=3h-e\) define genus-one pencils of **index exactly \(3\)** (hence without a section). The degree-two covering involution associated with \(h\) exchanges these pencils; consequently the second pencil also has \(24\) irreducible nodal fibers and geometric permutation monodromy \(S_{24}\) in this same coefficient family. Monodromy here means permutation of the exceptional *base parameters as the coefficients vary*, not homological monodromy of an individual elliptic curve.

## Assumptions and scope

The ground field is \(\mathbb C\) for geometric monodromy; the coefficient-field Galois statement is over \(\mathbb Q\) with \(30\) independent indeterminates. A point of \(\mathcal U\) specifies an embedded smooth bidegree-\((2,3)\) K3 surface. The Picard and exact-index assertions require *very general* coefficients, i.e. exclusion of the countably many Noether–Lefschetz loci; they are not claimed for every point of \(\mathcal U\). The degree-\(24\) cover is defined after deleting the root-collision discriminant from the coefficient space.

## Proof

**1. Degree, existence and node type.** The hypersurface \(\Delta\subset\mathbb P(V)\) of singular ternary cubics is irreducible and has degree \(12\). This degree is the standard plane-cubic discriminant degree \(3(3-1)^2\). For a triple with linearly independent \(F,G,H\), the map
\[
\nu_{F,G,H}:\mathbb P^1\longrightarrow\mathbb P(V),\qquad [s:t]\longmapsto[s^2F+2stG+t^2H]
\]
is a quadratic Veronese conic in the plane spanned by \(F,G,H\); hence \(\deg\nu^*\Delta=2\cdot12=24\). A general triple is transverse to the smooth locus of \(\Delta\) and avoids its singular locus: for fixed \([s:t]\), the evaluation \(V^3\to V\) is surjective, while varying \((F,G,H)\) independently controls its first derivative in the parameter. The singular locus of \(\Delta\) has codimension at least two (cubics with worse than one ordinary node). The incidence dimension estimate plus generic smoothness/Bertini therefore give \(24\) simple discriminant roots, each corresponding to an irreducible plane cubic with one ordinary node. Bertini for the basepoint-free ample linear system \(\mathcal O(2,3)\) ensures that the total K3 surface is smooth simultaneously. Adjunction shows \(K_S=0\), and weak Lefschetz gives \(H^1(S,\mathcal O_S)=0\).

**2. Irreducibility of marked-incidence spaces.** Put \(P=V^3\), and for \(q=([s:t],x)\in\mathbb P^1\times\mathbb P^2\), consider the linear conditions
\[
\partial_{x_0}(s^2F+2stG+t^2H)(x)
=\partial_{x_1}(s^2F+2stG+t^2H)(x)
=\partial_{x_2}(s^2F+2stG+t^2H)(x)=0.
\]
These are three independent linear conditions: evaluation to a cubic at a chosen base parameter is surjective, and cubic first jets at a projective point can be prescribed independently. By Euler's identity they include the equation that the cubic vanishes at \(x\). Thus the universal singular-point incidence \(I_1\to\mathbb P^1\times\mathbb P^2\) is a rank-\(27\) vector bundle and is irreducible. Above \(\mathcal U\), a singular cubic has a unique node, so \(I_1|_{\mathcal U}\to\mathcal U\) is exactly the degree-\(24\) root cover; its irreducibility gives transitivity.

For *ordered pairs* with distinct parameters \([s:t]\ne[s':t']\), the map \(V^3\to V\oplus V\) evaluating the quadratic binary form at those two parameters is surjective: quadratic forms on \(\mathbb P^1\) separate any pair of points. The two independent sets of three cubic first-jet equations therefore define a rank-\(24\) vector bundle over the irreducible open subset of \((\mathbb P^1\times\mathbb P^2)^2\) where the base parameters differ. Restricting to \(\mathcal U\) gives the ordered-distinct-root cover of degree \(24\cdot23\), which is irreducible. Therefore the permutation group is doubly transitive.

**3. A simple transposition.** Consider \([s:t]=[1:0]\) and \(x=[1:0:0]\). Choose \(F\) with one ordinary node at \(x\) and otherwise general, and impose \(G(x)=0\); these are independent linear conditions on \((F,G,H)\). In affine local coordinates \(\tau=t/s\) and \(y=(y_1,y_2)\), write
\[
F=q(y)+O(|y|^3),\qquad G=b\cdot y+O(|y|^2),\qquad H=h_0+O(|y|),
\]
where \(q\) is a nonsingular binary quadratic. Solving the two critical-point equations in \(y\) gives an analytic critical branch \(y(\tau)=O(\tau)\). Its critical value is \(\kappa\tau^2+O(\tau^3)\), where \(\kappa=h_0-q^*(b)\) and \(q^*(b)\) is the quadratic form obtained by completing the square. Since \(H(x)\) is freely variable, choose \(\kappa\ne0\). Vary \(F(x)\) by a transverse scalar \(\varepsilon\): the critical-value function becomes
\[
\varepsilon+\kappa\tau^2+\text{higher terms},
\]
which has two simple roots permuted by a loop around \(\varepsilon=0\). General choices under these constraints keep the other \(22\) roots simple: away from \(\tau=0\), the coefficient of \(H\) in the cubic is nonzero, so first jets remain freely variable, and the failure-of-transversality and second-collision loci are proper closed conditions. The nearby \(\varepsilon\ne0\) choices lie in the smooth-total-space open locus; hence the monodromy contains an ordinary transposition.

**4. Full group and arithmetic conclusion.** A doubly transitive subgroup of \(S_{24}\) containing a transposition is all of \(S_{24}\): conjugates of the transposition give every two-cycle. The incidence cover and its equations are defined over \(\mathbb Q\). Its arithmetic Galois group on the \(24\) discriminant roots contains the full geometric group \(S_{24}\) and embeds in \(S_{24}\), so it is \(S_{24}\) as claimed.

**5. The index-three companion pencils.** The class \(e=\mathcal O_S(1,0)\) satisfies \(e^2=0\), while \(h=\mathcal O_S(0,1)\) satisfies \(h^2=2\) and \(e\cdot h=3\), by intersections in \(\mathbb P^1\times\mathbb P^2\). For very general \(S\), the full Picard lattice is generated by \(e,h\), a fact established for the relevant rank-two K3 family in Galluzzi–van Geemen, §3.3 (and its cited lattice reference). Consequently every divisor has fiber degree divisible by \(3\), while \(h\) has fiber degree exactly \(3\). The multisection index is therefore exactly \(3\). The second nef primitive isotropic class \(e'=3h-e\) also pairs with \(h\) to degree \(3\), and every divisor meets it with degree divisible by \(3\). Galluzzi–van Geemen identify the double-plane involution as interchanging \(e,e'\). It conjugates the two fibration maps on each surface (up to their base identifications), so their singular-fiber counts and monodromy groups agree.

## Verification

A standalone arithmetic-and-local-model checker verifies the intersection matrix, the two primitive isotropic rays, the index gcds, the binary conic evaluation rank, the formula \(2\deg\Delta=24\), and a transverse local Morse model \(y_1^2+y_2^2+2\tau y_1+2\tau^2+\varepsilon\), whose critical value is \(\varepsilon+\tau^2\). It does **not** substitute finite examples for the universal incidence and monodromy arguments above. Run \(\texttt{python verify.py}\) using SymPy.

## Relationship to prior work

Galluzzi–van Geemen, arXiv:2611.15908v1, §3.3, give the bidegree-\((2,3)\) embedding, rank-two Picard lattice and two genus-one pencils, but do not compute the permutation Galois group of the \(24\) singular-fiber parameters. Zhan, arXiv:2004.08719, Theorem 1.1 and §2, proves \(S_{24}\) for the *universal Weierstrass family with a section*, not the bidegree-\((2,3)\) family of index-three torsors and its restricted discriminant cover. The Harris double-transitivity/transposition framework, as surveyed by Sottile–Yahl, is a general method; the incidence and collision hypotheses for this quadratic cubic-plane family are proved here. The number \(24\) alone is classical K3 Euler-number geometry and is not claimed as original.

## Limitations

The result concerns the geometric *coefficient-family* permutation group, not the \(\mathrm{SL}_2(\mathbb Z)\) homological monodromy on an individual genus-one fiber. It does not assert that every smooth bidegree-\((2,3)\) surface has Picard rank two or only nodal fibers, nor does it compute the integral Brauer class of the torsor. Arithmetic specializations can have smaller Galois groups. Generic-enumerative-monodromy principles are classical and could furnish an alternative proof; no absolute priority is asserted without exhaustive historical checking.

## References

1. Federica Galluzzi and Bert van Geemen, *Some families of birational cubic and Verra fourfolds*, arXiv:2611.15908v1 (first available 2026-11-11), §3.3, https://arxiv.org/html/2611.15908v1.
2. Sailun Zhan, *Monodromy of rational curves on K3 surfaces of low genus*, arXiv:2004.08719, Theorem 1.1 and §2, https://arxiv.org/abs/2004.08719.
3. Frank Sottile and Thomas Yahl, *Galois Groups in Enumerative Geometry and Applications*, arXiv:2108.07905v2, §1, https://arxiv.org/html/2108.07905v2.
4. Jonas Baltes, *Singular rational curves on elliptic K3 surfaces*, Math. Nachr. 296 (2023), §2.3, https://doi.org/10.1002/mana.202200228.
