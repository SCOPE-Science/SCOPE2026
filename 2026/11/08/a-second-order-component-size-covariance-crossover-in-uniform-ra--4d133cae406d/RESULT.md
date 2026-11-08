# A second-order component-size covariance crossover in uniform random mappings

## Finding
For an integer \(n\ge2\), let \(F_n:[n]\to[n]\) be chosen uniformly among all \(n^n\) functions. Write \(K_n\) for the number of weakly connected components of its functional digraph and \(X_{n,r}\) for the number of components containing exactly \(r\) vertices, \(1\le r\le n\). Set \(\mu_0=0\) and
\[
\mu_m=\sum_{j=1}^{m}\frac{(m)_j}{j m^j}\quad(m\ge1),
\]
where \((m)_j=m(m-1)\cdots(m-j+1)\). The exact covariance is
\[
\operatorname{Cov}(K_n,X_{n,r})=\mathbb E[X_{n,r}](1+\mu_{n-r}-\mu_n),\qquad
\mathbb E[X_{n,r}]=\frac{\binom nr c_r(n-r)^{n-r}}{n^n},
\]
with \(c_r=(r-1)!\sum_{q=0}^{r-1}r^q/q!\) and the convention \(0^0=1\). Every displayed expectation is positive.

The covariance is strictly positive at \(r=1\), strictly negative at \(r=n\), and its sign factor \(1+\mu_{n-r}-\mu_n\) is strictly decreasing in \(r\). Thus there is exactly one transition from positive to nonpositive values, allowing at most one zero. Let \(R_n\) be the smallest integer \(r\) with nonpositive covariance. Then
\[
R_n=(1-e^{-2})n+\frac23\sqrt{\frac\pi2}\,e^{-2}(e-1)\sqrt n+o(\sqrt n).
\]
Equivalently, for every fixed \(\alpha\in(0,1)\) and sequence \(r_n/n\to\alpha\),
\[
\frac{\operatorname{Cov}(K_n,X_{n,r_n})}{\mathbb E[X_{n,r_n}]}
\longrightarrow 1+\tfrac12\log(1-\alpha).
\]
The crossover occurs at a macroscopic fraction \(1-e^{-2}\), with an explicit positive order-\(\sqrt n\) displacement of the finite threshold.

## Assumptions and scope
The probability space consists of all functions on \([n]\), sampled independently and uniformly coordinatewise. A component means a weak connected component of the directed graph with one outgoing edge at each vertex, including self-loops. Components are counted by vertices rather than cycle length. All finite identities hold for every integer \(n\ge2\) and every \(1\le r\le n\). The limit in \(\alpha\) is pointwise for fixed \(\alpha\in(0,1)\); the threshold expansion refers to the integer cutoff \(R_n\).

## Proof
**1. Component-count expectation.** Every functional component contains exactly one directed cycle. For a prescribed ordered \(j\)-tuple of distinct vertices, the probability that they form a directed cycle is \(n^{-j}\), and every directed \(j\)-cycle has \(j\) ordered presentations. Therefore the expected number of cycles of length \(j\) is \((n)_j/(j n^j)\). Summation proves \(\mathbb E K_n=\mu_n\).

**2. Component conditioning and finite covariance.** For a fixed subset \(S\subset[n]\) of size \(r\), the event that \(S\) is precisely a connected component depends only on the map restricted to \(S\) being connected and on every vertex outside \(S\) mapping outside \(S\). Conditional on this event, the outside restriction is a uniform random mapping on \(n-r\) points. Thus the conditional expected total component count is \(1+\mu_{n-r}\). Summing these events over all \(r\)-subsets and applying the definition of covariance gives
\[
\mathbb E[K_n X_{n,r}]=\mathbb E[X_{n,r}](1+\mu_{n-r}),
\]
and hence the stated covariance. The connected-mapping count \(c_r\) follows by selecting its unique cycle and attaching a rooted forest: the number with cycle length \(j\) is \(\binom rj(j-1)!j r^{r-j-1}\), and summing over \(j\) simplifies to the stated expression. For \(r=n\), the empty outside map contributes one possible configuration.

**3. Strict finite sign transition.** For each fixed \(j\), the product \((m)_j/m^j=\prod_{h=0}^{j-1}(1-h/m)\) strictly increases in \(m\) for \(j\ge2\); an extra positive term appears when \(m\) increases. Hence \(\mu_m\) strictly increases over positive integers, and \(\mu_1=1\). More specifically, for each \(j\ge2\),
\[
\frac{(n)_j}{j n^j}<\frac{(n-1)_{j-1}}{(j-1)(n-1)^{j-1}},
\]
so \(\mu_n<1+\mu_{n-1}\), including the \(n\)-term. Since \(\mu_n>1\) for \(n\ge2\), the sign factor is positive at \(r=1\) and negative at \(r=n\). Its strict decrease as \(r\) increases establishes the claimed unique cutoff and at-most-one equality.

