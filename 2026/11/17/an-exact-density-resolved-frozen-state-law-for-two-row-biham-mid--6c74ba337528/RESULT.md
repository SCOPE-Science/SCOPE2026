# An exact density-resolved frozen-state law for two-row Biham–Middleton–Levine traffic

## Finding
For each integer \(n\ge3\), consider the labelled \(2\times n\) periodic grid, with sites in \(\mathbb Z/2\mathbb Z\times\mathbb Z/n\mathbb Z\). Every site is empty, occupied by an eastbound car, or occupied by a northbound car. In one full update, eastbound cars simultaneously advance one column if the destination was vacant at the start of their substep; northbound cars then simultaneously advance one row if their destination is vacant after the east substep. This is the two-species Biham–Middleton–Levine exclusion rule.

Write \(J_n(u,v)=\sum_{F_n(x)=x}u^{E(x)}v^{N(x)}\), with \(E(x)\) and \(N(x)\) the two species populations. Define
\[
D(z,u,v)=(1-uz)\left[1-(1+u+u^2+2uv+v^2)z+(u+u^2+u^3+2uv-uv^2)z^2-u^3z^3\right].
\]
The exact density-resolved frozen-state law is
\[
\boxed{\sum_{n\ge1}J_n(u,v)z^n=-z\frac{\partial}{\partial z}\log D(z,u,v).}
\]
Here the coefficients at \(n\ge3\) are the physical two-row torus counts; smaller coefficients are formal transfer coefficients. In particular, if \(\lambda\) is the unique real root of \(\lambda^3-6\lambda^2+4\lambda-1=0\), then
\[
J_n(1,1)=1+\sum_{\xi^3-6\xi^2+4\xi-1=0}\xi^n\sim\lambda^n,\qquad 5.278039<\lambda<5.278040.
\]
The number of frozen states containing both car species and at least one empty site equals exactly
\[
\boxed{J_n(1,1)-4^n-2^n-1.}
\]
Thus asymptotically almost every frozen state has both species and vacancies, even though every completely occupied configuration is frozen. Under the uniform distribution on frozen states, the vacancy fraction converges in probability to
\[
\boxed{\delta=1-\frac{9\lambda^2-7\lambda+3}{2\lambda(3\lambda^2-12\lambda+4)}=0.152713299756\ldots.}
\]

## Assumptions and scope
The grid is fully periodic in both directions, but the two vertically adjacent sites are distinct and each northbound car has exactly one north destination. The horizontal circumference is at least three. Configurations are indexed and distinct under translations. The update uses parallel exclusion within each directional phase, not sequential individual-car updates. The result concerns one-full-update fixed configurations, not arbitrary eventual jams, basin probabilities or nonzero-velocity periodic states.

## Proof
If an eastbound car moves in its substep, its old site becomes vacant and cannot be refilled by another eastbound car in that same parallel substep, because destinations must be initially vacant. The subsequent northbound phase cannot restore an eastbound car to that site. Hence a full-update fixed configuration has no eastbound move. Likewise, if a northbound car moves, the old site is vacant after the northbound phase and cannot be occupied again by a northbound car in that phase; therefore fixedness forces no northbound moves. Conversely, if neither type can move, the configuration is fixed. This argument also makes the frozen configurations independent of which phase is chosen first.

