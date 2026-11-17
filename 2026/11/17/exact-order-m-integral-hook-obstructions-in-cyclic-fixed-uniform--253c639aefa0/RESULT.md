# Exact order-\(m\) integral hook obstructions in cyclic-fixed uniform-matroid complexes

## Finding
For every \(m\ge4\), \(p\ge2\), and \(2\le k\le m-2\), consider the rank-\(kp\) uniform matroid \(U_{kp,mp+1}\) on the set \(\{0\}\sqcup\{(i,a):1\le i\le m,\ a\in\mathbb Z/p\mathbb Z\}\). Its independence complex \(K\) contains exactly the subsets of size at most \(kp\). The cyclic group \(H=C_p\) fixes \(0\) and acts by \((i,a)\mapsto(i,a+1)\); a commuting symmetric group \(S_m\) permutes the \(m\) cycles. Let \(X=|K|^H\) be the **geometric** fixed space.

There is an explicit \(S_m\)-equivariant PL homeomorphism
\[
 X\cong_{\mathrm{PL},S_m}|\operatorname{sk}_{k-1}\Delta^m|.
\]
All reduced integral homology of \(X\) vanishes except in degree \(k-1\), and
\[
 \widetilde H_{k-1}(X;\mathbb Z)\cong_{\mathbb Z[S_m]}\bigwedge^k P_m,
 \qquad P_m=\mathbb Z^m,
\]
with the standard signed exterior action on oriented subsets of \(k\) cycle labels. In particular \(X\simeq\bigvee^{\binom{m}{k}}S^{k-1}\).

**Sharp integral extension theorem.** Put \(A_m=\ker(\epsilon:P_m\to\mathbb Z)\), with \(\epsilon(e_i)=1\). The canonical contraction \(\iota_\epsilon\) gives a short exact sequence of **integral** \(S_m\)-modules
\[
 0\longrightarrow\bigwedge^k A_m
 \longrightarrow\widetilde H_{k-1}(X;\mathbb Z)
 \xrightarrow{\ \iota_\epsilon\ }\bigwedge^{k-1} A_m\longrightarrow0.
\]
Its Yoneda class has **exact additive order \(m\)** in
\[
 \operatorname{Ext}^{1}_{\mathbb Z[S_m]}\left(\bigwedge^{k-1} A_m,\bigwedge^{k} A_m\right).
\]
Consequently this natural sequence is non-split for every interior rank, although its rationalization splits into the two inequivalent hook Specht representations \(S^{(m-k+1,1^{k-1})}\) and \(S^{(m-k,1^k)}\). The topological skeleton and wedge formulas are known; the new assertion is the *uniform sharp integral extension order in every intermediate degree*, realized by these geometric fixed spaces.

## Assumptions and scope
All simplicial complexes and groups are finite. The uniform matroid rank means the cardinality of an independent set is at most \(kp\). The action is the simultaneous rotation of the \(p\)-cycles and the full commuting permutation action on cycle labels, not the complete automorphism action of the uniform matroid. Geometric fixed points of a realization are distinguished from vertexwise-fixed simplices and from quotient spaces. The notation \(\operatorname{Ext}^1\) refers to Yoneda extensions of left modules over the integral group ring; its class order is not torsion in homology. The parameter \(2\le k\le m-2\) specifically addresses interior hook degrees, distinct from the boundary-degree cyclic example treated in earlier work. Reduced integral homology is used throughout unless rational coefficients are explicitly indicated.

## Proof
**1. Actual fixed-point model.** A point of a simplex has unique barycentric coordinates. Under the order-\(p\) rotation, a point is fixed exactly when every one of its \(m\) cyclic coordinate blocks is constant. Write \(t_{i,a}=u_i/p\) and \(t_0=u_0\), with \(u_0+\sum_i u_i=1\). Because an original face consists of at most \(kp\) vertices, the support condition reads
\[
 p\cdot|\{i:u_i>0\}|+\mathbf1_{u_0>0}\le kp.
\]
If \(u_0=0\), at most \(k\) heavy orbit coordinates can be positive; if \(u_0>0\), at most \(k-1\) can be positive. These are *exactly* the subsets of at most \(k\) vertices of the \((m+1)\)-vertex simplex on labels \(\{0,1,\ldots,m\}\), i.e. its \((k-1)\)-skeleton. The coordinate map \((t_0,(t_{i,a}))\leftrightarrow(u_0,(u_i))\) and its inverse are linear on the respective simplices, continuous and mutually inverse, and commute with every permutation of the \(m\) heavy labels. This proves the claimed equivariant PL homeomorphism, without mistaking setwise invariant faces for individually fixed original vertices.

