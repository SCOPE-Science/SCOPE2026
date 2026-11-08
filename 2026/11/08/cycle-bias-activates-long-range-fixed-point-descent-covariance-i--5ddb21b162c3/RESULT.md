# Cycle bias activates long-range fixed-point–descent covariance in Ewens permutations

## Finding

For every integer \(n\ge3\) and real \(\theta>0\), let \(\Pi\) have the Ewens permutation law
\[
\Pr\{\Pi=\pi\}=\frac{\theta^{c(\pi)}}{\theta(\theta+1)\cdots(\theta+n-1)},\qquad \pi\in S_n,
\]
where \(c(\pi)\) is the total number of cycles, including fixed points. Put
\(F_j=\mathbf1\{\Pi(j)=j\}\), \(D_i=\mathbf1\{\Pi(i)>\Pi(i+1)\}\),
\(F=\sum_{j=1}^nF_j\), \(D=\sum_{i=1}^{n-1}D_i\), and
\(D_\circ=D+\mathbf1\{\Pi(n)>\Pi(1)\}\). Thus \(D_\circ\) counts descents when the **one-line** image sequence is read around a circle; it is not a cycle-notation descent statistic.

Define, for every integer \(m\ge2\),
\[
q_m=\frac{(m-1)(m/2+\theta-1)}{(m+\theta-1)(m+\theta-2)}.
\]
The full fixed-point/ordinary-descent cross-covariance matrix is
\[
\boxed{\operatorname{Cov}(F_j,D_i)=
\frac{\theta}{n+\theta-1}
\begin{cases}
\dfrac{i-1}{n+\theta-2}-q_n,&j=i,\\[5pt]
\dfrac{n-i-1}{n+\theta-2}-q_n,&j=i+1,\\[5pt]
q_{n-1}-q_n,&j\notin\{i,i+1\},
\end{cases}}
\qquad 1\le i<n,\quad1\le j\le n.
\]
For every nonadjacent pair \(j\notin\{i,i+1\}\), the entry equals the same number,
\[
\boxed{\operatorname{Cov}(F_j,D_i)=
-\frac{\theta^2(\theta-1)}{(n+\theta-3)(n+\theta-2)(n+\theta-1)^2}.}
\]
It is strictly positive when \(0<\theta<1\), zero when \(\theta=1\), and strictly negative when \(\theta>1\). At \(\theta=1\), these nonadjacent indicators are in fact independent. Thus the uniform model is the exact parameter at which the off-neighborhood covariance background disappears.

The aggregate *cyclic* count has the sharp sign transition
\[
\boxed{\operatorname{Cov}(F,D_\circ)=
-\frac{n\theta(n-2)(\theta-1)(n+2\theta-3)}{(n+\theta-3)(n+\theta-2)(n+\theta-1)^2}.}
\]
For every \(n\ge3\), it is positive when \(0<\theta<1\), zero precisely when \(\theta=1\), and negative when \(\theta>1\). By contrast, the ordinary descent count satisfies
\[
\operatorname{Cov}(F,D)=
-\frac{\theta^2(n-1)(n^2+2n\theta-4n-2\theta+2)}{(n+\theta-3)(n+\theta-2)(n+\theta-1)^2},
\]
which is strictly negative for all \(n\ge4\) and \(\theta>0\). For \(n=3\), the latter covariance changes sign at \(\theta=1/4\). These aggregate formulas are consequences of the same positionwise calculation; the aggregate ordinary-descent covariance is not asserted to be a new enumeration independent of older cycle-type/descent-set formulas.

## Assumptions and scope

Every \(\theta>0\) is allowed, including nonintegral values. No large-sample assumption is made: the positionwise and aggregate statements hold at each finite integer \(n\ge3\). Positions and labels are \(1,\ldots,n\), with ordinary descents only at \(1,\ldots,n-1\). All conditional probabilities below refer to conditioning under the same Ewens law. The circular comparison is between the last and first *positions* in the one-line representation.

## Proof

