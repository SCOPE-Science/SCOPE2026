# The Fano-matroid base support is a cubic bent difference set

## Finding

Let \(E=\mathbb F_2^3\setminus\{0\}\) be the seven points of the Fano plane and let \(\mathcal B\) be the 28 three-element subsets of \(E\) that are not Fano lines. Interpret the characteristic vectors \(\mathbf1_B\) of these matroid bases as points of the odd-parity affine hyperplane \(H\subset\mathbb F_2^7\). Identify \(H\) with \(\mathbb F_2^6\) by taking the first six coordinates \(x_1,\ldots,x_6\) and setting \(x_7=1+\sum_{i=1}^6x_i\), with arithmetic in \(\mathbb F_2\). Write \(D\subset\mathbb F_2^6\) for the resulting 28-point set and \(b=\mathbf1_D\).

**Theorem.** With the unnormalized Walsh convention \(\widehat b(w)=\sum_{x\in\mathbb F_2^6}b(x)(-1)^{w\cdot x}\), the spectrum consists of
\[
\widehat b(0)=28,\qquad
\#\{w:\widehat b(w)=4\}=28,\qquad
\#\{w:\widehat b(w)=-4\}=35.
\]
The support \(D\) is a \((64,28,12)\) difference set: for every nonzero \(h\in\mathbb F_2^6\),
\[
|D\cap(D+h)|=12.
\]
Consequently the Boolean function \(b\) is bent, in the usual sign convention \(s(x)=(-1)^{b(x)}\): every Walsh coefficient of \(s\) has absolute value \(8\). Its algebraic normal form has degree exactly **three**, with 12 quadratic and 16 cubic monomials and no others. Convolution by \(b\) on the 64-point group is invertible; its singular values are \(28\) once and \(4\) 63 times, giving condition number \(7\).

## Assumptions and scope

Choose the labels \(1,\ldots,7\) for the seven nonzero three-bit vectors, with the label understood as its binary integer. The seven Fano lines are precisely the sets \(\{a,c,a\oplus c\}\) for distinct nonzero labels \(a,c\). Thus the 28 bases are the three-subsets not equal to any of these seven lines. The symbol \(\oplus\) is bitwise addition of labels in \(\mathbb F_2^3\). The six-bit chart eliminates coordinate seven of the odd-weight hyperplane; it is an affine chart, not a group homomorphism from the odd coset itself. Fourier and difference-set statements are taken after this fixed affine identification. Changing the chart only applies an affine automorphism and does not change spectral magnitudes or the bent property.

The ambient object has exactly \(64\) points, so the theorem is an exhaustive finite exact statement, not an assertion about arbitrary higher-rank matroids or all Steiner triple systems. The term *bent* refers to equal absolute Walsh magnitudes for the \(\{+1,-1\}\)-valued sign of \(b\), not to a claim of a new extended-affine class of bent functions.

## Proof

**1. Seven-bit signed character sums.** For each \(S\subseteq E\), put \(s=|S|\) and
\[
W(S)=\sum_{B\in\mathcal B}(-1)^{|B\cap S|}.
\]
Summing first over all 35 three-subsets and subtracting the seven Fano lines gives
\[
W(S)=K_3(s)-L(S),\quad
K_3(s)=\sum_{j=0}^3(-1)^j\binom{s}{j}\binom{7-s}{3-j},\quad
L(S)=\sum_{\ell\text{ a line}}(-1)^{|S\cap\ell|}.
\]
The Fano incidence axioms (every point on three lines and every pair on exactly one) give the following exact table. The categories \(\text{line}\) and \(\text{nonline}\) refer to a three-subset; for four-subsets they refer to the complement.

| \(s\) | Category | \(K_3(s)\) | \(L(S)\) | \(W(S)\) | Count |
|---:|---|---:|---:|---:|---:|
| 0 | only | 35 | 7 | 28 | 1 |
| 1 | only | 5 | 1 | 4 | 7 |
| 2 | only | −5 | −1 | −4 | 21 |
| 3 | line | −3 | −7 | 4 | 7 |
| 3 | nonline | −3 | 1 | −4 | 28 |
| 4 | complement of line | 3 | 7 | −4 | 7 |
| 4 | complement of nonline | 3 | −1 | 4 | 28 |
| 5 | only | 5 | 1 | 4 | 21 |
| 6 | only | −5 | −1 | −4 | 7 |
| 7 | only | −35 | −7 | −28 | 1 |

The table follows directly by enumerating intersections against the seven lines; the checker independently validates every one of the 128 subsets. The Fano automorphism group is transitive on each indicated category.

**2. Restricting to the affine hyperplane.** In the chosen chart, the seven-coordinate character indexed by \(S\subseteq\{1,\ldots,6\}\) restricts to the six-coordinate Walsh character indexed by the same \(S\). From the table, its trivial coefficient is \(28\), and all \(63\) others have magnitude \(4\). Their positive and negative counts are obtained by summing the table over subsets not containing coordinate seven (or equivalently using \(b(0)=0\), which implies \(\sum_w\widehat b(w)=0\)). Thus \(28+4p-4q=0\) and \(p+q=63\), giving \(p=28\), \(q=35\).