**2. Integral chain model and spheres.** Set \(Y=\operatorname{sk}_{k-1}\Delta^m\). The closed star \(C\) of vertex \(0\) is a cone, hence is contractible and preserved by \(S_m\). All faces of \(Y\) outside \(C\) are precisely its \(k\)-element subsets of heavy vertices \(\{1,\ldots,m\}\): every smaller heavy subset lies in the star because it can be joined to \(0\). The boundaries of these missing \((k-1)\)-simplices lie in \(C\). Hence the quotient \(Y/C\) is a bouquet of \(\binom{m}{k}\) spheres of dimension \(k-1\). Because \(C\subseteq Y\) is a contractible subcomplex, collapsing it is an ordinary homotopy equivalence. The relative oriented-cell generators give a **canonical integral** \(S_m\)-equivariant identification \(\widetilde H_{k-1}(Y;\mathbb Z)\cong H_{k-1}(Y,C;\mathbb Z)\cong\bigwedge^kP_m\): a permutation acts on an oriented heavy \(k\)-subset by the sign of the restricted reorder. All other reduced integral homology vanishes. This does not assert an equivariant wedge equivalence.

**3. The natural exact sequence.** Regard \(P_m\) as the free \(\mathbb Z\)-lattice on \(e_1,\ldots,e_m\), with \(\epsilon(e_i)=1\), and let \(A_m=\ker\epsilon\). The integral interior product \(\iota_\epsilon:\bigwedge^kP_m\to\bigwedge^{k-1}P_m\) satisfies
\[
 \iota_\epsilon(z_1\wedge\cdots\wedge z_k)
 =\sum_{j=1}^{k}(-1)^{j-1}\epsilon(z_j)
 z_1\wedge\cdots\wedge\widehat{z_j}\wedge\cdots\wedge z_k.
\]
Choose any basis element \(e_m\) with \(\epsilon(e_m)=1\). The underlying abelian lattice splits as \(P_m=A_m\oplus\mathbb Ze_m\). Therefore \(\bigwedge^kP_m=\bigwedge^kA_m\oplus (e_m\wedge\bigwedge^{k-1}A_m)\), and contraction kills the first summand and sends \(e_m\wedge z\) to \(z\). Its image is exactly \(\bigwedge^{k-1}A_m\), its kernel is exactly \(\bigwedge^kA_m\), and it is \(S_m\)-equivariant since \(\epsilon\) is invariant. This gives the asserted integral sequence.

**4. The extension class has order dividing \(m\).** Let \(v=e_1+\cdots+e_m\in P_m\). It is invariant under the whole symmetric group and \(\epsilon(v)=m\). For every \(z\in\bigwedge^{k-1}A_m\),
\[
 \iota_\epsilon(v\wedge z)=m z.
\]
Thus \(z\mapsto v\wedge z\) is an *integral* \(S_m\)-equivariant lift of \(m\) times the identity map on the quotient. By the long exact Hom–Ext sequence (equivalently, by the Baer multiplication description of extensions), multiplication by \(m\) annihilates the Yoneda class. After tensoring with \(\mathbb Q\), \((v/m)\wedge-\) is an equivariant splitting.

**5. Sharpness for every interior \(k\).** Over \(\mathbb Q\), the exterior powers \(\bigwedge^j(A_m\otimes\mathbb Q)\) are the irreducible hook Specht modules indexed by \((m-j,1^j)\). In particular \(\bigwedge^{k-1}A_{m,\mathbb Q}\) and \(\bigwedge^k A_{m,\mathbb Q}\) are nonisomorphic irreducibles, so
\[
 \operatorname{Hom}_{\mathbb Q[S_m]}(\bigwedge^{k-1}A_{m,\mathbb Q},\bigwedge^k A_{m,\mathbb Q})=0.
\]
Consequently any rational equivariant lift \(f\) of \(q\) times the identity is **unique**, because its difference from \((q/m)v\wedge-\) takes values in \(\bigwedge^kA_{m,\mathbb Q}\). Take the primitive wedge
\[
 z=(e_1-e_m)\wedge\cdots\wedge(e_{k-1}-e_m)\in\bigwedge^{k-1}A_m.
\]
Since \(k\le m-2\), the coefficient of \(e_1\wedge\cdots\wedge e_k\) in \(v\wedge z\) is \(\pm1\): it comes only from the \(e_k\) term in \(v\) and the \(e_1,\ldots,e_{k-1}\) terms in \(z\). Thus the unique rational lift \((q/m)v\wedge z\) is integral only if \(m\mid q\). It follows that no positive integer smaller than \(m\) kills the extension, whereas Step 4 shows that \(m\) does. The exact order is \(m\). This also proves non-splitting over the integers, independent of any finite experiment.

