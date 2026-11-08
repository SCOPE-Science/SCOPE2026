# Universal finite-time information volume for two sensors on even cycles

## Finding
Let \(M\ge2\), \(N=2M\), and let \(A\) be the ordinary adjacency matrix of the undirected cycle on \(\mathbb Z_N\). Its distinct real eigenvalues are \(a_k=2\cos(\pi k/M)\), \(0\le k\le M\). Let \(\phi\) be any complex-valued function on these \(M+1\) points such that its values \(b_k=\phi(a_k)\) are pairwise distinct. Define \(B=\phi(A)\) by the spectral functional calculus. For \(1\le d<N\), form the square \(N\)-by-\(N\) observation matrix \(O_{M,d}(B)\) whose rows, in time-major order, are
\[
 e_0^{\mathsf T} B^t,\quad e_d^{\mathsf T}B^t,\qquad t=0,\ldots,M-1.
\]
Here \(e_j\) is the standard coordinate vector, and transpose means ordinary linear measurement (no conjugation of the row). Write
\[
 V_{-}=\prod_{0\le i<j\le M-1}(b_j-b_i),\qquad
 V_{+}=\prod_{1\le i<j\le M}(b_j-b_i).
\]
Then the following *exact information-volume law* holds:
\[
 \boxed{|\det O_{M,d}(B)|=
 \begin{cases}
 N^{1-M}|V_{-}V_{+}|,&\gcd(d,N)=1,\\
 0,&\gcd(d,N)>1.
 \end{cases}}
\]
Thus precisely the \(\varphi(N)\) coprime sensor separations provide full-state reconstruction in the **information-theoretically minimal** \(M\) consecutive time samples, and *every one of them has exactly the same information determinant*, for every injective spectral evolution \(\phi\). They are all and only the determinant-optimal separations (with equal unweighted observations). In particular, for \(B=A\),
\[
 \boxed{\det O_{M,d}(A)\in\{-1,1\}\ \text{if}\ \gcd(d,N)=1;\qquad
 \det O_{M,d}(A)=0\ \text{otherwise}.}
\]
Every successful adjacency observation therefore has a **unimodular integer inverse**: integer initial signals can be reconstructed from the integer time observations using integer coefficients.

## Assumptions and scope
The graph is the simple cycle with an even number \(N\ge4\) of vertices, with nearest-neighbor adjacency \((Af)(x)=f(x-1)+f(x+1)\). Two distinct coordinate sensors at \(0,d\) are read simultaneously at the \(M\) integer times starting at zero, and all measurements have unit weight. The source space is the full complex \(N\)-dimensional signal space, not just a low-pass band. Each \(b_k\) must differ from every other; otherwise the determinant vanishes. Real examples include \(\phi(a)=a\) and \(\phi(a)=\exp[-\tau(2-a)]\) for every \(\tau>0\). The optimization is of determinant magnitude, or equivalently \(\det(O^*O)=|\det O|^2\), **not** the lower singular value or spectral condition number.

## Proof
**Fourier spectral decomposition.** Put \(\zeta=e^{2\pi i/N}\). The orthonormal Fourier eigenvector at frequency \(k\) has coordinate \(N^{-1/2}\zeta^{kx}\). Frequencies \(k\) and \(N-k\) share eigenvalue \(a_k\) for \(1\le k\le M-1\); the single frequencies \(0,M\) have distinct eigenvalues \(a_0,a_M\). Let \(v_k=(1,b_k,\ldots,b_k^{M-1})^{\mathsf T}\). After multiplying the observation matrix on the right by the unitary discrete Fourier matrix and grouping rows by sensor, its columns (up to their common factor \(N^{-1/2}\)) are
\[
 \begin{aligned}
  &v_0\otimes(1,1),\qquad v_M\otimes(1,(-1)^d),\\
  &v_k\otimes(1,\zeta^{kd}),\quad
  v_k\otimes(1,\zeta^{-kd})\qquad(1\le k<M).
 \end{aligned}
\]
The tensor notation uses the time-major ordering in the definition; regrouping rows only changes the sign of the determinant. Since the Fourier matrix is unitary, its determinant has modulus one.

**Two Vandermonde factors.** For each repeated-eigenvalue pair, a column subtraction produces a column living only in the second sensor's rows, with scalar multiplier \(\zeta^{-kd}-\zeta^{kd}\); its companion can be made to live only in the first sensor's rows. The \(M-1\) first-sensor columns are then indexed by eigenvalues \(b_1,\ldots,b_{M-1}\); the \(M-1\) second-sensor columns have the same indices. Expanding along the two remaining singleton columns (frequencies \(0\) and \(M\)) leaves exactly two terms: one assigns \(v_0\) to the first-sensor block and \(v_M\) to the second, while the other reverses those assignments. Their scalar difference is \((-1)^d-1\); the two Vandermonde determinants have the same product, namely \(V_{-}V_{+}\), up to a common harmless sign. Consequently the exact determinant magnitude is
\[
 |\det O_{M,d}(B)|=
 N^{-M}\left|(-1)^d-1\right|
 \prod_{k=1}^{M-1}|\zeta^{-kd}-\zeta^{kd}|\,|V_{-}V_{+}|.
\]
Because \(|\zeta^{-kd}-\zeta^{kd}|=2|\sin(\pi kd/M)|\), this becomes
\[
 N^{-M}|(-1)^d-1|\,2^{M-1}
 \prod_{k=1}^{M-1}|\sin(\pi kd/M)|\,|V_{-}V_{+}|.
\]
All Vandermonde factors are nonzero by hypothesis. If \(d\) is even, the singleton factor vanishes. If \(d\) is odd and \(\gcd(d,M)>1\), one sine factor vanishes. Conversely, if \(\gcd(d,N)=1\), \(d\) is odd and multiplication by \(d\) permutes the nonzero residue classes modulo \(M\). The standard sine product gives
\[
 \prod_{k=1}^{M-1}|\sin(\pi kd/M)|=
 \prod_{k=1}^{M-1}\sin(\pi k/M)=\frac{M}{2^{M-1}}.
\]
Substitution yields \(N^{-M}(2)(2^{M-1})(M/2^{M-1})=N^{1-M}\), proving the entire determinant law and its complete equality classification. (The sine product also holds when \(M=2\).)

