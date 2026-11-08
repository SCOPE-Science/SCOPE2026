# Two sharp Euclidean metric transitions in scaled two-level enriched order polytopes

## Finding

For integers \(m,n\ge2\) and real \(a,b>0\), consider the blockwise-scaled enriched order and enriched chain polytopes
\[
O_{m,n}(a,b)=\operatorname{conv}\bigl(a[-1,1]^m\times\{b\mathbf1_n\},\ \{0_m\}\times b[-1,1]^n\bigr),
\]
\[
C_{m,n}(a,b)=\operatorname{conv}\bigl(a[-1,1]^m\times\{0_n\},\ \{0_m\}\times b[-1,1]^n\bigr).
\]
Let \(w(K)=\min_{\|z\|_2=1}\bigl(h_K(z)+h_K(-z)\bigr)\), where \(h_K\) is the support function. Put
\[
A=\frac1{a^2}+\frac1{2b^2},\qquad B=\frac1{b^2}.
\]
The exact Euclidean metric formulas are
\[
\boxed{w(O_{m,n}(a,b))=\frac2{\sqrt{\max\{A,B\}}}},\quad
\boxed{\operatorname{diam}(O_{m,n}(a,b))^2=\max\{4ma^2,ma^2+4nb^2\}},
\]
\[
\boxed{w(C_{m,n}(a,b))=\frac2{\sqrt{a^{-2}+b^{-2}}}},\quad
\boxed{\operatorname{diam}(C_{m,n}(a,b))^2=4\max\{ma^2,nb^2\}}.
\]

The minimum-width normals of the enriched order polytope undergo a sharp transition at \(a=\sqrt2\,b\), whereas its diameter-determining pairs change at \(3ma^2=4nb^2\). At \(a=b=1\), the two lattice polytopes are Ehrhart-equivalent by earlier results, but their minimum widths have the dimension-independent ratio
\[
\frac{w(O_{m,n}(1,1))}{w(C_{m,n}(1,1))}=\frac2{\sqrt3}>1.
\]
More generally the enriched order polytope is strictly wider in its minimum direction for all positive scales; the two diameters coincide if and only if \(3ma^2\ge4nb^2\).

The **complete set of oriented unit width-minimizers** for \(O_{m,n}(a,b)\) is as follows. If \(a<\sqrt2\,b\), select any lower coordinate \(i\), any two distinct upper coordinates \(j,k\), and signs \(\epsilon,\eta\in\{-1,+1\}\). Set
\[
u_i=\frac{\epsilon}{a\sqrt A},\qquad
v_j=\frac{\eta}{2b\sqrt A},\qquad
v_k=-\frac{\eta}{2b\sqrt A},
\]
with all other entries zero. There are exactly \(4m\binom n2\) oriented minimizing normals. If \(a>\sqrt2\,b\), the only minimizing normals are the \(2n\) signed upper coordinate vectors. At \(a=\sqrt2\,b\), the minimizer set is precisely the disjoint union of those two families, with \(4m\binom n2+2n\) members.

For the diameter, if \(3ma^2>4nb^2\), the diametral pairs are opposite vertices of \(a[-1,1]^m\times\{b\mathbf1_n\}\). If \(3ma^2<4nb^2\), they join a vertex \((a\epsilon_1,\ldots,a\epsilon_m,b\mathbf1_n)\) to \((0_m,-b\mathbf1_n)\), with every \(\epsilon_i\in\{\pm1\}\). At equality both classes, and no other classes, occur.

## Assumptions and scope

The underlying poset is the ordinal sum \(P=A_m\oplus A_n\): all elements of the lower antichain precede every element of the upper antichain, and no elements within a level are comparable. The unscaled convex hulls displayed above are exactly its enriched order and enriched chain polytopes in their standard coordinate embeddings. The blockwise scalings are positive diagonal linear maps and preserve full dimension, but need not preserve the lattice/Ehrhart properties. All widths and diameters are ambient Euclidean quantities, not graph distances, vertex-averaged statistics, or widths in a rescaled metric. The condition \(m,n\ge2\) ensures the two-coordinate upper-block cancellation family exists; one-element levels are not asserted.

## Proof

Write an arbitrary dual vector as \(z=(u,v)\in\mathbb R^m\times\mathbb R^n\), and set
\[
U=a\|u\|_1,\quad V=b\|v\|_1,\quad S=b\sum_{j=1}^n v_j,\quad T=|S|\le V.
\]
The two defining cubes of \(O_{m,n}(a,b)\) have support values \(U+S\) and \(V\). Hence
\[
h_O(z)=\max\{U+S,V\},\qquad
W_O(z)=h_O(z)+h_O(-z)=\max\{2U,2V,U+V+T\}.
\]
The second equality follows by considering whether both, neither, or exactly one of \(U+S\) and \(U-S\) exceed \(V\). For the chain partner, \(W_C(z)=2\max\{U,V\}\).

