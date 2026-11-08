# Long pendant paths reveal balanced transport in graph Lipschitz spread

## Finding
Let \(G\) be any connected finite simple graph on \(n\ge2\) vertices. Attaching an equal-length pendant path at **every** core vertex admits an exact reduction of the Lipschitz-variance extremal problem to an integer core potential and a sign partition. In the long-path range, the sharp constant becomes an **exact quadratic** whose linear coefficient is an optimal balanced transport cost. Among all connected cores of a fixed order, the path is the unique eventual maximizer, with an explicit uniform cutoff.

For the construction and notation below,
\[
\operatorname{spr}(G^{[\ell]})=\frac{\ell(\ell+2)}{12}+\max_{c\in\mathcal E_G,\,\varepsilon\in\{-1,1\}^n}\left[\frac{\ell^2}{4}\operatorname{Var}_G(\varepsilon)+\ell\operatorname{Cov}_G(c,\varepsilon)+\operatorname{Var}_G(c)\right]. \tag{1}
\]
Every optimizer has a strictly monotone, unit-slope restriction to each attached path. Define \(\kappa=n\bmod2\), \(a_n=(1-\kappa^2/n^2)/4\) and the quantities \(\beta_G,\gamma_G\) below. Then whenever \(\ell\ge n^2(\Delta+1)^2\),
\[
\operatorname{spr}(G^{[\ell]})=\left(\frac1{12}+a_n\right)\ell^2+\left(\frac16+\beta_G\right)\ell+\gamma_G. \tag{2}
\]
The sharp transport bounds are
\[
\frac{2\lfloor n^2/4\rfloor}{n^2}\le\beta_G\le\frac{\lfloor n^2/4\rfloor}{n}. \tag{3}
\]
The complete graph realizes the lower bound; the path realizes the upper bound and is its only equality case for \(n\ge3\). Consequently, for each \(n\ge3\) and every \(\ell\ge n^2(n+1)^2\), the path is the unique maximum-spread connected core of size \(n\).

One exact closed family valid for **all** lengths is
\[
\operatorname{spr}(K_n^{[\ell]})=\frac{\ell(\ell+2)}{12}+\frac{\lfloor n^2/4\rfloor}{n^2}(\ell+1)^2. \tag{4}
\]
Its complete maximizing configurations consist, modulo common translation and global sign, of two classes whose sizes differ by at most one: the smaller-valued cores and their paths decrease with unit increments, while the larger-valued cores are exactly one unit above and their paths increase with unit increments.

## Assumptions and scope
A connected simple graph \(G=(V,E)\) has \(|V|=n\ge2\) and unweighted graph distance; its diameter is \(\Delta\ge1\). In \(G^{[\ell]}\), each \(v\in V\) is the root of a new path \((v,0),(v,1),\ldots,(v,\ell)\), with \((v,0)=v\). All core edges and pendant edges have length one. Every one of the \(n(\ell+1)\) vertices has weight \(1/[n(\ell+1)]\). All functions are real-valued. The spread is the maximum of the variance over functions satisfying \(|f(x)-f(y)|\le1\) on every edge.

Let \(\mathcal L_G\) be the compact polytope of core potentials \(c_v\) with \(|c_v-c_w|\le1\) on core edges and with one chosen coordinate fixed at zero. Let \(\mathcal E_G\) denote its finite vertex set. Incidence-matrix total unimodularity implies all \(c\in\mathcal E_G\) have integer coordinates. For vectors indexed by \(V\), define \(\operatorname{Var}_G(c)=n^{-1}\sum(c_v-\bar c)^2\) and \(\operatorname{Cov}_G(c,e)=n^{-1}\sum(c_v-\bar c)(e_v-\bar e)\).

Let \(\mathcal B_n\) be the set of vectors \(e\in\{-1,1\}^n\) satisfying \(|\sum e_v|=\kappa\), where \(\kappa=0\) for even \(n\) and \(1\) for odd \(n\). Put
\[
\beta_G=\max_{e\in\mathcal B_n,\ c\in\mathcal E_G}\operatorname{Cov}_G(c,e),\qquad
\gamma_G=\max\{\operatorname{Var}_G(c): e\in\mathcal B_n,\ c\in\mathcal E_G,\ \operatorname{Cov}_G(c,e)=\beta_G\}.
\]
These quantities are exact rationals with denominator dividing \(n^2\). The distance \(W_1\) below is the transportation cost of **equal finite measures**, not necessarily probability measures.

