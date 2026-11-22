# An exact three-site Langmuir paradox: greater density polarization but weaker correlations

## Finding
Consider a three-site open totally asymmetric simple exclusion process with unit rightward hopping, equal entry and exit rates \(a>0\), and equal bulk attachment and detachment rates \(w\ge 0\) **at the middle site only**. Let \(\eta_j\in\{0,1\}\) denote stationary occupation at site \(j\), from left to right. Write
\[
D(a,w)=2a^3+3a^2+2a+w(2a+1)^2.
\]
Then the three distinct stationary occupation covariances are exactly
\[
\operatorname{Cov}(\eta_1,\eta_2)=\operatorname{Cov}(\eta_2,\eta_3)=\frac{a(1-2a)}{4D(a,w)},
\]
\[
\operatorname{Cov}(\eta_1,\eta_3)=\frac{a^2(1-2a)(2a+4w+1)}{4D(a,w)^2}.
\]
Thus **all** off-diagonal covariances are positive for \(0<a<1/2\), vanish for \(a=1/2\), and are negative for \(a>1/2\), independently of the bulk exchange rate. For every \(a\ne1/2\), increasing \(w\) strictly **reduces the absolute magnitude of every off-diagonal covariance** while strictly **increasing the boundary density contrast**
\[
\Delta(a,w)=\mathbb E[\eta_3]-\mathbb E[\eta_1]
=\frac{(1-2a)(a^2+a+w(2a+1))}{D(a,w)}
\]
in absolute value. Specifically,
\[
\frac{\partial\Delta}{\partial w}=
\frac{a(1-2a)(2a+1)}{D(a,w)^2}.
\]
The mean middle occupancy is exactly \(1/2\) and the mean total occupancy is exactly \(3/2\), for **all** allowed rates. The limiting contrast at strong exchange is
\[
\lim_{w\to\infty}\Delta(a,w)=\frac{1-2a}{2a+1},
\]
while all off-diagonal covariances tend to zero. This simultaneously classifies all three pair-correlation signs and resolves the opposite effects of bulk exchange on spatial polarization and connected spatial fluctuations in the first chain length with an interior Langmuir site.

## Assumptions and scope
The continuous-time chain has state \((\eta_1,\eta_2,\eta_3)\in\{0,1\}^3\). It accepts a particle at site 1 at rate \(a\) if empty; a particle at site 3 leaves at rate \(a\); an occupied site \(j\in\{1,2\}\) transfers its particle to \(j+1\) at rate 1 if the latter is empty; at site 2 alone, a zero flips to one and a one flips to zero, each at rate \(w\). All mechanisms use independent exponential clocks. The result is finite-volume, not a claim of a thermodynamic phase transition. For \(a>0\), the finite-state chain is irreducible also at \(w=0\); thus its unique stationary law exists. No mean-field closure is assumed.

## Proof
Use the following four weights, with each expression applying to the two listed occupation triples:

| Occupation triples | Unnormalized weight |
|---|---|
| \(000,111\) | \(a(2w+1)\) |
| \(100,110\) | \(a^2(2a+4w+1)\) |
| \(010,101\) | \(2a(a+w)\) |
| \(001,011\) | \(a+w\) |

The total of these eight weights is \(2D(a,w)\). Substituting each weight into the eight stationary master equations gives zero net probability flux at each configuration. For example, at the empty state the balance equation is \(aP_{001}+wP_{010}-(a+w)P_{000}=0\), with triple coordinates ordered from entry to exit. The accompanying checker constructs every legal transition directly and verifies all eight balance equations as exact polynomial identities. The weights are strictly positive for every \(a>0,w\ge0\), so irreducibility makes this the unique stationary law.

Summation of the weights gives
\[
\mathbb E[\eta_1]=\frac{a(2a+1)(2a+4w+1)}{2D(a,w)},\quad
\mathbb E[\eta_2]=\frac12,\quad
\mathbb E[\eta_3]=1-\mathbb E[\eta_1].
\]
Likewise summing weights at configurations with two specified occupied sites and subtracting products of single-site means yields the two displayed covariance formulas. Every factor of \(D\) is positive on the whole parameter domain, so each covariance sign is the sign of \(1-2a\). In particular, at \(a=1/2\) the eight stationary probabilities are all \(1/8\), hence the law is product Bernoulli one-half.

