# First Walsh singularity of alternating-sign-matrix negative-site profiles at order six

## Finding

Let \(\mathcal A_n\) be the set of order-\(n\) alternating-sign matrices (ASMs), with entries in \(\{-1,0,1\}\), all row and column sums equal to one, and nonzero entries alternating in sign. Encode an ASM by the binary indicator of its negative entries in the \((n-2)\times(n-2)\) interior. Let \(F_n\) count the multiplicity of each such indicator and let \(T_n\) be unnormalized XOR convolution by \(F_n\) on \(\mathbb F_2^{(n-2)^2}\); for \(n=1,2\), use the trivial group when the interior is empty.

**The first singular order is exactly six.** For each \(1\le n\le5\), every Walsh multiplier of \(T_n\) is nonzero. At \(n=6\), exactly \(180\) of the \(2^{16}=65{,}536\) multipliers vanish; they form \(24\) orbits under the eight symmetries of the interior square, with \(21\) orbits of size eight and three of size four. Thus
\[
\operatorname{rank}T_6=65{,}356,\quad \operatorname{nullity}T_6=180.
\]
The zero character weights occur only at \(8,9,10,11,12,13\), with respective counts \(4,8,40,96,4,28\). The four lowest-weight vanishing characters are the square-symmetry orbit of the eight-site pattern

```
.##.
###.
###.
....
```

At order six, \(60{,}402\) multipliers are positive and \(4{,}954\) are negative. The smallest nonzero absolute multiplier is \(2\), and the maximum absolute multiplier is \(7{,}436\). Consequently the Moore–Penrose inverse has sharp \(\ell^2\) norm \(1/2\), and the positive-singular-value condition ratio is \(3{,}718\).

For the convolution range \(R=\operatorname{ran}T_6\), the optimal endpoint projection norms **among all projections**, without a translation-invariance assumption, are
\[
\inf_{Q^2=Q,\,\operatorname{ran}Q=R}\|Q\|_{\ell^1\to\ell^1}
=\inf_{Q^2=Q,\,\operatorname{ran}Q=R}\|Q\|_{\ell^\infty\to\ell^\infty}
=\boxed{\frac{94{,}295}{8{,}192}}.
\]

## Assumptions and scope

