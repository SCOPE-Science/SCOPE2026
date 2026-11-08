# Sharp parity-dependent automorphism maxima for simple evolution algebras over \(\mathbb F_2\)

## Finding
For every integer \(n\ge 1\), let \(M_n\) denote the maximum of \(|\operatorname{Aut}(E)|\), over all simple \(n\)-dimensional evolution algebras \(E\) defined over \(\mathbb F_2\), with ordinary \(\mathbb F_2\)-linear algebra automorphisms. Then
\[
M_n=\begin{cases}
1,&n=1,\\
n!,&n\ge2\text{ even},\\
3,&n=3,\\
(n-1)!,&n\ge5\text{ odd}.
\end{cases}
\]
Every bound is attained by an explicit algebra. Thus the full symmetric group is attainable as the automorphism group of a simple binary evolution algebra precisely in even dimension (and trivially for dimension one); in odd dimension at least five, the exact maximum is the point-stabilizer size, with a three-dimensional cyclic exception.

## Assumptions and scope
An evolution algebra over \(K\) is a finite-dimensional commutative, generally nonassociative algebra with natural basis \(e_1,\ldots,e_n\) satisfying \(e_ie_j=0\) for \(i\ne j\). Write \(e_i^2=\sum_j a_{ij}e_j\). Its structure matrix is \(A=(a_{ij})\), and its directed graph has arc \(i\to j\) exactly when \(a_{ij}\ne0\), including loops. Simple means \(E^2\ne0\) and no nonzero proper ideals. All dimensions in the claim are positive; the base field is exactly \(\mathbb F_2\), not an algebraic closure, and automorphisms are ordinary rational points, not group-scheme points.

For this field, every structure matrix is binary. Simplicity is equivalent to \(A\) being nonsingular and its directed graph strongly connected. For clarity, if \(E\) is simple then \(E^2=E\), since \(E^2\) is a nonzero ideal, so the squares \(e_i^2\) form a basis. If the graph were not strongly connected, any sink strongly connected component would span a proper nonzero ideal. Conversely, if \(A\) is nonsingular and the graph strongly connected, any nonzero ideal contains some square \(e_i^2\) (multiply a nonzero ideal element by an appropriate \(e_i\)); multiplying squares by basis vectors propagates along all directed paths, so the ideal contains every square, hence all of \(E\).

## Proof
**1. Exact automorphism reduction.** Suppose \(A\) is nonsingular. If \(\varphi\) is an automorphism with \(\varphi(e_i)=\sum_k p_{ki}e_k\), then for distinct \(i,j\),
\[
0=\varphi(e_i)\varphi(e_j)=\sum_k p_{ki}p_{kj}e_k^2.
\]
Because the squares are linearly independent, \(p_{ki}p_{kj}=0\) for all \(k\) and distinct \(i,j\). Invertibility of \((p_{ki})\) forces exactly one nonzero entry in each row and column. Since \(\mathbb F_2^{\times}=\{1\}\), \(\varphi\) is a permutation of the natural basis. Preservation of each square is then exactly preservation of the directed adjacency matrix. Consequently
\[
\operatorname{Aut}_{\mathbb F_2}(E)\cong\operatorname{Aut}(\Gamma_A)\le S_n.
\]
The immediate universal bound is \(M_n\le n!\).

**2. Even dimensions attain \(n!\).** For even \(n\ge2\), take the zero-diagonal, all-one off-diagonal structure matrix \(A=I_n+J_n\), where \(J_n\) is the all-ones matrix, with arithmetic in characteristic two. As \(J_n^2=nJ_n=0\), \(A^2=I_n\); hence \(A\) is invertible. Its digraph has every arc between distinct vertices, so is strongly connected, and its full graph automorphism group is \(S_n\). Therefore \(M_n=n!\).

**3. Odd dimensions cannot attain \(n!\).** Assume \(n\ge3\) is odd, and suppose \(S_n\) preserves a binary adjacency matrix \(A\) of a simple algebra. Transitivity on vertices and ordered distinct pairs forces \(A\) to have constant diagonal \(a\in\mathbb F_2\) and constant off-diagonal \(b\in\mathbb F_2\). Strong connectivity forces \(b=1\). If \(a=1\), then \(A=J_n\), of rank one. If \(a=0\), then \(A=I_n+J_n\), which kills the all-ones vector because \(n\) is odd. Both contradict invertibility.

