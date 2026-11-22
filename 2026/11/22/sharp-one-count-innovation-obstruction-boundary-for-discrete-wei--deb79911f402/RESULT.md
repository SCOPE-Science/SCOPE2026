# Sharp one-count innovation obstruction boundary for discrete Weibull thinning

## Finding

**Theorem (exact first-innovation obstruction curve).** Let \(0<\beta<1\), \(0<q<1\), and let \(X\) have the type-I discrete Weibull law
\[
\Pr(X=n)=p_n=q^{n^\beta}-q^{(n+1)^\beta},\qquad n=0,1,2,\ldots.
\]
Put \(A=2^\beta\), \(B=3^\beta\), and define
\[
H_\beta(q)=-q+3q^A-2q^B-q^{1+A}+2q^{1+B}-q^{2A}.
\]
There is **exactly one** \(q_*(\beta)\in(0,1)\) satisfying \(H_\beta(q_*)=0\); it is a simple root, and \(H_\beta(q)<0\) for \(q<q_*\) while \(H_\beta(q)>0\) for \(q>q_*\).

For every \(q>q_*(\beta)\), the law is **not self-decomposable under Bernoulli thinning**: indeed, for every retention probability \(c\) sufficiently close to \(1\) from below, there is no independent nonnegative-integer innovation \(\varepsilon_c\) such that
\[
X\ \overset{d}=\ c\circ X'+\varepsilon_c,
\]
where \(X'\) is an independent copy of \(X\), \(c\circ X'\) independently retains each of its \(X'\) units with probability \(c\), and \(\varepsilon_c\) is independent of \(X'\) and its thinnings. Thus the entire region \(q>q_*(\beta)\) is excluded as a stationary marginal for an INAR(1) model at all sufficiently high retention probabilities, despite ordinary additive infinite divisibility.

The boundary has two explicit endpoint laws:
\[
\lim_{\beta\downarrow0}\beta\log\frac1{q_*(\beta)}=\tau_0,
\qquad
\tau_0=0.2837755261699677959\ldots,
\]
where \(\tau_0>0\) is the unique positive solution of \(3\,2^{-\tau}-2\,3^{-\tau}=1\); and
\[
\lim_{\beta\uparrow1}\frac{1-q_*(\beta)}{1-\beta}
=10\log2-6\log3=0.3397980735907949458\ldots.
\]
This theorem gives a **sharp boundary for the sign of the first-order one-count innovation obstruction**, not a sufficient condition for thinning self-decomposability at \(q\le q_*(\beta)\).

## Assumptions and scope

The shape is strictly between zero and one; the scale-survival parameter belongs to the open unit interval. All integer probabilities are on \(\mathbb N_0\). The term *self-decomposable under Bernoulli thinning* means existence of the independent innovation **for every** \(0<c<1\), not merely for one retention. The geometric endpoint \(\beta=1\) is excluded from the strict phase diagram and is self-decomposable by its standard geometric generating function. There is no claim that the entire lower region \(q<q_*\) is thinning self-decomposable, or that the equality curve is classified.

## Proof

**1. A generalized sign-variation lemma.** If \(\lambda_1<\cdots<\lambda_m\) are real and every \(d_i\ne0\), the number of positive roots of \(f(x)=\sum_{i=1}^m d_ix^{\lambda_i}\), counted with multiplicity, is at most the number of sign changes in \((d_1,\ldots,d_m)\). One elementary proof is by induction on \(m\): divide by \(x^{\lambda_1}\), then differentiate. By induction the derivative has at most the sign changes among \(d_2,\ldots,d_m\). Rolle's theorem accounts for all but at most one of the zeros of the divided function. When \(d_1\) and \(d_2\) have the same sign, the divided function initially moves away from zero, forcing a further critical point before its first zero, so no additional sign change is needed. When they have opposite signs, the one potentially unaccounted-for zero is precisely covered by the extra sign change. Multiplicity is handled by repeated Rolle at a multiple zero. This yields the stated bound.

