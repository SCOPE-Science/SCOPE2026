# Exponential enrichment of perfect packing in random sequential adsorption on a square ladder

## Finding
Let \(G_L=P_L\square K_2\) be the open two-row ladder with \(L\ge2\) rungs. Attach mutually independent continuous uniform priorities to its \(2L\) vertices and accept a vertex in increasing-priority order precisely when none of its neighbors has already been accepted. Let \(p_L\) denote the probability of terminal occupation number \(L\), the maximum independent-set size.

Set \(g(x,y)=1-\min(x,y)\), \(k(x,y,z)=1-\min(x,y,z)\), and define the positive operator \(T\) on \(H=L^2([0,1]^2)\) by
\[
(Tf)(x,y)=\int_0^1 k(x,y,z)f(y,z)\,dz.
\]
For every integer \(L\ge2\), the exact probability is
\[
p_L=2\langle g,T^{L-2}g\rangle_H.
\]
There is a well-defined real number \(\lambda=\rho(T)\) and constants \(C>0\), \(0<\eta<\lambda\) such that
\[
p_L=C\lambda^L+O(\eta^L),\qquad
\frac34\le\lambda\le\left(\frac34\right)^{1/3}<1.
\]
For a uniformly selected *jammed* (maximal independent) configuration on the same ladder, the probability of the *maximum* occupation is exactly \(u_L=1/F_L\), where \(F_1=F_2=1\) are Fibonacci numbers. Consequently, with \(\varphi=(1+\sqrt5)/2\),
\[
\frac{p_L}{u_L}\sim\frac{C}{\sqrt5}(\lambda\varphi)^L,
\qquad \lambda\varphi\ge\frac{3\varphi}4>1.
\]
Both probabilities vanish exponentially, but kinetic adsorption selects perfect alternating packings an exponentially larger fraction of the time than uniform sampling of all jammed packings. A midpoint-discretization sanity check estimates \(\lambda\) near \(0.782\); no certified decimal approximation is claimed.

## Assumptions and scope
The ladder is finite and open (no longitudinal periodic wrap). Every vertex receives one independent continuous priority, so equal-rate Poisson deposition or random unused-vertex proposals have the same acceptance-order law. The constraint is nearest-neighbor exclusion, equivalently blockade range \(b=1\). The comparison ensemble is uniform across *distinct terminal configurations*, not weighted by the number of arrival histories. The main asymptotic takes integer \(L\to\infty\). The operator acts on real \(L^2\) functions with Lebesgue measure.

## Proof
**1. Perfect configurations and exact integral.** An independent set has at most one vertex in each rung; achieving occupation \(L\) therefore requires one vertex from every rung. Adjacent rungs force alternating rows, so exactly two perfect configurations exist. Fix one, name its vertices \(A_i\), and the opposite-row vertices \(B_i\), indexed by rungs \(i=1,\ldots,L\). Write independent uniform priorities \(U_i\) and \(V_i\) respectively. The neighbors of \(B_i\) in the target perfect set are exactly \(A_j\) with \(j\in\{i-1,i,i+1\}\cap[1,L]\). Since the \(B_i\) are mutually nonadjacent, the greedy process selects precisely all \(A_i\) if and only if
\[
V_i>\min_{j\in\{i-1,i,i+1\}\cap[1,L]}U_j\quad\hbox{for all }i.
\]
For necessity, a selected \(B_i\) is forbidden, so it must arrive after some already accepted adjacent \(A_j\). For sufficiency, if the displayed inequalities hold, the first attempted \(B_i\) that could otherwise be accepted has a smaller-priority adjacent \(A_j\), which must already have been accepted because it cannot have been blocked by any previously accepted \(B\); contradiction. Equivalently, an induction over priorities proves that every \(A\) is accepted and no \(B\) is. Integrating independent \(V_i\) yields
\[
q_L:=\Pr(\hbox{a prescribed perfect packing})
=\int_{[0,1]^L}\prod_{i=1}^L
\left(1-\min_{j\in\{i-1,i,i+1\}\cap[1,L]}u_j\right)\,du_1\cdots du_L.
\]
The boundary factors are \(g(u_1,u_2)\) and \(g(u_{L-1},u_L)\); the \(L-2\) interior factors are \(k(u_{i-1},u_i,u_{i+1})\), giving \(q_L=\langle g,T^{L-2}g\rangle_H\). The two disjoint perfect packings have equal probability, hence \(p_L=2q_L\).

