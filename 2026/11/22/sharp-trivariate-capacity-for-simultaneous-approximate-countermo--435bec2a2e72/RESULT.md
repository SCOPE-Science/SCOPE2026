# Sharp trivariate capacity for simultaneous approximate countermonotonicity

## Finding
Let \(U_1,U_2,U_3\) have standard-uniform one-dimensional marginal laws on \([0,1]\); their joint dependence may be arbitrary, including singular. For every \(\varepsilon\ge0\), define the simultaneous approximate-antithetic event
\[
E_{\varepsilon}=\bigcap_{1\le i<j\le3}\{|U_i+U_j-1|\le\varepsilon\}.
\]
Then the exact, attained three-marginal copula capacity is
\[
\boxed{\sup_{\mathcal L(U_1,U_2,U_3)}\Pr(E_{\varepsilon})=\min\{3\varepsilon,1\}.}
\]
The supremum is over all Borel joint laws with all three marginals uniform on \([0,1]\). In particular, a coupling satisfying all three inequalities almost surely exists precisely when \(\varepsilon\ge1/3\); for smaller positive tolerance the optimal joint success probability is \(3\varepsilon\), not merely an upper bound.

## Assumptions and scope
There are exactly three continuous, individually standard-uniform coordinates. No independence, exchangeability, absolute continuity, or pairwise copula restrictions are assumed. The reference sum is \(1\) for every pair; the same absolute tolerance \(\varepsilon\) is used for all three pairs. The result concerns the probability of simultaneous pair constraints, not a single bivariate sum distribution. For each fixed tolerance the optimizing coupling can depend on that tolerance.

## Proof
**1. Universal bound.** Put \(X_i=U_i-1/2\). On \(E_{\varepsilon}\), every \(|X_i+X_j|\le\varepsilon\). For every permutation \((i,j,k)\) of \((1,2,3)\),
\[
2X_i=(X_i+X_j)+(X_i+X_k)-(X_j+X_k),
\]
so \(|X_i|\le3\varepsilon/2\). Consequently \(E_{\varepsilon}\) is contained in the interval-projection event \(\{|U_1-1/2|\le3\varepsilon/2\}\). Uniformity of \(U_1\) yields
\[
\Pr(E_{\varepsilon})\le\min\{3\varepsilon,1\}.
\]
This also covers \(\varepsilon=0\): the candidate event forces \(U_1=1/2\), a null event.

**2. A normalized coupling supported inside all three slabs.** Let \(A\) be uniform on \([1,3/2]\), let \(S\) be an independent fair sign, and let \(\Pi\) be an independent uniformly random permutation of three entries. Construct \(V=(V_1,V_2,V_3)\) by permuting
\[
S\,(A,\,1-A,\,A-2).
\]
Before permutation its three pair sums are \(S\), \(S(2A-2)\), and \(-S\); because \(1\le A\le3/2\), every pair sum has absolute value at most \(1\). The sign and the permutation preserve that assertion.

Each of the six sign-and-position component laws is uniform on one half-unit interval, and the six intervals are exactly
\[
[-3/2,-1],\ [-1,-1/2],\ [-1/2,0],\ [0,1/2],\ [1/2,1],\ [1,3/2].
\]
Because the sign and coordinate position are equally likely, each interval has weight \(1/6\) and conditional density \(2\), giving the constant marginal density \(1/3\) on \([-3/2,3/2]\). Thus, for each coordinate,
\[
V_i\sim\operatorname{Unif}[-3/2,3/2],\qquad |V_i+V_j|\le1\ \text{a.s.}
\]

**3. Embed the central portion of the marginal distributions.** Fix \(0<\varepsilon\le1/3\), and put
\[
W_i=\tfrac12+\varepsilon V_i,\qquad I_{\varepsilon}=[\tfrac12-\tfrac32\varepsilon,\tfrac12+\tfrac32\varepsilon].
\]
Each \(W_i\) is uniform on \(I_{\varepsilon}\), an interval of length \(3\varepsilon\), and every pair satisfies \(|W_i+W_j-1|\le\varepsilon\) almost surely. Let \(B\) be independent Bernoulli with \(\Pr(B=1)=3\varepsilon\). On \(B=1\), set \(U=W\). If \(3\varepsilon<1\), on \(B=0\) let the three \(U_i\) be independently uniform on \([0,1]\setminus I_{\varepsilon}\); when \(3\varepsilon=1\) the second branch is absent.

