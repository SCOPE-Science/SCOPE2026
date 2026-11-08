# Exact zero-temperature Ising response and correlations on the Petersen line graph

## Finding

The line graph \(G=L(P)\) of the Petersen graph is a 15-site, 30-bond cluster of ten edge-disjoint frustrated triangles. For the uniform antiferromagnetic Ising model with \(J>0\), the exact ground energy for every longitudinal field \(h\in\mathbb R\) is

\[
E_0(h)=\begin{cases}-10J-5|h|,&|h|\le4J,\\30J-15|h|,&|h|\ge4J.\end{cases}
\]

The number of ground states is exactly \(1782\) when \(h=0\), \(6\) when \(0<|h|<4J\), \(332\) when \(|h|=4J\), and \(1\) when \(|h|>4J\). The positive-field plateau magnetization is \(M=5\), one third of the saturation value \(15\); its negative-field counterpart is \(M=-5\).

At zero field the **complete magnetization-resolved ground-state polynomial**, with \(k\) the number of negative spins, is

\[
F(z)=6(z^5+z^{10})+195(z^6+z^9)+690(z^7+z^8).
\]

Under the uniform probability measure on these \(1782\) ground states, for any two distinct sites \(e,f\in V(G)\) at graph distance \(r\), the two-point function \(C_r=\langle\sigma_e\sigma_f\rangle_0\) is

\[
C_1=-\frac13,\qquad C_2=\frac{95}{891},\qquad C_3=-\frac{145}{891}.
\]

All \(105\) unordered site pairs are covered: \(30\), \(60\), and \(15\) have respective distances \(1\), \(2\), and \(3\). The coefficients and correlations are exact integers/rationals, not sampled estimates.

## Assumptions and scope

Let \(P\) have vertices \(u_i,v_i\) for \(i\in\mathbb Z/5\mathbb Z\) and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), with indices modulo five. It has ten vertices and fifteen edges. Each edge \(e\in E(P)\) carries one spin \(\sigma_e\in\{-1,+1\}\). Distinct edges of \(P\) interact if they share a vertex. The energy is

\[
H_{J,h}(\sigma)=J\sum_{\{e,f\}\in E(L(P))}\sigma_e\sigma_f-h\sum_{e\in E(P)}\sigma_e,
\quad J>0,\quad h\in\mathbb R.
\]

Every configuration is counted as a distinct labelled assignment to the fifteen edges. In particular, no quotient by spin reversal or graph automorphisms is taken. The zero-temperature expectations are uniform averages over all zero-field minima. These are finite-system statements, not assertions about thermodynamic limits, dynamics, or nonzero-temperature transitions.

## Proof

**Local energy and field optimization.** For a spin configuration define \(D=\{e\in E(P):\sigma_e=-1\}\), \(k=|D|\), \(d_D(v)=|D\cap E_P(v)|\), and \(n_j=|\{v\in V(P):d_D(v)=j\}|\) for \(j=0,1,2,3\). Each of the ten root vertices contributes a separate triangle of \(L(P)\). Its energy is \(+3J\) if all three spins agree and \(-J\) otherwise. With \(B=n_0+n_3\),

\[
H(D)=-10J+4JB-h(15-2k).
\]

The identities \(n_0+n_1+n_2+n_3=10\) and \(n_1+2n_2+3n_3=2k\) give

\[
B=10-2k+n_2+3n_3.
\]

The Petersen graph has a perfect matching; take any one as \(D_*\), so \(k=5\), \(n_0=n_2=n_3=0\), and \(H(D_*)=-10J-5h\) for \(h\ge0\). If \(k\le5\), then

\[
H(D)-H(D_*)=4J(n_2+3n_3)+2(4J-h)(5-k)\ge0
\]

for \(0\le h\le4J\). If \(k\ge5\), then \(H(D)-H(D_*)=4JB+2h(k-5)\ge0\) over the same range. When \(0<h<4J\), equality occurs precisely for \(k=5\) and \(B=0\), i.e. perfect matchings. At \(h=0\), equality is exactly \(B=0\), meaning every root triangle has both spin signs. At \(h=4J\),

\[
H(D)-H(D_*)=4J(n_2+3n_3),
\]

so equality holds exactly for all matchings \(D\), including the empty matching. Finally, the all-plus state has energy \(30J-15h\) and, for every \(h>4J\),

\[
H(D)-(30J-15h)=4J(n_2+3n_3)+2(h-4J)k\ge0,
\]

with equality only for \(D=\varnothing\). Global spin reversal handles all \(h<0\). This proves the energy curve, ground-state descriptions, and the absence of any other field thresholds.

**Exact zero-field polynomial.** For each root vertex \(v\) let \(A_v\) be the event that all three incident edge spins agree. Zero-field minima avoid all ten events. For any \(S\subseteq V(P)\), let \(\pi(P[S])\) be the connected components of the subgraph induced by \(S\); let \(I(C)\) be the set of root edges incident with at least one vertex in component \(C\); and set \(f(S)=15-|\bigcup_{v\in S}E_P(v)|\). Imposing all events \(A_v\) for \(v\in S\) makes the signs on each block \(I(C)\) identical, while the \(f(S)\) remaining edges are free. These blocks are pairwise disjoint. Inclusion-exclusion therefore gives the finite, exact polynomial identity

