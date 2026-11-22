# Exact founder-age bias in critical geometric branching with immigration

## Finding

Consider a critical branching population with one new immigrant per generation, where each individual has geometric offspring with probability \(\Pr(\xi=j)=2^{-j-1}\) for integers \(j\ge0\). At time \(n\), choose one living individual uniformly *after observing the realized population*, and let \(A_n\) be the age in generations of its immigrant founder and \(Y_n\) the population size. The exact conditional distribution is, for integers \(n\ge2\), \(0\le m\le n-2\), \(k\ge1\),

\[
\Pr(A_n\le m\mid Y_n=k)=\frac1k\sum_{j=0}^{k-1}\left(\frac{mn}{(m+1)(n-1)}\right)^j.
\]

It decreases strictly with the observed population size \(k\); larger populations favor older immigrant ancestry. Its unconditional distribution is

\[
\Pr(A_n\le m)=\frac{m+1}{n-m-1}\log\frac{n}{m+1}.
\]

Set \(T_n=A_n/n\) and \(X_n=Y_n/n\). Then \((T_n,X_n)\Rightarrow(T,X)\), where \(X\) has the mean-one exponential law and, for \(0<r<1\), \(x>0\),

\[
\Pr(T\le r\mid X=x)=\frac{r}{(1-r)x}\left(1-e^{-x(1-r)/r}\right).
\]

Equivalently the joint subdistribution of \((T,X)\) has density in the second coordinate

\[
\Pr(T\le r,\ X\in dx)=\frac{r}{1-r}\frac{e^{-x}-e^{-x/r}}{x}\,dx.
\]

Consequently \(T\) has continuous distribution

\[
\Pr(T\le r)=\frac{-r\log r}{1-r},\qquad
f_T(r)=\frac{r-1-\log r}{(1-r)^2},\qquad
\mathbb E T=2-\frac{\pi^2}{6}.
\]

The sampling convention is essential. If the random population is first size-biased and only then an individual is uniformly selected, every immigrant age is *exactly uniform* on \(\{0,\ldots,n-1\}\) at every finite \(n\).

## Assumptions and scope

The process begins with \(Y_0=0\). At each step all existing individuals reproduce independently with offspring generating function \(f(s)=1/(2-s)\), and precisely one individual immigrates *after* reproduction. Immigration is independent of reproduction and every immigrant carries a distinct immutable founder label. Thus \(Y_{n+1}=1+\sum_{i=1}^{Y_n}\xi_{n+1,i}\), \(Y_n\ge1\), and \(A_n=0\) means the most recent immigrant. The oldest possible age is \(n-1\). Conditional probabilities are defined by sampling one of the \(Y_n\) living individuals with equal weight in each realization, not by sampling from a size-biased law for \(Y_n\). The remaining boundary values are \(\Pr(A_n\le n-1)=1\), \(\Pr(A_n<0)=0\), and \(A_1=0\) almost surely.

The results concern this discrete-time critical geometric-offspring and deterministic unit-immigration model. No universality assertion for other offspring or immigration laws is made.

## Proof

**1. Founder-family generating functions.** For a single immigrant whose descendants have evolved for \(a\) generations, the iterated offspring generating function is

\[
f_a(s)=1-\frac{1-s}{1+a(1-s)}
=\frac{1+(a-1)(1-s)}{1+a(1-s)},\qquad a\ge0.
\]

This follows by induction from \(f(s)=1/(2-s)\) and \(f_0(s)=s\). At generation \(n\) there is precisely one independent family of each age \(0,\ldots,n-1\). Telescoping their generating functions gives

\[
F_n(s)=\mathbb E[s^{Y_n}]=\prod_{a=0}^{n-1}f_a(s)
=\frac{s}{1+(n-1)(1-s)}.
\]

Hence \(\Pr(Y_n=k)=n^{-1}[(n-1)/n]^{k-1}\) for \(k\ge1\).

**2. Population-weighted recent descendants.** Let \(B_{n,m}\) denote the number of living descendants of immigrants with ages in \(\{0,\ldots,m\}\). The recent-family product is \(H_m(s)=\prod_{a=0}^{m}f_a(s)=s/[1+m(1-s)]\). Differentiating only these factors yields the *exact* marked generating function

