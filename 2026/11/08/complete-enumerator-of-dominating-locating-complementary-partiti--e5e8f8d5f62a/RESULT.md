# Complete enumerator of dominating--locating complementary partitions of clique coronas

## Finding

Let \(H\) be an arbitrary nonempty finite simple graph of order \(n\), not necessarily connected, and let \(r\ge 2\) be an integer. In the clique corona \(G=H\circ K_r\), one private copy \(Q_v\cong K_r\) is joined completely to each hub \(v\in V(H)\), with no edges from \(Q_v\) to other clusters. A locating-dominating set \(S\subseteq V(G)\) has the property that each vertex outside \(S\) has a nonempty open-neighborhood intersection with \(S\), and these intersections are distinct for different outside vertices. A role-specified complementary partition is an ordered pair \((S,T)\) with \(T=V(G)\setminus S\), where \(S\) is locating-dominating and \(T\) is dominating.

For each \(A\subseteq V(H)\), put
\[
c_H(A)=\bigl|N_H(A)\setminus A\bigr|,
\]
where \(N_H(A)\) is the union of open neighborhoods of vertices in \(A\). The complete enumerator of role-specified complementary partitions, weighted by the cardinality of their locating-dominating side, is
\[
\mathcal P_{H,r}(z)
=\sum_{(S,T)}z^{|S|}
=\sum_{A\subseteq V(H)}\sum_{j=0}^{c_H(A)}
\binom{c_H(A)}{j}r^{|A|+j}z^{rn-j}.
\]
Equivalently, as an identity in Laurent polynomials whose negative exponents cancel,
\[
\mathcal P_{H,r}(z)=z^{rn}\sum_{A\subseteq V(H)}
 r^{|A|}\left(1+\frac r z\right)^{c_H(A)}.
\]
The smallest locating-dominating side in such a partition has size exactly
\[
\min_{(S,T)}|S|=(r-1)n+\gamma(H),
\]
where \(\gamma(H)\) is the ordinary domination number. The number of partitions attaining the minimum is exactly
\[
\sum_{\substack{A\subseteq V(H)\\c_H(A)=n-\gamma(H)}}
 r^{|A|+n-\gamma(H)}.
\]
All counts concern labelled vertices and a specified locating-dominating role; partitions are not quotiented by graph automorphisms.

## Assumptions and scope

The base graph \(H\) is finite, simple and nonempty, and may contain isolated vertices or multiple components. The attached clique size is the fixed integer \(r\ge 2\). Each hub \(v\) and its private \(r\) vertices form a complete cluster \(C_v=\{v\}\cup Q_v\). Apart from edges inherited from \(H\), different clusters have no cross-edges. A set dominates a graph when every vertex outside the set has a neighbor inside it. A locating-dominating set additionally distinguishes every pair of vertices outside it by their open-neighborhood intersections with the set. The two classes in \((S,T)\) are distinguishable by their roles, even if both happen to be locating-dominating.

## Proof

**Local necessity.** Fix an admissible pair \((S,T)\) and a hub \(v\). Two different vertices of \(Q_v\) have identical neighbors outside themselves. If both were in \(T\), their intersections \(N_G(\cdot)\cap S\) would be identical, contradicting location by \(S\). Thus at most one vertex of \(Q_v\) lies in \(T\). Since the complementary set \(T\) dominates \(S\), at least one member of \(C_v\) lies in \(T\): otherwise each of the private vertices in \(Q_v\subseteq S\) would have no neighbor in \(T\). Consequently exactly one of the following cases occurs:

- **A:** \(v\in S\), exactly one private clique vertex lies in \(T\). There are \(r\) choices of that vertex, and the cluster contributes \(r\) vertices to \(S\).
- **B:** \(v\in T\), all \(r\) private vertices lie in \(S\). There is one choice, and the cluster contributes \(r\) vertices to \(S\).
- **C:** \(v\in T\), exactly one private vertex lies in \(T\). There are \(r\) choices of that vertex, and the cluster contributes \(r-1\) vertices to \(S\).

In case C, let \(x\) be the omitted private vertex. Both \(v\) and \(x\) belong to \(T\), and their selected-neighbor signatures are
\[
N_G(x)\cap S=Q_v\cap S,
\qquad
N_G(v)\cap S=(Q_v\cap S)\cup(N_H(v)\cap A),
\]
where \(A=S\cap V(H)\). These are distinct exactly when \(N_H(v)\cap A\ne\varnothing\). Thus case C requires \(v\in N_H(A)\setminus A\).