All matrices are labelled by their row and column positions. For \(n\ge3\), the interior is \(D_n=\{(i,j):2\le i,j\le n-1\}\), and the encoding is \(b(A)_{ij}=\mathbf1\{A_{ij}=-1\}\). Thus \(F_n(x)=\#\{A\in\mathcal A_n:b(A)=x\}\), including multiplicity if distinct matrices have the same negative-site mask. With \(G_n=\mathbb F_2^{D_n}\), unnormalized convolution and Walsh multipliers are
\[
(T_n f)(y)=\sum_{x\in G_n}F_n(x)f(y+x),\qquad
\lambda_n(s)=\sum_{A\in\mathcal A_n}(-1)^{\sum_{(i,j)\in D_n}s_{ij}\mathbf1\{A_{ij}=-1\}}.
\]
Every boundary entry of an ASM is nonnegative, so the encoding loses no negative sites. No theorem for orders exceeding six is asserted. Frequencies are indexed row-major in the interior, with the upper-left interior cell at bit zero. Decimals in the orbit table are binary-mask encodings, not values of mathematical invariants requiring normalization.

## Proof

**1. Exact finite transition recurrence.** After \(i\) rows, let \(S_i\subseteq[n]\) be the columns whose partial column sums are one. At height zero, \(S_0=\varnothing\); after \(n\) rows, \(S_n=[n]\). Row \(i\) is uniquely the coordinate difference \(\mathbf1_{S_i}-\mathbf1_{S_{i-1}}\). Its nonzero coordinates must alternate \(+1,-1,+1,\ldots,+1\), and therefore \(|S_i|=i\). Conversely, any path through these states satisfying the alternation rule determines an ASM, because the column partial sums stay in \(\{0,1\}\), every column finishes at one, and every row has the required alternating signs. There are finitely many such paths, and this is an exact bijection, not an approximation.

For each binary character \(s\), start with \(D_0(\varnothing)=1\) and compute
\[
D_i(V)=\sum_{U\subset[n],\ |U|=i-1\atop U\leadsto V}
D_{i-1}(U)(-1)^{\#\{j:2\le i,j\le n-1,\ U\ni j,\ V\not\ni j,\ s_{ij}=1\}},
\]
where \(U\leadsto V\) means the coordinate differences of the two incidence vectors alternate starting and ending with \(+1\). The resulting exact character sum is \(\lambda_n(s)=D_n([n])\). This recurrence evaluates all frequencies exhaustively using integer additions; it supplies a direct finite proof independent of statistical sampling.

**2. Independent enumeration and transform.** A strictly increasing row of length \(r-1\) in a monotone triangle interlaces the lower row of length \(r\), beginning from bottom row \((1,2,\ldots,n)\). Every choice of such interlacing rows corresponds bijectively to an ASM: successive row membership indicators give its successive matrix rows. The standalone certificate independently generates the complete multiset of negative-site masks by both the transition recurrence and the interlacing-triangle construction. They agree at every mask for all six orders, giving respective total ASM counts \(1,2,7,42,429,7436\).

For each order the verifier constructs the entire frequency vector by the integer Walsh-Hadamard recurrence replacing each pair \((p,q)\) by \((p+q,p-q)\). The exact inverse transform gives \(|G_n|F_n\), and Parseval gives \(\sum_s\lambda_n(s)^2=|G_n|\sum_x F_n(x)^2\). These independent integer identities check the normalization. Complete direct sums against independently generated masks are also checked at every one of the \(24\) order-six orbit representatives. Exact results are zero zeros at orders one through five; at order six the count and signed multiplicities are those in the Finding section.

**3. Exhaustive character-orbit certificate.** The following list gives all \(24\) canonical orbit representatives of zero frequencies, with orbit sizes and weights. Apply the dihedral group of the four-by-four interior square to each listed mask; the resulting disjoint orbits contain all \(180\) zeros and no other frequency.

| Representative decimal mask | Orbit size | Weight |
|---:|---:|---:|
| `1910` | 4 | 8 |
| `5501` | 8 | 9 |
| `7151` | 8 | 11 |
| `7806` | 8 | 10 |
| `7911` | 8 | 10 |
| `8031` | 8 | 11 |
| `8043` | 8 | 10 |
| `8119` | 8 | 11 |
| `11195` | 8 | 10 |
| `11255` | 8 | 11 |
| `14076` | 8 | 10 |
| `15095` | 8 | 11 |
| `15354` | 8 | 11 |
| `15865` | 8 | 11 |
| `16310` | 8 | 11 |
| `23279` | 8 | 11 |
| `23545` | 8 | 11 |
| `24505` | 8 | 11 |
| `24511` | 8 | 13 |
| `32239` | 8 | 13 |
| `32719` | 8 | 13 |
| `37871` | 8 | 11 |
| `40863` | 4 | 12 |
| `48623` | 4 | 13 |


In particular, the minimum possible vanishing weight is eight and the orbit of representative `1910` comprises exactly four characters. All assertions are checked by the standalone enumerator against all \(65{,}536\) frequency values.

**4. Spectral norms and sharp unrestricted endpoint projection.** Walsh diagonalization of XOR convolution makes the rank equal the number of nonzero multipliers. The sharp pseudoinverse \(\ell^2\) norm is the reciprocal of the least positive multiplier magnitude, \(1/2\); the condition ratio is \(7436/2\).

Write \(Z\) for the set of \(180\) zero frequencies and \(H(x)=\sum_{s\in Z}(-1)^{s\cdot x}\). The canonical range projection has Fourier symbol \(\mathbf1_{G_6\setminus Z}\) and convolution kernel
\[
K(x)=\mathbf1_{\{0\}}(x)-2^{-16}H(x).
\]
The exact integer butterfly computation gives \(H(0)=180\) and \(\sum_{x\ne0}|H(x)|=689{,}004\). Therefore
\[
\|K\|_1=\frac{2^{16}-180+689{,}004}{2^{16}}=\frac{94{,}295}{8{,}192}.
\]
A convolution kernel has \(\ell^1\)- and \(\ell^\infty\)-operator norm exactly its absolute coefficient sum. To prove the displayed value is optimal among all projections, average any projection onto \(R\) over conjugation by the \(2^{16}\) translations of \(G_6\). Each conjugate fixes \(R\) pointwise and maps into \(R\), so its average is still a projection onto \(R\), now commuting with translations, and its norm does not exceed the original. Such a projection must be the unique Fourier multiplier equal to one on the nonzero spectrum and zero elsewhere. This proves unrestricted sharpness.

## Verification

The self-contained file `verify_asm_negative_support.py` uses only the Python standard library. Run `python3 verify_asm_negative_support.py` beside this document. It explicitly enumerates all ASMs through size six by two different bijections, compares each profile histogram, checks full Walsh-Hadamard inversion and Parseval at each order, confirms \(180\) zeros, their weight distribution and their \(24\) dihedral orbits, checks direct signed sums at canonical representatives, and verifies the exact endpoint norm by a second integer Fourier transform. It terminates with an explicit PASS marker if all assertions hold. These exhaustive finite certificates prove precisely the finite claims made here, not any asymptotic or higher-order assertion.

## Relationship to prior work

The classical ASM counts, monotone-triangle bijection and the unrefined and bulk-minus-one enumeration are already known and not claimed as discoveries. Lalonde (2004) studies the exactly-one-negative-entry subclass and its reflection bijections, whereas Behrend (2012) evaluates statistics including the **total count** of negative entries and four boundary positions. Neither result states the pointwise sixteen-cell signed Fourier transform, its first zero order, or its range projection constant.

A published finite spectral census for order-four ASMs uses the **binary support of all nonzero entries** in a sixteen-cell ambient cube; that is neither the order-six object nor the negative-entry-only embedding here. Another order-five result concerns linear reconstruction of arbitrary probability measures from up-to-four-cell ternary marginals, rather than XOR convolution by the distribution of negative-site masks. Their conclusions do not imply the signed spectrum or sharp projection constant established here. Translation averaging is a standard argument, credited rather than claimed as new.

## Limitations

The result is a finite complete classification for the first singular ASM size, not a uniform invertibility theorem or a claim about orders seven or larger. The count depends on the fully labelled **negative-site indicator**, not the nonzero-support indicator or the full ternary entry array. The source literature can imply general weighted-ASM partition-function expressions but no inspected work supplies this complete evaluated zero locus and sharp endpoint constant. An unindexed or unpublished equivalent computation is a remaining historical-priority risk. The proof uses an exhaustive, reproducible exact-integer enumeration, not a short conceptual classification of the \(24\) orbit types. Independent external mathematical validation has not been performed.

## References

1. P. Lalonde, *Alternating sign matrices with one \(-1\) under vertical reflection*, arXiv:math/0401339v1, first public 2004-01-25. https://arxiv.org/abs/math/0401339
2. R. E. Behrend, *Multiply-refined enumeration of alternating sign matrices*, arXiv:1203.3187v1, first public 2012-03-14. https://arxiv.org/abs/1203.3187 ; accepted manuscript https://orca.cardiff.ac.uk/id/eprint/27750/1/MultiplyRefinedEnumerationOfASMs-November2014.pdf
3. D. Zeilberger, *Proof of the Alternating Sign Matrix Conjecture*, arXiv:math/9407211. https://arxiv.org/abs/math/9407211
