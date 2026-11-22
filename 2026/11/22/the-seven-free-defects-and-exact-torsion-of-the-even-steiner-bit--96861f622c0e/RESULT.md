# The seven free defects and exact torsion of the even-Steiner bitangent lattice

## Finding

Let \(C\) be a smooth geometrically connected nonhyperelliptic genus-three curve over a field \(k\) of characteristic different from \(2\), and let \(\eta\) be a *chosen even theta characteristic* on \(C_{\overline k}\). Its \(28\) geometric bitangents are the odd theta characteristics \(\Theta^-\). For each nonzero \(v\in J(C_{\overline k})[2]\) with the even quadratic refinement \(q_\eta(v)=0\), let \(\Sigma(v)\) be the classical twelve-bitangent Steiner complex. There are precisely \(35\) such complexes. Define the geometric integral incidence map

\[
I_\eta:\mathbb Z^{35}\longrightarrow\mathbb Z^{\Theta^-},\qquad
[\Sigma(v)]\longmapsto\sum_{b\in\Sigma(v)}[b].
\]

**Theorem.** The Smith invariant factors of \(I_\eta\), including zero factors in its \(28\)-dimensional target, are

\[
\boxed{\operatorname{SNF}(I_\eta)=\operatorname{diag}(1^{\times7},2^{\times13},6,0^{\times7}).}
\]

Equivalently,

\[
\boxed{\operatorname{coker}(I_\eta)\cong\mathbb Z^7\oplus(\mathbb Z/2\mathbb Z)^{13}\oplus\mathbb Z/6\mathbb Z.}
\]

Thus \(I_\eta\) has rational rank \(21\), and its image has index \(49152\) in its saturation. This saturation has a natural description: identify bitangents with the edges of the complete graph on the eight labels of the Cayley octad determined by \(\eta\). Then the saturation consists **exactly** of the integral edge-weight vectors whose eight weighted vertex degrees are all equal. The finite obstruction in that equal-degree lattice has exponent \(6\): multiplying **every** equal-degree integral vector by \(6\) makes it a sum of the selected Steiner incidences, and no smaller positive universal multiplier works. Its only odd-primary part is one cyclic group of order \(3\).

This is a statement about the *formal integer lattice on geometric bitangents*. It makes no assertion about the Picard or Chow lattice of the quartic, the base field of each bitangent, or the descent of the abstract quotient as a Galois module.

## Assumptions and scope

An even theta characteristic is a line bundle \(\eta\) with \(\eta^{\otimes2}\simeq K_C\) and even \(h^0(C,\eta)\). If \(\eta\) is defined over \(k\), all constructions are Galois-stable; otherwise the claim holds for the chosen geometric marking. On the six-dimensional binary symplectic space \(J[2]\), the quadratic form \(q_\eta(v)=h^0(\eta\otimes v)-h^0(\eta)\pmod2\) is an even quadratic refinement.

For a Cayley octad \(\Omega\) of eight geometric points, use the standard model

\[
J[2]\cong\{S\subseteq\Omega:|S|\text{ even}\}/(S\sim\Omega\setminus S),
\qquad q_\eta([S])=|S|/2\pmod2.
\]

The \(28\) nonzero classes with \(q_\eta=1\) are the unordered two-element subsets \(e\subset\Omega\), labelling bitangents. The \(35\) nonzero classes with \(q_\eta=0\) are unordered bipartitions \(\{S,S^c\}\), \(|S|=4\), labelling the selected Steiner complexes. This is the classical Cayley-octad marking of the \(28+35\) Steiner families; the definitions and geometric identifications are not new.

## Proof

**1. Exact incidence model.** Fix the ordered ground set \(\Omega=\{0,1,\ldots,7\}\) only to write a matrix. Represent each four-four partition by the half \(S\) containing \(0\), and enumerate the \(28\) pairs \(e\). Bergvall's classical criterion for membership is \(b_e\in\Sigma(v)\) if and only if the odd theta quadratic refinement attached to \(b_e\) vanishes on \(v\). Here