**2. Compact positive transfer and strict dominant rate.** The square of the operator is the integral operator
\[
(T^2f)(x,y)=\int_0^1\int_0^1
k(x,y,z)k(y,z,w)f(z,w)\,dw\,dz.
\]
Its kernel is continuous, bounded and strictly positive except on a Lebesgue-null boundary set. Therefore \(T^2\) is Hilbert–Schmidt compact and positivity improving. The compact positive-kernel Perron–Frobenius–Jentzsch theorem implies its spectral radius \(s>0\) is algebraically simple, has strictly positive right and left eigenfunctions, and strictly dominates the moduli of all other eigenvalues. Because \(T\) commutes with \(T^2\), it acts by a scalar on the one-dimensional leading eigenspace; positivity forces that scalar to be \(\lambda=\sqrt s>0\). Every other spectral value of the power-compact operator \(T\) has modulus strictly less than \(\lambda\); the leading eigenprojection \(\Pi\) is rank one with positive left and right eigenfunctions. Hence for any \(\eta\) strictly between the remaining spectral radius and \(\lambda\),
\[
\langle g,T^{L-2}g\rangle
=\lambda^{L-2}\langle g,\Pi g\rangle+O(\eta^{L-2}),
\]
where \(\langle g,\Pi g\rangle>0\). Taking \(C=2\langle g,\Pi g\rangle/\lambda^2\) gives the asserted sharp exponential law.

**3. Bounds independent of spectral numerics.** The integrand factors are nonnegative coordinatewise decreasing functions of independent uniforms. The Harris/association product inequality gives
\[
q_L\ge\bigl(\mathbb E[1-\min(U_1,U_2)]\bigr)^2
\bigl(\mathbb E[1-\min(U_1,U_2,U_3)]\bigr)^{L-2}
=\frac49\left(\frac34\right)^{L-2}.
\]
Conversely retain only the factors indexed by interior positions \(2,5,8,\ldots\le L-1\); their triples are disjoint, hence independent, and all omitted factors are at most one. Therefore \(q_L\le(3/4)^{\lfloor L/3\rfloor}\). Taking \(L\)-th roots and the sharp transfer asymptotic gives \(3/4\le\lambda\le(3/4)^{1/3}\), in particular \(\lambda<1\).

**4. Uniform jammed comparison.** The full maximal-independent-set enumerator of the nearest-neighbor open two-row ladder is \(2F_L\), as also follows by splitting successive rung patterns into gaps of length one or two (the Fibonacci recurrence). Only the two alternating row patterns achieve \(L\) occupied vertices; therefore \(u_L=2/(2F_L)=1/F_L\). The Binet asymptotic \(F_L\sim\varphi^L/\sqrt5\) and \(\lambda\ge3/4>\varphi^{-1}\) complete the exponential-enrichment theorem.

## Verification
The included standalone `CHECK.py` exhaustively enumerates all priority permutations for \(L=1,2,3,4\), reproducing \(p_L=1,1,7/9,3/5\). It also computes independent positive midpoint discretizations of the transfer operator and checks the basic spectral bounds. These are finite consistency checks only; the compact-kernel and association arguments, not numerical extrapolation, prove the infinite-length theorem. Execute `python CHECK.py` with Python 3 and no third-party dependencies.

## Relationship to prior work
Došlić, Puljiz, Šebek and Žubrinić (2023 preprint, later revised in 2024) give the blockade-ladder model and distinguish kinetic and uniform jammed average densities; their static enumerator at \(b=1\) implies the Fibonacci count used above. Chern, Hwang and Tsai (2015) analyze the *same nearest-neighbor two-row seating process* and derive an exact probability generating function for its entire finite-size terminal count; consequently the exact finite probabilities here are **not** claimed as previously unknown. Their main proved limit statements treat the mean and central/local ranges, with general large-deviation extensions noted; the target of the present theorem is specifically the global upper endpoint: the isolated positive spectral rate, its rigorous two-sided bounds, and its exponential quantitative comparison to uniform sampling of terminal states. The full prior generating function can in principle be analyzed to extract endpoint coefficients, and that potential alternative implication is a publication-priority qualification.

## Limitations
No numerical eigenvalue enclosure or closed elementary expression for \(\lambda\) is asserted. The probability formula for a single perfect packing is an alternative representation of a coefficient already determined implicitly by the previously known full generating function. The additional theorem concerns its sharp endpoint asymptotic and exponential kinetic-versus-uniform comparison. Results for longer blockade ranges, periodic ladders, nonuniform deposition rates, or finite-temperature dynamics are not established. Independent literature and mathematical review remain necessary for publication priority.

## References
- T. Došlić, M. Puljiz, S. Šebek and J. Žubrinić, *A model of random sequential adsorption on a ladder graph*, arXiv:2312.02747 (first public version 2023-12-05), https://arxiv.org/abs/2312.02747 .
- H.-H. Chern, H.-K. Hwang and T.-H. Tsai, *Random unfriendly seating arrangement in a dining table*, arXiv:1406.0614 (2015 manuscript), https://arxiv.org/abs/1406.0614 .
- W. Feller, *An Introduction to Probability Theory and Its Applications*, for the classical Fibonacci asymptotic (standard background).
