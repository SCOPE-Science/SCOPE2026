# Sharp second-best two-color trace-probing penalty on odd screened cycles

## Finding

Let \(n=2m+1\ge5\), \(\mu>0\), and \(G=(\mu I+L(C_n))^{-1}\), with the vertices of the simple cycle numbered modulo \(n\). Partition the vertices into two nonempty color classes, and estimate \(\operatorname{tr}G\) using one independent Rademacher vector supported on each class. The two resulting quadratic forms are summed without further normalization. This unbiased estimator uses two applications of \(G\); its variance is denoted \(V(s)\), where \(s\in\{-1,1\}^n\) encodes the classes.

Put \(r\in(0,1)\) for the solution of \(r+r^{-1}=\mu+2\), set \(c=\bigl[(r^{-1}-r)(1-r^n)\bigr]^{-1}\), and \(g_d=c(r^d+r^{n-d})\), \(f_d=g_d^2\), for \(1\le d\le m\). The exact optimum is

\[
V_{\min}=2\sum_{d=1}^m\bigl[n+(-1)^d(n-2d)\bigr]f_d.
\]

A partition is optimal if and only if its binary cyclic word has **exactly one monochromatic adjacent edge**. These are precisely the \(n\) alternating-with-one-defect partitions, or \(2n\) labeled spin words. More strongly, the smallest variance among all NONoptimal partitions is \(V_{\min}+\Delta_n\), where

\[
\boxed{\Delta_5=8(f_1-f_2)=8c^2r^2(1-r^2)(1-r^4)}
\]

and, for every odd \(n\ge7\),

\[
\boxed{\Delta_n=8(f_1-2f_2+f_3)=8c^2(1-r^2)^2(r^2+r^{2n-6}).}
\]

Both are strictly positive. Equality in the second-best bound is attained by the word obtained from \(s_j=(-1)^j\) by flipping just \(s_2\) and \(s_3\). In particular, an additional pair of monochromatic bonds incurs an exactly quantified nonzero variance penalty, not merely a loss of a known ground-state classification.

With two *independent full-support* Hutchinson probes averaged for the same two solves, the variance is \(V_{H,2}=2n\sum_{d=1}^mf_d\). Consequently the optimal restricted-color-to-Hutchinson variance ratio is

\[
\frac{V_{\min}}{V_{H,2}}=
\frac{\sum_{d=1}^m[n+(-1)^d(n-2d)]f_d}{n\sum_{d=1}^mf_d},
\qquad \lim_{n\to\infty}\frac{V_{\min}}{V_{H,2}}=\frac{2r^2}{1+r^2}.
\]

## Assumptions and scope

All claims are for **every** odd integer \(n\ge5\) and **every** real \(\mu>0\), and all binary partitions, including unbalanced and improper graph colorings. The signs of distinct coordinates in each class are independent and symmetric; the two probes are independent. The only design variable is membership in the two classes, and the number of solves is exactly two. The result does not optimize coupling between probes, the number of probes, or deterministic trace evaluation. The parameter \(r\) is uniquely determined, since \(r+r^{-1}\) decreases strictly from infinity to two as \(r\) increases from zero to one.

## Proof

**Covariance and variance.** The positive-definite screened cycle matrix is diagonalized by Fourier modes, or directly by the cyclic Green recurrence. Specifically \(G_{i,j}=g_d\), where \(d\equiv j-i\pmod n\) and \(g_d=c(r^d+r^{n-d})\). This solves \((\mu+2)g_d-g_{d-1}-g_{d+1}={\bf1}_{d=0}\) with cyclic indices. For a symmetric matrix, a Rademacher quadratic form has variance \(4\sum_{i<j}G_{ij}^2\). Restricting independent probes to the classes therefore gives

\[
V(s)=4\sum_{i<j:s_i=s_j}G_{ij}^2=2\sum_{d=1}^m f_d(n+C_d),\quad C_d=\sum_{i=0}^{n-1}s_i s_{i+d}.
\]

**Nonnegative finite-window certificate.** Let \(S=\sum_i s_i\) and let \(T_k=\sum_i(\sum_{j=0}^{k-1}s_{i+j})^2\) for \(2\le k\le m\). Cyclic identities give \(\sum_{d=1}^mC_d=(S^2-n)/2\) and \(T_k=nk+2\sum_{d=1}^{k-1}(k-d)C_d\). Define

\[
a_m=\tfrac12(f_{m-1}-f_m),\qquad
 a_k=\tfrac12(f_{k-1}-2f_k+f_{k+1})\quad(2\le k<m).
\]

For \(m=2\), only the first definition applies, and is written \(a_2\). By the elementary expression \(f_d=c^2(r^{2d}+r^{2n-2d}+2r^n)\), the \(f_d\) decrease strictly up to \(m\), and their interior discrete second differences are strictly positive. Hence all \(a_k>0\). Direct telescoping yields, relative to \(s^*_j=(-1)^j\),

\[
\boxed{V(s)-V(s^*)=f_m(S^2-1)+2\sum_{k=2}^m a_k\bigl(T_k(s)-T_k(s^*)\bigr).}
\]

