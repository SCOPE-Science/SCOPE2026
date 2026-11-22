# Sharp Doeblin-minorized adjugate norm for finite Markov operators

## Finding
Let \(n\ge 2\), let \(\alpha\in[0,\infty)^n\) have \(s=\sum_{i=1}^n\alpha_i<1\), and put \(a=\min_i\alpha_i\). Among all column-stochastic \(n\times n\) matrices \(P\) satisfying \(P_{ij}\ge\alpha_i\) for every \(i,j\), the exact optimal adjugate operator norm is
\[
\max_P\|\operatorname{adj}P\|_{\ell_1^n\to\ell_1^n}
=2(1-a)(1-s)^{n-2}.
\]
The same number is the sharp supremum of \(|\det P|\,\|P^{-1}\|_{\ell_1^n\to\ell_1^n}\) over *invertible* matrices in this class. The maximum over all stochastic matrices is attained by a singular, deterministic-after-minorization channel with exactly one duplicated output and one omitted output. Invertible channels approach the same bound explicitly.

For the uniform Doeblin lower bound \(\alpha_i=\theta/n\), \(0\le\theta<1\), the sharp constant is \(2(1-\theta/n)(1-\theta)^{n-2}\). Thus any fixed positive common refresh probability \(\theta\) produces an exponentially decaying sharp determinant-weighted inverse bound as the number of states increases, whereas the unmixed endpoint has the dimension-independent constant \(2\).

## Assumptions and scope
All stochastic matrices here are real, entrywise nonnegative, and **column** stochastic: \(\mathbf1^{\mathsf T}P=\mathbf1^{\mathsf T}\). The matrix is viewed as an operator on real or complex \(\ell_1^n\), with induced norm equal to the maximum absolute column sum. Its classical adjugate is defined by cofactors for *every* square matrix, singular or nonsingular. The minorization vector is fixed in advance, and the theorem makes no reversibility, irreducibility, or spectral-gap assumption. The restriction \(s<1\) makes the residual stochastic factor nondegenerate; the displayed formula extends continuously at \(s=1\), with the usual degree-zero convention when \(n=2\).

## Proof
Write \(t=1-s>0\), \(\mathbf1=(1,\dots,1)^{\mathsf T}\), and \(B=tI+\alpha\mathbf1^{\mathsf T}\). Every admissible \(P\) is uniquely \(\alpha\mathbf1^{\mathsf T}+tQ\), with \(Q\) column stochastic. Since \(\mathbf1^{\mathsf T}Q=\mathbf1^{\mathsf T}\), one has \(P=BQ\), \(\det B=t^{n-1}\), and \(B^{-1}=t^{-1}(I-\alpha\mathbf1^{\mathsf T})\). The polynomial adjugate identity gives
\[
\operatorname{adj}P=t^{n-2}\operatorname{adj}Q\,(I-\alpha\mathbf1^{\mathsf T}).\tag{1}
\]
For \(n=2\) the exponent in (1) is zero.

Fix all but one column of \(Q\). Each entry of \(\operatorname{adj}(BQ)\) is a cofactor, hence a determinant of an \((n-1)\times(n-1)\) minor and is affine in that remaining column. Therefore the absolute column sums, and their maximum \(\|\operatorname{adj}(BQ)\|_1\), are convex in each column separately. Every stochastic column belongs to the simplex spanned by the standard basis. Replacing columns successively by appropriate simplex vertices cannot decrease this function. It is therefore enough to test deterministic maps: matrices \(Q\) with precisely one standard-basis vector in every column. This reduction is valid even for singular matrices and requires no assumption about inverse continuity.

Let \(r\) be the number of distinct rows hit by the deterministic map. If \(r\le n-2\), then \(\operatorname{rank}Q\le n-2\) and \(\operatorname{adj}Q=0\). If \(r=n\), then \(Q\) is a permutation and \(\operatorname{adj}Q\) is a signed permutation. Consequently (1) has norm
\[
t^{n-2}\max_j\bigl((1-\alpha_j)+\sum_{i\ne j}\alpha_i\bigr)
=t^{n-2}(1+s-2a)\le 2(1-a)t^{n-2}.
\]
If \(r=n-1\), one output row \(k\) is omitted and precisely two input columns, say \(u,v\), have the same output. The adjugate is \(\pm(e_u-e_v)e_k^{\mathsf T}\). Multiplying by the second factor in (1) gives
\[
\|\operatorname{adj}P\|_1
=2t^{n-2}\max\{1-\alpha_k,\alpha_k\}
\le 2(1-a)t^{n-2}.
\]
Indeed \(1-\alpha_k\le1-a\), while \(\alpha_k\le s-a<1-a\). Choose the omitted row \(k\) with \(\alpha_k=a\). Because \(a\le s/n<1/2\), this deterministic matrix attains \(2(1-a)t^{n-2}\), proving the stated maximum.

