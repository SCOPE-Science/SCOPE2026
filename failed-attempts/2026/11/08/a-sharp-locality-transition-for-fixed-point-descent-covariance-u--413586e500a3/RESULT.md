# A sharp locality transition for fixed-point–descent covariance under the Ewens law

## Finding

Let \(n\ge 3\), \(\theta>0\), and draw \(\pi\) from the Ewens distribution on the symmetric group \(S_n\), with mass proportional to \(\theta^{\#\mathrm{cycles}(\pi)}\). Write \(F_i=\mathbf 1\{\pi(i)=i\}\) and \(B_j=\mathbf 1\{\pi(j)>\pi(j+1)\}\) for \(1\le i\le n\) and \(1\le j\le n-1\). Define

\[
q_n=\frac{\theta}{\theta+n-1},\qquad
p_n=\frac{(n-1)(n+2\theta-2)}{2(\theta+n-1)(\theta+n-2)}.
\]

Then \(\mathbb E F_i=q_n\) and \(\mathbb E B_j=p_n\), and the entire mixed covariance matrix has entries

\[
\operatorname{Cov}(F_i,B_j)=q_n
\begin{cases}
\frac{i-1}{\theta+n-2}-p_n,&i=j,\\[3pt]
\frac{n-i}{\theta+n-2}-p_n,&i=j+1,\\[3pt]
p_{n-1}-p_n,&i\notin\{j,j+1\}.
\end{cases}
\tag{1}
\]

The last case equals the position-independent rational value

\[
h_{n,\theta}=-\frac{\theta^2(\theta-1)}{(\theta+n-3)(\theta+n-2)(\theta+n-1)^2}.
\tag{2}
\]

Consequently every off-incidence pair \((i,j)\) with \(i\notin\{j,j+1\}\) has strictly positive covariance for \(0<\theta<1\), zero covariance precisely for \(\theta=1\), and strictly negative covariance for \(\theta>1\). Thus the uniform law is the unique positive Ewens parameter at which the mixed covariance is supported only on the two positions touching the descent; every nonuniform parameter produces a dense, constant-sign off-incidence part.

Writing \(F=\sum_{i=1}^n F_i\) and \(D=\sum_{j=1}^{n-1} B_j\), summation gives

\[
\operatorname{Cov}(F,D)=-\frac{\theta^2(n-1)(n^2+2n\theta-4n-2\theta+2)}{(\theta+n-3)(\theta+n-2)(\theta+n-1)^2}.
\tag{3}
\]

This aggregate covariance is negative for all \(n\ge4\), while for \(n=3\) its sign is positive, zero, or negative according as \(\theta<1/4\), \(\theta=1/4\), or \(\theta>1/4\). In particular, formula (3) specializes to the previously known \(-1/n\) identity at \(\theta=1\); that specialization is **not** claimed as new.

## Assumptions and scope

The underlying permutation is the bijection \(\pi:\{1,\dots,n\}\to\{1,\dots,n\}\), written as its one-line values when forming descents. Its Ewens mass is

\[
\Pr_{n,\theta}(\pi)=\frac{\theta^{\#\mathrm{cycles}(\pi)}}{\theta(\theta+1)\cdots(\theta+n-1)}.
\]

All claims quantify over every integer \(n\ge3\), every real \(\theta>0\), and every permitted position pair. The indicators are not claimed to be independent when their covariance vanishes. The parameter \(\theta=0\) and the size \(n=2\) are outside the theorem's domain.

## Proof

**Forced-arrow enumeration.** Fix \(k\) compatible arrows \(a\mapsto b\) in a permutation (all specified tails distinct, all heads distinct), and suppose they complete \(c\) directed cycles. Each remaining path is contracted to one unit. There are \(n-k\) such units, with completed cycles contributing the factor \(\theta^c\). Every bijective completion of the remaining units contributes exactly the cycle weight of its contracted permutation, and the total weight of these completions equals \(\theta^c\theta(\theta+1)\cdots(\theta+n-k-1)\). Dividing by the normalizer gives the forced-arrow probability

\[
\Pr(\text{all prescribed arrows})=\frac{\theta^c}{(\theta+n-k)(\theta+n-k+1)\cdots(\theta+n-1)}.
\tag{4}
\]

In particular, the probability of a specified fixed point is \(q_n\); conditioned on this fixed point, the restriction to the other \(n-1\) labels is again Ewens with parameter \(\theta\).

**One descent.** For two adjacent input positions \(j\) and \(j+1\), there are \(\binom n2\) possible decreasing ordered image pairs. Under the two-arrow formula, the generic pair has weight \(1/((\theta+n-2)(\theta+n-1))\). Exactly \(n-1\) pairs have one completed cycle and therefore weight \(\theta\) times this generic weight. They are: \(\pi(j)=j\), with \(j-1\) admissible smaller second images; \(\pi(j+1)=j+1\), with \(n-j-1\) admissible larger first images; and the two-cycle \(\pi(j)=j+1,\ \pi(j+1)=j\). Hence

\[
\Pr(B_j=1)=\frac{\binom n2+(\theta-1)(n-1)}{(\theta+n-2)(\theta+n-1)}=p_n.
\]

**Condition on a specified fixed point.** If \(i\notin\{j,j+1\}\), deletion of fixed point \(i\) leaves two consecutive surviving *labels* at the queried positions, so the conditional descent probability is \(p_{n-1}\), independent of their absolute labels. If \(i=j\), the comparison becomes \(j>\pi(j+1)\). There are \(j-1\) possible smaller images, each with conditional probability \(1/(\theta+n-2)\). If \(i=j+1\), the comparison becomes \(\pi(j)>j+1\), with \(n-j-1=n-i\) possible larger images at the same conditional probability. Multiplication by \(q_n\) and subtraction of the product of means proves (1).

**Sign and aggregation.** Directly reducing \(q_n(p_{n-1}-p_n)\) to a common denominator yields (2). Its denominators are strictly positive since \(n\ge3\), \(\theta>0\). The factor \(\theta-1\) alone therefore controls every remote sign. Summing (1) over \(i\) and \(j\), followed by common-denominator simplification, gives (3). The polynomial in its numerator is \((n-2)^2-2+2(n-1)\theta\), strictly positive for \(n\ge4\) and equal to \(4\theta-1\) at \(n=3\). All sign assertions follow. At \(\theta=1\), (3) reduces to \(-1/n\) and (2) to zero.

## Verification

A standalone Python standard-library checker, `verify.py`, enumerates permutations for all \(3\le n\le7\), computing exact Ewens weights, mean descent indicators, each individual mixed covariance, and total covariance. It tests six integer parameters and four nonintegral rational parameters with `fractions.Fraction`. Further exact checks for \(3\le n\le39\) compare the sum of all entries with (3), and verify the remote sign and zero classifications. Running the embedded checker returns `VERIFY_OK 225302 exact assertions`. These finite checks supplement, but do not replace, the all-size argument above.

## Relationship to prior work

Kammoun (2018) analyzes limiting descent processes for conjugation-invariant permutations, including the Ewens model, but does not state this finite position-resolved fixed-point–descent covariance matrix. Kim and Lee (2018) study descents conditioned on a conjugacy class, not the location-indexed mixed Ewens matrix. Hultman (2013) provides class-averaged descent/inversion formulas, and Gessel and Zhuang (2020, §§6–7) provide powerful generating functions for cycle type, total fixed-point count, and descent statistics. The **aggregate** part of (3) is in principle accessible by existing enumerators and is not asserted independent of that literature. Those statistics do not label *which positions* are fixed: for example the permutations \((1,4,2,3)\) and \((2,3,1,4)\) have identical cycle type \((3,1)\) and descent set \(\{2\}\), but have fixed-point sets \(\{1\}\) and \(\{4\}\). Thus those aggregate enumerators do not by themselves imply the individual entries in (1).

An earlier public result, *Boundary localization of fixed-point–descent dependence in a uniform permutation* (2026), establishes the \(\theta=1\) case, including its negative total covariance. The present contribution is the complete positive-parameter sign/locality transition and exact nonuniform position-resolved matrix, not the uniform case.

## Limitations

The covariance calculation does not identify joint independence or furnish a central limit theorem. The formulas are elementary enough that an older implicit position-sensitive generating function or identity could subsume the claimed nonuniform matrix; bibliographic priority is not proved. The result is restricted to the Ewens family and ordinary adjacent descents, not arbitrary conjugation-invariant permutation laws or nonadjacent comparisons. Verification is a self-review, not an independent mathematical audit.

## References

- M. S. Kammoun, *Monotonous subsequences and the descent process of invariant random permutations*, arXiv:1805.05253v1 (public 2018-05-14), https://arxiv.org/abs/1805.05253.
- G. B. Kim and S. Lee, *Central limit theorem for descents in conjugacy classes of* \(S_n\), arXiv:1803.10457v1 (2018-03-28), https://arxiv.org/abs/1803.10457.
- A. Hultman, *Permutation statistics of products of random permutations*, arXiv:1301.0430v1 (2013), https://arxiv.org/abs/1301.0430.
- I. M. Gessel and Y. Zhuang, *Plethystic formulas for permutation enumeration*, arXiv:2001.00654v1 (public 2020-01-02), https://arxiv.org/abs/2001.00654.
- J. E. Paguyo, *Fixed points, descents, and inversions in parabolic double cosets of the symmetric group*, arXiv:2112.07728v1 (2021-12-14), https://arxiv.org/abs/2112.07728.
- *Boundary localization of fixed-point–descent dependence in a uniform permutation* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-boundary-localization-of-fixed-point-descent-dependence-in-a-uni--6e228e1e9495.
