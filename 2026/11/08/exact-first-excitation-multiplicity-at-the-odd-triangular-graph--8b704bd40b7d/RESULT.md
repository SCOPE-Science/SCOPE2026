# Exact first-excitation multiplicity at the odd triangular-graph Ising parity field

## Finding
For each odd integer \(n\ge5\), consider the classical antiferromagnetic Ising model on the triangular graph \(T_n=L(K_n)\), with uniform coupling \(J>0\), and fix the positive longitudinal field at \(h_*=2J(n-3)\). Write the Ising partition function as \(Z_n(\beta,h_*)\) for inverse temperature \(\beta>0\). Let \(E_0\) be the minimum energy. Set \(m=(n-3)/2\). The first strictly higher energy is exactly \(E_0+4J\). Its complete degeneracy is
\[
 D_1(n)=\frac{n!}{(n-3)!}(n-4)!!\,\frac{m^3+6m^2+8m+2}{6},
\]
where \((2r-1)!!=(2r-1)(2r-3)\cdots1\). The ground-state degeneracy is
\[
 D_0(n)=\frac{n(n+1)}2(n-2)!!.
\]
Consequently, at every fixed odd \(n\ge5\),
\[
 Z_n(\beta,h_*)=e^{-\beta E_0}\bigl(D_0(n)+D_1(n)e^{-4\beta J}+O_n(e^{-8\beta J})\bigr)
 \quad(\beta\to\infty),
\]
and the relative first-excitation prefactor is
\[
 \frac{D_1(n)}{D_0(n)}=
 \frac{(n-1)(m^3+6m^2+8m+2)}{3(n+1)}
 \sim\frac{n^3}{24}.
\]
The cubic prefactor shows why a fixed-size low-temperature expansion need not be uniform in graph order. No joint-limit crossover or phase transition is asserted.

## Assumptions and scope
The graph \(K_n\) is simple and labeled, with vertices \(1,\ldots,n\); the spins \(\sigma_e\in\{-1,+1\}\) live on its \(\binom n2\) edges, equivalently on vertices of \(T_n\). The Hamiltonian is
\[
 H_{J,h}(\sigma)=J\sum_{\{e,f\}\in E(T_n)}\sigma_e\sigma_f-h\sum_{e\in E(K_n)}\sigma_e.
\]
Every spin assignment is counted once; no quotient by permutation or global spin reversal is made. Only odd \(n\ge5\), \(J>0\), the exact field \(h_*=2J(n-3)\), and positive inverse temperature are asserted.

## Proof
Let \(F\subseteq E(K_n)\) be the edges carrying spin \(-1\), let \(d_v\) be their degrees in \(F\), and let \(N=\binom n2\). Each adjacent edge pair of \(T_n\) shares exactly one vertex of \(K_n\), so the interaction, including the field, is
\[
 H_{J,h}(\sigma)=J|E(T_n)|-hN+2J\sum_{v=1}^n d_v^2+(h-2J(n-1))\sum_{v=1}^n d_v.
\]
At \(h=h_*\), this becomes
\[
 H_{J,h_*}(\sigma)=C_n+2J\sum_{v=1}^n(d_v-1)^2,
 \qquad C_n=J|E(T_n)|-h_*N-2Jn.
\]
The degree sum \(\sum_v d_v=2|F|\) is even. Because \(n\) is odd, \(\sum_v(d_v-1)\) is odd. Hence \(\sum_v(d_v-1)^2\) is an odd positive integer. It attains \(1\) (one isolated vertex and a perfect matching on the others), and the next possible value \(3\) is attained (three isolated vertices and a perfect matching on the others). Thus \(E_0=C_n+2J\), the first higher energy is \(C_n+6J\), and the gap is exactly \(4J\).

At square-defect sum one there is exactly one exceptional vertex of degree \(0\) or \(2\) and every other vertex has degree \(1\). The degree-zero case contributes \(n(n-2)!!\) labeled graphs. For degree two, select its vertex, two neighboring endpoints, and match the remaining \(n-3\) vertices; this contributes \(n\binom{n-1}2(n-4)!!\). Adding gives \(D_0(n)\).

