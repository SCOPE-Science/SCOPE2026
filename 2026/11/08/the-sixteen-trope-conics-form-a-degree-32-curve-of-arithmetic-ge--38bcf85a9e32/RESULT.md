# The sixteen trope conics form a degree-32 curve of arithmetic genus 129

## Finding
Let \(K\subset\mathbb P^3_{\mathbb C}\) be the classical Kummer quartic of a smooth genus-two Jacobian, with sixteen ordinary nodes. Let \(D\subset K\) be the **reduced** union of its sixteen smooth trope conics. Then \(D\) is a connected Cartier divisor of degree \(32\), and its singular locus consists of the sixteen Kummer nodes. At each node exactly six smooth branches of \(D\) pass through, with six distinct tangent directions lying on the smooth projectivized quadratic tangent cone. Each such *spatial*, non-planar six-branch singularity has normalization delta invariant \(9\), rather than the delta \(15\) of an ordinary plane sextuple point. Consequently
\[
\deg D=32,\qquad \delta_P(D)=9\text{ for every node }P,\qquad p_a(D)=129.
\]
The claim is about the reduced union, not the nonreduced Cartier sum of the sixteen doubled trope-plane sections.

## Assumptions and scope
The base field is \(\mathbb C\). Each trope plane \(H_i\) cuts \(K\) along the doubled smooth conic \(2C_i\). There are sixteen distinct nodes and conics, exactly six conics through each node, and two different trope planes share exactly two nodes (Böhning–Graf von Bothmer, Definition 4.10 and Remark 4.11, which quote classical Kummer geometry). Put \(D=(\bigcup_i C_i)_{\mathrm{red}}\).

## Proof
**1. Only the nodes are intersections.** Distinct trope planes meet in a line containing exactly two Kummer nodes. Since each trope conic lies in its own plane and contains the six designated nodes, two distinct conics share those two nodes and no additional point. Their individual smoothness is classical. Every node lies on six of the conics, hence is singular in \(D\); there are no other singularities. Each conic is irreducible of degree two, so \(\deg D=16\cdot2=32\). The 16 components intersect, so \(D\) is connected.

**2. Six distinct tangent directions.** At a Kummer node \(P\), the quadratic leading part \(q\) of a local equation of \(K\) has rank three, so the projectivized tangent cone \(q=0\) is a smooth conic in \(\mathbb P(T_P\mathbb P^3)\). A trope plane through \(P\) cuts \(K\) as twice its smooth trope conic. Accordingly, its linear tangent plane restricts \(q\) to a square and is tangent to this projective conic. The branch tangent direction is the point of tangency. Two distinct trope planes through \(P\) yield distinct tangent lines to \(q=0\), hence distinct points of tangency. They therefore give six smooth branches with distinct directions on the smooth conic.

**3. Local delta is nine.** Let \(\widehat{\mathcal O}\) be the completed local ring of \(D\) at a node, and let its normalization be the product of six one-variable power-series rings. The leading-direction evaluation maps on homogeneous polynomials of degrees \(j=0,1,2,3\) have respective ranks \(1,3,5,6\). Indeed the six distinct directions lie on a smooth conic; restrictions of linear, quadratic and cubic forms have dimensions \(3,5,7\), and six distinct points on \(\mathbb P^1\) impose independent conditions on polynomials of degree at least five. For degree two, the only quadric vanishing on all six conic points is the defining quadric, which accounts for rank five. Because the degree-one evaluation has full rank three, no lower-degree term can cancel its first-order jets. More generally the associated graded map from the local ring into its normalized branches has ranks \(1,3,5,6,6,\ldots\) in successive orders: surjectivity in degree three lifts recursively to all higher orders. Therefore
\[
\delta_P(D)=\dim_{\mathbb C}(\widetilde{\mathcal O}/\widehat{\mathcal O})
=(6-1)+(6-3)+(6-5)=9.
\]
This argument uses only the six distinct tangent directions on a nonsingular conic; it does not identify the full analytic germ with its tangent cone.

**4. Arithmetic genus.** The normalization is the disjoint union of sixteen smooth conics, each isomorphic to \(\mathbb P^1\). The normalization exact sequence gives
\[
\chi(\mathcal O_D)=16-\sum_{P\in\operatorname{Sing}D}\delta_P
=16-16\cdot9=-128.
\]
Thus \(p_a(D)=1-\chi(\mathcal O_D)=129\).

**5. Independent Cartier intersection check.** The local divisor class group of a complex ordinary surface double point is \(\mathbb Z/2\), and each smooth trope branch through a node represents its nontrivial class (it meets the exceptional curve once on the minimal resolution). Six branches sum to class zero, so \(D\) is Cartier at every node, and it is Cartier elsewhere on the smooth locus. Every trope plane satisfies \(2C_i\sim H\) as Weil divisors, where \(H\) is a hyperplane section. Hence \(2D\sim16H\), \(D^2=(8H)^2=256\) and adjunction/Riemann–Roch for the Gorenstein quartic with rational double points gives \(p_a(D)=1+D^2/2=129\), independently confirming the local calculation.

## Verification
The standalone `verify_genus.py` uses exact modular linear algebra to check a sample of six points on a smooth conic: the leading-form evaluation ranks are \((1,3,5,6)\). It also checks the displayed delta/genus arithmetic. The universal rank statements follow from interpolation on \(\mathbb P^1\), not from the sample.

## Relationship to prior work
Böhning and Graf von Bothmer (arXiv:1704.01807v1, Section 4, Definition 4.10 and Remark 4.11) record the established sixteen trope conics and \((16,6)\) incidence design; the geometric incidence is prior art. Dolgachev (2024) discusses Kummer configurations and the disjoint proper transforms of trope conics on the resolution. Neither inspected source states the **reduced union's local spatial delta invariant** or its arithmetic genus \(129\). The claim is those invariants and their local-to-global compatibility, not the existence or incidence pattern of the trope conics.

## Limitations
This proves a statement over \(\mathbb C\) for smooth genus-two Jacobian Kummer quartics, not all degenerations or characteristics two. The degree, classical incidence pattern and resolution of nodes are known inputs, not new results. The proof does not classify analytic equivalence classes of all six-branch germs or any embedding-dependent syzygy table. A classical source might already imply the arithmetic genus by an unrecorded divisor-class computation; that historical priority uncertainty remains.

## References
1. C. Böhning and H.-C. Graf von Bothmer, *Degenerations of Gushel–Mukai fourfolds, with a view towards irrationality proofs*, arXiv:1704.01807v1 (first public April 6, 2017), Section 4, Definition 4.10 and Remark 4.11; Eur. J. Math. 4 (2018), 802–826, doi:10.1007/s40879-018-0227-z.
2. I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, Bull. Lond. Math. Soc. (2024), section on classical tropes and their proper transforms, doi:10.1112/blms.13033.
3. Classical normal-surface double point and normalization-length formulas; standard local algebra and adjunction/Riemann–Roch for a K3 quartic with rational double points.
