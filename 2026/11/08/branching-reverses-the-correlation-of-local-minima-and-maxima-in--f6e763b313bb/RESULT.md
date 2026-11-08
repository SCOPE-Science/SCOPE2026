# Branching reverses the correlation of local minima and maxima in random tree labelings

## Finding

Let the vertices of a finite tree carry independent identically distributed continuous labels. Let \(M\) count strict local minima and \(P\) count strict local maxima (relative to all adjacent vertices). For the complete rooted \(m\)-ary tree \(T_{m,h}\) of height \(h\), the following branching dichotomy holds.

**Path regime.** For \(m=1\), the tree is the path with \(n=h+1\) vertices. For every \(n\ge4\),
\[
\operatorname{Cov}(M,P)=\frac{8n-37}{180},\qquad
\operatorname{Var}(M)=\operatorname{Var}(P)=\frac{2(n+1)}{45},\qquad
\operatorname{Corr}(M,P)=1-\frac{45}{8(n+1)}.
\]
For \(n=3\) the covariance is \(-1/9\); on a two-vertex path both counts are identically one. Thus the covariance changes sign at the first possible order \(n=5\), and the correlation tends to \(+1\) along paths.

**Branching regime.** For every integer \(m\ge2\) and every \(h\ge1\),
\[
\boxed{\operatorname{Cov}_{T_{m,h}}(M,P)<0.}
\]
For each fixed \(m\ge2\), as \(h\to\infty\), with \(n=|T_{m,h}|\),
\[
\operatorname{Cov}(M,P)=n L_m+O_m(1),\qquad
\operatorname{Var}(M)=\operatorname{Var}(P)=n V_m+O_m(1),
\]
where, on writing \(c_m=(m!)^2/(2m+2)!\),
\[
L_m=-\frac{m^7+10m^6+26m^5+4m^4-43m^3-14m^2-56m-120}
{12m(m+1)^2(m+2)^2(m+3)}-\frac{3m+5}{m(2m+3)}c_m,
\]
\[
V_m=\frac{2m^5+19m^4+42m^3+7m^2-10m+36}
{12(m+2)^2(m+3)(2m+3)}>0.
\]
Consequently \(\operatorname{Corr}(M,P)\to\rho_m=L_m/V_m<0\). In particular, \(\rho_2=-19/33\), and \(\lim_{m\to\infty}\rho_m=-1\).

The negative covariance describes the simultaneous counts of minima and maxima in the **same** random labeling. It is not a result about independently generated orientations of edges.

## Assumptions and scope

All trees are finite, simple, and connected. In \(T_{m,h}\), the root has exactly \(m\) children, all nonleaf vertices have exactly \(m\) children, and all leaves are at depth \(h\). The arity \(m\) and height \(h\) are positive integers. A local minimum (respectively maximum) has a label strictly below (respectively above) every neighbor's label. With independent continuous identically distributed labels, the induced rank order is uniform, and the choice of continuous label distribution does not affect the result. Correlation is asserted only when both count variances are positive. The statements about infinite height are limits of finite trees, not claims about infinite random sums.

## Proof

### Local covariance kernels

Let \(a,b\ge1\) be degrees. A vertex of degree \(a\) is locally minimal or maximal with probability \(1/(a+1)\). A vertex cannot simultaneously be a local minimum and maximum. For two adjacent vertices with respective degrees \(a,b\), direct integration over their independent uniform labels gives
\[
\Pr(u\text{ minimum},v\text{ maximum})=
\frac1{ab}-\frac{(a-1)!(b-1)!}{(a+b)!}.
\]
The contribution from the two ordered minimum-maximum pairings of this unordered edge to \(\operatorname{Cov}(M,P)\) is \(2E(a,b)\), with
\[
E(a,b)=\frac1{ab}-\frac1{(a+1)(b+1)}-\frac{(a-1)!(b-1)!}{(a+b)!}.
\]
For vertices at distance two in a tree, with unique common neighbor, integration over the three labels and other independent neighbors gives the contribution from both orders
\[
B(a,b)=-\frac{2}{ab(a+1)(b+1)}+\frac{2(a-1)!(b-1)!}{(a+b+1)!}.
\]
For example, the ordered probability of a minimum at the degree-\(a\) vertex and a maximum at the degree-\(b\) vertex is
\[
\frac1{a(b+1)}-\frac1{a(a+1)b}+\frac{(a-1)!(b-1)!}{(a+b+1)!}.
\]
Events at distance at least three use disjoint sets of independent labels and hence are independent. Therefore, for any tree \(T\) with degrees \(d_v\), the exact identity is
\[
\operatorname{Cov}(M,P)
=-\sum_v\frac1{(d_v+1)^2}
+2\sum_{uv\in E(T)}E(d_u,d_v)
+\sum_{\{u,v\}:\operatorname{dist}(u,v)=2}B(d_u,d_v).
\tag{1}
\]
Similarly, two local minima at distance two have covariance \(1/[(a+1)(b+1)(a+b+1)]\), while adjacent minima are incompatible. Thus
\[
\operatorname{Var}(M)=\sum_v\frac{d_v}{(d_v+1)^2}
-2\sum_{uv\in E(T)}\frac1{(d_u+1)(d_v+1)}
+2\sum_{\{u,v\}:\operatorname{dist}(u,v)=2}
\frac1{(d_u+1)(d_v+1)(d_u+d_v+1)}.
\tag{2}
\]
Symmetry under reversing all labels gives \(\operatorname{Var}(M)=\operatorname{Var}(P)\).

