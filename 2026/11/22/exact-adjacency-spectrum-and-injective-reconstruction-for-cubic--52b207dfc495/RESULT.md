# Exact adjacency spectrum and injective reconstruction for cubic-contact bitangent hexads

## Finding
Let \(C\subset\mathbb P^2_{\mathbb C}\) be a sufficiently general smooth plane quartic. A *cubic-contact hexad* is an unordered set of six ordinary bitangents whose twelve distinct points of contact lie on a plane cubic. Class I consists of the \(1008\) hexads with no syzygetic triad; class II consists of the \(5040\) hexads with eight syzygetic triads. These two families, their sizes, and their cross-class four-overlap graph are previous results.

Let \(B\) be the \(1008\times5040\) matrix with entry one when a class-I and a class-II hexad share exactly four bitangents and zero otherwise. Its integer Gram matrix \(G=BB^{\mathsf T}\) has characteristic polynomial

\[
\boxed{\begin{aligned}
\chi_G(z)={}&(z-21)^{105}(z-24)^{280}(z-45)^{168}(z-48)^{330}(z-405)\\
&\cdot(z^2-141z+3888)^{35}(z^2-285z+19440)^{27}.
\end{aligned}}
\]

Every eigenvalue is positive. Consequently the incidence map \(B^{\mathsf T}:\mathbb Q^{1008}\to\mathbb Q^{5040}\) is injective: a weight on each class-I hexad is uniquely determined by the \(5040\) sums over its class-II neighbors. In particular the \(1008\) class-I four-overlap neighborhood vectors are linearly independent. The sharp smallest singular value of \(B\) is \(\sqrt{21}\); the largest is \(\sqrt{405}\).

The two-step Markov walk from a class-I hexad to one of its \(45\) class-II neighbors and then uniformly to one of that neighbor's \(9\) class-I neighbors has matrix \(G/405\). Its exact spectral gap is
\[
\boxed{\gamma=1-\frac{285+\sqrt{3465}}{810}\approx0.5754762338.}
\]
The eigenvalue \(405\) is simple. This gives quantitative mixing and reconstruction beyond the previously known connectedness and biregularity.

## Assumptions and scope
The curve is a sufficiently general complex plane quartic, so its bitangents have two distinct tangent points each and no three bitangents concur. The word *syzygetic* for a triad means its six contact points lie on a conic. The result concerns a finite combinatorial incidence operator associated with a fixed quartic, not the spectrum of an algebraic variety, a deformation between arrangement components, or an arithmetic reduction.

## Proof
**Theta coordinates.** Choose an even theta characteristic \(\theta_0\) on \(C\). The space of two-torsion characters is a six-dimensional symplectic binary vector space \(V\), and a symplectic choice of basis gives the parity quadratic form
\[
q(a_1,a_2,a_3,b_1,b_2,b_3)=a_1b_1+a_2b_2+a_3b_3\pmod2.
\]
The \(28\) odd theta characteristics, hence the bitangents, are the vectors \(v\in V\) with \(q(v)=1\). A contact divisor \(D_v\) satisfies \(2D_v\sim K_C\). Since plane cubics restrict to the complete linear system \(|3K_C|\), a six-set of bitangents is a cubic-contact hexad precisely when the sum of its six binary vectors is zero. For a triple \(\{u,v,w\}\), the corresponding syzygetic status is detected by \(q(u+v+w)=1\), so class I has zero such triples and class II has eight, by the classical classification. These equivalences are standard consequences of the theta-characteristic correspondence, also explicitly used in the references.

**Finite model and symmetry.** Enumerate all \(\binom{28}{5}=98280\) five-sets of odd vectors. Their forced sixth vector is the XOR of the five. Discard it unless it is a distinct odd vector. Each admissible six-set is produced six times. The resulting exact set comprises \(6048\) hexads, with \(1008\) having \(20\) triples of \(q\)-sum zero and \(5040\) having \(12\). Each nonzero vector \(w\in V\) defines a symplectic transvection acting on the odd characteristics by
\[
T_w(v)=v+[q(w)+1+\langle v,w\rangle]w,
\]
where brackets are evaluated in \(\mathbb F_2\). The formula preserves the odd-theta condition, hexad condition, and triad parity. A complete breadth-first enumeration under the \(63\) nonzero transvections finds orbits of exactly \(1008\) and \(5040\) hexads. Therefore the action is transitive on each class and preserves the matrix \(B\) under separate row and column permutations.

**Exact Gram certificate.** Enumerate all tetrads of each hexad and insert an edge between opposite-class hexads exactly when they have a common tetrad. An intersection of size five is impossible for two distinct zero-sum hexads, because their two remaining vectors would be equal. The complete adjacency has \(45360\) edges, row degree \(45\) and column degree \(9\). Build \(G=BB^{\mathsf T}\) as an exact integer matrix using its sparse column-neighborhood lists.

