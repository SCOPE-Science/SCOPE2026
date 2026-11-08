# Sharp rectangular puncture norms and complete-row localization in real bilinear Walsh spaces

## Finding

Let \(m,n\ge2\) be **unequal** integers, with independent uniform signs \(\varepsilon_1,\ldots,\varepsilon_m\) and \(\eta_1,\ldots,\eta_n\). For real coefficients \(a_{ij}\), where the corner \(a_{mn}=0\), put
\[
F_a=\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}\varepsilon_i\eta_j,
\qquad B=\mathbb E F_a^2=\sum_{i,j}a_{ij}^2.
\]
Then **the exact unrestricted coefficient norm** is
\[
\boxed{\sup_{B>0}\frac{\mathbb E F_a^4}{B^2}
=\left(3-\frac{2}{\max(m,n)-1}\right)
\left(3-\frac2{\min(m,n)}\right).}
\tag{1}
\]
If \(m>n\), *every* nonzero optimizer has its entire last row zero, and the remaining \((m-1)\times n\) coefficient block has one common nonzero magnitude with factorized signs:
\[
a_{ij}=s\sigma_i\tau_j \quad (i<m,\ 1\le j\le n),
\qquad a_{mj}=0,
\tag{2}
\]
for \(s\in\mathbb R\setminus\{0\}\) and \(\sigma_i,\tau_j\in\{-1,1\}\). For \(n>m\), transpose (2): the last column vanishes, and the other \(m\times(n-1)\) entries are flat with factorized signs. All those patterns attain (1). The sharp \(L^2\to L^4\) operator norm is the fourth root of (1).

This **complete-row/column localization** differs from the square puncture problem, where the exact optimizer retains nonzero coefficients on both arms adjacent to the missing corner. The transition is structural and is not obtained by substituting unequal dimensions into the known square formula.

## Assumptions and scope

All coefficient scalars are real, and all signs are independent, symmetric and normalized to probability one. The corner deletion is exactly one coordinate \((m,n)\); no other coefficient is required to vanish. The integers satisfy \(m,n\ge2\) and \(m\ne n\). For the proof assume \(m>n\), set \(a=m-1\), \(b=n-1\); then \(a\ge b+1\) and \(b\ge1\). The case \(n>m\) follows by transposition. The zero coefficient array satisfies the unnormalized fourth-power inequality trivially, but does not enter its normalized ratio.

## Proof

**1. Exact moment expansion.** Regard entries as edges in the punctured complete bipartite graph. Rademacher orthogonality implies that in a fourth power, edge multiplicities must have even vertex degree. Besides pairings of equal edges, the only configuration with four distinct edges is a four-cycle (rectangle). Thus, with \(\mathcal R\) the set of allowed rectangles,
\[
\mathbb E F_a^4=3B^2-2\sum_{i,j}a_{ij}^4
+24\sum_{R\in\mathcal R}\prod_{(i,j)\in R}a_{ij}.
\tag{3}
\]
Taking absolute values preserves \(B\), preserves the quartic self-term and weakly increases the rectangle contribution. Therefore we first maximize over nonnegative arrays.

**2. Two energy-preserving RMS symmetrizations.** For each column \(j\), replace its first \(a\) entries \(u_i\) by the common value \(\sqrt{S_j/a}\), where \(S_j=\sum_{i=1}^{a}u_i^2\), leaving the final row unchanged. This preserves \(B\) and decreases \(\sum a_{ij}^4\). To check the rectangle term explicitly, for any columns \(j<\ell\), with their top vectors \(u_i,v_i\),
\[
\sum_{i<k\le a}u_iu_kv_iv_k
\le \sqrt{\sum_{i<k}u_i^2u_k^2}\sqrt{\sum_{i<k}v_i^2v_k^2}
\le\frac{a-1}{2a}S_jS_\ell.
\tag{4}
\]
When both columns are among the first \(b\), their rectangles with the bottom row obey
\[
a_{mj}a_{m\ell}\sum_{i=1}^{a}u_iv_i
\le a_{mj}a_{m\ell}\sqrt{S_jS_\ell}.
\tag{5}
\]
Every right-hand side is attained after flattening, so the fourth moment does not decrease. Next apply the transposed construction to the **first \(b\) columns within every row**, leaving the rightmost column unchanged. Again quartic self-terms decrease and each rectangle contribution is bounded by its flattened value. Since the upper rows are identical after the first operation, the second keeps them identical. The resulting matrix has just three nonnegative block values:
\[
a_{ij}=\begin{cases}
 t,&i\le a,\ j\le b,\\
 u,&i\le a,\ j=b+1,\\
 v,&i=a+1,\ j\le b,\\
 0,&i=a+1,\ j=b+1.
\end{cases}
\tag{6}
\]
Both operations preserve the energy. Hence maximizing (3) reduces rigorously to (6).