**4. Uniform asymptotic expansion of the mean.** Let \(a_{m,j}=(m)_j/m^j\), extended by zero past \(j=m\), and \(S_m=\sum_{j\ge1}j^{-1}e^{-j^2/(2m)}\). Expanding \(\sum_{h=0}^{j-1}\log(1-h/m)\) on \(j=O(\sqrt m\log m)\), then using a Gaussian tail bound on the remaining indices, gives the absolutely summable expansion
\[
\mu_m=S_m+\frac1{\sqrt m}\int_0^\infty e^{-x^2/2}
\left(\frac12-\frac{x^2}{6}\right)dx+O(m^{-1})
=S_m+\frac{A}{\sqrt m}+O(m^{-1}),
\qquad A=\frac13\sqrt{\frac\pi2}.
\]
For clarity, putting \(x=j/\sqrt m\), the first correction to \(a_{m,j}\) is
\(e^{-x^2/2}(x/2-x^3/6)/\sqrt m\); the remaining correction is bounded by \(m^{-1}\) times a Gaussian-weighted polynomial in \(x\) with zero constant term, whose sum after division by \(j\) is \(O(m^{-1})\). Gaussian tails make the truncation error smaller than any fixed negative power. The integral is a standard Gaussian second-moment evaluation.

For any fixed \(0<\varepsilon<1/2\), uniformly for integers \(m\) with \(\varepsilon n\le m\le(1-\varepsilon)n\), a Riemann-sum comparison gives
\[
S_n-S_m=\frac12\log(n/m)+O_\varepsilon(n^{-1}).
\]
Indeed the summand difference is a discretization of the smooth integrable function \(x\mapsto [e^{-x^2/2}-e^{-x^2/(2m/n)}]/x\), which vanishes at zero; its integral is \(\frac12\log(n/m)\) by differentiating under the integral sign. Euler summation bounds the discretization error by \(O(n^{-1})\) because its value at zero vanishes and its derivative is integrable. Thus
\[
\mu_n-\mu_m=\frac12\log(n/m)+A(n^{-1/2}-m^{-1/2})+O_\varepsilon(n^{-1}).\tag{1}
\]

**5. Macroscopic and second-order cutoff.** Set \(\beta=e^{-2}\), \(\alpha_*=1-\beta\), and \(r=\alpha_* n+s\sqrt n+O(1)\). Then \(m=n-r=\beta n-s\sqrt n+O(1)\), and (1) yields
\[
1+\mu_m-\mu_n=\frac1{\sqrt n}
\left(A(e-1)-\frac{s}{2\beta}\right)+O(n^{-1}),
\]
uniformly for bounded \(s\). The sign changes at \(s_*=2\beta A(e-1)=\frac23\sqrt{\pi/2}e^{-2}(e-1)\). Strict monotonicity of the finite sign factor and upper/lower comparisons at \(s_*\pm\delta\) for each fixed \(\delta>0\) imply \(R_n=\alpha_*n+s_*\sqrt n+o(\sqrt n)\). Taking \(m/n\to1-\alpha\) in (1) proves the remaining limit.

## Verification
The standalone Python 3 script `verify.py` exhaustively examines all maps on \([n]\) for \(2\le n\le6\), checks the finite mean and covariance identities with exact rational arithmetic, checks monotonic sign factors through \(n=80\), and numerically tests the asymptotic cutoff at three larger sizes. It completed 3,386 assertions successfully. Its numerical large-size checks are illustrations, not proofs of the infinite limits; the proof is analytical above. Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work
The classical random-mapping framework of Flajolet and Odlyzko develops component-count statistics via generating functions. Donnelly, Ewens and Padmadisastra discuss exact and asymptotic frequency spectra, including macroscopic component sizes, and constitute an especially relevant potential earlier source. Hansen extends random mapping models to exchangeable indegrees. Timashov investigates component-size distributions conditional on the number of components. The distinct claim here is the **finite covariance sign cutoff with its explicit order-\(\sqrt n\) displacement**; neither marginal component counts nor a frequency-spectrum formula by itself asserts that displacement. Priority is qualified because complete text of some plausible broad older studies was not accessible.

## Limitations
This is not a claim of an independent external audit. Exact source-spectrum moment identities can implicitly subsume the finite covariance formula, even if they do not state its sign and second-order cutoff. The analysis is for uniform independent images and weakly connected component sizes only; it is not a theorem about uniform partitions, conditioned random mappings, or directed-cycle sizes. No distributional limit for \(X_{n,r}\) is asserted. The cutoff expansion gives an \(o(\sqrt n)\), not a bounded, error. The finite verifier does not prove the asymptotics.

## References
- P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT '89 proceedings (1990), DOI: https://doi.org/10.1007/3-540-46885-4_34.
- P. J. Donnelly, W. J. Ewens and S. Padmadisastra, *Functionals of random mappings: exact and asymptotic results*, Advances in Applied Probability 23 (1991), 437–455, DOI: https://doi.org/10.2307/1427616.
- J. C. Hansen, *Random mappings with exchangeable in-degrees*, Random Structures & Algorithms (first published September 4, 2007), DOI: https://doi.org/10.1002/rsa.20187.
- A. N. Timashov, *Limit theorems for the joint distribution of component sizes of a random mapping with a known number of components*, Discrete Mathematics and Applications 21 (2011), DOI: https://doi.org/10.1515/DMA.2011.003.
- S. Finch, *Components and Cycles of Random Mappings*, arXiv:2205.05579 (2022), https://arxiv.org/abs/2205.05579.
