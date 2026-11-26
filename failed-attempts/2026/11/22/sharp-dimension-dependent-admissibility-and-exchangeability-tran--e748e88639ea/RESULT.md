# Sharp dimension-dependent admissibility and exchangeability transition for generalized ratio-polynomial copulas

## Finding

Fix an integer \(n\ge 2\). Consider the generalized ratio-polynomial expression
\[
C_{n,\alpha}(u_1,\ldots,u_n)
=\left(\prod_{i=1}^n u_i\right)
\frac{(1+\alpha)^{n-1}\left(1+\alpha\prod_{i=1}^n u_i\right)}{\prod_{i=1}^n(1+\alpha u_i)},\qquad 0\le u_i\le1.
\]
There is exactly one \(s_n\) in \((0,2/(n+1))\) such that
\[
s_n(2-s_n)^n=1.
\]
**The expression is a copula on the entire cube if and only if \(\alpha\ge-s_n\).** In particular, the precise negative-parameter interval is strictly larger than the previously established sufficient interval \([-2^{-n},0)\). The endpoints begin with
\[
s_2=\frac{3-\sqrt5}{2}=0.381966011250105\ldots,\qquad
s_3=0.160713244785838\ldots,\qquad
s_4=0.0724380245170747\ldots.
\]
The sequence \(s_n\) decreases strictly and obeys the sharp dimension expansion
\[
s_n=2^{-n}+\frac n2\,4^{-n}+O(n^2 8^{-n})\quad(n\to\infty).
\]
For a fixed negative \(\alpha=-s\) with \(0<s\le s_2\), the formula defines copulas in precisely the integer dimensions
\[
2\le n\le N(s):=\left\lfloor\frac{\log(1/s)}{\log(2-s)}\right\rfloor.
\]
These are exact cutoffs **for this specified ratio formula**, not asserted upper bounds for all possible finite exchangeable extensions of its bivariate margin.

There is also an exact infinite-exchangeability dichotomy. For \(\alpha\ge0\), all dimensions are jointly consistent and admit a single binary latent-factor construction (a mixture of two conditional i.i.d. product laws). For \(-s_2\le\alpha<0\), the bivariate copula has strictly negative covariance and **no infinite exchangeable extension of any form**, even though the displayed finite-dimensional formula remains valid through dimension \(N(-\alpha)\).

## Assumptions and scope

An \(n\)-copula means a grounded, \(n\)-increasing continuous distribution function on \([0,1]^n\) with uniform one-dimensional margins. No boundary-supported singular measure is added to the displayed formula. The parameter \(\alpha\) is real, \(n\) is any integer at least two, and the formula is interpreted by its ordinary continuous rational extension at boundary coordinates whenever such an extension exists. The first publicly verified source for this family was published on 29 March 2023.

## Proof

**1. Domain and normalized margins.** For \(\alpha>-1\), every denominator is positive on the cube. The function is smooth and grounded. Setting all coordinates except \(u_j\) to one gives exactly \(u_j\), and setting any coordinate to zero gives zero. More generally,
\[
C_{n,\alpha}(u_1,\ldots,u_k,1,\ldots,1)=C_{k,\alpha}(u_1,\ldots,u_k)
\]
for \(2\le k<n\). A continuous grounded function with these margins is an \(n\)-copula exactly when its full mixed derivative is everywhere nonnegative. This follows by integration of the continuous mixed derivative over arbitrary axis-aligned boxes; conversely an interior strictly negative derivative forces a box of negative probability. At \(\alpha=-1\), the formula tends to zero at every interior cube point, contradicting the required uniform margins under continuity. At \(\alpha<-1\), the denominator vanishes at an interior coordinate \(u_i=-1/\alpha\), with a noncancelling numerator for generic other coordinates, so no continuous copula is defined. Thus it remains to analyze \(\alpha>-1\).

