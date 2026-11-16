# Complete Walsh spectrum and optimal range projections for the smallest simple periodic square-ice torus

## Finding
Let \(G=C_3\square C_3\), the simple four-regular graph with vertices \((r,c)\in(\mathbb Z/3\mathbb Z)^2\), and orient its eighteen edges initially eastward and southward. Denote by \(\mathcal I\subseteq\mathbb F_2^{18}\) the incidence words encoding all Eulerian (two-in, two-out) edge orientations relative to this reference. For \(u\in\mathbb F_2^{18}\), let
\[
 W(u)=\sum_{x\in\mathcal I}(-1)^{\langle u,x\rangle},\qquad T f=\mathbf1_{\mathcal I}*f.
\]
All sums and convolutions here use counting measure, without Fourier normalization. There are exactly \(148\) orientations, and the **complete signed Walsh spectrum** is:

| \(W(u)\) | Multiplicity |
|---:|---:|
| \(-40\) | 2,304 |
| \(-28\) | 4,608 |
| \(-16\) | 4,608 |
| \(-12\) | 10,752 |
| \(-8\) | 9,984 |
| \(-4\) | 9,216 |
| \(0\) | **162,816** |
| \(4\) | 20,736 |
| \(8\) | 9,984 |
| \(12\) | 13,824 |
| \(16\) | 4,608 |
| \(20\) | 2,304 |
| \(40\) | 2,304 |
| \(44\) | 1,536 |
| \(68\) | 2,304 |
| \(148\) | 256 |

Therefore
\[
 \operatorname{rank}T=99\,328,\quad
 \min_{W(u)\ne0}|W(u)|=4,\quad
 \|(T|_{\operatorname{ran}T})^{-1}\|_{2\to2}=\tfrac14,
 \quad\kappa_2(T|_{\operatorname{ran}T})=37.
\]
Every multiplier is divisible by four, and its Walsh zero set contains the \(131\,072\) odd-weight frequencies plus precisely \(31\,744\) additional even-weight frequencies. For pairs of distinct edge directions, the exact weight-two zero frequencies are the \(45\) pairs consisting of a *disjoint horizontal and vertical edge*; no other weight-two frequency vanishes.

Writing \(R=\operatorname{ran}T\), the sharp projection constants, minimized among **all** real or complex linear projections onto \(R\), are
\[
 \boxed{\Lambda_1(R)=\Lambda_\infty(R)=\frac{445}{64}}.
\]

## Assumptions and scope
All vertex and edge indices and the Fourier normalization are fixed as follows. Write \(v(r,c)=3r+c\) for \(r,c\in\{0,1,2\}\). Edge \(2v(r,c)\) points from \((r,c)\) to \((r,c+1)\), and edge \(2v(r,c)+1\) points from \((r,c)\) to \((r+1,c)\), all coordinates reduced modulo three. An edge bit is one if and only if its initial direction is reversed. Because every degree is four, the Eulerian condition is equivalent to two arrows entering and two leaving every vertex. The ambient Walsh group has \(2^{18}=262\,144\) elements. The grid \(C_3\square C_3\) is the smallest square periodic lattice of this family without parallel edges; the result makes no assertion about other sizes.

## Proof
**1. Exhaustive characterization.** Let \(h_{r,c}\) and \(v_{r,c}\) be the reversal bits on eastward and southward edges. The number of outgoing arrows at a vertex is
\[
 (1-h_{r,c})+h_{r,c-1}+(1-v_{r,c})+v_{r-1,c}.
\]
Consequently the ice rule is exactly the nine simultaneous **integer** equations
\[
 h_{r,c}+v_{r,c}=h_{r,c-1}+v_{r-1,c}.
\]
One independently complete enumeration tests every eighteen-bit word against all nine indegree equalities. A second complete enumeration chooses the nine vertical bits and the first horizontal bit in each of three rows, forces the remaining horizontal bits with these integer equations, then imposes binary admissibility and row closure. These two independently generated sets coincide and have cardinality \(148\). Every finite loop bound and edge convention is explicit in `check_ice3.py`.

