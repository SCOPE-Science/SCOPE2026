# Sharp balanced mixed time–Fourier sampling on the seven-cycle

## Finding
Let \(F\) be the unitary \(7\times7\) discrete Fourier matrix with entries \(F_{k,j}=7^{-1/2}e^{2\pi i kj/7}\). Choose any three distinct time indices \(T\subset\mathbb Z_7\) and any four distinct measured Fourier indices \(K\subset\mathbb Z_7\). The seven-measurement analysis operator is
\[
 A_{T,K}x=\big((x_t)_{t\in T},((Fx)_k)_{k\in K}\big).
\]
There are exactly \(\binom73\binom74=1225\) labelled designs; every one is invertible. Write \(C=\mathbb Z_7\setminus K\) for the three *unmeasured* frequencies and put \(u=2\cos(2\pi/7)\). Let \(h_*\) be the smallest real root of
\[
 h^3-\frac97h^2+\frac{22+3u}{49}h-\frac{14+7u}{343}=0,
 \qquad h_*=0.245386644265346\ldots.
\]
Then the **sharp least squared singular value**, maximized over all labelled designs, and the **sharp minimum spectral condition number** are
\[
 \max_{T,K}\sigma_{\min}(A_{T,K})^2=1-\sqrt{1-h_*}
 =0.131315157416308\ldots,
 \quad
 \min_{T,K}\kappa_2(A_{T,K})=
 \sqrt{\frac{1+\sqrt{1-h_*}}{1-\sqrt{1-h_*}}}
 =3.772338032362\ldots.
\]
Exactly **147** of the 1225 designs attain either optimum. They are precisely those for which
\[
 T=\{t_0-h,t_0,t_0+h\},\qquad
 C=\{c_0-k,c_0,c_0+k\},\qquad
 h,k\in\mathbb Z_7^\times,\quad hk\equiv\pm2\pmod7.
\]
Every nonoptimal design satisfies the strict gap \(\lambda_{\min}(F_{C,T}^*F_{C,T})<1/5<h_*\). The entire seven-value squared singular spectrum for each design is \(\{1\}\cup\{1\pm\sqrt{1-\lambda_j(F_{C,T}^*F_{C,T})}:j=1,2,3\}\), multiplicities included.

## Assumptions and scope
All indices are elements of \(\mathbb Z_7\) and all six or seven measured quantities are complex with their exact amplitudes and phases, not intensities. Each time sample and each normalized Fourier sample has equal measurement weight and equal noise scale. Exactly three time samples and four Fourier samples are used, with no repeated indices. The result is finite-dimensional and does not claim optimal designs at any other cyclic order or under weighted, constrained, or phaseless measurements.

## Proof
**1. Reduction to three principal angles.** Let \(P\) project onto the coordinate subspace supported on \(T\), and \(Q=F^*P_KF\). Then \(A_{T,K}^*A_{T,K}=P+Q\), with ranks \(3\) and \(4\). Set \(H=F_{C,T}^*F_{C,T}\), so on the range of \(P\) the compression of \(Q\) is \(I_3-H\). Since \(F\) is unitary, the eigenvalues \(h_1,h_2,h_3\) of \(H\) lie in \([0,1]\). The canonical two-projection decomposition has three two-dimensional summands with eigenvalues \(1\pm\sqrt{1-h_j}\) for \(P+Q\), and an additional eigenvalue \(1\). (The formula extends by continuity to endpoint principal angles.) Thus maximizing the least singular value, or minimizing the full spectral condition number, is equivalent to maximizing \(h_{\min}=\lambda_{\min}(H)\).

**2. Exact symmetry quotient.** Put \(\zeta=e^{2\pi i/7}\), \(B_{c,t}=\zeta^{ct}\) for \(c\in C,t\in T\), and \(G=B^*B=7H\). The transformation
\[
 (T,C)\longmapsto(aT+b,a^{-1}C+d),\quad
 a\in\mathbb Z_7^\times,\ b,d\in\mathbb Z_7,
\]
changes \(B\) only by row/column permutations and unit phases, hence leaves \(G\)'s eigenvalues unchanged. Directly forming the image sets for all \(6\cdot7\cdot7=294\) transformations partitions the complete 1225-pair space into the following seven orbits. The right column is the **exact**, not floating-point, determinant \(\det(5G-7I_3)\); here \(u^3+u^2-2u-1=0\).

