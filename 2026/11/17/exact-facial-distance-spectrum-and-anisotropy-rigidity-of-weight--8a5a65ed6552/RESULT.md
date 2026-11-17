# Exact facial-distance spectrum and anisotropy rigidity of weighted cross-polytopes

## Finding

Let \(d\ge2\) and \(a_1,\ldots,a_d>0\). For the Euclidean orthogonal weighted cross-polytope
\[
P(a)=\operatorname{conv}\{\pm a_i e_i:1\le i\le d\}\subset\mathbb R^d,
\]
write \(D(F)=\operatorname{dist}_2(F,P[F])\), where \(P[F]\) is the convex hull of the vertices outside the nonempty proper face \(F\). Every such face has the form
\[
F_{I,\varepsilon}=\operatorname{conv}\{\varepsilon_i a_i e_i:i\in I\},\qquad
\varnothing\ne I\subseteq[d],\quad\varepsilon_i\in\{\pm1\}.
\]
**Complete face-distance spectrum:**
\[
\boxed{D(F_{I,\varepsilon})=
\begin{cases}
\bigl(\sum_{i\in I}a_i^{-2}\bigr)^{-1/2},&1\le|I|<d,\\[2pt]
2\bigl(\sum_{i=1}^d a_i^{-2}\bigr)^{-1/2},&|I|=d.
\end{cases}}
\]
For each fixed nonempty \(I\) there are exactly \(2^{|I|}\) faces with this value (even when equal numerical values occur for different subsets).

