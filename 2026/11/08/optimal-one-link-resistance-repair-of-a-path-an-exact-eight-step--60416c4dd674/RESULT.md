# Optimal one-link resistance repair of a path: an exact eight-step placement law

## Finding

Let \(P_n\) be the unweighted path on labeled vertices \(1,2,\ldots,n\), where \(n\ge3\). Add exactly one unit-conductance edge \(\{i,j\}\) with \(j-i\ge2\). The Kirchhoff index is the sum \(K(G)=\sum_{u<v}R_G(u,v)\) of all effective resistances.

**Theorem.** With \(k=\lfloor(n-2)/8\rfloor\), the **unique** choice minimizing \(K(P_n+\{i,j\})\) is
\[
\boxed{(i,j)=(k+1,n-k).}
\]
Writing \(d=n-2k-1\), the exact minimum is
\[
\boxed{K_{\min}(n)=\frac{n(n^2-1)}6-\frac{nd(3nd-2d^2+2)}{12(d+1)}.}
\]
In particular, the optimal connection approaches one-eighth and seven-eighths of the path; \(K_{\min}(n)=7n^3/96+O(n^2)\). Thus the optimal single unit edge removes asymptotically \(9/16\) of the unaugmented path's total resistance. The first move away from an end-to-end connection occurs at \(n=10\): connect vertices \(2\) and \(9\).

## Assumptions and scope

Every original path edge and the added edge has resistance exactly one. Vertices are labeled along the path and an added edge must be absent from the original path, so \(n\ge3\) and \(1\le i<j\le n\) with \(j-i\ge2\). Optimization is over the one new edge only, not edge weights or an arbitrary number of links. Reversal of the path maps a pair \((i,j)\) to \((n+1-j,n+1-i)\); the displayed optimizer is itself reflection-invariant, so uniqueness is literal in the labeled problem.

## Proof

**1. An exact update formula.** Let \(L\) be the combinatorial Laplacian of \(P_n\) and let \(b=e_i-e_j\). On the mean-zero subspace, the rank-one inverse update is
\[
K(P_n+\{i,j\})=K(P_n)-\frac{n\,b^{\mathsf T}(L^+)^2b}{1+b^{\mathsf T}L^+b},\qquad K(P_n)=\frac{n(n^2-1)}6.
\]
Here \(L^+\) is the Moore–Penrose inverse. As the path's resistance between \(i\) and \(j\) is \(d=j-i\), the denominator is \(d+1\). The path potential \(y_t=\min\{d,\max\{0,t-i\}\}\), for \(1\le t\le n\), has the same centered vector as \(L^+b\), up to sign. With \(r=n-j\), direct summation gives
\[
S:=\sum_t y_t=\frac{d(d+1)}2+dr,\quad Q:=\sum_t y_t^2=\frac{d(d+1)(2d+1)}6+d^2r.
\]
Consequently the gain in the Kirchhoff index is exactly \(F=(nQ-S^2)/(d+1)\). Put \(\ell=i-1\); then \(n=d+\ell+r+1\). Completing the square yields
\[
\boxed{F(d,\ell,r)=g_n(d)-\frac{d^2(\ell-r)^2}{4(d+1)},\qquad g_n(d)=\frac{nd(3nd-2d^2+2)}{12(d+1)}.} \tag{1}
\]
For fixed \(d\), \(\ell+r=n-1-d\). The largest gain is therefore obtained at the most balanced possible pair \(\ell,r\); for even sum this pair is uniquely equal, and for odd sum there are two reflected balanced pairs.

**2. An odd number of exterior edges cannot be optimal.** For an odd value of \(s=\ell+r\), let \(d=n-1-s\). Its best possible gain is \(g_n(d)-q(d)\) where \(q(d)=d^2/[4(d+1)]\). Its two neighboring even values of \(s\) have gains \(g_n(d-1)\) and \(g_n(d+1)\), when those are admissible.

