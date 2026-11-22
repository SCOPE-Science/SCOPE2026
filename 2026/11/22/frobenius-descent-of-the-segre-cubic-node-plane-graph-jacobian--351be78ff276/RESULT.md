# Frobenius descent of the Segre-cubic node–plane graph Jacobian

## Finding

Let \(k=\mathbb F_q\) have characteristic at least \(7\), and let \(X/k\) be a form of the ten-nodal Segre cubic. Its ten geometric nodes and fifteen geometric distinguished planes form a canonical bipartite incidence graph \(\Gamma_X\) with \(25\) vertices and \(60\) edges. Let \(K(\Gamma_X)=\operatorname{Div}^0(\Gamma_X)/L\mathbb Z^{25}\) be its **integral graph Jacobian**, where \(L\) is the graph Laplacian. The underlying geometric group is

\[
K(\Gamma_X)\cong(\mathbb Z/2)^6\oplus(\mathbb Z/10)^2\oplus\mathbb Z/20\oplus\mathbb Z/40\oplus(\mathbb Z/80)^4.
\]

The Galois action factors through the coordinate-label group \(S_6\). If \(\sigma\in S_6\) represents geometric Frobenius, the finite coinvariant group \(K(\Gamma_X)_\sigma=K(\Gamma_X)/(\sigma-1)K(\Gamma_X)\) has **exactly** the following eleven possibilities. In the third column the notation \(m^r\) means \(r\) cyclic factors \(\mathbb Z/m\); a solitary \(m\) denotes one such factor.

| Frobenius cycle type | Nonunit invariant factors of \(K(\Gamma_X)_\sigma\) | Number of rational graph-Jacobian classes |
|---|---|---:|
| \((1^6)\) | \(2^6,10^2,20,40,80^4\) | \(2^{29}5^8\) |
| \((2,1^4)\) | \(2^5,10^2,20,80^2\) | \(2^{17}5^5\) |
| \((2^2,1^2)\) | \(2^4,20,40,80^2\) | \(2^{17}5^4\) |
| \((2^3)\) | \(2^4,20,40,80^3\) | \(2^{21}5^5\) |
| \((3,1^3)\) | \(2^4,20,40\) | \(2^{9}5^2\) |
| \((3,2,1)\) | \(2^3,20\) | \(160\) |
| \((3^2)\) | \(4,8,80^2\) | \(204800\) |
| \((4,1^2)\) | \(2^3,4,80\) | \(2560\) |
| \((4,2)\) | \(2^3,20,80\) | \(12800\) |
| \((5,1)\) | \(20,40\) | \(800\) |
| \((6)\) | \(4,8,80\) | \(2560\) |

The fixed group \(K(\Gamma_X)^\sigma\) is abstractly isomorphic to \(K(\Gamma_X)_\sigma\) (without asserting a canonical isomorphism). Thus the displayed invariant factors classify the rational points of the finite étale group scheme obtained by descending this graph Jacobian along the Segre-cubic form. The group orders can equally be obtained by multiplying the displayed invariant factors. In particular, a six-cycle has \(2560\) rational classes, a five-cycle with a fixed label has \(800\), and a cycle type \((3,2,1)\) has only \(160\), although the geometric group is constant throughout.

## Assumptions and scope

The geometric configuration is defined over an algebraic closure of \(k\). Every form is considered via the natural \(S_6\)-action on the ten nodes and fifteen pairing planes, as established for Segre forms in the classical coordinates. The assertion is about an **abstract graph Jacobian/critical group** and its finite Galois module, **not** the divisor-class group, Picard group, Chow group, Néron–Severi group, or Brauer group of the Segre cubic. We make no assertion that the graph Jacobian embeds in any such group.

## Proof

**1. Integral incidence model.** Take a six-label set \(E=\{0,1,2,3,4,5\}\). Index the ten nodes by unordered complementary triples \(\{T,E\setminus T\}\), \(\lvert T\rvert=3\). Index the fifteen distinguished planes by perfect matchings \(M\) of \(E\). A node is on a plane exactly when all three matching edges cross the two triples. Define the \(10\times15\) incidence matrix \(I\) by this rule. Each node has degree six and each plane degree four. Two distinct nodes share exactly two planes, hence
\[
II^{\mathsf T}=4I_{10}+2J_{10}.
\]
The \(25\times25\) graph Laplacian, with node vertices first, is
\[
L=\begin{pmatrix}6I_{10}&-I\\-I^{\mathsf T}&4I_{15}\end{pmatrix}.
\]
Here the block \(I\) without a subscript is the incidence matrix, while \(I_r\) denotes an identity matrix.

