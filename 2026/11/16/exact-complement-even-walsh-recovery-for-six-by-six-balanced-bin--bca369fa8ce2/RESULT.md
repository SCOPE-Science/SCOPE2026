# Exact complement-even Walsh recovery for six-by-six balanced binary tables

## Finding

Let \(\mathcal B\) consist of all \(6\times6\) matrices with entries in \(\{0,1\}\), every row sum equal to three, and every column sum equal to three. There are exactly \(297200\) such matrices. In the Boolean matrix group \(G=(\mathbb F_2)^{6\times6}\), define the unnormalized Walsh multiplier
\[
W(S)=\sum_{B\in\mathcal B}(-1)^{\langle S,B\rangle},\qquad S\in G,
\]
where the inner product is taken modulo two. **For every frequency \(S\)**, if its number of ones \(|S|\) is odd then \(W(S)=0\); if \(|S|\) is even then
\[
W(S)\equiv16\pmod {32}.
\]
Thus the Fourier zero set is *exactly* the odd-cardinality characters, and the smallest nonzero absolute multiplier is exactly \(16\), attained explicitly by a frequency whose entries outside the lower-right \(5\times5\) block are zero and whose lower-right row-major binary mask is the integer \(36045\).

Let \(T f=1_{\mathcal B}*f\) be unnormalized convolution on \(G\), and let \(J\) be the all-one matrix. Its rank and nullity are both \(2^{35}=34359738368\), with
\[
\|T^\dagger\|_{\ell^2\to\ell^2}=\frac1{16},\qquad
\kappa_{\mathrm{positive}}(T)=\frac{297200}{16}=18575.
\]
The orthogonal projection onto the range of \(T\) is exactly
\[
(Pf)(X)=\frac{f(X)+f(X+J)}2.
\]
Consequently \(\|P\|_{\ell^p\to\ell^p}=1\) for every \(1\le p\le\infty\). The range consists precisely of functions invariant under \(X\mapsto X+J\); the kernel consists of the anti-invariant functions.

## Assumptions and scope

All labels are retained: rows and columns are each ordered \(0,1,\ldots,5\). Matrices are distinct if any coordinate differs; no quotient by row/column permutations is taken. The ambient group has size \(2^{36}\), and the Walsh transform is unnormalized (so \(W(0)=297200\)). The matrix-entry complement map is \(B\mapsto B+J\). All arithmetic and Fourier identities are exact, over the integers or the Boolean field, not floating-point computations.

## Proof

**Odd frequencies.** Since every row of \(B\in\mathcal B\) has three ones, \(B+J\) also belongs to \(\mathcal B\). The complement map has no fixed point. The summands for \(B\) and \(B+J\) cancel when \(\langle S,J\rangle=|S|\pmod2\) is odd. Hence \(W(S)=0\) for odd \(|S|\).

**Frequency reduction.** For each row and column, let \(R_i\) or \(C_j\) be the full corresponding six-entry frequency mask. Since every matrix has row/column sum three,
\[
W(S+R_i)=-W(S),\qquad W(S+C_j)=-W(S).
\]
The row and column masks span a subspace of dimension \(6+6-1=11\). Each coset has a unique representative whose first row and first column are zero: the only row/column-mask combination vanishing on all these eleven positions is the zero mask. Consequently it is sufficient to evaluate precisely \(2^{25}\) representatives supported in the lower-right \(5\times5\) block. Since each row/column mask has six coordinates, the parity of \(|S|\) is unchanged by this reduction; the coefficient may change sign, but its absolute value and zero status do not.

