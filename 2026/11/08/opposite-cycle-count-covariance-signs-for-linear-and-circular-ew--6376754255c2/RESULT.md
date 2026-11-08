# Opposite cycle-count covariance signs for linear and circular Ewens successions

## Finding
For each integer \(n\ge3\) and parameter \(\theta>0\), let \(\Pi\) be a random permutation of \(\{1,\ldots,n\}\) with the Ewens probability \(\Pr_\theta(\Pi=\pi)=\theta^{K(\pi)}/\theta^{\overline n}\), where \(K(\pi)\) counts cycles and \(\theta^{\overline n}=\prod_{j=0}^{n-1}(\theta+j)\). Let
\[
L=\sum_{i=1}^{n-1}\mathbf1\{\Pi(i+1)=\Pi(i)+1\},\qquad
R=\sum_{i=1}^{n}\mathbf1\{\Pi(i+1\bmod n)=\Pi(i)+1\bmod n\},
\]
where modular arithmetic uses residues \(\{1,\ldots,n\}\). These are retained *oriented* adjacencies in a linear and a circular arrangement.

Put \(a=n-2\), \(D=(\theta+a)(\theta+a+1)\), and
\[
P_L=(2a+1)\theta^2+2a^2\theta-a(2a+1),\quad
P_R=(2a+1)\theta^2+2(a^2-1)\theta-(a+1)(2a+1).
\]
Then the following identities hold for every admissible \(n\) and \(\theta\):
\[
\mathbb E_\theta L=\frac{(n-1)(\theta^2+n-2)}{D},\qquad
\mathbb E_\theta R=\frac{n(\theta^2+n-1)}{D},
\]
\[
\operatorname{Cov}_\theta(K,L)=\frac{\theta(n-1)P_L}{D^2},\qquad
\operatorname{Cov}_\theta(K,R)=\frac{\theta nP_R}{D^2}.
\]
Each covariance switches sign exactly once as \(\theta\) increases. If \(\tau_L\) and \(\tau_R\) are the unique positive roots of \(P_L\) and \(P_R\), respectively, then
\[
0<\tau_L<1<\tau_R,
\]
and throughout the nonempty interval \(\tau_L<\theta<\tau_R\), **linear** successions are positively correlated with cycle count, while **circular** successions are negatively correlated with cycle count. At the uniform point \(\theta=1\), the covariances have the opposite exact signs
\[
\operatorname{Cov}_1(K,L)=\frac1{n^2},\qquad
\operatorname{Cov}_1(K,R)=-\frac1{(n-1)^2}.
\]
In particular the one additional wraparound site reverses the covariance sign. The two thresholds approach one from opposite sides:
\[
\tau_L=1-\frac1{2(n-2)}+O(n^{-2}),\qquad
\tau_R=1+\frac1{2(n-2)}+O(n^{-2}).
\]

## Assumptions and scope
The result is exact for all integers \(n\ge3\) and all real parameters \(\theta>0\), with no asymptotic assumptions for the identities or sign ordering. A circular succession wraps both the source index and the image label modulo \(n\). A linear succession wraps neither. The cycle count \(K\) is that of the original mapping \(\Pi\), not of a transformation obtained by erasing cycle parentheses. Primary classification: MSC2020 60C05.

## Proof
**Weighted partial-injection contraction.** Suppose \(m\) prescribed arrows of a permutation have distinct sources and distinct destinations and, among those arrows, \(c\) closed directed cycles are already completed. Then the total Ewens weight of all permutation completions is \(\theta^c\theta^{\overline{n-m}}\). Indeed, delete the \(c\) closed cycles and contract the remaining directed paths of prescribed arrows; the choices of how to join the \(n-m\) remaining open paths/isolated vertices form a bijection with permutations of \(n-m\) labeled objects, with the number of eventual cycles equal to \(c\) plus the number of cycles in the contracted permutation. This includes the case of fixed loops as prescribed arrows.

Fix a source site \(i\) in a line, so the event \(\Pi(i+1)=\Pi(i)+1\) requires the two arrows \(i\mapsto b\) and \(i+1\mapsto b+1\) for some \(b\in\{1,\ldots,n-1\}\). When \(b=i\), both arrows are loops and have contraction weight \(\theta^2\theta^{\overline{n-2}}\). For each of the other \(n-2\) choices of \(b\), the prescribed arrows have no closed cycle and contribute \(\theta^{\overline{n-2}}\). Therefore every linear site has probability \((\theta^2+n-2)/D\), proving the formula for \(\mathbb E_\theta L\).