## Proof
**1. Every attached path is straight at an optimum.** For a fixed root \(v\), write its path values \(z_0,\ldots,z_\ell\), with \(z_0=c_v\). The pairwise variance identity gives
\[
\operatorname{Var}_{0\le t\le\ell}(z_t)
=\frac1{2(\ell+1)^2}\sum_{s,t}(z_s-z_t)^2
\le\frac1{2(\ell+1)^2}\sum_{s,t}(s-t)^2
=\frac{\ell(\ell+2)}{12}.
\]
Equality requires \(|z_s-z_t|=|s-t|\) for all pairs, hence \(z_t=c_v+e_v t\) with one \(e_v\in\{-1,1\}\). The path mean \(\mu_v\) necessarily belongs to \([c_v-\ell/2,c_v+\ell/2]\), since \(|z_t-c_v|\le t\). The law of total variance across the \(n\) equal-sized paths gives
\[
\operatorname{Var}_{G^{[\ell]}}f=\frac1n\sum_v\operatorname{Var}_{0\le t\le\ell}(f(v,t))+\operatorname{Var}_G(\mu).
\]
For fixed \(c\), \(\operatorname{Var}_G(\mu)\) is strictly convex in each \(\mu_v\) separately when \(n\ge2\): its quadratic coefficient is \((n-1)/n^2>0\). Therefore its maximum on the product of allowed intervals occurs with each \(\mu_v=c_v+e_v\ell/2\). Choosing all the corresponding straight paths simultaneously realizes both upper bounds; conversely every global maximizer must attain the path-variance upper bound on each path, so must be straight.

**2. Finite core-potential reduction.** For every sign vector \(e\), the map \(c\mapsto\operatorname{Var}_G(c+\ell e/2)\) is strictly convex after one core value is fixed. Its maximum on \(\mathcal L_G\) therefore occurs at a vertex, and every maximizing anchored core potential is a vertex. Expansion proves (1) exactly, for every integer \(\ell\ge1\). Each core vertex has integral coordinates because its active constraints are differences of incident coordinates with right-hand side \(\pm1\), and the reduced edge-incidence matrix is totally unimodular.

**3. Eventual exact quadratic with a uniform cutoff.** For \(e\in\{-1,1\}^n\) put \(s=|\sum e_v|\). The leading coefficient of \(\operatorname{Var}_G(c+\ell e/2)\) is \((1-s^2/n^2)/4\). Its maximum \(a_n\) occurs exactly for \(s=\kappa\); any other sign vector loses at least \(1/n^2\) in this coefficient. If \(c\) is 1-Lipschitz on a graph of diameter \(\Delta\), then \(\operatorname{Var}_G(c)\le\Delta^2/4\) and Cauchy–Schwarz gives \(|\operatorname{Cov}_G(c,e)|\le\Delta/2\). Hence the best balanced candidate beats every unbalanced candidate whenever
\[
\frac{\ell^2}{n^2}>\Delta\ell+\frac{\Delta^2}{4}.
\]
For balanced pairs, integral core vertices imply \(\operatorname{Cov}_G(c,e)\in n^{-2}\mathbb Z\). Any balanced pair whose covariance falls below \(\beta_G\) loses at least \(\ell/n^2\), which dominates the entire possible gain \(\Delta^2/4\) in the constant term once \(\ell/n^2>\Delta^2/4\). Both inequalities hold strictly for every \(\ell\ge n^2(\Delta+1)^2\). Thus only balanced pairs of maximum covariance, and then of maximum core variance, survive; expansion together with the common within-path variance proves (2).

**4. The transport coefficient.** For balanced \(e\), put \(\bar e=n^{-1}\sum e_v\) and define equal-mass nonnegative measures on \(V\) by
\[
\nu_e^+=\frac{1-\bar e}{n}\sum_{e_v=1}\delta_v,\qquad
\nu_e^-=\frac{1+\bar e}{n}\sum_{e_v=-1}\delta_v.
\]
Their signed difference is \(n^{-1}\sum_v(e_v-\bar e)\delta_v\). Finite Kantorovich–Rubinstein duality gives \(\max_{c\in\mathcal L_G}\operatorname{Cov}_G(c,e)=W_1(\nu_e^+,\nu_e^-)\). Hence \(\beta_G=\max_{e\in\mathcal B_n}W_1(\nu_e^+,\nu_e^-)\). For even \(n\), writing the two half-partitions as uniform probability measures \(\rho_+,\rho_-\), this becomes \(\beta_G=\frac12\max W_1(\rho_+,\rho_-)\).