**3. Exact three-block polynomial.** Write \(p=ab t^2/B\), \(q=a u^2/B\), \(r=b v^2/B\). Then \(p,q,r\ge0\), \(p+q+r=1\). Counting \(\binom a2\binom b2\) internal rectangles and \(a\binom b2\), \(b\binom a2\) mixed rectangles yields
\[
\Phi_{a,b}(p,q,r)=3
+\frac{6(a-1)(b-1)-2}{ab}p^2
-\frac2a q^2-\frac2b r^2
+\frac{12(a-1)}a pq+\frac{12(b-1)}b pr.
\tag{7}
\]
Define
\[
C=\frac{3a-2}{a}\frac{3b+1}{b+1},\qquad
p_*(r)=\frac{3ab-2b-(3a-2b)r}{(3a-2)(b+1)},
\tag{8}
\]
\[
H=\frac{2N}{ab(3a-2)(b+1)},\quad
L=\frac{4(3a-3b-1)}{a(b+1)},
\tag{9}
\]
where, setting \(h=a-b\ge1\),
\[
N=(21b-6)h^2+(27b^2-17b-2)h+(6b^3-5b^2).
\tag{10}
\]
Direct expansion of (7), substituting \(q=1-p-r\), proves the **exact nonnegative deficit identity** for every simplex point:
\[
\boxed{C-\Phi_{a,b}(p,q,r)=
\frac{2(3a-2)(b+1)}{ab}\bigl(p-p_*(r)\bigr)^2
+Lr(1-r)+Hr^2.}
\tag{11}
\]
Here \(L>0\), because \(a-b\ge1\). Each coefficient in (10) is strictly positive for every integer \(b\ge1\), so \(N>0\), hence \(H>0\). Thus (11) proves \(\Phi\le C\) for all \(0\le r\le1\). Equality forces \(r=0\), \(p=p_*(0)=b/(b+1)\), and \(q=1/(b+1)\). Translating these identities back to \(t,u,v\), we obtain \(v=0\) and \(t^2=u^2>0\). This proves sharpness and uniqueness of the *nonnegative three-block optimizer*.

**4. Pullback of all equality cases.** To attain the global maximum, the pre-symmetrized nonnegative coefficient matrix must attain equality at every symmetrization step. In each column the inequality \(\sum_{i=1}^a u_i^4\ge S_j^2/a\) is strict unless all \(a\) upper squared entries are equal. The final three-block pattern has strictly positive top coefficients in every column, so this forces the original top block to have the same magnitudes; the bottom row already has zero energy from the equality in (11). For the original signed array, equality on taking absolute values requires the product of signs on every rectangle in the complete \(a\times(b+1)\) active block to be positive. A sign matrix has all positive rectangular products exactly when it factorizes into row and column signs (fix a base row and column). This gives (2) and completes the equality classification. Conversely (2) factorizes \(F_a\) into a product of two independent equal-coefficient Rademacher sums, whose normalized fourth moments are \(3-2/a\) and \(3-2/(b+1)\), proving direct attainment of \(C\).

## Verification

The accompanying `verify.py` uses exact rational arithmetic (Python standard library). It independently enumerates all signs for 180 seeded integer coefficient arrays in rectangular sizes up to \(6\times5\), checks the rectangle moment identity, confirms explicit sharp witnesses, tests the exact global deficit at 2,700 rational simplex points spanning all dimension regimes up to \(b=30\), and verifies the positive polynomial identity on a wide integer range. Running `python3 verify.py` returned `ALL_RECTANGULAR_RADEMACHER_NORM_CHECKS_PASSED`. The proof for infinitely many dimensions is the exact expansion and inequalities (3)–(11); finite tests are consistency checks, not an exhaustive substitute.

## Relationship to prior work

Ibragimov, Sharakhmetov and Cecen [1] establish sharp moment estimates for ordinary and decoupled bilinear forms under restrictions on moments of individual independent random variables. Their Theorems 4–8 concern distributional optimization of the unweighted complete or off-diagonal bilinear expressions and do not optimize an arbitrary real coefficient matrix with one deleted corner. The complete-space bilinear Rademacher bound is the product of the finite Khintchine constants, \((3-2/m)(3-2/n)\), but that broader ambient bound is strictly weaker for the punctured rectangular space.

A more directly comparable **published square puncture classification** [2] obtains an optimizer with a positive central block and two nonzero arms for every \(m=n\ge2\). It explicitly assumes a square coefficient matrix; its three-block stationary formula and equality statements do **not** imply the present unequal-dimensional localization. The proof technique of two RMS symmetrizations is related, but here the crucial rectangular nonnegative certificate (11) gives a different support pattern. The distinction is the mathematical point: exactly when the row and column counts differ, the optimal coefficient matrix discards an entire damaged row/column, whereas the square counterpart retains both arms.

The fourth-moment literature on Rademacher chaos and normal approximation [3] studies different asymptotic questions. Searches of published-finding corpus and accessible prior records for rectangular, deleted-edge, sparse and bilinear formulations identified no stronger covering theorem. This is a qualified comparison, not an assertion that a search establishes absolute historical novelty.

## Limitations

This exact theorem is restricted to real coefficients, independent symmetric signs, one missing corner, unequal **rectangular** dimensions, and exponent four. The equal-dimensional case is not covered here and is addressed separately by [2]. The deficit (11) concerns the RMS-reduced three-block energy parameters, not an independently derived lower bound on coefficient distance to the full equality orbit. Sparse graph generalizations, complex coefficients, nonuniform signs and other moments remain untreated. An unindexed earlier inequality might contain an equivalent sharp restricted-space statement.

## References

[1] R. Ibragimov, Sh. Sharakhmetov and A. Cecen, *Exact Estimates for Moments of Random Bilinear Forms*, arXiv:math/9909111, first submitted September 20, 1999; *Journal of Theoretical Probability* **14** (2001), 21–37. https://arxiv.org/abs/math/9909111 . Author-hosted open full text: https://scholar.harvard.edu/files/ibragimov/files/jtp.pdf .

[2] *Sharp fourth moments for a punctured bilinear Rademacher chaos*, published-finding corpus, 2026, square coefficient-space theorem. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-for-a-punctured-bilinear-rademacher-chaos--452326a16334 .

[3] C. Döbler and K. Krokowski, *On the Fourth Moment Condition for Rademacher Chaos*, arXiv:1706.00751, 2017. https://arxiv.org/abs/1706.00751 .