**4. Strict small-index bound for odd \(n\ge5\).** Let \(H\le S_n\) be an automorphism group of a simple algebra. By step 3, \(H\ne S_n\). Suppose \(|H|>(n-1)!\), and put \(m=[S_n:H]<n\). The action of \(S_n\) on the \(m\) left cosets of \(H\) gives a homomorphism \(S_n\to S_m\). It cannot be injective because \(n!>m!\). Its kernel is a nontrivial proper normal subgroup of \(S_n\) contained in \(H\). For \(n\ge5\), the only nontrivial proper normal subgroup of \(S_n\) is \(A_n\), so \(A_n\subseteq H\). As \(A_n\) is two-transitive for \(n\ge5\), its invariance forces the same constant-diagonal/constant-off-diagonal matrix, contradicting step 3. Hence \(|H|\le(n-1)!\).

**5. Odd-dimensional attainment.** For every odd \(n\ge5\), index the basis by \(0,1,\ldots,n-1\) and let
\[
e_0^2=e_0+\sum_{j=1}^{n-1}e_j,\qquad e_i^2=e_0+e_i\quad(1\le i<n).
\]
The matrix is
\[
B_n=\begin{pmatrix}1&\mathbf1^{\mathsf T}\\\mathbf1&I_{n-1}\end{pmatrix}.
\]
Its determinant equals \(1-(n-1)=1\) in \(\mathbb F_2\) for odd \(n\); its digraph is strongly connected because every leaf connects to the hub and conversely. The hub is the unique vertex of outdegree \(n\), while all leaves have outdegree two. Thus its graph automorphism group is precisely the permutations of the leaves, isomorphic to \(S_{n-1}\). Steps 1 and 4 give \(M_n=(n-1)!\).

**6. Low-dimensional cases.** For \(n=3\), step 3 excludes \(S_3\). The order of any proper subgroup of \(S_3\) is at most three; the simple directed three-cycle algebra \(e_1^2=e_2,\ e_2^2=e_3,\ e_3^2=e_1\) has automorphism group \(C_3\), showing \(M_3=3\). For \(n=1\), simplicity forces \(e_1^2=e_1\) and the unique algebra automorphism is the identity. This exhausts all cases.

## Verification
The accompanying `verify.py` performs exact exhaustive enumeration of all binary structure matrices for \(1\le n\le4\); it tests nonsingularity by binary elimination, strong connectivity by reachability, and automorphisms by checking all permutations. The resulting maxima are \(1,2,3,24\), respectively, with numbers of simple matrices \(1,3,80,11658\). It separately checks explicit even witnesses for \(n=2,4,6,8\), odd hub witnesses for \(n=3,5,7\), the exceptional three-cycle, and the absence of connected nonsingular symmetric-invariant matrices in odd dimensions \(3,5,7,9\). The accompanying `verification_output.txt` records the exact output. These are finite checks supporting, not replacing, the arbitrary-dimensional proof, which uses the normal-subgroup theorem for \(S_n\) as its only non-elementary group-theoretic input.

## Relationship to prior work
The motivating 2026 survey by Kaygorodov, Martín González and Viruel states a maximal-automorphism conjecture **over the complex field**, not a theorem over \(\mathbb F_2\). The field change is essential: nontrivial diagonal scalars available over larger fields disappear over the two-element field. Sriwongsa and Zou (2022), in particular Theorem 3.2, classify perfect evolution algebras with full \(S_n\) automorphism group and thereby contain the full-symmetric attainment/obstruction subproblem. Costoya, Mayorga and Viruel (2025), in Theorem A, establish strong restrictions on highly transitive permutation representations. Their results are used as context rather than claimed as new. Neither inspected work gives the sharp binary maximum in **every** dimension, including the odd-dimensional point-stabilizer attainment and the three-dimensional exception. The proof here combines the known graph perspective with a small-index argument and a binary hub construction. Earlier implicit equivalence in graph-automorphism or evolution-algebra literature remains possible.

## Limitations
The theorem concerns simple algebras and ordinary automorphism groups over the base field \(\mathbb F_2\), not perfect-but-nonsimple algebras, extensions to \(\mathbb F_{2^k}\), or geometric automorphism-group schemes. The maximum over isomorphism classes is the same as the maximum over labeled structure matrices, but no classification of all maximizing algebras is asserted. The finite enumeration is not an independent proof of the all-dimensional bound; a separate independent scholarly review has not been conducted.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15), Section 2.3, Conjecture 4, and Section 1.
2. S. Sriwongsa, Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333 (2022), Theorems 2.1 and 3.2.
3. C. Costoya, P. Mayorga, A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, *Mediterranean Journal of Mathematics* (2025), DOI:10.1007/s00009-025-02924-0, Theorem A.
4. Standard finite-group fact: for \(n\ge5\), the only nontrivial proper normal subgroup of \(S_n\) is \(A_n\), and \(A_n\) is two-transitive.
