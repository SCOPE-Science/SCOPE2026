# Exact stationary-state zeta and density law on the three-row BML torus

## Finding
For each integer \(n\ge3\), consider the classical deterministic Biham–Middleton–Levine (BML) traffic rule on the labelled \(3\times n\) periodic grid, with east-moving cars updated synchronously first and north-moving cars updated synchronously second. Each site is empty, east-occupied, or north-occupied. A stationary configuration means fixed after a complete two-phase update.

Let \(F_n(x,y)\) count stationary configurations with weight \(x\) per east-moving car and \(y\) per north-moving car. Define the 18-column alphabet
\[
\mathcal A=\{a\in\{0,E,N\}^3:\ a_r=N\Rightarrow a_{r+1\pmod3}\ne0\},
\]
and the explicitly specified 18-by-18 matrix
\[
T(x,y)_{a,b}=x^{\#E(a)}y^{\#N(a)}\prod_{r=0}^2 \mathbf1\{a_r\ne E\ \text{or}\ b_r\ne0\},\qquad a,b\in\mathcal A.
\]
Then the full bivariate stationary-state zeta is the following finite, exact rational function:
\[
\boxed{\sum_{n\ge1}F_n(x,y)z^n=-z\frac{\partial}{\partial z}\log\det(I-zT(x,y)).}
\]
The interpretation for physical tori is \(n\ge3\); smaller coefficients are formal transfer traces.

At \(x=y=1\), the denominator factors into *two quartics*:
\[
\det(I-zT(1,1))=
(1-13z+14z^2-10z^3+z^4)
(1-5z+9z^2-5z^3+z^4).
\]
Hence the exact population \(F_n=F_n(1,1)\) is the sum of the \(n\)-th powers of the four roots of each reciprocal quartic. In particular, the populations for \(n=3,4,5,6,7,8,9\) are respectively
\[
1686,\quad19988,\quad237828,\quad2829334,\quad33652161,\quad400231244,\quad4759942476.
\]
Let \(\lambda=11.8929366011799\ldots\) be the dominant root of \(t^4-13t^3+14t^2-10t+1\). Then
\[
F_n\sim\lambda^n,\qquad
h_{\mathrm{site}}=\frac{\log\lambda}{3}=0.825314886987737\ldots .
\]
For a uniformly selected stationary configuration, the expected fraction of occupied sites tends to \(0.8610902482461\ldots\); more precisely, the mean east and north populations divided by \(n\) tend to \(1.288377862242\ldots\) and \(1.294892882497\ldots\), respectively. The full finite-size distribution is encoded by \(F_n(x,y)\).

## Assumptions and scope
Coordinates are \((r,j)\in\mathbb Z_3\times\mathbb Z_n\). East is \((r,j)\mapsto(r,j+1)\), and north is \((r,j)\mapsto(r+1,j)\), with all indices periodic. In the first simultaneous substep, an east car moves one site only when its destination was empty at the *start* of that substep. The second substep applies the analogous rule to north cars using the state after the east update. There are no multiple occupancies and no stochastic choices. Sites, rows, columns and species are labelled; states are not identified under translations or exchange of species. The statement counts configurations fixed **immediately**, not eventual stationary attraction basins or the probability of jamming after a transient.

## Proof
**1. Reduction from two-stage dynamics to blocked-neighbor predicates.** In the east update, every moving east car enters a site that was originally empty; north cars neither move nor change species during that substep. In the subsequent north update, east cars do not move. Thus, if an east car moves, its new east-occupied site was not east-occupied at the beginning of the full step, and cannot be restored to the original state by north movement. Consequently a full-step fixed point has no east moves. Once all east cars are blocked, the same reasoning shows that no north cars may move. Conversely if both species are initially blocked, neither stage changes the configuration. Therefore stationary configurations are exactly those satisfying
\[
a_{r,j}=E\Longrightarrow a_{r,j+1}\ne0,
\qquad a_{r,j}=N\Longrightarrow a_{r+1,j}\ne0.
\]

**2. Complete transfer reduction.** The north predicate is internal to each vertical column, admitting exactly 18 of the 27 ternary columns. The east predicate couples successive columns and is precisely the indicator in \(T_{a,b}\). Multiplying the weights for each departing column along a closed length-\(n\) walk yields the weight of the corresponding labelled stationary configuration exactly once. Therefore \(F_n(x,y)=\operatorname{tr}(T(x,y)^n)\) for every physical \(n\ge3\). The formal matrix identity \(-z\partial_z\log\det(I-zT)=\sum_{n\ge1}\operatorname{tr}(T^n)z^n\) follows from the formal expansion of \(\log\det(I-zT)\), proving the weighted claim without an asymptotic approximation.

**3. Exact finite algebra and growth.** Exact integer characteristic-polynomial arithmetic gives
\[
\det(tI-T(1,1))=t^{10}
(t^4-13t^3+14t^2-10t+1)
(t^4-5t^3+9t^2-5t+1).
\]
The accompanying SymPy program constructs the matrix directly from the displayed predicates and checks this factorization and the weighted determinant symbolically. For dominance without relying on floating-point experiments: on \(|t|=11\), the term \(-13t^3\) of the first quartic has modulus \(17303\), exceeding the sum \(11^4+14\cdot11^2+10\cdot11+1=16446\). Rouché's theorem gives exactly three roots of this quartic inside \(|t|<11\); its values at 11 and 12 have opposite signs, so the remaining real root is \(\lambda\in(11,12)\). By the Cauchy root bound, every root of the second quartic has modulus at most 10. Thus \(\lambda\) is the unique dominant root and has multiplicity one, proving \(F_n\sim\lambda^n\) and the entropy formula.

**4. Limiting stationary occupation.** Let \(Q(z,x,y)\) be the weighted determinant factor whose unweighted form is \(1-13z+14z^2-10z^3+z^4\), and write \(z_0=1/\lambda\). Differentiation of the exact polynomial determinant yields
\[
\left.\partial_xQ\right|_{x=y=1}=z(6z^3-38z^2+39z-17),
\quad\left.\partial_yQ\right|_{x=y=1}=-2z(4z^2+7).
\]
Since the dominant zero \(z_0\) is simple and isolated, analytic implicit differentiation of the dominant eigenvalue and standard finite-matrix spectral separation show that normalized first moments converge to the logarithmic derivatives of \(\lambda(x,y)\). Explicitly, writing \(Q_0(z)=1-13z+14z^2-10z^3+z^4\),
\[
\lim_{n\to\infty}\frac{\mathbb E E_n}{n}=\frac{6z_0^3-38z_0^2+39z_0-17}{Q_0'(z_0)},\quad
\lim_{n\to\infty}\frac{\mathbb E N_n}{n}=\frac{-2(4z_0^2+7)}{Q_0'(z_0)}.
\]
Both are positive; their sum divided by three gives the quoted occupied-site fraction. These formulas concern the uniform measure on **fixed configurations**, not random initial states conditioned on eventual trapping.

## Verification
`verify_transfer.py` uses exact SymPy arithmetic to build the 18 columns and matrix, check the complete characteristic polynomial, calculate the full symbolic bivariate determinant, and check the derivative identities; it also recomputes all seven listed totals. `verify_bruteforce.cpp` independently implements the original, simultaneous two-substep BML rule on every ternary state of the labelled \(3\times n\) torus for \(n=3,4,5\), without using the stationary predicates. Its results are 1686, 19988, and 237828, matching the transfer calculation. Both programs' exact output is included. The exhaustive finite simulation is an independent check of the rule interpretation, not a replacement for the all-\(n\) transfer proof. Reproduce with `python verify_transfer.py` (SymPy 1.14) and `g++ -O3 -std=c++17 verify_bruteforce.cpp -o verify_bruteforce && ./verify_bruteforce`.

## Relationship to prior work
Biham, Middleton and Levine (1992) introduce the deterministic two-species square-lattice traffic automaton and study its numerical jamming transition on two-dimensional periodic tori; their article does not give a complete three-row fixed-state generating function. Angel, Holroyd and Martin (2005) prove high-density jamming for the infinite lattice and growing two-dimensional tori, not this fixed-strip enumeration. Austin and Benjamini (2006) give existence and threshold results for jammed states on square tori, not a labelled three-by-\(n\) census. D'Souza (2004/2005) studies structured intermediate flow phases and aspect-ratio effects, rather than the complete zero-velocity microstate polynomial on three-row rings. A previous result concerning the two-row periodic BML torus does not imply the displayed 18-state three-row transfer polynomial: the three-row vertical blocking constraints have genuinely different column alphabets and recurrence factors. The exact claim here is the three-row bivariate fixed-state law, its two-quartic simplification and the resulting stationary ensemble statistics, not the already known existence of jammed configurations.

## Limitations
No result is claimed about the global BML jamming transition, basins of attraction, high-probability dynamical freezing, typical initial-condition trajectories, other grid heights, or any thermodynamic limit in both dimensions. Transfer computations are mathematically exhaustive only because the 18-column reduction and exact determinant identity have been proved. Historical priority is qualified by the possible existence of unindexed specialized enumerations. Independent external mathematical audit has not been performed.

## References
1. O. Biham, A. A. Middleton, D. Levine, *Self Organization and a Dynamical Transition in Traffic Flow Models*, arXiv:cond-mat/9206001 (first posted 2 June 1992), https://arxiv.org/abs/cond-mat/9206001 ; Phys. Rev. A 46, R6124 (1992).
2. O. Angel, A. E. Holroyd, J. B. Martin, *The Jammed Phase of the Biham-Middleton-Levine Traffic Model*, arXiv:math/0504001 (2005), https://arxiv.org/abs/math/0504001 .
3. T. D. Austin, I. Benjamini, *For what number of cars must self organization occur in the Biham-Middleton-Levine traffic model from any possible starting configuration?*, arXiv:math/0607759 (2006), https://arxiv.org/abs/math/0607759 .
4. R. M. D'Souza, *Geometric structure of coexisting phases found in the Biham-Middleton-Levine traffic model*, arXiv:cond-mat/0402351 (2004), https://arxiv.org/abs/cond-mat/0402351 ; Phys. Rev. E 71, 066112 (2005).
