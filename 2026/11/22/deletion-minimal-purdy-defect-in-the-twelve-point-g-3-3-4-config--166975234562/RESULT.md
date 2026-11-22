# Deletion-minimal Purdy defect in the twelve-point \(G(3,3,4)\) configuration

## Finding

Let \(\zeta\) be a primitive cube root of unity, and let
\[
S=\{[e_i-\zeta^a e_j]:i\in\{0,1\},\ j\in\{2,3\},\ a\in\mathbb Z/3\mathbb Z\}\subset\mathbb P^3_{\mathbb C}.
\]
For each subset \(T\subseteq S\), let \(f_k(T)\) count distinct projective \(k\)-flats spanned by \(k+1\) independent points of \(T\), and set
\[\Delta(T)=f_2(T)-f_1(T)+|T|+2.\]
Then \(\Delta(T)<0\) holds **if and only if** \(T=S\), or \(T\) is the union of the two three-point groups on one of the four pairs of coordinate-support lines that share a coordinate index. In the first case
\[ (|T|,f_1(T),f_2(T),\Delta(T))=(12,58,43,-1),\]
and in each of the other four cases
\[(|T|,f_1(T),f_2(T),\Delta(T))=(6,11,1,-2).\]
Each six-point exception spans a projective plane, whereas \(S\) spans \(\mathbb P^3\). In particular, \(S\) is the **unique negative-defect spanning subset of itself**; every proper essential dual hyperplane subarrangement satisfies the nonnegative Purdy inequality. In fact every deletion of one point gives \((11,49,42,6)\).

## Assumptions and scope

The ground field is \(\mathbb C\) and \(\zeta^2+\zeta+1=0\). The twelve labelled points are pairwise distinct. Order the four support lines as
\[
L_0=L_{02},\quad L_1=L_{03},\quad L_2=L_{12},\quad L_3=L_{13},
\qquad L_{ij}=\mathbb P(\langle e_i,e_j\rangle).
\]
Write \(T_g\subseteq\mathbb Z/3\mathbb Z\) for the selected exponents on \(L_g\), and \(r_g=|T_g|\). A pair of support lines is *adjacent* when their coordinate-index sets intersect, and *opposite* otherwise. There are four adjacent pairs and two opposite pairs. "Essential" refers to the dual arrangement having rank four, equivalently the dual point set spanning the entire \(\mathbb P^3\). We make no claim of global minimality among all complex arrangements.

## Proof

Every line containing at least two points of \(S\) is either one of the four coordinate-support lines, or joins exactly one point from each of two different support lines. Hence
\[
f_1(T)=\sum_{g=0}^{3}\mathbf1_{r_g\ge2}+\sum_{0\le g<h\le3}r_gr_h.
\]
The complete plane classification consists of: (i) four coordinate-face planes, each containing one adjacent pair of support lines; (ii) twelve planes containing one support line and one point of its opposite line; and (iii) twenty-seven planes containing a balanced quadruple, one point from each support line, with exponents \((a,b,c,d)\) satisfying \(a+d\equiv b+c\pmod3\). The three families are disjoint. The combinatorial classification is also established in the cited source; independent determinant calculations are given by the attached checker.

Let \(\mathcal F\) denote the four adjacent unordered pairs, and \(\mathcal O\) the two opposite unordered pairs. A plane is spanned by a selected subset precisely when that subset contains an independent triple in its point support. Consequently
\[
\begin{aligned}
f_2(T)={}&\sum_{\{g,h\}\in\mathcal F}
\mathbf1_{(r_g\ge2\land r_h\ge1)\lor(r_h\ge2\land r_g\ge1)}\\
&+\sum_{\{g,h\}\in\mathcal O}\bigl(r_h\mathbf1_{r_g\ge2}+r_g\mathbf1_{r_h\ge2}\bigr)\\
&+\sum_{a,b,c\in\mathbb Z/3\mathbb Z}
\mathbf1_{\bigl|T\cap\{(0,a),(1,b),(2,c),(3,b+c-a)\}\bigr|\ge3}.
\end{aligned}
\]
Here \((g,a)\) means the point of exponent \(a\) on the \(g\)-th support line. No non-support line contains three points of \(S\); thus every three points on a balanced quadruple are independent. All three types of plane are therefore counted exactly once.

There are exactly \(2^3=8\) choices of \(T_g\) for each \(g\), hence \(8^4=4096\) subsets. Iterate through the twelve-bit masks \(0,1,\ldots,4095\), calculate \(r_g\), then the two displayed formulas and \(\Delta(T)\). Exhaustion gives precisely five negative masks (with three consecutive bits assigned to each \(L_g\)):
\[
63,\quad455,\quad3640,\quad4032,\quad4095.
\]
The first four are exactly the unions of both complete groups of an adjacent pair; the last is \(S\). Each proper negative subset is in one coordinate-face plane, with only that plane spanned, and the full set spans \(\mathbb P^3\). The computed exact quadruples and every one-point-deletion result are as claimed. The attached `verify.py` is a self-contained finite exhaustive proof certificate, separately calculating all \(4096\) results by this incidence formula and by exact determinants in \(\mathbb Q(\zeta)\); the two agree subset by subset. \(\square\)

## Verification

Run `python3 verify.py` (standard-library-only). It constructs all \(58\) spanned lines and \(43\) spanned planes independently from the point-coordinate determinants. It uses exact rational arithmetic in \(\mathbb Q[\zeta]/(\zeta^2+\zeta+1)\), checks the combinatorial and determinant counts for all \(4096\) masks, asserts precisely the five negative cases, and checks all twelve single deletions. The proof is exhaustive over a finite, explicitly defined twelve-point configuration; it does not claim anything for other arrangements.

## Relationship to prior work

Michałek and Pokora exhibit \(S\) as a counterexample to the refined Purdy inequality and prove the original full configuration has \((f_0,f_1,f_2)=(12,58,43)\). They also classify the support incidence relevant to the full count. Ashfaque determines the full-support flat counts and Purdy defect for the general \(\mu_m\)-balanced family; uniqueness of \(m=3\) **among complete root-of-unity configurations** is not the present theorem. Neither inspected source establishes which of the \(4096\) **proper subconfigurations** have negative defect or essential deletion-minimality. These are different quantifiers, and a full-support formula does not imply the subconfiguration classification. Targeted mathematical-record searches found no equivalent result, subject to the limitations below.

## Limitations

This is a classification of restrictions of **one specific** arrangement, not a theorem that twelve hyperplanes are globally minimal. The four planar six-point cases are nonessential, so they are not counterexamples within the essential rank-four class. The proof is finite and exhaustive for this labelled object; it does not cover other reflection groups, other \(m\), or combinatorial realizations unrelated to this coordinate model. Unindexed priority and independent mathematical validation remain open.

## References

1. M. Michałek and P. Pokora, *A counterexample to Purdy's inequality for hyperplane arrangements in projective three-space*, arXiv:2607.08463v1 (first publicly available 2026-07-09), https://arxiv.org/abs/2607.08463.
2. J. M. Ashfaque, *Analytical bounds on the \(\mu_m\)-balanced counterexamples to Purdy's inequality*, public text dated 2026-07-11, https://www.researchgate.net/publication/408877941_ANALYTICAL_BOUNDS_ON_THE_m_-BALANCED_COUNTEREXAMPLES_TO_PURDY%27S_INEQUALITY.
