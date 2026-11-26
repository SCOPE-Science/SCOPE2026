# Sharp rare-symmetry law for perfect binary evolution algebras

## Finding

Let \(E_M\) be the evolution algebra associated with a uniformly sampled invertible matrix \(M\in\operatorname{GL}_n(\mathbb F_2)\). Write \(A_n=\operatorname{Aut}_{\mathbb F_2}(E_M)\), let \(T_n=\binom n2\), and let \(I_n\) count the isomorphism classes of \(n\)-dimensional evolution algebras \(E\) over \(\mathbb F_2\) satisfying \(E^2=E\). For every \(n\ge2\), the proportion fixed by any prescribed natural-basis transposition is exactly

\[
p_n=\frac{2^{1-2n}}{(1-2^{-(n-1)})(1-2^{-n})}.
\]

As \(n\to\infty\),

\[
\Pr(A_n\ne1)=T_np_n+O(n^4 2^{-3n})\sim T_n2^{1-2n},
\]

\[
I_n=\frac{|\operatorname{GL}_n(\mathbb F_2)|}{n!}
\left(1+T_np_n+O(n^4 2^{-3n})\right),
\]

and

\[
\Pr(A_n\not\cong1\text{ and }A_n\not\cong C_2)=O(n^4 2^{-3n}).
\]

Consequently, conditioned on having any nonidentity automorphism, a uniformly sampled algebra has automorphism group \(C_2\) with probability tending to one. For contrast, a uniform (not necessarily invertible) binary matrix is fixed under a prescribed simultaneous transposition with probability \(2^{2-2n}\); invertibility asymptotically divides this probability by two.

## Assumptions and scope

The field is exactly \(\mathbb F_2\), the vector-space dimension \(n\) tends to infinity, and the uniform distribution is on the \(|\operatorname{GL}_n(\mathbb F_2)|\) *labeled structure matrices*, not on isomorphism classes. For a natural basis \(e_1,\ldots,e_n\), write \(e_ie_j=0\) when \(i\ne j\), and \(e_i^2=\sum_j M_{ji}e_j\). The requirement \(E^2=E\) is equivalent to invertibility of \(M\). The notation \(A_n\ne1\) means that the group is nontrivial; the third display bounds groups other than the trivial group and \(C_2\). The implicit constants in every big-O statement are absolute for sufficiently large \(n\). This theorem does not address other finite fields or sampling uniformly among isomorphism classes.

## Proof

**Step 1: classify algebra isomorphisms.** Suppose \(E_M\) and \(E_N\) are perfect evolution algebras and \(\phi:E_M\to E_N\) is an isomorphism. If \(Q\) is its matrix, then \(\phi(e_i)\phi(e_j)=0\) for \(i\ne j\) forces \(\sum_k Q_{ki}Q_{kj}e_k^2=0\). Because the squares form a basis, \(Q_{ki}Q_{kj}=0\) for every \(k\) and distinct \(i,j\). Each row of the invertible matrix \(Q\) has exactly one nonzero entry; invertibility therefore makes it monomial. Over \(\mathbb F_2\), all nonzero entries are one, so \(Q=P_\sigma\). Squaring the images of generators shows that \(E_M\cong E_N\) exactly when \(N=P_\sigma M P_\sigma^{-1}\). Thus \(A_n\) is the simultaneous-permutation stabilizer of \(M\), and \(I_n\) is the number of permutation-similarity orbits on \(\operatorname{GL}_n(\mathbb F_2)\). This structural reduction is established in the cited literature; only the quantitative large-dimension consequences below are proposed as new.

**Step 2: calculate the transposition contribution without singular matrices.** For a transposition \(\tau\), in characteristic two the permutation operator has form \(P_\tau=I+N\), where \(N^2=0\) and \(\operatorname{rank}(N)=1\). Choose a basis \(u,v,w_1,\ldots,w_{n-2}\) with \(Nv=u\) and \(N\) vanishing on all other basis vectors. Every linear operator commuting with \(N\) then has block form

\[
\begin{pmatrix}
\alpha&\beta&b\\
0&\alpha&0\\
0&c&B
\end{pmatrix},
\]

where \(\alpha,\beta\in\mathbb F_2\), \(b\) is a row and \(c\) a column of length \(n-2\), and \(B\) is an \((n-2)\times(n-2)\) matrix. Its determinant is \(\alpha^2\det B\), so the invertible centralizer has precisely \(2^{2n-3}|\operatorname{GL}_{n-2}(\mathbb F_2)|\) elements, with \(\operatorname{GL}_0\) understood to have one element. Since

\[
|\operatorname{GL}_n(\mathbb F_2)|=2^{n^2}\prod_{j=1}^n(1-2^{-j}),
\]

the claimed formula for \(p_n\) follows by cancellation. For a uniform unrestricted binary matrix, simultaneous transposition invariance leaves \(n^2-(2n-2)\) free binary parameters, giving probability \(2^{2-2n}\).

**Step 3: uniformly bound all other permutation symmetries.** Let \(\sigma\in S_n\) have cycle lengths \(\ell_1,\ldots,\ell_c\), including fixed points. Its invariant full matrix space has dimension

\[
d_\sigma=\sum_{i,j=1}^c\gcd(\ell_i,\ell_j),
\]

because a binary matrix commuting with \(P_\sigma\) is constant on the orbits of the simultaneous permutation action on ordered pairs of indices; the orbit count of two cycles of lengths \(\ell_i,\ell_j\) is their gcd. Consequently the number of *invertible* fixed matrices is at most \(2^{d_\sigma}\).

