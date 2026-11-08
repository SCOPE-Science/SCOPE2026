# An odd-unicycle criterion and a four-placement exception for multipartite line-graph control

## Finding

Let integers \(r\ge3\) and \(k\ge2\) be given, let \(G=K_{k,\ldots,k}\) have \(r\) equal parts, and let \(H=L(G)\) be its unit-weight line graph. Each vertex of \(H\) represents one edge of \(G\). Consider the full-state linear system
\[
\dot z=-L_H z+E_Uu,
\]
where \(E_U\) has one coordinate column for each selected vertex \(U\subseteq V(H)=E(G)\). Put \(n=rk\), \(m=\binom r2 k^2\), and \(d=(r-1)k\).

**Theorem.** The minimum possible number of independent coordinate actuators is
\[
\boxed{q=m-n=\frac{rk((r-1)k-2)}2.}
\]
For \(|U|=q\), form the spanning subgraph \(F=(V(G),E(G)\setminus U)\), which has exactly \(n\) edges. The control pair is controllable precisely when every connected component of \(F\) contains exactly one cycle and that cycle has odd length, subject to a single exception: at \((r,k)=(3,2)\), the four spanning configurations \(F\cong C_3\sqcup C_3\) are not controllable. These are the only failures among odd-unicyclic configurations. All such \(r,k\) admit minimum controllable placements.

In particular, \(L(K_{2,2,2})\) has exactly **496 labeled minimum coordinate-actuator sets** of size six, compared with 500 spanning odd-unicyclic candidate complements. More generally, if \(\mathcal U_{r,k}\) denotes all minimum controllable sets, and \(c(F)\) is the number of connected components of the complementary graph, then
\[
\boxed{\sum_{U\in\mathcal U_{r,k}}4^{c(F)}
=2d\,d^{r(k-1)}\big((r-2)k\big)^{r-1}
-64\mathbf 1_{\{(r,k)=(3,2)\}}.}
\]
The last identity is a component-weighted census, **not** a claim that the ordinary number of placements is given by the product on its right.

## Assumptions and scope

All edges of \(G\) and \(H\) are unweighted and undirected. There are \(r\) labeled parts of size \(k\); vertices within parts are distinguished. Each actuator independently drives one coordinate of the **whole line-graph state**, with ordinary linear time-invariant controllability in the Kalman/PBH sense. The input constraint is coordinate-only, not arbitrary dense input columns. The result does not apply to unequal part sizes, edge-weighted line graphs, or directed switchboard dynamics.

An odd-unicyclic component means a connected graph with the same number of edges as vertices, whose unique cycle is odd; tree attachments are allowed. The word spanning means all original vertices of \(G\) remain in \(F\).

## Proof

**1. Exact modal decomposition.** Let \(B\in\{0,1\}^{n\times m}\) be the unsigned vertex-edge incidence matrix of \(G\). Since \(G\) is \(d\)-regular,
\[
B^\top B=2I_m+A_H,\qquad L_H=2dI_m-B^\top B,\qquad BB^\top=Q_G=dI_n+A_G.
\]
For \(r\ge3\), \(G\) has triangles and is connected, so \(Q_G\) is positive definite and \(B\) has row rank \(n\). By decomposing vectors into constants, vectors constant on each part with total sum zero, and vectors summing to zero inside every part, the spectrum of \(Q_G\) is
\[
2d\ (1),\quad (r-2)k\ (r-1),\quad d\ (r(k-1)),
\]
with multiplicities in parentheses. Hence \(L_H\) has eigenspace \(\ker B\), eigenvalue \(2d\), dimension \(m-n\), and the other eigenspaces \(B^\top E_\mu(Q_G)\), where the eigenvalue is \(2d-\mu\). Their dimensions are respectively \(1,r-1,r(k-1)\). For \(r\ge3,k\ge2\), \(m-n\) is at least all three other multiplicities. PBH therefore forces at least \(q=m-n\) coordinate actuators.

**2. The large eigenspace and odd pseudoforests.** Fix any \(U\) of size \(m-n\). Since the complement \(F\) has \(n\) edges, PBH for eigenvalue \(2d\) states that no nonzero vector \(y\in\ker B\) may be supported in the coordinates \(F\). This is equivalent to invertibility of the square unsigned incidence submatrix \(B_F\). For each connected component \(C\) of \(F\), full rank requires \(|E(C)|=|V(C)|\); thus \(C\) is unicyclic. Along any tree edge, a null vector of \(B_C^\top\) alternates signs from its root, and the cycle closure gives a nonzero solution exactly when its cycle is even. Consequently \(B_F\) is invertible if and only if each component is odd-unicyclic. In that case \(|\det B_F|=2^{c(F)}\).

