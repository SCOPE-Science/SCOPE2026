# Complete empirical-measure interval spectrum on a two-point rank-two compactum

## Finding
Let \(X\) be an infinite countable compact metric space, let \(T:X\to X\) be continuous with a dense forward orbit \(z\), and suppose the second Cantor–Bendixson derivative is \(X^{(2)}=\{p_0,p_1\}\) and both points are fixed. For \(N\ge1\), write
\[
\mathcal E_N(z)=\frac1N\sum_{j=0}^{N-1}\delta_{T^jz},\qquad
\mathcal V(z)=\bigcap_{M\ge1}\overline{\{\mathcal E_N(z):N\ge M\}}.
\]
Then there are unique \(0\le a\le b\le1\) such that
\[
\mathcal V(z)=\{t\delta_{p_0}+(1-t)\delta_{p_1}:t\in[a,b]\}.
\]
**Every** interval \([a,b]\subseteq[0,1]\), including singleton intervals and the entire segment, occurs for a compact forward-invariant binary orbit closure \(X\subseteq\{0,1\}^{\mathbb N}\) with \(X^{(2)}=\{0^\infty,1^\infty\}\), a dense forward orbit, and exactly these two fixed points. Every resulting space is homeomorphic to \(\omega^2\cdot2+1\). In these realizations the stationary probability simplex is always the whole segment \(\operatorname{conv}\{\delta_{0^\infty},\delta_{1^\infty}\}\), independently of the selected empirical interval.

Thus even on one fixed countable compact homeomorphism type, and with the same stationary simplex, a dense orbit can be generic for any prescribed mixture, have precisely any nontrivial interval of limiting mixtures, or visit all stationary mixtures as subsequential time averages.

## Assumptions and scope
The derivatives are \(X^{(1)}=X'\), \(X^{(2)}=(X')'\), and \(X^{(3)}=\emptyset\). A dense forward orbit means \(\overline{\{T^jz:j\ge0\}}=X\). Weak-star convergence of probabilities is tested on \(C(X)\); the points \(p_0,p_1\) are labelled, and the interval refers to the coefficient of \(\delta_{p_0}\). The fixed-point condition on these two top-rank points is part of the universal upper-bound statement. The concrete shift realizations satisfy it. We do not require \(T(X)=X\): the one-sided orbit closure constructed below is forward invariant, not necessarily surjectively invariant.

