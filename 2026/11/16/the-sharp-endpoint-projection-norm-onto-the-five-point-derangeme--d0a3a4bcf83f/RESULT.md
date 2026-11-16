# The sharp endpoint projection norm onto the five-point derangement convolution range

## Finding
Let \(G=M_5(\mathbb F_2)\), with its additive structure and binary trace pairing \(\langle A,B\rangle=\sum_{i,j=0}^4A_{ij}B_{ij}\pmod2\). Let \(\mathcal D\subset G\) be the 44 permutation matrices with no diagonal ones, and let \(C h=\mathbf1_{\mathcal D}*h\) be unnormalized counting convolution. The **new exact norm** of a smallest-norm linear projection onto \(\operatorname{ran}C\), allowing every (not necessarily translation-invariant) linear projection, is
\[
\boxed{
\inf_{Q^2=Q,\ \operatorname{ran}Q=\operatorname{ran}C}
\|Q\|_{\ell^1(G)\to\ell^1(G)}
=\inf_{Q^2=Q,\ \operatorname{ran}Q=\operatorname{ran}C}
\|Q\|_{\ell^\infty(G)\to\ell^\infty(G)}
=\frac{6999}{512}.}
\]
The canonical Fourier projection attains both infima. It is the projection onto precisely the \(28{,}016{,}640\) Fourier modes where the signed derangement permanent is nonzero. These rank and signed-permanent support counts were known in an earlier exact spectrum census; the contribution here is the **sharp norm of the projector onto that support**, not a rediscovery of the signed-permanent histogram or the smaller norm of projection onto the original 44 derangement characters.

## Assumptions and scope
The Walsh transform is unnormalized: \(\widehat f(A)=\sum_{B\in G}f(B)(-1)^{\langle A,B\rangle}\). For \(A\in G\), \(\widehat{\mathbf1_{\mathcal D}}(A)\) is the ordinary integer permanent of the matrix having zero diagonal and off-diagonal entries \((-1)^{A_{ij}}\). The Fourier spectral projector is the unique convolution projection whose multiplier is the indicator of the **nonzero set** of this permanent. Its range is \(\operatorname{ran}C\). Both Banach-space norms use counting measure, for which the convolution norm equals the sum of absolute kernel values. The claim concerns only order five and does not assert an all-dimensional closed formula.

## Proof
**1. Gauge quotient and frequency support.** The 20 off-diagonal cells of a \(5\times5\) matrix form the edge set of the connected bipartite crown graph on five row and five column vertices. Take the nine-edge spanning tree
\[
T=\{(0,j):1\le j\le4\}\cup\{(i,0):1\le i\le4\}\cup\{(1,2)\}.
\]
Sign changes in individual rows and columns of the off-diagonal sign matrix multiply the signed derangement permanent by a global sign and do not change whether it vanishes. Every signing is uniquely gauge normalized to \(+1\) on the nine tree edges, leaving eleven independent chord signs. The five diagonal frequency bits are irrelevant. Hence the signed permanent's zero/nonzero indicator factors through a linear \(11\)-dimensional quotient \(\pi:G\to\mathbb F_2^{11}\), each fiber containing \(2^{14}\) frequency matrices. Let \(E\subset\mathbb F_2^{11}\) be the set of normalized chord masks at which the permanent is nonzero. Its known size \(|E|=1710\) is also independently verified by the packaged code, which evaluates each of the 2048 signed permanents via two distinct integer formulas.

**2. Exact Fourier transform of the spectral support.** On each chord mask \(s\), the signed permanent is
\[
F(s)=\sum_{\pi\text{ derangement of }\{0,1,2,3,4\}}
(-1)^{\langle s,p_\pi\rangle},
\]
where \(p_\pi\) records the chords used by \(\pi\). The checker evaluates all 2048 integer \(F(s)\) using both the 44-term sum and Ryser's subset formula for a matrix with zero diagonal, then constructs \(\mathbf1_E(s)=\mathbf1_{F(s)\ne0}\). It computes the full Walsh transform
\[
H(u)=\sum_{s\in\mathbb F_2^{11}}\mathbf1_E(s)(-1)^{\langle u,s\rangle}
\]
using both butterfly recursion and independent direct character summation at **every** of the 2048 dual frequencies. The certified complete absolute-value distribution is
\[
\begin{array}{c|rrrrrrrrr}
 |H(u)|&6&10&14&18&22&26&46&338&1710\\\hline
 \#u&960&360&44&70&360&240&12&1&1
\end{array}.
\]
The counts sum to 2048, the zero-mode value is 1710, and \(\sum_u|H(u)|=27996\). These are complete finite exact-integer identities, not numerical approximations or extrapolations.

