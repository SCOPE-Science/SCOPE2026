# Sharp negative type of the binary \(2\times2\times2\) tensor-rank metric

## Finding
Let \(V=(\mathbb F_2^2)^{\otimes3}\) and let \(d(X,Y)=\operatorname{trk}_{\mathbb F_2}(X-Y)\), where \(\operatorname{trk}\) denotes the minimum number of nonzero simple tensors summing to the given tensor (and the zero tensor has rank zero). Define \(\alpha_*\) as the unique positive solution of
\[
2^{\alpha_*}+3^{\alpha_*}=\frac52.
\]
Numerically, \(\alpha_*=0.2476710881978436\ldots\). For every real \(\alpha>0\), the distance-power kernel \(d(X,Y)^\alpha\) is conditionally negative semidefinite **if and only if** \(\alpha\le\alpha_*\). Strict conditional negative definiteness holds for \(0<\alpha<\alpha_*\). At the endpoint the zero-sum nullity is exactly \(54\).

Equivalently, the metric \(d^{\alpha/2}\) is isometrically Euclidean precisely in this parameter interval. The least real Euclidean embedding dimension is \(255\) for \(\alpha<\alpha_*\) and exactly \(201\) at \(\alpha=\alpha_*\).

## Assumptions and scope
All tensors are over the **binary** field and have exactly three factors of dimension two. We use the coordinate basis \(e_i\otimes e_j\otimes e_k\), with indices in \(\{0,1\}\). Encode a tensor as an eight-bit nonnegative integer, placing coordinate \((i,j,k)\) at bit position \(4i+2j+k\). Addition is bitwise XOR. No statement is made about other field orders or larger tensor formats. By \(\alpha\)-negative type we mean
\[
\sum_{X,Y\in V}c_Xc_Y\,d(X,Y)^\alpha\le0
\quad\text{whenever }c_X\in\mathbb R\text{ and }\sum_Xc_X=0.
\]

## Proof
**Step 1: exact complete rank shells.** There are precisely \(27=3^3\) nonzero simple tensors \(u\otimes v\otimes w\), since each vector factor has three nonzero options. Let \(R_r\) be the set of tensors of rank \(r\). The entire rank-two set is formed by pairwise XOR sums of simple tensors, excluding zero and rank one. Every remaining tensor is a sum of three simples; thus a self-contained exhaustive enumeration of all \(256\) eight-bit coordinate vectors gives
\[
(|R_0|,|R_1|,|R_2|,|R_3|)=(1,27,162,66).
\]
The Python certificate independently confirms rank-three attainability by testing every remaining eight-bit vector against all sums of rank-two and rank-one vectors. There are no higher-rank vectors. The same rank distribution is also documented in Bremner–Stavrou, Table 3; that older enumeration is background, not the new theorem.

**Step 2: complete Walsh spectral table.** For each frequency \(a\in V\), write \(\chi_a(x)=(-1)^{\langle a,x\rangle}\), using the coordinatewise binary dot product. For nonzero \(a\), set \(K_r(a)=\sum_{x\in R_r}\chi_a(x)\), with \(r=1,2,3\). The exact frequencies fall into these **exhaustive** classes:

| \((K_1,K_2,K_3)\) | Number of nonzero frequencies | Example bitmask |
|:--|--:|:--|
| \((-9,18,-10)\) | 12 | `0x6b` |
| \((-5,2,2)\) | 54 | `0x16` |
| \((-1,2,-2)\) | 108 | `0x18` |
| \((3,-14,10)\) | 54 | `0x06` |
| \((11,2,-14)\) | 27 | `0x01` |

The multiplicities add to \(255\). The table is a finite exhaustive exact-integer certificate, not extrapolation from a sample. The supplied standalone script constructs every simple tensor, computes the entire rank partition, checks the \(255\) direct character sums, and independently repeats all sums using a fast Walsh–Hadamard transform. Its loops and assertions are visible, so the table is reconstructible without relying on program output alone. Each row also has \(K_1+K_2+K_3=-1\), as required by nontrivial-character orthogonality.