**3. Other eigenspaces from the selected-edge graph.** Write \(S=(V(G),U)\). For an eigenvector \(B^\top x\), where \(x\) is a \(Q_G\)-eigenvector, zero coordinates on \(U\) mean \(B_S^\top x=0\). On a connected nonbipartite component of \(S\), these equations \(x_a+x_b=0\) along every edge force \(x=0\). On an isolated vertex, they leave its coordinate free. If \(S\) has one isolated vertex and all other vertices lie in a connected nonbipartite component, then \(\ker B_S^\top\) is spanned by the corresponding coordinate vector, which is not an eigenvector of \(Q_G\) because \(G\) has positive degree at every vertex. Thus either of these shapes of \(S\) passes PBH for all non-\(2d\) modes.

**4. Dense-complement lemma.** First suppose \((r,k)\ne(3,2)\). Deleting only \(n=rk\) edges of \(G\) cannot disconnect a vertex set of size between two and \(n/2\) from the rest. Indeed, for a vertex set of size \(t\), its edge boundary is at least \(t(d-t+1)\); concavity in \(t\), checked at \(t=2\) and \(t=\lfloor n/2\rfloor\), shows that this exceeds \(n\) whenever \((r-2)k>2\). Therefore \(S\) is connected, or consists of one isolated vertex and a connected remainder.

The maximum cut of \(G\) has \(\lfloor r^2/4\rfloor k^2\) edges. For a cut containing \(x_i\) of the \(k\) vertices from part \(i\), its size is \(\sum_{i<j}[k(x_i+x_j)-2x_ix_j]\), which is separately affine in each \(x_i\); moving part assignments to endpoints gives the stated maximum. The minimum number of edges whose deletion makes \(G\) bipartite is therefore
\[
\tau(G)=\left(\binom r2-\left\lfloor\frac{r^2}4\right\rfloor\right)k^2.
\]
It exceeds \(n\), except for \((r,k)=(3,2),(3,3),(4,2)\). At \((3,3)\) or \((4,2)\), equality holds, but **every** maximum-cut complement is bipartite. Indeed, two simultaneously split original parts cannot maximize a cut: shifting one vertex count upward and the other downward while keeping their sum fixed makes the cut size strictly convex along that direction. Thus at most one part is split. With four parts the slope in a remaining split count is nonzero, forcing all parts unsplit; with three parts the only possible split has one other whole part on each side. Explicitly: with three parts, a maximizing cut puts one complete part on each side and may split the third, leaving two disjoint complete bipartite subgraphs; with four parts, a maximizing cut puts two complete parts on each side, leaving two complete bipartite subgraphs. Such an \(F\) has singular \(B_F\). Thus an odd-unicyclic \(F\) never leaves a connected bipartite \(S\).

If \(S\) has one isolated vertex \(v\), the deleted edges include all \(d\) edges incident to \(v\), leaving at most \(n-d=k\) deletions in \(G-v\). When \(\tau(G)>n\), the elementary inequality \(\tau(G-v)\ge\tau(G)-d>k\) makes \(S-v\) nonbipartite. In the two equality cases, \(G-v\) contains respectively \(K_{2,3,3}\) or \(K_{1,2,2,2}\); their minimum bipartizing deletion sizes are respectively six and six, strictly above \(k\). These values follow by maximizing cuts over their four or three part-size counts, again moving each count to an endpoint. Hence the connected remainder is nonbipartite. This proves the iff condition without exception for all \((r,k)\ne(3,2)\).

**5. The small exceptional graph.** For \(G=K_{2,2,2}\), \(n=6,m=12,d=4\), and \(\dim\ker B=6\). If the candidate \(F\) is two disjoint triangles, \(S\) is a spanning six-cycle alternating between the two vertices of each original part. The alternating vector on this six-cycle has sum zero on every original part; it is a nonzero eigenvector of \(Q_G\) of eigenvalue four with \(B_S^\top x=0\). PBH fails. There are \(2^3/2=4\) such labeled complements.

For any other odd-unicyclic \(F\), the selected graph \(S\) cannot have a nontrivial disconnected component: a cut separating two or three vertices of \(G\) costs at least six edges; equality would force all of \(F\) to be a bipartite cut, contradicting invertibility of \(B_F\). Thus \(S\) is connected or has one isolated vertex. If it has one isolated vertex, its remaining five vertices induce a connected graph obtained by deleting two edges from \(K_{1,2,2}\). Making that graph bipartite needs exactly the two edges between its singleton part and one complete two-vertex part; together with the four incident edges of the isolated vertex, these would make \(F\) bipartite (in fact containing an even four-cycle), again contradicting invertibility. Therefore its remaining component is nonbipartite and Step 3 applies.

