# Sharp higher-dimensional failure of \(r\)-flagified Dowker duality for uniform incidence relations

## Finding
For every pair of integers \(r\ge2\) and \(n\ge r+2\), let \(X=[n]\), let \(Y=\binom{[n]}{r}\), and use the incidence relation \(i\mathrel{R}S\) if and only if \(i\in S\). Denote its two ordinary Dowker complexes by \(D_X\) and \(D_Y\). Define \(F_r(D)\) to retain the original faces of dimension below \(r\) and to contain a set of at least \(r+1\) vertices precisely if all of its \(r\)-vertex subsets are faces of \(D\). This is the higher \(r\)-flagification of Huber and Schnider.

**Theorem.** The higher flagifications have precisely the following integral homotopy types:
\[
|F_r(D_X)|\simeq *,\qquad
|F_r(D_Y)|\simeq\operatorname{skel}_{r}\Delta^{n-1}
\simeq\bigvee^{\binom{n-1}{r+1}}S^{r}.
\]
In particular, the two transposed complexes have isomorphic integral homology in every degree less than \(r\), but fail to have isomorphic integral homology in degree \(r\); the failure rank is \(\binom{n-1}{r+1}\) and can be arbitrarily large for each fixed \(r\). The classification is nonequivariant; no assertion about integral permutation representations is needed.

## Assumptions and scope
All complexes are ordinary abstract simplicial complexes on finite sets. The simplex \(\Delta^{n-1}\) has vertex set \([n]\). Every family of fewer than \(r\) distinct \(r\)-subsets is treated according to the original Dowker face condition; higher flagification does **not** automatically insert missing lower-dimensional faces. The displayed equivalences are integral homotopy equivalences, not deductions from finite Betti-number computations.

## Proof
**1. The point-side complex.** A subset \(I\subseteq[n]\) lies in \(D_X\) exactly when some \(r\)-subset contains it. Hence \(D_X=\operatorname{skel}_{r-1}\Delta^{n-1}\). Every \(r\)-element subset of \([n]\) is a face of \(D_X\), so \(F_r(D_X)=\Delta^{n-1}\), a contractible simplex.

**2. The only new faces on the subset side.** A family \(\mathcal A\subseteq Y\) lies in \(D_Y\) precisely when its members have a common point. Consider a family with at least \(r+1\) members such that every \(r\)-member subfamily has nonempty intersection. Suppose its total intersection is empty, and select an inclusion-minimal subfamily \(A_1,\ldots,A_t\) with empty intersection. Since all subfamilies of size at most \(r\) intersect, \(t\ge r+1\). Minimality supplies \(x_i\in\bigcap_{j\ne i}A_j\) with \(x_i\notin A_i\). The \(x_i\) are distinct, and each \(A_i\) contains the other \(t-1\) points; thus \(t-1\le r\), forcing \(t=r+1\). With \(T=\{x_1,\ldots,x_{r+1}\}\), necessarily \(A_i=T\setminus\{x_i\}\).

There can be no additional member \(B\). Indeed, for every two distinct indices \(i,j\), intersect the \(r-1\) members \(A_l\) with \(l\notin\{i,j\}\); their intersection is precisely \(\{x_i,x_j\}\). Adding \(B\) to these \(r-1\) members must still leave a point, so \(B\) meets **every** pair in \(T\). Since \(|B|=r\) and \(|T|=r+1\), we must have \(B=T\setminus\{x_i\}\) for some \(i\), already present. Therefore every new face is exactly an \(r\)-simplex
\[
\sigma_T=\{T\setminus\{t\}:t\in T\},\qquad |T|=r+1.
\]
Its entire boundary is already in \(D_Y\), because every proper subfamily of \(\sigma_T\) has a common point. Distinct such new simplices have disjoint interiors. Consequently \(F_r(D_Y)\) is obtained from \(D_Y\) by attaching one \(r\)-simplex \(\sigma_T\) along its complete boundary for each \((r+1)\)-subset \(T\subseteq[n]\).

**3. A natural nerve description of the attaching spheres.** Cover \(D_Y\) by the simplices \(C_i\), where \(C_i\) consists of all vertices \(S\in Y\) containing \(i\). For every nonempty \(I\subseteq[n]\), the intersection \(\bigcap_{i\in I}C_i\) is a nonempty simplex exactly when \(|I|\le r\); otherwise it is empty. The nerve is thus \(N=\operatorname{skel}_{r-1}\Delta^{n-1}\). The usual good-cover nerve equivalence \(|D_Y|\simeq|N|\) can be constructed by the homotopy-colimit model of this intersection diagram and is natural for subcomplexes equipped with their restricted covers.

