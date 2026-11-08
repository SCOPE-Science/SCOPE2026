# The full ambient symmetry group of the four-point Segre determinant has 192 components

## Finding
Over \(\mathbb C\), let \(Q=\mathbb P^1\times\mathbb P^1\) be the Segre quadric, and let \(D\subset Q^4=(\mathbb P^1)^8\) be the reduced divisor of ordered quadruples lying in a hyperplane in the Segre embedding. Its complete stabilizer **inside the automorphism group of the ambient product** is
\[
\operatorname{Stab}_{\operatorname{Aut}(Q^4)}(D)
= (\operatorname{PGL}_2\times\operatorname{PGL}_2)\rtimes F,
\qquad |F|=192,
\]
where
\[
F=\big\{(\sigma,\tau)\in S_4\times S_4:\bar\sigma=\bar\tau\text{ in }S_4/V_4\big\}\rtimes C_2.
\]
The \(C_2\) interchanges the two four-factor blocks, and \(V_4\) is the normal Klein four group of double transpositions. Thus \(F\) has \(24\cdot4\cdot2\) elements. In particular, the two sets of four labels may be permuted **independently by a Klein four permutation**, an extra symmetry invisible if all labels are required to move together.

## Assumptions and scope
All varieties and groups are over \(\mathbb C\). Write the eight homogeneous factor coordinates as \((a_{i0}:a_{i1})\) and \((b_{i0}:b_{i1})\), for \(i=1,2,3,4\). Put \(F(a,b)=\det(a_i\otimes b_i)_{i=1}^4\), where the columns correspond in order to \((0,0),(0,1),(1,0),(1,1)\). The divisor is \(D=V(F)\). We compute the subgroup of automorphisms of the **ambient eightfold** preserving the divisor. We make no assertion about all abstract automorphisms of \(D\).

## Proof
The full ambient automorphism group is \((\operatorname{PGL}_2)^8\rtimes S_8\). The two diagonal \(\operatorname{PGL}_2\) actions on the first and last four factors preserve \(F\) up to a nonzero scalar because applying \(g\otimes h\) to the four rows scales the determinant by \((\det g)^2(\det h)^2\). Call their product \(G_0\), of dimension six.

**Infinitesimal maximality.** Expand \(F\) in the binary monomial basis of \(H^0((\mathbb P^1)^8,\mathcal O(1,\ldots,1))\). Its 24 nonzero coefficients are indexed by the eight-bit strings \((a_1,\ldots,a_4,b_1,\ldots,b_4)\) such that \(\sum a_i=\sum b_i=2\) and \(\sum a_ib_i=1\); the coefficient is the parity of the column permutation \((2a_i+b_i)_{i=1}^4\). For the usual three generators \(E_i,F_i,H_i\) of each \(\mathfrak{sl}_2\) acting on the \(i\)-th tensor factor, form the integer matrix \(M\) of their images of this 24-term coefficient tensor in the 256-dimensional binary monomial basis. The accompanying exact checker constructs all entries and obtains \(\operatorname{rank}_{\mathbb Q}M=18\). Augmenting by the original tensor yields rank 19, so even allowing a scalar multiple of \(F\) introduces no further infinitesimal stabilizer. Therefore the infinitesimal projective stabilizer has dimension \(24-18=6\), exactly that of \(G_0\). In characteristic zero this identifies the connected identity subgroup of the algebraic stabilizer with \(G_0\).

**All remaining components.** Every automorphism preserving \(D\) normalizes its identity stabilizer \(G_0\). Inside \((\operatorname{PGL}_2)^8\), the diagonal \(\operatorname{PGL}_2\) in each four-factor block is self-normalizing; among permutations of the factors, its normalizer preserves or exchanges the two four-element blocks. Hence any stabilizer element is in \(G_0\) times a permutation of this block-preserving or block-exchanging type. In the 24-term support, two distinct variables occur together as 1 in exactly four monomials if they are in the same block, and in exactly six if they are in different blocks. The support therefore intrinsically determines the two unordered four-element blocks. The simultaneous row/column choice is a permutation of the four binary pairs, so a block-preserving permutation \((\sigma,\tau)\) preserves the support precisely when it induces the same permutation of the three unordered perfect matchings of four labels. The kernel of \(S_4\to S_3\) is \(V_4\). The criterion is \(\bar\sigma=\bar\tau\) in \(S_4/V_4\). The exact signed-coefficient check verifies that every such permutation sends \(F\) to \(F\) or \(-F\); the exchange of the two blocks also sends \(F\) to a scalar multiple (it transposes the tensor-product row coordinates). Thus precisely \(24\cdot4\cdot2=192\) permutation cosets occur, and the asserted semidirect product follows.

## Verification
Run `python verify_segre_symmetry.py` using Python 3 and SymPy. This enumerates all 24 signed monomials, builds and ranks the exact 256-by-24 integer infinitesimal-action matrix, separately checks the augmented projective-action rank, verifies the two four-blocks from monomial co-occurrences, and checks the 192 signed permutation symmetries. The computation is finite and exhaustive. The group-theoretic normalizer and identity-component arguments above make the computation an all-parameter proof, not an extrapolation.

## Relationship to prior work
Pratt's *The Segre Determinant* introduces the determinant in a more general setting and relates it to Chow–Lam forms; the coplanarity and cross-ratio interpretation is used here as **prior context**. The classical six-value anharmonic action of \(S_4\) on a cross-ratio explains the kernel \(V_4\); the additional claim here is maximality of the full ambient-product stabilizer, including its identity component. Existing work on the same four-point divisor also analyzes its singular locus, a different invariant. No claim of priority over a possible earlier symmetry computation under alternative terminology is made.

## Limitations
Only ambient-product automorphisms are classified, not all abstract automorphisms of the possibly singular divisor. The main primary paper's accessible abstract was checked, but its complete full text could not be independently read in this investigation; the possibility of an equivalent group statement in inaccessible primary literature remains a historical-priority risk. Independent verification has not been performed.

## References
1. Elizabeth Pratt, *The Segre Determinant*, arXiv:2505.09204v1, first public 2025-05-14.
2. Classical cross-ratio identities, including the anharmonic \(S_4\to S_3\) action and its Klein-four kernel.
