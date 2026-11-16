# Exact Walsh nullity and sharp endpoint projection norm for \(4\times4\) alternating-sign matrices

## Finding

Let \(\mathcal A_4\) be the set of all \(4\times4\) alternating-sign matrices: entries belong to \(\{-1,0,1\}\), each row and column sums to \(1\), and its nonzero entries alternate in sign. Embed each matrix \(A\) in \(G=\mathbb F_2^{16}\) by the binary support vector \(b(A)_{ij}=1\) precisely when \(A_{ij}\ne0\). Let \(f\) be the indicator of these \(42\) distinct vectors and \(C_f h(x)=\sum_{y\in G}f(y)h(x-y)\) its **unnormalized** convolution operator.

At every binary frequency \(\xi\in G\), write
\[
W(\xi)=\sum_{A\in\mathcal A_4}(-1)^{\sum_{i,j}\xi_{ij}b(A)_{ij}}.
\]
The complete **absolute** multiplier distribution is as follows. Multiplicities in the right column refer to the \(512\) inequivalent reduced frequencies; those on \(G\) are precisely \(128\) times larger.

| \(\lvert W\rvert\) | Reduced multiplicity |
| ---: | ---: |
| 0 | 120 |
| 2 | 146 |
| 4 | 80 |
| 6 | 77 |
| 8 | 40 |
| 10 | 7 |
| 12 | 8 |
| 14 | 22 |
| 20 | 4 |
| 22 | 2 |
| 26 | 1 |
| 28 | 4 |
| 42 | 1 |

In particular, exactly \(15{,}360\) of the \(65{,}536\) multipliers vanish, and
\[
\operatorname{rank}C_f=50{,}176,\qquad
\min_{W(\xi)\ne0}|W(\xi)|=2,\qquad
\max_{\xi}|W(\xi)|=42.
\]
Thus \(\|C_f^\dagger\|_{2\to2}=1/2\) and the positive-spectrum Hilbert condition number is \(21\).

Let \(R=\operatorname{ran}C_f\) and let \(\Lambda_p(R)\) be the infimum of operator norms \(\|P\|_{\ell^p(G)\to\ell^p(G)}\) over **all** linear projections \(P\) onto \(R\). The exact sharp endpoint constants coincide:
\[
\boxed{\Lambda_1(R)=\Lambda_\infty(R)=\frac{199}{32}.}
\]
The minimum is achieved by the Fourier projection onto the nonzero multipliers; the assertion optimizes over arbitrary projections, not just translation-invariant ones.

## Assumptions and scope

All arithmetic is over exact integers or binary vector spaces. The order is **exactly four**; this is a natural first nontrivial even ASM order beyond the two-permutation case of order two. The binary embedding records **nonzero entries regardless of their signs**, not the usual signed matrices as real vectors. The Fourier transform and convolution are unnormalized; the projection kernel uses normalized Fourier inversion. Norms are on functions on the entire \(65{,}536\)-point group \(G\).

## Proof

**1. Affine reduction.** For every ASM each integer row and column sum equals one. Modulo two, \(-1=1\), so its support has odd parity in each row and column. Those eight parity equations have exactly one dependency and define an affine coset \(a+H\) of a \(9\)-dimensional subgroup \(H\) of \(G\). The upper-left \(3\times3\) binary entries determine the other seven entries uniquely: for \(i<4\), \(b_{i4}=1+\sum_{j<4}b_{ij}\pmod2\); similarly \(b_{4j}=1+\sum_{i<4}b_{ij}\pmod2\), and the final entry follows from either last parity equation. Therefore the \(9\)-bit upper-left mask identifies each full support vector. Restriction of ambient characters to \(H\) gives \(512\) reduced characters, each represented by exactly \(2^7=128\) ambient frequencies, with the same multiplier magnitude (possibly different signs).

**2. Exact exhaustive integer certificate.** A valid length-four ASM row is exactly a word over \(\{-1,0,1\}\) whose left-to-right partial sums always lie in \(\{0,1\}\) and end at one. There are precisely eight such words, directly enumerated by the provided checker. The Cartesian fourth power contains \(8^4=4096\) candidate matrices. Retaining exactly those whose column partial sums also lie in \(\{0,1\}\) and end at one exhausts the ASM definition and gives \(42\) distinct supports: \(24\) with no negative entries, \(16\) with one negative entry and \(2\) with two. The attached `support_masks.csv` records each unique full and reduced mask.

Write \(X\subseteq\mathbb F_2^9\) for the \(42\) reduced masks. The integer formula
\[
T(u)=\sum_{x\in X}(-1)^{u\cdot x},\quad u\in\mathbb F_2^9
\]
requires exactly \(512\cdot42\) character signs and is independently reproduced by an in-place integer Walsh-Hadamard recurrence: at every stage replace each adjacent pair \((p,q)\) by \((p+q,p-q)\). The two methods agree on all \(512\) coefficients. Counting their absolute magnitudes gives the table above, and \(\sum_u T(u)^2=512\cdot42=21{,}504\) is an independent Parseval checksum. Multiplication of multiplicities by \(128\) proves the full spectrum, rank, and spectral endpoints. The exact coefficient of the zero character is \(42\), so the maximum is attained.

