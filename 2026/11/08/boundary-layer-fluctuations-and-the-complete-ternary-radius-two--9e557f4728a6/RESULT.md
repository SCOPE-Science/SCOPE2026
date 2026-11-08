# Boundary-layer fluctuations and the complete ternary radius-two multiset-ball spectrum

## Finding

The volume of a fixed-radius multiset deletion ball is maximal at almost every uniformly sampled center as the multiset size increases; exceptional centers occur in a thin, explicitly classified boundary layer. For fixed \(q\ge2\) and \(r\ge1\), there are exactly \(r\) distinct first-order volume deficits, occurring with equal leading probability. This gives an exact leading variance and a uniform conditional deficit law. At ternary radius two, the **entire finite-length volume distribution** has six possible values and closed frequency formulas.

Write \(\mathcal Z_{q,r}\) for the ideal difference set and \(M=|\mathcal Z_{q,r}|\). With \(h_s=|\{z\in\mathcal Z_{q,r}:z_1\le-(s+1)\}|\) for \(0\le s<r\), the principal conclusions are

\[
\Pr\{M-B_r(X)=h_s\}=\frac{q(q-1)}n+O_{q,r}(n^{-2}),\qquad
\Pr\{B_r(X)<M\}=\frac{qr(q-1)}n+O_{q,r}(n^{-2}),
\]
\[
\operatorname{Var}(B_r(X))=
\frac{q(q-1)}n\sum_{s=0}^{r-1}h_s^2+O_{q,r}(n^{-2}),
\qquad
\Pr\{M-B_r(X)=h_s\mid B_r(X)<M\}\longrightarrow\frac1r.
\]

The error constants depend on fixed \(q,r\), and the limit is taken through integers \(n\to\infty\).

## Assumptions and scope

Let \(q\ge2,r\ge1\) be integers. For each \(n\ge qr\), let
\[
\mathcal S_{n,q}=\{x=(x_1,\ldots,x_q)\in\mathbb Z_{\ge0}^q:\ \sum_i x_i=n\},
\qquad |\mathcal S_{n,q}|=\binom{n+q-1}{q-1}.
\]
The center \(X\) is **uniform over multiplicity vectors**, not a vector of symbol counts of a uniformly random ordered word. Define the multiset metric and ball cardinality by
\[
d(x,y)=\tfrac12\sum_{i=1}^q|x_i-y_i|,\qquad
B_r(x)=|\{y\in\mathcal S_{n,q}:d(x,y)\le r\}|.
\]
Let
\[
\mathcal Z_{q,r}=\{z\in\mathbb Z^q:\ \sum_i z_i=0,\ \sum_i\max(z_i,0)\le r\},
\quad M=|\mathcal Z_{q,r}|,
\quad h_s=\sum_{z\in\mathcal Z_{q,r}}\mathbf1\{z_1\le-(s+1)\},\quad 0\le s<r.
\]
All sums are finite, and \(h_s\) depends only on \(q,r\), not on \(n\). Use \(\binom ab_+=\binom ab\) for integers \(a\ge b\ge0\), and zero otherwise. The asymptotic statements concern fixed \(q,r\); no assertion is made for a growing alphabet or radius.

## Proof

**1. Exact ball formula and second moment.** Every output \(y\) uniquely corresponds to a difference vector \(z=y-x\). Such a \(z\) has zero sum, its positive mass equals its negative mass, and \(d(x,x+z)=\sum_i(z_i)_+\). Thus
\[
B_r(x)=\sum_{z\in\mathcal Z_{q,r}}\prod_{i=1}^q\mathbf1\{x_i\ge(-z_i)_+\}.
\tag{1}
\]
For \(z,w\in\mathcal Z_{q,r}\), set \(a_i(z,w)=\max\{0,-z_i,-w_i\}\) and \(A(z,w)=\sum_i a_i(z,w)\). By replacing \(x_i\) with \(x_i-a_i(z,w)\), the number of centers for which both indicators in (1) equal one is precisely \(\binom{n-A(z,w)+q-1}{q-1}_+\). Squaring (1), summing over all centers and dividing by their number gives the exact formula
\[
\boxed{\ \mathbb E B_r(X)^2=
\frac{\displaystyle\sum_{z,w\in\mathcal Z_{q,r}}
\binom{n-A(z,w)+q-1}{q-1}_+}
{\binom{n+q-1}{q-1}}.\ }
\tag{2}
\]
Similarly, with \(A(z)=\sum_i(-z_i)_+\),
\[
\mathbb E B_r(X)=\frac{\sum_{z\in\mathcal Z_{q,r}}\binom{n-A(z)+q-1}{q-1}_+}{\binom{n+q-1}{q-1}}.
\tag{3}
\]
Equations (2) and (3) give an **exact finite-\(n\) variance** for all listed parameters, via \(\operatorname{Var}(B_r)=\mathbb EB_r^2-(\mathbb EB_r)^2\). They do not require probabilistic independence of the ball indicators.

