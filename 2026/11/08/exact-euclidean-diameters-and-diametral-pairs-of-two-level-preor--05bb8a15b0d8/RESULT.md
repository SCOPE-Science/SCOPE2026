# Exact Euclidean diameters and diametral pairs of two-level preorder polytopes

## Finding

Let \(m\ge 1\) and \(n\ge 2\) be integers. Let \(\tau_{m,n}\) be the ordinal sum of an \(m\)-element antichain and an \(n\)-element antichain. Its preorder polytope in its standard coordinate realization is
\[
\mathcal Q_{m,n}=\left\{(x,y)\in\mathbb R_{\ge0}^{m+n}: x_i\le1\ (1\le i\le m),\quad \sum_{i=1}^m x_i+\sum_{j\in J}y_j\le m+|J|\quad\text{for every }J\subseteq[n]\right\}.
\]
(The inequality for \(J=\varnothing\) is redundant.) Distances below are ordinary Euclidean distances in \(\mathbb R^{m+n}\), not shortest-path distances in the one-skeleton.

**Theorem.** The exact squared Euclidean diameter is
\[
\boxed{\operatorname{diam}_2(\mathcal Q_{m,n})^2=2(m+1)^2+n-2.}
\]
Every unordered diametral pair has the following form, and each such pair is diametral. Pick two distinct indices \(i,j\in[n]\), and for every \(\ell\in[n]\setminus\{i,j\}\) choose \(\varepsilon_\ell\in\{0,1\}\). The pair is \(\{(0^m,v),(0^m,w)\}\), where
\[
 v_i=m+1,\quad v_j=0,\quad w_i=0,\quad w_j=m+1,\quad
 v_\ell=\varepsilon_\ell,\quad w_\ell=1-\varepsilon_\ell\quad(\ell\ne i,j).
\]
Consequently the exact number of distinct **unordered** diametral pairs is
\[
\boxed{\binom n2\,2^{n-2}=n(n-1)2^{n-3}.}
\]
Notably this count does not depend on the size \(m\) of the lower antichain, although the diameter does.

## Assumptions and scope

The polytope is the full-dimensional preorder polytope of Athanasiadis and Chapoton, not Stanley's order polytope, its polar, or a graph whose one-skeleton is being measured. The first antichain has size \(m\ge1\), the upper antichain has size \(n\ge2\), both are labeled, and each lower element precedes every upper element. The empty-subset inequality is harmless; no strict inequality or genericity assumption is imposed. The Euclidean metric is inherited from the displayed \(m+n\) coordinate axes and is not invariant under arbitrary unimodular affine transformations.

## Proof

**1. Exact finite generating set.** All lower ideals give \(0\le x_i\le1\). Fix \(x\in[0,1]^m\), write \(s=m-\sum_i x_i\ge0\), and let \(\Delta_n^0=\operatorname{conv}\{0,e_1,\ldots,e_n\}\). We first claim that the constraints on the upper coordinates are equivalent to
\[
 y\in[0,1]^n+s\Delta_n^0. \tag{1}
\]
The forward implication follows by taking \(b_j=\min\{y_j,1\}\) and \(t_j=(y_j-1)_+\). For the subset \(J=\{j:y_j>1\}\), the ideal inequality gives \(\sum_jt_j\le s\); hence \(y=b+t\), with \(b\in[0,1]^n\), \(t\ge0\), and \(\sum_jt_j\le s\). The reverse implication follows because \(\sum_{j\in J}b_j\le|J|\) and \(\sum_{j\in J}t_j\le s\). This includes the boundary \(s=0\).

Define the finite set
\[
G_{m,n}=\Bigl\{(a,b+(m-|a|)e_j):a\in\{0,1\}^m,\ b\in\{0,1\}^n,\ j\in\{0,1,\ldots,n\}\Bigr\},\quad e_0=0,\quad |a|=\sum_i a_i.
\]
Every such point satisfies all defining inequalities by (1). Conversely, for any feasible \((x,y)\), write \(y=b+s z\) with \(b\in[0,1]^n\), \(z\in\Delta_n^0\), and express \(x\) as a convex combination \(x=\sum_a\lambda_a a\) of zero-one vectors. Then
\[
(x,y)=\sum_a\lambda_a\bigl(a,b+(m-|a|)z\bigr).
\]
For each \(a\), the last point is a convex combination of members of \(G_{m,n}\) by decomposing \(b\) into cube vertices and \(z\) into simplex vertices. Thus \(\mathcal Q_{m,n}=\operatorname{conv}G_{m,n}\). No assertion that every member of this generating set is a vertex is needed.

**2. Universal distance bound.** The Euclidean distance between two points of a compact polytope is maximized at two vertices. In fact, strict convexity of the squared Euclidean norm ensures that both endpoints of any diametral pair are vertices: if one endpoint were a nontrivial convex combination, at least one constituent would be strictly farther from the other endpoint. Hence both endpoints belong to \(G_{m,n}\).

