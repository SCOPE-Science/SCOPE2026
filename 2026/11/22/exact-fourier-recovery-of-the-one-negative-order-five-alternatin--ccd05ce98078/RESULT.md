# Exact Fourier recovery of the one-negative order-five alternating-sign matrix stratum

## Finding
Let \(\mathcal A\) be the 200 fully labelled \(5\times5\) alternating-sign matrices with exactly one entry \(-1\). Encode each by its nonzero-cell incidence vector \(e(A)\in\mathbb F_2^{25}\). Their unnormalized Walsh transform is
\[
W(S)=\sum_{A\in\mathcal A}(-1)^{\sum_{(i,j)\in S}e(A)_{ij}},\qquad S\subseteq\{0,1,2,3,4\}^2.
\]
The counting-convolution operator \(Tf(x)=\sum_{A\in\mathcal A}f(x+e(A))\) on complex or real functions on \(\mathbb F_2^{25}\) has precisely \(4{,}194{,}816\) zero Walsh multipliers, hence rank \(29{,}359{,}616\). Its least nonzero multiplier magnitude is \(4\), and its largest is \(200\), giving sharp condition number \(50\) on the recoverable Hilbert subspace.

Exactly twelve Walsh zeros are supported on two cells, while none are supported on one cell. Index cells from \(0\) to \(24\) in row-major order. The twelve unordered pairs are
\[
\{6,12\},\{6,13\},\{6,17\},\{7,16\},\{7,18\},\{8,11\},\{8,12\},\{8,17\},\{11,18\},\{12,16\},\{12,18\},\{13,16\}.
\]
Under the eight symmetries of the square, they comprise an orbit of four represented by \(\{6,12\}\), and an orbit of eight represented by \(\{6,13\}\). Exactly \(200\) three-cell characters vanish.

The unique translation-invariant projection onto the range has optimal operator norm even among all (not necessarily invariant) real or complex projections:
\[
\min_{Q:\,Q^2=Q,\operatorname{ran}Q=\operatorname{ran}T}\|Q\|_{\ell^1\to\ell^1}
=\min_Q\|Q\|_{\ell^\infty\to\ell^\infty}
=\frac{2{,}170{,}129}{32{,}768}.
\]

## Assumptions and scope
An alternating-sign matrix is a square matrix with entries in \(\{-1,0,1\}\) whose nonzero entries alternate \(+1,-1,+1,\ldots,+1\) in every row and column; all row and column sums equal one. We retain exactly one negative entry and record **all occupied cells**, not only the positive cells. Every such order-five matrix has seven occupied cells (six positives and one negative); the occupancy profile uniquely determines the signed matrix by alternation. No quotient by rotations, reflection, row permutations or column permutations is applied. The convolution is unnormalized, and norms are with respect to counting measure; the condition ratio is unchanged under normalized Haar measure.

## Proof
**Exhaustiveness of the enumerator.** Every row has entries in \(\{-1,0,1\}\), each prefix sum in \(\{0,1\}\), and full sum \(1\). Enumerate all such length-five rows. For each partial five-row assembly, retain a row only when every column's running sum remains in \(\{0,1\}\), then at the end demand each sum equal \(1\). These constraints are necessary and sufficient for the alternating property of every row and column: a \(0/1\) partial sum toggles exactly at nonzero entries, beginning with positive \(1\). Thus the tree enumerates every order-five alternating-sign matrix exactly once. The complete tree has \(429\) leaves, including \(200\) with exactly one negative entry; their occupancy masks are distinct. A separate independently structured Python enumerator reproduces both totals and all signed one-, two-, and three-cell characters.