**5. Sharp extreme-core bounds.** Since every function 1-Lipschitz on \(K_n\) is also 1-Lipschitz on \(G\), \(\beta_G\ge\beta_{K_n}\). For the clique choose the largest \(\lceil n/2\rceil\) values at 1 and the remainder at 0, with matching signs; the covariance is \(\beta_{K_n}=2\lfloor n^2/4\rfloor/n^2\). Conversely, for any core \(G\), sort \(c_1\le\cdots\le c_n\). Connectedness forces \(c_{j+1}-c_j\le1\): every cut of the sorted vertices has at least one edge crossing it and the values of its endpoints differ by at least this gap. For a fixed \(c\), maximizing over balanced signs puts the positive signs at one end of the sorted order. Writing the resulting covariance as a linear combination of consecutive gaps produces **nonnegative coefficients**; replacing every gap by 1 can only increase it. On \(c_j=j-1\), its exact value is \(\lfloor n^2/4\rfloor/n\). All those gap coefficients are strictly positive when \(n\ge2\), so equality forces all gaps to equal 1. An edge can then only join consecutive levels. Connectivity on \(n\) distinct levels forces the entire graph to be the path \(P_n\). Conversely the path realizes \(c_j=j-1\). This proves (3) and the upper equality classification.

**6. Unique eventual maximizing core at fixed order.** For a nonpath \(G\) on \(n\ge3\) vertices, strictness in step 5 plus the denominators dividing \(n^2\) give \(\beta_{P_n}-\beta_G\ge1/n^2\). The exact quadratic (2) holds for both cores whenever \(\ell\ge n^2(n+1)^2\), because both diameters are at most \(n-1\). Their leading coefficients agree, while the difference between their constants \(\gamma\) is at least \(-(n-1)^2/4\). The strictly positive difference \(\ell/n^2-(n-1)^2/4\) proves that the hairy path uniquely maximizes spread among all connected size-\(n\) cores at the stated cutoff.

**7. All-length clique formula and its equality cases.** For a clique core, all branch means lie in a single interval of length at most \(\ell+1\). Applying the discrete range-variance bound to the \(n\) branch means gives at most \(\lfloor n^2/4\rfloor(\ell+1)^2/n^2\). This is attained by splitting the cores into two classes as equally as possible, assigning the lower class core value 0 and straight paths \(-t\), and the upper class core value 1 and straight paths \(1+t\). Equality in the path-variance bound forces all paths straight; equality in the range-variance bound forces both classes to occupy their interval endpoints, with their sizes differing by at most one. Since the class means differ by \(\ell+1\), the core values must differ by 1 and their path directions point outward. This proves (4) and the complete optimizer description.

## Verification
The attached standalone file `check.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. Run `python check.py`. It independently enumerates signed increments on **all** attached paths in seven small test families and checks them against the reduced core-potential optimization; it also tests thirty clique closed-form values, six exact path transport coefficients and fifteen eventual-polynomial identities. These checks corroborate, but do not replace, the infinite proofs above. Integer potential enumeration in the checker uses all feasible integer-valued core functions, which is sufficient for these finite tests but does **not** purport to enumerate every continuous Lipschitz function.

## Relationship to prior work
Alon–Boppana–Spencer introduced graph spread; Addario-Berry, Janson and McDiarmid (arXiv:0902.1156, initial public posting 2009-02-06) studied random graphs and discuss integral extremizers and pendant trees in barely supercritical random graphs. Their Section 4 treats random decoration sizes and lower bounds, not an exact deterministic equal-path transfer law, balanced transport coefficient or fixed-core-order extremum. Sammer and Tetali's *Concentration on the Discrete Torus Using Transportation* (2009) relates spread to transportation and proves cycle concentration results; it does not state this rooted-path blow-up. Barthe and O'Connell's *Matchings and the variance of Lipschitz functions* (2009) concerns Gaussian and uniform-ball distributions rather than finite graph coronas. The transport duality used in step 4 is classical; the claimed contribution is the exact graph operation law, the eventual polynomial and its sharp extremal slope, not the duality itself. See limitations for residual originality uncertainty.

## Limitations
All statements require connected unweighted simple core graphs, equally long independent pendant paths, uniform weights on **all** vertices, real functions and quadratic variance. The effective length bound is sufficient, not claimed optimal; for a given core, stabilization may occur earlier. The transport coefficient measures an optimal balanced partition but is not automatically equal to the original core spread. No result is asserted for unequal arm lengths, weighted vertices, arbitrary tree-shaped decorations, sub-Gaussian (rather than variance) constants, or random graph limits. Equivalent proofs in unindexed literature cannot be excluded; a relevant article about Lipschitz variance and matchings was checked at abstract level only.

## References
- L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, initial public arXiv posting 2009-02-06, arXiv:0902.1156, https://arxiv.org/abs/0902.1156 .
- M. Sammer, P. Tetali, *Concentration on the Discrete Torus Using Transportation*, Combinatorics, Probability and Computing 18 (2009), 835–860, doi:10.1017/S0963548309990319, https://tetali.math.gatech.edu/PUBLIS/torus_Jun3.pdf .
- F. Barthe, N. O'Connell, *Matchings and the variance of Lipschitz functions*, ESAIM: Probability and Statistics 13 (2009), 400–408, doi:10.1051/ps:2008018, https://www.numdam.org/articles/10.1051/ps:2008018/ .
