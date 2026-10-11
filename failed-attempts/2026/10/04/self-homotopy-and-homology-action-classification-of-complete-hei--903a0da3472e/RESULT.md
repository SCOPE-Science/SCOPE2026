# Self-homotopy and homology-action classification of complete height-two finite graph models
## Finding
For integers \(p,q\ge 3\), let \(P_{p,q}=A\oplus B\) be the finite \(T_0\)-space with \(|A|=p\) minimal points, \(|B|=q\) maximal points, and every point of \(A\) below every point of \(B\). Its order complex is the complete bipartite graph \(K_{p,q}\), hence has first Betti number \((p-1)(q-1)\).

The number of continuous self-maps is
\[
N_{p,q}=p^p q^q+q\big((p+1)^p-p^p\big)+p\big((q+1)^q-q^q\big).
\]
All self-maps inducing zero on \(H_1(P_{p,q};\mathbb Z)\) lie in one homotopy class, of cardinality
\[
Z_{p,q}=q(p+1)^p+p(q+1)^q-pq,
\]
and every other self-map is isolated in the pointwise poset of continuous maps. Consequently
\[
|[P_{p,q},P_{p,q}]|=1+(p^p-p)(q^q-q).
\]

For a level-preserving map \(f=(\alpha,\beta)\), there is a natural identification
\[
H_1(P_{p,q};\mathbb Z)\cong \widetilde H_0(A;\mathbb Z)\otimes\widetilde H_0(B;\mathbb Z),
\]
under which \(H_1(f)=\widetilde\alpha_*\otimes\widetilde\beta_*\). Therefore
\[
\operatorname{rank}H_1(f)=(|\alpha(A)|-1)(|\beta(B)|-1).
\]
If \(F_n(r)=(n)_rS(n,r)\), where \(S(n,r)\) is a Stirling number of the second kind, then for every positive integer \(\rho\), the number of self-maps with homology rank \(\rho\) is
\[
R_\rho(p,q)=\sum_{\substack{2\le r\le p,\ 2\le s\le q\\(r-1)(s-1)=\rho}}F_p(r)F_q(s).
\]
In particular, a self-map induces an integral \(H_1\)-isomorphism exactly when it is a homeomorphism; there are \(p!q!\) such maps.

## Assumptions and scope
The theorem is stated for all integers \(p,q\ge 3\). The topology on \(P_{p,q}\) is the Alexandrov topology associated with the displayed partial order, and continuity is therefore equivalent to order preservation. The homotopy relation used here is ordinary homotopy of finite spaces; comparable maps in the pointwise map poset are homotopic, and a zigzag of comparable maps gives one homotopy class.

The order complex has one vertex for every point and one edge for every comparable pair. Since the poset has height two, this order complex is exactly \(K_{p,q}\), so there are no higher simplices and no hidden higher-chain contributions to the computation of \(H_1\).

## Proof
Write a self-map as its values on the lower shore \(A\) and upper shore \(B\). Order preservation gives three disjoint cases.

First, if the image of \(A\) is contained in \(A\) and the image of \(B\) is contained in \(B\), the map is an arbitrary pair of set maps \(\alpha:A\to A\) and \(\beta:B\to B\), giving \(p^p q^q\) maps.

Second, suppose some point of \(A\) maps into \(B\). Because every input point of \(A\) lies below every input point of \(B\), maximality forces all of \(B\) to one common value \(b_0\in B\). Once \(b_0\) is fixed, every point of \(A\) may map independently into \(A\cup\{b_0}\). Removing the already counted maps whose lower-shore image stays entirely in \(A\) gives \(q((p+1)^p-p^p)\) maps. Dually, the remaining non-level-preserving maps contribute \(p((q+1)^q-q^q)\). This proves the formula for \(N_{p,q}\).

Every map in the second case is pointwise below the constant map at \(b_0\), and every map in the dual case is pointwise above a constant map at some \(a_0\in A\). A level-preserving map with constant \(\alpha\) is pointwise above a constant lower-shore map, while one with constant \(\beta\) is pointwise below a constant upper-shore map. All constant maps are connected through inequalities \(c_a\le c_b\) for \(a\in A\) and \(b\in B\). Thus all these maps lie in one homotopy class.

Now let \(f=(\alpha,\beta)\) be level preserving with both \(\alpha\) and \(\beta\) nonconstant. If \(f\le g\), then maximality forces \(g|_B=\beta\). Were some lower-shore value of \(g\) maximal, order preservation would force \(\beta\) to be constant, a contradiction. Hence \(g=f\). The dual argument shows that \(g\le f\) also implies \(g=f\). Thus such an \(f\) is isolated. There are \((p^p-p)(q^q-q)\) of them, proving the homotopy-class formula and showing that the remaining class has size \(Z_{p,q}=N_{p,q}-(p^p-p)(q^q-q)=q(p+1)^p+p(q+1)^q-pq\).

