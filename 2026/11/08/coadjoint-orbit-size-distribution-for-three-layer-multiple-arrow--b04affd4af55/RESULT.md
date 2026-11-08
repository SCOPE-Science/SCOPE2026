# Coadjoint orbit-size distribution for three-layer multiple-arrow path algebras

## Finding
Let \(k=\mathbb F_q\) be any finite field, and let \(a,b\ge1\). Consider the acyclic quiver with three vertices, \(a\) distinct arrows from the first to the second vertex, and \(b\) distinct arrows from the second to the third, with no other arrows. Let \(A=kQ\) be its path algebra, \(G=A^\times\) its full unit group, and \(A^*\) the dual of its underlying vector space. The action is \((g\cdot f)(x)=f(g^{-1}xg)\).

The algebra has radical \(J\) satisfying \(J^3=0\) and \(\dim_k J^2=ab>0\). Write \(U\cong k^a\) and \(V\cong k^b\) for the two arrow spaces, and identify the length-two path space with \(W=U\otimes V\). Every functional is uniquely \(f=(\delta,\alpha,\beta,C)\), with \(\delta\in k^3\), \(\alpha\in U^*\), \(\beta\in V^*\), and \(C\in(U\otimes V)^*\), a bilinear form on \(U\times V\).

For \(1\le s\le\min(a,b)\) define
\[
N_s(q)=\begin{bmatrix}a\\s\end{bmatrix}_q\begin{bmatrix}b\\s\end{bmatrix}_q\prod_{i=0}^{s-1}(q^s-q^i).
\]
This is the number of bilinear forms of rank \(s\). The **entire coadjoint orbit-size distribution** is the following table. The last column counts *distinct orbits*, not individual functionals.

| Condition on the functional | Cardinality of each orbit | Number of these orbits |
|---|---|---|
| \(C=0,\ \alpha=\beta=0\) | \(1\) | \(q^3\) |
| \(C=0\), exactly one of \(\alpha,\beta\) is nonzero | \(q(q-1)\) | \(q^2(q^a+q^b-2)/(q-1)\) |
| \(C=0,\ \alpha\ne0,\ \beta\ne0\) | \(q^2(q-1)^2\) | \(q(q^a-1)(q^b-1)/(q-1)^2\) |
| \(\operatorname{rank}C=s\ge1\), both \(\alpha\in\operatorname{im}(V\to U^*)\) and \(\beta\in\operatorname{im}(U\to V^*)\), the maps induced by \(C\) | \(q^{2s+1}(q-1)\) | \(N_s(q)q^2/(q-1)\) |
| \(\operatorname{rank}C=s\ge1\), at least one of those two image conditions fails | \(q^{2s+2}(q-1)^2\) | \(N_s(q)q(q^{a+b-2s}-1)/(q-1)^2\) |

A zero numerator in the last row means that no such orbits exist, notably when \(a=b=s\). All listed counts are integers for every prime power \(q\), including even characteristic. The two nonzero-\(C\) series are absent if the length-two path multiplication is artificially killed: they genuinely record the first nontrivial radical-square layer.

For example, when \(a=b=2\) and \(q=2\), the counts by (orbit size, number of orbits) are
\[
(1,8),\ (2,24),\ (4,18),\ (8,36),\ (16,54),\ (32,24).
\]
The weighted total is \(2^{11}\), exactly the number of functionals on \(A\).

## Assumptions and scope
All fields are finite, of arbitrary characteristic; no division by two or orbit-method representation-theoretic correspondence is assumed. All arrow multiplicities \(a,b\) are positive. The action is the coadjoint action of the *full unit group* \(A^\times\) on the entire dual vector space \(A^*\), including the duals of the three primitive idempotents. It is not the action of only the unipotent subgroup \(1+J\) on \(J^*\), nor the usual change-of-basis action on quiver representations.

## Proof
Take primitive idempotents \(e_1,e_2,e_3\). The only nonzero products between basis arrows are the length-two paths \(uv=u\otimes v\) for \(u\in U\) and \(v\in V\); the usual endpoint idempotent products also hold. Every unit is uniquely
\[
g=d_1e_1+d_2e_2+d_3e_3+x+y+z,
\]
with \(d_i\in k^\times\), \(x\in U\), \(y\in V\), and \(z\in W\). Hence \(|G|=(q-1)^3q^{a+b+ab}\).

For any invertible \(g\), the equation \(g\cdot f=f\) is equivalent to \(f(gh-hg)=0\) for every \(h\in A\). Indeed, in the defining coadjoint identity substitute \(h\mapsto gh\); this equivalence uses no characteristic restriction. Evaluating the commutators on the primitive idempotents and the three path spaces gives exactly
\[
\alpha(x)=\beta(y)=-C(z),\qquad
C(-,y)=(d_1-d_2)\alpha,\qquad
C(x,-)=-(d_2-d_3)\beta,\qquad
(d_1-d_3)C=0. \tag{1}
\]
Thus the stabilizer of \(f\) is the set of units satisfying (1). The three coordinates \(\delta\) do not enter the equations and are free.

If \(C=0\), each nonzero \(\alpha\) enforces \(d_1=d_2\) and \(\alpha(x)=0\), while each nonzero \(\beta\) enforces \(d_2=d_3\) and \(\beta(y)=0\). With \(t\in\{0,1,2\}\) the number of nonzero arrow functionals, this leaves \((q-1)^{3-t}\) diagonal choices and \(q^{a+b+ab-t}\) choices in the radical. Orbit-stabilizer gives the cardinality \([q(q-1)]^t\). Counting \(\delta,\alpha,\beta\) and dividing by that cardinality yields the first three rows.