\[
q_{\eta+e}([S])=q_\eta([S])+|e\cap S|\pmod2=|e\cap S|\pmod2.
\]

Consequently the \(35\times28\) matrix with row \(S\) and column \(e\) is

\[
M_{S,e}=\begin{cases}
1,&|e\cap S|\in\{0,2\},\\
0,&|e\cap S|=1.
\end{cases}
\]

A row is the sum of the \(12\) edges lying within the two blocks of its partition. Every edge lies in precisely \(\binom62=15\) such rows. Replacing the octad ordering permutes rows and columns, so it does not change the integral invariant factors. The matrix of \(I_\eta\) is \(M^{\mathsf T}\).

**2. Rational rank and the saturated lattice.** Let \(A\) be the adjacency matrix of the triangular graph on the \(28\) unordered pairs of eight vertices (two distinct pairs are adjacent when they share one vertex), and \(J\) the all-ones matrix of size \(28\). The number of four-four partitions in whose two blocks two specified pairs both lie is \(15\) for identical pairs, \(5\) for intersecting pairs, and \(7\) for disjoint pairs. Hence

\[
M^{\mathsf T}M=8I_{28}-2A+7J.
\]

Let \(D\) be the ordinary unsigned vertex-edge incidence matrix of the complete graph on eight vertices. Then \(A=D^{\mathsf T}D-2I_{28}\) and \(DD^{\mathsf T}=6I_8+J_8\). It follows that \(A\) has eigenvalues \(12\) once, \(4\) seven times and \(-2\) twenty times. Therefore \(M^{\mathsf T}M\) has eigenvalues \(180\), \(0^{\times7}\), and \(12^{\times20}\), proving \(\operatorname{rank}_\mathbb Q M=21\).

For each vector \(a=(a_0,\ldots,a_7)\in\mathbb Q^8\) with \(\sum_i a_i=0\), put \(w_{ij}=a_i+a_j\). Every row of \(M\) has each vertex in exactly three selected edges, so

\[
\sum_{i<j}M_{S,\{i,j\}}w_{ij}=3\sum_i a_i=0.
\]

These \(w\) give a seven-dimensional kernel, and the rank calculation shows they exhaust the rational kernel. An integral edge-weight vector \(x=(x_{ij})\) is orthogonal to every such \(w\) if and only if the weighted vertex degrees \(d_i=\sum_{j\ne i}x_{ij}\) are all equal. This defines a saturated sublattice of rank \(21\): it is the kernel of the homomorphism sending \(x\) to \((d_0-d_7,\ldots,d_6-d_7)\in\mathbb Z^7\). Since it contains \(\operatorname{im}(I_\eta)\) and has the same rational span, it is exactly that image's saturation. Each Steiner-support row has common weighted vertex degree \(3\), so its integral span has common degree divisible by \(3\). By contrast, any perfect matching of the eight octad labels has common degree \(1\), giving an explicit nontrivial homomorphism from the saturation quotient onto \(\mathbb Z/3\mathbb Z\). This gives a geometric explanation of the odd-primary obstruction proved exactly in Step 3.

**3. Integral invariant factors.** The reproducible certificate `certificate.json` records \(474\) elementary integer row and column operations, each a swap, integer multiple added to another row/column, or row negation, on the explicit \(35\times28\) matrix \(M\). The standalone `verify.py` reconstructs all entries from the quadratic-refinement criterion and replays the entire operation list. It checks exact equality with the diagonal matrix

\[
\operatorname{diag}(\underbrace{1,\ldots,1}_{7},
\underbrace{2,\ldots,2}_{13},6,
\underbrace{0,\ldots,0}_{7})
\]

