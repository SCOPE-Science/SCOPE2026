# Threefold space–time locking and exact orbit populations for directed Fibonacci cellular automata

## Finding
Let \(q=2^f\), with integer \(f\ge1\). Let \(n=2^k\) with integer \(k\ge0\), and let \(s\in\mathbb Z\) be a prescribed spatial stride. On paired configurations \((u,v)\in\mathbb F_q^n\times\mathbb F_q^n\) with cyclic indices, define the reversible linear cellular automaton
\[
T_s(u,v)=(S^su+v,u),
\]
where \(S\) is one-site cyclic rotation. For a nonzero pair \((u,v)\), let \(d_s(u,v)\) be the least positive integer with \(S^{s d_s}u=u\) and \(S^{s d_s}v=v\). Then its *exact least temporal period* is
\[
\boxed{\pi_{T_s}(u,v)=3d_s(u,v)}.
\]
The zero pair is the unique fixed point. Put \(g=\gcd(n,s)\), \(L=n/g\), and \(J=\log_2 L\) (a nonnegative integer). The exact global permutation order is \(3L\), and the full labelled state census is
\[
\boxed{P_1=1,\qquad P_3=q^{2g}-1,\qquad P_{3\cdot2^j}=q^{2g2^j}-q^{2g2^{j-1}}\ (1\le j\le J).}
\]
No other least temporal periods occur, and each listed count is positive. The number of distinct temporal cycles of period \(m\) is \(P_m/m\). More generally, for every integer \(t\ge1\),
\[
\boxed{\#\operatorname{Fix}(T_s^t)=\begin{cases}1,&3\nmid t,\\q^{2\gcd(n,s2^{\nu_2(t)})},&3\mid t.\end{cases}}
\]
For \(L>1\), the fraction of all \(q^{2n}\) states attaining the maximal period \(3L\) is exactly \(1-q^{-n}\), **independent of the stride**. For \(L=1\), every nonzero state has period three.

## Assumptions and scope
The cyclic ring has \(n=2^k\) labelled sites, including the one-site ring. The stride \(s\) may be zero, negative, or larger than \(n\); only its residue modulo \(n\) acts on the finite ring. The pair \((u,v)\) stores two components per site. All additions are in the characteristic-two field \(\mathbb F_q\), and every configuration is counted separately without quotienting by spatial rotation. The dynamical period is an exact first return from time zero; reversibility rules out transient states. No claim is made for odd spatial circumferences or fields of odd characteristic.

## Proof
**1. Reversible matrix and a factorization of the third iterate.** Identify a cyclic row with the group algebra \(R=\mathbb F_q[z,z^{-1}]/(z^n-1)\), where \(S\) acts by multiplication by \(z\), and write \(a=z^s\in R^\times\). The two-row update is the invertible matrix
\[
M=\begin{pmatrix}a&1\\1&0\end{pmatrix},\qquad M^{-1}=\begin{pmatrix}0&1\\1&a\end{pmatrix}.
\]
A direct multiplication in characteristic two gives
\[
M^3-I=(a+1)C(a),\qquad
C(a)=\begin{pmatrix}a^2+a+1&a+1\\a+1&1\end{pmatrix}.
\]
Crucially, \(\det C(a)=a\), which is a unit of \(R\); and \(C(a)\) commutes with the scalar spatial shift \(zI\). Therefore \(C(a)\) and every positive integer power preserve, bijectively, every spatial-shift fixed subspace.

**2. Exact fixed spaces at three times a power of two.** By characteristic-two Frobenius, for every integer \(j\ge0\),
\[
M^{3\cdot 2^j}-I=(M^3-I)^{2^j}=(a^{2^j}+1)C(a)^{2^j}.
\]
Since \(C(a)^{2^j}\) is invertible and commutes with \(a^{2^j}\), its action preserves the kernel of the scalar factor. Consequently
\[
\boxed{\operatorname{Fix}(M^{3\cdot2^j})=\operatorname{Fix}(S^{s2^j}\oplus S^{s2^j}).}
\]
The permutation \(S^{s2^j}\) has exactly \(\gcd(n,s2^j)\) coordinate cycles. Its fixed vectors are constant on each cycle, with that many free entries of \(\mathbb F_q\). Choosing two rows independently proves the fixed-point count \(q^{2\gcd(n,s2^j)}\).

**3. Exclude other periods.** As \(n=2^k\), in characteristic two the algebra \(R\) is local: writing \(z=1+\epsilon\), it is \(\mathbb F_q[\epsilon]/(\epsilon^n)\). Reducing \(M\) modulo \(\epsilon\) gives the constant companion matrix \(M_0=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\), whose characteristic polynomial \(t^2+t+1\) has order three, and \(M_0^h-I\) is invertible when \(3\nmid h\). Thus \(M^h-I\) is invertible over the local ring in that case; the zero pair is the only fixed state for \(3\nmid h\). Now \(S^{sL}=I\), so Step 2 gives \(M^{3L}=I\). Every temporal period divides \(3L\), hence each nonzero period has the form \(3\cdot2^j\), \(0\le j\le J\).

For a nonzero state the least such \(j\) fixing it under \(M^{3\cdot2^j}\) equals, by Step 2, the least \(j\) fixing it under \(S^{s2^j}\) in both rows. Since the order of \(S^s\) is a power of two, this proves \(\pi_{T_s}(u,v)=3d_s(u,v)\). It also shows that if \(t=3\cdot2^j h\) with odd \(h\), then \(\operatorname{Fix}(M^t)=\operatorname{Fix}(M^{3\cdot2^j})\), giving the formula at arbitrary time \(t\).

**4. Sharp state and orbit census.** The order of the spatial permutation \(S^s\) is \(L=n/g\). It consists of \(g\) independent cycles of length \(L\); the paired system has \(q^{2g2^j}\) states of spatial \(S^s\)-period dividing \(2^j\) for \(0\le j\le J\). Step 3 maps each nonzero such state to temporal period \(3\cdot2^j\). Subtracting successive cumulative counts gives \(P_3=q^{2g}-1\) and, for \(1\le j\le J\), the stated differences. Each difference is positive, so the maximal period \(3L\) is attained, and therefore the global order is exactly \(3L\). Invertibility gives disjoint cycles and the orbit counts by division by period. When \(J\ge1\), \(P_{3L}=q^{2n}-q^n\), proving the claimed maximal-period proportion.

## Verification
The bundled standalone Python standard-library program `verify.py` evolves the local rule independently of the ring-algebra proof. It exhaustively enumerates all paired binary states for every dyadic size \(n\in\{1,2,4,8\}\) and all strides \(0\le s<n\), checking for each state the least temporal period against three times the observed joint shifted spatial period. It also compares the complete population histogram with the formulas, on 15 size–stride combinations and 525,348 labelled initial states. Running `python3 verify.py` prints `PASS: 15 dyadic size/stride cases; 525348 exhaustive states; space-time equality and cycle census`. These finite tests do not prove the statements for unbounded ring sizes or all characteristic-two fields; that scope follows from the algebraic steps above.

## Relationship to prior work
Castronuovo, Dennunzio, Kari, and Margara (2026) compute topological entropy of finite-group cellular automata and provide a characteristic-polynomial formula for linear systems; for the present infinite-line rule, its characteristic polynomial has form \(t^2+z^s t+1\), giving entropy \(|s|\log q\) for nonzero \(s\). Their analyzed theorem is about entropy, **not** finite spatial-ring least-period synchronization or the primitive-period populations. Therefore the present distinction is material: different nonzero strides can have different infinite-line entropies while exhibiting identical finite-ring temporal distributions when they have the same \(\gcd(n,s)\).

A prior census of reversible nearest-neighbor waves on cycles treats \(S+S^{-1}\), whose characteristic polynomial factors into traveling branches and whose even-ring global order is \(n\), not the directed one-neighbor companion matrix and the present period \(3n/\gcd(n,s)\). A dyadic-sunlet wave census proves a threefold global clock for a different graph with four row components per ring site; its dimension and fixed-point populations differ, and its theorem does not imply the present pointwise \(3d_s\) space–time locking or the all-stride classification. Dyadic ring-coupled cat maps have a distinct half-spatial-period temporal law. Reversibility, cyclotomic factors, and finite-field module counting are classical techniques, and are not claimed as new by themselves.

## Limitations
The complete arithmetic classification uses both characteristic two and a power-of-two spatial circumference. In particular, odd factors of the circumference can introduce additional temporal eigenvalues and invalidate the simple space–time law. The field can be any \(\mathbb F_{2^f}\), but odd-characteristic extensions are unproved here. Exhaustive small cases are corroboration, not an all-length certificate. Unindexed equivalents in older reversible-cellular-automaton literature, including inaccessible full papers on matrix representations, remain a genuine historical-priority risk. No independent audit has been performed.

## References
1. N. Castronuovo, A. Dennunzio, J. Kari and L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746v1, first publicly available 2026-11-12, especially Theorem 4. https://arxiv.org/abs/2611.16746
2. *An exact periodic-orbit census for reversible finite-field waves on cycles*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-periodic-orbit-census-for-reversible-finite-field-waves--6f3d55fba7da
3. *Parity-split orbit census for reversible nearest-neighbor waves on binary rings*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-split-orbit-census-for-reversible-nearest-neighbor-waves--a400d5cad467
4. *Pendant memory creates a threefold wave clock on dyadic sunlet graphs*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-pendant-memory-creates-a-threefold-wave-clock-on-dyadic-sunlet-g--0c20c45a4756
5. *Exact space–time period halving and complete cycle census for binary ring-coupled cat maps*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-space-time-period-halving-and-complete-cycle-census-for-bi--2dcbd8ca3b34
6. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, *Journal of Physics A* **37** (2004), 10791–10814, DOI:10.1088/0305-4470/37/45/006. Historical full-text comparison remains incomplete.