Set
\[
\begin{aligned}
P(z)={}&(z-21)(z-24)(z-45)(z-48)(z-405)\\
&\cdot(z^2-141z+3888)(z^2-285z+19440).
\end{aligned}
\]
The standalone checker constructs the standard first basis column \(e_0\) and evaluates all nine successive vectors \(G^ke_0\), for \(0\le k\le9\), in exact integer arithmetic. It verifies every coordinate of \(P(G)e_0\) is zero. Because the transvection group is transitive on the \(1008\) class-I hexads and commutes with \(G\), it follows that \(P(G)e_i=0\) for every basis column; hence \(P(G)=0\) exactly, not merely modulo a prime or up to numerical tolerance.

For \(0\le k\le6\), transitivity also gives \(\operatorname{tr}(G^k)=1008(G^ke_0)_0\). The exact traces are
\[
1008,\ 45360,\ 3039120,\ 339882480,\ 61534967760,\ 15985643511600,\ 5215177324964880.
\]
All seven displayed factors of \(P\) are distinct and separable over \(\mathbb Q\). The multiplicities of the five linear roots and of the two quadratic-conjugate root pairs are rational unknowns. The seven traces give a nonsingular \(7\times7\) rational linear system, solved exactly by the checker, with ordered multiplicities
\[
(105,280,168,330,1,35,27).
\]
This proves the claimed characteristic polynomial, with degrees summing to \(1008\). Both quadratic factors have positive real roots: the smaller and larger eigenvalues of the first factor are \((141\mp\sqrt{4329})/2\), and those of the second are \((285\mp\sqrt{3465})/2\). In particular the least eigenvalue is \(21\), the largest is \(405\), and the second largest is \((285+\sqrt{3465})/2\). The rank and gap assertions now follow from positive definiteness and the biregular degrees.

## Verification
Run `python3 artifacts/verify_spectrum.py` with Python 3. No third-party library, randomness, online data, or floating point arithmetic is used. It exhaustively constructs the finite theta-space model, proves the two full symmetry orbits by transvection traversal, independently builds the bipartite adjacency from all shared tetrads, verifies every degree and all \(45360\) edges, checks the integer polynomial on every coordinate of one Gram column, and solves the exact rational trace system. Its success marker is `CHECK_OK` and its output prints the polynomial coefficients, trace values and characteristic multiplicities. The proof of matrix-wide annihilation uses proven class-I transitivity; the code does not assert a matrix identity from a single unproved sample.

## Relationship to prior work
Bannai and Tokunaga (2026) analyze the two classical families of cubic-contact hexads and their topologically distinct arrangement types; the numbers \(1008\) and \(5040\), as well as their syzygetic-triad patterns, are not claimed new. Shimada (2022, Table 9.1) enumerates the individual six-bitangent orbits and their internal two-graph invariants. Edge (1960) describes the bitangent group through finite orthogonal geometry and tabulates incidence of its subspaces.

A 2026 published exact-incidence study, *Cubic-contact bitangent hexads: tetrad extensions and a connected exchange graph*, gives the full tetrad extension counts, all four pairwise hexad intersection rows, and the connected \((45,9)\)-biregular graph of \(45360\) edges. The present result does **not** reclaim any of those facts. Its new assertion is the exact characteristic polynomial of the \(1008\)-dimensional Gram operator, with the resulting positive-definite reconstruction theorem and quantitative spectral gap. These do not follow from connectedness or biregular degrees alone. Specialist priority checking for an older representation-theoretic equivalent remains appropriate.

## Limitations
The conclusion is a finite exact invariant for the given classical theta incidence model, not a general spectral theorem for all tetrad-incidence designs, a proof of geometric deformation connectedness, or an independently audited classification. The classical theta/bitangent correspondence is cited rather than reproved. Any unindexed prior representation-theoretic spectrum for this same group action could cover the result; the literature and mathematical-record checks performed did not reveal one.

## References
1. S. Bannai and H. Tokunaga, *A curve of genus 2 over C(t) and hexads of bitangents to a smooth quartic*, arXiv:2610.38071v1, first public 2026-10-27, Introduction and Lemma 4.1. https://arxiv.org/abs/2610.38071
2. I. Shimada, *Zariski multiples associated with quartic curves*, Journal of Singularities **24** (2022), 169–189, Sections 8–9 and Table 9.1, DOI 10.5427/jsing.2022.24g. https://www.journalofsingularities.com/volume24/shimada.pdf
3. W. L. Edge, *A setting for the group of the bitangents*, Proc. London Math. Soc. (3) **10** (1960), 583–598, Table 1. https://webhomes.maths.ed.ac.uk/~icheltso/edge2016/pdf/1960a.pdf
4. *Cubic-contact bitangent hexads: tetrad extensions and a connected exchange graph*, publicly accessible mathematical finding, 2026-11-08, especially Finding and Proof. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-cubic-contact-bitangent-hexads-tetrad-extensions-and-a-connected--2363b4154825