Represent column \(i\) by the ordered pair \((x_{0,i},x_{1,i})\). Northbound cars are blocked exactly when no column is \((N,0)\) or \((0,N)\). The resulting seven allowed columns, in order, are
\[
(0,0),(0,E),(E,0),(E,E),(E,N),(N,E),(N,N).
\]
An eastbound car in row \(r\) of column \(a\) is blocked precisely when the next column \(b\) has a nonempty entry in row \(r\). Thus define the seven-state weighted matrix
\[
T_{a,b}=u^{\#E(b)}v^{\#N(b)}\prod_{r=0}^1\mathbf1\{a_r\ne E\text{ or }b_r\ne0\}.
\]
Every indexed cyclic word of length \(n\) of columns satisfying all blocking constraints corresponds bijectively to a labelled frozen configuration. Its weight is the product of the target-column weights around the cycle. Consequently \(J_n(u,v)=\operatorname{tr}(T^n)\). Direct fraction-free symbolic determinant elimination gives exactly \(\det(I-zT)=D(z,u,v)\). The formal identity \(-z\partial_z\log\det(I-zT)=\sum_{n\ge1}\operatorname{tr}(T^n)z^n\) proves the generating function for all admissible lengths.

At \(u=v=1\), the characteristic polynomial of \(T\) is \(X^3(X-1)(X^3-6X^2+4X-1)\). The cubic discriminant is \(-139\); its two nonreal roots have product of squared modulus \(1/\lambda\), and its sole real root \(\lambda\) lies strictly between \(5.278039\) and \(5.278040\) by exact rational sign checks. Thus its two nonreal roots have modulus \(\lambda^{-1/2}\), and \(J_n(1,1)=\lambda^n+1+O(\lambda^{-n/2})\).

There are exactly four frozen east-only states (each row entirely empty or entirely east-occupied), and exactly \(2^n\) north-only states (each column empty or occupied by two northbound cars). There are exactly \(4^n\) completely occupied states (either car species at each site). The pairwise intersections contain respectively the all-empty state, the all-east state and the all-north state, and the triple intersection is empty. Inclusion–exclusion leaves \(J_n(1,1)-4^n-2^n-1\) states with both car types and vacancies. Since \(\lambda>4\), these constitute a fraction tending to one.

For the uniform measure on frozen states, use \(t\) to mark every car. The nontrivial characteristic cubic is
\[
P(X,t)=X^3-(1+t+4t^2)X^2+(t+3t^2)X-t^3.
\]
Its simple dominant positive root \(\lambda(t)\) is analytic in a neighborhood of \(t=1\), with all other eigenvalues uniformly smaller in modulus there. Differentiating \(P(\lambda(t),t)=0\) yields
\[
\lambda'(1)=\frac{9\lambda^2-7\lambda+3}{3\lambda^2-12\lambda+4}.
\]
The exact car-count probability generating function is \(J_n(t,t)/J_n(1,1)\). Simple-root spectral dominance gives \(\lim_{n\to\infty}\mathbb E(E+N)/(2n)=\lambda'(1)/(2\lambda)\). Moreover, the same analytic dominance with \(t=e^s\) and exponential Markov inequalities on both sides yields convergence in probability of the car fraction to this value, hence of the vacancy fraction to \(\delta\).

## Verification
An independent direct implementation of the full two-phase, three-symbol configuration update exhaustively enumerates all \(3^{2n}\) states for \(3\le n\le7\), agreeing with the symbolic transfer count and with the both-species/vacancy formulas. The resulting frozen counts are \(148,777,4097,21620,114107\). A standalone symbolic program constructs the seven allowed columns and weighted transfer, recomputes its complete polynomial determinant, its unweighted characteristic polynomial and counts through length twelve, and checks the root bracket and limiting density. The exact programs and their reproduced outputs are supplied as separate files.

## Relationship to prior work
Biham, Middleton and Levine introduced this deterministic alternating species traffic rule and studied the dynamical jamming transition on large square tori [1]. D'Souza analyzed intermediate-velocity phases, geometric patterns, and lattice aspect-ratio effects [2]. Angel, Holroyd and Martin proved high-density jamming on infinite lattices and large nearly square tori [3]. Austin and Benjamini studied bounds on car populations associated with obstruction and self-organization on square tori [4]. None of these inspected source texts evaluates the two-row, all-circumference density-resolved fixed-point generating function, the corresponding cubic entropy or the limiting vacancy fraction. The prior dynamical results do not imply these exact stationary-state enumerations. A separate published mathematical-record search returned a two-car, all-aspect-ratio BML dynamical classification but not an all-population frozen-state census [5]. The counting is a finite-width stationary ensemble, not an inference about random initial-condition jam probabilities or global planar phase transitions.

## Limitations
Only width two is classified; the result does not classify attraction basins, transient time, the complete set of recurrent orbits, or the random-initial-configuration probability of eventually freezing. The asymptotic proportion is uniform over frozen configurations and is not the vacancy fraction for typical trajectories from random initial data. A bounded literature and record search cannot establish absolute historical uniqueness, especially against unindexed tables or unpublished computations. No independent external mathematical audit has been performed.

## References
[1] O. Biham, A. A. Middleton, D. Levine, *Self Organization and a Dynamical Transition in Traffic Flow Models*, first arXiv public version 1992-06-02, https://arxiv.org/abs/cond-mat/9206001 .

[2] R. M. D'Souza, *Geometric structure of coexisting phases found in the Biham-Middleton-Levine traffic model*, first arXiv public version 2004-02-13, https://arxiv.org/abs/cond-mat/0402351 .

[3] O. Angel, A. E. Holroyd, J. B. Martin, *The Jammed Phase of the Biham-Middleton-Levine Traffic Model*, first arXiv public version 2005-03-31, https://arxiv.org/abs/math/0504001 .

[4] T. D. Austin, I. Benjamini, *For what number of cars must self organization occur in the Biham-Middleton-Levine traffic model from any possible starting configuration?*, first arXiv public version 2006-07-31, https://arxiv.org/html/math/0607759v3 .

[5] published-finding corpus published record, *Two-car BML traffic has a sharp gcd trichotomy on rectangular tori*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-two-car-bml-traffic-has-a-sharp-gcd-trichotomy-on-rectangular-to--4734b945da68 .
