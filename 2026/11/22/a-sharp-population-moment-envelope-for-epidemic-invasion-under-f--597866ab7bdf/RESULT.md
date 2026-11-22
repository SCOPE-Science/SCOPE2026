# A sharp population-moment envelope for epidemic invasion under fixed-budget community mixing

## Finding

Consider an arbitrary finite number \(m\ge2\) of epidemiological communities with positive population fractions \(p_1,\ldots,p_m\) summing to one. When all groups have the same positive mean susceptibility–transmissibility product and the *population-wide* contact budget is held fixed, the random-mixing contact pattern is a universal minimizer of the linearized SIR reproduction number. It is the **unique** minimizer if and only if not all community fractions are equal. In this unequal-size case, both negative and positive departures from random mixing raise the reproduction number strictly, and the increase has an explicit second-order coefficient determined by the second and third population-share moments.

More precisely, define \(s_k=\sum_{i=1}^m p_i^k\), \(v=s_3/s_2^2-1\), and \(c>0\) as the well-mixed reproduction number. For every admissible community-preference parameter \(-s_2/(1-s_2)\le e\le1\), the reproduction number \(R(e)\) satisfies
\[
R(e)\ge c,
\qquad
R(e)=c\left(1+ve^2+O(e^3)\right)\quad(e\to0).
\]
If the fractions are unequal, the inequality is strict for every \(e\ne0\), \(v>0\), and \(R(e)\) strictly decreases on the negative side and strictly increases on the positive side. If all fractions equal \(1/m\), then \(R(e)=c\) throughout the admissible range.

There is also a **sharp moment envelope** valid away from the perturbative regime. For unequal fractions put
\[
t=\frac{s_4-2s_2s_3+s_2^3}{s_2(s_3-s_2^2)}.
\]
Then
\[
\boxed{\frac{R(e)}c\ge\frac{1+et+\sqrt{(1-et)^2+4e^2v}}2.}
\]
At \(e\ne0\), equality holds **if and only if** the community fractions assume at most two distinct values, even for arbitrarily many communities. This is a sharp bound expressed using only \(s_2,s_3,s_4\), with a rigid equality class.

A two-community instance shows that the phenomenon can reverse the linearized epidemic invasion verdict without changing either the budget or biological parameters. With fractions \(p=(4/5,1/5)\), \(c=19/20\), and the same contact budget at each setting,
\[
R(-1)=\frac{19(9+\sqrt{769})}{680}>1,\qquad
R(0)=\frac{19}{20}<1,\qquad
R(3/4)=\frac{19(23+\sqrt{202})}{680}>1.
\]
Both extremal example settings have strictly positive between-community contact rates and generate irreducible next-generation matrices. Here \(e=-1\) is permitted because the unequal communities make the admissible lower endpoint \(-17/8\).

## Assumptions and scope

Let \(m\ge2\), \(p_i>0\), \(\sum_i p_i=1\). Consider a large-population planted-partition contact model in which the probability of a potential edge between an individual in group \(i\) and an individual in group \(j\) is asymptotically \(\kappa a_{ij}(e)/N\), where \(\kappa>0\) is the fixed population-wide expected mean degree and
\[
a_{ij}(e)=(1-e)+\frac{e}{s_2}\mathbf 1_{i=j}.
\]
Equivalently \(a_{ii}=1+\alpha e\), \(a_{ij}=1-e\) for distinct groups, and \(\alpha=(1-s_2)/s_2\). The allowed closed interval \(I=[-s_2/(1-s_2),1]\) ensures all edge intensities are nonnegative; statements about finite \(N\) require the edge probabilities to be at most one. The population-average intensity is identically \(\sum_{ij}p_ip_ja_{ij}(e)=1\), so this parameter change reallocates contacts and does not change their total expected number in the leading large-\(N\) normalization.

Assume a continuous-time SIR linearization with mass-action infection on existing edges, baseline transmission rate \(\beta>0\), common exponential infectious removal rate \(\gamma>0\), and a common positive mean product \(q=\mathbb E_i[\delta\varepsilon]>0\) across all groups, for transmissibility \(\delta\) and susceptibility \(\varepsilon\). Homogeneous unit traits are a sufficient special case. The reduced next-generation matrix acting on the group infection modes is
\[
K_{ij}(e)=c\,p_j a_{ij}(e),\qquad c=\frac{\beta\kappa q}{\gamma}.
\]
This formulation is the large-population heterogeneous-mean-field *invasion* criterion, not a finite-population outbreak-probability identity. \(R(e)=\rho(K(e))\) is the reproduction number of this reduced model. The equality and sharpness statements refer to this precisely specified family, not to arbitrary degree-preserving mixing matrices or all compartmental epidemic models.