**Sufficiency and complete classification.** Choose arbitrary \(A\subseteq V(H)\). For every \(v\in A\), choose case A and one of its \(r\) omitted private vertices. For every \(v\notin A\), choose case B, or choose case C provided \(v\in N_H(A)\), again choosing one omitted private vertex. Every chosen cluster contains a vertex of \(T\), so \(T\) dominates all vertices of \(S\). Every vertex of \(T\) has at least \(r-1\ge 1\) private neighbors in \(S\), so \(S\) dominates \(T\). Vertices in \(T\) from distinct clusters have distinct selected-neighbor signatures because each contains a nonempty subset of private vertices from its own cluster and no vertex of another cluster has those private vertices as neighbors. The only two outside vertices in one cluster arise in case C, and the required neighbor of \(v\) in \(A\) distinguishes them, as calculated above. Thus \(S\) locates \(T\). Every valid pair was necessarily of these forms, and the construction specifies it uniquely.

**Enumerator.** The set \(A\) of selected hubs determines \(|A|\) cases A, each with \(r\) choices. Exactly \(c_H(A)\) outside hubs are eligible for case C. Choosing any \(j\) of them contributes \(\binom{c_H(A)}j\) choices of hubs and \(r^j\) choices of their omitted private vertices. Each case C reduces the size of \(S\) by one relative to the baseline \(rn\) obtained from cases A and B. Therefore the coefficient contribution is \(\binom{c_H(A)}j r^{|A|+j}z^{rn-j}\). Summing over \(A\) and \(j\) proves the displayed polynomial.

**Minimum and extremal count.** For any \(A\subseteq V(H)\), the set \(D=A\cup(V(H)\setminus N_H[A])\) dominates \(H\) and has size \(n-c_H(A)\). Hence \(c_H(A)\le n-\gamma(H)\). If \(A\) is a minimum dominating set of \(H\), then every vertex outside \(A\) has a neighbor in \(A\); therefore \(c_H(A)=n-\gamma(H)\). Thus \(\max_A c_H(A)=n-\gamma(H)\), and the lowest exponent in the polynomial is \(rn-(n-\gamma(H))=(r-1)n+\gamma(H)\). The extremal coefficient is obtained precisely by taking \(j=c_H(A)=n-\gamma(H)\) in the enumerator. This gives the stated count, completing the proof.

## Verification

The included standalone Python script `verify.py` independently constructs the original graph adjacency, enumerates every possible choice of \(S\), and checks the defining domination and location conditions directly for each choice. It also enumerates the domination number of the base graph separately. Its output agrees with the polynomial coefficients and minimum formula for all labelled simple graphs of orders one through four under the parameters described in `VERIFICATION.md`, and for four additional profiles. One sample is \(H=P_4\), \(r=2\):
\[
\mathcal P_{P_4,2}(z)=80z^6+168z^7+81z^8.
\]
These finite checks corroborate, but do not replace, the proof above.

## Relationship to prior work

Chakraborty, Foucaud, Henning and Laihonen (2026) established the existence of complementary locating-dominating/dominating partitions for every isolate-free graph and illustrated the one-leaf corona \(H\circ K_1\). Their published proof does not classify or enumerate all such partitions for clique coronas with \(r\ge2\), nor does it recover \(\gamma(H)\) from their smallest locating-dominating sides. Foucaud, Maniya, Paul and Pradhan (2025) considered partitions into two locating-dominating sets for specified twin-free graph classes, a different condition. Omamalin, Canoy and Rara (2014) studied locating **total** domination in coronas, which imposes a stronger condition on selected-set internal neighborhoods; this does not classify the present complementary partitions. These comparisons do not establish absolute historical priority; other equivalent counting results under different terminology remain possible.

## Limitations

The theorem requires \(r\ge2\): the nonempty private selected-neighbor signature used to distinguish clusters fails for the pendant-leaf case. It concerns ordinary locating domination, not identifying codes or locating total domination. The enumerator is a finite exact formula over all subsets of the base graph and is not a polynomial-time evaluation claim. Vertex labels and the designated role of \(S\) are retained. No independent external mathematical validation has been performed, and literature priority is provisional.

## References

- D. Chakraborty, F. Foucaud, M. A. Henning, and T. Laihonen, *A Note on Partitioning the Vertex Set of a Graph into a Dominating Set and a Locating Dominating Set*, Electronic Journal of Combinatorics **33** (2026), #P1.51, published 2026-03-13. DOI: `10.37236/14049`. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i1p51
- F. Foucaud, P. Maniya, K. Paul, and D. Pradhan, *Locating-dominating partitions for some classes of graphs* (2025), arXiv:`2506.12933`. https://arxiv.org/abs/2506.12933
- B. N. Omamalin, S. R. Canoy, Jr., and H. M. Rara, *Locating total dominating sets in the join, corona and composition of graphs*, Applied Mathematical Sciences **8** (2014), 2363–2374. DOI: `10.12988/ams.2014.43205`.