**2. Unique obstruction root.** Since \(0<\beta<1\), strict concavity of positive powers gives
\[
1<A<B<1+A<1+B<2A.
\]
For \(H_\beta\), the ordered coefficient signs are \((- ,+,-,-,+,-)\), with four changes; the lemma gives at most four positive roots counted with multiplicity. Direct differentiation at \(q=1\) gives \(H_\beta(1)=H'_\beta(1)=0\) and
\[
\tfrac12H''_\beta(1)=F_\beta:=2B-A-A^2
=2\,3^\beta-2^\beta-4^\beta>0.
\]
The last strict inequality is the midpoint-concavity inequality for the points \(2,3,4\). Thus \(1\) is a root of exact multiplicity two and \(H_\beta(q)>0\) immediately below \(1\). On the other hand, \(H_\beta(q)=-q+o(q)<0\) as \(q\downarrow0\). Hence there is an odd-multiplicity zero in \((0,1)\). Since no more than two positive zeros counted with multiplicity remain after accounting for the double root at one, there can be exactly one root in \((0,1)\), and it is simple. Continuity fixes the signs on either side. There may be a positive root beyond one; the theorem neither needs nor asserts its absence.

**3. Exact innovation-coefficient obstruction.** Write \(G(z)=\sum_{n\ge0}p_nz^n\); for \(|z|<1\), this is analytic and \(G(0)=p_0=1-q>0\). Were a thinning innovation to exist, its generating function would necessarily be
\[
R_c(z)=\frac{G(z)}{G(1-c+cz)}.
\]
In particular \(R_c(0)>0\) and the probability of one innovation must be nonnegative. Define \(r_1=(\log G)'(0)=p_1/p_0\) and \(r_2=(\log G)''(0)=2p_2/p_0-(p_1/p_0)^2\). Logarithmic differentiation shows
\[
\frac{R'_c(0)}{R_c(0)}=r_1-c\,\frac{G'(1-c)}{G(1-c)}
=(1-c)(r_1-r_2)+O((1-c)^2).
\]
With \(p_0=1-q\), \(p_1=q-q^A\), \(p_2=q^A-q^B\), elementary expansion gives the exact identity
\[
r_2-r_1=\frac{H_\beta(q)}{(1-q)^2}.
\]
Thus, for every \(q>q_*\), \(H_\beta(q)>0\) and \(R'_c(0)<0\) for all \(c<1\) sufficiently near one. Such a function cannot be a probability generating function. Conversely, the first-order coefficient obstruction has the opposite sign below \(q_*\), which alone says nothing about other innovation coefficients.

**4. Endpoint \(\beta\uparrow1\).** At \(\beta=1\), the formal expression reduces to \(H_1(q)=-q(1-q)^3<0\) for \(0<q<1\). Therefore \(q_*(\beta)\to1\) as \(\beta\uparrow1\). Set \(t=-\log q\). A Taylor expansion of the six exponentials, uniform for \(\beta\) near one and \(t\) near zero, gives
\[
H_\beta(e^{-t})=t^2\{F_\beta-t+O((1-\beta)t+t^2)\}.
\]
Moreover \(F_\beta=(10\log2-6\log3)(1-\beta)+O((1-\beta)^2)\). Substitution of the unique positive zero shows \(t_*\sim F_\beta\) (by comparing signs at \(t=(1\pm\delta)F_\beta\) for fixed \(\delta>0\)); since \(1-e^{-t_*}\sim t_*\), the second displayed limit follows.

**5. Endpoint \(\beta\downarrow0\).** For each fixed \(\tau>0\), put \(q=e^{-\tau/\beta}\). Then
\[
\frac{H_\beta(q)}q\longrightarrow g(\tau):=-1+3\,2^{-\tau}-2\,3^{-\tau}.
\]
Here \(g(0)=0\), \(g'(0)=2\log3-3\log2=\log(9/8)>0\), and \(g(\tau)\to-1\). The derivative \(g'(\tau)\) has a unique positive zero, since the ratio of its two exponential terms is strictly monotone. Consequently \(g\) is positive until one unique positive zero \(\tau_0\), then negative. The sharp signs of \(H_\beta\) around \(q_*\), evaluated at \(q=e^{-(\tau_0\pm\delta)/\beta}\), squeeze \(\beta\log(1/q_*)\) between \(\tau_0-\delta\) and \(\tau_0+\delta\). The first limit follows.

**6. Independent supporting fact: ordinary infinite divisibility.** For \(0<\beta<1\) and \(t=-\log q>0\), the function \(e^{-t x^\beta}\) is the Laplace transform of a positive stable random variable \(S\); for example the Lévy–Khintchine identity
\[
x^\beta=\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty(1-e^{-xy})y^{-1-\beta}\,dy
\]
constructs it as a limit of compound-Poisson subordinators. With \(U=e^{-S}\in(0,1)\), \(p_n=\mathbb E[(1-U)U^n]\), a mixture of geometric probability masses. Cauchy–Schwarz applied to this positive mixture shows \(p_n^2\le p_{n-1}p_{n+1}\). Set \(a_n=p_n/p_0\), \(a_0=1\), and define recursively \(b_n=a_n-\sum_{j=1}^{n-1}b_ja_{n-j}\). Monotonicity of ratios \(a_n/a_{n-1}\) and induction show \(b_n\ge0\): if the earlier \(b_j\) are nonnegative, then
\[
a_n=\frac{a_n}{a_{n-1}}\sum_{j=1}^{n-1}b_ja_{n-1-j}\ge\sum_{j=1}^{n-1}b_ja_{n-j}.
\]
Therefore \(G(z)=p_0/[1-\sum_{n\ge1}b_nz^n]\). Since \(G(1)=1\), \(\sum b_n=1-p_0<1\) (by monotone convergence); expanding \(-\log(1-\sum b_nz^n)\) gives a finite nonnegative compound-Poisson Lévy sequence. This confirms the known ordinary infinite divisibility independently of the original article's inaccessible proof. It does **not** imply thinning self-decomposability.

## Verification

The included `check.py` (Python standard library only) reproduces the polynomial identity at finite sample parameters using direct mass and logarithmic derivatives, brackets the six reported transition values by bisection, checks the large- and small-shape limiting constants, and verifies the negative one-count innovation coefficient for \(\beta=1/2\), \(q=4/5\), \(c=99/100\) using high-precision decimal arithmetic. Its finite computations corroborate rather than replace the all-parameter proof in the preceding section. For illustration, \(q_*(1/2)=0.6337051370046700169\ldots\).

## Relationship to prior work

The discrete Weibull survival construction dates back to Nakagawa–Osaki (1975). Kreer, Kizilersu and Thomas (2024) characterize *ordinary* infinite divisibility of the discrete Weibull law, identifying \(0<\beta\le1\), and their result is treated as prior art, not claimed here. The new assertion concerns a sharper, operationally different property: nonexistence of independent thinning innovations, via a unique nontrivial obstruction curve and two endpoint asymptotics. General theory of thinning-based count processes and compound-Poisson laws does not itself supply this curve. The source's complete 2024 proof was not accessible; therefore a claim of comprehensive historical priority is not made.

## Limitations

The theorem supplies a **necessary exclusion region**, not a complete self-decomposability parameter classification: nothing is asserted on the curve or on the low-\(q\) side. The derivative obstruction concerns all sufficiently high retentions, rather than a universal numerical retention cutoff. The cited 2024 article was available in bibliographic/abstract form only; older general theory may bear on historical priority. The proof and numerical reproduction here were reviewed in the same study, not independently validated.

## References

1. M. Kreer, A. Kizilersu, A. W. Thomas, *When is the discrete Weibull distribution infinitely divisible?* Statistics & Probability Letters **215** (2024), 110238. DOI: https://doi.org/10.1016/j.spl.2024.110238 ; preprint record: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4785843 (public record dated 2024-04-05).
2. T. Nakagawa and S. Osaki, *The discrete Weibull distribution*, IEEE Transactions on Reliability **24** (1975), 300–301. DOI: https://doi.org/10.1109/TR.1975.5214915.
3. A. A. Adesina and coauthors, *On the Performance of Dirichlet Prior Mixture of Generalized Linear Mixed Models for Zero Truncated Count Data*, Journal of Statistics Applications & Probability **12** (2023), 1167–1182, DOI: https://doi.org/10.18576/jsap/120324 (2023-09-01; freely available PDF includes the explicit mass function).
4. H. S. Bakouch, *A weighted negative binomial Lindley distribution with applications to dispersed data*, Anais da Academia Brasileira de Ciências **90** (2018), section on discrete analogues of self-decomposability. https://www.scielo.br/j/aabc/a/NHrM8Y4mnHGjJrBWC8zqqQy/?lang=en.
