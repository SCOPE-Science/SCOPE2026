# Complete Walsh singularity and sharp spectral gap for all matchings of \(K_{3,n}\)

## Finding
Let \(n\geq1\) be an integer. In the binary edge-coordinate group \(G_n=\mathbb F_2^{3n}\), let \(\mathcal M_n\) be the incidence vectors of **all** matchings of \(K_{3,n}\), including the empty matching and matchings of sizes one, two, and three. Define the unnormalized Walsh transform
\[
W_n(\omega)=\sum_{M\in\mathcal M_n}(-1)^{\langle\omega,M\rangle}.
\]
Then the complete existence criterion for a vanishing multiplier and the sharp positive spectral gap are
\[
\exists\,\omega\in G_n:\ W_n(\omega)=0
\quad\Longleftrightarrow\quad n\equiv1\pmod2,
\]
\[
\min_{\omega:\,W_n(\omega)\ne0}|W_n(\omega)|
=\begin{cases}1,&n\text{ even},\\2,&n\text{ odd}.\end{cases}
\]
When \(n\) is odd, there are at least \(24^{\lfloor(n-1)/4\rfloor}\) distinct vanishing frequencies. Consequently, unnormalized convolution by \(\mathbf1_{\mathcal M_n}\) is invertible exactly for even \(n\). On the counting-measure Hilbert space \(\ell^2(G_n)\), its inverse (even \(n\)) has norm exactly \(1\), while its Moore--Penrose pseudoinverse (odd \(n\)) has norm exactly \(1/2\).

## Assumptions and scope
All groups, characters, and convolution operators are finite. The bipartition of \(K_{3,n}\) is a distinguished three-vertex row part and an \(n\)-vertex column part. Each edge corresponds to an independent binary coordinate. A frequency \(\omega\) is represented by its \(3\times n\) sign matrix \(z_{ij}=(-1)^{\omega_{ij}}\). No nonnegative-weight hypothesis is imposed: all signs \(\pm1\) occur. The Fourier transform is **unnormalized** as written; convolution is \((Tf)(x)=\sum_{y\in G_n}\mathbf1_{\mathcal M_n}(y)f(x-y)\).

## Proof
**1. Exact signed matching identity.** Put
\[
S_i=\sum_{j=1}^{n}z_{ij},\qquad C_{i\ell}=\sum_{j=1}^{n}z_{ij}z_{\ell j},\qquad T=\sum_{j=1}^{n}z_{1j}z_{2j}z_{3j}.
\]
The empty and one-edge matchings contribute \(1+S_1+S_2+S_3\). The two-edge matchings contribute \(\sum_{i<\ell}(S_iS_\ell-C_{i\ell})\), because the two chosen columns must differ. For three edges, subtract coincidences among the three chosen columns from \(S_1S_2S_3\): the result is \(S_1S_2S_3-S_1C_{23}-S_2C_{13}-S_3C_{12}+2T\). Therefore, for every sign matrix,
\[
\boxed{W_n=(1+S_1)(1+S_2)(1+S_3)
 -(1+S_1)C_{23}-(1+S_2)C_{13}-(1+S_3)C_{12}+2T.}
\tag{1}
\]

**2. The parity obstruction.** The number of all matchings is
\[
|\mathcal M_n|=\sum_{r=0}^{3}\binom3r\binom nr r!
=1+3n+3n(n-1)+n(n-1)(n-2)=n^3+2n+1.
\]
Every sign equals one modulo two, so \(W_n(\omega)\equiv n+1\pmod2\). Thus no Fourier zero occurs for even \(n\), and every nonzero multiplier for odd \(n\) has absolute value at least two.

**3. A four-column zero-preserving block.** Use the four successive sign columns
\[
H_4=((+,+,-),(+,-,-),(-,+,+),(-,-,+)).
\]
Their sums in all three individual rows are zero, as are their pair products except \(C_{13}\), which changes by \(-4\); their triple-product sum is zero. Formula (1) shows that appending \(H_4\) changes the multiplier by precisely \(4(1+S_2)\). In particular, it preserves the multiplier for every starting sign matrix having \(S_2=-1\). The following length-one and length-three matrices all have \(S_2=-1\):

* At length one, \((-, -, +)\) has multiplier zero and \((-,-,-)\) has multiplier \(-2\).
* At length three, \(((+,+,-),(-,-,-),(-,-,-))\) has multiplier zero and \(((+,+,+),(-,-,-),(-,-,-))\) has multiplier \(-2\).

For every odd \(n\), begin with the length-one matrix if \(n\equiv1\pmod4\), or the length-three matrix if \(n\equiv3\pmod4\), and append \(\lfloor(n-1)/4\rfloor\) copies of \(H_4\). This gives, for the same \(n\), one zero multiplier and one multiplier \(-2\). Within each block the four columns are distinct, so independently permuting them gives \(24^{\lfloor(n-1)/4\rfloor}\) distinct zero-frequency matrices.