## Proof

**1. Budget, symmetrization, and the universal trial vector.** The contact normalization is
\[
\sum_{ij}p_ip_ja_{ij}(e)=(1-e)+\frac e{s_2}\sum_i p_i^2=1.
\]
Let \(u_i=\sqrt{p_i}\), \(D=\operatorname{diag}(p_1,\ldots,p_m)\). The positive diagonal similarity \(\operatorname{diag}(\sqrt p)K(e)\operatorname{diag}(1/\sqrt p)\) equals \(cS(e)\), where
\[
S(e)=(1-e)uu^T+\frac e{s_2}D=uu^T+eB,\quad B=\frac D{s_2}-uu^T.
\]
The matrix \(S(e)\) is symmetric, entrywise nonnegative on \(I\), and has the same eigenvalues as \(K(e)/c\). Therefore its largest algebraic eigenvalue is its spectral radius. We have \(\|u\|=1\) and \(u^TS(e)u=1\) for all \(e\). Rayleigh–Ritz gives \(\rho(S(e))\ge1\). For \(e\ne0\), equality would make \(u\) a top eigenvector, but
\[
B u=\left((p_i/s_2-1)\sqrt{p_i}\right)_{i=1}^m.
\]
This vector vanishes exactly when every \(p_i=s_2\), equivalent (because shares sum to one) to equal community sizes. Thus the lower bound is strict for all nonuniform shares and nonzero \(e\). With uniform shares, \(S(e)=uu^T+e(I-uu^T)\); its eigenvalues are \(1\) and \(e\), and \(e\le1\), so \(R(e)=c\).

**2. Convexity, strict one-sided monotonicity, and the perturbation coefficient.** Since \(S(e)\) is affine symmetric, \(\lambda_{\max}(S(e))\), the supremum of affine Rayleigh quotients, is convex in \(e\). It has the unique global minimum at \(e=0\) when fractions are unequal. For any \(e_1<e_2<0\), writing \(e_2\) as a nontrivial convex combination of \(e_1\) and \(0\) proves \(R(e_1)>R(e_2)\); the positive side follows similarly. At \(e=0\), \(S(0)=uu^T\) has simple top eigenvalue 1 and all remaining eigenvalues zero. Ordinary isolated-eigenvalue perturbation therefore applies. As \(u^TBu=0\), the linear coefficient is zero and the quadratic coefficient equals \(\|Bu\|^2\), namely
\[
\|Bu\|^2=\sum_i p_i(p_i/s_2-1)^2=\frac{s_3}{s_2^2}-1=v.
\]
Cauchy–Schwarz yields \(s_3\ge s_2^2\), with equality precisely for uniform shares.

**3. Sharp moment envelope and its equality class.** Suppose the shares are unequal, so \(v>0\), and set \(w=Bu/\sqrt v\). Then \(u,w\) are orthonormal. Compression of \(S(e)\) to their span gives exactly
\[
\begin{pmatrix}1&e\sqrt v\\e\sqrt v&et\end{pmatrix},
\quad
 t=w^TDw/s_2=\frac{s_4-2s_2s_3+s_2^3}{s_2(s_3-s_2^2)}.
\]
The larger eigenvalue of this \(2\times2\) matrix is the displayed moment envelope. The variational principle makes it a lower bound on the largest eigenvalue of the full \(S(e)\).

If there are exactly two different share values, the span of \(u,w\) is precisely the subspace of vectors whose entries are proportional to \(\sqrt{p_i}\) with coefficients constant on each equal-share class; it is invariant under \(D\) and \(uu^T\). For \(e<1\), the strictly positive off-diagonal entries make \(S(e)\) irreducible; its Perron eigenvector is invariant under permutations within equal-share classes and hence lies in that span. At \(e=1\), an eigenvector supported uniformly on a largest-share class also lies in the span. Thus equality holds for every admissible \(e\) if there are exactly two distinct share values.

