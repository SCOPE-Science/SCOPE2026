# The unique finite-field rigidity point for local automorphisms of Heisenberg Lie algebras

## Finding
For every prime power \(q\) and positive integer \(m\), let \(H_m(\mathbb F_q)=V\oplus\mathbb F_q z\), with \(\dim V=2m\), be the Heisenberg Lie algebra defined by a nondegenerate alternating form \(\omega\) on \(V\): \([u+az,v+bz]=\omega(u,v)z\). A **linear local automorphism** is a linear map \(T\) such that for every element \(x\) there exists a Lie algebra automorphism \(g_x\), depending on \(x\), with \(T(x)=g_x(x)\).

The complete finite-field index and its rigidity boundary are
\[
[\operatorname{LocAut}(H_m(\mathbb F_q)):\operatorname{Aut}(H_m(\mathbb F_q))]
=q^{m(m-1)}\prod_{i=1}^{m}(q^{2i-1}-1).
\]
In particular the index is one **if and only if** \(q=2\) and \(m=1\). Hence the nonabelian, class-two, three-dimensional algebra \(H_1(\mathbb F_2)\) has **no proper linear local automorphisms**; its automorphism and linear local-automorphism groups each have order \(24\). Every other finite-field Heisenberg Lie algebra has a proper linear local automorphism. The next binary-rank case has index \(28\), whereas \(H_1(\mathbb F_3)\) has index \(2\).

These statements give the sharp finite-field boundary of the complex-field existence theorem of Atajonov, Khudoyberdiyev and Yusupov (arXiv:2610.40348v1, Theorem 4.4). **They do not contradict that theorem**, whose hypotheses specify complex Lie algebras.

## Assumptions and scope
The field is \(\mathbb F_q\), where \(q\) is any prime power, including characteristic two. The integer \(m\ge1\) is unrestricted. The bracket is alternating and bilinear, including in characteristic two. Only **linear** local automorphisms are considered. Standard group orders use the full group of \(\mathbb F_q\)-rational linear maps. Locality has the pointwise-witness definition above, not the stronger two-local requirement.

## Proof
**1. Ordinary automorphisms.** The derived algebra and the center coincide and equal \(\mathbb F_qz\). Every automorphism has a unique block form
\[
T(v+tz)=Av+(f(v)+\lambda t)z,
\qquad A\in\operatorname{GL}(V),\quad f\in V^*,\quad\lambda\in\mathbb F_q^\times.
\]
It preserves the bracket exactly when
\[
\omega(Au,Av)=\lambda\omega(u,v)
\quad\text{for every }u,v\in V.
\]
Thus \(A\) lies in \(\operatorname{GSp}(V,\omega)\), with similitude factor \(\lambda\); \(f\) is unconstrained. The multiplier map \(\operatorname{GSp}_{2m}(q)\to\mathbb F_q^\times\) is surjective: in a symplectic basis, scale one of the paired Lagrangian halves by \(\lambda\). Its kernel is \(\operatorname{Sp}_{2m}(q)\). Therefore
\[
|\operatorname{Aut}(H_m(\mathbb F_q))|=q^{2m}(q-1)|\operatorname{Sp}_{2m}(q)|.
\]

**2. All linear local automorphisms.** If \(T\) is local then it is injective: \(T(x)=0\) implies \(g_x(x)=0\) and hence \(x=0\). Finite-dimensional injectivity is bijectivity. At the center element, \(T(z)=g_z(z)\in\mathbb F_q^\times z\). Thus its block form is as above with \(A\in\operatorname{GL}(V)\), arbitrary \(\lambda\in\mathbb F_q^\times\), and arbitrary \(f\in V^*\); no symplectic condition has yet been imposed.

Conversely fix such a block map \(T\) and \(x=v+tz\). If \(v=0\), choose an ordinary automorphism with multiplier \(\lambda\), obtainable by the Lagrangian scaling above, and with zero central functional. This sends \(x\) to \(T(x)\). If \(v\ne0\), there is a symplectic automorphism \(S\in\operatorname{Sp}(V)\) with \(Sv=Av\). To see this over **every field**, choose \(v'\) with \(\omega(v,v')=1\) and \(w'\) with \(\omega(Av,w')=1\), extend both pairs to symplectic bases, and send the first basis to the second. Next choose \(h\in V^*\) with
\[
h(v)=f(v)+(\lambda-1)t.
\]
Then the ordinary automorphism \(g_x(u+sz)=Su+(h(u)+s)z\) agrees with \(T\) on \(x\). This proves the exact local block classification over any field, including \(\mathbb F_2\):
\[
\operatorname{LocAut}(H_m(\mathbb F_q))
=\left\{\begin{pmatrix}A&0\\f&\lambda\end{pmatrix}:A\in\operatorname{GL}_{2m}(q),\ f\in(\mathbb F_q^{2m})^*,\ \lambda\in\mathbb F_q^\times\right\}.
\]
Consequently
\[
|\operatorname{LocAut}(H_m(\mathbb F_q))|=q^{2m}(q-1)|\operatorname{GL}_{2m}(q)|.
\]