**4. An eight-column universal identity block and even witnesses.** The eight sign columns in \(H_8=\{\pm1\}^3\), used exactly once each, have zero sum for every nonconstant product of the three sign coordinates. Consequently appending \(H_8\) leaves every one of the seven aggregates \(S_i,C_{i\ell},T\) in (1) unchanged, so the multiplier is unchanged. Direct substitution in (1) gives the following base sign matrices with multiplier \(\pm1\):

* Length two: \(((+,+,+),(-,-,+))\), multiplier \(+1\).
* Length four: \(((+,+,+),(-,+,+),(+,-,-),(+,-,-))\), multiplier \(-1\).
* Length six: four copies of \((+,+,+)\), followed by \((-,-,+),(-,-,-)\), multiplier \(-1\).
* Length eight: one copy of each element of \(\{\pm1\}^3\), multiplier \(+1\).

For every even \(n\), one of these four lengths is congruent to \(n\pmod8\), and appending copies of \(H_8\) gives a multiplier \(\pm1\). Together with Step 2, this proves the sharp positive spectral gap and the full invertibility dichotomy.

**5. Operator consequence.** The characters \(\chi_\omega(x)=(-1)^{\langle\omega,x\rangle}\) form an orthogonal basis of \(\ell^2(G_n)\) and are eigenvectors of convolution by \(\mathbf1_{\mathcal M_n}\), with eigenvalues \(W_n(\omega)\). Therefore this convolution is invertible exactly when every multiplier is nonzero, and its inverse or Moore--Penrose pseudoinverse has Hilbert-space norm the reciprocal of the smallest positive \(|W_n(\omega)|\). This yields the stated operator norms with no normalization factor missing.

## Verification
Run the self-contained Python 3 checker `check.py`. It independently constructs every matching incidence vector, applies the complete integer Walsh--Hadamard transform, and compares each coefficient with formula (1) for all \(1\le n\le6\). The tested numbers of vanishing frequencies for these lengths are respectively \(3,0,72,0,2730,0\). For \(7\le n\le12\), it exhausts all eight-sign column-type multisets (all frequencies up to column permutation), comparing an independent matching dynamic program with formula (1). It also checks the stated block identities and explicit witnesses through \(n=200\). The expected terminal marker is `THREE_ROW_MATCHING_WALSH_EXACT_PASS`. Exhaustive finite verification does not replace the proof for all \(n\).

## Relationship to prior work
The classical unsigned matching or rook generating polynomial, including Heilmann--Lieb theory and Wagner's graph-factor refinements, supplies the structural setting. Wagner's 2004 manuscript and its expanded 2008 version address polynomial zero regions, principally with nonnegative edge weights or sector hypotheses; they do not give the independent \(\pm1\)-edge-sign Walsh zero classification here. Li, Shi, and Trinks (2014) study reconstruction of the ordinary matching polynomial from vertex-deleted subgraphs, not Fourier spectral invertibility. An earlier formula for the **two-edge-only** matching Walsh transform on the same graph is acknowledged: its zeros are not the zeros of the full matching transform, since the degree-zero, degree-one, and degree-three contributions materially change the outcome. Specifically, the two-edge-only Fourier transform has zero-free lengths in two residue classes modulo four; the full matching family has a different parity criterion. The distinct contribution established here is the exact all-size matching zero dichotomy and the sharp positive multiplier gaps for every strip length, using sign-block invariance.

## Limitations
This theorem does not enumerate the exact zero-multiplier multiplicity for arbitrary odd \(n\), nor does it give sharp endpoint \(\ell^1\) inverse norms. The \(24^{\lfloor(n-1)/4\rfloor}\) multiplicity bound is constructive, not necessarily sharp. The self-review has not been independently validated, and an unidentified earlier equivalent signed-rook-polynomial result remains a possible historical-priority risk.

## References
1. D. G. Wagner, *Enumeration of spanning subgraphs with degree constraints*, arXiv:math/0412059v1, publicly submitted 2004-12-02; revised v2 2004-12-15, https://arxiv.org/abs/math/0412059.
2. D. G. Wagner, *Weighted enumeration of spanning subgraphs with degree constraints*, arXiv:0803.1659, publicly submitted 2008-03-11, https://arxiv.org/abs/0803.1659.
3. X. Li, Y. Shi, M. Trinks, *Polynomial reconstruction of the matching polynomial*, arXiv:1404.3469, publicly submitted 2014-04-14, https://arxiv.org/abs/1404.3469.
4. E. W. Weisstein, *Rook Polynomial*, MathWorld, https://mathworld.wolfram.com/RookPolynomial.html (background to unsigned rectangular rook counts).