(with seven extra zero rows). Every recorded operation is invertible over \(\mathbb Z\); the nonzero diagonal entries satisfy the divisibility condition \(1\mid2\mid6\). Therefore this diagonal is a certified Smith normal form, not a numerical approximation. The cokernel and the index \(2^{13}\cdot6=49152\) follow by the structure theorem for finitely generated abelian groups. The quotient exponent is exactly \(6\), proving the sharp uniform integral reconstruction multiplier stated in the theorem. An independent exact Smith calculation with SymPy returned the same factors.

## Verification

Unpack the two accompanying files `verify.py` and `certificate.json` beside this document and run:

```text
python3 verify.py certificate.json
```

The verifier uses only Python's standard library. It independently enumerates \(35\) partitions and \(28\) edges, reconstructs the entire incidence matrix, checks the \(12\)-per-row and \(15\)-per-column identities, the full Gram matrix entry by entry, the seven rational kernel witnesses, equivariance under the seven adjacent-transposition generators of \(S_8\), and replays all \(474\) certified unimodular operations. It additionally computes modular ranks \(7,20,21\) in characteristics \(2,3,5\), agreeing with the integral invariant factors. The expected final line begins `VERIFIED: 35 even Steiner complexes, 28 bitangents`.

The certificate proves the indicated finite matrix equality. The all-characteristic geometric assertion follows from the classical theta/Steiner identifications in Step 1; no finite-field experiment is being extrapolated to infinitely many fields.

## Relationship to prior work

Plaumann, Sturmfels and Vinzant explicitly classify the \(63\) Steiner complexes into \(28\) pair-type and \(35\) four-four partition-type families and specify their bitangent memberships. Bergvall identifies the associated even-theta Cayley-octad marking and the quadratic-refinement criterion. These constructions are premises of the theorem, not new claims.

An earlier integral reconstruction theorem for **all \(63\)** Steiner complexes gives a full-rank map onto a finite-index sublattice of the \(28\)-bitangent lattice, with cokernel \((\mathbb Z/2)^{14}\oplus(\mathbb Z/4)^6\oplus\mathbb Z/12\). Its full-matrix Smith form does **not determine** the Smith form of the naturally selected \(35\)-row submatrix. Here that submatrix has rational rank only \(21\), has precisely the equal-degree saturation, and has distinct torsion \((\mathbb Z/2)^{13}\oplus\mathbb Z/6\). These latter assertions are the new proposed contribution.

The rational \(S_8\)-permutation characters on \(28\) and \(35\) objects are classical, but a character calculation over characteristic zero does not determine the integral Smith factors or the \(3\)-primary torsion. A possible equivalent computation hidden in older incidence-design or integral-representation literature remains a historical-priority risk.

## Limitations

This is an abstract geometric incidence-lattice theorem for a **chosen** even theta characteristic. The quotient is not identified with a divisor-class group or the Néron–Severi group; its full Galois module structure, its relationship with individual finite-field Frobenius operators, and any analogous genus-generalization are not determined. The certificate is an exact finite check, but historical uniqueness against all obscure integral design tables is not certified. An independent mathematical audit has not been performed.

## References

1. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104 (first public 2010-08-24), especially Sections 5 and 6, on the \(28+35\) Steiner families and their incidence with bitangents. https://arxiv.org/abs/1008.4104
2. O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, arXiv:2106.13072 (first public 2021-06-24), especially Sections 2.2, 2.3, and 2.5 on theta characteristics, Cayley octads, and Steiner complexes. https://arxiv.org/abs/2106.13072
3. *Integral Steiner reconstruction lattice of plane-quartic bitangents*, publicly available integral full-\(63\)-complex incidence theorem (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-steiner-reconstruction-lattice-of-plane-quartic-bitange--b76c5509eb43
4. D. Crnković, V. Mikulić Crnković, A. Švob, *On some transitive combinatorial structures and codes constructed from the symplectic group S(6,2)*, Journal of Combinatorial Mathematics and Combinatorial Computing 97 (2016), 119–138; potential code-theoretic background, not taken as evidence of a complete integral calculation. https://combinatorialpress.com/article/jcmcc/Volume%20097/vol-097-paper%209.pdf