For \(a\ne1/2\), the adjacent covariance magnitudes strictly decrease because \(D\) is affine increasing in \(w\), with \(\partial_wD=(2a+1)^2>0\). For the separated pair, differentiation gives
\[
\frac{\partial}{\partial w}\operatorname{Cov}(\eta_1,\eta_3)=
\frac{a^2(2a-1)(2D(a,w)-2a+1)}{2D(a,w)^3},
\]
whose sign is opposite to that of the covariance because \(2D-2a+1=4a^3+6a^2+2a+1+w(8a^2+8a+2)>0\). Thus all absolute pair covariances decrease strictly.

Subtracting the two boundary means yields the displayed \(\Delta\). Differentiation yields its stated derivative, which has the same sign as \(\Delta\) whenever \(a\ne1/2\). Hence \(|\Delta|\) strictly increases. Taking the explicit rational limits as \(w\to\infty\) finishes the proof.

## Verification
Run `python check.py` with standard Python. It independently forms the full eight-state generator, verifies each stationary balance identity as an exact bivariate rational-coefficient polynomial, checks normalization and all displayed mean/covariance/derivative identities, and solves the original stationary equations afresh with rational Gauss–Jordan elimination for 20 parameter pairs. Every reported check passed. The symbolic master-equation identities, not the numerical samples, justify the universal quantifiers. No simulation or finite parameter grid is used to infer a global sign law.

## Relationship to prior work
Silva, Carvalho, Almeida and Duarte-Filho (2026) formulated the finite-chain TASEP–Langmuir master equation and computed stationary density profiles and covariance matrices using a general zero-eigenvector method, including numerical finite-size examples. That exact stationary methodology is prior work. The result here singles out the first interior-exchange chain, derives closed rational formulas for **all rates in a natural symmetry subfamily**, and establishes a global covariance-sign boundary and the simultaneous strict, oppositely directed dependence of spatial polarization and correlation strength on bulk exchange. These qualitative inequalities do not appear in its examined text, and its fixed-parameter covariance figures alone do not imply the universal statements. Botto, Pelizzola, Pretti and Zamparo (2018/2019) considered balanced Langmuir kinetics and mean-field dynamical transitions; their mean-field equations neglect the connected finite-chain covariances determined here. Previously established product-measure behavior at matched boundary and bulk densities is compatible with the special case \(a=1/2\) and is not claimed as novel.

## Limitations
The classification is restricted to **exactly three sites**, unit rightward hop rate, equal entry and exit rates, and balanced attachment/detachment at the single interior site. It is not proved for longer chains, asymmetric reservoirs, or unequal adsorption and desorption. The stationary linear-algebra computation is elementary at this size, and prior general finite-state methods may implicitly permit recovery of the formulas; the novelty asserted is the *global qualitative sign and monotonicity classification*, not the ability to solve an eight-state Markov chain. No independent validation or publication-priority certification is claimed.

## References
1. L. D. S. Silva, A. M. S. Carvalho, F. A. G. Almeida and G. C. Duarte-Filho, *Langmuir kinetics and totally asymmetric volume exclusion in linear chains via Fock space formalism*, arXiv:2611.07053v1, first submitted 2026-11-04. https://arxiv.org/abs/2611.07053
2. D. Bott, A. Pelizzola, M. Pretti and M. Zamparo, *Dynamical transition in the TASEP with Langmuir kinetics: Mean-field theory*, arXiv:1809.03231v1 (2018); J. Phys. A 52 (2019) 045001. https://arxiv.org/abs/1809.03231
3. See the published finite-volume TASEP–Langmuir and open-exclusion literature cited in the two works above for the underlying model, its symmetry, and the previously known mean-field/steady-state frameworks.