## Verification
The standalone `verify.py` uses only Python's standard library. For each \(p\in\{2,3,4\}\), \(2\le m\le6\), and \(1\le k<m\), it explicitly constructs the cyclic vertex permutation, enumerates the orbit-invariant independent-set supports directly in the original matroid, and computes reduced simplicial homology ranks over \(\mathbb F_2\). It compares them with the predicted simplex-skeleton groups. It identifies critical heavy faces, verifies their boundaries belong to the stable cone, and for every permutation of the heavy labels compares the signed exterior-power character with an independently calculated full simplicial alternating Lefschetz trace. The finite checker also tests the claimed primitive coefficient-divisibility pattern. It prints `UNIFORM_MATROID_ORBIT_EXTERIOR_CHECKS_PASS cases=45 symmetric_actions=12498 signed_trace_checks=12498`. The count refers to finite checks, **not** to a proof of any infinite family or to an independent computation of an Ext group; the exact Ext order is established in Proof Steps 4 and 5.

## Relationship to prior work
Pakianathan and Winfree established the scalar quota-complex wedge formula and its critical-face description. The present fixed-point model is a particularly simple quota complex and is **literally an ordinary simplex skeleton**; neither its standard wedge decomposition nor that identification alone is asserted as a new topological phenomenon. The published *Universal-apex higher independence complexes and unbounded equivariant splitting obstructions* already provides a canonical equivariant exterior-power exact sequence for simplex skeleta in the complete-graph specialization. It also proves an exact cyclic extension obstruction in the **extremal** degree. These results are acknowledged as covering the sequence itself and the extremal cyclic case. The distinct assertion here is the **exact order \(m\) over the entire \(S_m\)** in *every intermediate degree* \(2\le k\le m-2\), with a single sharp proof; its cyclic-fixed uniform-matroid realization makes this a natural geometric fixed-point invariant for an infinite family of nontrivial group actions. The previous multiclique fixed-point results concern different cell complexes and rational normalizer characters, not these exact integral extension orders. General papers on matroid symmetry representations and hook Specht modules provide representation-theoretic background but do not state this specific all-interior-rank integral extension computation.

## Limitations
The ambient weighted fixed-space model reduces to a familiar skeleton. The topological homotopy classification and the very existence of the natural exterior-power extension are not novel by themselves. The asserted additional result is an exact integral equivariant extension order, **not** an intrinsic torsion class of ordinary homology and not a proof that every rational splitting fails for every subgroup. The theorem is for the specified rank, cycle action, and commuting \(S_m\)-action; no general statement about all uniform-matroid subgroup actions is claimed. The rational hook-module irreducibility used in the sharpness proof is a standard characteristic-zero result. Historical representation-theoretic work may contain an equivalent exterior-power extension exponent under other terminology; this remains a publication-priority risk. There is no independent mathematical certification.

## References
1. J. Pakianathan and T. Winfree, *Quota Complexes, Persistent Homology and the Goldbach Conjecture*, arXiv:1104.4324v1, first public 2011-04-21, especially Theorem 2.3, https://arxiv.org/abs/1104.4324.
2. *Universal-apex higher independence complexes and unbounded equivariant splitting obstructions*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-universal-apex-higher-independence-complexes-and-unbounded-equiv--60080b49cdbc (the canonical sequence and extremal cyclic case).
3. L. Moci and G. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760, https://arxiv.org/abs/2001.03760.
4. Y. Jiang, *On the symmetric and exterior powers of Young permutation modules*, arXiv:1911.03220, https://arxiv.org/abs/1911.03220.
5. *Integral symmetry lattices of total two-cut complexes over clique–tree products*, published result on a different complex and order-\(m\) augmentation extension, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-symmetry-lattices-of-total-two-cut-complexes-over-cliqu--5f7d8e83034b.
6. *Exterior sixth-power symmetry in ninth Kneser-complex homology*, published result on a distinct complex with two rational hook constituents, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exterior-sixth-power-symmetry-in-ninth-kneser-complex-homology--d2b89996295b.