**3. Projection kernel and global optimality.** Let \(P\) be the multiplier projection \(\widehat{Ph}(A)=\mathbf1_{\operatorname{ran}\widehat C}(A)\widehat h(A)\). Since its multiplier is constant on all fibers of \(\pi\), its kernel is zero away from the annihilator of \(\ker\pi\). On that annihilator the kernel values are exactly \(H(u)/2048\), indexed by \(u\in\mathbb F_2^{11}\). Hence
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}
=\frac1{2048}\sum_u|H(u)|
=\frac{27996}{2048}=\frac{6999}{512}.
\]
To prove that this is the **minimum among all linear projections**, let \(Q\) be any projection onto \(\operatorname{ran}C\). Average the translation conjugates \(U_t Q U_t^{-1}\) over all \(t\in G\). The result has range in \(\operatorname{ran}C\), acts identically on that range, commutes with every translation, and has operator norm at most \(\|Q\|\) in both endpoint spaces. Every translation-invariant projection onto \(\operatorname{ran}C\) is \(P\), because its Walsh multiplier is forced to equal one on the nonzero-multiplier frequencies and zero elsewhere. Thus \(\|Q\|\ge\|P\|\). Convolution attains its \(\ell^1\) norm on a delta function and its \(\ell^\infty\) norm on a sign-aligned function, completing the exact proof.

## Verification
Run `python3 check_derangement_walsh.py`, with Python 3 standard library only. It independently compares 2048 signed permanents via derangement enumeration and Ryser inclusion--exclusion, recovers the previously known multiplier histogram and nonzero count, checks two Parseval identities, independently computes all 2048 dual support-transform coefficients via both Walsh recursion and direct summation, checks the **new** full absolute kernel histogram, and verifies the exact sum \(27996\). Success marker: `DERANGEMENT5_WALSH_PROJECTOR_PASS`. The CSV files contain both the supporting old signed-permanent histogram and the new projection-kernel histogram, clearly distinguished by their filenames. The code and exact finite identities are the exhaustive certificate.

## Relationship to prior work
A previous five-point derangement-matrix Walsh census already determined all signed-permanent absolute values, their multiplicities, rank \(28{,}016{,}640\), and the norm \(1269/256\) of the **different** Fourier projection onto the 44 original derangement characters. None of those facts gives the \(\ell^1\) norm of the Fourier indicator of the **1710-class nonzero signed-permanent support**. The new result requires the further complete transform \(H\), and \(6999/512\ne1269/256\). A separate published all-permutation order-five calculation concerns 120 permutation characters, not the nonzero support of derangement convolution. Renteln studies the derangement Cayley graph on the nonabelian symmetric group, a different operator. Wanless studies general signed permanents and their extrema; Tao--Vu prove asymptotic random-permanent estimates. The averaging lemma is classical and is used, not claimed as novel. Historical priority is judged by a bounded comparison of actual mathematical implications, not only by matching titles.

## Limitations
The exact evaluated projector norm concerns \(5\times5\) derangement incidence matrices and counting-measure endpoint norms only. No formula for other orders or intermediate \(\ell^p\) projection constants follows. The decisive finite transform histogram is certified by exhaustive exact integer computation rather than by a compact symbolic closed form. An unidentified earlier table of the signed-derangement *nonzero-support indicator transform* might cover the result; independent mathematical validation has not been performed.

## References
1. P. Renteln, *On the Spectrum of the Derangement Graph*, Electronic Journal of Combinatorics **14** (2007), R82, published 2007-11-28, DOI `10.37236/1000`.
2. I. M. Wanless, *Permanents of matrices of signed ones*, Linear and Multilinear Algebra **53** (2005), 427--433, DOI `10.1080/03081080500093990`; lawful author full text `https://users.monash.edu.au/~iwanless/papers/wangconjLAMA.pdf`.
3. T. Tao and V. Vu, *On the permanent of random Bernoulli matrices*, arXiv:0804.2362, initial preprint 2008-04-15.
4. *Exact order-five binary permutation Fourier spectrum and endpoint norm*, public online result, `https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-order-five-binary-permutation-fourier-spectrum-and-endpoin--69d359ed8a05/RESULT.md`.