**Exact finite certificate for the even coefficients.** Enumerate the \(\binom63=20\) possible row masks, consecutively selecting six such rows while maintaining six remaining column capacities initially equal to three. Accept only sequences that exhaust all capacities. For each accepted matrix place a one at the binary index of its lower-right \(5\times5\) block, using row-major ordering of rows and columns \(1,\ldots,5\). The other eleven entries are uniquely determined by the row and column margins, so this is an injective encoding of all accepted matrices. The recursion produces exactly \(297200\) matrices. Apply the integer Walsh–Hadamard butterfly \((a,b)\mapsto(a+b,a-b)\) along each of the 25 coordinate axes. The exhaustive check over all \(33554432\) transformed entries yields:
\[
\#\{s:W(s)=0\}=16777216,\quad W(s)=0\text{ for every odd }|s|,
\]
\[
W(s)\equiv16\pmod{32}\text{ for every even }|s|,
\quad \min_{W(s)\ne0}|W(s)|=16.
\]
The reduced representative with binary integer index \(36045\), of Hamming weight eight, has exact multiplier \(16\). The independent column-first verifier repeats the enumeration and the complete 25-axis transform with a different algorithm and obtains identical assertions. The exact Parseval check is \(\sum_s W(s)^2=2^{25}\cdot297200=9972377190400\). The two complete programs are supplied as standalone source artifacts, with assertions checking the claimed facts. These finite exhaustive programs are part of the proof of the specific six-by-six assertion, not empirical sampling.

**Operator consequences.** The 11-dimensional frequency-gauge classes all have equal zero status, so exactly half the \(2^{36}\) full multipliers vanish. All remaining multipliers have absolute value at least 16, with equality attained, while the maximum absolute value is \(W(0)=297200\) by the triangle inequality. Fourier diagonalization of counting convolution gives the claimed rank, nullity, pseudoinverse norm and condition number. A multiplier is nonzero precisely when \(\langle S,J\rangle=0\), so the Fourier range projection is \((I+\tau_J)/2\). It is the average of two isometries on every \(\ell^p\), has norm at most one, and fixes constants, giving norm exactly one.

## Verification

Two independently written, exact-integer programs are included: `check_spectrum.cpp` enumerates rows with remaining column capacities and carries out an integer butterfly; `check_spectrum.py` enumerates columns with remaining row capacities and carries out a separate NumPy integer transform. Both check the full \(2^{25}\) frequency table, the \(297200\) table count, the zero locus, the modulo-32 congruence, the nonzero minimum, and the Parseval identity. Reproduce with `g++ -O3 -std=c++17 check_spectrum.cpp -o check_spectrum && ./check_spectrum` and `python check_spectrum.py` (Python 3 and NumPy required). Both finished with PASS in the reported verification. No approximate arithmetic is used.

## Relationship to prior work

Binary contingency tables with fixed margins and their interpretation as fixed-degree bipartite graphs are classical. Blanchet and Stauffer study exact uniform sampling and approximate cardinality of such sets, not their Boolean character sums. De Launey and Levin analyze Fourier inversion for a different combinatorial design family (partial Hadamard matrices) but do not evaluate the signed row-and-column-margin sums here. Existing enumeration tables record the number \(297200\) but not the exact Fourier zero locus. The elementary complement symmetry alone forces odd-frequency zeros; because \(297200\) is divisible by \(32\), it does not establish that the even-frequency block is zero-free. The new assertion is the uniform modulo-32 residue for *all* even frequencies and the resulting sharp deconvolution stability.

## Limitations

The result is specific to the labelled six-by-six matrix family with margins three. It does not prove the corresponding nonvanishing congruence for other margin vectors or larger balanced tables. The strong modulo-32 assertion rests on a finite complete integer certificate, independently regenerated, rather than a closed-form symbolic proof for arbitrary sizes. Unindexed or differently worded pre-existing evaluations may pose historical-priority risk. Independent external mathematical audit has not been performed.

## References

- J. Blanchet and A. Stauffer, *Characterizing Optimal Sampling of Binary Contingency Tables via the Configuration Model*, arXiv:1007.1214, initial public version July 7, 2010, https://arxiv.org/abs/1007.1214.
- W. de Launey and D. A. Levin, *A Fourier-analytic Approach to Counting Partial Hadamard Matrices*, arXiv:1003.4003, March 21, 2010, https://arxiv.org/abs/1003.4003.
- OEIS A058527, counts of balanced \(2n\times2n\) binary matrices; https://oeis.org/A058527 (only the cardinality is used as comparison evidence).
