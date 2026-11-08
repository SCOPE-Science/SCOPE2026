# Exponential-to-polynomial optimal-multicover multiplicity across three spider lengths

## Finding
Let \(S_{r,\ell}\) be the tree formed by identifying one endpoint of \(r\) vertex-disjoint paths of length \(\ell\), with their individual arms distinguished by the vertex labels. Fix integers \(r\ge3\) and \(k\ge1\). A total \(\{k\}\)-dominating function is \(f:V(S_{r,\ell})\to\{0,1,\ldots,k\}\) such that \(\sum_{u\in N(v)}f(u)\ge k\) at every vertex. Let \(W_{r,\ell}(k)\) be the minimum of \(\sum_v f(v)\) and let \(M_{r,\ell}(k)\) be the number of **distinct labelled** minimizing functions. For the three consecutive arm lengths \(\ell=3,4,5\), the complete optimal weights and multiplicities are
\[
\begin{array}{c|c|c}
\ell&W_{r,\ell}(k)&M_{r,\ell}(k)\\\hline
3&2rk&(k+1)^r-\binom{k+r-1}{r}\\
4&(2r+1)k&\binom{k+r-1}{r-1}\\
5&(2r+2)k&\binom{k+2r-1}{2r-1}.
\end{array}
\]
The new contribution is the **exact enumeration and classification of every optimal function for all \(r,k\)**, not the scalar optimal weights. In particular, for each fixed \(k\ge1\), the counts change from exponential to polynomial growth when each arm is lengthened from three to four:
\[
M_{r,3}(k)\sim(k+1)^r,\qquad
M_{r,4}(k)\sim\frac{r^k}{k!},\qquad
M_{r,5}(k)\sim\frac{(2r)^k}{k!}\quad(r\to\infty).
\]

## Assumptions and scope
The graphs are finite, undirected, simple, and labelled. The central vertex is \(c\); for each \(i\in\{1,\ldots,r\}\), the vertices of arm \(i\) in their order away from \(c\) are \(v_{i,1},\ldots,v_{i,\ell}\). Vertex labels and arm identities are fixed, so functions differing on interchanged arms are counted separately. The number of arms is at least three, so the examples are not caterpillars. Each assigned weight is an integer between zero and \(k\), inclusive; the open, not closed, neighborhood is used. The theorem counts minimum-weight assignments, not all feasible assignments and not orbit classes under automorphisms. An isolated vertex never arises.

## Proof
All inequalities below use the definition \(\sum_{u\in N(v)}f(u)\ge k\), including at chosen vertices themselves. For every arm, its leaf forces the weight of its penultimate vertex to equal \(k\), since no value exceeds \(k\).

**Three-edge arms.** Abbreviate the arm weights as \(a_i=f(v_{i,1})\), \(b_i=f(v_{i,2})\), \(d_i=f(v_{i,3})\), and \(t=f(c)\). The leaf forces \(b_i=k\). The remaining nonautomatic constraints are \(a_i+d_i\ge k\) for each arm and \(\sum_i a_i\ge k\) at the center. Indeed, the condition at \(v_{i,1}\) is \(t+b_i\ge k\), automatic since \(b_i=k\). It follows that
\[
\sum_v f(v)=rk+t+\sum_i(a_i+d_i)\ge 2rk+t\ge2rk.
\]
Equality holds precisely when \(t=0\), every \(a_i+d_i=k\), and \(\sum_i a_i\ge k\). Each \(a_i\) can be chosen independently from \(\{0,\ldots,k\}\) before the final condition. Among the \((k+1)^r\) vectors, those with \(\sum a_i<k\) number \(\binom{k+r-1}{r}\) by stars and bars (the individual upper bounds are automatic in this range). The displayed count follows, and choosing any one \(a_i=k\) proves attainability.

**Four-edge arms.** Write the five successive vertex weights on the path starting at the center as \((t,a_i,b_i,d_i,e_i)\). The leaf constraint gives \(d_i=k\). The nonautomatic inequalities are
\[
b_i+e_i\ge k,\qquad t+b_i\ge k,\qquad\sum_i a_i\ge k.
\]
The vertex \(v_{i,2}\) is already dominated by \(a_i+d_i\ge k\). Hence
\[
\sum_v f(v)=rk+t+\sum_i a_i+\sum_i(b_i+e_i)\ge(2r+1)k+t.
\]
Equality is attained with \(t=0\), \(d_i=b_i=k\), \(e_i=0\), and any \(a_i\ge0\) summing to \(k\). Conversely, equality forces \(t=0\), \(\sum_i a_i=k\), and \(b_i+e_i=k\); the condition \(t+b_i\ge k\) then forces \(b_i=k\) and \(e_i=0\). Thus the minimizing functions are indexed bijectively by the weak compositions \((a_1,\ldots,a_r)\) of \(k\), numbering \(\binom{k+r-1}{r-1}\). All choices obey \(a_i\le k\).

