# Ternary Fourier rigidity and a rank-three resonance for signed permutation matrices

## Finding

For each integer \(n\ge1\), let \(G_n=(\mathbb F_3)^{n\times n}\). Let \(\mathcal B_n\subset G_n\) consist of the \(2^n n!\) signed permutation matrices: matrices with one nonzero entry, equal to \(+1\) or \(-1\), in each row and column. Define the *unnormalized counting convolution* \(T_nf(x)=\sum_{B\in\mathcal B_n}f(x-B)\), and write \(\omega=e^{2\pi i/3}\).

For any character indexed by \(K\in G_n\), let \(Z(K)\) be the binary matrix of those positions at which \(K_{ij}=0\). Then its multiplier is the **integer**
\[
W_n(K)=\sum_{B\in\mathcal B_n}\omega^{\langle K,B\rangle}=\operatorname{per}(3Z(K)-J_n)
=\sum_{k=0}^n(-1)^{n-k}3^k(n-k)!\,r_k(Z(K)),
\]
where \(J_n\) is the all-ones matrix and \(r_k(Z)\) is the number of placements of \(k\) nonattacking rooks on the 1-cells of \(Z\), with \(r_0=1\).

**Infinite zero-free family.** For every integer \(a\ge1\), and \(n=3^a-1\) or \(n=3^a-2\), every character satisfies
\[
v_3(W_n(K))=v_3(n!)\quad\text{and}\quad W_n(K)\ne0.
\]
Thus \(T_n\) is invertible in all these ranks, and \(\|T_n^{-1}\|_{\ell^2\to\ell^2}\le3^{-v_3(n!)}\). The additional ranks \(n=4,5\) are also zero-free, with \(W_4(K)\equiv6\pmod9\) and \(W_5(K)\equiv6\pmod9\) for every \(K\).

**First resonance and recovery.** At \(n=3\), exactly 3,816 of the 19,683 characters vanish, and \(\operatorname{rank}T_3=15,867\). Their zero-position boards form exactly four orbits under independent row and column permutations and transposition, with orbit size and number of zero positions respectively \((9,1),(9,4),(36,4),(18,7)\). Weighting each board by \(2^{9-r}\), where \(r\) is its number of zero positions, gives \(2,304+288+1,152+72=3,816\) vanishing characters. At \(n=4\), every one of the \(3^{16}=43,046,721\) characters is nonzero: \(\operatorname{rank}T_4=43,046,721\). Its smallest multiplier magnitude is exactly \(3\), its largest is \(384\), and \(\|T_4^{-1}\|_{\ell^2\to\ell^2}=1/3\).

## Assumptions and scope

All arithmetic on the ambient matrix entries and in the character pairing is modulo three; a negative sign is the residue 2. Signed permutation matrices themselves are counted once each, with no normalization. Character multiplicities in the finite tables include both choices \(+1\) and \(-1\) at each nonzero frequency coordinate. Invertibility refers to the linear counting convolution on complex functions on the finite additive group \(G_n\); the group law is matrix addition, not signed permutation multiplication.

## Proof

Fix a permutation \(\pi\). Summing independently over its \(n\) chosen signs gives
\[
\sum_{\varepsilon_i\in\{\pm1\}}\omega^{\sum_i\varepsilon_iK_{i,\pi(i)}}
=\prod_i\bigl(\omega^{K_{i,\pi(i)}}+\omega^{-K_{i,\pi(i)}}\bigr)
=\prod_i(3Z(K)_{i,\pi(i)}-1).
\]
Summing over permutations proves the permanent identity. Expanding the product by selecting \(k\) distinct zero cells in distinct rows and columns proves the rook expansion: each \(k\)-rook placement lies in precisely \((n-k)!\) full permutations, and the remaining factors contribute \((-1)^{n-k}\).

