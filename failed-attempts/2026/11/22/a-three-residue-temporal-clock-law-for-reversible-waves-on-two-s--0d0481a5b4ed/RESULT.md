# A three-residue temporal clock law for reversible waves on two-subset Kneser graphs

## Finding
Let \(n\ge4\), \(N=\binom n2\), and \(q=3^f\) for any integer \(f\ge1\). The vertices of the labelled Kneser graph \(KG(n,2)\) are the two-element subsets of \(\{1,\ldots,n\}\), adjacent exactly when disjoint. Write \(A_n\) for its loopless adjacency over \(\mathbb F_q\). Consider the reversible two-time-level evolution
\[
T_n(u,v)=(A_nu-v,u),\qquad (u,v)\in\mathbb F_q^N\times\mathbb F_q^N.
\]
Every state is periodic immediately. The *exact* global order of this permutation is
\[
\operatorname{ord}(T_n)=\begin{cases}
12,&n\equiv0\pmod3,\\
6,&n\equiv1\pmod3,\\
36,&n\equiv2\pmod3.
\end{cases}
\]
These are exact for every \(n\ge4\) in the stated residue classes and for every permitted field extension.

For each positive integer \(t\), let \(E_n(t)=\dim_{\mathbb F_q}\ker(T_n^t-I)\), write \([P]\) for the indicator of \(P\), and put \(h(t)=3^{\nu_3(t)}\) (so \(h(t)=1\) when \(3\nmid t\)). The complete fixed-state census is
\[
E_n(t)=\begin{cases}
2n[4\mid t]+(N-n)([2\mid t]+[6\mid t]),&n\equiv0\pmod3,\\
(n-1)(1+[3\mid t])+(N-n+1)([2\mid t]+[6\mid t]),&n\equiv1\pmod3,\\
2[4\mid t]+(n-1)[2\mid t]\min\{4,h(t)\}+(N-2n+1)([2\mid t]+[6\mid t]),&n\equiv2\pmod3.
\end{cases}
\]
In particular \(\#\operatorname{Fix}(T_n^t)=q^{E_n(t)}\), and for each positive \(d\) dividing the displayed order, the exact number of labelled configurations of primitive temporal period \(d\) is
\[
P_n(d)=\sum_{e\mid d}\mu(d/e)q^{E_n(e)};
\qquad \text{the number of temporal orbits is }P_n(d)/d.
\]
The possible primitive periods are precisely \(\{1,2,4,6,12\}\) when \(n\equiv0\), \(\{1,2,3,6\}\) when \(n\equiv1\), and \(\{1,2,4,6,12,18,36\}\) when \(n\equiv2\), always modulo three. For \(n\equiv2\), the fraction of all configurations with primitive period \(36\) is exactly
\[
\frac{P_n(36)}{q^{2N}}=(1-q^{-2})(1-q^{-(n-1)}).
\]
Thus the characteristic-three clock reaches \(36\) in one residue class while it collapses to \(6\) in the adjacent class, despite the common combinatorial construction of these graphs.

## Assumptions and scope
The graph has \(N\) distinct, individually labelled vertices; time cycles are not quotiented by graph automorphisms. \(n\ge4\), \(f\ge1\), and \(t\ge1\) are integers. The field is any \(\mathbb F_{3^f}\); the adjacency entries \(0,1\) lie in its prime subfield. The two time layers are independent vectors. The subtraction in the update is essential. The exceptional edgeless graph \(KG(3,2)\) is excluded: it has order \(4\), not \(12\). No claim is made for larger-subset Kneser graphs, other field characteristics, or nonlinear updates.

## Proof
**1. An incidence factorization in characteristic three.** Let \(B\) be the \(n\)-by-\(N\) unsigned vertex–edge incidence matrix of the complete graph on \(n\) labels: the column for \(\{i,j\}\) has ones at \(i,j\) and zeros elsewhere. Let \(J_n\) and \(J_N\) be the all-ones square matrices of indicated sizes. Then \(B^\top B\) has diagonal entries two and entries one for intersecting distinct pairs. Therefore the disjointness adjacency satisfies, over \(\mathbb F_3\),
\[
A_n=J_N+I_N-B^\top B.
\]
Since \(B^\top J_n B=4J_N=J_N\) in characteristic three, define \(U=B^\top\) and \(V=(J_n-I_n)B\). It follows that
\[
A_n=I_N+UV.
\]
The incidence identity \(BB^\top=(n-2)I_n+J_n\) gives
\[
VU=(J_n-I_n)((n-2)I_n+J_n)
=(2-n)I_n+(2n-3)J_n=(2-n)I_n-nJ_n.
\]
All final coefficients here are interpreted in characteristic three. \(U\) is injective because if every pair-sum \(x_i+x_j\) vanishes, any three labels give \(2x_i=0\); hence \(x=0\). Consequently \(B\) is surjective. Finally \(J_n^2=nJ_n\).

**2. Exact adjacency Jordan blocks.** The preceding relations yield three cases.

* If \(n\equiv0\pmod3\), then \(VU=2I_n\). Hence \((UV)^2=2UV\) and \(UV\) has rank \(n\). It has eigenvalue \(2\) in dimension \(n\) and eigenvalue zero in dimension \(N-n\), both semisimple. Thus \(A_n\) has scalar blocks \(0^{\oplus n}\) and \(1^{\oplus(N-n)}\).
* If \(n\equiv1\pmod3\), then \(VU=I_n-J_n\), which is the rank-\((n-1)\) projection onto the sum-zero hyperplane; also \(V\) has exactly this rank. Thus \((UV)^2=UV\) of rank \(n-1\). The adjacency blocks are \(2^{\oplus(n-1)}\) and \(1^{\oplus(N-n+1)}\).
* If \(n\equiv2\pmod3\), then \(VU=J_n\). The operator \(UV\) has rank \(n\) and \((UV)^2=UJ_nV\) has rank one, while \(U\mathbf1\) is an eigenvector of \(UV\) with eigenvalue \(2\). Off this one-dimensional eigenvalue-\(2\) sector, \(UV\) is square-zero of rank \(n-1\). Its nilpotent Jordan structure consists of \(n-1\) blocks of size two and \(N-2n+1\) blocks of size one. Adding \(I_N\), the adjacency blocks become one scalar \(0\), \(n-1\) size-two Jordan blocks at eigenvalue \(1\), and \(N-2n+1\) scalar blocks at eigenvalue \(1\). The last multiplicity is nonnegative for all admissible \(n\equiv2\) (the smallest is \(n=5\)).

This is a decomposition over the prime field, hence remains valid over every \(\mathbb F_q\) in the statement.

**3. Temporal blocks and their fixed spaces.** On an adjacency eigenline of eigenvalue \(a\), the wave block has characteristic polynomial \(z^2-az+1\). For \(a=0\), it is \(z^2+1\); the block is semisimple with exact order four, contributes two fixed dimensions precisely when \(4\mid t\), and zero otherwise. For \(a=1\), the polynomial is \((z+1)^2\) in characteristic three; the nonscalar temporal block is a size-two Jordan block at eigenvalue minus one. Its \(t\)-th power fixes dimension \([2\mid t]+[6\mid t]\). For \(a=2=-1\), the block is a size-two Jordan block at eigenvalue plus one, fixing dimension \(1+[3\mid t]\).

A size-two adjacency Jordan block at eigenvalue one produces a *single size-four temporal Jordan block* at eigenvalue minus one. To verify its nonstandard block length, write its spatial part as \(I+R\), where \(R^2=0\) but \(R\ne0\), and put \(Z=T+I\) on the corresponding four-dimensional time space. The block recurrence yields \(Z^2=R(Z-I)\), whence \(Z^4=0\). Moreover \(Z^3=-RZ\ne0\): in temporal coordinates \((u,v)\), the two entries of \(RZ(u,v)\) are \((-R(u+v),R(u+v))\), which is nonzero for a suitable \(u+v\) because \(R\ne0\). Therefore its Jordan size is exactly four. For a Jordan block of size \(s\) with eigenvalue minus one, an iterate fixes nothing when \(t\) is odd and fixes exactly \(\min\{s,3^{\nu_3(t)}\}\) dimensions when \(t\) is even: this follows from the characteristic-three binomial identity \((I+L)^{3^a}=I+L^{3^a}\) for nilpotent \(L\). Here \(s=4\), giving the third case's minimum term.

Adding these contributions with the adjacency block multiplicities in step 2 proves every displayed formula for \(E_n(t)\). Reversibility is explicit: \(T_n^{-1}(u,v)=(v,A_nv-u)\), so every finite-field configuration is periodic from the initial time.

**4. Sharp orders and primitive periods.** The temporal blocks above have exact orders four (scalar adjacency zero), six (scalar adjacency one), three (scalar adjacency minus one), and eighteen (size-two adjacency block at one), respectively. Their least common multiples are \(12\), \(6\), and \(36\) in the three residue classes. In the first case both needed block kinds occur because \(n\ge6\) whenever \(n\equiv0\) and \(N-n>0\). In the other cases the required blocks likewise have positive multiplicities. Taking vectors with top nonzero Jordan coordinates realizes every listed block period, and summing vectors in independent primary sectors realizes their possible least common multiples. This gives the exact primitive-period supports stated in the Finding.

For the period-\(36\) formula in the third case, inclusion-exclusion over the two maximal proper divisors \(18\) and \(12\) gives
\[
P_n(36)=q^{2N}-q^{E_n(18)}-q^{E_n(12)}+q^{E_n(6)}
=q^{2N}-q^{2N-2}-q^{2N-n+1}+q^{2N-n-1},
\]
which factors as asserted. Ordinary Möbius inversion proves the general primitive-population formula. This completes the all-size proof.

## Verification
The self-contained standard-library file `verify_kneser.py` constructs disjointness adjacency matrices, independently multiplies the full two-time-layer matrices over \(\mathbb F_3\), and computes fixed-space nullities by modular Gaussian elimination. It tests nine iterate exponents for each \(n=4,5,\ldots,10\), plus the exact global-order identity. A separate coordinate-level update routine enumerates **all \(3^{12}=531441\) labelled states** for \(n=4\), with populations \(27,729,729,531441\) fixed by updates \(1,2,3,6\), respectively. The companion `verification_output.txt` records the completed run. These finite checks corroborate but do not constitute the infinite-family proof; the incidence/Jordan argument above does.

## Relationship to prior work
The reversible previous-state construction is established rather than new: Vlasov (first public preprint 2013, §3 and §6.2) supplies general second-order rules, not Kneser-specific period and orbit counts. Ducey–Hill–Sin (first public preprint 2017, §§1–4) investigate Smith normal forms of the **Laplacian** of \(KG(n,2)\), with its established combinatorial spectrum; the Laplacian's Smith invariants are not temporal Jordan blocks of \(T_n\). Published characteristic-two strongly-regular-wave theorems cannot be specialized to characteristic three, and characteristic-three biclique formulas concern a different adjacency module. The all-size characteristic-three incidence trichotomy, temporal block of size four, and complete orbit formulas here are not assertions of those sources. An already studied reversible wave on the *complementary triangular graph* concerns a different adjacency and yields a different residue-class period law: complementing the graph does not conjugate the wave updates. Its statement does not by itself supply the present disjointness-incidence factorization or these fixed-space dimensions.

## Limitations
Only two-subset Kneser graphs, field characteristic three, and the specified linear reversible update are covered. The apparent historical novelty follows a bounded comparison, not an exhaustive universal priority guarantee. Finite verification cannot replace the symbolic all-size proof. No external independent mathematical audit or certification has been performed.

## References
1. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first submitted 2013-11-18, https://arxiv.org/abs/1311.4297 ; inspected §§3, 6.2 via https://arxiv.org/pdf/1311.4297 .
2. J. E. Ducey, I. Hill and P. Sin, *The critical group of the Kneser graph on 2-subsets of an n-element set*, arXiv:1707.09115, first submitted 2017-07-28, https://arxiv.org/abs/1707.09115 ; inspected §§1–4 via https://arxiv.org/pdf/1707.09115 .
3. *Three universal wave periods and spectrally invisible orbit counts on strongly regular graphs*, public mathematical report, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-universal-wave-periods-and-spectrally-invisible-orbit-coun--6be21916ed4f .
4. *Mod-three resonance trichotomy for reversible waves on complete bipartite graphs*, public mathematical report, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mod-three-resonance-trichotomy-for-reversible-waves-on-complete--167b2c8980f2 .