**Step 3: analytic negative-type threshold.** Walsh characters diagonalize every translation-invariant real symmetric kernel on \(V\). On a nonconstant character, the eigenvalue of \(d^\alpha\) is
\[
F_a(\alpha)=K_1(a)+2^\alpha K_2(a)+3^\alpha K_3(a).
\]
Conditional negative semidefiniteness is equivalent to \(F_a(\alpha)\le0\) for all nonzero \(a\). Put \(u=2^\alpha\), \(v=3^\alpha\). The five spectral possibilities are
\[
-9+18u-10v,\quad -5+2u+2v,\quad -1+2u-2v,\quad 3-14u+10v,\quad11+2u-14v.
\]
The second is strictly increasing in \(\alpha\), equals \(-1\) at zero and \(5\) at one, and therefore has a unique root \(\alpha_*\in(0,1)\) given by \(u+v=5/2\). The third is strictly negative since \(v>u\), and the fifth is strictly negative since \(11+2u-14v\le11-12v<0\).

For every \(\alpha>0\), the first is strictly smaller than the second, because their difference is \(-4(1-4u+3v)\) and \(1-4\,2^\alpha+3\,3^\alpha>0\): the latter starts at zero and its derivative is \(3\log(3)3^\alpha-4\log(2)2^\alpha>0\) (using \(3\log3>4\log2\)). For \(0<\alpha<1\), the fourth is strictly smaller than the second, because their difference is \(8(1-2u+v)<0\) by strict concavity of \(x\mapsto x^\alpha\) at the equally spaced points \(1,2,3\). Thus every nonconstant eigenvalue is strictly negative below \(\alpha_*\), and at \(\alpha_*\) the only zero eigenvalues are the \(54\) members of the second row. Above \(\alpha_*\), the second-row eigenvalue is positive, excluding negative type.

**Step 4: minimal Euclidean dimension.** Define the centered squared-distance Gram matrix \(G=-\frac12 JD_\alpha J\), where \(D_\alpha=(d(X,Y)^\alpha)_{X,Y\in V}\) and \(J=I-256^{-1}\mathbf1\mathbf1^\mathsf T\). It is positive semidefinite exactly on the negative-type interval, and its rank equals the number of strictly negative nonconstant Walsh eigenvalues. Its standard Euclidean realization gives \(d(X,Y)^\alpha=\|\Phi(X)-\Phi(Y)\|_2^2\). Every Euclidean realization has affine dimension at least \(\operatorname{rank}G\); hence the exact minimum dimensions are \(255\) and \(255-54=201\).

## Verification
Run `python3 tensor_rank_negative_type_check.py` with Python 3 (standard library only). The source enumerates all \(256\) possible binary tensors, all \(27\) rank-one simple tensors, all rank-two XOR sums, and all \(255\) nontrivial frequencies. It checks a direct Walsh-sum table against an independently coded fast Walsh–Hadamard transform and prints the exact five rows and their multiplicities. The final successful marker is `ALL_2X2X2_TENSOR_NEGATIVE_TYPE_CERTIFICATES_OK`. The transcendental scalar root is obtained from elementary strict monotonicity, not a floating-point certificate.

## Relationship to prior work
Bremner–Stavrou (2011), Section 3 and Table 3, and Bremner–Hu (2012), Section 3 and Table 2, established tensor-rank orbits and their sizes over the binary field. These published orbit counts match the rank shells used here, but the present claim concerns a different invariant: the full nonconstant Walsh spectra of all three rank shells, the sharp powered-distance negative-type threshold and the minimum Euclidean embedding dimensions. Byrne–François (2026), Theorem 42 and Section 4, study the eigenvalues of the **rank-one adjacency** Cayley graph for tensor codes, a substantial spectral antecedent; their result does not itself give the full rank-two and rank-three Fourier-shell table or the powered-metric phase transition. The present exact certificate verifies the additional ingredients directly.

## Limitations
This theorem is only for the \(256\)-point binary \(2\times2\times2\) tensor space. The computational certificate is exhaustive **for that finite domain only**; the analytic sign argument covers every real positive exponent for that domain. The source comparisons are bounded, and an unlocated prior result on negative type of tensor-rank metrics or an implicit specialization of a broader tensor scheme could subsume the finding. No independent validation has been performed.

## References
1. M. R. Bremner and S. G. Stavrou, *Ranks of 0-1 arrays of size 2 x 2 x 2 and 2 x 2 x 2 x 2* (first public version 2011-12-01), arXiv:1112.0298, https://arxiv.org/abs/1112.0298 .
2. M. R. Bremner and J. Hu, *Canonical forms of small tensors over F2* (first public version 2012-06-22), arXiv:1206.5179, https://arxiv.org/abs/1206.5179 .
3. E. Byrne and L. François, *The multilinear forms Cayley graph and the eigenvalue method for tensor codes* (first public version 2026-07-03), arXiv:2607.03479, https://arxiv.org/abs/2607.03479 .
4. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536, for the classical negative-type/Euclidean embedding equivalence.
