# Exact coupling-dependent variance and error laws for Poisson-path quadrature

## Finding
For an integrated homogeneous Poisson counting path, the dependence between one uniform location in each equal time cell has an exactly measurable impact on numerical integration error. All schemes in the theorem are conditionally unbiased for every fixed path, yet their unconditional mean-square errors differ at the leading \(n^{-2}\) scale for a common shift versus balanced dependence. The complete theorem is given below, including a sharp coupling variance floor and distributional error laws.

## Assumptions and scope
Fix \(\lambda>0\) and an integer \(n\ge1\). Let \(N(t)\) be a rate-\(\lambda\) homogeneous Poisson counting process on \([0,1]\) with \(N(0)=0\). Let \(U_1,\dots,U_n\) be jointly distributed independently of the whole process \(N\), each marginally uniform on \([0,1]\); their dependence is arbitrary. Define
\[
I=\int_0^1N(t)\,dt,\qquad
Q_n=\frac1n\sum_{i=1}^nN\!\left(\frac{i-1+U_i}{n}\right),\qquad Z_n=n(Q_n-I).
\]
Then every such randomized scheme obeys \(\mathbb E[Q_n\mid N]=I\), \(\mathbb E Z_n=0\), and
\[
\boxed{\operatorname{Var}(Z_n)=\frac\lambda6+
\frac{\lambda^2}{n^2}\operatorname{Var}\!\left(\sum_{i=1}^nU_i\right).}
\]
Consequently \(\operatorname{Var}(Z_n)\ge\lambda/6\), with equality exactly when the sum of the offsets is almost surely constant. For even \(n\), independent uniform variables \(V_j\) and pairs \((U_{2j-1},U_{2j})=(V_j,1-V_j)\) attain equality. Independent offsets yield \(\lambda/6+\lambda^2/(12n)\); a single shared uniform offset yields \(\lambda/6+\lambda^2/12\).

For independent offsets, \(Z_n\) approaches in total variation the compound Poisson variable \(Z_\infty=\sum_{j=1}^{K}W_j\), where \(K\sim\mathrm{Poisson}(\lambda)\), and independent \(W_j\) have density \((1-|w|)_+\) on the real line:
\[
 d_{\mathrm{TV}}(\mathcal L(Z_n),\mathcal L(Z_\infty))\le\frac{\lambda^2}{2n}.
\]
The even-\(n\) complementary-pair construction has the same limit with total-variation distance bounded by \(\lambda^2/n\). A single common shift has an exactly \(n\)-invariant law: conditionally on the common \(U=u\), it is compound Poisson with rate \(\lambda\) and jump law uniform on \([u-1,u]\). By contrast, deterministic midpoint offsets \(U_i=1/2\), which are not individually uniform, give an exactly \(n\)-invariant compound-Poisson law with rate \(\lambda\), jump law uniform on \([-1/2,1/2]\), and \(\operatorname{Var}(Z_n)=\lambda/12\). The midpoint comparison is unconditional over paths and does not assert conditional unbiasedness for a fixed path.

## Proof
Every path consists of a finite number \(K\) of jumps almost surely. A jump at \(t=(i-1+v)/n\), with relative phase \(v\in[0,1]\), contributes to \(Z_n\) the mark
\[
w(v,u)=\mathbf1_{\{u\ge v\}}-(1-v)=v-\mathbf1_{\{u<v\}}.
\]
This is an *identity* for the actual quadrature error. Conditional on the vector of offsets, the jump sets in different time cells are independent Poisson point processes of mean count \(\lambda/n\). For a fixed \(u\), direct integration over the jump phase gives
\[
\int_0^1 w(v,u)\,dv=u-\tfrac12,\qquad
\int_0^1 w(v,u)^2\,dv=\frac{u^3+(1-u)^3}{3}=u^2-u+\tfrac13.
\]
The elementary Poisson mean and variance identities therefore give
\[
\mathbb E[Z_n\mid(U_i)]=\frac\lambda n\sum_i(U_i-\tfrac12),\qquad
\operatorname{Var}(Z_n\mid(U_i))=\frac\lambda n\sum_i(U_i^2-U_i+\tfrac13).
\]
Since all margins are uniform, \(\mathbb E(U_i^2-U_i+1/3)=1/6\). The conditional-variance decomposition gives the displayed exact variance identity, with no independence assumption between offsets. The variance floor and complementary-pair attainment are immediate, as are the independent and shared specializations.