## Proof
**1. The only periodic points are the two specified top points.** Every isolated point belongs to the dense orbit and occurs there exactly once. Indeed every singleton isolated point must be reached, and repetition would make the forward orbit eventually periodic and hence not dense in the infinite space. Put \(Y=X'\). Continuity and density imply \(T(Y)\subseteq Y\): a sequence of distinct isolated points converging to \(y\in Y\), when mapped forward, consists of distinct isolated orbit points, so its limit cannot be isolated.

Suppose there is a finite periodic orbit \(Q\subset Y\setminus X^{(2)}\). The points of \(Y\setminus X^{(2)}\) are isolated in \(Y\), so zero-dimensionality of the countable compact metric space supplies a clopen \(U\subset X\) with \(U\cap Y=Q\). Since \(T(Q)=Q\subset U\), continuity gives a neighborhood of every element of \(Q\) within \(U\) that maps into \(U\). Consequently all points in \(U\) whose images leave \(U\) lie in a compact subset of \(U\) disjoint from \(Y\), hence comprise a finite set. But both \(U\) and \(X\setminus U\) contain infinitely many isolated points: \(U\) accumulates at every member of \(Q\), and its complement contains \(X^{(2)}\). The dense orbit visits every isolated point exactly once, so it must cross from \(U\) to its complement infinitely often. This contradiction excludes \(Q\). The only remaining periodic points are \(p_0,p_1\), which are fixed by assumption.

**2. All empirical limits lie on one segment and form an interval.** Every invariant Borel probability on a countable space is atomic. Poincaré recurrence applied to any positive singleton atom implies that atom lies on a periodic orbit. Part 1 therefore gives
\[
\mathcal M_T(X)=\{t\delta_{p_0}+(1-t)\delta_{p_1}:0\le t\le1\}.
\]
All weak-star limits of \(\mathcal E_N(z)\) are invariant, since for every \(\varphi\in C(X)\),
\[
\left|\int\varphi\circ T\,d\mathcal E_N-\int\varphi\,d\mathcal E_N\right|\le \frac{2\|\varphi\|_\infty}{N}.
\]
Moreover successive empirical probabilities differ by a quantity tending to zero in any metric inducing weak-star convergence, because \(\mathcal E_{N+1}=\frac N{N+1}\mathcal E_N+\frac1{N+1}\delta_{T^Nz}\). In a compact metric space the cluster set of any sequence with vanishing successive distance is connected (otherwise its tail eventually cannot cross a positive separating gap). Hence \(\mathcal V(z)\) is a nonempty compact connected subset of the displayed probability segment, and so equals a unique closed subinterval.

**3. Explicit realization for any prescribed interval.** For \(0\le a<b\le1\), start with the single symbol \(1\). At stage \(n\ge1\), let
\[
\ell_n=a+\frac{b-a}{4(n+1)},\qquad h_n=b-\frac{b-a}{4(n+1)}.
\]
Let \(S\) be the current word length and \(Z\) its zero count. Append the **smallest positive** number \(A_n\) of zeros that makes the zero frequency at least \(h_n\), followed by the **smallest positive** number \(B_n\) of ones that makes the zero frequency at most \(\ell_n\). Both thresholds lie strictly between zero and one. Equivalently, for the values of \(S,Z\) at the beginning of stage \(n\),
\[
A_n=\left\lceil\frac{h_nS-Z}{1-h_n}\right\rceil,
\qquad
B_n=\left\lceil\frac{Z+A_n-\ell_n(S+A_n)}{\ell_n}\right\rceil.
\]
The first stage starts at zero frequency and every later stage starts below \(h_n\), so these integers are positive. The rounding errors in the achieved frequencies are at most the reciprocal of the new total length. The zero frequency rises monotonically through each zero block and falls monotonically through each one block. Both types of block length tend to infinity: the target oscillation gap \(h_n-\ell_n\) is bounded below by \((b-a)/2>0\), so each newly appended block has length at least a fixed positive multiple of the preceding total length for all sufficiently large \(n\). Thus the zero-frequency liminf and limsup are exactly \(a\) and \(b\).

For \(a=b=c\in(0,1)\), instead take
\[
w=0^{A_1}1^{B_1}0^{A_2}1^{B_2}\cdots,\qquad
A_n=\max\{1,\lceil cn^2\rceil\},\quad B_n=\max\{1,\lceil(1-c)n^2\rceil\}.
\]
When \(c=0\), use \(A_n=n\), \(B_n=n^2\); when \(c=1\), use \(A_n=n^2\), \(B_n=n\). All block lengths tend to infinity, the largest block among the first \(n\) is lower order than their total length, and the zero frequency converges to \(c\).

In all cases let \(w\) denote the resulting infinite binary word, and put \(X=\overline{\{\sigma^jw:j\ge0\}}\) inside the one-sided full binary shift, with \(T=\sigma|_X\). Because the successive zero and one block lengths both tend to infinity, an accumulation point of distinct shifts sees at most one symbol change in any fixed initial observation window. Both boundary orientations occur with arbitrarily long blocks. Consequently the accumulation points are **exactly**
\[
X'=\{0^\infty,1^\infty\}
\cup\{0^k1^\infty:k\ge1\}
\cup\{1^k0^\infty:k\ge1\}.
\]
These are all the possible limits, and all are actually attained by shifts starting a fixed distance before an ever later run boundary. Thus \(X''=\{0^\infty,1^\infty\}\), \(X'''=\emptyset\), and the two top points are fixed. Each original shift is isolated (its prefix containing two successive changes is not repeated arbitrarily late), so \(X\) is exactly the countable set of shifts of \(w\) together with the displayed points. The Mazurkiewicz–Sierpiński classification of countable compact metric spaces identifies \(X\cong\omega^2\cdot2+1\).

Finally, the number of symbol changes among the first \(N\) symbols of \(w\) is \(o(N)\), since both kinds of run length diverge. Given a cylinder-observation length \(m\), all but \(o(N)\) of the first \(N\) shifted sequences begin with \(m\) identical symbols. Uniform continuity therefore gives, for every \(\varphi\in C(X)\),
\[
\int\varphi\,d\mathcal E_N(w)
-d_N\varphi(0^\infty)-(1-d_N)\varphi(1^\infty)\longrightarrow0,
\]
where \(d_N\) is the zero frequency in the first \(N\) symbols. The vanishing one-step jumps of \(d_N\) force its full cluster set to be \([a,b]\), proving the desired empirical-measure limit set. The only periodic points are the two constants, so the entire stationary simplex is their convex hull for every constructed system.

## Verification
The all-length deductions use the compactness, periodic-orbit, rank and block-frequency arguments above; finite computations are not substituted for these proofs. The standalone `CHECK.py` reproducibly evaluates the exact rational block recurrences for three nontrivial intervals and the prescribed convergent case, checking endpoint bracketing and frequency monotonicity at each generated stage. In particular, for \([a,b]=[1/4,3/4]\), the first two block pairs are \((3,6)\), \((14,35)\). No brute-force enumeration is asserted to establish the classification of an infinite orbit closure.

## Relationship to prior work
Pérez-Remolina and Uzcátegui-Aylwin (2026) prove existence and a topological-conjugacy dichotomy for countable compact dense-orbit systems; they do not formulate the time-average interval spectrum. García-Ferreira, Rodríguez-López and Uzcátegui (2016/2018), especially Lemmas 3.1–3.2 for single-top-point ordinal compacta, establish foundational periodicity restrictions; the exclusion of lower-rank periodic points is not asserted as the original contribution. Sigmund's specification theorem (1974) permits general connected sets of empirical limit measures in specification systems such as full shifts, but does not provide a countable rank-two forward orbit closure with only two stationary atoms. Barwell–Good–Knight–Raines (2009/2010) characterize omega-limit sets in shifts of finite type, a different (topological rather than statistical) question. The contribution here is the **complete fixed-rank countable realization-and-necessity classification** for empirical measures, including the full continuum of intervals and endpoints.

## Limitations
The necessity statement assumes that both top-rank points are fixed. It does not classify top-rank permutations on larger finite derivatives, assert surjectivity of the constructed one-sided shift restriction, or provide rates of statistical convergence. The realization is a family of distinct maps on homeomorphic spaces, not a claim that one fixed map simultaneously realizes every interval with different dense-orbit points. Earlier equivalent sparse-block or historic-point constructions not found in the inspected literature remain a priority risk. No independent validation is claimed.

## References
1. J. Pérez-Remolina and C. Uzcátegui-Aylwin, *Countable dynamical systems with a dense orbit*, arXiv:2611.17315v1, first public 2026-11-12, https://arxiv.org/html/2611.17315v1.
2. S. García-Ferreira, Y. Rodríguez-López, and C. Uzcátegui, *Cardinality of the Ellis semigroup on compact metric countable spaces*, arXiv:1611.08290 (2016); *Semigroup Forum* 97 (2018), 162–176, https://arxiv.org/pdf/1611.08290.
3. K. Sigmund, *On dynamical systems with the specification property*, *Transactions of the AMS* 190 (1974), 285–299, doi:10.1090/S0002-9947-1974-0352411-X.
4. A. Barwell, C. Good, R. Knight and B. E. Raines, *A characterization of omega-limit sets in shift spaces*, *Ergodic Theory and Dynamical Systems* 30 (2010), 21–31, https://web.mat.bham.ac.uk/C.Good/research/pdfs/omega-shift.pdf.