**1. Marginals and fixed-point deletion.** The Ewens weight and its normalization give
\[
\Pr(F_j=1)=p_n:=\frac{\theta}{n+\theta-1}.
\]
Conditional on \(F_j=1\), delete the fixed letter \(j\) and order-preservingly relabel all remaining positions and values. The induced permutation has the Ewens law on \(n-1\) letters with parameter \(\theta\): its cycle count is one less and every remaining permutation has the same conditional normalizing factor. The single-image formula in the reduced model is
\[
\Pr\{\Pi'(k)=a\}=
\begin{cases}\theta/(n+\theta-2),&a=k,\\1/(n+\theta-2),&a\ne k.\end{cases}
\]
This also follows from the partial-permutation moment formula in Féray, Lemma 2.11, but no independence of permutation entries is assumed.

**2. An ordinary-descent marginal.** The partial-permutation moment formula gives denominator \((n+\theta-1)(n+\theta-2)\) for each pair of prescribed distinct images at adjacent positions. Among the \(\binom n2\) pairs \(a>b\), a fixed arc at the left position occurs in \(i-1\) choices; a fixed arc at the right position in \(n-i-1\) choices; and the transposition of these two positions occurs once. Each of these \(n-1\) configurations receives the extra factor \(\theta\) rather than \(1\). The two simultaneously fixed arcs form an ascent and introduce no double correction. Consequently, for every \(1\le i<n\),
\[
\Pr(D_i=1)=\frac{\binom n2+(n-1)(\theta-1)}{(n+\theta-1)(n+\theta-2)}=q_n.
\]
The calculation is valid also for \(n=3\).

**3. Positionwise conditional descents.** Given \(F_j=1\), if \(j\notin\{i,i+1\}\), deleting \(j\) preserves the ordinary descent between the two adjacent remaining positions, hence \(\Pr(D_i=1\mid F_j=1)=q_{n-1}\). If \(j=i\), there are exactly \(i-1\) possible smaller images of \(i+1\), none equal to that position; hence the conditional probability is \((i-1)/(n+\theta-2)\). If \(j=i+1\), there are exactly \(n-i-1\) possible larger images of \(i\), none fixed there; hence the conditional probability is \((n-i-1)/(n+\theta-2)\). Multiplying each difference from \(q_n\) by \(p_n\) gives the entire cross-covariance matrix. Elementary common-denominator reduction gives
\[
q_{n-1}-q_n=-\frac{\theta(\theta-1)}{(n+\theta-3)(n+\theta-2)(n+\theta-1)},
\]
which proves the nonadjacent sign classification. When \(\theta=1\), \(q_{n-1}=q_n=1/2\); the displayed conditional probability equals the unconditional probability, proving independence rather than merely zero covariance for nonadjacent pairs.

**4. Circular boundary comparison.** Let \(W=\mathbf1\{\Pi(n)>\Pi(1)\}\). For \(n\ge2\), the \(\binom n2\) image pairs producing \(W=1\) include \(n-1\) with the first prescribed arc fixed at position \(n\) and \(n-1\) with the second arc fixed at position \(1\). The pair with both arcs fixed is counted in both groups, hence receives the correction \((\theta-1)^2\) in addition to the two linear corrections. The transposition of the two endpoints is an ascent for the circular comparison. Therefore
\[
w_n:=\Pr(W=1)=\frac{\binom n2+2(n-1)(\theta-1)+(\theta-1)^2}{(n+\theta-1)(n+\theta-2)}.
\]
Conditioning on \(F_j=1\), \(W\) is certain for \(j=1\) or \(j=n\), and has probability \(w_{n-1}\) for every other \(j\), by order-preserving deletion. Summing the conditional differences yields
\[
\operatorname{Cov}(F,W)=p_n\{2+(n-2)w_{n-1}-nw_n\}.
\]
Similarly summing the full ordinary cross-covariance matrix gives
\[
\operatorname{Cov}(F,D)=p_n\left\{(n-1)(n-2)q_{n-1}+\frac{(n-1)(n-2)}{n+\theta-2}-n(n-1)q_n\right\}.
\]
Combining these two equations and substituting the rational expressions for \(q_m,w_m\), a common denominator \((n+\theta-3)(n+\theta-2)(n+\theta-1)^2\) yields the two aggregate formulas in the Finding section.

**5. Signs and boundary cases.** For \(n\ge3\), all denominators are positive and \(n+2\theta-3>0\). Thus the cyclic sign is exactly the sign of \(1-\theta\). For \(n\ge4\), the numerator factor in the ordinary covariance is
\[
n^2+2n\theta-4n-2\theta+2=(n-2)^2-2+2(n-1)\theta>0.
\]
At \(n=3\) it becomes \(4\theta-1\). At \(n=2\), outside the stated theorem's domain, the cyclic descent count is identically one and has zero covariance with \(F\).

## Verification

Run `python3 verify.py` from the directory containing this document and the verifier. The standalone Python-standard-library script exhaustively enumerates permutations through \(n=8\), weights each by \(\theta^{c(\pi)}\), and compares the resulting exact rational covariances with every matrix entry, the ordinary-total formula and the cyclic-total formula at seven rational \(\theta\)-values. It reports **1,252 exact rational checks passed**. Enumeration checks finite instances and is not substituted for Steps 1–5, which establish the universal statements for all \(n\) and positive real \(\theta\).

## Relationship to prior work

Féray, *Asymptotic behavior of some statistics in Ewens random permutations*, arXiv:1201.2157 (first posted 2012-01-10), gives the general partial-permutation moment identity (Lemma 2.11) and asymptotic results for permutation patterns, including descents. The moment identity underlies Step 2 and implies that finite covariances can be calculated by sums, but its inspected statements do not provide the present indexed sign classification or the cyclic boundary transition.

Reutenauer's 1989/1990 precursor to Gessel–Reutenauer (1993), and Gessel–Zhuang (arXiv:2001.00654, 2020), give strong joint enumeration of cycle type, fixed-point **counts**, and ordinary descent sets/counts. In particular they encompass finite aggregate ordinary-descent moments in principle; such count-level results do not retain the positions \(j\) of fixed points, and the extra last-to-first comparison is not an ordinary descent-set statistic. The aggregate ordinary formula here is therefore a consistency consequence, not an independent claim of novelty.

A published uniform-permutation result entitled *Boundary localization of fixed-point–descent dependence in a uniform permutation* gives the \(\theta=1\) bidiagonal covariance pattern and cyclic cancellation. That case is an explicit antecedent, not a new contribution of this finding. What is assessed here is the all-\(\theta\) matrix, the emergence of a nonzero long-range background for \(\theta\ne1\), and the opposite signs of cyclic covariance on either side of \(\theta=1\).

## Limitations

The statement concerns covariance and pairwise indicator independence at the special parameter \(\theta=1\), not independence of the total fixed-point and cyclic-descent counts. It does not identify higher joint cumulants, or extend directly to arbitrary cycle-weighted permutations. Generic joint-moment and symmetric-function formulas provide substantial antecedent machinery and may admit equivalent specializations not detected in the inspected literature. The published uniform indexed result was available as a searchable summary; full-text comparison was unavailable, and it is treated as covering the uniform specialization. The claimed priority of the \(\theta\ne1\) structural phase is provisional pending independent literature review.

## References

1. V. Féray, *Asymptotic behavior of some statistics in Ewens random permutations*, arXiv:1201.2157v1 (2012-01-10); *Electronic Journal of Probability* **18** (2013), no. 76. https://arxiv.org/html/1201.2157v5
2. C. Reutenauer, *Number of permutations with given descent set and cycle structure*, *Séminaire Lotharingien de Combinatoire* B21h (1989), precursor to the Gessel–Reutenauer article. https://www.mat.univie.ac.at/~slc/s/s21reut.html
3. I. M. Gessel and C. Reutenauer, *Counting permutations with given cycle structure and descent set*, *Journal of Combinatorial Theory, Series A* **64** (1993), 189–215. https://doi.org/10.1016/0097-3165(93)90095-p
4. I. M. Gessel and Y. Zhuang, *Plethystic formulas for permutation enumeration*, arXiv:2001.00654v1 (2020-01-02), *Advances in Mathematics* **375** (2020). https://arxiv.org/abs/2001.00654
5. *Boundary localization of fixed-point–descent dependence in a uniform permutation*, published research record (2026-10-04). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-boundary-localization-of-fixed-point-descent-dependence-in-a-uni--6e228e1e9495