### Paths

For \(n\ge4\), a path has two degree-one vertices, \(n-2\) degree-two vertices, two degree-\((1,2)\) edges, \(n-3\) degree-\((2,2)\) edges, two degree-\((1,2)\) distance-two pairs, and \(n-4\) degree-\((2,2)\) distance-two pairs. Substitution in (1) yields
\[
-\frac12-\frac{n-2}{9}+\frac23+\frac{7(n-3)}{36}-\frac16-\frac{7(n-4)}{180}
=\frac{8n-37}{180}.
\]
Substitution in (2) yields \(2(n+1)/45\). The exceptional three-vertex case follows directly from (1). The claimed path sign and correlation now follow by arithmetic.

### Complete branching trees

Fix \(m\ge2\) and put \(d=m+1\). Except for the root, all nonleaf vertices have degree \(d\); leaves have degree one. With \(n=(m^{h+1}-1)/(m-1)\), as \(h\to\infty\), the counts of local configurations divided by \(n\) converge to:

| Configuration | Limiting count divided by \(n\) |
|---|---:|
| Leaves | \((m-1)/m\) |
| Nonroot internal vertices | \(1/m\) |
| Leaf–internal edges | \((m-1)/m\) |
| Internal–internal edges | \(1/m\) |
| Distance-two leaf–leaf sibling pairs | \((m-1)^2/(2m)\) |
| Distance-two internal–leaf ancestor pairs | \((m-1)/m\) |
| Distance-two internal–internal pairs (siblings and ancestors) | \((m+1)/(2m)\) |

All contributions involving the root are \(O_m(1)\). Using
\[
E(d,1)=\frac1{2(d+1)},\quad B(1,1)=-\frac16,\quad
B(d,1)=-\frac1{(d+1)(d+2)},
\]
\[
E(d,d)=\frac{2d+1}{d^2(d+1)^2}-c_m,\qquad
B(d,d)=-\frac2{d^2(d+1)^2}+\frac{2c_m}{2d+1},
\]
substitution into (1) produces the displayed \(L_m\); substitution into (2) produces \(V_m\). Counting each level as a geometric progression shows that the errors are \(O_m(1)\), not merely \(o(n)\).

For exact finite-height negativity, define
\[
Q_m=m^6+11m^5+37m^4+41m^3-2m^2+32m+120.
\]
For this finite count, there are \(m^h\) leaves and \(\sum_{j=1}^{h-1}m^j\) nonroot internal vertices. The edge classes (root–internal, internal–internal, internal–leaf) have respective counts \(m\), \(\sum_{j=2}^{h-1}m^j\), and \(m^h\). The distance-two classes (leaf–leaf, leaf–internal, root–internal, internal–internal) have respective counts
\[
\binom m2 m^{h-1},\quad m^h,\quad m^2,\quad
\binom m2\sum_{j=0}^{h-2}m^j+m\sum_{j=2}^{h-2}m^j.
\]
Here the last sum is zero if its upper endpoint is below its lower endpoint; the root–internal class refers to a pair containing the root, whose degree is \(m\), and the other member has degree \(m+1\). Inserting these counts in (1) and simplifying gives, for every \(h\ge3\),
\[
\operatorname{Cov}_{T_{m,h}}(M,P)=nL_m+R_m,
\]
\[
R_m=-\frac{Q_m}{12m(m+1)^2(m+2)^2(m+3)}
-\frac{2m^3+7m^2+4m-5}{m(2m+3)}c_m.
\]
Both \(L_m\) and \(R_m\) are strictly negative for \(m\ge2\). Indeed, writing \(t=m-2\ge0\), the numerator of the rational term in \(-L_m\) is
\[
t^7+24t^6+230t^5+1144t^4+3189t^3+4976t^2+3948t+1032>0,
\]
and \(Q_m\) becomes
\[
t^6+23t^5+207t^4+937t^3+2252t^2+2772t+1512>0.
\]
All factorial terms and their coefficients have the claimed strict signs.

