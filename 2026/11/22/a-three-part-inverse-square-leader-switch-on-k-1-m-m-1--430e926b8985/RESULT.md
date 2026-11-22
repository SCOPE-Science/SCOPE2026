# A three-part inverse-square leader switch on \(K_{1,m,m+1}\)

## Finding

Let \(G_m=K_{1,m,m+1}\) be the unweighted complete tripartite graph, with parts \(U,B,C\) having \(1,m,m+1\) vertices, respectively, and integer \(m\ge2\). Choose **exactly two distinct** vertices \(S\) as perfectly pinned (noise-free) leaders. Let \(L\) be the combinatorial Laplacian, let \(F=V(G_m)\setminus S\), and minimize the squared-inverse grounded-Laplacian spectral sum
\[
J_2(S)=\operatorname{tr}\bigl((L_{FF})^{-2}\bigr).
\]
The complete global optimizer classification is
\[
\operatorname*{argmin}_{|S|=2}J_2(S)=
\begin{cases}
\binom{B}{2},&m=2,\\[2pt]
\{\{u,b\}:u\in U,\ b\in B\},&m\ge3.
\end{cases}
\]
Every unlisted pair is **strictly suboptimal**, including all possible cross-part and same-part alternatives. Thus the optimizer count is one for \(m=2\), and \(m\) for every \(m\ge3\). The exact minimum is \(J_2^*(2)=1/2\) and, for \(m\ge3\),
\[
J_2^*(m)=\frac{2}{(2m+2)^2}+\frac{m-1}{(m+2)^2}+\frac{m}{(m+1)^2}
 +\frac{8m^4+44m^3+59m^2-30}{18(m+1)^2(m+2)^2}.
\]
In particular, \(J_2^*(3)=187/300\). At \(m=3\), the optimizer is a universal–middle pair, while the first inverse-power objective \(J_1(S)=\operatorname{tr}(L_{FF}^{-1})\) instead selects two middle-part vertices. Thus changing only the spectral order changes the optimal control locations on the same eight-vertex graph.

## Assumptions and scope

All cross-part edges have conductance one and there are no within-part edges. The leader set contains exactly two distinct vertices; the combinatorial Laplacian is **not normalized** by degree, and perfect pinning means deleting both leader rows and columns without changing follower diagonal degrees. Each grounded matrix is positive definite because the original graph is connected and the leader set is nonempty. All objective values omit any positive stochastic-noise or controller-gain factor that is common to every candidate. Only integer \(m\ge2\) is asserted; the two-member middle part exists even at the smallest size. The five and only five automorphism classes of possible pairs are denoted \(UB,UC,BB,BC,CC\).

## Proof

**1. Full Laplacian and resolvent.** More generally, let \(K_{n_1,\ldots,n_k}\) have \(N=\sum_i n_i\) vertices, and write \(d_i=N-n_i\). Its Laplacian has eigenvalue zero once, eigenvalue \(N\) with multiplicity \(k-1\) in the global-zero-sum space of part-constant vectors, and eigenvalue \(d_i\) with multiplicity \(n_i-1\) within part \(i\). For real \(z>0\), spectral projections give the exact entrywise resolvent \(R(z)=(L+zI)^{-1}\):
\[
R_{vw}(z)=\frac{1}{z(z+N)}+
\mathbf1_{\{v,w\text{ in the same part }i\}}
\left[\frac{\mathbf1_{\{v=w\}}}{z+d_i}-
\frac{1}{(z+N)(z+d_i)}\right].\tag{1}
\]
For a pair \(S\), Jacobi's complementary principal-minor identity yields
\[
\det(L_{FF}+zI)=\det(L+zI)\det(R(z)_{SS}).\tag{2}
\]
If the two leaders lie in one part with common degree \(d\), then directly evaluating the \(2\times2\) determinant in (1) gives
\[
D_{ss}(z;d)=\det R(z)_{SS}=
\frac{z^2+Nz+2d}{z(z+N)(z+d)^2}.\tag{3}
\]
If they lie in distinct parts with degrees \(d,e\), it gives
\[
D_{cr}(z;d,e)=\det R(z)_{SS}
=\frac{(z+N-1)[z^2+(N+1)z+d+e]}{z(z+N)^2(z+d)(z+e)}.\tag{4}
\]
The identity (2) holds at positive \(z\); the pole at \(z=0\) cancels between its two factors. As the grounded Laplacian is positive definite,
\[
J_2(S)=-\left.\frac{\mathrm d^2}{\mathrm dz^2}\log\det(L_{FF}+zI)\right|_{z=0}.\tag{5}
\]