The marginal density contributed by \(B=1\) equals \((3\varepsilon)/(3\varepsilon)=1\) on \(I_{\varepsilon}\), and the marginal density contributed by \(B=0\) equals \((1-3\varepsilon)/(1-3\varepsilon)=1\) on its complement. Hence every \(U_i\) is uniform on \([0,1]\). On \(B=1\) the event \(E_{\varepsilon}\) occurs surely. Conversely, the universal projection constraint from Step 1 makes \(E_{\varepsilon}\) impossible on \(B=0\), where every coordinate lies outside \(I_{\varepsilon}\). Therefore
\[
\Pr(E_{\varepsilon})=\Pr(B=1)=3\varepsilon.
\]
At \(\varepsilon=1/3\), the successful branch already has standard-uniform marginals and probability one. For every \(\varepsilon>1/3\) this same coupling remains successful, because the event increases with tolerance. Together with the zero-tolerance case and Step 1, this proves the exact formula and attainment for every \(\varepsilon\ge0\). \(\square\)

## Verification
The self-contained standard-library program `checker.py` tests the construction in exact rational arithmetic. Run `python3 checker.py` from the directory containing the two files. The program verifies the six-interval marginal partition, the extreme affine pair-sum inequalities, the mixture marginal-density identities, and rational sample realizations for five tolerances in \((0,1/3]\). It reports `PASS: 1891 exact rational assertions/groups`. These finite computations check the construction; the preceding algebraic and measure-theoretic proof establishes the continuum statement.

## Relationship to prior work
Chaudhary and Khandelwal (arXiv:2610.24197, first publicly available October 16, 2026) characterize attainable laws for the sum of **two** dependent uniform variables using joint tail bounds and lattice couplings. Their statement does not impose the three simultaneous, mutually incompatible near-complementarity conditions above. Separate pairwise attainability cannot imply joint attainability: all three pairs can separately have sum exactly \(1\), whereas simultaneous equality for three standard-uniform marginals has probability zero.

Omladič, Vuk and Zalar (arXiv:2611.14008, first publicly available November 10, 2026) analyze **finite pointwise** copula interpolation and copula-sandwich feasibility via finite grids. They do not give the optimal mass of this continuum-defined intersection of three pair-sum slabs. Their feasibility results and the present sharp event-probability calculation address different constraints.

Lauzier, Lin and Wang (arXiv:2302.11701) study qualitative pairwise countermonotonicity and the restrictive nature of perfect negative dependence in higher dimensions. Lee, Cheung and Ahn (2017) analyze multivariate countermonotonicity and minimal copulas under concordance order, a different extremal dependence notion. These illuminate the zero-tolerance obstruction but neither supplies the positive-tolerance coefficient \(3\), the threshold \(1/3\), or the attaining measure-preserving construction. In particular, this result does not assert pairwise countermonotonicity of the constructed marginals: it concentrates a controllable fraction of probability close to that impossible three-way condition.

## Limitations
The theorem is specific to exactly three standard-uniform marginals and a common target sum. It does not classify all optimizing copulas or extend the sharp coefficient to arbitrary marginal laws, pair-specific tolerances, or a larger odd cycle. The displayed optimizer is not generally absolutely continuous: its successful component lies on a finite union of line segments. The assertion of priority is provisional and subject to unlocated specialized optimal-transport or copula-capacity literature. Computational checks are finite supporting evidence, not independent validation of the continuum theorem.

## References
1. P. Chaudhary and K. Khandelwal, *Sums of two dependent uniform random variables: a characterization by joint tail bounds*, arXiv:2610.24197, first submitted 2026-10-16. https://arxiv.org/abs/2610.24197
2. M. Omladič, M. Vuk and A. Zalar, *A linear programming approach to finite copula interpolation*, arXiv:2611.14008, first submitted 2026-11-10. https://arxiv.org/abs/2611.14008
3. J. Lauzier, L. Lin and R. Wang, *Pairwise counter-monotonicity*, arXiv:2302.11701. https://arxiv.org/abs/2302.11701
4. W. Lee, K. C. Cheung and J. Y. Ahn, *Multivariate countermonotonicity and the minimal copulas*, Journal of Computational and Applied Mathematics 317 (2017), 589–602. https://doi.org/10.1016/j.cam.2016.12.032
