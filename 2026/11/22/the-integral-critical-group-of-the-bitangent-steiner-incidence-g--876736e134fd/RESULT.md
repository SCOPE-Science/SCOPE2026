# The integral critical group of the bitangent–Steiner incidence graph of a plane quartic

## Finding

Let \(C\) be any smooth geometrically connected nonhyperelliptic genus-three curve over a field of characteristic different from \(2\). Its \(28\) geometric bitangents (odd theta characteristics) and \(63\) geometric Steiner complexes form the bipartite graph \(\Gamma_C\), with an edge precisely when a bitangent belongs to a complex. The complete integral graph Jacobian is

\[
\boxed{K(\Gamma_C)\cong
(\mathbb Z/2\mathbb Z)^6\oplus
(\mathbb Z/4\mathbb Z)^{20}\oplus
(\mathbb Z/12\mathbb Z)^9\oplus
\mathbb Z/132\mathbb Z\oplus
(\mathbb Z/924\mathbb Z)^{20}\oplus
(\mathbb Z/1848\mathbb Z)^6.}
\]

In particular, the exponent is \(1848\), the group order (the number of spanning trees) is

\[
\tau(\Gamma_C)=2^{124}3^{36}7^{26}11^{27},
\]

and \(\Gamma_C\) has \(91\) vertices, \(756\) edges, and first Betti number \(666\). The listed factors are ordered by divisibility and omit \(28\) unit Smith entries. This is the geometric abstract graph Jacobian; no Frobenius-module classification is asserted.

## Assumptions and scope

Work over an algebraic closure and identify \(V=\operatorname{Jac}(C)[2]\cong\mathbb F_2^6\) with a six-dimensional symplectic space. A theta characteristic gives a quadratic refinement of the Weil pairing. Fix standard coordinates \((x,y)\in\mathbb F_2^3\oplus\mathbb F_2^3\), symplectic form

\[
\omega((x,y),(x',y'))=x\cdot y'+x'\cdot y,
\qquad q_0(x,y)=x\cdot y.
\]

The \(28\) odd refinements are \(q_v=q_0+\omega(v,-)\), indexed by \(v\in V\) satisfying \(q_0(v)=1\). The \(63\) Steiner complexes are \(\Sigma(a)\), indexed by \(a\in V\setminus\{0\}\). Classical theta geometry gives the incidence criterion

\[
q_v\in\Sigma(a)\quad\Longleftrightarrow\quad q_v(a)=q_0(a)+\omega(v,a)=0.
\]

Thus the graph is canonical up to isomorphism and is independent of the chosen coordinates, plane-quartic equation, and algebraic closure. Its edges are *bitangent-to-complex memberships*, not line intersections. The node count and critical group are geometric, valid for every stated curve. A graph critical group is the cokernel of any reduced integral Laplacian.

## Proof

**1. Incidence parameters.** Let \(B\) be the \(28\times63\) integer zero-one matrix with entries \(B_{v,a}=1\) when \(q_v(a)=0\). An odd six-variable quadratic form has \(28\) zero vectors, including zero; hence every row has exactly \(27\) ones. For each nonzero \(a\), exactly \(12\) odd quadratic refinements vanish on \(a\); hence every column has \(12\) ones. The total is \(28\cdot27=63\cdot12=756\) edges.

For two distinct odd refinements \(q,q'\), write \(q'=q+\omega(d,-)\), where \(d\ne0\). Equality of their Arf invariants forces \(q(d)=0\). Their common nonzero zero vectors are obtained from the zeros of \(q\) on \(d^\perp\), excluding the zero vector. The quadratic form descends to an odd nondegenerate form on the four-dimensional symplectic quotient \(d^\perp/\langle d\rangle\), with exactly six zero vectors. Each has two lifts, and one of the twelve lifts is zero. Thus distinct rows share exactly eleven columns. Consequently,

\[
BB^{\mathsf T}=16I_{28}+11J_{28}.
\]

This proves connectivity as well: any two bitangent vertices have a common complex, and all complex vertices are nonisolated.

**2. Rational spectral part.** In bitangent/complex order the integral Laplacian is

\[
L=\begin{pmatrix}27I_{28}&-B\\-B^{\mathsf T}&12I_{63}\end{pmatrix}.
\]

The Gram identity yields eigenvalues \(324\) once and \(16\) twenty-seven times for \(BB^{\mathsf T}\). On each nonzero singular-vector plane of \(B\), the eigenvalue equation is

\[
(27-\lambda)(12-\lambda)=\sigma^2.
\]

For \(\sigma^2=324\) this gives \(\lambda=0,39\); for \(\sigma^2=16\) this gives \(\lambda=11,28\), each twenty-seven times. The additional thirty-five kernel vectors of \(B\) produce \(\lambda=12\). Hence

\[
\operatorname{Spec}(L)=0^1,39^1,28^{27},11^{27},12^{35}.
\]

Kirchhoff's matrix-tree theorem gives

\[
\det L_{\mathrm{red}}=\frac{39\cdot 28^{27}\cdot11^{27}\cdot12^{35}}{91}
=2^{124}3^{36}7^{26}11^{27}.
\]

This determines the possible torsion primes, not their integral invariant factors.

