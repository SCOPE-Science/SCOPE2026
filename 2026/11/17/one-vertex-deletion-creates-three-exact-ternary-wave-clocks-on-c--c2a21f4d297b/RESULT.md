# One-vertex deletion creates three exact ternary wave clocks on cocktail-party graphs

## Finding

Let \(r\ge2\), let \(C_{r+1}=K_{2r+2}\setminus M_{r+1}\) be the cocktail-party graph with a perfect matching removed, and delete any one vertex to obtain \(H_r=C_{r+1}-w\). Equivalently, \(H_r\) is the complete graph on \(2r+1\) labelled vertices with exactly \(r\) disjoint edges deleted. Over any finite field \(\mathbb F_q\), \(q=3^f\) and \(f\ge1\), write \(A_r\) for the loopless adjacency operator of \(H_r\), and define the reversible second-order wave
\[
T_r(u,v)=(A_ru-v,u),\qquad (u,v)\in\mathbb F_q^{2r+1}\times\mathbb F_q^{2r+1}.
\]
Every state is immediately periodic. For every integer \(t\ge1\), define \(w_t=3^{\nu_3(t)}\), \(b_t=\min(2,w_t)\), \(c_t=\min(4,w_t)\), and let \([d\mid t]\) be the indicator of divisibility. Then the dimension \(E_r(t)=\dim_{\mathbb F_q}\ker(T_r^t-I)\) is exactly
\[
\boxed{E_r(t)=\begin{cases}
2(r+1)[4\mid t]+[2\mid t]\bigl((r-2)b_t+c_t\bigr),&r\equiv0\pmod3,\\
2r[4\mid t]+(r-1)[2\mid t]b_t+4[8\mid t],&r\equiv1\pmod3,\\
2r[4\mid t]+(r-1)[2\mid t]b_t+4[5\mid t],&r\equiv2\pmod3.
\end{cases}}
\]
Consequently, \(\#\operatorname{Fix}(T_r^t)=q^{E_r(t)}\). The exact global permutation order and the corresponding order *before* the vertex deletion are
\[
\boxed{\begin{array}{c|ccc}
r\bmod3&0&1&2\\\hline
\operatorname{ord}(T_r)&36&24&60\\
\operatorname{ord}(T_{C_{r+1}})&12&12&36
\end{array}.}
\]
In particular, deletion produces primitive five-fold temporal motion exactly for \(r\equiv2\pmod3\) and primitive eight-fold temporal motion exactly for \(r\equiv1\pmod3\), whereas the intact graphs have no such factors. Here \(r\equiv1\) means \(r\ge4\) under the stated domain.

The complete set of attainable primitive periods for each residue class is, respectively,
\[
\begin{array}{c|l}
0&1,2,4,6,12,18,36\\
1&1,2,4,6,8,12,24\\
2&1,2,4,5,6,10,12,20,30,60.
\end{array}
\]
For any positive divisor \(d\) of the displayed global period \(L_r\), the exact labelled population with least period \(d\) and the number of temporal orbits are
\[
P_r(d)=\sum_{e\mid d}\mu(d/e)q^{E_r(e)},\qquad O_r(d)=P_r(d)/d;
\]
for other positive \(d\), both are zero. The proportion of all paired-time states attaining the maximal period is
\[
\boxed{\Pr(\operatorname{per}=L_r)=\begin{cases}
(1-q^{-2r-2})(1-q^{-1}),&r\equiv0\pmod3,\\
(1-q^{-4})(1-q^{-(r-1)}),&r\equiv1\pmod3,\\
(1-q^{-2r})(1-q^{-4})(1-q^{-(r-1)}),&r\equiv2\pmod3.
\end{cases}}
\]
These are exact finite-field probabilities under the uniform distribution on all \(q^{4r+2}\) labelled two-time-level states, not approximations.

## Assumptions and scope

The deleted edges form a matching; no two share a vertex. All vertex labels distinguish configurations. Each vertex sees the sum of its actual neighbors (there are no loops or normalizations). The distinguished unmatched vertex has degree \(2r\); each vertex participating in a missing edge has degree \(2r-1\). The temporal update is the two-row recurrence with *subtraction*, rather than a synchronous first-order neighbor-sum rule. The integer \(r\) is at least two, the field characteristic is exactly three, \(t\) is any positive integer, and \(\mu\) is the classical Möbius function. An orbit consists of successive temporal states without quotienting by spatial graph automorphisms.

## Proof

**1. Reversibility and spatial splitting.** The inverse is \(T_r^{-1}(u,v)=(v,A_rv-u)\), so no state has a transient. Label the matched pairs \((a_i,b_i)\) for \(1\le i\le r\) and the unmatched vertex \(c\). Because two is invertible in characteristic three, the adjacency space is a direct sum of an \(r\)-dimensional antisymmetric space \(D\), spanned by \(e_{a_i}-e_{b_i}\), and a symmetric space \(W\), on which the pair coordinates share common values \(x_i\) while \(c\) has value \(z\). On \(D\), \(A_r=0\), since each opposite pair is a nonedge. Write \(S=\sum_i x_i\). On \(W\) the adjacency map is exactly
\[
 (z,x_1,\ldots,x_r)\longmapsto
 (-S,\ z+x_1-S,\ldots,z+x_r-S).
\]
The invariant subspace \(U=\{z=0,\ S=0\}\), of dimension \(r-1\), carries eigenvalue one. On the quotient by \(U\), the coordinates \((z,S)\) obey
\[
 Q_r=\begin{pmatrix}0&-1\\r&1-r\end{pmatrix},\qquad
 \chi_{Q_r}(\lambda)=\lambda^2-(1-r)\lambda+r.
\]

**2. Complete characteristic-three spatial modules.** If \(r\not\equiv0\pmod3\), the constant pair-vector complements \(U\), so \(W=U\oplus W_2\) with \(Q_r\) on \(W_2\). If \(r\equiv1\pmod3\), its irreducible polynomial is \(\lambda^2+1\); if \(r\equiv2\pmod3\), it is \(\lambda^2+\lambda+2\), irreducible because its discriminant is the nonsquare two. In each case, \(A_r\) has \(r\) simple zero blocks, \(r-1\) simple one blocks, and the displayed quadratic sector.

If \(3\mid r\), the quotient polynomial factors as \(\lambda(\lambda-1)\), but the eigenvalue-one eigenvectors of the full symmetric operator satisfy \(z=S=0\). Their dimension is \(r-1\), whereas the algebraic multiplicity is \(r\). Thus the one-primary part has one Jordan block of length two and \(r-2\) blocks of length one. The zero-primary part has \(r+1\) simple blocks: \(r\) from \(D\) and one from the quotient. This proves every spatial invariant factor without assuming diagonalizability of a modular reduction of a real spectrum.

**3. Lifting to the temporal wave.** On an adjacency eigenline with eigenvalue \(\lambda\), the two-time companion has characteristic polynomial \(z^2-\lambda z+1\). At \(\lambda=0\), this is \(z^2+1\), whose roots have order four in characteristic three; a simple zero block contributes two fixed dimensions exactly when \(4\mid t\). At \(\lambda=1\), it is \((z+1)^2\); the temporal module is one size-two Jordan block at \(-1\), contributing \([2\mid t]\min(2,3^{\nu_3(t)})\) fixed dimensions.

One size-two spatial block at eigenvalue one gives a four-dimensional temporal module with characteristic polynomial \((z+1)^4\). Its eigenvalue \(-1\) has one-dimensional eigenspace, because the temporal eigenvector equations reduce to \((A_r-I)u=0\) on that spatial block. Thus the temporal module is one size-four Jordan block, contributing \([2\mid t]\min(4,3^{\nu_3(t)})\) fixed dimensions. For a general Jordan block \(J_s(\rho)\) in characteristic three, \(\dim\ker(J_s(\rho)^t-I)\) equals \(\min(s,3^{\nu_3(t)})\) if \(\rho^t=1\), and zero otherwise; this follows by factoring the first nonzero binomial coefficient of \((I+N)^t-I\).

For a two-dimensional quadratic spatial sector with characteristic polynomial \(h(\lambda)\), its temporal polynomial is \(z^2h(z+z^{-1})\). When \(r\equiv1\), this is \(z^4+1=\Phi_8(z)\), so all four eigenroots have exact order eight and the fixed contribution is \(4[8\mid t]\). When \(r\equiv2\), the result is \(z^4+z^3+z^2+z+1=\Phi_5(z)\), all roots of exact order five, contributing \(4[5\mid t]\). Both polynomials are separable in characteristic three. Summing these independent block contributions proves the three displayed fixed-space formulas.

**4. Exact clocks and orbit populations.** A nonzero size-four Jordan block at \(-1\) has order eighteen; the size-two blocks there have order six; the zero-adjacency companions have order four; and the exceptional factors have orders eight and five. Taking least common multiples yields \(36,24,60\) for the three residue classes (the \(r\equiv1\) class has at least one size-two block since \(r\ge4\)). Every listed primitive period is obtained from the lcm of allowed periods of independent blocks, and no others can arise. Möbius inversion applied to \(\#\operatorname{Fix}(T_r^t)\) yields the population and orbit equations.

For the intact cocktail-party graph with \(m=r+1\) matched pairs, antisymmetric modes again have eigenvalue zero, while symmetric modes have adjacency operator \(I-J_m\). If \(3\mid m\), its nonzero rank-one nilpotent part supplies one size-two spatial Jordan block at one, yielding temporal order \(36\); otherwise it is semisimple and yields order \(12\) for \(m\ge2\). Substituting \(m=r+1\) establishes the intact graph comparison. Finally, independence of primary summands makes maximal-period probabilities products of nonzero-projection probabilities. For \(r\equiv0\) the required projections are to the \(2(r+1)\)-dimensional order-four sector and outside the codimension-one order-eighteen kernel; for \(r\equiv1\) they are to the four-dimensional order-eight sector and outside the codimension-\(r-1\) order-six kernel; for \(r\equiv2\) there is additionally the \(2r\)-dimensional order-four sector. Multiplying gives the formulas above. \(\square\)

## Verification

The included standard-library program `verify_wave_punctured_cp.py` directly builds the original vertex adjacency matrices over \(\mathbb F_3\), forms the temporal companion and checks 1,080 exact matrix-power nullities for every \(1\le r\le9\), \(1\le t\le120\). It verifies the asserted sharp orders and Möbius-derived populations for \(q=3\) and \(q=9\), and separately checks the intact graph orders for \(2\le m\le10\). The second program `direct_wave_punctured_cp.py` computes graph-local neighbor updates and an independent complete permutation-orbit census: all \(729\) states for \(r=1\) (a boundary sanity check outside the theorem) and all \(59{,}049\) states for \(r=2\). For \(r=2\), the primitive-60 population is exactly \(38{,}400\), or \(640\) temporal orbits. The files `wave_mod3_rank_output.txt` and `wave_mod3_direct_output.txt` are the actual outputs of these programs. Reproduce by executing each program with Python 3, without third-party dependencies. Finite computations corroborate, but do not prove, the unbounded-parameter theorem; the proof is the invariant-factor argument above.

## Relationship to prior work

Cámara and Haemers (2012, Section 2, Proposition 2.1) establish spectral identification of complete graphs with a matching deleted. This concerns ordinary adjacency cospectrality, not characteristic-three Jordan structure or temporal periods, and real eigenvalues alone do not settle modular Jordan multiplicities. Vlasov (2013, Section 3) supplies the standard reversible second-order construction; the recurrence itself is not claimed as new.

Published work on characteristic-three waves on complete bipartite graphs treats a different zero/paired-shore adjacency module, and work on characteristic-two edge-neighbor dynamics of matching-deleted cliques concerns a line-graph update over a different field. Neither gives these exact odd matching-deletion fixed-space dimensions or the vertex-deletion period comparison. The new contribution is the precise \(36/24/60\) three-residue temporal law, the fifth- and eighth-root emergence under deletion, and the all-time orbit census on \(H_r\).

## Limitations

The result is specific to the stated loopless, unweighted, undirected graphs and to finite fields of characteristic three. It does not classify arbitrary matching-defect counts beyond a near-perfect matching, arbitrary vertex deletion, nonlinear majority maps, or other characteristics. The finite verification does not substitute for the algebraic proof. The literature search was finite; inaccessible or unindexed general theorems could affect priority, and no independent external mathematical validation has been performed.

## References

1. Marc Cámara and Willem H. Haemers, *Spectral characterizations of almost complete graphs*, first public arXiv version 2012-11-19, arXiv:1211.4420, Section 2, https://arxiv.org/abs/1211.4420.
2. Alexander Yu. Vlasov, *On generalization of reversible second-order cellular automata*, first public arXiv version 2013-11-18, arXiv:1311.4297, Section 3, https://arxiv.org/abs/1311.4297.
3. *A matching-defect Jordan law and a parity switch in edge-parity networks*, published mathematical result on characteristic-two line-graph dynamics, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-matching-defect-jordan-law-and-a-parity-switch-in-edge-parity--91ddaed42d5a.
4. *Mod-three resonance trichotomy for reversible waves on complete bipartite graphs*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mod-three-resonance-trichotomy-for-reversible-waves-on-complete--167b2c8980f2.
