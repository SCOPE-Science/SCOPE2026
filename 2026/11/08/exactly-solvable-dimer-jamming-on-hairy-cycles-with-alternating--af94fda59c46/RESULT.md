# Exactly solvable dimer jamming on hairy cycles with alternating superfactorial finite-size correction

## Finding

For each integer \(n\ge3\), let the *sunlet* \(S_n=C_n\circ K_1\) consist of an \(n\)-vertex simple cycle with exactly one pendant leaf attached to each cycle vertex. Subject this graph to irreversible, uniform-rate dimer random sequential adsorption: choose a currently admissible edge uniformly, occupy its two endpoints, and repeat until none remains. Equivalently, order all original edges uniformly at random and accept each if both endpoints are still vacant. Let \(X_n\) denote the final number of dimers.

Write \(P_m^\dagger=P_m\circ K_1\) for the corresponding comb path, and \(F_m\) for its expected final dimer count, with \(F_0=0\). For every \(m\ge1\) and \(n\ge3\),
\[
(2m-1)F_m=2m-1+4\sum_{j=0}^{m-2}F_j+2F_{m-1},\qquad
\mathbb E X_n=1+\frac{F_{n-1}+F_{n-2}}2.
\]
The empty sum at \(m=1\) is zero. The complete exact generating function is
\[
F(z):=\sum_{m\ge0}F_m z^m
=\frac{z/2+\sqrt{\pi z}\,e^{-z}\operatorname{erfi}(\sqrt z)/4}{(1-z)^2},
\]
where the apparently square-rooted numerator means its unique entire power series at zero. Define
\[
\rho=\frac12+\frac{\sqrt\pi}{4e}\operatorname{erfi}(1)
=0.7690397534563842095681937102\ldots.
\]
Since the graph has \(2n\) vertices and each accepted dimer occupies two vertices, its mean occupied-vertex fraction is \(\mathbb E X_n/n\), and it tends to \(\rho\). The finite-size effect is far smaller than a generic boundary correction: for every \(n\ge3\),
\[
0<(-1)^{n-1}(\mathbb E X_n-n\rho)
<\frac{2^{n-3}}{(2n-1)!!},\qquad
\mathbb E X_n-n\rho\sim (-1)^{n-1}\frac{2^{n-3}}{(2n-1)!!}.
\]
In particular, odd cycles approach the thermodynamic value from above and even cycles from below in the unnormalized expected dimer count; the error decays superfactorially.

## Assumptions and scope

All edges are distinct, every edge has the same strictly positive Poisson attempt rate (or one random uniform priority), dimers are irreversible, and no sites are initially occupied. The core is the *simple cycle* for \(n\ge3\); no loop or parallel-edge conventions are used. The expectation is over the complete random adsorption history, not over uniformly chosen maximal matchings. The law on a finite graph is exhausted by the first admissible edge followed by independent restrictions of the remaining uniform priorities to separated components.

## Proof

**1. First-accepted-edge decompositions.** The comb \(P_m^\dagger\) has \(2m-1\) edges: \(m\) spokes and \(m-1\) path edges. A spoke attached at core position \(i\) (with \(1\le i\le m\)) consumes that core site and its own leaf. It leaves independent combs of lengths \(i-1\) and \(m-i\), contributing \(1+F_{i-1}+F_{m-i}\). A path edge between cores \(i\) and \(i+1\) consumes two core sites. The remaining disconnected combs have lengths \(i-1\) and \(m-i-1\); the two isolated pendant leaves carry no edges. Averaging all \(2m-1\) possible first edges gives
\[
(2m-1)F_m=(2m-1)+\sum_{i=1}^m(F_{i-1}+F_{m-i})
+\sum_{i=1}^{m-1}(F_{i-1}+F_{m-i-1}),
\]
which rearranges to the recurrence above. The sunlet has \(n\) spokes and \(n\) cycle edges, totaling \(2n\) equally likely first accepted edges. After a spoke, the available portion is one comb of length \(n-1\). After a cycle edge, the available portion is one comb of length \(n-2\). Therefore
\(\mathbb E X_n=1+[F_{n-1}+F_{n-2}]/2\).