**Exact pyramidal width and rigidity:** Let \(a_*=\max_i a_i\), and choose any longest-axis index \(j_*\). Then
\[
\boxed{\Phi_2(P(a))=\bigl(\sum_{i=1}^d a_i^{-2}-a_*^{-2}\bigr)^{-1/2},\quad
\operatorname{diam}_2(P(a))=2a_*.}
\]
Exactly \(2^{d-1}\#\{i:a_i=a_*\}\) faces minimize \(D(F)\): they are the \((d-2)\)-dimensional faces using all axes except a single longest one. No facet is minimizing. Moreover,
\[
\frac{\Phi_2(P(a))}{\operatorname{diam}_2(P(a))}
=\frac{1}{2\sqrt{\sum_{i\ne j_*}(a_*/a_i)^2}}
\le\frac{1}{2\sqrt{d-1}},
\]
with equality **if and only if** every \(a_i\) is equal. The exact relative penalty is
\[
\frac{2\sqrt{d-1}\,\Phi_2(P(a))}{\operatorname{diam}_2(P(a))}
=\left[1+\frac{1}{d-1}\sum_{i\ne j_*}
\left(\frac{a_*^2}{a_i^2}-1\right)\right]^{-1/2}.
\]

## Assumptions and scope

All distances, diameters and dual norms use the **fixed ambient Euclidean metric**, not a coordinate-rescaled metric. The weights are arbitrary strictly positive real numbers; axes may coincide in length. The integer dimension satisfies \(d\ge2\). A face is nonempty, proper, and includes its boundary; \(P[F]=\operatorname{conv}(\operatorname{vert}(P)\setminus F)\). The pyramidal width is the minimum \(D(F)\) over all these faces, as in Peña–Wirth's Definition 2.1. The face notation is exhaustive because the weighted cross-polytope is the invertible positive diagonal image of the standard cross-polytope: each face uses at most one sign on each axis, and any such signed subset is exposed.

## Proof

**1. Faces with a missing coordinate.** Let \(k=|I|<d\), and let \(x\in F_{I,\varepsilon}\). Write \(x_i=\varepsilon_i a_i\alpha_i\) for \(i\in I\), where \(\alpha_i\ge0\) and \(\sum_{i\in I}\alpha_i=1\); other coordinates vanish. Every \(y\in P[F_{I,\varepsilon}]\) satisfies \(\varepsilon_i y_i\le0\) for each \(i\in I\), since its allowed vertices either lie on another axis or have the opposite sign on an included axis. Thus
\[
\|x-y\|_2^2\ge\sum_{i\in I}(a_i\alpha_i)^2.
\]
The opposite vertices of any omitted axis both belong to the complement; their midpoint is the origin. Hence \(0\in P[F_{I,\varepsilon}]\), and choosing \(y=0\) makes this lower bound attainable at any chosen \(x\). Cauchy–Schwarz gives
\[
1=(\sum_{i\in I}\alpha_i)^2
\le (\sum_{i\in I}a_i^2\alpha_i^2)(\sum_{i\in I}a_i^{-2}),
\]
with equality precisely when \(\alpha_i=a_i^{-2}/\sum_{r\in I}a_r^{-2}\). This proves the nonfacet formula, with an explicit optimal pair.

**2. Facets.** When \(I=[d]\), the complement of a signed facet is exactly its opposite simplex: \(P[F]=-F\). By convexity of \(F\), for any \(x,z\in F\),
\[
\|x-(-z)\|_2=\|x+z\|_2\ge2\min_{w\in F}\|w\|_2,
\]
because \((x+z)/2\in F\). Choosing \(x=z\) at the minimum attains equality. The same weighted Cauchy–Schwarz calculation gives \(\min_{w\in F}\|w\|_2=(\sum_i a_i^{-2})^{-1/2}\), proving the facet formula.

**3. Exact minimizing faces.** Put \(b_i=a_i^{-2}>0\) and \(S=\sum_i b_i\). Among nonfacets, the distance \(1/\sqrt{\sum_{i\in I}b_i}\) strictly decreases on enlarging \(I\). Therefore every minimizing nonfacet has \(|I|=d-1\); its squared reciprocal distance is \(S-b_j\), maximized exactly when the omitted \(b_j\) is smallest, i.e. \(a_j=a_*\). Since \(S\ge d\min_i b_i\) and \(d\ge2\), one has \(4(S-\min_i b_i)>S\); hence \(2/\sqrt S>1/\sqrt{S-\min_i b_i}\) and facets never minimize. Each allowed omitted index has \(2^{d-1}\) independent sign choices. This proves the facial distance and the count of all minimizers.

**4. Diameter and anisotropy rigidity.** Vertex-pair distances are \(2a_i\) for opposite vertices on one axis and \(\sqrt{a_i^2+a_j^2}\) for distinct axes. Every latter distance is at most \(2a_*\), while the former attains \(2a_*\). Substitution into the facial-distance formula gives
\[
\frac{\Phi_2(P(a))}{\operatorname{diam}_2(P(a))}
=\frac{1}{2\sqrt{\sum_{i\ne j_*}(a_*/a_i)^2}}.
\]
Every summand is at least one. Equality holds precisely when all axes equal \(a_*\). Rearrangement gives the exact rigidity/penalty identity.

## Verification

A standalone verifier, `check_crosspoly.py`, builds every signed face and its complementary vertex polytope in dimensions two through five, then independently minimizes the squared Euclidean distance between the two convex hulls using SciPy's constrained optimizer. For the eight weight vectors specified in the script, it evaluated **712 face–complement pairs**. Each computed distance agreed with the appropriate formula within \(3\times10^{-6}\) (in the actual run, the largest difference was below \(2\times10^{-13}\)). It also checked the minimum against the predicted pyramidal width. Run `python check_crosspoly.py` with NumPy and SciPy installed. The finite numerical test is supplementary; all dimensions and arbitrary positive weights are covered by the proof above.

## Relationship to prior work

Peña and Wirth, *Calculus of the Facial Distance* (2026, arXiv:2608.28971), Section 6, Example 6.2, explicitly compute the unweighted \(\ell_1\) ball's all-rank face distances and \(\Phi_2=1/\sqrt{d-1}\). That exact symmetric case is **known** and is not a novelty claim here. Their Section 5, Corollary 5.2, gives general norm-dependent upper/lower bounds after invertible linear transformations, rather than the present exact arbitrary diagonal-weight formula. The new focus is the all-face spectrum for all weights, the identity and multiplicity of the minimizing faces when axis lengths tie, and the exact Euclidean anisotropy rigidity. Positive diagonal changes of variables preserve face combinatorics but *not* distances in the fixed Euclidean metric. Deza, Martínez-Rubio, Peña and Wirth (2026, arXiv:2609.32440) address the dimension-normalized facial-distance-to-diameter problem for all polytopes and an exact Birkhoff-polytope computation; their general extremality statement does not itself determine the weighted cross-polytope spectrum. Peña–Wirth's Section 7, Example 7.4, considers a nonorthogonal perturbation of the three-dimensional unit cross-polytope, not the diagonal-weight family.

## Limitations

The result concerns only orthogonal, axis-aligned (up to Euclidean rotations) cross-polytopes with positive semiaxes; a general invertible affine image has a non-diagonal Euclidean quadratic form and is outside scope. It does not prove that these formulas were unknown under every alternative terminology. Relevant exact formulas may appear in sources or unpublished notes not found in available searches, so historical priority is provisional. Numerical verification is finite and subject to optimization tolerances; no independent external mathematical audit has been performed.

## References

1. J. Peña and E. Wirth, *Calculus of the Facial Distance*, arXiv:2608.28971 (first public 2026-08-29). https://arxiv.org/abs/2608.28971 ; full text https://optimization-online.org/wp-content/uploads/2026/08/calculusoptonline.pdf ; especially Definition 2.1, Corollary 5.2 and Example 6.2.
2. A. Deza, D. Martínez-Rubio, J. Peña and E. Wirth, *Facial distance and diameter*, arXiv:2609.32440 (2026). https://arxiv.org/abs/2609.32440.
3. J. Zhao, *Pyramidal Width Can Increase Under Vertex Insertion*, arXiv:2607.29555 (2026). https://arxiv.org/abs/2607.29555.
