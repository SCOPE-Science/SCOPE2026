# A two-index thinning self-decomposability criterion for Bernoulli–Poisson–Lindley counts

## Finding

Consider the two-parameter Bernoulli–Poisson–Lindley (BPL) count distribution of Bakouch et al. (2023). **Theorem.** For every \(\theta>0\) and \(0<\alpha<1\), define
\[
q=\frac1{1+\theta},\qquad r=\frac1{2+\theta},\qquad b=\frac{\alpha}{1-\alpha}.
\]
The BPL count is self-decomposable under independent Bernoulli thinning at **every** retention parameter \(c\in(0,1)\) if and only if all three inequalities hold:
\[
\boxed{b\le q,\qquad
2q(1-q)-r(1-r)+b(1+b)\ge0,\qquad
2q^2(1-q)-r^2(1-r)-b^2(1+b)\ge0.}
\]
The last two inequalities are exactly the first two adjacent comparisons of the canonical compound-Poisson sequence; these two comparisons control all infinitely many later comparisons, including at equality boundaries.

The result produces **both creation and destruction** of thinning self-decomposability as the Bernoulli contribution is increased, without leaving the ordinary compound-Poisson regime. At the exact parameter \(\theta=1/10\), writing \(b=\alpha/(1-\alpha)\), the choices \(b=0,\ 1/10,\ 1/3\) yield, respectively, failure, success, and failure. The successful interior choice is \(\alpha=1/11\), while \(b=1/3\) corresponds to \(\alpha=1/4\). The first choice is the unmodified Poisson–Lindley endpoint, used only for comparison.

## Assumptions and scope

The Poisson–Lindley count \(L_\theta\) is supported on \(\mathbb N_0\), with
\[
\Pr(L_\theta=k)=\frac{\theta^2(k+\theta+2)}{(1+\theta)^{k+3}},\qquad k=0,1,2,\ldots.
\]
The independent Bernoulli summand \(B_\alpha\) has success probability \(\alpha\), and \(X=B_\alpha+L_\theta\). For a count \(Y\), \(c\circ Y\) denotes the sum of \(Y\) independent Bernoulli variables with success probability \(c\), independent of \(Y\). The assertion is that for each \(c\in(0,1)\), there exists an independent nonnegative integer innovation \(I_c\) such that \(X\stackrel d=c\circ X'+I_c\), where \(X'\stackrel d=X\). No assertion concerns ordinary real-variable self-decomposability, independence of innovations for different retention values, or uniqueness of an autoregressive transition construction.

## Proof

**1. Exact generating function and canonical coefficients.** Direct summation of the stated mass function, followed by independent Bernoulli convolution, gives the normalized probability-generating function
\[
P(z)=\frac{1+bz}{1+b}\frac{1-rz}{1-r}
       \left(\frac{1-q}{1-qz}\right)^2.
\]
This is also the BPL generating function in the original 2023 construction. Its formal logarithmic expansion at zero is
\[
\log P(z)=\log P(0)+\sum_{k=1}^\infty \nu_kz^k,\qquad
\nu_k=\frac{2q^k-r^k+(-1)^{k+1}b^k}{k}.
\]
Write \(v_k=k\nu_k\). For a nondegenerate nonnegative-integer law with positive mass at zero, additive infinite divisibility is equivalent to nonnegative summable logarithmic jump intensities. The Steutel–van Harn discrete self-decomposability criterion further requires and is equivalent to the canonical sequence \((v_k)_{k\ge1}\) being nonincreasing.

**2. The exact compound-Poisson boundary.** If \(b>q\), then \(v_{2j}=2q^{2j}-r^{2j}-b^{2j}<0\) for all sufficiently large \(j\), so no infinite divisibility or thinning self-decomposability is possible. If \(b\le q\), then every odd coefficient is positive, while every even coefficient satisfies
\[
v_{2j}=2q^{2j}-r^{2j}-b^{2j}\ge q^{2j}-r^{2j}>0
\]
because \(0<r<q<1\). Also \(\sum_k\nu_k<\infty\). Thus \(b\le q\) is exactly the ordinary compound-Poisson domain, and it remains to decide whether \((v_k)\) decreases.

**3. All-index reduction to two comparisons.** Set \(A=2(1-q)>0\), \(U=1-r>0\), \(V=1+b>0\), \(R=r/q\in(0,1)\), and \(T=b/q\in(0,1]\). For an even index \(k\ge2\),
\[
\frac{v_k-v_{k+1}}{q^k}=A-UR^k-VT^k.
\]
The right-hand side is nondecreasing as \(k\) increases. Therefore \(v_2\ge v_3\) is necessary and sufficient for **all** even-index differences to be nonnegative.

For an odd index \(k\ge3\),
\[
\frac{v_k-v_{k+1}}{q^k}=A-UR^k+VT^k
>A-UR^2\ge VT^2\ge0,
\]
where the first strict inequality uses \(R<1\), and the second uses the even-index condition at \(k=2\). Therefore all odd-index comparisons beyond the first hold strictly whenever the second comparison holds. Finally,
\[
\begin{aligned}
v_1-v_2&=2q(1-q)-r(1-r)+b(1+b),\\
v_2-v_3&=2q^2(1-q)-r^2(1-r)-b^2(1+b).
\end{aligned}
\]
These are exactly the two displayed finite tests. Their necessity is immediate; their sufficiency follows from the preceding even- and odd-index arguments. This proves the if-and-only-if classification for every admissible parameter pair, with weak inequalities at genuine boundary points.