\[
F(z)=\sum_{S\subseteq V(P)}(-1)^{|S|}(1+z)^{f(S)}
\prod_{C\in\pi(P[S])}(1+z^{|I(C)|}).
\]

The standalone `verify_inclusion.py` evaluates all \(2^{10}=1024\) terms by integer polynomial arithmetic and obtains the displayed \(F(z)\); in particular \(F(1)=1782\). Independently, `verify_exhaustive.cpp` constructs \(P\) as the Kneser graph on two-subsets of a five-element set, and enumerates every \(2^{15}=32768\) spin configuration, recovering every coefficient of \(F\) and the complete energy envelope.

**Exact ground-state correlations.** Inclusion-exclusion also computes each pair numerator \(N_{ef}=\sum_{\sigma:\,B(\sigma)=0}\sigma_e\sigma_f\). For any fixed event intersection indexed by \(S\), the signed sum of \(\sigma_e\sigma_f\) vanishes unless \(e\) and \(f\) belong to the same constrained block \(I(C)\). In that case the product is identically \(+1\), and the intersection contains \(2^{|\pi(P[S])|+f(S)}\) configurations. Hence

\[
N_{ef}=\sum_{\substack{S\subseteq V(P):\\ e,f\in I(C)\ \text{for some }C\in\pi(P[S])}}
(-1)^{|S|}2^{|\pi(P[S])|+f(S)}.
\]

The integer evaluation of this explicit 1024-term sum for each unordered pair gives \(N_{ef}=-594\) at distance one, \(190\) at distance two, and \(-290\) at distance three. The independent complete-spin enumeration obtains the same \(105\) numerators without using inclusion-exclusion. Dividing each by \(1782\) proves all displayed correlations, and the computed pair-distance counts exhaust all unordered pairs.

**Critical multiplicity.** The matching numbers of the Petersen graph are already tabulated as \((m_0,\ldots,m_5)=(1,15,75,145,90,6)\). Their sum is \(332\), and the perfect-matching count is \(6\). The standalone inclusion-exclusion verifier independently rederives these coefficients by vertex deletion, while the exhaustive verifier independently checks them via spin masks.

## Verification

The package contains `verify_inclusion.py`, requiring Python 3 and no third-party packages, and `verify_exhaustive.cpp`, requiring a C++17 compiler. Run:

```sh
python3 verify_inclusion.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
```

The first returns `IE_MATCHING_OK` and `IE_CORRELATION_OK`; the second returns `EXHAUSTIVE_OK`. Both have exact assertions for the 1782-state zero-field profile, 332-state critical degeneracy, all 105 pair correlations, and relevant field energies. The computation is finite and exhaustive for this fixed fifteen-spin graph. The analytic field inequalities apply to all real \(h\) and all \(J>0\).

## Relationship to prior work

Loh, Yao and Carlson (arXiv:0711.3471, public 2007-11-23) give a different, periodic triangular-kagome Ising Hamiltonian with its own frustrated-triangle/dimer phases and field transitions; the generic geometric mechanism is not claimed here. Dyer, Heinrich, Jerrum and Müller (arXiv:2005.07944, public 2020-05-16) give the general line-graph Ising/Holant representation and approximation algorithms, but not the explicitly evaluated Petersen-line-graph ground-state polynomial or the distance-resolved correlations. The Sage matching-polynomial reference explicitly prints the Petersen matching polynomial, so the matching numbers and 332-sum are acknowledged as prior knowledge and used only to interpret the critical-field states. The new finite-system data principally consist of the zero-field magnetization distribution, the uniform two-point correlations at all graph distances, and their placement in the exact ground-state response of this canonical fifteen-site frustrated cluster.

## Limitations

No independent scientific audit has been performed. The originality assessment is based on the identified published sources and mathematical implications, and cannot rule out an unindexed equivalent Ising, graph-cut, or constraint-count table. The result concerns identical pairwise antiferromagnetic couplings and a uniform longitudinal field on one fixed finite graph; no statement is made about arbitrary anisotropic couplings, the thermodynamic limit, finite-temperature criticality, experimental realizations, or dynamical relaxation.

## References

- Y. L. Loh, D.-X. Yao, and E. W. Carlson, *Thermodynamics of Ising spins on the Triangular Kagome Lattice: Exact analytical method and Monte Carlo simulations*, arXiv:0711.3471, first public 2007-11-23. https://arxiv.org/abs/0711.3471
- M. Dyer, M. Heinrich, M. Jerrum, and H. Müller, *Polynomial-time approximation algorithms for the antiferromagnetic Ising model on line graphs*, arXiv:2005.07944, first public 2020-05-16. https://arxiv.org/abs/2005.07944
- SageMath, *Matching Polynomial*, graph-theory reference manual, Petersen graph example. https://sporadic.stanford.edu/reference/graphs/sage/graphs/matchpoly.html