Write \(r=n-c\) and let \(m\) be the number of moved points. The number of nontrivial cycles is \(s=m-r\), with \(s\le r\), hence \(m\le2r\). The \(n-m\) fixed points contribute \((n-m)^2+2(n-m)s\) to the sum for \(d_\sigma\). Each ordered pair of nontrivial cycles contributes at most the length of the second cycle, giving an additional at most \(sm\). Thus

\[
d_\sigma\le(n-m)^2+2(n-m)s+ms=n^2-2nr+mr\le n^2-2r(n-r).
\]

Independently, \(\gcd(\ell_i,\ell_j)\le\ell_j\) gives \(d_\sigma\le cn=n(n-r)\). Therefore

\[
n^2-d_\sigma\ge\max\{2r(n-r),nr\}.
\]

The infinite product \(c_\infty=\prod_{j\ge1}(1-2^{-j})\) is strictly positive: the tail converges by the summability of \(2^{-j}\). Hence every permutation of deficiency \(r\) fixes a random invertible matrix with probability at most

\[
c_\infty^{-1}2^{-\max\{2r(n-r),nr\}}.
\]

Any such permutation factors into exactly \(r\) transpositions. There are therefore at most \(\left(\binom n2\right)^r\) permutations of deficiency \(r\). For \(2\le r\le n/4\), the exponent is at least \(3nr/2\), so summing the geometric majorant gives \(O(n^4 2^{-3n})\). For \(r>n/4\), the exponent is at least \(nr\), so the sum is bounded by a tail of \(\sum_r(n^2 2^{-n})^r\), which is smaller than \(O(n^4 2^{-3n})\). It follows that

\[
\sum_{\substack{\sigma\in S_n\\n-c(\sigma)\ge2}}
\Pr(P_\sigma M=MP_\sigma)=O(n^4 2^{-3n}).
\]

The estimate concerns the sum over *all* permutations, not merely the probability of one exceptional type.

**Step 4: symmetry probability and type.** Exactly \(T_n\) permutations have deficiency one; they are transpositions. Two distinct transpositions both stabilizing a matrix imply that their product stabilizes it. Such a product has deficiency two, so the union-bound and Step 3 control every intersection between transposition events by \(O(n^4 2^{-3n})\). The union therefore has probability \(T_np_n+O(n^4 2^{-3n})\). Nontransposition symmetries have probability at most the same error by Step 3. If a stabilizer contains exactly one nonidentity permutation and it is a transposition, it is \(C_2\); any other nontrivial stabilizer contains either a nontransposition or two transpositions and lies in the error event. Since \(T_np_n\) dominates the error, the conditional \(C_2\) assertion follows.

**Step 5: isomorphism-class count.** Burnside's lemma gives

\[
I_n=\frac{|\operatorname{GL}_n(\mathbb F_2)|}{n!}
\sum_{\sigma\in S_n}\Pr(P_\sigma M=MP_\sigma).
\]

The identity contributes one, the \(T_n\) transpositions contribute \(T_np_n\), and Step 3 bounds the rest. This proves the claimed sharp orbit-count correction.

## Verification

The standalone `verify.py` independently enumerates every binary matrix in dimensions one through four, determines its rank by binary row reduction, calculates every permutation stabilizer by comparing entries, and sums orbit stabilizers. It obtains \(|\operatorname{GL}_n(\mathbb F_2)|=1,6,168,20160\), corresponding isomorphism-orbit counts \(1,4,33,908\), and fixed invertible matrices under a specified transposition equal to \(2,8,192\) for dimensions two through four. Each matches the corresponding exact formula. The finite verification is not an infinite proof, and the asymptotic error bounds are proved by Steps 3–5 rather than extrapolated from data.

## Relationship to prior work

Wei and Zou (arXiv:2310.12368) establish the general orbit/Burnside framework for idempotent evolution algebras over finite fields, and give explicit isomorphism-class counts in dimensions two through four. Their isomorphism relation and the lower-dimensional counts are used as **previously known mathematics**, not claimed as new. Sriwongsa and Zou (arXiv:2202.01333) classify certain specified automorphism groups, including full symmetric groups, rather than the frequency of nontrivial automorphisms in uniform high dimension. Elduque and Labra (arXiv:1902.02191) give the structural graph/automorphism framework. Costoya, Mayorga, and Viruel (2025) study realizable permutation representations and high-transitivity obstructions, not uniform counting of random binary algebras. The proposed addition is the exact invertible transposition proportion and a sharp leading rare-automorphism and isomorphism-class correction with a uniform bound on all other types. The older exact Burnside formula logically determines each finite-degree orbit count, but its statement does not itself provide this all-dimension sharp asymptotic; deriving it uses a nontrivial centralizer count and a uniform high-cycle-deficiency estimate. An unidentified broader random-matrix symmetry theorem may nonetheless imply this result; independent priority checking remains necessary.

## Limitations

The conclusions concern the exact two-element field, uniformly labeled invertible natural-basis matrices, and \(n\to\infty\). The result does not classify nontrivial automorphism groups at finite \(n\), establish a higher-order asymptotic, describe the automorphism group scheme over extension rings, or extend to general finite fields. The probability is not for a uniformly sampled *isomorphism class*. The asserted novelty is provisional and depends on the inspected sources; independent verification has not been performed.

## References

1. Yangjiang Wei and Yi Ming Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, first public preprint 2023-10-18, https://arxiv.org/abs/2310.12368.
2. Songpon Sriwongsa and Yi Ming Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333, https://arxiv.org/abs/2202.01333.
3. Alberto Elduque and Alicia Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191, https://arxiv.org/abs/1902.02191.
4. Cristina Costoya, Pedro Mayorga, and Antonio Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterranean Journal of Mathematics 22, article 149 (2025), DOI:10.1007/s00009-025-02924-0, https://link.springer.com/article/10.1007/s00009-025-02924-0.