**3. Difference-set and bent equivalence.** For \(h\ne0\), Fourier inversion of the squared magnitudes gives
\[
\sum_x b(x)b(x+h)
=\frac1{64}\left(28^2+16\sum_{w\ne0}(-1)^{w\cdot h}\right)
=\frac{784-16}{64}=12.
\]
The sign transform equals \(\widehat s(w)=64\mathbf1_{\{0\}}(w)-2\widehat b(w)\), so it has magnitude \(8\) everywhere. These are precisely the Hadamard difference-set and Boolean bent conditions; the derivative of \(b\) in each nonzero direction has 32 ones. The Fourier convolution operator is diagonal under the unnormalized character basis, and its singular values are the absolute multipliers stated in the theorem.

**4. Exact cubic algebraic degree.** The algebraic normal form is the unique multilinear polynomial over \(\mathbb F_2\), with coefficient of a squarefree monomial indexed by \(S\) equal to \(\sum_{T\subseteq S}b(\mathbf1_T)\pmod2\). The 64-entry exact subset-Möbius inversion in `verify_fano.py` yields exactly 12 nonzero degree-two coefficients, 16 degree-three coefficients and none of other degrees. In particular the coefficient indexed by \(\{1,2,3\}\) equals one: these three points form a line, so \(b(\{1,2,3\})=0\), whereas each of the three two-subsets extends with point seven to a noncollinear base. Thus the cubic degree is attained. This finite identity is verified exhaustively for all 64 monomials, not inferred from sample evaluations.

## Verification

The standalone standard-library Python program `verify_fano.py` rebuilds the seven lines from bitwise sums and validates the seven-point pair-design axiom. It then checks the 28 bases and independently computes all 128 seven-bit character sums, including the Krawtchouk-minus-line formula and the ten rows of the frequency table. In the parity chart it performs both a six-stage integer Walsh–Hadamard transform and a second direct 64-character summation, checks all 63 nontrivial autocorrelations and derivatives, verifies bent flatness, and performs complete binary subset-Möbius inversion. It prints `CHECK_OK` only when all assertions pass.

Reproduce with `python3 verify_fano.py`; Python 3.8 or later suffices. Finite exhaustivity is appropriate here because the claim concerns this fixed 64-element group. No numerical floating-point rounding, external package, unprovided table, or independent certification is used.

## Relationship to prior work

The 28 noncollinear triples are the classical bases of the Fano matroid. De Loera, Lee, Margulies and Miller enumerate the dependent triples in Section 4 of their matroid-orientability paper, and count the bases implicitly, but do not analyze their signed Boolean Fourier spectrum. Kantor discusses bent functions and associated difference-set constructions in broad generality; the inspected full text does not identify these particular Fano bases as a cubic bent support. Published analyses of Steiner-design base polytopes determine geometric asymmetry, not the indicator's full Walsh transform. A published Fano-plane compatibility theorem concerns orthogonal Walsh spectra of two eight-point affine simplices, rather than the 28-point Fano base support. The Fano-plane triangle–antiflag correspondence and its 28-bitangent analogy explain the combinatorial count but do not alone establish the affine six-bit signed spectrum or the cubic algebraic degree in this chart.

## Limitations

The construction produces one specific 6-variable cubic bent function (and its affine variants); it does **not** establish a new equivalence class, a general theorem for all matroids, or a property of arbitrary seven-point configurations. The finite proof assumes the standard Fano incidence rules, and the coefficient table can equally be verified by the supplied exhaustive exact checker. Historic priority cannot be guaranteed: an older specialized account of Fano triangles, odd theta characteristics, or a Hadamard difference-set realization might imply the same result under another encoding. Independent mathematical and priority review has not been performed.

## References

1. W. M. Kantor, *Bent functions generalizing Dillon's partial spread functions*, arXiv:1211.2600, first posted 12 November 2012. https://arxiv.org/abs/1211.2600
2. J. A. De Loera, J. Lee, S. Margulies and J. Miller, *Weak Orientability of Matroids and Polynomial Equations*, arXiv:1309.7719, first posted 30 September 2013, especially Section 4. https://arxiv.org/abs/1309.7719
3. *Steiner design base polytopes have hypersimplex asymmetry except for the Fano plane*, published mathematical finding (2026). https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-steiner-design-base-polytopes-have-hypersimplex-asymmetry-except--3dc4fabc4271/RESULT.md
4. *A Fano-plane compatibility law for simultaneous eight-point Walsh spectra*, published mathematical finding (2026). https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-fano-plane-compatibility-law-for-simultaneous-eight-point-wals--a2101219c95b/RESULT.md