**2. Exact mixed density and its minimum.** Differentiation yields the identity
\[
c_{n,\alpha}(\mathbf u)=(1+\alpha)^{n-1}
\frac{1+\alpha\prod_{i=1}^n u_i(2+\alpha u_i)}{\prod_{i=1}^n(1+\alpha u_i)^2}.
\]
For \(\alpha\ge0\), all factors in the numerator are nonnegative and the leading \(1\) proves strict positivity. For \(-1<\alpha<0\), define \(A_\alpha(u)=u(2+\alpha u)\). On \([0,1]\),
\[
A_\alpha(0)=0,\qquad A_\alpha(1)=2+\alpha>1,
\qquad A_\alpha'(u)=2+2\alpha u>0.
\]
Consequently \(\prod_i A_\alpha(u_i)\) has maximum \((2+\alpha)^n\), attained only at the all-one corner. Since \(\alpha<0\), the density is nonnegative on the entire cube **if and only if**
\[
1+\alpha(2+\alpha)^n\ge0.
\]
If this inequality fails, the continuous density is strictly negative in a nonempty box immediately inside the all-one corner, proving necessity for an actual copula, not merely for positivity at a single boundary point.

**3. A unique sharp boundary.** Put \(s=-\alpha\in(0,1)\) and \(q_n(s)=s(2-s)^n\). Direct differentiation gives
\[
q_n'(s)=(2-s)^{n-1}(2-(n+1)s).
\]
Thus \(q_n\) rises from zero to a single maximum at \(2/(n+1)\), then falls to \(q_n(1)=1\). Because \(n\ge2\), \(q_n'(1)<0\), so the maximum is strictly larger than one. Hence \(q_n(s)=1\) has precisely one root \(s_n\) strictly between zero and \(2/(n+1)\) and its other endpoint root is \(s=1\), which is outside the permitted open interval. Therefore \(q_n(s)\le1\) on \(0<s<1\) exactly when \(s\le s_n\). This proves the copula classification and inclusion of equality. Moreover, with \(t=2^{-n}\), \(q_n(t)=(1-t/2)^n<1\), so \(s_n>2^{-n}\).

For each \(s\in(0,1)\), the factor \(2-s>1\), so the inequality \(s(2-s)^n\le1\) is equivalent to \(n\le\log(1/s)/\log(2-s)\). It also proves that \(s_n\) strictly decreases with \(n\). For the expansion, the equation is \(s_n=t(1-s_n/2)^{-n}\). For all sufficiently large \(n\), \(q_n(2t)=2(1-t)^n>1\), so \(t<s_n<2t\). Hence \(ns_n\to0\), and the uniform binomial/Taylor expansion yields
\[
s_n=t\left(1+\frac n2s_n+O(n^2s_n^2)\right)
=t+\frac n2t^2+O(n^2t^3).
\]
All constants in the asymptotic remainder can be made absolute for sufficiently large \(n\).

**4. Exact positive-parameter latent representation.** When \(\alpha\ge0\), let
\[
H_0(u)=\frac{(1+\alpha)u}{1+\alpha u},\qquad
H_1(u)=\frac{(1+\alpha)u^2}{1+\alpha u}.
\]
Both are distribution functions on \([0,1]\), because \(H_j(0)=0\), \(H_j(1)=1\), and
\[
H_0'(u)=\frac{1+\alpha}{(1+\alpha u)^2}\ge0,\qquad
H_1'(u)=\frac{(1+\alpha)u(2+\alpha u)}{(1+\alpha u)^2}\ge0.
\]
The exact factorization is
\[
C_{n,\alpha}(\mathbf u)
=\frac1{1+\alpha}\prod_{i=1}^n H_0(u_i)
+\frac\alpha{1+\alpha}\prod_{i=1}^n H_1(u_i).
\]
Therefore draw one common Bernoulli latent state \(J\), with probability \(1/(1+\alpha)\) of state zero, and then conditionally sample all coordinates i.i.d. with CDF \(H_J\). Every coordinate has unconditional CDF \([H_0+\alpha H_1]/(1+\alpha)=u\); the joint CDF in every dimension is the displayed \(C_{n,\alpha}\). This is a concrete, infinitely extendible exchangeable construction; at \(\alpha=0\) it reduces to independence.

**5. Why the negative phase has no infinite exchangeable extension.** For the two-dimensional member, direct algebra gives
\[
C_{2,\alpha}(u,v)-uv
=\alpha F_\alpha(u)F_\alpha(v),\qquad
F_\alpha(u)=\frac{u(1-u)}{1+\alpha u}.
\]
For \(-s_2\le\alpha<0\), \(F_\alpha\) is strictly positive on \((0,1)\). Hoeffding's covariance identity therefore gives
\[
\operatorname{Cov}(U_1,U_2)
=\alpha\left(\int_0^1F_\alpha(u)\,du\right)^2<0.
\]
If an infinite exchangeable uniform sequence had this two-variable margin, every pair would have this same covariance \(c<0\). But
\[
0\le\operatorname{Var}\left(\sum_{i=1}^m U_i\right)
=\frac m{12}+m(m-1)c
\]
would be negative for all sufficiently large \(m\), a contradiction. This says nothing about whether *alternative* exchangeable joint distributions may extend the given bivariate margin to some finite dimensions exceeding the GRP cutoff.

## Verification

A standalone Python checker, `check_grpcopula.py`, confirms symbolic mixed-derivative and two-component factorization identities in dimensions two through four, exact rational cutoff examples, exact marginal normalizations, numerical algebraic root calculations, and covariance signs. In its recorded execution it passed 51 assertions. The assertions on finitely many dimensions and numerical roots are diagnostics: the quantifiers over all integers and the exact parameter boundary are proved in Sections 2–5 above. Run `python check_grpcopula.py` with Python 3, SymPy and mpmath; see `check_output.txt` for the recorded run.

For the concrete rational example \(\alpha=-1/8\), the density criterion holds at \(n=3\), since \((1/8)(15/8)^3=3375/4096<1\), but fails at \(n=4\), since \((1/8)(15/8)^4=50625/32768>1\). Thus the same negatively dependent bivariate marginal belongs to this GRP family at dimension three but not dimension four.

## Relationship to prior work

Chesneau's 2023 open-access article introduced this ratio-polynomial copula and its multivariate generalization in Proposition 6, including the displayed mixed-density formula; it proved the **sufficient** range \(\alpha\ge-2^{-n}\). The density formula, the family itself, its exchangeability and consistent finite margins, and all results inside the author's restricted parameter range are prior work. The present result takes the *same* explicitly published density as its starting point and establishes the complete real-parameter admissibility criterion, exact maximum GRP dimension for any negative parameter, and a constructive all-dimension binary-mixture representation for the nonnegative phase. No claim of inventing the copula or the density formula is made.

Rodríguez-Lallena and Úbeda-Flores established general bivariate separable perturbation criteria; indeed the two-dimensional member belongs to that broad family with a parameter-dependent perturbing function. Dolati and Úbeda-Flores described generic multivariate FGM-type perturbations, some with independent proper margins and some with additional interaction terms. Those general criteria provide background rather than a stated optimization for this specific rational \(n\)-variate formula. Chesneau's later 2023 *Symmetry* article studies a different, principally bivariate ratio scheme; it does not state the GRP cutoffs. The exact numerical boundaries and comparison with the published sufficient interval should not be interpreted as a proof of absolute historical priority.

## Limitations

The result concerns the exact rational GRP construction, not every possible \(n\)-copula with the same pairwise margins. The finite cutoff \(N(s)\) therefore need not equal the maximum dimension of an arbitrary exchangeable extension. The positive-phase binary mixture is one explicit representation, not a claimed unique de Finetti mixing law. The all-dimension impossibility on the negative side follows only for *infinite exchangeability*, not for finite extensions. Published generic separable-copula criteria and possible unindexed further studies leave residual historical-priority uncertainty. Independent verification by a separate mathematical reviewer has not been performed.

## References

1. C. Chesneau, *Theoretical Advancements on a Few New Dependence Models Based on Copulas with an Original Ratio Form*, **Modelling** 4 (2023), 102–132, Proposition 1 and Proposition 6, published 29 March 2023. https://doi.org/10.3390/modelling4020008
2. J. A. Rodríguez-Lallena and M. Úbeda-Flores, *A new class of bivariate copulas*, **Statistics & Probability Letters** 66 (2004), 315–325. https://doi.org/10.1016/j.spl.2003.09.010
3. A. Dolati and M. Úbeda-Flores, *Some new parametric families of multivariate copulas*, **International Mathematical Forum** 1 (2006), 17–25. https://www.m-hikari.com/imf-password/1-4-2006/ubeda-floresIMF1-4-2006.pdf
4. C. Chesneau, *A Collection of Two-Dimensional Copulas Based on an Original Parametric Ratio Scheme*, **Symmetry** 15 (2023), 977, published 25 April 2023. https://doi.org/10.3390/sym15050977