Write two members of the set as \((a,b+k e_i)\) and \((a',b'+k'e_j)\), where \(k=m-|a|\) and \(k'=m-|a'|\) belong to \(\{0,\ldots,m\}\), \(b,b'\in\{0,1\}^n\), and \(i,j\in\{0,\ldots,n\}\). Let \(h\) be the Hamming distance between \(a\) and \(a'\). Since \(|a|=m-k\) and \(|a'|=m-k'\),
\[
0\le h\le(m-k)+(m-k'). \tag{2}
\]
If \(i,j\) are distinct nonzero indices, the two special upper-coordinate differences have absolute values at most \(k+1\) and \(k'+1\); each of the remaining \(n-2\) upper-coordinate differences has absolute value at most one. By (2),
\[
\begin{aligned}
\|(a,b+k e_i)-(a',b'+k'e_j)\|_2^2
&\le(k+1)^2+(k'+1)^2+(n-2)+(m-k)+(m-k')\\
&=2(m+1)^2+n-2-(m-k)(m+k+1)-(m-k')(m+k'+1)\\
&\le2(m+1)^2+n-2. \tag{3}
\end{aligned}
\]
Equality in (3) requires \(k=k'=m\), hence \(a=a'=0^m\).

If the two excess indices coincide and are nonzero, the exceptional coordinate difference is at most \(|k-k'|+1\le m+1\). If at least one excess index is zero, there is at most one exceptional coordinate with difference exceeding one, again bounded by \(m+1\). In either situation, using \(h\le m\), the squared distance is at most
\[
(m+1)^2+(n-1)+m < 2(m+1)^2+n-2\qquad(m\ge1). \tag{4}
\]
(The case of no exceptional coordinates is also covered.) Therefore every diametral pair must have distinct nonzero excess indices.

**3. Exact equality and count.** With \(k=k'=m\), equality requires special upper differences of absolute value \(m+1\): at the first peak index \(i\), the first endpoint has \(b_i=1\) and the second has \(b'_i=0\); at the second peak index \(j\), the first has \(b_j=0\) and the second has \(b'_j=1\). At each other upper coordinate the two zero-one values must be complementary. These are precisely the pairs in the theorem. The indicated vectors belong to \(G_{m,n}\), their squared distance is exactly \(2(m+1)^2+n-2\), and hence equality is attained.

Choose an unordered pair of peak indices, then distinguish the endpoint peaking at the smaller index. The other \(n-2\) binary coordinates of that endpoint can be chosen independently; the opposite endpoint is forced. There are therefore \(\binom n2 2^{n-2}\) unordered pairs, with no repetitions. This completes the proof.

## Verification

Run `python3 verify_preorder_diameter.py` in the directory containing this file (Python standard library only). It independently enumerates the finite generator set, checks every generated point against the original order-ideal inequalities, checks all pairwise squared distances and every equality pair for \(1\le m\le4\), \(2\le n\le5\), and separately enumerates lattice points from the original inequalities for \(1\le m\le2\), \(2\le n\le3\). The verifier reports `EXACT_CHECKS_OK 4983576` when all exact integer assertions pass. These finite checks corroborate the proof; they do not establish the unbounded theorem.

## Relationship to prior work

Athanasiadis and Chapoton [1] define preorder polytopes and study the ordinal sum of two antichains in Section 9.2, where Proposition 9.2 supplies lattice-point and rank-generating formulas. Their general Theorems 1.4 and 1.5 give integrality, generalized-permutohedron structure, and Ehrhart–zeta duality. The present theorem concerns a different, metric invariant and a full equality classification; neither follows from those enumerative formulas without the distance argument here.

Luo [2] proves an ordinal-sum factorization for the Ehrhart series of *polar preorder polytopes*, using a piecewise unimodular shear. The object there is a different polytope, and such shears do not preserve Euclidean distances; that result does not imply the present exact metric formula.

The published star-hypergraphic diameter theorem [3] treats a cardinality-weighted Minkowski sum of simplices in a fixed-sum hyperplane, and its equality pairs are a single hub vertex versus leaf permutations. Our preorder polytope has a box plus variable simplex slack, and its diameter pairs are two *distinct* upper-coordinate peaks with complementary binary backgrounds. Neither the objects nor their metric classifications identify under the standard Euclidean realization. Results on graph diameters of order polytopes concern different polytopes and combinatorial graph distances [4].

## Limitations

The theorem is restricted to ordinal sums of two antichains with at least two upper elements, in the specified coordinate metric. It does not classify arbitrary preorders, three or more levels, Santaló points, John ellipsoids, or one-skeleton graph diameters. The literature search and accessible published-record comparisons provide best-knowledge priority evidence, not a proof of global novelty. No independent mathematical audit has been performed.

## References

1. C. A. Athanasiadis and F. Chapoton, *Polytopes and posets associated to preorders*, arXiv:2605.26916v1, first public 26 May 2026, especially Definition (2), Theorem 1.5, and Section 9.2. https://arxiv.org/html/2605.26916
2. C. Luo, *A proof of the Athanasiadis–Chapoton ordinal-sum conjecture*, arXiv:2609.28507v1, first public 19 September 2026, especially Theorems 1.1–1.2. https://arxiv.org/abs/2609.28507
3. *Diametral rigidity of cardinality-weighted star hypergraphic polytopes*, published mathematical record, 11 October 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-diametral-rigidity-of-cardinality-weighted-star-hypergraphic-pol--fc74a3f40add/RESULT.md
4. J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv preprint, 2026; bibliographic overview https://www.arxiv.symmetricfunctions.com/keyword/ordinal%20sum .