For nonzero \(z\), rescale so \(W_O(z)=2\). Then \((U,V,T)\) belongs to the compact three-dimensional polytope
\[
0\le U\le1,\quad0\le V\le1,\quad0\le T\le V,\quad U+V+T\le2.
\]
For lower coordinates, \(\|u\|_2^2\le(U/a)^2\), with equality exactly when \(u\) has at most one nonzero component. Split the upper coordinates into positive and negative parts with their respective sums \((V+T)/(2b)\) and \((V-T)/(2b)\). Their squared sum is bounded by the squares of the two sums, giving
\[
\|z\|_2^2\le \frac{U^2}{a^2}+\frac{V^2+T^2}{2b^2}=:Q(U,V,T).
\]
Equality in the upper bound requires at most one positive and one negative upper coordinate. The feasible triple polytope has precisely the six vertices
\[
(0,0,0),\ (1,0,0),\ (0,1,0),\ (1,1,0),\ (0,1,1),\ (1,\tfrac12,\tfrac12).
\]
The strictly convex quadratic \(Q\) attains its maximum on this polytope only at \((1,1,0)\), with value \(A\), or at \((0,1,1)\), with value \(B\), according to which of \(A,B\) is larger. Indeed \(Q(1,\tfrac12,\tfrac12)=a^{-2}+(4b^2)^{-1}<A\); the remaining three vertices are dominated by one of the listed candidates. Strict convexity excludes all nonvertex equality points even when \(A=B\). Reversing the normalization proves
\[
\|z\|_2^2\le\frac{W_O(z)^2}{4}\max\{A,B\},
\]
and the equality conditions yield exactly the minimizing normals stated in the Finding section. The boundary \(A=B\) is equivalent to \(a=\sqrt2\,b\).

For \(C\), the support function gives \(W_C=2\max\{U,V\}\) and
\[
\|z\|_2^2\le\frac{U^2}{a^2}+\frac{V^2}{b^2}\le\max\{U,V\}^2(a^{-2}+b^{-2}).
\]
Equality is achieved by a vector supported in one coordinate of each block with \(U=V\); the chain width formula follows. Since \(A<a^{-2}+b^{-2}\) and \(B<a^{-2}+b^{-2}\), the strict minimum-width comparison follows.

For the diameter, it suffices to compare pairs of vertices from the two cubes. The largest squared distance within the lower cube is \(4ma^2\), within the upper cube it is \(4nb^2\), and between the cubes it is \(ma^2+4nb^2\). The upper-cube value is strictly smaller than the cross-cube value because \(m,a>0\). This proves the order diameter formula and the claimed complete diametral-pair classification, including the equality case. The chain polytope has maximum within-block squared distances \(4ma^2\) and \(4nb^2\), while its largest cross-block squared distance \(ma^2+nb^2\) is strictly smaller than their maximum. Finally, \(\operatorname{diam}(O)=\operatorname{diam}(C)\) if and only if \(3ma^2\ge4nb^2\), as the formulas show.

## Verification

A standalone Python 3 checker, `verify.py`, uses only the standard library and exact rational arithmetic. It enumerates generating points and directly recomputes the support functions, squared diameters, sharp width bounds, and equality-witness normals for \(m,n\in\{2,3,4\}\) and six pairs of positive integer scales. It checks \(82{,}080\) nonzero ternary normal vectors across \(54\) profiles. Run: `python3 verify.py`. The expected terminal line begins with `TWOLEVEL_ENRICHED_SCALED_CHECKS_PASSED`. The checker does not establish the all-real-scale or all-dimension theorem; those are proved above.

## Relationship to prior work

Ohsugi and Tsuchiya introduced enriched chain and enriched order polytopes and proved their Ehrhart equivalence; Okada and Tsuchiya described an explicit enriched transfer map. Those antecedent definitions and the Ehrhart equivalence are not claimed as new. Previously recorded exact metric results for enriched chain polytopes already imply the unscaled chain width in this setting, while a separate earlier two-level computation gives the same canonical convex-hull descriptions together with uniform-volume covariance. They do not themselves state the two independent Euclidean transition laws or the complete sharp minimizing-normal classification for positive blockwise scales. These new metric claims are obtained from an explicit support-function optimization rather than from the Ehrhart equivalence or covariance data.

## Limitations

The classification assumes two nonempty antichain levels of size at least two each and a single positive scale per level; arbitrary posets or arbitrary coordinatewise scales are not covered. Exact novelty relative to every possible older geometric formulation has not been independently established. The chain-polytope metric formulas are provided for comparison, not asserted to be independently novel. The finite checker is a reproducibility aid, not a proof for infinitely many parameter values. The mathematical assessment is a self-review; no independent audit has been performed.

## References

- H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097 (first public version, 2018-12-05). https://arxiv.org/abs/1812.02097
- H. Ohsugi and A. Tsuchiya, *Enriched order polytopes and Enriched Hibi rings*, arXiv:1903.00909 (first public version, 2019-03-03). https://arxiv.org/abs/1903.00909
- S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271 (first public version, 2020-03-27). https://arxiv.org/abs/2003.12271
