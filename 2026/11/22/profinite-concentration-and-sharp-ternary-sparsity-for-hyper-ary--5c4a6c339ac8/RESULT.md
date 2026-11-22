# Profinite concentration and sharp ternary sparsity for hyper-ary partition counts

## Finding
For an integer \(b\ge2\), let \(h_b(n)\) be the number of partitions of \(n\) into powers of \(b\), with each power used at most \(b\) times. In particular, \(h_b(0)=1\). Let
\[
E_{b,q}(r)=\#\{0\le n<b^r:q\nmid h_b(n)\}
\]
for positive integers \(r\) and \(q\ge2\). **For every \(b\ge3\) and every \(q\ge2\)**,
\[
\boxed{E_{b,q}(r)\le b^r(1-b^{-(q+1)})^{\lfloor r/(q+1)\rfloor}.}
\]
Consequently, for every fixed \(q\), the natural density of indices whose partition count is divisible by \(q\) is one; equivalently, the empirical residue distributions of \(h_b(n)\) converge to the Dirac measure at zero on the profinite integers. This is a simultaneous statement for all fixed moduli, not merely a parity statement.

There is also an **exact and sharp ternary law**. Put
\[
N_b(r)=\#\{0\le n<b^r:3\nmid h_b(n)\}.
\]
For every \(b\ge2\),
\[
\boxed{\sum_{r\ge0}N_b(r)z^r=
\frac{1+z^2-4z^3}{(1-z)\bigl(1-(b-1)z-(b-2)z^2-4z^3\bigr)}.}
\]
For each fixed \(b\ge3\), let \(\lambda_b\) be the largest positive real root of
\[
t^3-(b-1)t^2-(b-2)t-4=0.
\]
Then \(1<\lambda_b<b\), and with \(\alpha_b=\log_b\lambda_b\),
\[
\boxed{\#\{0\le n<X:3\nmid h_b(n)\}=\Theta_b(X^{\alpha_b})}
\]
for all sufficiently large real \(X\). Thus the all-modulus zero-density theorem has a precise nontrivial sharp power-law refinement at modulus three.

## Assumptions and scope
Indices are nonnegative integers; \(b\ge2\) is an integer base. The concentration theorem is asserted for each fixed \(b\ge3\) and each fixed integer modulus \(q\ge2\), not uniformly in either parameter. The ternary generating-function identity holds even for \(b=2\); its stated zero-density exponent is for \(b\ge3\). Every interval \([0,b^r)\) includes indices with leading-zero base-\(b\) expansions, as needed in the digit argument. In the \(\Theta_b\) notation the implicit constants depend on the fixed base. The profinite statement refers to the ordinary projective limit of the rings \(\mathbb Z/q\mathbb Z\), and weak convergence of empirical distributions.

## Proof
**Digit recursion.** The generating product \(\prod_{j\ge0}(1+x^{b^j}+\cdots+x^{b\cdot b^j})\) yields the classical identities
\[
h_b(bn)=h_b(n)+h_b(n-1)\quad(n\ge1),\qquad
h_b(bn+d)=h_b(n)\quad(1\le d<b),
\]
with \(h_b(-1)=0\). For a digit-expanded index \(n\), write its state \((x,y)=(h_b(n),h_b(n-1))\). Appending a least-significant digit \(d\) gives the following integer-linear maps:
\[
T_0(x,y)=(x+y,y),\quad T_1(x,y)=(x,x+y),\quad
T_d(x,y)=(x,x)\quad(2\le d<b).
\]
This is also true at \(n=0\), with the initial state \((1,0)\); in particular leading zeros are harmless. The identities determine all \(h_b(n)\) exactly by reading the base-\(b\) digits from most to least significant.

**A modular reset word.** Fix \(b\ge3\) and \(q\ge2\), and take the digit word consisting of \(2\), followed by \(q-1\) zero digits, followed by \(2\). For every initial integer state \((x,y)\), the successive transformations are
\[
(x,y)\longmapsto(x,x)\longmapsto(qx,x)\longmapsto(qx,qx).
\]
The terminal state is zero modulo \(q\), and all further digit maps preserve the zero state. Let \(L=q+1\) be the word length. Partition the first \(L\lfloor r/L\rfloor\) digits of an arbitrary \(r\)-digit expansion into disjoint blocks of length \(L\). An index counted by \(E_{b,q}(r)\) must avoid the distinguished reset word in every one of these blocks. There are \(b^L-1\) other words per block, and the remaining digits are arbitrary; hence
\[
E_{b,q}(r)\le b^{r-L\lfloor r/L\rfloor}
(b^L-1)^{\lfloor r/L\rfloor}
=b^r(1-b^{-L})^{\lfloor r/L\rfloor}.
\]
The ratio tends to zero exponentially in \(r\). If \(b^r\le X<b^{r+1}\), monotonicity and division by \(X\) transfer this conclusion to every real cutoff \(X\to\infty\). For every \(q\), the residue mass at zero therefore tends to one. Convergence on all finite residue-cylinder functions, followed by uniform approximation of continuous functions, gives weak convergence to the point mass at zero on the profinite completion.

**Complete ternary transfer.** Reduce states modulo three. The zero state is absorbing. The eight nonzero states form four opposite pairs, with representatives
\[
A=(1,0),\quad B=(0,1),\quad C=(1,1),\quad D=(1,2).
\]
Since digit transformations are linear, these opposite pairs can be combined without affecting whether the first component is zero. The counting transfer matrix, with state order \(A,B,C,D\), is
\[
P_b=\begin{pmatrix}
1&0&b-1&0\\
0&1&1&0\\
0&0&b-2&2\\
1&1&b-2&0
\end{pmatrix}.
\]
The initial state is \(A\), and the first coordinate is nonzero precisely in classes \(A,C,D\). Thus, with \(e_A=(1,0,0,0)\) and \(v=(1,0,1,1)^{\mathsf T}\),
\[
N_b(r)=e_AP_b^rv.
\]
Direct inversion of \(I-zP_b\), or solving the four elementary linear equations for its first coordinate, yields
\[
e_A(I-zP_b)^{-1}v=
\frac{1+z^2-4z^3}{(1-z)(1-(b-1)z-(b-2)z^2-4z^3)}.
\]
Equivalently, its denominator is \(1-bz+z^2+(b-6)z^3+4z^4\), so the assertion is an exact integer-coefficient recurrence, not a fitted finite sequence.

**Sharp growth.** For every \(b\ge3\), \(P_b\) is a primitive nonnegative matrix: its directed graph is strongly connected, and state \(A\) has a self-loop. Row \(B\) has total outgoing nonabsorbed weight only \(2<b\), while the other row totals are \(b\). Irreducibility and a strict row-sum deficit imply its Perron root is strictly below \(b\). Its characteristic polynomial is
\[
(t-1)\bigl(t^3-(b-1)t^2-(b-2)t-4\bigr).
\]
The cubic has exactly one positive root by Descartes' rule and has value \(-2b\) at \(t=1\); that root is \(\lambda_b>1\), and it is the Perron root. The positive left/right Perron eigenvectors have nonzero pairings with the nonnegative, nonzero vectors \(e_A\) and \(v\). Therefore, by Perron–Frobenius theory, \(N_b(r)\sim c_b\lambda_b^r\) with some \(c_b>0\). Bracketing an arbitrary cutoff between consecutive powers of \(b\) establishes the claimed sharp exponent \(\alpha_b\) for every real cutoff.

## Verification
The standalone file `verify_hyper_concentration.py` computes exact restricted-partition values using the original integer recurrence; tests the three digit maps over all applicable indices in ten bases; compares complete nonzero-mod-three block counts with powers of the independent four-state transition matrix; checks the exact generating-function recurrence for 24 levels per base; tests the reset word for many moduli and initial residue states; and verifies the concentration bound on directly enumerated blocks. All assertions use integers and the standard Python library. Running the actual included script prints `VERIFY_OK 2251422` (2,251,422 assertions). These bounded computations corroborate, but do not replace, the infinite proofs above.

## Relationship to prior work
Courtright and Sellers (2004) established the classical hyper-ary recurrence and exact progressions of divisible values (including their Theorem 3.1); those pointwise/progression results are input here, not claims of novelty. The general digit-product approach of Edgar (2018) can compute individual hyper-ary counts but does not itself state the all-modulus density-one law or the evaluated ternary level-count generating function. Studies of generalized Stern maximal values by Defant (2015) and Coons–Spiegelhofer (2015) concern extremal magnitude instead of modular frequencies. The previously published result *A parity-sparsity transition for hyper-ary partitions* evaluates the corresponding **modulo-two** level-count generating function and sharp exponent, and explicitly leaves odd-prime moduli untreated. The present exact modulus-three law is not obtained simply by substituting three into its parity formula: it uses a different projective transfer with a genuinely cubic Perron factor, and the simultaneous all-modulus concentration comes from an absorbing finite digit word.

## Limitations
The bound for a general modulus is exponential but need not have its optimal exponent; exact higher-modulus level spectra are not claimed. No statement about uniformity in \(b\) or \(q\) is made. A full-text comparison with Eom–Jeong–Sohn (2016), which addresses pointwise evaluation of hyper-ary partition functions, remained unavailable; an implicit earlier aggregate-frequency deduction in the broader digital-partition literature is an acknowledged historical-priority risk. The ternary matrix was independently checked for finite levels but its universal validity relies on the displayed digit recursion and symbolic transition argument. No independent external mathematical audit has been performed.

## References
- K. M. Courtright and J. A. Sellers, *Arithmetic Properties for Hyper m-Ary Partition Functions*, Integers **4** (2004), A06, first published 23 April 2004, https://math.colgate.edu/~integers/e6/e6.pdf.
- C. Coons and L. Spiegelhofer, *The maximal order of generalized Stern sequences*, arXiv:1511.08267, first posted 26 November 2015, https://arxiv.org/abs/1511.08267.
- C. Defant, *Upper Bounds for Stern's Diatomic Sequence and Related Sequences*, arXiv:1506.07824, first posted 25 June 2015, https://arxiv.org/abs/1506.07824.
- J. Eom, G. Jeong and J. Sohn, *Three Different Ways to Obtain the Values of Hyper m-Ary Partition Functions*, Bulletin of the Korean Mathematical Society **53** (2016), 1857–1868, https://doi.org/10.4134/BKMS.b151039.
- T. Edgar, *On the Number of Hyper m-Ary Partitions*, Integers **18** (2018), A47, https://math.colgate.edu/~integers/s47/s47.pdf.
- *A parity-sparsity transition for hyper-ary partitions*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-parity-sparsity-transition-for-hyper-ary-partitions--bb0ad70479bb/RESULT.md.
