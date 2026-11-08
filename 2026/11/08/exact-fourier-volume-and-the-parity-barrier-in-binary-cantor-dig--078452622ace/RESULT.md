# Exact Fourier volume and the parity barrier in binary Cantor digit towers

## Finding
Fix an integer base \(b\geq3\), a spatial digit gap \(1\leq d<b\), and a depth \(n\geq1\). At the \(2^n\) distinct points
\[
x_{\boldsymbol\delta}=d\sum_{k=1}^{n}\delta_k b^{-k},\qquad \boldsymbol\delta\in\{0,1\}^{n},
\]
use the \(2^n\) integer frequencies
\[
\lambda_{\boldsymbol\varepsilon}=\sum_{j=0}^{n-1}t_j\varepsilon_{j+1}b^j,\qquad
\boldsymbol\varepsilon\in\{0,1\}^{n},\quad t_j\in\{1,\ldots,b-1\}.
\]
Write \(F_n\) for their square normalized Fourier evaluation matrix,
\[
(F_n)_{\boldsymbol\varepsilon,\boldsymbol\delta}
=2^{-n/2}\exp(2\pi i\lambda_{\boldsymbol\varepsilon}x_{\boldsymbol\delta}).
\]
Then **the determinant, including singular instances, has the exact magnitude**
\[
\boxed{\ |\det F_n|=\prod_{j=0}^{n-1}\left|\sin\left(\frac{\pi d t_j}{b}\right)\right|^{2^{n-1}}.\ }
\]
In particular, the system is a basis of the \(2^n\)-dimensional atomic signal space if and only if \(b\nmid d t_j\) at every level.

Set \(q=b/\gcd(b,d)\) and
\[
s_q=\begin{cases}1,&q\text{ even},\\ \cos(\pi/(2q)),&q\text{ odd}.\end{cases}
\]
Among **all** integer digit-step selections \(t_j\in\{1,\ldots,b-1\}\), the sharp global determinant optimum is
\[
\boxed{\ \max_{\boldsymbol t}|\det F_n|=s_q^{n2^{n-1}}.\ }
\]
Every maximizer chooses independently at each level a residue class satisfying
\[
(d/\gcd(b,d))t_j\equiv q/2\pmod q\quad(q\text{ even})
\]
or
\[
(d/\gcd(b,d))t_j\equiv(q-1)/2\ \text{or}\ (q+1)/2\pmod q\quad(q\text{ odd}).
\]
For \(q\) even, these and only these maximizing choices give a unitary matrix. For \(q\) odd, every such Fourier matrix has exponentially deteriorating squared lower Riesz bound \(A_n\) in the precise sense
\[
\boxed{\ A_n=\sigma_{\min}(F_n)^2\le s_q^n<1,\quad
\operatorname{cond}_2(F_n)\ge s_q^{-n/2}.\ }
\]
The inequalities need not be equalities; the determinant optimum, not the condition-number optimum, is sharp. For the standard middle-third digit system \((b,d)=(3,2)\), the optimal normalized determinant equals \((\sqrt3/2)^{n2^{n-1}}\). When \(b\) is odd and \(d\) is coprime to \(b\), the same formula uses \(s_q=\cos(\pi/(2b))\). The result concerns the entire natural integer digit-tower class, not arbitrary sets of \(2^n\) integer or real frequencies.

## Assumptions and scope
All depths are positive integers and all spatial digits are exactly \(0,d\). The digits define distinct points in \([0,1)\) because \(d<b\). Each frequency digit step is an integer between \(1\) and \(b-1\); different binary frequency words give different integer frequencies by the least-different-digit base-\(b\) argument. The rows and columns may be ordered arbitrarily because only the absolute determinant and singular values are asserted. Counting measure on the finite point set is normalized to mass \(2^{-n}\). The theorem is **not** an assertion about arbitrary Fourier frames for the limiting infinite Cantor measure, nor about all non-digit-product frequency sets at fixed depth.

## Proof
Let \(M_n=2^{n/2}F_n\) denote the unnormalized matrix. At depth \(n\), write a spatial point as \(y+d\delta_n/b^n\), where \(y\) uses the first \(n-1\) digits, and a frequency as \(\lambda'+t_{n-1}\varepsilon_n b^{n-1}\), where \(\lambda'\) uses the first \(n-1\) frequency digits. Since \(b^{n-1}y\) is an integer multiple of \(d\), its exponential at integer frequency step \(t_{n-1}\) is one. With rows grouped by \(\varepsilon_n\) and columns by \(\delta_n\), the matrix therefore takes the block form
\[
M_n=\begin{pmatrix}M_{n-1}&D M_{n-1}\\ M_{n-1}&\omega D M_{n-1}\end{pmatrix},\qquad
\omega=e^{2\pi i d t_{n-1}/b},
\]
where \(D\) is the diagonal unitary matrix indexed by \(\lambda'\), with entries \(e^{2\pi i\lambda' d/b^n}\). This formula also holds for \(n=1\), taking \(M_0=(1)\).