**2. Exact generating function.** Multiply the comb recurrence by \(z^m\) and sum from \(m=1\). The formal generating function with \(F(0)=0\) satisfies
\[
2zF'(z)-F(z)=\frac{z(1+z)}{(1-z)^2}
+\left(2z+\frac{4z^2}{1-z}\right)F(z),
\]
or equivalently
\[
F'(z)=\left(\frac1{2z}-1+\frac2{1-z}\right)F(z)
+\frac{1+z}{2(1-z)^2}.
\]
Multiplication by its integrating factor \(z^{-1/2}e^z(1-z)^2\), followed by integration with the analytic initial condition, gives the stated closed form. This may be checked directly using \(\operatorname{erfi}'(x)=2e^{x^2}/\sqrt\pi\).

**3. Entire numerator and finite-size asymptotics.** Set \(N(z)=(1-z)^2F(z)=\sum_{k\ge1}a_kz^k\). The explicit form yields
\[
a_1=1,\qquad
 a_k=\frac{(-1)^{k-1}2^{k-2}}{(2k-1)!!}\quad(k\ge2).
\]
Here \((2k-1)!!=1\cdot3\cdots(2k-1)\). This series is entire. Consequently, \(F_m=\sum_{k=1}^m(m-k+1)a_k\), while \(N(1)=\rho\). Differentiation of the explicit numerator at \(z=1\) gives \(N'(1)=1-\rho/2\). Substituting the coefficient formula into the sunlet recurrence and subtracting \(n\rho\) yields the *exact, absolutely convergent* tail identity
\[
\mathbb E X_n-n\rho
=\sum_{k=n}^\infty\left(k-n+\frac12\right)a_k.
\]
The magnitudes of its successive summands have ratio
\[
\frac{(2(k-n)+3)}{(2(k-n)+1)}\,\frac{2}{2k+1}
\le\frac6{2n+1}<1\qquad(k\ge n\ge3).
\]
They strictly decrease and their signs alternate. The alternating-series theorem therefore places the tail strictly between zero and its first signed term, whose magnitude is \(2^{n-3}/(2n-1)!!\). The ratio after the first term is \(O(n^{-1})\), proving the sharper signed asymptotic. Double-factorial growth makes this correction superfactorially small.

## Verification

The standalone script `check_sunlet.py` independently evaluates greedy adsorption by exact rational dynamic programming on vacant-vertex subsets, without using first-edge comb formulas. It agrees with the theorem for nine comb sizes and ten cyclic sizes: \(1\le m\le9\) and \(3\le n\le10\). The script `verify_generating.py` independently constructs the entire numerator series, validates rational generating-function and first-edge recurrences at 110 indices, checks the exact finite truncated-tail algebra and alternating signs/bounds at 92 sizes, and evaluates \(\rho\) at high precision (if `mpmath` is installed). All included checks passed when rerun from the completed standalone package. Those finite tests support reproducibility; the all-size conclusions follow from the analytic proof, not from enumeration.

## Relationship to prior work

Evans's review of random/cooperative sequential adsorption [1] documents the classical irreversible adsorption model and exact one-dimensional techniques. Pippenger [2] treats both vertex adsorption and an edge adsorption variant on graph families, including regular and large-girth situations. Evans and Nord [3] study dimer adsorption on infinite ladders/strips, with a different local incidence pattern and a distinct jamming constant; Lebovka et al. [4] give square-lattice and one-dimensional \(k\)-mer results. The present result concerns a degree-three cyclic backbone with one leaf per backbone vertex, its *uniform edge-dimer* random-priority law, and the explicit closed-form finite-size parity correction. It does not claim the general first-edge decomposition or generating-function method as new. Publisher summaries of [1]–[3] were accessible but the complete texts of the especially relevant older papers were not; historical priority for an equivalent exact sunlet formula therefore remains conditional on a full-text comparison. The complete open preprint [4] describes square-lattice/one-dimensional straight-polymer adsorption, not the stated leaf-decorated cyclic family.

## Limitations

The formulas describe expected saturation, not the full probability distribution or finite-time kinetics; nonuniform spoke/edge rates and additional arms are not covered. The classical model has no quantum effects. The first-public date records a verified foundational source, not a claimed publication date for the present derivation. No independently performed scientific audit is claimed. Novelty is relative to the examined accessible record, and may be revised if an inaccessible older full text is found to state an equivalent result.

## References

1. J. W. Evans, *Random and cooperative sequential adsorption*, Reviews of Modern Physics **65**, 1281–1329 (published 1 October 1993). https://doi.org/10.1103/RevModPhys.65.1281
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics **2** (1989), 393–401. https://doi.org/10.1137/0402034
3. J. W. Evans and R. S. Nord, *Random and cooperative sequential adsorption on infinite ladders and strips*, Journal of Statistical Physics **69** (1992), 151–162. https://doi.org/10.1007/BF01053787
4. N. I. Lebovka, N. N. Karmazina, Y. Y. Tarasevich, V. V. Laptev, *Random sequential adsorption of partially oriented linear k-mers on square lattice* (first posted 15 September 2011). https://arxiv.org/abs/1109.3271
