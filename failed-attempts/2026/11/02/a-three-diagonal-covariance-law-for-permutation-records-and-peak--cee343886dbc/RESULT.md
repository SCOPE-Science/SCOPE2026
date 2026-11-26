# A three-diagonal covariance law for permutation records and peaks

## Finding

Let \(\pi\) be a uniform permutation of \(\{1,\ldots,n\}\), with \(n\ge3\). Let \(R_i\) indicate an upper record at position \(i\) and \(P_j\) indicate an interior peak at position \(j\). For all \(1\le i\le n\) and \(2\le j\le n-1\), the complete cross-covariance kernel is
\[
\operatorname{Cov}(R_i,P_j)=
\begin{cases}
\dfrac{2-j}{3(j-1)(j+1)},&i=j-1,\\[4pt]
\dfrac{2j-1}{3j(j+1)},&i=j,\\[4pt]
-\dfrac1{3(j+1)},&i=j+1,\\[4pt]
0,&\lvert i-j\rvert\ge2.
\end{cases}
\]
For \(R=\sum_{i=1}^nR_i\) and \(P=\sum_{j=2}^{n-1}P_j\), each peak contributes strictly positively to their overall covariance:
\[
\operatorname{Cov}(R,P_j)=\frac1{3j(j-1)(j+1)}>0,
\]
and the aggregate covariance satisfies the exact finite-size and limiting laws
\[
\boxed{\operatorname{Cov}(R,P)=\frac{(n-2)(n+1)}{12n(n-1)}
=\frac1{12}-\frac1{6n(n-1)}\ \longrightarrow\ \frac1{12}.}
\]
For \(n\ge4\), the exact correlation is
\[
\operatorname{Corr}(R,P)=
\frac{(n-2)(n+1)}{12n(n-1)
\sqrt{(H_n-H_n^{(2)})\,2(n+1)/45}}
\sim\frac{\sqrt{45/2}}{12\sqrt{n\log n}},
\]
where \(H_n=\sum_{k=1}^n1/k\) and \(H_n^{(2)}=\sum_{k=1}^n1/k^2\). Thus the covariance stays positive and bounded away from zero while correlation vanishes.

## Assumptions and scope

Use the one-line permutation convention and define, for \(1\le i\le n\),
\[
R_i=\mathbf1\{\pi_i>\max(\pi_1,\ldots,\pi_{i-1})\},\qquad R_1=1.
\]
For \(2\le j\le n-1\), set \(P_j=\mathbf1\{\pi_{j-1}<\pi_j>\pi_{j+1}\}\). There is no peak indicator at an endpoint. All probabilities and covariances are under the uniform law on \(S_n\), and the assertions are exact for integer \(n\ge3\). The correlation identity requires \(n\ge4\), since the displayed peak-count variance expression starts at that size. Sampling independent continuous identically distributed observations and recording only their relative ranks gives the identical result.

## Proof

**Locality.** Realize the permutation as ranks of independent continuous uniform variables \(U_1,\ldots,U_n\). An upper record event at \(i\) depends on the first \(i\) variables; a peak at \(j\) depends only on \(U_{j-1},U_j,U_{j+1}\). If \(i\le j-2\), the sets of variables are disjoint and the events are independent. If \(i\ge j+2\), the record event is independent of the relative ranking of the first \(i-1\) entries: the insertion rank of \(U_i\) into those entries is uniform and independent of their internal order. The peak event is measurable with respect to that internal order. Thus the covariance vanishes off the three indicated diagonals.

**Local mixed moments.** Symmetry gives \(\Pr(R_i=1)=1/i\) and \(\Pr(P_j=1)=1/3\). If \(R_{j+1}=1\), a peak at \(j\) is impossible, so \(\Pr(R_{j+1}=P_j=1)=0\). Conditional on \(R_j=1\), \(U_j\) has density \(ju^{j-1}\) and \(\Pr(U_{j+1}<U_j\mid R_j=1)=j/(j+1)\). Consequently \(\Pr(R_j=P_j=1)=1/(j+1)\). Conditional on \(R_{j-1}=1\), \(U_{j-1}\) has density \((j-1)u^{j-2}\); for fixed \(u=U_{j-1}\), the event \(U_j>u\) and \(U_j>U_{j+1}\) has probability \((1-u^2)/2\). Integration therefore gives
\[
\Pr(R_{j-1}=P_j=1)
=\frac1{j-1}\cdot\frac12\left(1-\frac{j-1}{j+1}\right)
=\frac1{(j-1)(j+1)}.
\]
Subtracting \(\Pr(R_i=1)\Pr(P_j=1)=1/(3i)\) in these three cases proves the full kernel.

