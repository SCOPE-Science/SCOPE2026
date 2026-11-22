# Strict log-concavity of zero-forcing polynomials for fully subdivided stars

## Finding
Let \(m\ge 2\) be an integer and let \(T_m\) be the tree obtained by subdividing every edge of \(K_{1,m}\) exactly once. If \(\mathcal Z(T_m;z)=\sum_k a_{m,k}z^k\) counts all ordinary zero-forcing sets by cardinality, then

\[
\mathcal Z(T_m;z)=z^{m-1}\left[(1+z)(2+z)^{m-1}(m+2z+z^2)-m-z\right].
\]

Every coefficient from degree \(m-1\) through degree \(2m+1\) is positive, and the nonzero coefficient sequence is **strictly log-concave**:
\[
a_{m,k}^2>a_{m,k-1}a_{m,k+1}\qquad(m\le k\le 2m).
\]
In particular it is unimodal for every branching number. The result concerns ordinary zero forcing, not connected, total, positive-semidefinite, or super domination.

## Assumptions and scope
The graph is a finite simple tree. Its center is \(c\), each interior arm vertex \(u_i\) is adjacent to \(c\) and to a private leaf \(v_i\), and there are no other edges, for \(1\le i\le m\). Hence the graph has \(2m+1\) vertices. A blue vertex with exactly one white neighbor may color that neighbor blue; a zero-forcing set is an initial blue set from which repeated such moves color every vertex. All initial sets are counted once, without counting forcing orders. The two-arm case is a path and is included in the theorem. Strict log-concavity is asserted on the full contiguous positive support; no statement is made about arbitrary trees or spiders with other arm lengths.

## Proof

**Step 1: classification of all forcing sets.** For arm \(i\), use the two-bit state of \((u_i,v_i)\). The three nonempty states have generating polynomial \(A(z)=2z+z^2\); the empty state has weight \(1\).

If the center is initially blue, at most one arm may be empty. Indeed, with two empty arms the center has at least two white neighbors forever, while no vertex of either empty arm can force. Conversely, on every nonempty arm the leaf or interior blue vertex can complete that arm (when necessary), and the center subsequently forces the unique empty arm, if present. The polynomial for this case is \(z[A(z)^m+mA(z)^{m-1}]\).

If the center is initially white, the same at-most-one-empty-arm condition is necessary. In addition, at least one arm must have its leaf initially blue; otherwise all occupied arms consist only of a blue interior vertex, no first force is possible, and the center remains white. Conversely, an initially blue leaf forces its interior vertex if needed, that interior vertex forces the white center once its leaf is blue, all other occupied arms complete, and the center forces a possible single empty arm. There are exactly \(z^m+mz^{m-1}\) nonempty-arm configurations with no blue leaf. The polynomial for the white-center case is \(A(z)^m+mA(z)^{m-1}-z^m-mz^{m-1}\).

Adding the cases, factoring \(A(z)=z(2+z)\), gives precisely the displayed formula. In particular the minimum forcing cardinality is \(m-1\), and the full cardinality polynomial has no missing positive-support degrees.

**Step 2: an exact positive coefficient formula.** Set
\[
P_m(z)=(1+z)(2+z)^{m-1}(m+2z+z^2)=\sum_{j=0}^{m+2}p_jz^j,
\quad Q_m(z)=P_m(z)-m-z=\sum_{j=0}^{m+2}q_jz^j.
\]
For \(0\le j\le m+2\), let \(L=m+2-j\), and put \(f_j=L(L-1)+4j\). Binomial expansion and cancellation of factorials yield
\[
p_j=\frac{2^{m-1-j}\binom{m+2}{j}(m+j)f_j}{(m+1)(m+2)}.
\]
This formula remains valid at the endpoints; negative exponents of \(2\) in the displayed expression are balanced by other factors and give integer coefficients. All \(p_j\) are positive. The correction gives \(q_0=m(2^{m-1}-1)>0\), \(q_1=p_1-1>0\), and \(q_j=p_j>0\) for \(j\ge2\).

