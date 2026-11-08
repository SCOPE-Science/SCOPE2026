# An optimal linear inequality description of planar vertex-normal cones

## Finding

Let \(N\ge3\), and let \(a_0,\ldots,a_{N-1}\) be distinct unit vectors in the Euclidean plane, indexed by strictly increasing polar angles \(0\le\theta_0<\cdots<\theta_{N-1}<2\pi\). Put \(\theta_N=\theta_0+2\pi\), \(\delta_i=\theta_{i+1}-\theta_i\), with indices cyclically interpreted when appropriate, and consider the closed vertex-normal parameter cone
\[
\mathcal C(a)=\{(x_0,\ldots,x_{N-1})\in(\mathbb R^2)^N:\langle a_i,x_i-x_j\rangle\ge0\text{ for all }i\ne j\}.
\]
The entire quadratic-size defining system is equivalent to an **irredundant linear-size** one, as follows.

If \(\max_i\delta_i<\pi\), retain, for every \(i\) modulo \(N\), just the two inequalities
\[
\langle a_i,x_i-x_{i+1}\rangle\ge0,\qquad
\langle a_{i+1},x_{i+1}-x_i\rangle\ge0.
\]
These are precisely the \(2N\) facets of the full-dimensional cone \(\mathcal C(a)\). In particular, *all other inequalities are redundant simultaneously*, not merely individually.

If \(\max_i\delta_i\ge\pi\), the maximally sized angular gap is unique. Delete the two inequalities across this gap from the preceding cyclic list. The remaining \(2(N-1)\) inequalities describe \(\mathcal C(a)\), all irredundantly and all as facets.

In either case the cone's lineality is exactly the two-dimensional space of common translations \(\{(t,\ldots,t):t\in\mathbb R^2\}\). Thus the complete planar facet count depends only on whether the normals positively span the plane: \(2N\) when they do and \(2N-2\) otherwise.

## Assumptions and scope

The theorem concerns *all* distinct unit vectors in \(\mathbb R^2\), without an equal-spacing assumption, and all real point tuples, including coincident or otherwise degenerate configurations. The gap condition is an exact condition on the chosen cyclic order. Positive spanning is equivalent to \(\max_i\delta_i<\pi\). The cone is the labelled parameter cone for supporting points in the prescribed directions, **not** a deformation cone obtained by varying the support numbers of a fixed normal fan. No analogous claim for dimension three or higher is made.

## Proof

**1. The adjacent pair constrains its edge to a normal-angle wedge.** Let \(J\) be anticlockwise rotation by \(\pi/2\). Whenever \(a_i,a_{i+1}\) are separated by an angle strictly between \(0\) and \(\pi\), put \(d_i=x_{i+1}-x_i\). The two displayed adjacent inequalities mean
\[
\langle a_i,d_i\rangle\le0,\qquad\langle a_{i+1},d_i\rangle\ge0.
\]
Writing \(\gamma_i=\theta_{i+1}-\theta_i\in(0,\pi)\), these are *equivalent* to
\[
d_i=u_iJa_i+v_iJa_{i+1},\quad
u_i=\frac{\langle a_{i+1},d_i\rangle}{\sin\gamma_i}\ge0,
\quad v_i=\frac{-\langle a_i,d_i\rangle}{\sin\gamma_i}\ge0.
\]
Indeed \(\langle a_i,Ja_{i+1}\rangle=-\sin\gamma_i\) and \(\langle a_{i+1},Ja_i\rangle=\sin\gamma_i\). This identity also allows zero-length edges.

**2. Simultaneous implication when every gap is small.** Fix \(i\), and unwrap the cyclic angles along \(\theta_i,\theta_{i+1},\ldots,\theta_i+2\pi\). For the scalar projections \(p_j=\langle a_i,x_j\rangle\) we have
\[
\langle a_i,Ja_k\rangle=-\sin(\theta_k-\theta_i).
\]
Hence along every consecutive edge whose normal angles both lie in the first half-circle \([\theta_i,\theta_i+\pi]\), the projections are nonincreasing. Along every edge whose normal angles both lie in the second half-circle \([\theta_i+\pi,\theta_i+2\pi]\), they are nondecreasing. There is at most one intervening edge straddling the opposite direction, on which no monotonicity is claimed. The first portion starts at \(p_i\); the second ends at the same \(p_i\), because the chain closes. Thus every projection before the straddling edge is at most \(p_i\), and every projection after it is also at most \(p_i\). The endpoints of the straddling edge are covered by one of these conclusions. If a sampled direction equals the opposite direction, split there: the zero sine introduces no difficulty. Consequently \(p_i\ge p_j\) for every \(j\), giving the *entire* original defining system.

**3. Simultaneous implication when one gap is large.** Reindex the vectors so that the unique gap of size at least \(\pi\) lies from \(a_{N-1}\) to \(a_0\). The remaining angles lie in an interval \([\theta_0,\theta_{N-1}]\) of length at most \(\pi\). Apply Step 1 to the \(N-1\) consecutive edges along this interval. For fixed \(i\), the projections \(\langle a_i,x_j\rangle\) are nondecreasing as \(j\) runs from \(0\) to \(i\), and nonincreasing as \(j\) runs from \(i\) to \(N-1\), since all angular differences remain in \([-\pi,\pi]\). Hence their maximum occurs at \(j=i\), proving all inequalities without any condition across the deleted gap. This includes exactly semicircular configurations.