**4. Explicit background-driving batch law.** Whenever the tests hold, the positive constant \(v_1=2q-r+b\) and the nonnegative differences \(d_k=v_k-v_{k+1}\) define a probability law
\[
\Pr(J=k)=\frac{d_k}{v_1},\qquad k\ge1,
\]
since \(v_k\to0\) and \(\sum_{k\ge1}d_k=v_1\). Equivalently,
\[
\mathbb E[z^J]=\frac z{v_1}\left[
\frac{2q(1-q)}{1-qz}-\frac{r(1-r)}{1-rz}
+\frac{b(1+b)}{1+bz}\right]
\]
(the last expression is expanded as a formal power series at zero; its coefficients are nonnegative on the established domain). A continuous-time count process with per-capita deaths at unit rate and independent batches of size \(J\) arriving at Poisson rate \(v_1\) has this BPL law as its stationary distribution. Indeed,
\[
(1-z)\frac{P'(z)}{P(z)}
=v_1-\sum_{k\ge1}d_kz^k
=v_1\bigl(1-\mathbb E[z^J]\bigr),
\]
which is precisely the stationary immigration–death generating-function balance equation. It also supplies a constructive account of the thinning property.

**5. Exact reentrant example.** At \(\theta=1/10\), \(q=10/11\) and \(r=10/21\). The first two canonical differences are, respectively:
\[
\begin{array}{c|cc}
b & v_1-v_2 & v_2-v_3\\\hline
0 & -4490/53361 & 388100/12326391\\
1/10 & 137971/5336100 & 252509699/12326391000\\
1/3 & 19226/53361 & -479344/4108797
\end{array}
\]
All three have \(b\le q\) and hence are compound Poisson. The exact signs prove failure, success, failure of thinning self-decomposability in that order. As a function of \(b\) at fixed \(\theta\), the first finite condition improves strictly and the second deteriorates strictly; thus the successful set is an interval (possibly empty or including one endpoint), not a reentrant sequence with more than two crossings.

## Verification

The standalone `checker.py` uses only exact rational arithmetic. It independently matches the original convolution probabilities with coefficients extracted from the factored generating function, checks the sign criterion against sixty consecutive canonical differences across 648 rational parameter cases, and reproduces all six fractions in the example. These are finite consistency checks, not a proof of the quantified infinite-index statement. The proof above supplies that all-index step analytically via the monotone exponential comparisons and the classical canonical criterion.

## Relationship to prior work

Bakouch et al. (2023) introduced the BPL model and derived its probability mass function, generating function, mode, moments, hazard, dispersion and regression. Those formulas and the model itself are prior work; the present contribution is a global exact characterization of **Bernoulli-thinning self-decomposability** and the finite two-comparison certificate. Steutel and van Harn (1979) established the general equivalence between thinning self-decomposability and a nonincreasing canonical sequence; the new work does not reprove or claim that general characterization. Applying it here requires a model-specific all-index reduction, which is proved above.

The weaker *ordinary additive infinite-divisibility* criterion \(b\le q\), which follows from the displayed logarithmic coefficients, does not imply the present result. In particular, every choice in the exact reentrant example is compound Poisson, but only the intermediate one is thinning self-decomposable. Bakouch (2018) studied a *weighted negative-binomial Lindley* family with generating function of the form \((1+\gamma z)/(1-pz)^{\beta+1}\), which is not the present two-pole-zero BPL function. Its different distributional assertions do not establish these three BPL parameter inequalities. Searches for the aliases “Bernoulli–Poisson–Lindley self-decomposability,” “thinning,” and “canonical coefficients” did not identify a model-specific classification in the inspected literature; absence of hits is not a proof of historical novelty.

## Limitations

The theorem concerns a particular two-parameter marginal law and its Bernoulli-thinning representation. It does not show that any specific published count autoregression has this law as stationary marginal without specifying compatible innovations; the batch-immigration construction is one explicit possibility. No numeric global cutoffs in \(\theta\) or uniqueness of such cutoffs are asserted. Historical priority may be affected by uncatalogued work; independent mathematical validation and independent literature priority review have not been performed. The tests permit equality, so strict inequalities are not claimed on the parameter boundary.

## References

1. Bakouch, H. S., Chesneau, C., Maya, R., Irshad, M. R., Aswathy, S., and Qarmalah, N. (2023). *A Flexible Dispersed Count Model Based on Bernoulli Poisson–Lindley Convolution and Its Regression Model*. Axioms 12(9), 813. First published 2023-08-24. https://doi.org/10.3390/axioms12090813 . Full text: https://www.mdpi.com/2075-1680/12/9/813 .
2. Steutel, F. W., and van Harn, K. (1979). *Discrete analogues of self-decomposability and stability*. Annals of Probability 7, 893–899, Theorem 2.2. https://pure.tue.nl/ws/files/1956807/Metis199408.pdf .
3. Bakouch, H. S. (2018). *A weighted negative binomial Lindley distribution with applications to dispersed data*. Anais da Academia Brasileira de Ciências 90(3), 2617–2642. https://doi.org/10.1590/0001-3765201820170733 .