Subtract the first block row from the second. The block determinant, even when \(M_{n-1}\) is singular, gives
\[
|\det M_n|=|\omega-1|^{2^{n-1}}|\det M_{n-1}|^2.
\]
Using \(|\omega-1|=2|\sin(\pi d t_{n-1}/b)|\) and dividing the determinant by \(2^{n2^{n-1}}\), induction yields
\[
|\det F_n|=\prod_{j=0}^{n-1}|\sin(\pi d t_j/b)|^{2^{n-1}}.
\]
There is no assumption of nonsingularity in this induction. The displayed product also proves the criterion \(b\nmid d t_j\) at all levels.

For the optimization, let \(g=\gcd(b,d)\), so \(q=b/g\) and \(d/g\) is invertible modulo \(q\). As \(t\) ranges over \(1,\ldots,b-1\), the residues \((d/g)t\pmod q\) exhaust \(\mathbb Z/q\mathbb Z\). The largest absolute sine on that grid is one exactly when \(q\) is even, attained only at residue \(q/2\). If \(q\) is odd, the two residues nearest \(q/2\), namely \((q\pm1)/2\), give the maximum \(\cos(\pi/(2q))<1\). Each factor is independent, proving the stated sharp optimum and all maximizing digit choices.

Every column of \(F_n\) has Euclidean norm one; hence Hadamard's determinant inequality gives \(|\det F_n|\le1\), with equality if and only if the columns form an orthonormal basis. This proves the unitary assertion when \(q\) is even. Finally let \(m=2^n\) and write the singular values of \(F_n\) as \(\sigma_1,\ldots,\sigma_m\). The smallest squared singular value is at most their squared geometric mean,
\[
\sigma_{\min}(F_n)^2\le\left(\prod_{r=1}^{m}\sigma_r^2\right)^{1/m}
=|\det F_n|^{2/m}\le s_q^n.
\]
Because the sum of their squares is \(\|F_n\|_{\mathrm F}^2=m\), the largest singular value is at least one. The condition-number inequality follows, with the usual convention that the condition number is infinite for singular matrices. This proves every assertion.

## Verification
The standalone `CHECK.py` independently constructs the full complex Fourier matrices from their defining exponentials and computes determinant magnitudes by pivoted complex elimination; it does not call the block recurrence to compute those determinants. Eight different base/gap pairs and depths one through three are tested, including both singular and nonsingular cases. For depths one and two the checker also exhausts all allowed digit-step choices and compares the best determinant with the arithmetic closed form. The checks returned `FINITE_CANTOR_FOURIER_VOLUME_CHECKS_PASSED 88`. The proof establishes all depths and parameters; finite numerical tests are not used as an infinite proof.

## Relationship to prior work
The 2026 odd-base non-Fourier-frame theorems of de Dios Pont--Liehr--Taylor and Fu--Song--Wang motivate seeking quantitative finite-stage obstructions; they prove nonexistence of a frame for the **limiting measure**, whereas this finding gives an exact **normalized determinant and its optimum within a specified finite integer digit-tower family**. Their infinite nonexistence theorems neither state nor numerically determine the finite-stage optimal determinant. The compatible-pair theory of Łaba--Wang treats exact Hadamard (unitary) digit pairs, recovered here as the even-\(q\) endpoint, but does not give this non-Hadamard determinant or parity-optimal exponent. Lai--Wang prove general tower Riesz-bound estimates, not the all-depth exact determinant and complete maximizing-digit congruences. The closely related previously investigated two-character coherence of finite odd-base Cantor measures concerns a \(2\)-by-\(2\) Gram minor optimized over arbitrary frequency pairs, not the determinant of the full \(2^n\)-by-\(2^n\) digit-tower transform.

## Limitations
The sharp claim is a volume/determinant extremum among integer frequency-digit choices only. Other frequency sets, noninteger digits, and redundant frames are not classified or optimized. In particular, the exponential upper bound on the least singular value is not a sharp formula for that singular value. A finite-stage volume collapse alone does not prove that *every possible* frame fails for the infinite Cantor measure. The determinant identity follows from an elementary block factorization; older equivalent formulations in the literature of finite Fourier towers may exist under different terminology. Independent publication-priority review has not been carried out.

## References
1. J. de Dios Pont, L. Liehr, M. A. Taylor, *Cantor measures with odd base do not admit Fourier frames*, first public 2026-07-09, arXiv:2607.08656, https://arxiv.org/abs/2607.08656.
2. X.-Y. Fu, Z.-J. Song, W.-J. Wang, *A Walsh--Quotient Obstruction for Fourier Frames on Odd Reciprocal-Power Bernoulli Convolutions*, first public 2026-07-12, arXiv:2607.10547, https://arxiv.org/abs/2607.10547.
3. I. Łaba, Y. Wang, *On spectral Cantor measures*, preprint 2001, arXiv:math/0109126, https://arxiv.org/abs/math/0109126.
4. C.-K. Lai, Y. Wang, *Non-spectral fractal measures with Fourier frames*, preprint 2015, arXiv:1509.06855, https://arxiv.org/abs/1509.06855.
