# A convex commuting-invasion barrier and an exact reentrant window in a two-city epidemic network

## Finding

Consider the discrete-time susceptible–infected–susceptible (SIS) invasion linearization of Wang et al. [1] at a fixed, locally stable disease-free information equilibrium. Let the smaller City 1 have \(n_1\) vertices, the larger City 2 have \(n_2>n_1\) vertices, and let \(C,D\) be symmetric nonnegative within-city contact matrices and \(F\) a nonnegative \(n_1\)-by-\(n_2\) cross-city matrix. For \(0<\tau<1\), \(0\le\sigma\le1\), and a fixed positive diagonal protection matrix \(\Theta\), write
\[
M(\sigma)=\begin{pmatrix}(1-\sigma)\tau C&\sigma F\\\sigma F^{\mathsf T}&D\end{pmatrix},\qquad
L(\sigma)=\rho\bigl(\Theta M(\sigma)\bigr).
\]
**General barrier.** The map \(L\) is convex on \([0,1]\). Consequently, if infection is linearly suppressed at both commuting extremes for fixed probabilities \(0<\mu,\beta<1\), namely \(\beta L(0)<\mu\) and \(\beta L(1)<\mu\), it is suppressed at *every* intermediate commuting fraction. More generally, the strictly subcritical commuting fractions form an interval, possibly empty. This is a fixed-information-equilibrium statement: the disease-free information distribution must not vary with \(\sigma\).

**Complete equitable-class law.** Suppose \(C\) is \(c\)-regular, \(D\) is \(d\)-regular, each City-1 vertex has exactly \(f_1>0\) cross-city contacts, each City-2 vertex exactly \(f_2>0\), and the protection factors are constant within each city, \(\theta_1,\theta_2>0\). Put
\[
a=\theta_1\tau c,\quad e=\theta_2d,\quad b=\theta_1\theta_2f_1f_2>0.\]
Then
\[
L(\sigma)=\frac{a(1-\sigma)+e+\sqrt{[a(1-\sigma)-e]^2+4b\sigma^2}}2.\tag{1}
\]
If \(a\le e\), \(L\) is strictly increasing on \((0,1]\). If \(a>e\), it is strictly decreasing to
\[
\sigma_*=\frac{2a(a-e)}{a^2+4b},\qquad
L_* =\frac{a(ae+4b)}{a^2+4b},\tag{2}
\]
and strictly increasing thereafter when \(\sigma_*<1\); if \(\sigma_*\ge1\), it decreases throughout the open interval. Thus the exact condition for an interior optimal commuting fraction is
\[
a>e\quad\text{and}\quad 2a(a-e)<a^2+4b.\tag{3}\]
This includes an exact two-threshold invasion window *inside the source model's directional and transmission constraints*. Specifically, take a four-person City 1 with contact graph \(K_4\), a six-person City 2 with three disjoint contact edges, and the \(4\times6\) cross-contact matrix equal to the vertex–edge incidence matrix of \(K_4\). Choose \(\tau=2/3\), \(\Theta=I\), \(\mu=1/5\), and \(\beta=8/75\). Then
\[
L(\sigma)=\frac{3-2\sigma+\sqrt{(1-2\sigma)^2+24\sigma^2}}2,
\quad \sigma_*=\frac17,\quad L_*=\frac{13}7,
\]
and the disease-free state is linearly invasion-stable **exactly** for
\[
\boxed{\frac{7-\sqrt7}{48}<\sigma<\frac{7+\sqrt7}{48}}.\tag{4}
\]
It is linearly invasion-unstable for fractions outside the closed threshold interval, including both \(\sigma=0\) and \(\sigma=1\); infection has a unit linear multiplier at the two endpoints in (4). All contact matrices are simple, undirected, nonnegative, and the full ten-vertex contact graph is connected for every \(\sigma>0\). The information equilibrium \(\Theta=I\) is realizable as a locally stable all-unaware information state by setting pairwise information transmission to zero and giving active and removed information states positive exit probabilities, with any allowed higher-order information transmission rate.

## Assumptions and scope

The original two-city model [1, equations (6), (25), (28), (30), (33)] treats City 1 as smaller, allows only City-1 residents to commute to City 2, and assigns relative within-City-1 transmission \(\tau<1\) while cross-city contacts use City 2 transmission. Its disease-free information equilibrium yields \(\theta_i=\gamma+(1-\gamma)\bar p_i^{\mathrm U}\). We assume \(\theta_i>0\) and fix that information equilibrium while changing \(\sigma\); the information process at the disease-free state has no commuting parameter. The full disease-free state is locally stable only if the information equilibrium itself is stable, as required by [1]. Our result concerns the **linear epidemic invasion multiplier** \(1-\mu+\beta L(\sigma)\), not an unconditional global extinction theorem.

