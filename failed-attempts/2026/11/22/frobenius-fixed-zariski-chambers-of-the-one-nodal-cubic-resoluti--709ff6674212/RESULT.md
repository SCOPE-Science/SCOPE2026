# Frobenius-fixed Zariski chambers of the one-nodal cubic resolution

## Finding

Let \(q\) be any prime power of characteristic at least five. Let \(B\) be a Frobenius-stable, reduced degree-six divisor on a smooth \(\mathbb F_q\)-conic, consisting of six distinct geometric points. Let \(X\) be the blowup of \(\mathbb P^2_{\mathbb F_q}\) at \(B\); the conic is understood to be embedded in the plane. Let \(\sigma\in S_6\) be the Frobenius permutation on the geometric points of \(B\). A *rational Zariski chamber* means a chamber of the big cone of the real Néron–Severi space over \(\mathbb F_q\), equivalently a Frobenius-stable negative-definite geometric support (see proof).

The number of rational chambers depends only on the partition of six specifying the cycle type of \(\sigma\), as follows. The final column gives the **complete** distribution by cardinality of the geometric negative support, in order \(0,1,\ldots,6\); a Frobenius orbit of components contributes its individual geometric components to the support size.

| Frobenius cycle partition | \(S_6\) class size | Rational chambers | Geometric support sizes \(0,\ldots,6\) |
|---|---:|---:|---|
| \(1,1,1,1,1,1\) | 1 | **1898** | \(1,22,156,490,725,447,57\) |
| \(2,1,1,1,1\) | 15 | **468** | \(1,12,50,106,147,127,25\) |
| \(2,2,1,1\) | 45 | **118** | \(1,6,16,30,29,27,9\) |
| \(2,2,2\) | 15 | **24** | \(1,4,6,6,3,3,1\) |
| \(3,1,1,1\) | 40 | **113** | \(1,7,15,13,26,39,12\) |
| \(3,3\) | 40 | **11** | \(1,1,0,4,2,0,3\) |
| \(4,1,1\) | 90 | **26** | \(1,4,4,0,3,9,5\) |
| \(4,2\) | 90 | **8** | \(1,2,2,0,1,1,1\) |
| \(5,1\) | 144 | **8** | \(1,2,1,0,0,2,2\) |
| \(3,2,1\) | 120 | **33** | \(1,3,5,7,6,7,4\) |
| \(6\) | 120 | **3** | \(1,1,0,0,0,0,1\) |

The \(1898\) geometric chambers in the identity row are a previously published count and **are not claimed as new**. The new classification includes all eleven rational-support distributions and, more strongly, the complete Frobenius cycle decomposition of the chamber set in `nodal_cubic_chambers_results.json`. The natural combinatorial \(S_6\)-action on all geometric chambers has exactly \(39\) orbits; its orbit-size multiset is also in that JSON file. In the six-cycle case exactly three chambers descend: the nef chamber, the chamber supported on the strict conic \(Q\), and the chamber supported on all six geometric exceptional divisors \(E_1,\ldots,E_6\). All eleven cycle types are realizable for every \(q\) under consideration.

## Assumptions and scope

Over an algebraic closure, write \(H\) for the plane-line pullback and \(E_i\) for the six exceptional curves. The other negative curves are the fifteen strict line transforms \(L_{ij}=H-E_i-E_j\) and the strict conic \(Q=2H-\sum_iE_i\). Their self-intersections are \(-1\) and \(-2\), respectively. The anticanonical class has square three. The surface is the minimal resolution of its anticanonical cubic with one \(A_1\) singularity. Labels are merely geometric bookkeeping; the abstract \(S_6\) incidence action is **not** asserted to arise from actual automorphisms of every surface.

The result requires that the six geometric points be distinct on a smooth rational conic. It does not treat arbitrary configurations of six points, characteristic-dependent degenerations, or chambers over a non-finite imperfect field.

## Proof

**Geometric negative curves and intersection form.** The complete list follows by adjunction, anticanonical nefness, and Bézout with the strict conic. For a nonexceptional irreducible curve distinct from \(Q\), its plane image has degree \(d\) and multiplicities \(m_i\) satisfying \(\sum_i m_i\le2d\). Hence \((-K_X)\cdot C=3d-\sum_i m_i\ge d\), which forces a negative curve to be a line through two of the marked points. The conic provides the sole \((-2)\)-curve. This reproduces the prior geometric support classification rather than asserting it is novel. The Picard intersection pairing has diagonal \((1,-1,-1,-1,-1,-1,-1)\) in the indicated basis.

For \(i\ne j\) and distinct pairs, the intersection numbers are
\[
E_i\cdot E_j=0,\quad E_i\cdot L_{jk}=\mathbf 1_{i\in\{j,k\}},\quad
L_{ij}\cdot L_{kl}=\mathbf 1_{\{i,j\}\cap\{k,l\}=\varnothing},\quad
Q\cdot E_i=1,\quad Q\cdot L_{ij}=0.
\]
A selection of \((-1)\)-curves is negative definite exactly when its members are pairwise disjoint. If \(Q\) is also selected, the Schur complement of the \((-1)\)-block equals \(-2+s\), where \(s\) is the number of selected exceptional curves. Thus \(Q\) may be included if and only if \(s\le1\).