**2. Interior criterion and boundary deficits.** Every negative coordinate of a vector in \(\mathcal Z_{q,r}\) is at least \(-r\). Therefore (1) gives \(B_r(x)=M\) whenever all \(x_i\ge r\). Conversely, if some \(x_i=s<r\), choose \(j\ne i\) and take \(z_i=-(s+1)\), \(z_j=s+1\) and all other coordinates zero. This \(z\in\mathcal Z_{q,r}\) is forbidden at \(x\), so \(B_r(x)<M\). The number of all-interior centers is \(\binom{n-qr+q-1}{q-1}\); hence for \(n\ge qr\)
\[
\boxed{\ \Pr\{B_r(X)=M\}=\frac{\binom{n-qr+q-1}{q-1}}{\binom{n+q-1}{q-1}}.\ }
\tag{4}
\]
Suppose exactly one coordinate \(x_i\) is smaller than \(r\), with \(x_i=s\). Every other coordinate allows all negative components of \(z\), so the forbidden vectors are *exactly* those with \(z_i\le-(s+1)\); therefore \(M-B_r(x)=h_s\). For each \(s<r\), a vector \(z_i=-(s+1)\), \(z_j=s+1\) proves \(h_s>h_{s+1}\) when \(s<r-1\) and \(h_{r-1}>0\). Thus these \(r\) deficits are strictly decreasing and pairwise distinct.

**3. The rare-boundary law.** Fix a coordinate \(i\) and layer \(s<r\). Centers with \(x_i=s\) and all other coordinates at least \(r\) are counted by
\[
\binom{n-s-(q-1)r+q-2}{q-2},
\tag{5}
\]
under the binomial-zero convention above. Dividing by \(\binom{n+q-1}{q-1}\), a ratio of fixed-degree polynomials in \(n\), gives \((q-1)/n+O_{q,r}(n^{-2})\). For any two specified distinct coordinates \(i,j\) and fixed layers \(s,t<r\), the count of centers with \(x_i=s,x_j=t\) is \(O_{q,r}(n^{q-3})\) if \(q\ge3\), compared with a total \(\Theta_q(n^{q-1})\); if \(q=2\), such centers are impossible once \(n>2(r-1)\). A finite union bound therefore shows that multiple deficient coordinates have total probability \(O_{q,r}(n^{-2})\). Summing the disjoint single-deficiency contributions over the \(q\) coordinate choices yields the asserted probability for each \(h_s\). Their union and (4) yield the total submaximal probability. The conditional uniformity follows by division, with denominator asymptotic to \(qr(q-1)/n\).

Because the deficit \(\Delta_n=M-B_r(X)\) is bounded by the fixed integer \(M\), the multiple-deficiency event contributes \(O_{q,r}(n^{-2})\) to each of its fixed moments. Consequently
\[
\mathbb E\Delta_n=\frac{q(q-1)}n\sum_{s=0}^{r-1}h_s+O_{q,r}(n^{-2}),
\quad
\mathbb E\Delta_n^2=\frac{q(q-1)}n\sum_{s=0}^{r-1}h_s^2+O_{q,r}(n^{-2}).
\]
Since \((\mathbb E\Delta_n)^2=O(n^{-2})\), and a constant shift does not change variance, this proves the variance formula.