For a fixed \(u\), mapping \(v\mapsto w(v,u)\) sends a uniform phase to a uniform random variable on \([u-1,u]\). Thus a shared \(u\) yields the asserted conditional compound-Poisson law for every grid size. Fixing \(u=1/2\) gives the midpoint law. For a fresh independent uniform offset for each jump, the unconditional mark is the sum of two independent centered uniforms of width one and hence has triangular density \((1-|w|)_+\). Couple the actual independent-cell estimator to this ideal compound Poisson variable by giving each jump its own independent uniform offset, but using the actual cell offset whenever its cell contains exactly one jump. The variables agree unless some cell contains at least two jumps. The union bound using the second factorial moment of a \(\mathrm{Poisson}(\lambda/n)\) count gives at most \(n(\lambda/n)^2/2=\lambda^2/(2n)\). In the complementary-pair construction, use the whole pair of two cells as one block; different blocks have independent offsets, and the probability of two or more jumps in one block is at most \((\lambda(2/n))^2/2\), yielding \(\lambda^2/n\) after \(n/2\) blocks. Coupling bounds total variation and proves both statements.

For reproducibility, the independent-jitter characteristic function is also explicit. With \(s(t)=\sin(t/2)/(t/2)\), interpreted continuously at zero, it is
\[
\mathbb E e^{itZ_n}=\left[\int_0^1\exp\left\{\frac\lambda n\left(s(t)e^{it(u-1/2)}-1\right)\right\}\,du\right]^n.
\]
The limiting characteristic function is \(\exp\{\lambda(s(t)^2-1)\}\). This is a second verification of the limiting triangular compound-Poisson law.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 and no external libraries. It checks the exact uniform moment identities, pathwise jump decomposition against direct quadrature, numerical characteristic-function identities, predicted variance laws, and supplementary seeded Monte Carlo comparisons. The deterministic algebraic proof above, rather than finite simulation or the checker, proves the universal statements. The checker report at construction was: \(204657\) checks passed.

## Relationship to prior work
Doerr (2021) studies discrepancies of independently jittered point sets; his work fixes the standard independent-stratum construction and does not compare correlated offsets for integrated Poisson paths. Eisenmann and Kruse (2017) develop a randomized-mesh quadrature of Itô stochastic integrals, with a Poisson process used as a *stochastic integrand*, rather than ordinary time integration of the path and an exact cross-coupling variance law. Beentjes (2020) develops Poisson-bridge antithetic simulation for chemical reaction networks rather than this path-integration error law. Elementary Poisson random-measure formulas underlie our proof and could permit another author to derive special cases; this is a publication-precedence uncertainty, not a novelty certificate.

## Limitations
Only a homogeneous finite-activity Poisson counting path on a fixed unit interval is covered. All stated variances average over both the Poisson process and the sampling design; deterministic midpoint is generally not unbiased for the integral of a fixed realized path, although its unconditional mean error is zero in this model. The arbitrary-coupling variance minimum is explicitly attained here for even numbers of cells; nothing about odd-cell joint mixability is claimed. Total-variation estimates are valid upper bounds, not proved optimal rates. No claims are made about more general jump processes, time-varying intensities, or arbitrary integrands.

## References
- M. Eisenmann and R. Kruse, *Two quadrature rules for stochastic Itô-integrals with fractional Sobolev regularity*, arXiv:1712.08152, first submitted 2017-12-21, https://arxiv.org/abs/1712.08152 .
- B. Doerr, *A Sharp Discrepancy Bound for Jittered Sampling*, arXiv:2103.15712, first submitted 2021-03-29, https://arxiv.org/abs/2103.15712 .
- C. H. L. Beentjes, *Variance reduction techniques for chemical reaction network simulation*, doctoral thesis (2020), https://ora.ox.ac.uk/objects/uuid:3360f4a7-f78b-4da9-8431-c0899bb198c5 .