**Aggregate cancellation.** Summing the three neighboring covariances for a fixed \(j\) gives
\[
\frac{2-j}{3(j-1)(j+1)}+\frac{2j-1}{3j(j+1)}-\frac1{3(j+1)}
=\frac1{3j(j-1)(j+1)}.
\]
The exact partial fractions
\[
\frac1{3j(j-1)(j+1)}
=\frac1{6(j-1)}-\frac1{3j}+\frac1{6(j+1)}
\]
telescope from \(j=2\) to \(n-1\), yielding \((n-2)(n+1)/(12n(n-1))\), hence its positive limit.

**Variances and correlation.** The upper-record indicators are independent Bernoulli variables of means \(1/i\) (the initial insertion ranks are mutually independent). Thus \(\operatorname{Var}(R)=H_n-H_n^{(2)}\). Peak indicators are two-dependent, with individual variance \(2/9\), immediate-neighbor covariance \(-1/9\), and two-step covariance \(1/45\). The last assertion follows because the five ranks in an alternating word of form up-down-up-down have \(16\) admissible permutations, so the joint peak probability is \(16/120=2/15\). For all \(n\ge4\), summing these covariances gives
\[
\operatorname{Var}(P)=(n-2)\frac29-2(n-3)\frac19+2(n-4)\frac1{45}=\frac{2(n+1)}{45}.
\]
For \(n=3\), \(P=P_2\) has variance \(2/9\), and the covariance law still holds. Substituting the two variances gives the exact correlation and its asymptotic, since \(H_n-H_n^{(2)}\sim\log n\).

## Verification

The accompanying Python 3 script `verify.py` enumerates all \(46{,}230\) permutations with \(3\le n\le8\) and computes exact rational joint moments from integer counts. It passed \(150\) independent assertions of the local covariance kernel, the total covariance, the record variance, and (where applicable) the peak variance. Reproduce by running `python3 verify.py` in the same directory. The all-size proof above is analytic; the finite enumeration is a cross-check, not a substitute for the proof.

## Relationship to prior work

Gnedin's paper on record statistics ([1]) develops the independent initial-rank representation and record-dependent permutation laws, not the local interior-peak cross-covariance matrix. Kasraoui's peak-set paper ([2]) studies the most frequent peak sets, not record–peak mixed moments. Baril and Petrossian ([3]) enumerate equivalence classes based separately on descents and left-to-right maxima; their statements do not jointly encode the local record and peak indicators. Warren and Seneta ([4]) establish peak-count distribution theory and moments. The present finite-size banded cross-kernel and its limiting covariance are not stated by the inspected portions of those works.

## Limitations

The result assumes uniformly random permutations, equivalently an iid continuous sample without ties. It does not assert distributional independence of the record and peak totals; indeed their covariance is positive. The coefficient of the asymptotic correlation pertains only to that model. Earlier equivalent combinatorial derivations remain possible, particularly within historical joint-enumeration literature. Source [4] was accessible through its publisher abstract and bibliographic references but not as full text; therefore its complete results were not used for any definitive exclusion claim. These scientific priority limitations do not affect the internal exact proof.

## References

[1] A. Gnedin, *Coherent random permutations with record statistics*, first public arXiv version 17 November 2006, arXiv:math/0611538v1, https://arxiv.org/abs/math/0611538.

[2] A. Kasraoui, *The most frequent peak set of a random permutation*, first public arXiv version 22 October 2012, arXiv:1210.5869v1, https://arxiv.org/abs/1210.5869.

[3] J.-L. Baril and A. Petrossian, *Equivalence classes of permutations modulo descents and left-to-right maxima*, Pure Mathematics and Applications 25 (2015), 19–29, DOI:10.1515/puma-2015-0002, https://doi.org/10.1515/puma-2015-0002.

[4] D. Warren and E. Seneta, *Peaks and Eulerian numbers in a random sequence*, Journal of Applied Probability 33 (1996), 101–114, DOI:10.2307/3215267, https://doi.org/10.2307/3215267.