**2. Universal two-leader squared-inverse formula.** Differentiating (2)--(4) twice, and removing the common nonzero-spectrum contribution from \(\det(L+zI)\), shows that any same-part pair with degree \(d\) contributes the correction
\[
E_{ss}(d)=\frac{N^2}{4d^2}-\frac1d-\frac2{d^2}-\frac1{N^2},\tag{6}
\]
while a cross-part pair with degrees \(d,e\) contributes
\[
E_{cr}(d,e)=\frac1{(N-1)^2}-\frac2{d+e}
+\frac{(N+1)^2}{(d+e)^2}-\frac2{N^2}-\frac1{d^2}-\frac1{e^2}.\tag{7}
\]
Consequently, on \(G_m\), set \(N=2m+2\), \(d_U=2m+1\), \(d_B=m+2\), \(d_C=m+1\), and
\[
T_m=\frac2{N^2}+\frac{m-1}{(m+2)^2}+\frac m{(m+1)^2}.
\]
Every candidate has value \(T_m\) plus the correction (6) or (7) for its part types. In particular,
\[
\begin{aligned}
J_2(UB)-T_m&=\frac{8m^4+44m^3+59m^2-30}{18(m+1)^2(m+2)^2},\\
J_2(BB)-T_m&=\frac{4m^4+12m^3-m^2-24m-16}{4(m+1)^2(m+2)^2}.\tag{8}
\end{aligned}
\]

**3. Strict orbit comparisons.** For \(m\ge3\), subtracting the \(UB\) value obtained above from the four competitors and cancelling common factors gives the exact positive gaps:
\[
\begin{aligned}
J_2(UC)-J_2(UB)&=\frac{2(12m^5+85m^4+157m^3+103m^2+36m+12)}{9(m+1)^2(m+2)^2(3m+2)^2},\\
J_2(BB)-J_2(UB)&=\frac{20m^3-20m^2-87m-42}{36(m+1)^2(m+2)},\\
J_2(BC)-J_2(UB)&=\frac{2m(20m^4+62m^3+44m^2-24m-21)}{9(m+1)^2(2m+1)^2(2m+3)},\\
J_2(CC)-J_2(UB)&=\frac{20m^4+92m^3+89m^2-180m-264}{36(m+1)^2(m+2)^2}.\tag{9}
\end{aligned}
\]
Every denominator is positive. Writing \(h=m-3\ge0\), the four respective numerator polynomials inside the positive prefactors in (9) become
\[
\begin{aligned}
&12h^5+265h^4+2257h^3+9346h^2+18933h+15087,\\
&20h^3+160h^2+333h+57,\\
&20h^4+302h^3+1682h^2+4074h+3597,\\
&20h^4+332h^3+1997h^2+4998h+4101.
\end{aligned}
\]
Every coefficient and constant term is strictly positive. This proves strictly smaller objective for \(UB\) than for all other pairs, for **every** integer \(m\ge3\), not just for enumerated values.

At \(m=2\), the distinct competing objective gaps relative to \(BB\), in the order \(UB,UC,BC,CC\), are exactly
\[
\frac{17}{162},\qquad\frac{109}{576},\qquad\frac{1151}{3150},\qquad\frac{37}{144}.
\]
All are positive. Equations (6)--(8) yield \(J_2(BB)=1/2\) at \(m=2\). Since the five orbit types exhaust all two-element sets, the result and all optimizer counts follow.