For the equitable formula, the contact matrices can have zero entries or disconnected within-city graphs; a nonzero biregular cross block is sufficient. The row sums of \(C\), \(D\), \(F\), and \(F^{\mathsf T}\) are respectively \(c,d,f_1,f_2\), so necessarily \(n_1f_1=n_2f_2\). The example uses binary contacts, \(n_1=4<n_2=6\), \(0<\tau=2/3<1\), and genuine stochastic infection and recovery probabilities.

## Proof

**1. Convexity.** Positive diagonal similarity gives
\[
\Theta^{-1/2}(\Theta M(\sigma))\Theta^{1/2}
=\Theta^{1/2}M(\sigma)\Theta^{1/2}=:A(\sigma).
\]
Here \(A(\sigma)\) is symmetric, nonnegative and affine in \(\sigma\). Because the Perron eigenvalue of a nonnegative symmetric matrix is its largest (real) eigenvalue,
\[
L(\sigma)=\lambda_{\max}(A(\sigma))
=\max_{\|v\|_2=1}v^{\mathsf T}A(\sigma)v.
\]
A maximum of affine functions is convex. For \(0\le\sigma\le1\),
\[
L(\sigma)\le(1-\sigma)L(0)+\sigma L(1).
\]
Every strict sublevel set of a convex real-valued function on an interval is an interval. Since the infection multiplier is \(1-\mu+\beta L\), both claims of the general barrier follow. No smoothness or irreducibility assumption is needed for convexity.

**2. Equitable quotient.** In the biregular class, the vectors constant on each city are invariant under \(\Theta M\), with restriction
\[
Q(\sigma)=\begin{pmatrix}a(1-\sigma)&\theta_1 f_1\sigma\\\theta_2 f_2\sigma&e\end{pmatrix}.
\]
For \(\sigma>0\), this positive-off-diagonal matrix has a strictly positive Perron eigenvector. Lifting it to all vertices produces a strictly positive eigenvector of the full nonnegative matrix, hence its eigenvalue is the **full** Perron root by the Collatz–Wielandt characterization. This proves (1) for \(\sigma>0\), and continuity extends it to \(\sigma=0\).

