# A sharp compound-Poisson boundary for Bernoulli–Poisson–Lindley counts

## Finding: first negative coefficient just beyond the boundary

Let \(\theta>0\) be fixed and let \(X=B+Y\), with independent \(B\sim\operatorname{Bernoulli}(\alpha)\) and Poisson–Lindley \(Y\) of mass
\[
\Pr(Y=j)=\frac{\theta^2(j+\theta+2)}{(1+\theta)^{j+3}},\qquad j\in\mathbb N_0,
\]
where \(0<\alpha<1\). Write \(q=(1+\theta)^{-1}\), \(r=(2+\theta)^{-1}\), and \(b=\alpha/(1-\alpha)\). The ordinary additive infinite-divisibility boundary \(b=q\) (equivalently \(\alpha=1/(\theta+2)\)) and the log-PGF coefficients are background facts also established in [2].

**Theorem.** For \(\alpha>1/(\theta+2)\), the first negative formal log-PGF coefficient occurs at a finite even index \(K(\alpha,\theta)\). As \(\alpha\downarrow1/(\theta+2)\) with \(\theta\) fixed,
\[
K(\alpha,\theta)\log(b/q)\longrightarrow\log 2.
\]
In particular, no fixed finite initial segment of logarithmic coefficients detects the failure of infinite divisibility for all parameters arbitrarily close to the boundary on the nondivisible side.

## Proof

The probability generating function \(G\) of \(X\) from [1, §3.2] satisfies
\[
\frac{G(s)}{G(0)}=\frac{(1+bs)(1-rs)}{(1-qs)^2},\qquad
\lambda_k:=[s^k]\log G(s)=\frac{2q^k-r^k+(-1)^{k+1}b^k}{k}.
\]
Here \(G(0)>0\); the series is taken at zero formally and makes sense whether or not \(b<1\). Since \(0<r<q<1\), the odd coefficients are positive, and for \(b\le q\) the even coefficients have numerator at least \(q^k-r^k>0\). They are summable in that regime, and normalizing at \(s=1\) yields the compound-Poisson law with jump intensities \(\lambda_k\). If \(b>q\) all sufficiently large even coefficients are negative. Negative coefficients rule out ordinary additive infinite divisibility: for a positive zero atom, the formal expansion of the \(m\)-th PGF root shows that \(m[s^k]G(s)^{1/m}\to\lambda_k\) for each \(k\ge1\), while each root would have nonnegative coefficients. This recalls the boundary argument and establishes the existence and parity of \(K\).

Put \(t=\log(b/q)>0\) and \(\rho=r/q\in(0,1)\). At an even index \(k\), negativity is exactly \(e^{kt}+\rho^k>2\). At \(t=0\) each fixed even index has \(1+\rho^k<2\); by continuity every fixed finite set of even indices is nonnegative for all sufficiently small \(t\). Thus \(K\to\infty\). The first even integer at or above \((\log 2)/t\) certainly has a negative coefficient, even in the equality case because \(\rho^k>0\). Hence \(Kt\le\log 2+2t\). At \(K\) itself, \(Kt>\log(2-\rho^K)\); since \(\rho^K\to0\) at fixed \(\theta\), the lower bound tends to \(\log 2\). This proves the limit.

## Verification and scope

The accompanying `check_bpl.py` gives finite checks of the mass function, coefficient formula, boundary, and illustrative first negative indices. The limit follows from the inequalities above, not from these tests. There is no assertion uniform in \(\theta\), no claim about Bernoulli-thinning self-decomposability, and no implication of infinite divisibility from overdispersion alone.

## Relationship to prior work

Bakouch et al. give the BPL count model and PGF [1]. The same log-PGF coefficient formula and ordinary compound-Poisson criterion are also proved in [2, Proof §§1–2] as background for a different question, namely when this law is self-decomposable under thinning. They are not claimed here as original results. The present claim is the location of the first negative formal coefficient in the approaching-boundary regime, a separate limiting question not addressed by a criterion for thinning in the compound-Poisson region. Letac, Malouche and Maurer [3] instead study real convolution powers of laws with factors \((1+z/c)^x(1-z)^{-y}\), without the additional distinct numerator zero of the BPL law. Historical priority for the first-coefficient limit is limited to the comparisons described here.

## References

1. H. S. Bakouch, C. Chesneau, R. Maya, M. R. Irshad, S. Aswathy and N. Qarmalah, *A Flexible Dispersed Count Model Based on Bernoulli Poisson–Lindley Convolution and Its Regression Model*, Axioms **12** (2023), 813, https://doi.org/10.3390/axioms12090813.
2. *A two-index thinning self-decomposability criterion for Bernoulli–Poisson–Lindley counts*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-two-index-thinning-self-decomposability-criterion-for-bernoull--12cdb9820df2/RESULT.md.
3. G. Letac, D. Malouche and S. Maurer, *The Real Powers of the Convolution of a Negative Binomial Distribution and a Bernoulli Distribution*, Proc. Amer. Math. Soc. **130** (2002), 2107–2114, https://doi.org/10.1090/S0002-9939-02-05352-2.