**4. Complete ternary radius-two spectrum.** Set \(q=3,r=2,n\ge6\). The ideal difference set has \(M=1+6+12=19\) elements. Direct enumeration of the 19 zero-sum vectors (or grouping by their negative first coordinate) gives \(h_0=7\) and \(h_1=3\). A center with all coordinates at least two has ball size 19. One coordinate equal to one gives size 16; two coordinates equal to one give 13. One zero with the other coordinates at least two gives size 12; one zero and one one give 9. Finally, two zeros give size 6: the two sets of 7 forbidden vectors intersect in the **single** vector with negative components \((-1,-1)\) and the remaining component \(2\), so the total deficit is \(7+7-1=13\). There are no other possible deficiency patterns for \(n\ge6\).

Counting nonnegative solutions after fixing the small coordinates produces the *complete* frequency distribution:

| \(B_2(x)\) | Number of centers \(x\in\mathcal S_{n,3}\) |
|---:|---:|
| \(19\) | \(\binom{n+2}{2}-6n+9\) |
| \(16\) | \(3(n-4)\) |
| \(13\) | \(3\) |
| \(12\) | \(3(n-3)\) |
| \(9\) | \(6\) |
| \(6\) | \(3\) |

The frequencies total \(\binom{n+2}{2}\). Computing the first and second moments of the *deficit* from the table gives
\[
\mathbb E(19-B_2(X))=\frac{30n+18}{\binom{n+2}{2}},\qquad
\mathbb E(19-B_2(X))^2=\frac{174n+666}{\binom{n+2}{2}},
\]
so
\[
\boxed{\operatorname{Var}(B_2(X))=\frac{174n+666}{\binom{n+2}{2}}-\left(\frac{30n+18}{\binom{n+2}{2}}\right)^2.}
\]
As expected from the general theorem, \(n\operatorname{Var}(B_2(X))\to348\) and the conditional nonzero deficit is asymptotically uniform on \(\{3,7\}\).

## Verification

The accompanying `checker.py` independently enumerates fixed-cardinality centers and **actual balls through the distance definition**, then compares them with the difference-vector formula for \(q\in\{2,3,4\}\), \(r\in\{1,2,3\}\), four consecutive lengths per parameter pair. It verifies equation (2) by exact integer sums, checks the exact interior-center count (4), and compares the six-bin ternary distribution and its exact rational first two moments for every \(6\le n\le40\). The checker reported 4,451 direct-distance instances, all passing. Execute `python3 checker.py` in the same directory as this file; no external dependencies are required. The proof above, not the finite checker, establishes the unrestricted statements.

## Relationship to prior work

Kreindel, Essayag and Zabokritskiy (2026, arXiv:2603.18322, March 18 first version) establish the underlying difference-vector ball formula (their Lemma 4), the interior maximal-ball property (Corollary 7), the exact *mean* via a pair enumerator (Theorem 9), and ternary minimal and maximal volumes (Lemma 15). All are used as context, **not** claimed here. Equations (2) and (3) use the same basic difference-vector idea but newly count *simultaneous feasibility* of two distinct vectors. The specific fixed-radius uniform-center variance, boundary-deficit law and six-bin ternary distribution are not stated in the inspected source. Kovačević and Tan (2016) develop the multiset metric, difference sets and lattice-code bounds, but do not state this distributional result. Kreindel and coauthors (January 2026, arXiv:2601.05636) analyze code sizes and constructions, rather than the center-volume spectrum. Goyal and coauthors (2024, arXiv:2402.14712) study \(\ell_1\) coding bounds in different scaling regimes.

## Limitations

The results are about uniformly distributed **multiset centers** in a fixed-size simplex, not ordered-word centers. The first-order limiting law keeps \(q,r\) fixed, and the six-bin exact spectrum assumes \(q=3,r=2,n\ge6\). The variance formula is for the *radius-at-most* multiset metric ball, not solely exact-deletion outputs of size \(n-r\). No stronger coding-rate or code-optimality result is claimed. Earlier papers might implicitly contain equivalent consequences of their ball formulas; independent historical-priority and mathematical validation are not performed.

## References

1. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322, first made public March 18, 2026. https://arxiv.org/abs/2603.18322
2. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837, 2016. https://arxiv.org/abs/1612.08837
3. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636, first version January 9, 2026. https://arxiv.org/abs/2601.05636
4. M. Goyal et al., *Gilbert–Varshamov Bound for Codes in \(L_1\) Metric Using Multivariate Analytic Combinatorics*, arXiv:2402.14712, 2024. https://arxiv.org/abs/2402.14712