For the invertible supremum, choose a deterministic \(Q_0\) hitting all rows except \(k\) and repeating one row \(h\ne k\), with its last column equal to \(e_h\). Replace that last column by \((1-\delta)e_h+\delta e_k\), with \(0<\delta\le1\), and call the result \(Q_\delta\). The other columns hit all rows except \(k\) exactly once, so \(|\det Q_\delta|=\delta\). Thus \(P_\delta=BQ_\delta\) is admissible and invertible, with \(|\det P_\delta|=t^{n-1}\delta\). By continuity of cofactors,
\[
\lim_{\delta\downarrow0}|\det P_\delta|\,\|P_\delta^{-1}\|_1
=\lim_{\delta\downarrow0}\|\operatorname{adj}P_\delta\|_1
=2(1-a)t^{n-2}.
\]
This also supplies an explicit sharp near-singular channel.

## Verification
The proof is exact for every integer \(n\ge2\) and every admissible real vector \(\alpha\); no finite search is used to infer universal validity. The accompanying standard-library checker `check_markov_adjugate.py` uses rational arithmetic and direct signed-minor determinants. It exhaustively checks deterministic maps for several independent nonuniform minorants at \(n=2,3,4\), tests additional rational stochastic matrices through \(n=5\), and checks the explicit extremal maps. Run it with `python3 check_markov_adjugate.py` from the extracted file directory. Its output for this package is `MINORIZED_MARKOV_ADJUGATE_EXACT_CHECK_OK 1253`.

## Relationship to prior work
The determinant–inverse-norm problem originates with Schäffer's inequality. Houache, Szehr and Zarouf (2026) establish its sharp \(\sqrt n\) asymptotic for unrestricted Banach-space norms. The present claim instead fixes the endpoint \(\ell_1^n\) operator norm, restricts to Markov operators and determines the exact dependence on a nonuniform common stochastic minorant. Goldberg (1966) proves a sharp determinant bound for stochastic matrices, including common-entry-minimum effects; that determinant estimate is distinct from the maximal absolute column sum of the adjugate. Standard Doeblin minorization bounds concern total-variation mixing rather than the volume-weighted inverse norm. Existing stochastic-equilibrium adjugate formulae concern the stationary-vector equations, rather than this extremal inverse inequality.

## Limitations
The theorem concerns the induced \(\ell_1\)-norm of the *classical adjugate*, not the inverse norm alone, a smallest singular value, or the inverse of \(I-P\). It does not classify all stochastic matrices attaining the maximum and does not assert that an invertible matrix attains the supremum. The formulas should not be extrapolated to arbitrary signed matrices, arbitrary operator norms, or varying columnwise lower-bound vectors. A pre-existing equivalent adjugate extremum under different terminology remains a possible bibliographic risk; the source comparisons do not establish absolute novelty.

## References
1. S. Houache, O. Szehr and R. Zarouf, *Schäffer's matrix inequality: the exact asymptotic constant*, arXiv:2608.20217v1, first posted 20 August 2026. https://arxiv.org/abs/2608.20217 ; full text: https://pdfs.assets.alphaxiv.org/2608.20217v1.pdf
2. K. Goldberg, *Upper Bounds for the Determinant of a Row Stochastic Matrix*, Journal of Research of the National Bureau of Standards B 70B (1966), 157–158. https://nvlpubs.nist.gov/nistpubs/jres/70B/jresv70Bn2p157_A1b.pdf
3. M. Visser, *Explicit formulae for stochastic equilibria*, arXiv:2601.19023v1, 26 January 2026. https://arxiv.org/abs/2601.19023
4. E. Seneta, *Non-negative Matrices and Markov Chains*, Springer, second edition, 1981 (background on coefficients of ergodicity and stochastic matrices).