Finally, if \(S\) is connected and bipartite, its unsigned-incidence kernel is spanned by a vector with signs \(\pm1\) on the two sides. A \(Q_G\)-eigenvector of eigenvalue two is constant on each of the three original parts and sums to zero over these parts, impossible for three constants each equal to \(\pm1\). The eigenvalue-eight constant vector cannot alternate across edges. For eigenvalue four, every original two-vertex part must have opposite signs. There are exactly six edges of \(G\) crossing such a sign split, and \(S\) already has six edges; so \(S\) must contain all six, making \(F\) precisely two disjoint triangles, which was excluded. Therefore every remaining odd-unicyclic \(F\) yields a controllable \(U\).

**6. Existence and exact census.** To construct \(F\) for any \(r\ge3,k\ge2\), take a triangle through three different parts and attach each remaining vertex by one edge to a triangle vertex in a different part. This is a connected odd-unicyclic spanning graph, so its complement is a minimum placement; in the six-vertex case it is not the excluded pair of triangles.

Cauchy–Binet applied to \(Q_G=BB^\top\) yields
\[
\det Q_G=\sum_{F\subseteq E(G),\,|F|=n}(\det B_F)^2
=\sum_{F\text{ spanning odd-unicyclic}}4^{c(F)}.
\]
The explicit \(Q_G\)-spectrum in Step 1 evaluates this determinant to the product in the theorem. In the sole exceptional graph, each of the four forbidden two-triangle complements contributes \(4^2=16\), accounting for the correction \(64\). Moreover \(K_{2,2,2}\) on six vertices admits at most two odd-unicyclic components, and if it has two they must be triangles. Thus all 496 surviving complements are connected and contribute four each: \((2048-64)/4=496\). This proves both the weighted census and the ordinary six-vertex count.

## Verification

The standalone file `verify.py` uses exact rational row elimination. It enumerates all \(\binom{12}{6}=924\) six-edge complements of \(K_{2,2,2}\), checks unsigned-incidence rank against the odd-unicyclic criterion, and independently tests restrictions of explicit integer bases for all three nonkernel eigenspaces. It reports 500 odd-unicyclic candidates, four excluded complements and 496 controllable placements. It also verifies connected odd-unicyclic constructions and tests sampled complements for several larger multipartite sizes. Those larger samples illustrate the theorem but are not used as its infinite proof.

## Relationship to prior work

The PBH controllability criterion and the maximum-geometric-multiplicity lower bound are classical; Yuan and coauthors (2013) present their exact-network-controllability formulation. The spectral connection between signless incidence matrices and line graphs is established literature, including Ramane, Gudimani and Shinde (2013). Pang and coauthors (2017) analyze **different switchboard edge dynamics**, not the unit undirected line-graph Laplacian considered here. The new assertion is the all-parameter coordinate-placement equivalence for balanced multipartite line graphs, its four exceptional placements, and the corresponding actuator census. The spectral multiplicity and signless matrix-tree identities by themselves do not establish the full PBH characterization.

## Limitations

The result is about exact algebraic controllability, not conditioning, control energy, robustness or numerical implementation of the controls. The formula with \(4^{c(F)}\) is a weighted, not an ordinary, enumeration for general \(r,k\). The theorem is restricted to equal part sizes and equal edge weights. A complete survey of every specialist graph-controllability publication is not claimed; publication priority remains subject to further independent assessment.

## References

- Yuan, Z., Zhao, C., Di, Z., Wang, W.-X., Lai, Y.-C., *Exact controllability of complex networks*, Nature Communications 4 (2013), 2447. DOI: https://doi.org/10.1038/ncomms3447. First public journal date September 12, 2013.
- Ramane, H. S., Gudimani, S. B., Shinde, S. S., *Signless Laplacian Polynomial and Characteristic Polynomial of a Graph*, Journal of Discrete Mathematics (2013), 105624. DOI: https://doi.org/10.1155/2013/105624. Public date January 3, 2013.
- Pang, S.-P., Wang, W.-X., Hao, F., Lai, Y.-C., *Universal framework for edge controllability of complex networks*, Scientific Reports 7 (2017), 4224. DOI: https://doi.org/10.1038/s41598-017-04463-5. This reference studies a different system matrix.