**3. Exact quotient and the unique equality case.** The standard finite classical-group order identities are
\[
|\operatorname{GL}_{2m}(q)|=q^{m(2m-1)}\prod_{j=1}^{2m}(q^j-1),
\qquad
|\operatorname{Sp}_{2m}(q)|=q^{m^2}\prod_{i=1}^{m}(q^{2i}-1).
\]
Dividing yields
\[
[\operatorname{LocAut}:\operatorname{Aut}]
=q^{m(m-1)}\prod_{i=1}^{m}(q^{2i-1}-1).
\]
Every factor is a positive integer. The index equals one only when \(m=1\) and \(q-1=1\), that is, \((q,m)=(2,1)\). This is also evident directly at that point: \(\mathbb F_2^\times=\{1\}\), and every invertible \(2\)-by-\(2\) matrix has determinant one, hence is symplectic. Here \(|\operatorname{GL}_2(2)|=6\) and \(q^{2m}=4\), giving \(24\) maps in both groups. For \((q,m)=(2,2)\), the quotient is \(2^2(2-1)(2^3-1)=28\). For \((3,1)\), it is \(2\). No complex-field argument is extended by an unverified change of characteristic; the construction in Step 2 is field-independent.

## Verification
The standalone file `verify.py` enumerates all \(2^9=512\) and \(3^9=19683\) linear maps on the three-dimensional Lie algebras over \(\mathbb F_2\) and \(\mathbb F_3\), respectively. For every candidate and every vector, it directly tests whether an independently enumerated **ordinary automorphism** agrees with the map on that vector; it then compares with the proved block criterion. The results are exactly \(24/24\) local/ordinary automorphisms over \(\mathbb F_2\), and \(864/432\) over \(\mathbb F_3\). It additionally checks the group-order quotient formula for \(q\in\{2,3,4,5\}\) and \(m\in\{1,2,3\}\), and independently enumerates all \(2^{16}=65536\) binary \(4\)-by-\(4\) matrices to obtain \(|\operatorname{GL}_4(2)|=20160\) and \(|\operatorname{Sp}_4(2)|=720\). Run `python verify.py`; the expected terminal marker is `VERIFY_OK all_linear_matrices=20195 finite_fields=2 group_order_cases=12 sp4_direct=65536`. Finite enumeration is a check, **not** the proof of the universal statement.

## Relationship to prior work
Atajonov–Khudoyberdiyev–Yusupov (2026), Theorem 4.4, proves existence of proper local automorphisms for all nonabelian finite-dimensional **complex** nilpotent Lie algebras. Their proof in nilpotency class two uses scalar \(1/2\) and square roots. The present boundary identifies the first finite field where the analogous unrestricted field assertion fails, and its exact quantitative deficiency across the entire finite Heisenberg family. No claim is made about a defect in the published complex result.

Sheng–Liu–Miao (2024/2025) explicitly investigates the **forms of local automorphisms** of Heisenberg Lie (super)algebras. The field-independent block characterization in Steps 1–2 should be regarded as supporting material, **not claimed as a new characteristic-zero classification**. The contribution evaluated here is the finite-field index law and the unique binary rigidity point. Their complete 12-page primary text was not obtainable through accessible open routes; the possibility that it already implies even the finite-field result is a historical-priority risk requiring independent full-text comparison. Ayupov–Kudaybergenov (2016) studies general two-local automorphisms over algebraically closed fields of characteristic zero; that does not assert the specific finite-field local-automorphism index.

## Limitations
The formula is restricted to ordinary Heisenberg Lie algebras, not arbitrary nilpotent Lie algebras or Heisenberg Lie superalgebras. It concerns **linear local automorphisms**, not arbitrary nonlinear two-local maps. The 2024/2025 Sheng–Liu–Miao full-text comparison remains inaccessible; the claim of historical originality is therefore qualified. The assertion concerns the finite-field extension of a **complex** existence phenomenon and does not contradict its hypotheses.

## References
1. K. Atajonov, A. Khudoyberdiyev and B. Yusupov, *Local Derivations and Local Automorphisms of Arbitrary Finite-Dimensional Nilpotent Lie and Leibniz Algebras*, arXiv:2610.40348v1 (first public 2026-10-29), especially Theorem 4.4. https://arxiv.org/abs/2610.40348
2. Y. Sheng, W. Liu and X. Miao, *Local and Linear 2-local Automorphisms of Heisenberg Lie (Super)algebras*, *Frontiers of Mathematics*, DOI:10.1007/s11464-023-0061-6 (online journal 2025-03-28; research record 2024). https://doi.org/10.1007/s11464-023-0061-6
3. S. Ayupov and K. Kudaybergenov, *2-Local automorphisms on finite-dimensional Lie algebras*, arXiv:1602.05187v1 (2016). https://arxiv.org/abs/1602.05187