**4. A genuine change from first spectral order.** The same determinant method using the *first* derivative gives
\[
J_1(UB)-J_1(BB)
=\frac{-2m^2+5m+6}{6(m+1)(m+2)}.\tag{10}
\]
At \(m=3\) this is \(1/40>0\), whereas equation (9) gives \(J_2(BB)-J_2(UB)=19/960>0\). At \(m=3\), first differentiation of the same minor formulas gives the four exact \(J_1\) gaps relative to \(BB\), for competitors \(UB,UC,BC,CC\), respectively, as \(1/40,19/440,47/280,1/10\); hence \(BB\) is rigorously the unique first-order minimizing orbit without assuming any external leader-placement theorem. Hence the two optimization objectives select **disjoint** leader-pair classes in the same \(K_{1,3,4}\).

## Verification

The standalone `verify.py` requires Python 3 and SymPy and uses exact symbolic rational arithmetic. Execute `python3 verify.py` in its directory. It checks the resolvent-minor identities (3)--(4), their second derivatives (6)--(7), all four rational gaps (9), coefficientwise strict positivity after the shift \(m=3+h\), the four exact smallest-instance gaps, and the two displayed minimum values. It also independently constructs the full combinatorial Laplacian and computes all \(154\) two-leader grounded-matrix squared-inverse traces for \(m=2,3,4,5\), then checks \(25\) representative larger-size grounded inverses for \(6\le m\le10\). Recorded checker result: `VERIFY_OK rational_gap_identities=4 symbolic_resolvent=4 all_pair_exact_checks=154 larger_representative_checks=25 polynomial_positive_certificates=4`. The symbolic identities and positivity arguments, not the finite matrix checks, establish the infinite-family theorem.

## Relationship to prior work

Lin, Fardad and Jovanović's arXiv:1302.0450 supplies the general noise-free leader-selection model, inverse-grounded-Laplacian objective and optimization algorithms, but does not derive this tripartite inverse-square classification. Patterson and Bamieh's arXiv:1310.2592 supplies the inverse-square spectral measure in second-order stochastic consensus and develops coherence asymptotics for ungrounded fractal networks, not two pinned leaders on the present finite family.

The published *A gain-independent three-phase two-leader law on \(K_{1,m,m+1}\)* proves an exact optimizer classification for \(\operatorname{tr}(L+\kappa D_S)^{-1}\) with two finite equal-gain leaders, yielding \(BB\) for \(m=2,3\) and \(UB\) for \(m\ge4\); it does **not** study the squared inverse of the perfectly grounded follower Laplacian. Taking \(\kappa\to\infty\) retains the **first inverse power**, not the second, so the previous classification neither contains nor implies the displayed \(m=3\) inverse-square reversal. The published unequal-complete-multipartite two-leader theorem also concerns \(\operatorname{tr}(L_{FF}^{-1})\) and excludes singleton parts. These are direct mathematical distinctions rather than title-only comparisons.

## Limitations

Only two perfectly pinned leaders, exactly unit cross-part edge conductances, the family \(K_{1,m,m+1}\) for \(m\ge2\), and the exact squared-inverse spectral objective are treated. The theorem does not classify arbitrary unequal tripartite networks, arbitrary fractional spectral powers, finite-gain squared-inverse feedback, or nonuniform noise. The squared inverse is a specific spectral performance criterion and is not interchangeable with the traditional first-order steady-state variance. The analysis is a self-contained proof supported by exact rational checks; independent mathematical validation is not claimed. An unindexed equivalent statement may exist even though it was not found in the sources inspected.

## References

1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first public version 2013-02-03. https://arxiv.org/abs/1302.0450
2. S. Patterson, B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592, first public version 2013-10-09. https://arxiv.org/abs/1310.2592
3. *A gain-independent three-phase two-leader law on \(K_{1,m,m+1}\)*, public theorem and proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-gain-independent-three-phase-two-leader-law-on-k-1-m-m-1--2c6771e6ac36/RESULT.md
4. *Two noise-free leaders on unequal complete multipartite networks obey a smallest-part law*, public theorem and proof: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-two-noise-free-leaders-on-unequal-complete-multipartite-networks--6d40413d403f/RESULT.md