**2. Geometric graph Jacobian.** The matrix identity gives the characteristic polynomial
\[
\det(tI_{25}-L)=t(t-10)(t-4)^5(t^2-10t+20)^9.
\]
The matrix-tree theorem therefore yields \(\#K(\Gamma_X)=\tau(\Gamma_X)=2^{29}5^8\). Over the integers, delete any one row and column of \(L\); its Smith normal form has ten unit factors and the nonunit factors
\[
2^6,\quad10^2,\quad20,\quad40,\quad80^4.
\]
The attached exact verifier constructs \(I,L\) from the six labels and executes an integer-domain Smith normal form; this is an exhaustive calculation on a single explicitly determined \(24\times24\) matrix. The product of the factors equals the independent spectral spanning-tree count. This proves the geometric group statement.

**3. Coinvariants and an integral presentation.** Let \(\operatorname{Div}^0(\Gamma_X)\subset\mathbb Z^{25}\) be the degree-zero divisors. Fix one root vertex \(r\); the vectors \(e_v-e_r\), for the \(24\) other vertices, form an integral basis. In this basis, the graph Laplacian image is presented by the \(24\times25\) matrix \(R\) formed by deleting row \(r\) from \(L\). If \(g\) is the vertex permutation induced by \(\sigma\), write
\[
C_{w,v}=[g(v)=w]-[g(r)=w]-[v=w],\qquad w,v\ne r.
\]
The columns of \(C\) are exactly the images of \((\sigma-1)(e_v-e_r)\) in the chosen basis. Therefore **over the integers**, without dividing by the orbit lengths,
\[
K(\Gamma_X)_\sigma\cong\operatorname{coker}_{\mathbb Z}[\,R\mid C\,].
\]
This \(24\times49\) presentation is crucial: merely taking the graph quotient or counting Frobenius vertex orbits does not compute the integral coinvariants.

**4. Complete case calculation.** Conjugacy classes of \(S_6\) are indexed by the eleven partitions of six. For each partition choose the permutation that cycles consecutive blocks, act on the unordered triples and perfect matchings, and perform the exact integer Smith computation of \([R\mid C]\). The resulting nonunit factors are exactly the eleven rows above. The supplied executable constructs all eleven matrices from scratch, performs their Smith normal forms with three *different* choices of root vertex, and checks the entire \(720\)-element \(S_6\) action preserves the incidence relation. The eleven representatives exhaust every possible conjugacy class, so the result applies to every Frobenius permutation, not merely a sample of finite fields.

**5. Fixed-group interpretation.** The finite graph Jacobian has a canonical perfect symmetric monodromy pairing with values in \(\mathbb Q/\mathbb Z\), obtained from the rational pseudoinverse of the Laplacian modulo integers. Every automorphism of the graph preserves this pairing. Consequently it identifies the \(S_6\)-module \(K(\Gamma_X)\) with its Pontryagin dual. The dual of the coinvariants is the fixed subgroup of the dual module, so \(K(\Gamma_X)^\sigma\) is the dual of \(K(\Gamma_X)_\sigma\). Finite abelian groups are abstractly isomorphic to their duals, proving the fixed-group assertion and hence the rational-class counts.

## Verification

Install the declared dependency with `python -m pip install -r requirements.txt` and run `python verify_segre_graph.py`. The program uses exact integer arithmetic throughout. It checks the incidence row and column sums, \(II^{\mathsf T}\), the Laplacian polynomial, all \(720\) coordinate relabellings, the Smith factor table for all eleven types at three roots, and the spanning-tree determinant and factor product. Its success message is `SEGRE_GRAPH_FROBENIUS_INTEGRAL_VERIFIED_OK`. The proof of the fixed/coinvariant identification uses the standard perfect critical-group pairing in addition to these finite calculations.

## Relationship to prior work

Dolgachev (2015) and Avilov (2018) establish the ten-node, fifteen-plane Segre incidence and its coordinate symmetry; these geometric inputs are not claimed. A published calculation titled *Integral Frobenius coinvariants of the Segre cubic node–plane incidence* determines the cokernel of the **rectangular map** \(\mathbb Z^{15}\to\mathbb Z^{10}\), not the graph Jacobian \(\operatorname{Div}^0/(L\mathbb Z^{25})\). Its underlying group has order \(64\), whereas the present group's order is \(2^{29}5^8\), and neither its group nor its eleven-class formula implies the present Smith results. Likewise the published *Frobenius spectra of the sixty node–plane incidence flags of trace Segre cubics* counts finite étale flags but does not compute integer chip-firing relations. General sandpile-group and graph-Jacobian results provide the language, not these explicit eleven integral groups.

## Limitations

The theorem is conditional on the standard geometrically split Segre-cubic node/plane configuration in characteristic at least seven; it does not claim unrelated arithmetic invariants of the threefold. The distinction between graph Jacobians and the threefold's algebraic-geometric class groups is essential. The finite integral computations completely establish the eleven specified cases but do not prove exhaustive historical priority: a previously unindexed combinatorial-design Smith calculation could subsume them. The rational fixed/coinvariant isomorphism is abstract, not canonical.

## References

- Igor Dolgachev, *Corrado Segre and nodal cubic threefolds*, arXiv:1501.06432v1 (first posted 2015-01-26), especially §2, Proposition 2.2, and the symmetric model.
- Artem Avilov, *On forms of the Segre cubic*, arXiv:1812.11363v1 (posted 2018-12-29), especially §2, Definition 2.1 and Proposition 2.11.
- *Integral Frobenius coinvariants of the Segre cubic node–plane incidence*, publicly accessible research result at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-frobenius-coinvariants-of-the-segre-cubic-node-plane-in--be1de342035c (distinct rectangular incidence cokernel).
- *Frobenius spectra of the sixty node–plane incidence flags of trace Segre cubics*, publicly accessible research result at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-frobenius-spectra-of-the-sixty-node-plane-incidence-flags-of-tra--4c734c76e2d7 (distinct finite étale orbit count).
