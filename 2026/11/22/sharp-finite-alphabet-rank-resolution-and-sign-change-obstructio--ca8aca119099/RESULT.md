# Sharp finite-alphabet rank resolution and sign-change obstruction

## Finding

Let an ordered alphabet contain \(K\ge 2\) letters, with null probabilities \(p_j>0\), \(\sum_{j=0}^{K-1}p_j=1\). Let the observation have an arbitrary alternative distribution \(q\), and let \(R_m\) be the uniformly tie-broken stochastic rank against \(m\ge1\) independent draws from \(p\). With independent reference simulations and tie-breaking for each observation, the following statements hold.

1. The set of alternatives that give the exact null rank law \(\Pr(R_m=r)=1/(m+1)\) has affine dimension \(\max(K-m-1,0)\) near \(p\). In particular, **every positive null distribution admits strictly positive non-null alternatives invisible to the entire rank sample whenever \(1\le m\le K-2\)**. For \(m\ge K-1\), no non-null alternative has a uniform rank law.
2. Every nonzero invisible perturbation \(q-p\) has at least \(m+1\) sign changes when its coordinates are read in alphabet order, ignoring zeros. This requirement is sharp for *every* positive null distribution: a vector with exactly \(m+1\) sign changes can be constructed from alternating maximal minors of the interval-moment matrix.
3. In the equal-probability case, write \(s=K-1\). For any \(0<\varepsilon<(K\max_{0\le j\le s}\binom{s}{j})^{-1}\), the strictly positive alternative

\[
q_j=\frac1K+\varepsilon(-1)^j\binom{s}{j},\qquad 0\le j\le s,
\]

has exactly the null rank law for every \(1\le m<s\), but first becomes visible at \(m=s\), where

\[
\Pr_q(R_s=r)=\frac1K+\frac{\varepsilon s!}{K^s}(-1)^r\binom{s}{r},\qquad 0\le r\le s.
\]

The corresponding Pearson chi-square departure from uniformity is exactly

\[
K\sum_{r=0}^{s}\left(\Pr_q(R_s=r)-\frac1K\right)^2
=\varepsilon^2(s!)^2 K^{1-2s}\binom{2s}{s}.
\]

For example, when \(K=5\), the null is uniform and \(q=(13,8,18,8,13)/60\). Ranks against one, two, or three reference observations are exactly uniform, even under this different alternative; for four references the rank probabilities are \(1/5+(2/3125)(-1)^r\binom4r\).

## Assumptions and scope

The alphabet is a **finite, fixed, strictly ordered** set with \(K\ge2\); the null has full support. The alternative is an arbitrary probability vector on that set, including boundary points. Ties use an independent continuous uniform label for each observed or simulated value, as in the original stochastic-rank procedure; in particular, comparisons sharing one observation also share its tie-breaking label. Reference samples are newly and independently generated for every observed data point. No claim concerns common reused reference samples or a different tie-breaking convention. Rank-only tests observe the ranks, rather than the original alphabet symbols. The conclusions apply to each finite number of observed ranks, and therefore to any rank-only decision based on that sample.

## Proof

**Randomized transform and moment equivalence.** Define \(a_0=0\) and \(a_{j+1}=a_j+p_j\). Given the observation's alphabet index \(J=j\), let \(Z=a_j+p_jU\), with \(U\) independent uniform on \((0,1)\). For each independent reference draw use its own analogous transform. Ordering the original symbol and its tie-label lexicographically is equivalent to ordering these transforms. Thus \(R_m\mid Z=z\sim\operatorname{Binomial}(m,z)\). Under the null \(Z\) is uniform; under \(q\), its density is the constant \(q_j/p_j\) on \((a_j,a_{j+1})\). It follows exactly that

\[
\Pr_q(R_m=r)=\sum_{j=0}^{K-1}\frac{q_j}{p_j}
\int_{a_j}^{a_{j+1}}\binom mr z^r(1-z)^{m-r}\,dz.
\]

The Bernstein polynomials \(\binom mr z^r(1-z)^{m-r}\), \(0\le r\le m\), form a basis for the polynomials of degree at most \(m\). Therefore the null and alternative rank laws coincide if and only if

\[
M_m(q-p)=0,\qquad
(M_m)_{kj}=\frac{a_{j+1}^{k+1}-a_j^{k+1}}{(k+1)p_j},
\quad 0\le k\le m,\ 0\le j<K.
\]

The row \(k=0\) is the all-ones row, ensuring mass conservation.

**Strict minors and the sharp resolution threshold.** For any \(d\le K\), the determinant of the first \(d\) rows of \(M_m\) at \(d\) columns with increasing indices \(j_1<\cdots<j_d\) is

\[
\frac{1}{\prod_{i=1}^d p_{j_i}}
\int_{a_{j_1}}^{a_{j_1+1}}\!\cdots\!
\int_{a_{j_d}}^{a_{j_d+1}}
\prod_{1\le i<\ell\le d}(z_\ell-z_i)\,dz_d\cdots dz_1>0.
\]