For fixed \(T\) with \(|T|=r+1\), restrict the same cover to \(\partial\sigma_T\). Its nonempty intersections are exactly \(C_i\cap\partial\sigma_T\) for \(i\in T\). In fact \(C_i\cap\partial\sigma_T\) is the facet of \(\partial\sigma_T\) opposite the vertex \(T\setminus\{i\}\). Any \(s\le r\) of these facets intersect in a simplex and all \(r+1\) do not. Hence the restricted nerve is precisely \(\partial\Delta_T\). Naturality gives a homotopy-commutative square in which \(\partial\sigma_T\hookrightarrow D_Y\) corresponds to \(\partial\Delta_T\hookrightarrow N\), and both vertical maps are homotopy equivalences. This is the critical attaching-map comparison, not merely a comparison of homology ranks.

**4. Attach all cells.** Replacing \(D_Y\) and all boundary inclusions by these compatible nerve models does not change the homotopy type of their homotopy pushout (all simplicial boundary inclusions are cofibrations). Attaching the \(r\)-simplex \(\sigma_T\) to \(D_Y\) corresponds to attaching the standard simplex \(\Delta_T\) along \(\partial\Delta_T\) to \(N\). Performing this for all \(T\) adjoins precisely every \(r\)-simplex of \(\Delta^{n-1}\), producing \(\operatorname{skel}_{r}\Delta^{n-1}\). This proves the first claimed equivalence for \(F_r(D_Y)\).

**5. Count spheres integrally.** The \(r\)-skeleton of an \((n-1)\)-simplex admits the standard acyclic matching that pairs every nonempty face not containing the last vertex and of size at most \(r\) with its enlargement by that vertex, leaving one critical zero-cell and the \(\binom{n-1}{r+1}\) critical faces of size \(r+1\) avoiding the last vertex. Since \(r\ge2\), the resulting CW model has no positive-dimensional cells below dimension \(r\). The attaching maps of these \(r\)-cells are necessarily nullhomotopic. Therefore it is the displayed wedge of \(r\)-spheres, proving the theorem over the integers.

## Verification
A standalone checker in `VERIFY.py` independently forms the point and subset Dowker complexes, applies the literal higher-flag condition on all families through size \(r+2\), identifies all inserted exceptional simplices, and computes the full reduced mod-two simplicial boundary ranks on five finite instances. The tests cover \((n,r)\in\{(4,2),(5,2),(6,2),(5,3),(6,3)\}\). Their predicted nonzero reduced Betti ranks are respectively \(1,4,10,1,5\), each in degree \(r\). The unrestricted theorem follows instead from the proof in Steps 1–5.

## Relationship to prior work
Huber and Schnider, *Flagifying the Dowker Complex* (first public arXiv posting August 11, 2025), define higher flagification and prove an exact transpose-Dowker homology comparison below degree \(r\). Their Proposition 3.4 gives the tetrahedral-edge incidence example at \(r=2,n=4\), whose two flagifications are a point and \(S^2\). **That boundary instance is not new.** The present theorem determines the whole incidence family for every \(r\ge2,n\ge r+2\), including all higher arities, and quantifies the sharp first failing homological degree and its unbounded integral rank. The good-cover nerve theorem, simplex-skeleton homotopy type and minimal obstruction argument are standard proof ingredients rather than claimed independent inventions.

A related published classification of higher-arity neighborhood nerves of rank-selected finite Alexandrov spaces has a different simplicial complex and different sphere dimension; its stated conclusion neither determines this transpose-Dowker pair nor supplies these higher-flagified attaching maps.

## Limitations
This theorem is restricted to the **uniform incidence relation** between points and \(r\)-subsets. It does not establish sharpness for every relation, does not compute persistence under arbitrary changing relations, and does not determine the equivariant homotopy type under ground-label permutations. The usual small tetrahedral case is published prior work. No independent mathematical validation has been performed.

## References
1. M. Huber and P. Schnider, *Flagifying the Dowker Complex*, arXiv:2508.08025, initially public 2025-08-11, https://arxiv.org/abs/2508.08025, especially Definition 1.2, the higher-flagification duality theorem in Section 1, and Proposition 3.4.
2. C. H. Dowker, *Homology groups of relations*, Annals of Mathematics 56 (1952), 84–95; classical Dowker relation complexes and duality.
3. Classical simplicial nerve lemma and its natural homotopy-colimit construction; standard simplex-skeleton acyclic matching (proofs for the present situation are spelled out above).