For \(h=2\), the exact covariance is
\[
-\frac{m^7+8m^6+13m^5+2m^4+16m^3+8m^2-96m-48}
{12(m+1)^2(m+2)^2}
-\frac{7m^2+21m+12}{2m+3}c_m.
\]
The polynomial numerator of its first negative term becomes
\[
t^7+22t^6+193t^5+892t^4+2392t^3+3784t^2+3216t+1008>0,
\]
so this case is also strictly negative. For \(h=1\), let \(K\), uniform on \(\{0,\dots,m\}\), be the number of leaves ranked below the root. Then \(M=K+\mathbf1_{K=0}\) is nondecreasing in \(K\), while \(P=m-K+\mathbf1_{K=m}\) is nonincreasing. They are both nonconstant for \(m\ge2\), so their covariance is strictly negative by the elementary oppositely monotone covariance inequality.

Finally, \(V_m>0\) follows from its displayed rational expression (or from (2) and its limiting count). As \(m\to\infty\), \(L_m=-m/12+O(1)\) and \(V_m=m/12+O(1)\); the factorial term is negligible. Hence \(\rho_m\to-1\). Direct substitution gives \(L_2=-323/5040\) and \(V_2=187/1680\), so \(\rho_2=-19/33\). This proves every part of the finding.

## Verification

The standalone standard-library script `verify.py` reconstructs the local kernels, computes exact tree covariances from degrees and pair neighborhoods, checks the path identities and finite-height arity formulas, compares against exact enumeration of all label permutations on small trees, and verifies the special binary asymptotic constants. Run `python verify.py`. The packaged checker reports `VERIFY_OK 140 exact identity and finite-enumeration checks`. Analytic local integrations, finite-height identities, and explicit sign-polynomial expansions prove the infinite families; the finite tests are independent consistency checks only.

## Relationship to prior work

Random vertex-order greedy independent-set selection and its parallel first round are described by Krivelevich, Mészáros, Michaeli and Shikhelman (arXiv:1907.07216, first public version July 16, 2019). The present counts are precisely the first-round selected vertices in the original and reversed priority orders, *not* the sizes of the fully run greedy independent sets. Burdzy and Pal (arXiv:1606.08025) examine configurations conditioned on one or two peaks, including regular trees; their results concern peak locations, not the unconditioned two-sided min–max covariance. Baldi, Rinott and Stein (NeurIPS 1989) develop one-sided local-extremum count normal approximations, not the joint branching-sign classification here. In contrast, results for independently edge-oriented trees sample a different orientation law, so their source–sink covariance formulas do not imply the present statements.

## Limitations

The sign dichotomy is proved for complete rooted \(m\)-ary trees, not for every tree with a branch. It does not assert monotonicity of \(\rho_m\) at successive finite arities. The positive-path correlation limit is for path length increasing; the negative \(\rho_m\) is first a fixed-arity infinite-height limit, with a subsequent large-arity limit. Infinite-height point processes and independent mathematical audit are not included. Bibliographic searches and inspected primary texts do not establish historical uniqueness.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216v1 (July 16, 2019); AofA 2020, DOI:10.4230/LIPIcs.AofA.2020.20. https://arxiv.org/abs/1907.07216v1
2. K. Burdzy and S. Pal, *Twin peaks*, arXiv:1606.08025v1 (June 26, 2016); Random Structures & Algorithms 56 (2020). https://arxiv.org/abs/1606.08025
3. P. Baldi, Y. Rinott and C. Stein, *On the Distribution of the Number of Local Minima of a Random Function on a Graph*, NeurIPS (1989). https://papers.neurips.cc/paper_files/paper/1989/file/d947bf06a885db0d477d707121934ff8-Paper.pdf