For a circular site the possible image value \(b\) runs over all \(n\) residues and the second arrow is \(i+1\bmod n\mapsto b+1\bmod n\). For \(n\ge3\), only \(b=i\) creates cycles (two loops); each of the other \(n-1\) choices creates no directed cycle. The same contraction gives circular-site probability \((\theta^2+n-1)/D\) and hence \(\mathbb E_\theta R\).

**Differentiation.** For any statistic \(X\) on the finite symmetric group, differentiating the exactly normalized Ewens weights gives
\[
\theta\frac{d}{d\theta}\mathbb E_\theta X=\operatorname{Cov}_\theta(K,X).
\]
The derivatives of the two rational expectations are the displayed covariance identities; the respective derivative numerators are precisely \(P_L\) and \(P_R\).

**Signs and uniqueness.** A unified polynomial is
\[
P_b(\theta)=(2a+1)\theta^2+2[a(a+1)-b]\theta-(2a+1)b,
\]
with \(b=a\) for the line and \(b=a+1\) for the circle. Each has positive quadratic coefficient and negative constant coefficient, so exactly one root is positive, its sign being negative before the root and positive after it. Direct substitution shows \(P_L(1)=a+1>0\) and \(P_R(1)=-(a+2)<0\), proving \(\tau_L<1<\tau_R\). Substituting \(\theta=1\) in the covariance identities yields \(1/n^2\) and \(-1/(n-1)^2\) exactly. Finally, for \(b\in\{a,a+1\}\), the positive root is
\[
\tau_b=\frac{\sqrt{[a(a+1)-b]^2+(2a+1)^2b}-[a(a+1)-b]}{2a+1}.
\]
Expansion of this explicit root as \(a\to\infty\) yields \(\tau_a=1-(2a)^{-1}+O(a^{-2})\) and \(\tau_{a+1}=1+(2a)^{-1}+O(a^{-2})\), completing the proof.

## Verification
Run `python3 verify.py` in a directory containing the supplied standalone script. It enumerates every permutation for \(3\le n\le8\) at four rational parameter values, computes both statistics and their covariances exactly as rational numbers, and compares these with the analytic identities. It also checks the exact uniform-parameter covariance signs. These finite computations are independent checks, not a substitute for the proof of the universal statements.

## Relationship to prior work
The ordinary linear-succession statistic has been studied in the classical enumeration literature and by Diaconis, Evans and Graham, who show its equality in distribution with a set of fixed-point indicators for **uniform** permutations; they also analyze the circular statistic in that uniform setting. Reilly and Tanny enumerate unweighted line successions. Mansour and Shattuck enumerate *within-cycle* successions jointly with the number of cycles, explicitly distinguishing that statistic from one-line successions when joint statistics are involved. More recent work treats multi-statistic Eulerian enumerations. None of the inspected results explicitly gives the Ewens-weighted original-map cycle-covariance threshold pair or the opposite-sign interval. The new assertion is the simultaneous sharp \(\theta\)-dependent phase classification, not the previously known marginal uniform-succession laws or general Ewens weighting formula.

## Limitations
No claim of statistical detectability at large \(n\) is made: the covariance magnitudes at \(\theta=1\) are of order \(n^{-2}\), and the mixed-sign interval shrinks to \(\theta=1\). The theorem concerns only the specified two expectations and covariances, not a full joint law or stochastic ordering. An implicit earlier deduction from general multivariate enumerators cannot be completely excluded; detailed manuscript-priority comparison remains appropriate.

## References
- P. Diaconis, S. N. Evans and R. Graham, *Unseparated pairs and fixed points in random permutations*, arXiv:1308.5459 (first posted 2013-08-25); *Advances in Applied Mathematics* **61** (2014), 102–124. https://arxiv.org/abs/1308.5459
- J. W. Reilly and S. M. Tanny, *Counting Successions in Permutations*, *Studies in Applied Mathematics* **61** (1979), 73–81. https://doi.org/10.1002/sapm197961173
- T. Mansour and M. Shattuck, *Counting permutations by the number of successions within cycles*, *Discrete Mathematics* **339** (2016), 1368–1376. https://doi.org/10.1016/j.disc.2015.12.004
- S.-M. Ma, H. Qi, J. Yeh and Y.-N. Yeh, *On the joint distributions of succession and Eulerian statistics*, *Advances in Applied Mathematics* **162** (2025), 102772. https://doi.org/10.1016/j.aam.2024.102772
- W. J. Ewens, *The sampling theory of selectively neutral alleles*, *Theoretical Population Biology* **3** (1972), 87–112. https://doi.org/10.1016/0040-5809(72)90035-4