**Equivariant support enumeration.** Identify each \(L_{ij}\) with the edge \(\{i,j\}\) of \(K_6\). For a chosen set \(U\) of exceptional-curve labels, line edges must avoid \(U\), and the chosen line edges must be pairwise intersecting as subsets of the remaining labels. The empty family is permitted. Let \({\cal E}_\sigma(U)\) denote the \(\sigma\)-invariant families of pairwise intersecting edges among the labels outside \(U\). For a Frobenius permutation \(\sigma\), an explicit fixed-support polynomial is
\[
Z_\sigma(t)=\sum_{\substack{U\subseteq[6]\\\sigma U=U}}t^{|U|}
\left(1+\mathbf1_{|U|\le1}t\right)
\sum_{F\in{\cal E}_\sigma(U)}t^{|F|}.
\]
The expression applies uniformly to all eleven partitions. Enumerate invariant label-orbit blocks in \(U\), then invariant edge-orbit blocks \(F\); reject precisely those unions containing two disjoint edges. This gives the eleven integer coefficient vectors in the Finding table. It independently yields the previously known identity profile \((1,22,156,490,725,447,57)\). The resulting support classes are stable under the indicated permutation because \(Q\) itself is Frobenius-fixed.

**Descent of chambers.** The standard correspondence associates a Zariski chamber of the big cone to a negative-definite support of irreducible geometric curves. If a chamber is defined over \(\mathbb F_q\), its negative support is Frobenius-stable by uniqueness of the Zariski decomposition. Conversely, given a Frobenius-stable negative-definite support, the sum of its curves is a rational effective divisor. Choose a rational ample divisor \(A\) and sufficiently large rational coefficients on the Frobenius-orbit sums of its components. The nef/negative linear equations associated to that negative-definite matrix then give a rational big divisor with precisely the prescribed support. In particular, the fixed-support counts equal the numbers of rational chambers; separate geometric supports cannot collapse in this correspondence. The same argument applies to supports containing \(Q\).

**Full orbit count and order-six boundary.** The action of adjacent transpositions on the \(1898\) supports gives \(39\) orbits directly. Burnside's formula independently yields
\[
\frac1{720}\sum_{[\sigma]\subseteq S_6}|[\sigma]|\cdot Z_\sigma(1)=39.
\]
For a six-cycle the only possible invariant subsets of exceptional labels are the empty set and all six; the latter is incompatible with any line curve or \(Q\). The orbit of any line edge under the six-cycle contains two disjoint edges, so no nonempty invariant line family is allowed. Exactly the three supports stated in Finding remain.

For every finite field \(\mathbb F_q\), a smooth conic is isomorphic to \(\mathbb P^1\), and irreducible closed points of every positive degree exist on it. Choose distinct closed points of degrees given by a partition of six: this gives the required Frobenius type (for \(q\ge5\), there are six rational points for the split type). Thus the eleven cases are realized, not merely formal permutations.

## Verification

The standalone dependency-free checker `nodal_cubic_chambers.py` reconstructs the \(22\) divisor classes and exact intersection pairing, builds all \(1898\) allowed supports, verifies Sylvester's negative-definiteness inequalities for every support, and exhaustively applies all \(720\) permutations. It computes all eleven conjugacy-class distributions, the complete cycle profiles, and both the Burnside and direct \(39\)-orbit totals. Its output is `nodal_cubic_chambers_output.txt`, and the structured finite certificates are `nodal_cubic_chambers_results.json`.

The second, algorithmically different checker `nodal_cubic_independent.py` independently counts invariant exceptional-orbit blocks and line-edge-orbit blocks without looping through the \(1898\)-support set; the output is `nodal_cubic_independent_output.txt`. The checks use exact integer arithmetic. The finite enumeration is exhaustive because all \(22\) geometric negative curves have already been classified, and a negative-definite support has cardinality at most six by the Picard signature. The computer calculations do not themselves establish the geometric classification or the arithmetic descent argument; those are the preceding mathematical steps.

## Relationship to prior work

The geometric \(1898\)-chamber polynomial, the \(648\) supports containing \(Q\), and the star/triangle characterization of line edges were established in the prior public result cited below. They are used as a known combinatorial baseline, not relabeled as discoveries. That result expressly does not address arithmetic descent. Bauer–Funke–Neumann establish the general negative-support chamber correspondence, while Derenthal–Joyce–Teitler treat generalized del Pezzo geometry, its root lattice and nef-cone volumes. The present addition is a complete Frobenius-equivariant calculation: eleven fixed-support profiles, the complete chamber cycle distributions, and the \(39\) quotient orbits of the natural label action. These require evaluating group actions on the permitted support families, rather than just the ordinary count. No claim is made that the standard correspondence, the ordinary count or the root framework was unknown.

## Limitations

The \(S_6\) orbit number describes the abstract labeled configuration; for special six-point moduli, actual surface automorphisms can be smaller or different. No geometric moduli classification or chamber-volume computation is attempted. Statements about rational chambers refer to chamber supports of the real arithmetic Néron–Severi space, not individual geometrically irreducible negative curves over the ground field. Published prior results could conceivably encode an equivalent equivariant table in an unindexed appendix or specialist classification, and historical priority merits independent scrutiny. Independent mathematical audit has not been performed.

## References

1. U. Derenthal, M. Joyce, Z. Teitler, *The nef cone volume of generalized Del Pezzo surfaces*, arXiv:math/0703202 (first public 2007-03-07), https://arxiv.org/abs/math/0703202.
2. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (first public 2009-12-04), https://arxiv.org/abs/0912.0958.
3. Prior published computation, *Zariski-chamber spectrum of the one-nodal cubic’s minimal resolution*, full RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-zariski-chamber-spectrum-of-the-one-nodal-cubic-s-minimal-resolu--4b531d234d53/RESULT.md.
4. T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373, https://arxiv.org/abs/1204.4373.