Indeed, multilinearity of the determinant gives the integral of the Vandermonde determinant; ordered disjoint intervals give a strictly positive integrand except on null boundaries. Consequently every such maximal minor is positive and \(\operatorname{rank}M_m=\min(K,m+1)\). When \(m<K-1\), \(\dim\ker M_m=K-m-1\). Because the positive vector \(p\) lies in the interior of the simplex and every kernel vector has coordinate sum zero, a sufficiently small perturbation \(q=p+\delta h\) is strictly positive, giving the full-dimensional local blind family. When \(m\ge K-1\), the kernel is zero.

**Sign variation and extremizers.** Suppose \(h=q-p\ne0\) changes sign \(s\le m\) times along its nonzero coordinates. Pick \(s\) boundary points separating its consecutive constant-sign blocks and form a real polynomial \(P\) with those simple roots. Choose its overall sign so \(P\) agrees strictly with the sign of \(h_j\) throughout each interval having \(h_j\ne0\); zero-mass blocks create no obstruction. The interval integral of \(P\) weighted by \(h_j/p_j\) is then strictly positive after summation, contradicting \(M_m h=0\), since \(\deg P\le m\). Hence any nonzero blind vector has at least \(m+1\) sign changes.

For sharpness, select any \(m+2\) ordered columns of the first \(m+1\) rows of \(M_m\). Let \(h_j\) on these columns be the corresponding signed maximal determinant obtained by deleting the selected column, and zero on all other columns. Every maximal determinant is strictly positive by the preceding formula, so the nonzero entries alternate in sign. The Laplace/cofactor identity gives \(M_mh=0\), and the vector has exactly \(m+1\) sign changes. Scaling it sufficiently preserves positivity of \(q=p+\delta h\).

**Explicit alternating perturbation.** For \(p_j=1/K\) the conditional expectation of any polynomial in \(Z=(j+U)/K\) of degree below \(s=K-1\) is a polynomial of degree below \(s\) in the index \(j\). Its signed binomial sum against \((-1)^j\binom sj\) vanishes by the finite-difference identity. At degree \(s\), the leading monomial survives with coefficient \((-1)^s s!\); applied to the Bernstein rank polynomial this gives the displayed exact response. Squaring and applying \(\sum_{r=0}^s\binom sr^2=\binom{2s}s\) yields the Pearson departure. This completes the proof.

## Verification

The bundled standalone `rank_resolution_check.py` uses exact SymPy rational arithmetic. Execute `python rank_resolution_check.py` in an environment with SymPy installed. It checks full rank for irregular null masses with \(2\le K\le10\), all claimed alternating blind laws and first-visible probabilities for \(3\le K\le10\), the Pearson departure formula, exhaustive bounded signed perturbations for \(3\le K\le6\), and alternating maximal-minor constructions for nonuniform nulls with \(3\le K\le7\). It completed **10,485 exact assertions**. These are supplementary finite checks: the determinant, sign-variation, and finite-difference arguments above prove the general claims.

## Relationship to prior work

Saad, Freer, Ackerman, and Mansinghka (2019) introduced the stochastic rank statistic, exact distribution-free null calibration, the exact arbitrary-alternative rank probability formula (Theorem 3.8), and eventual detection of every distinct alternative as the number of simulations increases (Theorem 3.4). Those results and ingredients are not claimed as new. The present theorem instead supplies a finite-support **exact simulation-budget cutoff**, the complete dimension of fixed-budget blind alternatives, their sharp sign-variation constraint, and an explicit first-visible rank spectrum. The latter conclusions do not follow from eventual detection without a further finite-rank argument. The core matrix positivity is an instance of classical Vandermonde/total-positivity theory; only its specific exact testing consequence and combined sharp classification are claimed here. No claim of exhaustive historical priority is made.

## Limitations

The alphabet must be finite and fully supported under the null. The exact cutoff is a worst-case universal identifiability guarantee; a particular alternative may be visible with far fewer reference simulations, and higher reference counts do not by themselves guarantee useful finite-observation power. If the model order or null mass vector is unknown, estimated, or misspecified, the stated exact assertions need not hold. The theorem does not address other rank orderings jointly, continuous or countably infinite supports, reused reference pools, or different randomized tie-breaking. Its historical priority remains subject to possible broader results about mixtures of binomial distributions, total positivity, and later expanded accounts of the original test.

## References

1. F. A. Saad, C. E. Freer, N. L. Ackerman, and V. K. Mansinghka (2019), *A Family of Exact Goodness-of-Fit Tests for High-Dimensional Discrete Distributions*, Proceedings of Machine Learning Research **89**, 1640–1649. Public preprint first posted 2019-02-26: https://arxiv.org/abs/1902.10142 ; https://proceedings.mlr.press/v89/saad19a.html . Theorems 3.1, 3.4, and 3.8, plus Appendix.
2. S. Karlin (1968), *Total Positivity*, Volume I. Classical background on sign-regular and totally positive matrices; the proof above is self-contained and does not assume a theorem from this reference.