Conversely, suppose \(e\ne0\) and the compression bound is equality. A unit top Ritz vector \(x=A u+C w\) must be a true top eigenvector. Since the compressed off-diagonal term is \(e\sqrt v\ne0\), its \(w\) coefficient satisfies \(C\ne0\). The eigenvector equation then requires \(Dx\) to belong to \(\operatorname{span}(u,w)\). Dividing coordinates by \(\sqrt{p_i}>0\), this says a genuinely quadratic polynomial of \(p_i\) agrees with a linear polynomial at every distinct share value. It cannot hold at three or more distinct values. Hence equality is possible only if there are at most two distinct shares. This establishes the claimed rigidity, including \(e=1\).

**4. Exact two-sided threshold reversal.** For \(p=(4/5,1/5)\), direct rational evaluation yields \(s_2=17/25\), \(v=36/289\), \(t=8/17\). Since there are only two distinct shares, the moment envelope is an identity:
\[
\frac{R(e)}c=\frac{1+(8/17)e+\sqrt{(1-(8/17)e)^2+(144/289)e^2}}2.
\]
Substituting \(c=19/20\) and \(e=-1,0,3/4\) yields the three displayed values. The strict greater-than-one inequalities follow from \(\sqrt{769}>27\) and \(\sqrt{202}>14\). Both \(-1\) and \(3/4\) lie strictly between the admissible endpoints and have positive within- and between-group edge intensities.

## Verification

The included standalone \(verify.py\), using NumPy and SymPy, checks the displayed rational quantities, the exact quadratic radical eigenvalues and the three threshold inequalities, then tests 4,400 random finite-group spectral comparisons and 3,216 moment-envelope comparisons. These are independent finite sanity checks of formulas; correctness for all \(m\) and all real parameters rests on the proof above. Run \(python verify.py\) with Python 3, NumPy and SymPy installed. The provided program requires no input files or remote services.

## Relationship to prior work

Gupta and Landry (2026), Eqs. (28)–(32) and their discussion of imbalanced communities, derive the two-community mean-field infection threshold with correlated biological traits and a globally fixed expected contact degree. Their paper also observes that unequal community sizes can affect reproduction numbers. Those observations and formulas are credited, and neither the two-community forward matrix nor the general phenomenon of contact-structure sensitivity is claimed as new. The contribution assessed here is the all-finite-community fixed-budget spectral ordering, the explicit moment-curvature law and especially the global sharp three-moment envelope with its exact two-share-value equality classification; the two-sided threshold witness illustrates the latter.

Landry and Restrepo (2023) set up the fixed-budget planted-partition normalization for two communities and analyze higher-order SIS opinion-disparity equilibria; their model does not present this multi-community SIR spectral moment envelope. Hill, Glasser and Feng (2023) rederive increasing reproduction numbers under *positive* Jacquez preferential mixing with **fixed per-group activity rates**, whereas the present intervention preserves only the global edge budget and allows group-specific degrees to change, including negative within-group preference. Consequently that monotonicity theorem neither provides the two-sided minimum nor the exact moment envelope here. Published research records on commuter optimization and two-class contact-rate allocation likewise optimize different feasible sets, not this all-group contact-family envelope.

## Limitations

The theorem is a deterministic heterogeneous-mean-field invasion statement and does not prove finite-size stochastic major-outbreak probabilities, nonlinear final epidemic sizes or intervention efficacy in empirical networks. The model fixes the population-wide mean degree, not the degree of each community. The moment envelope need not be attained for three or more distinct shares, though it is the exact compression bound and is attained for any configuration with two share values. The independence of infectious traits across edges and common groupwise product are part of the reduction; different biological moments or degree-preserving rewiring need separate analysis. Historical priority remains subject to independent scholarly assessment; no independent audit has been performed.

## References

1. Abhay Gupta and Nicholas W. Landry, *The interplay of network structure and correlated infectious traits in epidemic models*, arXiv:2605.12773, first version May 12, 2026. https://arxiv.org/abs/2605.12773
2. Nicholas W. Landry and Juan G. Restrepo, *Opinion disparity in hypergraphs with community structure*, Physical Review E 108, 034311 (2023), DOI:10.1103/PhysRevE.108.034311. https://nwlandry.com/assets/docs/publications/2023_PhysRevE_opinion.pdf
3. Andrew N. Hill, John W. Glasser and Zhilan Feng, *Implications for infectious disease models of heterogeneous mixing on control thresholds*, Journal of Mathematical Biology 86, 53 (2023), DOI:10.1007/s00285-023-01886-9. https://pmc.ncbi.nlm.nih.gov/articles/PMC9993378/