**Five-edge arms.** Write the six successive weights beginning at the center as \((t,a_i,b_i,d_i,e_i,h_i)\). The leaf gives \(e_i=k\). The remaining constraints are
\[
d_i+h_i\ge k,\quad a_i+d_i\ge k,\quad t+b_i\ge k,\quad\sum_i a_i\ge k,
\]
while \(b_i+e_i\ge k\) is automatic. As \(b_i\ge k-t\), summing gives
\[
\begin{aligned}
\sum_v f(v)&=rk+t+\sum_i(a_i+b_i+d_i+h_i)\\
&\ge rk+t+k+r(k-t)+rk\\
&=(3r+1)k-(r-1)t\ge(2r+2)k.
\end{aligned}
\]
Since \(r\ge3\), equality forces \(t=k\), all \(b_i=0\), \(\sum_i a_i=k\), and all \(d_i+h_i=k\). The remaining inequality \(a_i+d_i\ge k\) requires \(k-a_i\le d_i\le k\). For each weak composition \((a_i)\) of \(k\) there are exactly \(\prod_i(a_i+1)\) choices of \((d_i)\), and each determines \(h_i=k-d_i\). These assignments satisfy every constraint, so the bound is attained. Finally,
\[
\sum_{a_1+\cdots+a_r=k}\prod_i(a_i+1)
=[z^k]\left(\sum_{a\ge0}(a+1)z^a\right)^r
=[z^k](1-z)^{-2r}
=\binom{k+2r-1}{2r-1}.
\]
All variables are automatically in \(\{0,\ldots,k\}\). This also gives the full structural classification for five-edge arms.

For fixed \(k\), the three asymptotics are obtained directly from these exact formulas. In the three-edge case, the subtracted binomial coefficient is polynomial in \(r\), whereas the first term is exponential; the two other binomial coefficients are polynomials in \(r\) of degree \(k\) with the indicated leading terms. This proves the claimed change of growth type.

## Verification
The standalone standard-library program `artifacts/verify.py` independently enumerates all local arm labels and runs an exact minimum-cost dynamic program for \(\ell\in\{3,4,5\}\), \(2\le r\le5\), and \(1\le k\le3\), without using the structural classification in the dynamic programming logic. In addition, it directly enumerates every vertex-labelled assignment in five smaller instances and checks every open-neighborhood inequality. The program's output ends with `VERIFY_OK`; execute `python3 artifacts/verify.py` from the package directory. These checks are finite corroboration. The proof for all integers \(r\ge3,k\ge1\) is the exact equality-case analysis above.

## Relationship to prior work
Escalante, Tolomei, and Lopez Pujato [1] prove that the minimum *weight* of a total \(\{k\}\)-dominating function on any caterpillar scales linearly with \(k\), and explicitly discuss the extension to arbitrary trees. The three spider families here are not caterpillars for \(r\ge3\); the claimed novelty is not merely their optimal weight, but the exact **numbers and complete classifications of all minimum functions**, together with the exponential-versus-polynomial change under arm subdivision. Lee [2] gives an earlier, more general optimization approach for total \(\{k\}\)-domination on chordal bipartite graphs; its linear-programming result provides stronger coverage for numerical optimal weights (including trees). Consequently the scalar entries in the middle column are **not claimed independently novel**. That algorithmic optimum-value result does not enumerate the minimizing functions or establish the three multiplicity formulas. Petr, Portier, and Versteegen [3] study how many *ordinary* minimum dominating and total dominating sets forests possess; the case \(k=1\) lies within that older area of study and is not isolated as a new discovery here. The present two-parameter counting formulas, including every \(k>1\), refine both value-only and ordinary-set results.

## Limitations
No formula for general nonuniform spiders or for all arm lengths is asserted. The results count named optimal assignments rather than automorphism orbits. No claim is made to have resolved the all-trees numerical question independently of the older linear-programming literature. Searches can miss unindexed equivalent formulas; historical priority of the optimum-function census is provisional. Independent mathematical validation has not been performed.

## References
[1] M. Escalante, P. Tolomei, and M. I. Lopez Pujato, *Total \(\{k\}\)-domination in caterpillars: Structural properties and exact results*, arXiv:2610.27181, first public 2026-10-19; https://arxiv.org/abs/2610.27181 .

[2] C.-M. Lee, *Exploring Dominating Functions and Their Complexity in Subclasses of Weighted Chordal Graphs and Bipartite Graphs*, first available as preprint 2024-11-27, subsequently *Mathematics* **13** (2025), 403; https://www.preprints.org/manuscript/202411.2117 ; https://doi.org/10.3390/math13030403 .

[3] J. Petr, J. Portier, and L. Versteegen, *On the number of minimum dominating sets and total dominating sets in forests*, arXiv:2206.13182, first public 2022-06-27, *J. Graph Theory* **106** (2024), 976–993; https://arxiv.org/abs/2206.13182 .
