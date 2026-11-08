# Critical-field entropy spikes for one-spin metastability on cyclic Ising ladders

## Finding

Let \(G_n=C_n\square K_2\) be the labeled \(2n\)-vertex circular ladder (prism graph), where \(n\ge 3\). The classical antiferromagnetic Ising energy is
\[
E_{J,h}(\sigma)=J\sum_{\{v,w\}\in E(G_n)}\sigma_v\sigma_w-h\sum_{v\in V(G_n)}\sigma_v,
\quad J>0,\quad \sigma_v\in\{-1,+1\}.
\]
Write \(N_n(t)\) for the number of spin configurations in which flipping **any one spin** cannot decrease energy, with \(t=|h|/J\). Zero-energy flips are permitted in the definition. Write \(L_n\) for the Lucas numbers \(L_0=2\), \(L_1=1\), \(L_n=L_{n-1}+L_{n-2}\), and set
\[
\epsilon_n=\begin{cases}2,&3\mid n,\\-1,&3\nmid n.\end{cases}
\]
For all \(n\ge3\), the exact classification is
\[
\boxed{
N_n(t)=\begin{cases}
L_n+1+(-1)^n+\epsilon_n,&0\le t<1,\\
\displaystyle\sum_{P_3(\lambda)P_6(\lambda)=0}\lambda^n,&t=1,\\
L_n+\epsilon_n,&1<t<3,\\
(1+\sqrt2)^n+(1-\sqrt2)^n+(-1)^n,&t=3,\\
1,&t>3,
\end{cases}}
\]
where each algebraic root is included with multiplicity (all nine roots are simple) and
\[
P_3(x)=x^3+x^2+2x+1,\qquad
P_6(x)=x^6-x^5-3x^4-x^3+x^2+x+1.
\]
In particular, let \(\rho=2.33935824388750\ldots\) be the largest positive root of \(P_6\), and let \(\varphi=(1+\sqrt5)/2\). Then the one-spin-stable configurational entropy **per vertex** is
\[
\lim_{n\to\infty}\frac{\log N_n(t)}{2n}
=\begin{cases}
\frac12\log\varphi,&0\le t<1\ \text{or}\ 1<t<3,\\
\frac12\log\rho,&t=1,\\
\frac12\log(1+\sqrt2),&t=3,\\
0,&t>3.
\end{cases}
\]
Consequently both \(t=1\) and \(t=3\) are isolated entropy spikes, and the \(t=3\) spike is higher. The sign of the field does not change the count.

## Assumptions and scope

The graph consists of two \(n\)-cycles with corresponding rung edges; each vertex has three distinct neighbors, including when \(n=3\). Spins are **labeled** by their graph vertices, with no quotient by rotations, reflections, or global spin reversal. Couplings are homogeneous and antiferromagnetic; no disorder, temperature-dependent weights, asynchronous dynamics, or finite-temperature metastable lifetimes are considered. A state is one-spin stable exactly when every single-spin energy difference is nonnegative. This weak inequality matters at the two critical fields and does **not** imply absorption for an update rule that permits zero-energy flips.

## Proof

**Local criterion and field reduction.** For a vertex \(v\), changing \(\sigma_v\) to \(-\sigma_v\) changes the energy by
\[
\Delta_vE=2\sigma_v\left(h-J\sum_{w\sim v}\sigma_w\right).
\]
Thus, after dividing by the positive number \(2J\), the necessary and sufficient condition is \(\sigma_v(t-\sum_{w\sim v}\sigma_w)\ge0\) for \(h\ge0\). Spin reversal maps \(h\) to \(-h\), so counts are even in the field. The three-neighbor sum belongs to \(\{-3,-1,1,3\}\). Therefore the allowed local spin triples are constant on each of the field intervals \([0,1)\), \((1,3)\), and \((3,\infty)\), with new marginal choices exactly at \(t=1\) and \(t=3\).