For \(n\ge13\), put \(b_n=(2n+3)/3\). If \(2\le d\le b_n\), then
\[
\frac{12}{n}[g_n(d+1)-g_n(d)]=H_n(d):=3n-4d-\frac{3n}{(d+1)(d+2)}>0. \tag{2}
\]
Indeed, \(H_n'(d)=-4+3n(2d+3)/[(d+1)^2(d+2)^2]\); its second summand is strictly decreasing, so \(H_n\) has at most one interior maximum and its minimum on this interval is at an endpoint. The endpoint values are \(H_n(2)=11n/4-8>0\) and
\[
H_n(b_n)=\frac{n-12}{3}-\frac{27n}{(2n+6)(2n+9)}>0.
\]
For the latter, write \(n=13+t\) with \(t\ge0\); positivity follows from the integer polynomial \(4t^3+138t^2+1173t+67>0\). Thus the even neighbor with larger \(d\) improves the gain.

If instead \(d\ge b_n\), both even neighbors are admissible and, by direct second difference,
\[
\frac{g_n(d-1)+g_n(d+1)}2-g_n(d)=-\frac n6+\frac{n^2}{4d(d+1)(d+2)}.
\]
But \(q(d)>n/6\), since \(d^2/(d+1)>d-1\ge 2n/3\). Consequently the average gain of those two even neighbors is strictly greater than \(g_n(d)-q(d)\). Thus no odd \(s\) is globally optimal. For \(3\le n\le12\), direct evaluation of the exact rational formula (1) gives the unique winning pairs: \((1,n)\) for \(3\le n\le9\), and \((2,n-1)\) for \(10\le n\le12\). These ten small cases are also reproduced by the standalone checker.

**3. Optimize the balanced even cases.** Write \(s=2k\), so \(\ell=r=k\) and \(d=n-1-2k\). The candidate gain is \(g_n(d)\). For two consecutive admissible values of \(k\), elementary algebra gives
\[
g_n(d-2)-g_n(d)=\frac{nP(n,k)}{6(d-1)(d+1)},\tag{3}
\]
where
\[
\begin{aligned}
P(n,k)={}&n^3-(12k+12)n^2+(36k^2+60k+23)n\\
&-32k^3-72k^2-40k.
\end{aligned}
\]
For integer \(n\ge2k+5\), the sign is **positive exactly if** \(n\ge8k+10\). To verify the positive half, substitute \(n=8k+10+t\), \(t\ge0\), obtaining
\[
P=t^3+6(2k+3)t^2+(36k^2+108k+83)t+6(4k+5)>0.
\]
For \(2k+5\le n\le8k+9\), the two endpoint values are \(P(2k+5,k)=-12(7k+5)\) and \(P(8k+9,k)=-36(k+1)^2\). Moreover, \(\partial P/\partial n\) has roots \(4k+4\pm\sqrt{36k^2+108k+75}/3\). The smaller is below \(2k+3\); therefore on the admissible interval \(P\) decreases and then increases, and is bounded above by its negative endpoint values. This proves the sign assertion without finite enumeration.

Set \(K=\lfloor(n-2)/8\rfloor\). For every admissible \(k<K\), one has \(n\ge8k+10\), and (3) shows that the gain strictly increases when \(k\) is incremented. For every admissible \(k\ge K\), one has \(n\le8k+9\), and (3) shows that the gain strictly decreases on incrementing \(k\). Therefore the unique even-case maximizer is \(k=K\). Combining this with step 2 proves the classification and the exact formula.

**4. Scale of the improvement.** The selected integer satisfies \(k=n/8+O(1)\) and \(d=3n/4+O(1)\). Substitution into (1) yields \(g_n(d)=3n^3/32+O(n^2)\), whereas \(K(P_n)=n^3/6+O(n)\). The remaining index is \(7n^3/96+O(n^2)\) and the removed fraction approaches \(9/16\).

## Verification

The accompanying \(\texttt{verify.py}\) uses only Python's standard library and replays three independent calculations: the explicit potential-vector variance versus the closed gain formula, a grounded-Laplacian rational inverse and all-pairs effective resistances for small graphs, and exhaustive exact-rational optimization across all distinct available links for \(3\le n\le140\). It also checks the adjacent balanced-candidate sign claim over these finite inputs. The code prints \(\texttt{VERIFY_OK 5868}\) upon success. These finite checks are not a substitute for the complete analytical proof in Steps 1–4.

## Relationship to prior work

The Kirchhoff index and its connection to network robustness, spectral consensus, and edge augmentation are classical. Qi–Zhou–Du (2013) study extremal unicyclic graphs under fixed order and matching number; those classes are not a one-edge augmentation of a fixed path. Abbas–Egerstedt (2012) analyze optimal additions to petal/star-type networks rather than classifying path shortcut endpoints. De Ridder et al. (2019) develop a quantum algorithm for selecting one optimal new edge on general networks, and Zhou–Zehmakan–Zhang (2025) develop efficient approximation algorithms for edge addition; the relevant inspected sections do not give this exact \(n\)-dependent path endpoint classification. Kooij–Achterberg (2023) establish hardness for general graph augmentation, which neither implies nor contradicts a solvable special case.

The distinguishing claim here is the **complete unique optimal-endpoint rule** for a path, its exact minimum, and the sharp eight-step transition. General effective-resistance update formulas, which are already known, are used as proof tools rather than claimed as novel.

## Limitations

The result concerns a single unit-resistance shortcut on an otherwise unit-resistance path, not non-unit added weights, multiple shortcuts, effective-resistance diameter, or a different objective such as algebraic connectivity. The exact classification has a self-contained proof and finite rational checks, but has not received independent mathematical review. The available inspection of Abbas–Egerstedt's archival PDF was through indexed text; its rendered page view returned an access error, and complete coverage of all older or unindexed literature cannot be guaranteed. Any equivalent existing classification would supersede the originality assessment.

## References

- X. Qi, B. Zhou, Z. Du, *The Kirchhoff indices and the matching numbers of unicyclic graphs*, first public arXiv posting 2013-04-29, https://arxiv.org/abs/1304.7546 .
- W. Abbas, M. Egerstedt, *Robust Graph Topologies for Networked Systems*, archival PDF, https://repository.gatech.edu/server/api/core/bitstreams/a34a558e-8c73-4469-8866-48012421c2da/content .
- F. de Ridder, N. Neumann, T. Veugen, R. Kooij, *A Quantum Algorithm for Minimising the Effective Graph Resistance upon Edge Addition*, 2019, https://ir.cwi.nl/pub/28632/28632.pdf .
- X. Zhou, A. N. Zehmakan, Z. Zhang, *Efficient Algorithms for Minimizing the Kirchhoff Index via Adding Edges*, first arXiv posting 2025-03-27, https://arxiv.org/abs/2503.21409 .
- R. E. Kooij, M. A. Achterberg, *Minimizing the effective graph resistance by adding links is NP-hard*, 2023, https://doi.org/10.1016/j.orl.2023.10.002 .
