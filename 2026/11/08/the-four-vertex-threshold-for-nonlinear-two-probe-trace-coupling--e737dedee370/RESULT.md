# The four-vertex threshold for nonlinear two-probe trace coupling

## Finding

For a real symmetric matrix \(B\in\mathbb R^{n\times n}\), let \(Z,Z'\in\{-1,1\}^n\) each have the uniform product Rademacher law, with arbitrary dependence between them. Consider the unbiased two-query trace estimator
\[
H_B(Z,Z')=\frac{Z^{\mathsf T}BZ+{Z'}^{\mathsf T}BZ'}{2}.
\]
A *fixed sign-flip coupling* has \(Z'=s\odot Z\) for a deterministic \(s\in\{-1,1\}^n\). The following is an exact dimension threshold and complete homogeneous-graph family calculation:

1. For every real symmetric \(B\) of size \(n\le3\), a fixed sign-flip coupling attains the minimum variance among all admissible joint laws. This assertion includes arbitrary signed off-diagonal entries and all repeated response values.
2. For the zero-diagonal adjacency matrix \(A_n\) of the unweighted complete graph on \(n\ge4\) vertices, **every** fixed sign-flip coupling is strictly suboptimal. The best sign flip changes \(\lfloor n/2\rfloor\) coordinates, and its estimator variance is
\[
V_{\mathrm{flip}}(n)=4\left[\binom n2-\left\lfloor\frac{n^2}{4}\right\rfloor\right].
\]
To specify the globally optimal variance exactly, form the increasing list \(L_1,\ldots,L_{2^n}\) by taking, for each \(j=0,\ldots,n\), the integer
\[
x_j=\frac{(n-2j)^2-n}{2}
\]
with multiplicity \(\binom nj\), and sorting all resulting values. Then
\[
\boxed{V_*(n)=2\binom n2+\frac{2}{2^n}\sum_{i=1}^{2^n}L_iL_{2^n+1-i}<V_{\mathrm{flip}}(n)\quad(n\ge4).}
\]
The list can be processed by matching cumulative binomial masses in \(O(n)\) arithmetic operations; enumerating \(2^n\) sign vectors is unnecessary.
3. On four vertices the exact variances for independent probes, the optimal fixed flip, and the unrestricted optimal coupling are respectively
\[
\boxed{V_{\mathrm{ind}}(4)=12,\qquad V_{\mathrm{flip}}(4)=8,\qquad V_*(4)=6.}
\]
Thus four vertices are the **smallest possible matrix dimension** for a strict nonlinear-over-fixed-flip improvement, and the additional improvement on this unweighted witness is \(25\%\) relative to the best fixed flip.
4. The all-dimensional gap persists asymptotically. With \(\Phi\) denoting the standard normal cumulative distribution function, define
\[
q(u)=\frac12\left[\bigl(\Phi^{-1}((1+u)/2)\bigr)^2-1\right],\qquad 0<u<1.
\]
Then the exact limiting variance ratio is
\[
\boxed{\lim_{n\to\infty}\frac{V_*(n)}{V_{\mathrm{flip}}(n)}=1+2\int_0^1q(u)q(1-u)\,du\ \approx\ 0.5606716095.}
\]
The displayed decimal is a numerical evaluation of the specified convergent integral, not an independently certified decimal enclosure.

## Assumptions and scope

All dimensions are finite and \(n\ge1\). Every individual probe must be uniform on the *entire* discrete cube, hence its coordinates are internally independent fair signs. The two probes may have arbitrary dependence. All variances refer to the unbiased two-query average at one fixed, known matrix, without a low-rank pilot, alternate probe marginals, or adaptive matrix-vector queries. Entries of \(B\) are real. The complete-graph result uses the symmetric zero-diagonal matrix with every off-diagonal entry equal to \(1\); adding any diagonal matrix changes the estimator by a deterministic constant and therefore leaves its variance unchanged.

## Proof

**1. Reduction to scalar optimal coupling.** Write \(X(z)=\sum_{i<j}B_{ij}z_iz_j\). Then \(z^{\mathsf T}Bz=\operatorname{tr}(B)+2X(z)\), and \(H_B-\operatorname{tr}(B)=X(Z)+X(Z')\). Any admissible joint law induces two copies of the same scalar distribution of \(X\). Conversely, every coupling of that scalar distribution lifts to a coupling of *uniform sign vectors*: conditionally on each scalar value, independently sample a sign vector uniformly from its finite fibre. Because the two scalar marginals are correct, both resulting vector marginals are uniform. The rearrangement inequality (or its elementary two-point swap proof) says that \(\mathbb E[XX']\) is minimized by pairing the increasing and decreasing quantiles. Indeed if \(a<b\) and \(c<d\), changing positive mass from the pairs \((a,c),(b,d)\) to \((a,d),(b,c)\) reduces the sum of products by the positive quantity \((b-a)(d-c)\) per mass unit. Finite repeated values pose no difficulty.

**2. All matrices of dimension at most three.** For \(n=1\) the quadratic response is constant. For \(n=2\) its two equally probable responses are paired oppositely by flipping exactly one sign. For \(n=3\), the response is invariant under global sign reversal, so the eight sign vectors form four equally probable classes under \(z\sim-z\). The quotient group \(\{-1,1\}^3/\{\pm(1,1,1)\}\) is a four-element elementary abelian group. The countermonotone pairing of its four equally weighted response values, after any chosen tie-breaking, is a perfect matching of the four classes. Every perfect matching of four points is translation by exactly one of the three nonidentity elements of this quotient group. That translation is implemented by a fixed coordinate sign flip. Hence a fixed flip realizes a globally minimizing pair distribution for any signed entries, including ties.

**3. Exact complete-graph variances.** Set
\[
X_n(z)=\sum_{i<j}z_iz_j=\frac{S_n^2-n}{2},\qquad S_n=\sum_i z_i.
\]
The random variable \(S_n=n-2J\) with \(J\sim\mathrm{Binomial}(n,1/2)\); this gives the stated binomial multiset of response values. Orthogonality of the distinct degree-two sign products gives \(\mathbb E X_n=0\) and \(v_n=\operatorname{Var}(X_n)=\binom n2\). The scalar rearrangement argument from Step 1 gives \(c_n=2^{-n}\sum_iL_iL_{2^n+1-i}\), so the estimator variance is \(V_*(n)=2(v_n+c_n)\).

If exactly \(k\) signs are flipped, each of the \(\binom n2\) pair products has covariance \(+1\) with its partner when the edge has both or neither endpoints flipped, and covariance \(-1\) when exactly one endpoint is flipped. There are precisely \(k(n-k)\) edges of the latter kind. Thus
\[
\operatorname{Cov}(X_n(Z),X_n(s\odot Z))=v_n-2k(n-k),
\]
and the estimator variance is \(4(v_n-k(n-k))\). Maximizing \(k(n-k)\) gives the fixed-flip formula.

**4. Strictness in every dimension at least four.** It suffices to defeat the best fixed flip. Because global reversal of \(s\) leaves the quadratic response unchanged, take its flip set of size \(k=\lfloor n/2\rfloor\) and put \(d=n-2k\in\{0,1\}\). Select a sign vector \(z^{(a)}\) with exactly two negative entries, one inside and one outside the flip set, and a sign vector \(z^{(b)}\) with exactly one negative entry inside the flip set. Both have positive probability under the uniform probe law, since \(k,n-k\ge2\) when \(n\ge4\). Their respective scalar response pairs are
\[
\left(\frac{(n-4)^2-n}{2},\frac{d^2-n}{2}\right),\qquad
\left(\frac{(n-2)^2-n}{2},\frac{(d+2)^2-n}{2}\right).
\]
Both coordinates in the second pair are strictly greater than the corresponding coordinates in the first pair whenever \(n\ge4\). Swapping a small equal amount of the second-coordinate mass between these two pairs preserves the entire scalar marginal distribution and strictly lowers covariance by the swap identity in Step 1. Lifting the improved scalar coupling back to uniform vector marginals proves that the balanced fixed flip, hence every fixed flip, is strictly suboptimal.

**5. The exact four-vertex witness.** For \(n=4\), \(X_4\) takes values \(-2,0,6\) with probabilities \(6/16,8/16,2/16\). Reversed-quantile pairing has \(\mathbb E[XX']=-3\). As \(v_4=6\), its estimator variance is \(2(6-3)=6\). The best fixed-flip covariance is \(6-2(2\cdot2)=-2\), hence its variance is \(2(6-2)=8\). Independent copies give \(2v_4=12\). Step 2 proves that no graph or real symmetric matrix on at most three vertices can exhibit this strict separation, completing minimality.

**6. Limiting ratio.** By the classical central limit theorem, \(S_n/\sqrt n\) converges weakly to a standard Gaussian \(G\), so \(X_n/n\) converges weakly to \((G^2-1)/2\). The centered second moments also converge, since \(\mathbb E[(X_n/n)^2]=(n-1)/(2n)\to1/2=\mathbb E[((G^2-1)/2)^2]\). Weak convergence together with convergence of second moments gives convergence in the one-dimensional quadratic Wasserstein metric, equivalently \(L^2(0,1)\) convergence of quantile functions. Cauchy--Schwarz therefore permits passage to the limit in the reflected quantile covariance:
\[
\frac{c_n}{n^2}\longrightarrow\int_0^1 q(u)q(1-u)\,du.
\]
Finally, \(V_{\mathrm{flip}}(n)/n^2\to1\) while \(V_*(n)/n^2\to1+2\int_0^1q(u)q(1-u)\,du\), yielding the claimed exact integral limit. The quantile formula follows from \(\mathbb P(G^2\le x)=2\Phi(\sqrt x)-1\) for \(x\ge0\).

## Verification

Run `python verify.py` in the same directory as this document. The script uses only the Python standard library. It independently checks the small-dimensional fixed-flip theorem on 300 rational weighted instances, computes complete-graph countermonotone covariances both by full enumeration and by cumulative binomial masses through dimension 12, verifies every fixed-flip covariance through dimension 12, tests exact rational inequalities through dimension 128, and replays the two-comonotone-pair strictness witness. It reports 832 exact assertions passed. This is finite corroboration: the unbounded dimensional claims follow from the proof above. Numerical integration of the limiting quantile expression is not part of the exact symbolic certificate.

## Relationship to prior work

Cortinovis and Kressner (initial public preprint 20 May 2020) study Rademacher quadratic-form trace estimates, including indefinite matrices, with independent probes and tail bounds. Their theorem and corollary on Rademacher chaos do not state a variance optimum over all *joint* two-probe laws or a fixed-flip comparison. Meyer, Musco, Musco and Woodruff (initial public preprint 19 October 2020) prove Hutch++ complexity guarantees using random low-rank decomposition, a fundamentally different estimator class. Switzer, Stathopoulos, Romero, Laeuchli and Orginos (initial public preprint 2 June 2021) discuss graph-coloring and hierarchical deterministic/masked probing, rather than the exact two-uniform-probe coupling frontier. Classical rearrangement/countermonotone coupling is *not* new; the contribution here is the minimal dimension and its all-dimensional complete-graph strictness and exact variance specification, with the limit formula. These comparisons do not rule out an earlier specialist treatment of the same complete-graph finite-coupling problem.

## Limitations

The global optimum is over joint laws at a known fixed matrix with each probe individually fully uniform Rademacher; it is not an optimality claim among arbitrary unbiased trace estimators, adaptive algorithms, non-Rademacher marginal designs, or general large-matrix methods. Computing a fully optimized coupling may itself require knowledge of the target response distribution and should not be represented as a demonstrated runtime improvement. The general rearrangement theorem already supplies a universal abstract solution for scalar coupled outputs; a claimed novelty of that theorem would be incorrect. The decimal limiting ratio is approximate. No independent mathematical audit has been performed.

## References

1. A. Cortinovis and D. Kressner, *On randomized trace estimates for indefinite matrices with an application to determinants*, arXiv:2005.10009v1, 20 May 2020, https://arxiv.org/abs/2005.10009 ; relevant full text https://arxiv.org/html/2005.10009v2 .
2. R. A. Meyer, C. Musco, C. Musco and D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649v1, 19 October 2020, https://arxiv.org/abs/2010.09649 ; open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC8553228/ .
3. H. Switzer, A. Stathopoulos, E. Romero, J. Laeuchli and K. Orginos, *Probing for the Trace Estimation of a Permuted Matrix Inverse Corresponding to a Lattice Displacement*, arXiv:2106.01275v1, 2 June 2021, https://arxiv.org/abs/2106.01275 ; full text https://arxiv.org/html/2106.01275v2 .
4. G. H. Hardy, J. E. Littlewood and G. Pólya, *Inequalities*, rearrangement inequality (classical principle; no claim of novelty).
