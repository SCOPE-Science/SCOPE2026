# Uniform Kronecker permutation lifts are direct sums of the base LDPC code
## Finding

Let \(A\) be the binary \(n\times n\) parity-check matrix used in Mostarac and Šimac's Theorem 3.1, and write
\[
C=\ker_{\mathbb F_2}A.
\]
For any positive integer \(m\) and any \(m\times m\) permutation matrix \(P\), define
\[
H_m=A\otimes P,
\qquad
C_m=\ker_{\mathbb F_2}H_m.
\]

Then \(C_m\) is coordinate-permutation equivalent to the direct sum of \(m\) copies of \(C\):
\[
C_m\cong C^{\oplus m}.
\]

Equivalently, the Tanner graph of \(H_m\) is isomorphic to the disjoint union of \(m\) copies of the Tanner graph of \(A\). Therefore the uniform construction has the following exact consequences:
\[
W_{C_m}(z)=W_C(z)^m,
\]
the minimum distance remains \(d(C_m)=d(C)\), the dimension is \(m\dim C\), and for every fixed even length \(2\ell\), the number of simple Tanner cycles of length \(2\ell\) is exactly \(m\) times the corresponding number for \(A\).

In particular, when \(m>1\), the uniform Kronecker lift in Theorem 3.1 is disconnected as a Tanner graph. The larger codes obtained in this way are repetitions of the same constituent code up to a coordinate relabeling rather than genuinely connected graph lifts.

## Assumptions and scope

The statement concerns the uniform construction
\[
A_m=A\otimes P
\]
from Theorem 3.1 of the source, where the same permutation matrix \(P\) appears in every nonzero block.

No extra assumption on the order of \(P\) is needed for the decomposition itself; only the fact that \(P\) is a permutation matrix is used.

The conclusion is about the binary linear code and its Tanner graph. It does not assert that the directed graph whose adjacency matrix is \(A\otimes P\) is itself a disjoint union under a single simultaneous vertex relabeling.

The source's Remark 3.4 allows different permutation matrices in different nonzero block positions. That more general construction is excluded here and can genuinely couple the copies.

## Proof

Because \(P\) is a permutation matrix,
\[
PP^T=I_m.
\]
Hence
\[
(A\otimes P)(I_n\otimes P^T)
=
A\otimes(PP^T)
=
A\otimes I_m.
\]
Right multiplication by \(I_n\otimes P^T\) merely permutes code coordinates, so
\[
\ker(A\otimes P)
\]
is coordinate-permutation equivalent to
\[
\ker(A\otimes I_m).
\]

Now index rows and columns of \(A\otimes I_m\) by pairs
\[
(i,a),
\qquad
1\le i\le n,\quad 1\le a\le m.
\]
Apply the perfect shuffle
\[
(i,a)\longmapsto(a,i)
\]
to both rows and columns. Under this simultaneous permutation,
\[
A\otimes I_m
\]
becomes
\[
I_m\otimes A.
\]
The latter is block diagonal with \(m\) identical diagonal blocks \(A\). Row permutations do not change the code, while column permutations give code equivalence. Therefore
\[
C_m\cong
\ker(I_m\otimes A)
=
C^{\oplus m}.
\]

The Tanner graph of a block-diagonal parity-check matrix is the disjoint union of the Tanner graphs of its diagonal blocks. Since row and column permutations only relabel check and variable vertices, the Tanner graph of \(A\otimes P\) is therefore isomorphic to \(m\) disjoint copies of the Tanner graph of \(A\).

For direct sums, Hamming weights add across blocks. Hence the ordinary weight enumerator multiplies:
\[
W_{C_m}(z)=W_C(z)^m.
\]
The smallest nonzero word can be placed in one constituent block, while every nonzero direct-sum word has at least one nonzero constituent. Thus
\[
d(C_m)=d(C).
\]
Dimensions add, giving
\[
\dim C_m=m\dim C.
\]

Finally, every simple cycle in a disjoint union lies wholly inside one component. There are \(m\) identical components, so every simple Tanner-cycle multiplicity is multiplied by exactly \(m\).

## Verification

`artifacts/verify.py` uses only the Python standard library.

It reconstructs the source example based on the Cayley digraph
\[
\operatorname{Cay}(\mathbb Z_{12},\{1,2,6\}),
\]
whose code is listed in the source as a binary
\[
[12,2,8]
\]
code. Direct enumeration of its \(2^{12}\) ambient vectors gives rank \(10\) and weight enumerator
\[
W_C(z)=1+3z^8.
\]

For a three-cycle permutation matrix \(P\), the script constructs
\[
H=A\otimes P,
\]
checks the exact identity
\[
H(I_{12}\otimes P^T)=A\otimes I_3,
\]
performs the perfect shuffle, and verifies that the result is
\[
I_3\otimes A.
\]

It computes the binary rank of the \(36\times36\) lifted check matrix as \(30\), so the lifted code has dimension \(6\) and exactly \(64\) words. It then enumerates the \(4^3=64\) direct-sum words, transports them through the verified coordinate permutations, checks every transported word against \(H\), and obtains
\[
W_{C_3}(z)
=
(1+3z^8)^3.
\]

The Tanner graph of the base example is checked to be connected, while the lifted Tanner graph is checked to have exactly three connected components, each with the same bipartite size as the base component. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Mostarac and Šimac prove that the uniform Kronecker construction produces a binary LDPC code with length and dimension multiplied by \(m\) while preserving the minimum distance. Their proof uses the permutation-block structure but does not state the stronger direct-sum decomposition, the disconnected Tanner-graph conclusion, or the induced weight-enumerator and cycle-multiplicity formulas.

The same paper immediately gives a broader construction in which distinct permutation matrices may occupy distinct nonzero block positions and notes that this yields greater diversity. The decomposition proved here explains why that generalization is structurally important: using one common permutation everywhere cannot mix the constituent Tanner graphs.

Earlier work on LDPC codes from Deza graphs and the general literature on permutation-matrix graph lifts provide the surrounding framework, but the inspected sources did not state that this particular published uniform Kronecker family is code-equivalent to a direct sum or derive its complete weight-enumerator factorization.

## Limitations

The result applies only to the uniform single-permutation Kronecker construction. It does not classify the source's position-dependent permutation-block lifts.

It concerns code equivalence under coordinate permutations and Tanner-graph isomorphism. It does not claim that all graph-theoretic structure of the associated directed Deza digraph decomposes in the same way.

The weight-enumerator formula is for the ordinary Hamming weight enumerator. No claim is made here about equivalence classes under larger automorphism groups beyond the explicit coordinate permutation.

## References

1. Nina Mostarac and Marina Šimac, *LDPC codes from Deza digraphs*, Glasnik Matematički 61 (2026), 175--194, DOI 10.3336/gm.61.1.08.
2. D. Crnković, S. Rukavina, and M. Šimac, *LDPC Codes from Deza Graphs*, Problems of Information Transmission 61 (2025), 219--234, DOI 10.1134/S0032946025030019.