For homology, orient every edge from \(A\) to \(B\). Fix base vertices \(a_p\in A\) and \(b_q\in B\). The cycles
\[
z_{ij}=e_{ij}-e_{iq}-e_{pj}+e_{pq},\qquad 1\le i<p,\ 1\le j<q,
\]
form a basis of \(H_1(K_{p,q};\mathbb Z)\). This identifies that group naturally with \(\widetilde H_0(A;\mathbb Z)\otimes\widetilde H_0(B;\mathbb Z)\). A level-preserving map \(f=(\alpha,\beta)\) acts as \(\widetilde\alpha_*\otimes\widetilde\beta_*\). For a set map on an \(n\)-point set with image of size \(r\), the image in reduced zeroth homology is the augmentation-zero subgroup on those \(r\) image points, of rank \(r-1\). Tensor-product rank therefore gives
\[
\operatorname{rank}H_1(f)=(|\alpha(A)|-1)(|\beta(B)|-1).
\]
Non-level-preserving maps and level-preserving maps with a constant shore map belong to the constant component, so their induced first-homology map is zero. Conversely, both shore maps nonconstant give positive rank. Hence zero homology action is exactly the unique non-isolated homotopy class.

There are \((n)_rS(n,r)\) endofunctions on an \(n\)-point set with image of size \(r\). Multiplying the independent shore counts and summing over \((r-1)(s-1)=\rho\) gives the rank-profile formula. Full homology rank requires \(r=p\) and \(s=q\), so \(\alpha\) and \(\beta\) are permutations. These are precisely the homeomorphisms, counted by \(p!q!\).

## Verification
The proof above is symbolic and covers every \(p,q\ge 3\); finite enumeration is used only as a regression check. The dependency-free script `artifacts/verify.py` enumerates all continuous self-maps for \(P_{3,3}\) and \(P_{3,4}\), computes induced first-homology ranks directly from the cellular edge-chain images of the basis cycles, and compares the results with the closed formulas. For \(P_{3,3}\) it additionally builds the full comparability graph of the map poset and checks the predicted homotopy-component sizes.

The replay output is stored in `artifacts/verification_output.txt`. It gives \(951\) maps and rank profile \((375,324,216,36)\) at ranks \(0,1,2,4\) for \(P_{3,3}\), with \(577\) homotopy components, one of size \(375\) and \(576\) singletons. For \(P_{3,4}\) it gives \(8167\) maps and rank profile \((2119,1512,3096,432,864,144)\) at ranks \(0,1,2,3,4,6\). The script terminates with `VERIFY_OK`.

## Relationship to prior work
Barmak and Minian establish the finite-poset framework, recall that continuous maps between finite spaces are exactly order-preserving maps, and characterize minimal finite models of finite graphs. Their Theorem 1.2 is a classification by height, number of points, and Hasse edges; it does not state the present self-map count, homotopy-component classification, tensor formula for induced first homology, or exact homology-rank profile. The present result instead studies the internal mapping theory of the complete height-two family \(P_{p,q}\).

The general core and homotopy theory traced to Stong supplies foundational context, but the exact complete-bipartite family formulas above are not consequences explicitly located in the inspected accessible source. Searches for complete-bipartite finite-space self-map, homotopy, and homology-action classifications also returned graph-embedding, poset-saturation, and unrelated complete-bipartite results rather than this statement.

## Limitations
The stated theorem deliberately covers only \(p,q\ge 3\). It does not claim a novelty determination for boundary-shore cases, nor does it classify the multiplicities of individual integral matrices having the same homology rank. The computational replay checks two small parameter pairs and is not an infinite proof; the infinite result rests on the symbolic classification above.

A residual literature risk remains because Stong's original 1966 full text was not directly accessible during this review. Its general theory is well represented in the accessible Barmak--Minian account, but absence of an exact older family formula cannot be proved from search failure alone.

## References
Jonathan Ariel Barmak and Elias Gabriel Minian, “Minimal Finite Models,” arXiv:math/0611156v1, first public version 6 November 2006. In particular, Theorem 1.2 and the preliminaries on finite spaces, order-preserving maps, beat points, and cores provide the background used here.

Robert E. Stong, “Finite topological spaces,” Transactions of the American Mathematical Society 123 (1966), 325–340, DOI 10.1090/S0002-9947-1966-0195042-2. This reference is recorded as foundational context; its full text was not directly inspected in this review.