At square-defect sum three, there are exactly three exceptional vertices, each of degree \(0\) or \(2\), with all \(p=n-3=2m\) remaining vertices of degree \(1\). Let \(t\in\{0,1,2,3\}\) be the number of degree-two exceptions. Choose labels for the \(3-t\) isolated and \(t\) degree-two vertices in \(n!/[p!\,t!(3-t)!]\) ways. The \(p\) degree-one vertices are paired into \(m\) unordered endpoint pairs in \((p-1)!!\) ways. Every non-cycle degree-two vertex belongs to a path connecting a pair of degree-one endpoints. Once each endpoint pair has been canonically oriented from the smaller to the larger label, placing the \(t\) labeled interior vertices in ordered strings along the \(m\) paths gives precisely \(t!\binom{t+m-1}{m-1}\) options: choose an ordering of the \(t\) labels and a weak composition of its length into \(m\) path lengths. Only when \(t=3\), a further configuration is possible: all three degree-two vertices form a triangle and all degree-one endpoints are directly matched. There is exactly one such cycle on the chosen labels. Thus
\[
 D_1(n)=\frac{n!}{p!}(p-1)!!\sum_{t=0}^3
 \frac{t!\binom{t+m-1}{m-1}+\mathbf1_{\{t=3\}}}{t!(3-t)!}.
\]
The sum equals \((m^3+6m^2+8m+2)/6\), proving the asserted formula. It counts all and only feasible simple graphs of square-defect sum three, with no additional shapes or overcounting.

By finite-state discreteness and the same parity argument the next square-defect sum, if any, is at least five, giving an energy gap of at least \(8J\) above \(E_0\) for all remaining states. This proves the fixed-size asymptotic expansion. Simplifying the ratio gives the displayed cubic asymptotic.

## Verification
The self-contained Python checker `verify_excited.py` verifies the integer formulas and independently enumerates every edge subset of \(K_5\) and \(K_7\), comparing the defect sums and degeneracies. The exhaustive counts are \((D_0,D_1)=(45,170)\) at \(n=5\) and \((420,5250)\) at \(n=7\). The verifier also checks the path/cycle sum against the simplified expression for odd \(n=5,7,\ldots,35\). These finite checks support the symbolic counting argument; they do not certify the infinite family independently of its proof.

## Relationship to prior work
The established all-field ground-energy staircase for Ising spins on \(L(K_n)\) includes the special field \(h_*=2J(n-3)\) and its parity-dependent ground sectors. Neither that ground-state description nor a restatement of its transition fields is presented here as new. The specific contribution is instead the **next energy shell**, its exact complete count, the strictly positive excitation gap, and the resulting leading finite-temperature coefficient. Dyer–Heinrich–Jerrum–Müller (2020) prove approximation/sampling properties for antiferromagnetic Ising partition functions on arbitrary line graphs, rather than this exact low-lying level count. Varma (2013) calculates saturation entropies on ladders and the kagome lattice, not on the triangular graph \(L(K_n)\). Betre–Lewis (2025) discuss equivalent Ising graph-state energies and ground-state graph patterns on \(L(K_n)\), but the examined low-energy material does not give the explicit three-defect degeneracy count.

## Limitations
The result treats a finite graph at exactly one field, not an interval of fields. There is no claim about the entire partition function, a thermodynamic phase transition, or a joint limit in \(n\) and \(\beta\). The common degree-square energy reduction is standard and is not claimed as novel. Independently resolving historical priority requires broader mathematical-physics bibliographic coverage; a search absence is not uniqueness proof.

## References
1. V. K. Varma, “Antiferromagnetic Ising model saturation field entropies: ladders and kagome lattice,” arXiv:1305.4606, first posted 2013-05-20, https://arxiv.org/abs/1305.4606.
2. M. Dyer, M. Heinrich, M. Jerrum and H. Müller, “Polynomial-time approximation algorithms for the antiferromagnetic Ising model on line graphs,” arXiv:2005.07944, first posted 2020-05-16, https://arxiv.org/abs/2005.07944.
3. K. H. Betre and N. Lewis, “Dynamical Quantum Multigraphs,” arXiv:2509.08296, first posted 2025-09-10, https://arxiv.org/abs/2509.08296.