**3. Prime-local Smith computation.** The accompanying self-contained `verify_steiner_graph.py` reconstructs the \(91\times91\) Laplacian directly from the six binary coordinates. It reduces a \(90\times90\) deleted-vertex Laplacian over \(\mathbb Z/p^e\mathbb Z\), using \(e=6\) for \(p=2\), and \(e=4\) for each of \(p=3,7,11\). At step \(k\), choose an entry of minimum \(p\)-adic valuation \(v\) in the remaining block. Its unit part has an inverse modulo \(p^{e-v}\), and every other entry in its row or column is divisible by \(p^v\). Therefore row and column additions of multiples of the pivot row and column diagonalize that factor using only invertible elementary operations. Every selected pivot valuation is strictly less than \(e\), so the finite-modulus calculation gives the *full* integral local Smith valuations, not merely lower bounds or a finite-sample conjecture.

For both a deleted bitangent vertex and a deleted Steiner vertex, the exact pivot-valuation multiplicities are

| Prime | Valuation zero | Valuation one | Valuation two | Valuation three |
|---|---:|---:|---:|---:|
| \(2\) | 28 | 6 | 50 | 6 |
| \(3\) | 54 | 36 | 0 | 0 |
| \(7\) | 64 | 26 | 0 | 0 |
| \(11\) | 63 | 27 | 0 | 0 |

Independent modular Gaussian ranks confirm each valuation-zero count. Their weighted valuations are exactly \(124,36,26,27\), matching the matrix-tree determinant. Combining the local valuations in ascending order yields the \(28\) units and the \(62\) nontrivial invariant factors stated in the finding. This finishes the integral Smith calculation.

**4. Stable-curve interpretation.** Since each vertex has valence \(12\) or \(27\), one can glue smooth rational components at distinct marked points according to this graph to obtain stable nodal curves with dual graph \(\Gamma_C\), at least over sufficiently large fields. Such a curve has arithmetic genus \(756-91+1=666\). For any regular split semistable one-parameter smoothing whose special-fiber dual graph is \(\Gamma_C\) and whose nodes all have unit thickness, the geometric component group of the Néron model of its Jacobian is the computed graph critical group by the graph-monodromy pairing theorem. This is conditional on that precise reduction graph and thickness; it makes no claim about a degeneration of the original genus-three quartic.

## Verification

The included `verify_steiner_graph.py` runs using Python 3 and the standard library alone:

```text
python3 verify_steiner_graph.py
```

The output includes `STEINER_GRAPH_CRITICAL_GROUP_VERIFIED_OK`. It checks the exact \(28\times63\) incidence matrix, all pairwise Gram entries, the Laplacian row sums, the determinant factorization, local Smith valuations at every possible torsion prime for two different reduced Laplacians, independent mod-prime ranks, invariant-factor divisibility, group order, and the graph's cycle rank. No random input, numerical approximation, external data file, or other script is used.

## Relationship to prior work

The \(28\) bitangents, \(63\) Steiner complexes, six-bitangent pairs per complex, and theta-theoretic incidence criterion are classical, not new; see the cited sources. Earlier published calculations give the **rectangular** integral Steiner-sum incidence cokernel and its exact exponent \(12\), whereas the present assertion concerns the **square graph Laplacian on 91 vertices**. The two maps have different domains, relations, and Smith groups; the prior rectangular result and the rational Gram spectrum do not directly provide the claimed integral graph Jacobian. Earlier work on the symplectic \(2\)-\((28,12,11)\) design computes construction and code parameters rather than this graph's complete critical group. Earlier graph-Jacobian computations on Cayley-octad-marked subconfigurations likewise concern different graphs.

## Limitations

Originality is asserted relative to the inspected mathematical statements, not as a certified exhaustive historical-priority claim. Older unindexed design literature and general Smith-form theorems may contain an equivalent computation. The result describes only the abstract integral graph Jacobian, not its Galois representation, the monodromy pairing as an explicit bilinear form, a canonical algebraic degeneration of the given quartic, or its Jacobian over the base field. Only regular unit-thickness split semistable smoothings with the specified dual graph have the stated Néron component group.

## References

1. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104 (first submitted 2010-08-24), especially §5. https://arxiv.org/abs/1008.4104
2. I. Dolgachev, *Topics in Classical Algebraic Geometry*, dated 2010-09-27, §§5.4.2, 6.1. https://mathweb.ucsd.edu/~eizadi/207A-14/Dolgachev-topics.pdf
3. D. Crnković, V. Mikulić Crnković, *On Some Combinatorial Structures Constructed from the Groups L(3,5), U(5,2), and S(6,2)*, International Journal of Combinatorics 2011, 137356, especially §5. https://doi.org/10.1155/2011/137356
4. O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, European Journal of Mathematics 9 (2023), 117, §3.4, preprint arXiv:2106.13072. https://link.springer.com/article/10.1007/s40879-023-00711-3
5. *Integral Steiner reconstruction lattice of plane-quartic bitangents*, accessible published calculation of the rectangular incidence Smith form. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-integral-steiner-reconstruction-lattice-of-plane-quartic-bitange--b76c5509eb43/RESULT.md
6. A. Blokhuis, A. R. Calderbank, *Quasi-symmetric designs and the Smith Normal Form*, Designs, Codes and Cryptography 2 (1992), 189–206; general constraints, not an identified formula for this Laplacian. https://doi.org/10.1007/BF00124897
