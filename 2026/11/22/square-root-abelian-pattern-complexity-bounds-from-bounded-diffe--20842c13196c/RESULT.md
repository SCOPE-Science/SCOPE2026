# Square-root Abelian pattern-complexity bounds from bounded differences

## Finding
For an infinite set \(D\subseteq\mathbb N_0\), let \(x_D(n)=\mathbf 1_D(n)\). Suppose every positive integer \(h\) has at most \(g\) representations \(h=d'-d\) with \(d<d'\) in \(D\), where \(g\ge1\). Let \(P_D(k)\) be the maximum, over all \(k\)-element sets \(S\subset\mathbb N_0\), of the number of distinct values of \(\sum_{s\in S}x_D(t+s)\) as \(t\ge0\) varies.

If \(P_D(k)\ge r+2\) for any integer \(r\ge1\), then
\[
 k\ge\frac{r(r+3)^2}{2((2g+1)r+3-2g)}.
\]
In particular,
\[
 P_D(k)\le \sqrt{(4g+2)k}+O_g(1)\qquad(k\to\infty).
\]
For Sidon supports (\(g=1\)), the coefficient is \(\sqrt6\); this does not assume that the sum-incidence graph is a forest.

A sharp small-pattern consequence is that for \(D=\{2^j:j\ge0\}\), \(P_D(6)=5\). The explicit six-pattern \(S=\{0,2,4,6,8,16\}\) gives counts \(4,1,3,0,2\) at shifts \(t=0,1,2,3,4\), respectively.

## Assumptions and scope
The difference-multiplicity condition counts **unordered increasing** pairs \((d,d')\) per *positive* difference. It is required for all positive integers with a common finite bound \(g\), and does not assume a density, a finite state description, recurrence or superlacunarity. The pattern is any finite \(k\)-element subset of \(\mathbb N_0\), not necessarily an interval. We use the **Abelian** pattern complexity: in a binary word, two sampled factors are equivalent exactly when their one-counts agree. No result is claimed for unrestricted supports or for ordinary (non-Abelian) pattern complexity.

## Proof
Fix \(S\) with \(|S|=k\), and write \(B_t=\{s\in S:t+s\in D\}\). For two distinct nonnegative shifts \(t,u\), each \(s\in B_t\cap B_u\) gives a distinct increasing pair of elements of \(D\) at difference \(|t-u|\). Consequently
\[
 |B_t\cap B_u|\le g. \tag{1}
\]
Let \(m\) distinct one-counts occur. At most two are zero or one. If \(m\ge r+2\), choose \(r\) distinct shifts with one-counts at least two. Arrange their block sizes as \(b_1<\dots<b_r\); necessarily \(b_i\ge i+1\), so their sum \(L=\sum_i b_i\) satisfies \(L\ge L_0=r(r+3)/2\).

For each \(s\in S\) let \(d_s\) count how many of these \(r\) blocks contain \(s\). Double-counting incidences and intersecting pairs gives
\[
 \sum_{s\in S}d_s=L,\qquad
 \sum_{s\in S}\binom{d_s}{2}=
 \sum_{1\le i<j\le r}|B_i\cap B_j|\le g\binom r2.
\]
Thus \(\sum_s d_s^2\le L+gr(r-1)\). Cauchy--Schwarz then gives
\[
 L^2\le k\sum_s d_s^2\le k\bigl(L+gr(r-1)\bigr),
 \quad\text{hence}\quad
 k\ge\frac{L^2}{L+gr(r-1)}.
\]
The right-hand side is strictly increasing in \(L>0\) with \(g,r\) fixed. Substituting \(L\ge r(r+3)/2\) proves the displayed finite bound. Since the right-hand side is \(r^2/(4g+2)+O_g(r)\), the square-root bound follows by inversion; \(m\le2\) is trivial.

For the dyadic example, the \(2\)-adic valuation of a positive difference \(2^b-2^a=2^a(2^{b-a}-1)\) uniquely determines \(a\), after which the difference determines \(b\). Thus \(D\) has \(g=1\). Were six counts to occur for a six-pattern, the finite inequality with \(r=4\) would force \(6\ge 98/13\), impossible. The indicated \(S\) exhibits all five counts, proving equality.

## Verification
The included `verify.py` independently enumerates all patterns of sizes one through six inside a twelve-position window for four finite test supports, determining the exact maximum positive-difference multiplicity in each. There are 10,036 tested pattern profiles; all satisfy the finite inequality. It separately checks the five dyadic witness counts and rejection of six counts at pattern size six. Run `python3 verify.py`; expected output is included in `verification_output.txt`. These finite checks are consistency tests, not the justification for the infinite theorem; the preceding counting proof is the justification.

## Relationship to prior work
Zeng, Xue and Zeng (2026) characterize the *minimum* possible Abelian maximal pattern complexity through a forest condition on the sum-incidence graph, show that Sidon supports give complexity three at pattern size three, and exhibit the powers-of-two support with complexity **at least** five at pattern size six. The present result instead gives an all-size upper bound, uniformly over every bounded-difference-multiplicity support, and closes the exact six-pattern value for that example. The 2013 work of Kamae, Widmer and Zamboni concerns basic Abelian maximal pattern complexity and lower bounds in recurrent settings; the difference-multiplicity upper bound here uses a distinct incidence second-moment argument.

## Limitations
The coefficient \(\sqrt{4g+2}\) is proved as an upper bound, not claimed asymptotically sharp. The statement does not classify extremal supports or give exact \(P_D(k)\) for all \(k\). An independently established prior equivalent bound not found in the inspected material would affect novelty, and independent verification is not yet performed.

## References
- Q. Zeng, Y. Xue, C. Zeng, *Abelian maximal pattern complexity and extremal words*, first posted 2026-09-23, arXiv:2609.28059, https://arxiv.org/abs/2609.28059 . Read: definitions, main results and Sections 5--7; in particular Proposition 6.8, Lemma 6.5, Example 6.10.
- T. Kamae, S. Widmer, L. Q. Zamboni, *Abelian maximal pattern complexity of words*, arXiv:1301.5113 (2013), https://arxiv.org/abs/1301.5113 ; subsequently *Ergodic Theory and Dynamical Systems* 35 (2015), 142--151.