| Representative \(T\) | Representative \(C\) | Orbit size | \(\det(5G-7I_3)\) |
|---|---|---:|---|
| \(\{0,1,2\}\) | \(\{0,1,2\}\) | 147 | \(112-350u-350u^2\) |
| \(\{0,1,2\}\) | \(\{0,1,3\}\) | 294 | \(-938\) |
| \(\{0,1,2\}\) | \(\{0,1,4\}\) | 147 | \(-938+350u^2\) |
| \(\{0,1,2\}\) | \(\{0,2,4\}\) | 147 | \(-238+350u\) |
| \(\{0,1,3\}\) | \(\{0,1,2\}\) | 294 | \(-938\) |
| \(\{0,1,3\}\) | \(\{0,1,3\}\) | 98 | \(-63\) |
| \(\{0,1,3\}\) | \(\{0,1,5\}\) | 98 | \(-63\) |

The embedded `check.py` constructs all 1225 pairs, exhaustively generates each listed orbit, proves the orbits are disjoint and exhaustive, and computes these seven determinants in exact integer arithmetic in \(\mathbb Z[\zeta_7]\). The script's ring representation and all executable operations are included, so no black-box symbolic algebra or numerical tolerance enters this finite certificate.

**3. An exact strict separating threshold.** Elementary trigonometric ordering and the minimal polynomial imply \(6/5<u<5/4\). Hence all determinants in the table except that of \((T,C)=(\{0,1,2\},\{0,2,4\})\) are strictly negative. Since \(\det(5G-7I_3)=5^3\prod_{j=1}^3(7h_j-7/5)\), each losing orbit has at least one \(h_j<1/5\). For the winning representative, the three leading principal minors of \(5G-7I_3\) are
\[
 8,\qquad 64+25u-25u^2,\qquad -238+350u,
\]
all strictly positive throughout \((6/5,5/4)\). Sylvester's criterion therefore gives \(G\succ(7/5)I_3\), or \(h_{\min}>1/5\). This proves the unique winning orbit with an exact algebraic gap, not an inference from rounded eigenvalues.

**4. Exact spectral value and optimizer geometry.** For the winning representative, exact cyclotomic arithmetic gives \(\operatorname{tr}G=9\), second characteristic coefficient \(22+3u\), and \(\det G=14+7u\). Dividing the characteristic polynomial by \(7^3\) gives the displayed cubic for \(h_j\), and the least root is \(h_*\). The winning orbit consists exactly of two three-term cyclic arithmetic progressions with steps whose product is \(\pm2\). Each such triple has a unique center, and direct enumeration of the nonzero steps yields 147 distinct pairs. The checker also verifies this equivalence exhaustively. The same principal-angle formula then supplies both sharp constants and the full singular spectrum. All seven orbits have \(\det G>0\); as \(G\) is a Gram matrix, every \(H\) is positive definite, so every original seven-measurement operator is invertible.

## Verification
The finite exact certificate is executable with `python3 check.py` (Python standard library only). It checks the complete 1225-pair space, every orbit and orbit cardinality, each orbit's determinant polynomial, the exact winner characteristic invariants and principal minors, and rational-interval sign inequalities. Its expected final line is `PASS: 1,225 configurations; 7 affine orbits; 147 exact optimizers`. The decimal numbers are supplementary approximations, not proof inputs.

## Relationship to prior work
Kayaalp and Szehr (2026) provide the direct two-sided measurement setting and finite-dimensional identifiability/stability framework, with numerical design comparisons; the exact seven-cycle joint design and complete optimizer census are not among their inspected statements. Perlstadt (1981) studies time-sample choices when some Fourier coefficients are already available and develops condition-number/determinant comparisons for an associated Fourier minor; those techniques are closely related, but the inspected paper does not give the present sharp **equal-noise stacked-operator** seven-cycle constant, strict orbit gap, or 147-design classification. Distinguishing the stacked operator's singular norm from the Fourier minor's own condition number is essential. General prime-order Fourier full-spark results establish invertibility, not this optimizer. Other nearby finite Fourier sampling results use different row/frequency budgets or optimize determinant instead of the smallest singular value.

## Limitations
This is a complete seven-dimensional result, not an assertion for larger primes or other sample ratios. The E-optimal objective and equal complex-measurement noise model are essential. The discrete orbit computation is exhaustive but must not be mistaken for an infinite-dimensional theorem. Published equivalences outside the inspected sources, including an older finite-design table or thesis, are a remaining bibliographic possibility. The result has not undergone independent mathematical audit.

## References
1. M. Kayaalp and O. Szehr, *Signal Recovery from Time and Frequency Samples*, arXiv:2603.16242, initial preprint 2026-03-17, https://arxiv.org/abs/2603.16242 .
2. M. Perlstadt, *Sampling Schemes for Fourier Transform Reconstruction*, SIAM J. Algebraic Discrete Methods 2 (1981), 176–191, https://doi.org/10.1137/0602022 .
3. T. Tao, *An uncertainty principle for cyclic groups of prime order*, Math. Res. Lett. 12 (2005), 121–127, https://arxiv.org/abs/math/0308286 .