**3. Sharp endpoint norm.** Put \(S(u)=1\) when \(T(u)\ne0\) and \(0\) otherwise. The reduced Fourier projection kernel is
\[
K(h)=\frac1{512}\sum_{u\in\mathbb F_2^9}S(u)(-1)^{u\cdot h}.
\]
The attached `frequency_spectrum.csv` contains both \(T(u)\) and the integer numerator \(512K(h)\), indexed in each case by all \(512\) masks. Applying the same integer butterfly transform to \(S\) yields exactly the following distribution of numerators: \(-40:1,-32:4,-20:8,-16:10,-8:46,-4:120,0:132,4:120,8:46,16:10,20:8,32:4,40:1,120:1,392:1\). Thus
\[
\sum_{h\in\mathbb F_2^9}|512K(h)|=3184,
\qquad \|K\|_1=\frac{3184}{512}=\frac{199}{32}.
\]
Because the Fourier support on \(G\) is the pullback of the reduced support, the ambient Fourier projection kernel is supported on \(H\) and has exactly these normalized values there. The full-group endpoint convolution norm is therefore also \(199/32\).

For any projection \(P\) onto the convolution range \(R\), average its conjugates by the \(65{,}536\) group translations. Every conjugate maps into \(R\) and fixes \(R\) pointwise; their average is consequently another projection onto \(R\), with no larger \(\ell^1\) or \(\ell^\infty\) norm. It commutes with all translations. Fourier diagonalization forces its multiplier to be one on the Fourier support of \(R\) and zero elsewhere, so this average is precisely the displayed Fourier projection. Finally, the \(\ell^1\) and \(\ell^\infty\) operator norms of convolution by \(K\) equal \(\|K\|_1\) (point-mass and sign-function tests achieve equality). This proves optimality among **all** projections.

## Verification

Run `python3 check_asm4.py` in the directory containing the two CSV certificates. The checker uses only the Python standard library and exact integer arithmetic. It separately (i) enumerates every matrix from its defining row/column partial-sum conditions, (ii) evaluates the \(512\) reduced character sums directly, (iii) computes independent integer butterfly transforms for Fourier coefficients and projection numerators, (iv) checks all tabulated multiplicities and Parseval, and (v) directly evaluates all \(65{,}536\) ambient Fourier coefficients and checks their complete absolute histogram. With `--write`, it reproduces the supplied CSV files. The expected success marker is `ASM4_WALSH_PROJECTION_EXACT_PASS`.

The proof of this **finite exact census** rests on exhaustion of the precisely defined \(4096\) candidates and exact integer operations, not on statistical sampling or numerical tolerance. The attached executable and complete small certificates make the finite evaluation independently reproducible. No higher-order extrapolation is claimed.

## Relationship to prior work

The cardinality \(42\) is classical, already covered by the ASM enumeration theorem; it is not claimed as new. The six-vertex model, ASM symmetries and various refined generating functions have established substantial prior literature. Okada addresses symmetry-class enumeration, while Behrend studies boundary/bulk statistics and row-wise refinements. These results do not state the binary-support all-frequency character census or the resulting sharp projection norm. Translation averaging is an established Fourier-analysis principle, not a new method. The claimed added information is the **evaluated complete Fourier multiplier distribution and exact optimal endpoint projection norm** for the canonical order-four ASM support set. Earlier work with a fully general position-weighted ASM partition function could theoretically subsume an unevaluated signed-sum formula; no identified inspected source supplies the evaluated spectral census or sharp constant.

## Limitations

The result is a finite natural classification for order four only; it is **not** an all-order ASM spectral theorem. The numerical values depend on binary **nonzero-support** encoding; encoding positive entries alone would be a different problem. The certificate relies on the exact finite enumeration supplied, not a closed uniform formula valid in all sizes. Independent human mathematical validation and exhaustive historical-priority confirmation have not been performed. The possibility of a previously published, indexed differently, complete site-weighted evaluation remains a residual priority risk.

## References

1. D. Zeilberger, *Proof of the Alternating Sign Matrix Conjecture*, arXiv:math/9407211 (first public arXiv version 1994-07-02), https://arxiv.org/abs/math/9407211 .
2. S. Okada, *Enumeration of Symmetry Classes of Alternating Sign Matrices and Characters of Classical Groups*, arXiv:math/0408234 (2004-08-18), https://arxiv.org/abs/math/0408234 .
3. R. E. Behrend, *Multiply-refined enumeration of alternating sign matrices*, Advances in Mathematics **245** (2013), 439–499, lawful accepted manuscript https://orca.cardiff.ac.uk/id/eprint/27750/1/MultiplyRefinedEnumerationOfASMs-November2014.pdf .
4. M. Zippin, *A variant of Rudin's inequality for translation invariant projections on group algebras and its generalization to finite dimensional Banach spaces*, Archiv der Mathematik **82** (2004), 61–67, https://doi.org/10.1007/s00013-003-0582-x .