**Finite-state enumeration with no asymptotic assumption.** Write rung \(i\) as \(a_i=(\sigma_{i,0},\sigma_{i,1})\) and let
\(\mathcal A=\{(-1,-1),(-1,+1),(+1,-1),(+1,+1)\}\).
Index the sixteen pairs \((a,b)\in\mathcal A^2\). Define the zero-one matrix \(T_t\) by
\[
(T_t)_{(a,b),(b',c)}=
\mathbf1\{b=b'\}
\prod_{j=0}^{1}\mathbf1\!\left\{b_j\left(t-a_j-b_{1-j}-c_j\right)\ge0\right\}.
\]
The cyclic word \((a_0,\ldots,a_{n-1})\) uniquely determines a labeled closed walk of length \(n\) in this matrix, and conversely: the transition at rung \(i\) tests both spin-flip inequalities at that rung. Hence for every \(n\ge3\),
\[
N_n(t)=\operatorname{tr}(T_t^n).
\]
This bijection is exact, including configurations with shorter cyclic periods; no division by a rotational orbit length occurs.

**Exact characteristic-polynomial certificates.** With the stated lexicographic ordering of \(\mathcal A\) and then \(\mathcal A^2\), direct finite integer elimination gives the following complete characteristic polynomials:
\[
\begin{array}{c|l}
t&\det(xI-T_t)\\\hline
0&x^{10}(x-1)(x+1)(x^2-x-1)(x^2+x+1)\\
1&x^{7}P_3(x)P_6(x)\\
2&x^{12}(x^2-x-1)(x^2+x+1)\\
3&x^{13}(x+1)(x^2-2x-1)\\
4&x^{15}(x-1)
\end{array}
\]
The self-contained file `verify.py` constructs these matrices from the local spin-flip inequalities and computes their characteristic polynomials using exact integer Faddeev–LeVerrier identities (rather than relying on an external numerical eigenvalue routine). It also compares their traces against a direct independent enumeration of full-Hamiltonian energy differences. These explicit matrices and integer computations provide finite reproducible certificates for the displayed factors.

For any finite square matrix, the trace of its \(n\)th power is the sum of \(n\)th powers of eigenvalues with algebraic multiplicity, even when Jordan blocks occur. Zero eigenvalues do not contribute. The two quadratic factors have roots \(\varphi\), \(-\varphi^{-1}\) and the primitive cube roots of unity, respectively. Their power sums give \(L_n\) and \(\epsilon_n\); the factors \(x\pm1\) supply the parity corrections. At \(t=3\), the quadratic roots are \(1\pm\sqrt2\). Substituting into \(\operatorname{tr}(T_t^n)\) yields every displayed exact count.

**Dominant critical root and entropy.** At \(t=1\), the recurrent cyclic component of the sixteen-state transition graph consists of the eleven indexed states \(3,5,6,7,9,10,11,12,13,14,15\) (indices starting at zero); all other states lie in an acyclic induced complement. The recurrent component is strongly connected and has cycles of lengths two and seven, so its nonnegative adjacency matrix is primitive. These finite assertions are checked exactly in `verify.py`. Perron–Frobenius then gives a simple positive strictly dominant eigenvalue. Since \(P_3\) has no positive root and \(P_6\) has, by Descartes' rule and the signs at \(0,1,2,3\), precisely two positive roots, one in \((0,1)\) and one in \((2,3)\), the Perron eigenvalue is the larger root \(\rho\) of \(P_6\). Thus \(N_n(1)=\rho^n(1+o(1))\). The explicit formulas establish the other exponential rates and the strict inequalities \(\varphi<\rho<1+\sqrt2\).

## Verification

Run `python3 verify.py` using Python 3 (standard library only). The code constructs the transfer matrices, checks all five sixteen-degree characteristic polynomials with exact integer arithmetic, compares direct cyclic-word enumeration for \(3\le n\le8\), and independently evaluates the original Hamiltonian and **every single-spin flip** for \(3\le n\le6\). It tests the closed-form Lucas, cube-root and Pell expressions for \(3\le n\le13\), field reversal symmetry, the recurrent-component connectivity, and the coprime-length cycles. All included assertions passed when run from the packaged source. These computations are finite exact checks and not substitutes for the all-\(n\) trace bijection and spectral argument above.

## Relationship to prior work

Shukla's *Voter Dynamics on an Ising Ladder: Coarsening and Persistence* (first public version January 31, 2005) discusses zero-temperature Glauber fixed points on a ladder with **ferromagnetic alignment** and emphasizes odd coordination; it does not supply fixed-coupling **antiferromagnetic** one-spin-stable counts in a field. Waclaw and Burda's *Counting metastable states of Ising spin glasses on arbitrary graphs* (first public January 8, 2008), including its Section VII on ladders, treats **Gaussian-distributed random bonds** and estimates ensemble-averaged complexity, not homogeneous antiferromagnetic field thresholds or the exact characteristic polynomial at \(t=1\). The prism's independent-set total at \(t=3\) is a known graph enumeration (and is listed in MathWorld): it is **not** claimed as independently novel. What is asserted beyond that known endpoint is the full field-dependent one-spin-stable classification, including the nine-root exact \(t=1\) law, the two strict-field Lucas regimes and the comparative entropy spikes. Separate earlier analyses of wheel-graph one-spin stability and Möbius-ladder **ground-state** degeneracies do not imply these prism metastability counts: their graphs or events differ.

## Limitations

This is an all-size theorem for weak one-spin stability only, not a classification of global ground states or dynamically absorbing states if neutral-energy flips are allowed. No claim is made about actual escape rates, stochastic occupation weights, thermodynamic singularities at positive temperature, or higher-dimensional ladders. The known \(t=3\) independent-set formula is used as an ingredient, not represented as new. The originality comparison is based on the inspected sources and searchable records and is subject to unindexed historical equivalents and independent review.

## References

1. P. Shukla, *Voter Dynamics on an Ising Ladder: Coarsening and Persistence*, arXiv:cond-mat/0501754, v1 posted 2005-01-31. https://arxiv.org/abs/cond-mat/0501754
2. B. Waclaw and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224, v1 posted 2008-01-08, especially Sections I and VII. https://arxiv.org/html/0801.1224v1
3. E. W. Weisstein, *Independent Vertex Set*, MathWorld, tabulation for prism graphs. https://mathworld.wolfram.com/IndependentVertexSet.html
4. S. Masui, T. Li, B. W. Southern and A. E. Jacobs, *Metastable states of Ising models on the honeycomb lattice*, Phys. Rev. B 40 (1989), 7096; random-bond honeycomb comparison. https://doi.org/10.1103/PhysRevB.40.7096