Now suppose \(C\ne0\) has rank \(s\). Equation (1) forces \(d_1=d_3\). Set \(h=d_1-d_2\). The equations on \(x,y\) become
\[
C(-,y)=h\alpha,\qquad C(x,-)=h\beta. \tag{2}
\]
Let \(U_0\subseteq U\) and \(V_0\subseteq V\) be the left and right radicals of \(C\), of dimensions \(a-s\) and \(b-s\).

First suppose both image conditions in the table hold. Every \(h\in k\) is allowed in (2), and the solutions for \((x,y)\) form an affine space of dimension \(a+b-2s\). They satisfy \(\alpha(x)=\beta(y)\): if \(h\ne0\), evaluate \(C(x,y)\) in the two ways given by (2); if \(h=0\), both functionals vanish on the respective radicals. Because \(C\ne0\), the remaining equation \(C(z)=-\alpha(x)\) has \(q^{ab-1}\) solutions. There are \((q-1)^2\) choices of \((d_1,d_2)\), so
\[
|G_f|=(q-1)^2q^{a+b+ab-2s-1},
\qquad |G\cdot f|=q^{2s+1}(q-1). \tag{3}
\]

If at least one image condition fails, (2) forces \(h=0\), hence all three diagonal entries coincide. Then \(x\in U_0\), \(y\in V_0\), and the linear condition \(\alpha(x)=\beta(y)\) is a genuinely nonzero equation on \(U_0\oplus V_0\). It reduces that combined dimension by one. Again \(C(z)=-\alpha(x)\) has \(q^{ab-1}\) solutions. Consequently
\[
|G_f|=(q-1)q^{a+b+ab-2s-2},
\qquad |G\cdot f|=q^{2s+2}(q-1)^2. \tag{4}
\]
No second case occurs if \(a+b=2s\), in agreement with the table.

The number of \(a\)-by-\(b\) matrices of rank \(s\) is \(N_s(q)\): choose their column and row spaces and an invertible map between the corresponding \(s\)-spaces. For each such \(C\), the two image conditions permit exactly \(q^{2s}\) choices of \((\alpha,\beta)\), out of \(q^{a+b}\). The idempotent-dual coordinate \(\delta\) has \(q^3\) possibilities. Dividing the resulting functional counts by (3) and (4) yields the final two rows. Every functional appears in one and only one of the five strata.

As a mass check, summing (orbit size) times (number of orbits) across the five strata gives
\[
q^3q^{a+b}\sum_{s=0}^{\min(a,b)}N_s(q)=q^{3+a+b+ab},
\]
where \(N_0(q)=1\) and the rank-stratum sum counts all \(q^{ab}\) bilinear forms. This agrees exactly with \(|A^*|\), completing the proof.

## Verification
Run `python3 verify.py` for direct finite-field commutator and stabilizer tests, and `python3 mass_identity.py` for independent arithmetic identities. The direct checker includes all functionals up to their arbitrary idempotent-dual coordinates for the parameter cases \((a,b,q)=(1,1,2),(1,1,3),(1,2,2),(1,2,3),(2,2,2),(2,2,3),(1,2,4)\). It evaluates commutators in the path basis, solves the full linear stabilizer constraints, checks orbit sizes, and in three small cases explicitly enumerates all units in the stabilizer. The order-four field uses \(\mathbb F_2[t]/(t^2+t+1)\), not integer arithmetic modulo four. The second program checks integrality, exact orbit-size mass, and matrix-rank mass in 288 further parameter configurations. Both produced the recorded pass markers. These finite checks corroborate but do not replace the proof for arbitrary \(q,a,b\).

## Relationship to prior work
Ning Yan's arXiv:1004.2674v1 (April 15, 2010), especially Sections 1 and 3, studies the unipotent upper-triangular group's action on the dual of its strictly upper-triangular algebra, and classifies certain coadjoint **clusters** under a double action. That does not provide the present full-unit coadjoint orbit-size distribution for arbitrary arrow multiplicities. The use of orbit-stabilizer and coadjoint stabilizers is classical, not claimed as new.

Ignatev and Titov's arXiv:2604.01358v1 (April 1, 2026), especially Proposition 3.1, enumerates coadjoint orbits of unipotent generalized Heisenberg groups using an alternating bilinear-form rank. This is close context for the nonzero radical-square contribution, but its acting group, representation space, and orbit sizes differ: it has no diagonal unit torus or the present mixed \((q-1)\)-factors. The new point here is the complete joint effect of the nonzero path-composition bilinear form and the three idempotent weights on all dual functionals.

## Limitations
This result enumerates coadjoint orbits by cardinality, not canonical representatives for every individual orbit. It is limited to the indicated three-vertex line with free parallel-arrow multiplicities and does not settle arbitrary higher-radical quivers, characteristic-dependent representation-theoretic correspondences, or unit-group conjugacy-class counts. A broader existing theorem might imply this specialization; comprehensive historical-priority verification and independent mathematical audit remain outstanding.

## References
1. N. Yan, *Representations of Finite Unipotent Linear Groups by the Method of Clusters*, arXiv:1004.2674v1, 2010-04-15. https://arxiv.org/abs/1004.2674
2. M. Ignatev and L. Titov, *On the Number of Irreducible Representations for Finite Unipotent Heisenberg-Type Groups*, arXiv:2604.01358v1, 2026-04-01. https://arxiv.org/abs/2604.01358