**Exact Fourier census.** Set \(f(x)\) equal to the number of listed matrices with occupancy vector \(x\in\mathbb F_2^{25}\). The in-place integer butterfly \((u,v)\mapsto(u+v,u-v)\) applied successively in the 25 coordinate directions gives \(W(S)\) at every one of the \(2^{25}\) frequencies. This standard Walsh identity follows by expanding the product of \(25\) two-point Fourier transforms. All intermediates are integers with absolute value at most \(200\). The completely enumerated transform has \(4{,}194{,}816\) zeros; its positive magnitudes are all divisible by four, with a minimum of four and maximum of 200. The full signed histogram, including every level and its multiplicity, is verified against the constants in the self-contained checker. Direct signed enumeration of all characters on at most three cells independently confirms zero counts \(0,12,200\); the twelve enumerated pairs fall into the two stated dihedral orbits.

**Convolution consequences and sharp projection norm.** The Walsh characters simultaneously diagonalize convolution and give eigenvalues \(W(S)\), hence rank and nonzero singular-value ratio. Put \(h(S)=1\) when \(W(S)\ne0\) and zero otherwise, and let \(K\) be its inverse Walsh transform with Fourier inversion factor \(2^{-25}\). The canonical Fourier range projection \(P\) is convolution by \(K\), so its \(\ell^1\) and \(\ell^\infty\) norms both equal \(\sum_x|K(x)|\). A second exact integer Walsh transform of \(h\) gives
\[
\sum_{x\in\mathbb F_2^{25}}\left|\sum_{S}h(S)(-1)^{S\cdot x}\right|=2{,}222{,}212{,}096,
\]
which after division by \(2^{25}\) reduces to \(2{,}170{,}129/32{,}768\). For any projection \(Q\) onto the translation-invariant range, average its conjugates over all translations. This cannot increase either endpoint norm and yields a translation-invariant projection with the same range. Fourier diagonalization forces it to be precisely \(P\): its multipliers must be one on the range frequencies and zero outside. Thus no other projection has smaller endpoint norm.

## Verification
Compile the included `check_spectrum.cpp` with `g++ -std=c++17 -O3 check_spectrum.cpp -o check_spectrum` and run `./check_spectrum`. The exact integer test returns `ONE_MINUS_ASM5_WALSH_PASS`, independently checks the entire unnormalized signed histogram, all \(2^{25}\) Fourier modes, the minimum gap and reverse-transform absolute sum. Run `python3 verify_small.py` to enumerate all 429 matrices with a different generator and to check the low-support signed sums directly, without a Fourier-transform algorithm. The observed output is `INDEPENDENT_LOW_DEGREE_PASS 429 200 [0, 12, 200]`. The C++ test requires approximately 160 MiB of memory; no floating-point comparisons or stochastic estimates are used. Exhaustive finite integer enumeration is complete for this precisely specified finite object; no claim for all matrix orders is inferred.

## Relationship to prior work
Lalonde's original study of alternating-sign matrices with exactly one negative entry treats bijections and refined enumeration, including reflection and path configurations; its full text was reviewed for those results. Existing Fourier calculations for **all** order-four alternating-sign matrices concern a different matrix order and a larger family. Existing order-five results on low-degree Fourier tomography concern injectivity of truncated marginals, not the complete counting-convolution multiplier spectrum or unrestricted optimal endpoint projection norm. The order-five **permutation** family omits the unique negative entry and is different as well. These comparisons do not establish absolute historical priority; an independently published, unindexed exact signed-occupancy calculation could coincide with this finite result.

## Limitations
The classification and exact norms concern only the 200 labelled order-five matrices with exactly one negative entry, encoded by nonzero occupancy. It is not a theorem for higher orders, the full 429-matrix family, or the ternary encoding that retains signs. The computation uses a complete finite search and an exact transform, not a shorter symbolic closed formula for the entire histogram. A third-party independent mathematical audit has not been performed.

## References
1. Pierre Lalonde, *Alternating sign matrices with one -1 under vertical reflection*, arXiv:math/0401339, first submitted 2004-01-25, https://arxiv.org/abs/math/0401339.
2. Doron Zeilberger, *Proof of the Alternating Sign Matrix Conjecture*, Electronic Journal of Combinatorics 3(2), R13 (1996), https://doi.org/10.37236/1271.
3. Mills, Robbins and Rumsey, *Alternating sign matrices and descending plane partitions* (1983), as cited in Lalonde.