**Step 3: strict log-concavity of the uncorrected coefficients.** For the sequence \(b_j=\binom{m+2}{j}f_j\), the internal strict log-concavity inequality is equivalent, after cancelling positive factorials, to
\[
E=(j+1)(L+1)f_j^2-jL f_{j-1}f_{j+1}>0,
\]
where the adjacent factors are computed using \(L+1\) and \(L-1\), respectively. Write \(x=j-1\ge0\) and \(y=L-1\ge0\). Direct polynomial expansion, without an approximation, gives
\[
\begin{aligned}
E={}&16x^3+(8y^2+16y+72)x^2\\
&+(y^4+12y^3+29y^2+42y+104)x\\
&+y^5+5y^4+17y^3+23y^2+26y+48>0.
\end{aligned}
\]
Every term is nonnegative and the constant term is strictly positive. Since \(p_j\) is a positive constant times \(2^{-j}(m+j)b_j\), and the geometric factor has equality in log-concavity whereas \((m+j)^2-(m+j-1)(m+j+1)=1\), the sequence \((p_0,\ldots,p_{m+2})\) is strictly log-concave at every interior index.

**Step 4: correction at the first two coefficients.** For \(j\ge2\), the inequality for \(q_j\) follows from the inequality for \(p_j\), because only \(q_0\) and \(q_1\) were reduced. At \(j=1\),
\[
q_1^2-q_0q_2=(p_1^2-p_0p_2)+(mp_2-2p_1+1).
\]
The first parenthesis is positive by Step 3. Directly from the coefficient formula,
\[
p_1=2^{m-2}(m^2+m+4),\qquad
p_2=2^{m-4}(m+2)(m^2-m+8),
\]
and hence
\[
mp_2-2p_1=2^{m-4}(m-2)(m^3+3m^2+4m+16)\ge0.
\]
Thus the remaining inequality also holds strictly for every \(m\ge2\). Multiplication by \(z^{m-1}\) merely shifts coefficient indices. This completes the proof.

## Verification
The attached standard-library program `verify_subdivided_star.py` independently enumerates every initial subset and applies the ordinary zero-forcing color-change rule for \(2\le m\le7\), comparing all coefficients with the formula. It also checks the positive-coefficient expression, the strict log-concavity inequalities for \(2\le m\le200\), and the complete bivariate polynomial identity for \(E\). The bivariate identity check uses interpolation on a grid exceeding both bidegrees; the infinite theorem follows from the algebraic identities proved above, not from finite enumeration. Recorded execution: `VERIFY_OK`, 43,680 initial subsets.

For a small reproducible example, \(\mathcal Z(T_3;z)=9z^2+31z^3+35z^4+21z^5+7z^6+z^7\).

## Relationship to prior work
Boyer and collaborators introduced the zero-forcing polynomial and proved general structural identities and initial coefficient monotonicity. Their 2018 preprint (2019 journal article), including its section on named graph families and concluding conjectures, does not state this subdivided-star log-concavity result. Newton and Brimkov's November 8, 2026 preprint disproves general unimodality and explicitly asks whether all **tree** zero-forcing polynomials are unimodal; this theorem proves the stronger strict-log-concavity property on the infinite fully subdivided-star subfamily.

Williams's publicly accessible research description, “Zero forcing polynomials: mapping spiders to paths,” describes unspecified spider polynomials and coefficientwise path comparisons. Its full thesis text was not accessible in this comparison. The polynomial formula here might have an earlier derivation there; the strict all-branching log-concavity proof is the principal claim. Related work on super-domination polynomials of radius-two spiders and on zero-forcing polynomials of subdivided complete graphs concerns different invariants or different graph families and does not itself imply the claim.

## Limitations
The theorem makes no assertion for general trees, arbitrary spiders, or all radius-two spiders with additional single-edge arms. Bibliographic search and available source inspection do not prove absolute historical priority; the inaccessible full spider thesis is a specific residual risk. The attached enumeration is finite and corroborative; it is not the all-order argument. No independent mathematical validation has been performed.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1 (January 26, 2018), *Discrete Applied Mathematics* 258 (2019), 35–48. https://arxiv.org/abs/1801.08910.
2. T. Newton and B. Brimkov, “Zero forcing is not unimodal,” arXiv:2611.11352v1 (November 8, 2026). https://arxiv.org/abs/2611.11352.
3. S. Williams, “Zero forcing polynomials: mapping spiders to paths,” publicly accessible research abstract, undated. https://sites.google.com/view/savannah-williams/research/undergraduate-research.