**3. Sharp minimum.** Put \(W(\sigma)=\sqrt{[a(1-\sigma)-e]^2+4b\sigma^2}\). For \(\sigma>0\), direct differentiation yields
\[
L''(\sigma)=\frac{2b(a-e)^2}{W(\sigma)^3}.
\]
If \(a<e\), then \(L'(0+)=0\) and \(L''>0\), so it strictly increases. If \(a=e\), the upper root simplifies to \(L(\sigma)=a+[\sqrt{a^2+4b}-a]\sigma/2\), also strictly increasing. If \(a>e\), then \(L'(0+)=-a<0\) and \(L''>0\); consequently there can be at most one turning point, and any is a strict minimum. At a turning point, the characteristic identity
\[
[L-a(1-\sigma)](L-e)=b\sigma^2
\]
and its first derivative, evaluated with \(L'=0\), give \(a(L-e)=2b\sigma\). Eliminating \(\sigma\) gives precisely (2). Its domain condition is (3). For completeness, when (3) fails the derivative stays negative on \((0,1)\); equality in (3) places the sole zero of the derivative at \(\sigma=1\). This establishes every case without numerical assumptions.

**4. Exact network witness and classification.** Label City-1 individuals by vertices \(1,2,3,4\), and the six City-2 individuals by unordered pairs of those vertices. In \(F\), City-1 vertex \(i\) contacts City-2 individual \(\{j,k\}\) exactly when \(i\in\{j,k\}\). Thus every City-1 vertex has three cross contacts and every City-2 vertex has two. Pair the six City-2 individuals into any three independent edges for \(D\). Since \(C\) is the adjacency of \(K_4\), its degree is three; \(D\) has degree one. Therefore \(a=2\), \(e=1\), \(b=6\), proving the displayed formulas. The invasion threshold is \(L=\mu/\beta=15/8\). Substituting \(15/8\) into the characteristic determinant gives
\[
\left(\frac{15}{8}-2+2\sigma\right)\left(\frac{15}{8}-1\right)-6\sigma^2
=-\frac{384\sigma^2-112\sigma+7}{64}.
\]
The quadratic has exactly the two roots in (4). The other quotient eigenvalue is less than \(e=1<15/8\), so both roots correspond to the *largest* eigenvalue. Since \(L(0)=2>15/8\), \(L(1)=3>15/8\), and \(L(1/7)=13/7<15/8\), continuity and strict convexity give the stated strict stability and instability intervals. For the information subsystem, with zero pairwise information transmission, higher-order acquisition is quadratic in small active-state probabilities; the linear information eigenvalues are \(1-\varphi\) and \(1-\delta\), both inside the unit disk when \(0<\varphi,\delta<1\). Thus the disease-free all-unaware state used for the witness is a legitimate locally attracting information equilibrium.

## Verification

The standalone Python script `verify.py` computes the matrix exactly from the ten-vertex specification, checks the city degrees and quotient identity, symbolically differentiates the spectral formula, checks the optimal commuting fraction and critical quadratic, and evaluates the full ten-by-ten spectrum at two crossings, the minimum, and both commuting extremes. Run `python verify.py` with Python 3, SymPy, and NumPy. Exact algebra proves all-parameter results; finite spectral checks only confirm the explicit construction and are not substituted for proofs.

## Relationship to prior work

Wang et al. [1] derive the effective invasion matrix and numerically explore how its threshold varies with information and commuting parameters (equations (25)–(33), Section 4). The exact convexity restriction, complete equitable-network commuter classification, and ten-node reentrant threshold interval are not stated in the inspected full text. Li et al. [2] already demonstrate nonmonotonic epidemic thresholds under recurrent movement, and Bliman et al. [3] give a general framework for commuter reproduction numbers. Those results concern movement–interaction–return or time-varying homogeneous group models, not the fixed-awareness, affine symmetric block contact matrix here. The general Rayleigh–Ritz convexity fact is classical, not asserted to be new: the contribution is its sharp application and the exact model-admissible two-threshold construction and classification.

Earlier analyses of commuter optimization, including Aronna and Moschen [4] and Rapaport and Mimouni [5], also exhibit interior optima and transmission reversals, but their averaged contact/commuter state matrices are not the above affine fixed-awareness adjacency block. No implication of (3) or (4) from these different matrix formulas was found in the inspected primary and related records. The novelty assessment is literature-bounded, not a proof of complete priority.

## Limitations

The interval result holds with the disease-free information equilibrium fixed, and the example uses the stable all-unaware state; it does not show that a nontrivial aware information state creates the same particular inversion. The theorem concerns the linear SIS invasion threshold, not nonlinear endemic prevalence, disease probability of finite stochastic realizations, optimal city policy or full nonlinear global attraction. The information layer may become coupled to infection away from the disease-free equilibrium. The local classification at the neutral crossings is left unresolved; both endpoints of the strictly subcritical window are excluded. Earlier literature might contain equivalent spectral simplifications not indexed or identified in the inspected sources.

## References

[1] Z. Wang, Y. Liang, H. Zhou, Q. Yin, S. Li, and Z. Hong, *Interplay Between Higher-Order Information Diffusion and Epidemic Spreading Under Asymmetric Intercity Commuting*, Entropy 28 (2026), 1163, first public 2026-10-21. https://doi.org/10.3390/e28101163 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC13702988/ .

[2] Y. Li, Y. Yao, M. Feng, T. P. Benko, M. Perc, and J. Završnik, *Epidemic Dynamics in Homes and Destinations under Recurrent Mobility Patterns*, arXiv:2503.14016 (first public 2025-03-18); Chaos, Solitons & Fractals 195 (2025), 116273. https://arxiv.org/abs/2503.14016 .

[3] P.-A. Bliman, B. Sangaré, and A. Savadogo, *A framework for the modelling and the analysis of epidemiological spread in commuting populations*, arXiv:2408.15634 (2024); Mathematical Biosciences 382 (2025), 109403. https://arxiv.org/abs/2408.15634 .

[4] L. M. Moschen and M. S. Aronna, *Optimal vaccination strategies on networks and in metropolitan areas*, arXiv:2402.00207, 2024. https://arxiv.org/abs/2402.00207 .

[5] A. Rapaport and I. Mimouni, *The role of permanently resident populations in the two-patches SIR model with commuters*, arXiv:2211.16137 (2022). https://arxiv.org/abs/2211.16137 .