**4. Every retained inequality defines a genuine facet.** First suppose all gaps are below \(\pi\). Fix adjacent indices \(i,i+1\). Choose an auxiliary cyclic list \(b_0,\ldots,b_{N-1}\) of unit normals, in the same order, with every gap below \(\pi\). To isolate the inequality based at \(a_i\), take \(b_i=a_i\) and take each \(b_j\) for \(j\ne i\) at a sufficiently small positive angular displacement from \(a_j\). All \(a_j\), except \(a_i\), then lie in the **interiors** of the angular wedges \((b_{j-1},b_j)\). Instead, to isolate the reverse inequality based at \(a_{i+1}\), take \(b_i=a_{i+1}\) and take each other \(b_j\) just before \(a_{j+1}\). Again all \(a_j\), except the targeted one, are interior to their respective wedges. The displacements can be chosen simultaneously small because the given angular gaps are positive and below \(\pi\).

Define the circumscribed polygon \(K=\bigcap_j\{y:\langle b_j,y\rangle\le1\}\), and let \(z_j\) be the intersection of its two tangent lines with normals \(b_{j-1},b_j\). Every line supports a nondegenerate side of this polygon; each \(z_j\) is a distinct vertex, with normal cone bounded by \(b_{j-1},b_j\). Assign \(x_j=z_j\). Every original defining inequality is then **strict**, except precisely the targeted adjacent inequality: its normal is the one side-normal \(b_i\), and it has equality at \(z_i,z_{i+1}\). Thus that inequality supports a codimension-one face and cannot follow from the other inequalities. Indeed, since the strict inequalities persist under small perturbations and the ambient cone has interior, an arbitrarily small perturbation across the target supporting hyperplane violates only the target inequality.

For the large-gap case, add finitely many *auxiliary* unit normals inside the large empty arc until every augmented angular gap is below \(\pi\). Each retained pair of original consecutive normals remains consecutive in this augmented list. Apply the preceding one-equality construction in the augmented list, then retain only the coordinates labelled by the original normals. This proves irredundancy of every retained original inequality. The two constraints across the large gap are already implied by Step 3, and every other constraint is either retained or implied; hence no other facets are missing.

**5. Dimension and lineality.** The tuple \(x_i=a_i\) makes every original inequality strict, by \(\langle a_i,a_i-a_j\rangle=1-\langle a_i,a_j\rangle>0\) for distinct unit vectors; the cone is full dimensional in \(\mathbb R^{2N}\). Common translations are lineality. Conversely, a lineality vector forces \(\langle a_i,x_i-x_j\rangle=0\) for all \(i,j\). Fix \(j,k\); for every \(i\) this implies \(\langle a_i,x_j-x_k\rangle=0\). Since at least two of the distinct unit vectors are linearly independent when \(N\ge3\), \(x_j=x_k\). This proves the claimed exact lineality. Together with Step 4, the facet count is exact. \(\square\)

## Verification

Run `python verify.py` in an environment with NumPy and SciPy. The verifier builds every original inequality and the theorem's retained subset for prescribed, random and highly nonuniform planar unit-normal sets. It independently solves a bounded linear program for each inequality: a missing inequality must be implied *jointly* by the retained set, while each retained inequality must admit a configuration violating it with every other retained one satisfied. The completed run passed 15,514 linear programs from 378 normal configurations: 4,748 nonredundancy witnesses and 10,766 simultaneous-implication checks. Floating-point LP tolerances are numerical safeguards only. The proof above is valid for all \(N\ge3\) and all admissible directions without numerical assumptions.

## Relationship to prior work

Rieger, *Galerkin approximations to the space of convex bodies by polytopes in nondegenerate V-representation* (first posted August 27, 2026), defines exactly this supporting-point cone and proves geometric properties and specific individually redundant inequalities in Lemmas 22–23. Its Section 5 explicitly distinguishes individual from simultaneous redundancy; it does not state the linear minimal planar description or its two angular cases. Pinelis's 2007 polygon-convexity criteria characterize angle ordering of polygon edges but do not provide this supporting-point parameter-cone facet census. Padrol–Pilaud–Poullot describe adjacent-fan inequalities for *support-height deformation cones* of polytopes; their variable space and normal-fan constraints are different. The present proof uses elementary planar wedge geometry to obtain a simultaneous reduction and a sharp irredundancy certificate. No claim is made that the underlying ordered-edge characterization is new.

## Limitations

The result is planar and assumes pairwise distinct **unit** prescribed normals. Coalescing normals or using higher-dimensional normal configurations can change the minimal inequality system. The prior-literature comparison supports provisional originality of the combined parameter-cone theorem and exact facet census, not exhaustive historical priority; equivalent older descriptions in convex interpolation or fan theory may exist. The numerical verifier is finite and does not certify the unrestricted theorem independently.

## References

1. J. Rieger, *Galerkin approximations to the space of convex bodies by polytopes in nondegenerate V-representation*, arXiv:2608.26615v1 (August 27, 2026), especially Sections 2–5 and Lemmas 22–23. https://arxiv.org/abs/2608.26615
2. I. Pinelis, *Polygon Convexity: Another O(n) Test*, arXiv:cs/0701045 (January 8, 2007), especially Theorem 1.12. https://arxiv.org/abs/cs/0701045
3. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, Discrete & Computational Geometry 73 (2025), 447–465; first publicly posted October 13, 2023. https://doi.org/10.1007/s00454-023-00586-x