**Minimal observation horizon.** With fewer than \(M\) time indices, two sensors provide fewer than \(2M\) scalar rows, so injectivity is impossible. The displayed determinant supplies injectivity at exactly \(M\) times if the separation is coprime. Among all separations, every positive determinant magnitude equals the universal product and every other determinant is zero. No stability claim beyond information volume is inferred.

**Unimodularity for adjacency evolution.** At adjacent sensors \(0\) and \(1\), order the observations by time. At time zero they give the coordinates \(0\) and \(1\). At time \(t\), \(1\le t\le M-1\), the walk-count observation at sensor \(0\) first reaches the previously unseen vertex \(-t\), and the observation at sensor \(1\) first reaches the previously unseen vertex \(1+t\). All other vertices contributing to these rows have already appeared at earlier times or earlier in the same pair, and each newly reached vertex has walk-count coefficient exactly one. Reordering the signal coordinates as \(0,1,-1,2,-2,3,\ldots,-(M-1),M\) thus makes the integer observation matrix triangular with every diagonal entry \(1\). Hence \(|\det O_{M,1}(A)|=1\). The universal determinant law transfers its absolute determinant to every coprime separation. Such a matrix is integer with determinant \(\pm1\), so its inverse is integer by the adjugate formula. This proves the final assertion.

## Verification
The dependency-free standalone `CHECK.py` uses fraction-free exact integer determinants, not floating-point singular values. It constructs every row from adjacency walk counts and checks \(|\det|=1\) exactly for the coprime offsets for all even cycle orders from four through eighteen, checking zero otherwise. It also checks the exact affine spectral-evolution law for \(B=\alpha A+\beta I\) with \((\alpha,\beta)=(1,5),(2,3),(-1,1)\), for all even cycle orders four through twelve and all offsets: the expected determinant magnitudes are \(|\alpha|^{M(M-1)}\) for coprime offsets and zero otherwise. The checker reports `CHECK_OK exact_determinants=185 even_cycles=4..18`. These finite tests support, but do not replace, the algebraic argument valid for every \(M\) and every injective spectral filter.

## Relationship to prior work
Parlangeli and Notarstefano's 2011 classification of observability for cycle graphs **already contains the coprime sensor-offset criterion**. That criterion is acknowledged as *known*: it is not the novelty claimed here. The added result is the **universal exact minimal-horizon information determinant** valid for every injective spectral evolution, its complete placement equality classification, and the unexpectedly exact unimodular volume for unnormalized adjacency evolution.

Bulai, Cabrelli, Cordero, Molter, and Saliani (September 2026) develop graph Paley–Wiener dynamical sampling, treating finite paths as a numerical model. Their accessible abstract does not assert this even-cycle determinant identity, but the complete manuscript could not be inspected and remains an overlap risk. Related published work on spectrally demixed two-sensor frames on cycles obtains sharp *demixed low-pass condition numbers*, which are different measurements and objective from the raw square time-trajectory determinant here. A related determinant theorem for *one sensor on normalized paths* concerns a different graph and sampling geometry. The classical Fourier diagonalization, Vandermonde determinant, sine product, and elementary walk counts are acknowledged proof ingredients, not presented as novel.

## Limitations
Only even simple cycles, exactly two point sensors and simultaneous consecutive times are treated. The determinant-optimality is for the unweighted square information volume and does not imply equality of noise-conditioned lower singular values or reconstruction condition numbers among different sensor spacings. A spectral function that merges distinct adjacency eigenvalues falls outside the theorem. Earlier equivalent formulas may exist in control or signal-processing literature, and the 2026 motivating article's full text was not accessible in this comparison. No independent audit is claimed.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley--Wiener Spaces*, arXiv:2609.25472v1, first publicly submitted 21 September 2026. https://arxiv.org/abs/2609.25472.
2. G. Parlangeli and G. Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs*, arXiv:1109.3556v1, first submitted 16 September 2011; IEEE Transactions on Automatic Control 57 (2012), 743–748. https://arxiv.org/abs/1109.3556.
3. *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, published mathematical research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-spectral-demixed-two-sensor-frame-bounds-on-finite-cycles--b03d8e4c7818/ .
4. *Universal endpoint optimality for dynamical sampling on normalized paths*, published mathematical research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f/ .