Since \(n\) is odd, \(|S|\ge1\). For odd \(k\), every window sum is an odd integer, so \(T_k\ge n\). For even \(k\), each window sum \(u\) is an even integer, and \(u^2\ge2|u|\), so \(T_k\ge2|\sum_i\sum_{j=0}^{k-1}s_{i+j}|=2k|S|\ge2k\). The alternating-with-one-defect word \(s^*\) simultaneously realizes all these lower bounds: \(T_k(s^*)=n\) for odd \(k\) and \(2k\) for even \(k\), while \(S^2=1\). Thus it is globally optimal and substitution into the exact variance formula yields \(V_{\min}\) as stated.

**Exact equality and sharp gap.** \(T_2=4b(s)\), where \(b(s)\) is the number of monochromatic neighboring bonds around the cycle. Every odd cyclic binary word has an odd number \(b\) of such bonds. Since \(a_2>0\), equality in the variance certificate forces \(b=1\), and conversely those words are shifts and global flips of \(s^*\). Every other partition has \(b\ge3\), so \(T_2(s)-T_2(s^*)\ge8\) and the certificate gives \(V(s)-V_{\min}\ge16a_2\).

To see sharpness simultaneously for all \(n\), flip entries \(2,3\) of \(s^*\). The sum \(S^2\) remains one, and \(T_2\) rises by eight. For \(3\le k\le m\), windows containing both flipped sites have unchanged sums because the two original signs are opposite. Windows containing neither are unchanged. Of the two windows containing exactly one flipped site, for odd \(k\) the window sum merely changes sign (squares unchanged); for even \(k\), their squared sums change by plus four and minus four, respectively. Therefore each \(T_k\) for \(k\ge3\) stays unchanged. Equality in the bound follows. Inserting \(a_2\) and simplifying the geometric weights proves both formulas for \(\Delta_n\).

**Large-cycle comparison.** With \(r<1\) fixed, \(c\to(r^{-1}-r)^{-1}\); the sum of same-class pairs per cyclic distance is asymptotically \(n\) for even distance and \(o(n)\) for odd fixed distance. Geometric domination of \(f_d\) makes the limiting ratio the even-distance geometric series \(\sum_{j\ge1}r^{4j}/\sum_{d\ge1}r^{2d}=r^2/(1+r^2)\), multiplied by two as indicated.

## Verification

The complete proof is analytic. The standalone pure-standard-library file `check.py` uses exact rational arithmetic to enumerate all \(2^{n-1}\) partitions (fixing one global sign) for \(n=5,7,9,11,13\) and \(r\in\{1/4,1/2,3/4\}\). It checks the variance identities, minimum and second-best gap, the extremizing perturbation, window identities, and the Green recurrence. Running `python check.py` produced: `PASS: 15 exact parameter cases, 16368 exact spin tests, 135 Green recurrence tests; sharp nonoptimal variance gap.` These finite checks validate the implementation and selected instances only; the proof covers all integers and real screening strengths.

## Relationship to prior work

The 2020 work of Kerimov on convex long-range antiferromagnetic Ising ground states, building on Hubbard's criterion, substantially anticipates or covers the **ground-state ordering** aspect of equally spaced alternating configurations. That aspect alone is not claimed as original. The new, targeted mathematical statement is the exact strictly positive **second-best (first-excitation) variance penalty** and its attaining defect geometry for every odd screened cycle and screening strength, together with an exact two-solve variance formula. The published even-cycle checkerboard-probing result for screened resolvents establishes an optimal even-cycle partition but is inapplicable to odd cycles. Switzer et al. establish a graph-coloring probing/variance framework rather than this sharp finite odd-cycle first-excitation law. Some full historical sources remain inaccessible, and a prior equivalent quantitative Ising gap is a residual priority risk.

## Limitations

Only simple odd cycles with \(n\ge5\), positive uniform screening, the specific two-class independent Rademacher estimator and squared-variance loss are treated. No claims of novelty are made for the general ground-state ordering principle, Rademacher variance identity or generic graph coloring. The exact positive gap is not a lower bound on the performance of arbitrary unbiased trace estimators or correlated-probe schemes. Independent mathematical and literature validation have not been performed.

## References

1. A. Kerimov, “Ground state criteria in one-dimensional antiferromagnetic Ising model with long range interaction,” *Journal of Mathematical Physics* 61 (2020), 043301, published online 2020-04-15. https://doi.org/10.1063/5.0001423
2. H. Switzer, A. Stathopoulos, E. Romero, J. Laeuchli, K. Orginos, “Probing for the Trace Estimation of a Permuted Matrix Inverse Corresponding to a Lattice Displacement,” first posted 2021-06-02, arXiv:2106.01275; *SIAM Journal on Scientific Computing* 44 (2022), B1096–B1121. https://arxiv.org/abs/2106.01275
3. “Checkerboard probing uniquely minimizes two-color trace variance on screened cycles,” published mathematical research record (2026-11-08; **even-cycle** result). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-checkerboard-probing-uniquely-minimizes-two-color-trace-variance--ad9f3c6dc76a
4. “Sharp two-color stochastic-probing transition on complete bipartite resolvents,” published mathematical research record (2026-11-08; graph family differs). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-color-stochastic-probing-transition-on-complete-bipart--1edc2b42b895