For the infinite-family congruence, put \(n=3^a-b\), with \(b\in\{1,2\}\). For \(0\le j\le k-1\), the integers \(3^a-b-j\) and \(b+j\) have the same 3-adic valuation (both are positive and strictly less than \(3^a\)). Therefore
\[
v_3\bigl(n!/(n-k)!\bigr)=v_3\bigl((k+b-1)!/(b-1)!\bigr).
\]
For every \(k\ge1\), this valuation is strictly below \(k\), by the elementary factorial bound \(v_3(m!)\le(m-1)/2\) together with direct verification at \(k=1\). Thus every nonconstant term in the rook expansion has strictly larger 3-adic valuation than the \(k=0\) term \((-1)^n n!\). Hence \(W_n(K)\equiv(-1)^nn!\pmod{3^{v_3(n!)+1}}\), proving nonvanishing and the stated common valuation. Fourier diagonalization on \(G_n\) gives invertibility and the inverse-norm bound.

For \(n=4\) or \(5\), the \(k=0\) term has 3-adic valuation one. The \(k=1\) term is divisible by nine, since \(3(n-1)!\) is; all \(k\ge2\) terms are also divisible by nine. Thus the permanent is congruent to 6 modulo nine in either rank. This proves the zero-free assertions without computer enumeration.

For \(n=3\), there are only \(2^9=512\) possible zero-position boards. The finite identity reduces their multipliers to \(-6+6r_1-9r_2+27r_3\). Exhausting these 512 binary boards with the attached exact checker yields 72 zero boards, grouped into four stated orbits. Their canonical masks, in row-major bit order with the lowest bit at position \((1,1)\), are 1 (orbit size 9), 15 (size 36), 27 (size 9), and 127 (size 18). These account for all 72, and the independent direct sum over all 48 signed permutation matrices agrees on all 19,683 characters. The weighted orbit counts give the rank claim. For \(n=4\), the rook expansion and an independent direct permanent calculation agree on every binary zero-position board; summing frequency multiplicities yields the full 27-level integer spectrum in the attached CSV. Its absolute minimum is three and its maximum is 384.

## Verification

Run `python3 check_signed_permutation.py signed_perm_rank3_zeros.csv signed_perm_rank4_spectrum.csv` in a directory containing all three attachments. The checker uses two independent exact routes to each small-rank multiplier: direct permutation expansion and a row-by-row rook recurrence. It separately enumerates all ternary characters in the three-by-three case, verifies the 72 board-level zeros and four symmetry orbit sizes, and checks the complete fourth-rank frequency histogram and its congruences. The CSV files are finite certificates of the null boards and rank-four spectrum; no probabilistic tests or floating-point tolerance enter these calculations. The infinite-rank result is established by the preceding symbolic proof, not inferred from the finite checks.

## Relationship to prior work

Signed permutations and their type-\(B\) statistics are classical; see Foata and Han (2006). Rook-polynomial identities and recursive enumeration are classical; see Mitchell (2004). The present object is the additive Fourier transform of the **entire signed-permutation matrix orbit embedded in a ternary matrix space**, not the ordinary group Fourier transform on the hyperoctahedral group, a restriction to a single conjugacy class, or a binary permutation-matrix transform. The rook transform formula uses known permanent and rook methods. The new outcome assessed here is the specific zero-free 3-adic family together with the first singularity/recovery threshold and complete rank-three zero-locus classification, rather than an assertion that rook theory itself is new.

## Limitations

The exact zero-locus classification concerns rank three; higher-rank characters outside the proved zero-free families are not classified. In particular, no universal invertibility criterion for arbitrary \(n\) is claimed. The least multiplier in the infinite zero-free family need not attain the stated 3-adic lower bound. The priority comparison is bounded to searched mathematical records and inspected primary sources, and no independent mathematical audit has been performed.

## References

1. A. G. Mitchell, *A Block Decomposition Algorithm for Computing Rook Polynomials*, arXiv:math/0407004, first posted 2004-06-30. https://arxiv.org/abs/math/0407004
2. D. Foata and G.-N. Han, *Signed Words and Permutations, IV; Fixed and Pixed Points*, arXiv:math/0606566, first posted 2006-06-23. https://arxiv.org/abs/math/0606566
3. J. R. Goldman, J. T. Joichi, D. L. Reiner, D. E. White, *Rook Theory. II: Boards of Binomial Type*, SIAM Journal on Applied Mathematics 31 (1976), 618–633. https://doi.org/10.1137/0131055