\[
\mathbb E[B_{n,m}s^{Y_n}]
=sF_n(s)\frac{H_m'(s)}{H_m(s)}
=\frac{(m+1)s}{[1+(n-1)(1-s)][1+m(1-s)]}.
\]

Write \(\alpha=(n-1)/n\) and \(\beta=m/(m+1)\). The coefficient of \(s^k\) in the last generating function is

\[
\frac1n\sum_{j=0}^{k-1}\alpha^{k-1-j}\beta^j.
\]

Since \(\Pr(A_n\le m\mid\text{realized families})=B_{n,m}/Y_n\), division by \(k\Pr(Y_n=k)\) proves the exact finite-size conditional formula, including its strict monotonicity in \(k\) when \(m\le n-2\), because the average of the first \(k\) terms in the strictly decreasing geometric sequence with ratio \(0\le\beta/\alpha<1\) decreases with \(k\).

**3. Unconditional age and tilted-versus-ordinary sampling.** Average the conditional formula with the geometric law of \(Y_n\), and use \(\sum_{k\ge1}z^k/k=-\log(1-z)\). With \(q=\beta/\alpha\),

\[
\Pr(A_n\le m)=\frac{1}{n\alpha(1-q)}
\log\frac{1-\beta}{1-\alpha}
=\frac{m+1}{n-m-1}\log\frac{n}{m+1}.
\]

In the alternative population-size-biased experiment, the chance to select an immigrant age \(a\) is \(\mathbb E Z_a/\mathbb E Y_n=1/n\), since every critical family has mean one; this yields exact uniformity under that *different* experiment.

**4. Joint scaling limit.** The geometric law shows \(X_n=Y_n/n\Rightarrow X\sim\operatorname{Exp}(1)\). For fixed \(0<r<1\) and \(m=\lfloor nr\rfloor\),

\[
q_{n,m}=\frac{mn}{(m+1)(n-1)}
=1-\frac{n-m-1}{(m+1)(n-1)}
=1-\frac{1-r}{rn}+o(n^{-1}).
\]

If \(k/n\to x>0\), then the exact conditional cumulative distribution converges to \(r[1-e^{-x(1-r)/r}]/[(1-r)x]\), uniformly when \(x\) ranges over any compact interval in \((0,\infty)\). Combining this with the geometric weak limit gives convergence of the joint mixed distribution functions \(\Pr(A_n/n\le r,Y_n/n\le x)\) for all \(0<r<1\) and \(x>0\). Indeed, restrict to \(\varepsilon\le k/n\le M\) for uniformity, then let \(\varepsilon\downarrow0\) and \(M\uparrow\infty\); the discarded probability is controlled by the exponential population limit. This proves the joint convergence. Multiplying the conditional limit by the exponential density gives the asserted joint subdistribution.

**5. Marginal density and mean.** Integration over \(x>0\) and the logarithmic integral identity \(\int_0^\infty(e^{-ax}-e^{-bx})\,dx/x=\log(b/a)\), for positive \(a,b\), give \(\Pr(T\le r)=-r\log r/(1-r)\). Differentiation gives the displayed density. The endpoints have no atoms because the cumulative distribution tends to \(0\) and \(1\) there. The tail integral for the mean, using the positive geometric-series expansion of \(1/(1-r)\), yields \(\mathbb E T=2-\sum_{j\ge1}j^{-2}=2-\pi^2/6\).

## Verification

The standalone Python 3 checker `check.py` independently enumerates all joint family-size/recent-descendant probabilities for finite populations, directly from the one-immigrant family offspring laws, using exact rational arithmetic. It checks the total geometric distribution, every tested conditional founder-age formula, strict conditional stochastic monotonicity, the explicit unconditional CDF by a bounded geometric mixture, and scaling consistency. The analytical identities and convergence proof above establish the infinite result; finite checks are supplementary and not proofs of general convergence.

Reproduce using `python3 check.py` from the extracted package directory. Only the Python standard library is required.

## Relationship to prior work

Sharipov, Tarasov and Wachtel (2026) give local limits for critical branching *population counts*, including approximation by critical geometric offspring. Their results do not identify founder labels or the sample-conditioned ancestral-age law. Klebaner and Sagitov (2002) use a backward geometric Galton–Watson construction with immigration but define population age as a *hitting time to one* in a backward process; their critical limit is an unrelated heavy-tailed stopping-time law, not the random immigrant founder age in the forward unit-immigration process. Cardona-Tobón and Palau (2025) study the ancestral coalescent for *one* linear-fractional Galton–Watson family with no immigration, rather than age comparisons among multiple immigrants. Smadi and Vatutin (2021) analyze the event that exactly one immigrant family survives in a random environment, which differs from uniformly sampling a present-day individual from all families.

The finite conditional law and its explicit joint limit are not asserted as independent validation or established universal priority; they are a theorem within the stated narrow model.

## Limitations

The offspring law and immigration timing are essential to the telescoping product and exact formula; the result does not directly extend to arbitrary Galton–Watson immigration models. A broad 1974 study of branching processes with immigration explicitly mentions age structure in its abstract, but its full text was unavailable during the literature comparison. Consequently historical priority beyond the available materials remains open. This result has not received independent mathematical assessment.

## References

- S. Sharipov, A. Tarasov and V. Wachtel, *Local limit theorem for critical branching processes with immigration*, arXiv:2611.19363v1 (first public 2026-11-14). https://arxiv.org/abs/2611.19363
- F. C. Klebaner and S. Sagitov, *The age of a Galton–Watson population with a geometric offspring distribution*, Journal of Applied Probability 39 (2002), 816–828. https://doi.org/10.1239/jap/1037816021
- N. Cardona-Tobón and S. Palau, *The coalescent of a sample from a linear-fractional branching process*, arXiv:2506.17470 (2025). https://arxiv.org/abs/2506.17470
- C. Smadi and V. A. Vatutin, *Critical branching processes in random environment with immigration: the size of the only surviving family*, arXiv:2109.13315 (2021). https://arxiv.org/abs/2109.13315
- S. D. Durham, *Limiting distributions for the general branching process with immigration*, Journal of Applied Probability (1974). https://doi.org/10.2307/3212563 (abstract consulted; full-text historical comparison unresolved)