**2. Fourier-space reduction and exact certificate.** Summing the ice equations modulo two shows that the reversal word has even incidence degree at every vertex, so \(\mathcal I\) lies in the binary cycle space of \(G\), of dimension \(18-9+1=10\). The orthogonal cut space has dimension eight. Therefore \(W\) is constant on each of the \(2^8=256\) frequencies in a cut-space coset. Removing the eight tree edges indicated in `SPECTRUM.json` gives exactly \(2^{10}=1024\) class representatives. The certificate lists the *integer* character sum at each representative; for each such sum, the checker directly evaluates all \(148\) terms from the independently generated states. It independently computes the full \(2^{18}\)-entry Fourier transform of the indicator by integer butterfly operations, and asserts agreement on every representative and on the signed histogram above. Multiplication of the representative frequencies by their cut-space multiplicities recovers all \(262\,144\) frequencies. The signed multiplicities sum to \(262\,144\), and the separate exact Parseval check reads \(\sum_u W(u)^2=2^{18}\cdot148\).

**3. Consequences.** Walsh characters diagonalize counting convolution, with eigenvalues \(W(u)\), so the number of nonzero coefficients equals \(\operatorname{rank}T\). The exact spectrum supplies the smallest nonzero magnitude four and maximal magnitude \(148\), yielding the asserted inverse norm and condition number. Reversing every arrow preserves Eulerian orientations and sends every edge bit to its complement, so odd-Hamming-weight multipliers vanish. The checker tests the residual even-weight zero count and independently classifies all \(\binom{18}{2}=153\) weight-two frequencies by actual edge endpoints.

**4. Unrestricted endpoint optimality.** The translation-invariant Fourier projection onto \(R\) has convolution kernel
\[
 K(x)=2^{-18}\sum_{u:W(u)\ne0}(-1)^{\langle u,x\rangle}.
\]
Exact integer Fourier inversion of the support indicator yields
\[
 \sum_x\left|\sum_{u:W(u)\ne0}(-1)^{\langle u,x\rangle}\right|=1\,822\,720.
\]
Thus \(\|K\|_{\ell^1}=1\,822\,720/262\,144=445/64\), which is the operator norm on both \(\ell^1\) and \(\ell^\infty\). For any other projection onto \(R\), averaging its conjugates over every group translation cannot increase either endpoint norm and yields a translation-commuting projection. Since the translations diagonalize in the character basis, the only such projection onto \(R\) is the displayed Fourier projection. The value is therefore the **minimum over all projections**, real or complex.

## Verification
Run `python3 check_ice3.py` in the directory containing `SPECTRUM.json`. It uses only the Python standard library. It independently enumerates all \(262\,144\) edge-orientation words and a second transfer-style family of at most \(4096\) candidate configurations; exactly reconstructs the spectrum by both direct sums on \(1024\) cut-class representatives and the full Walsh–Hadamard transform; checks exact Parseval, pair-frequency classifications, and the unnormalized projection-kernel absolute sum. The expected terminal marker is `ICE3_WALSH_EXACT_PASS`. The certificate itself contains all \(1024\) signed class-representative multipliers in a prescribed order, not a sample.

## Relationship to prior work
Periodic square ice and six-vertex partition functions are classical. Tavares–Ribeiro–Korepin treat periodic and mixed boundaries with integrable local vertex weights and free-energy/entropy questions. Jacobsen–Jiang–Zhang derive finite-torus partition functions with homogeneous spectral weights and study their zeros in a complex spectral parameter. The known unsigned square-torus sequence records \(148\) configurations at side three. These results motivate the support but, in the inspected relevant sections, do not evaluate the eighteen independently sign-twisted edge orientation sums or the Fourier projection norm. The present theorem is a complete binary-character specialization at the first simple periodic square lattice, not a claim of a new unsigned ice enumeration.

## Limitations
The complete exact computation is for the single simple torus \(C_3\square C_3\), not an all-size or thermodynamic-limit theorem. The independent enumeration and arithmetic verify precisely this finite domain; the abstract averaging argument gives the unrestricted projection optimality for this computed Fourier range. The origin and complete behavior of additional zeros on larger tori are not determined. Historical priority is assessed from accessible relevant literature and record searches, not certified exhaustively; no independent external mathematical audit has been performed.

## References
1. T. S. Tavares, G. A. P. Ribeiro and V. E. Korepin, *The entropy of the six-vertex model with variety of different boundary conditions*, arXiv:1501.02818 (first posted 2015-01-12). https://arxiv.org/abs/1501.02818
2. J. L. Jacobsen, Y. Jiang and Y. Zhang, *Torus partition function of the six-vertex model from algebraic geometry*, arXiv:1812.00447 (2018); JHEP 2019, 152. https://arxiv.org/abs/1812.00447
3. OEIS A054759, *Number of Eulerian orientations of the \(n\times n\) square lattice with wrap-around*, which includes the unsigned value \(148\). https://oeis.org/A054759
