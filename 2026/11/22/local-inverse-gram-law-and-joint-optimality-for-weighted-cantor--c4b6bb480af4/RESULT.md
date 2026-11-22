# Local inverse-Gram law and joint optimality for weighted Cantor Fourier towers

## Finding
Fix an integer base \(b\ge3\), digit gap \(1\le d<b\), depth \(n\ge1\), frequency-digit steps \(t_j\in\{1,\ldots,b-1\}\) for \(0\le j<n\), and Bernoulli probabilities \(0<p_k<1\) for \(1\le k\le n\). Let \(\boldsymbol\delta,\boldsymbol\varepsilon\in\{0,1\}^n\) and define
\[
x_{\boldsymbol\delta}=d\sum_{k=1}^n\delta_k b^{-k},\qquad
\lambda_{\boldsymbol\varepsilon}=\sum_{j=0}^{n-1}t_j\varepsilon_{j+1}b^j,\qquad
w_{\boldsymbol\delta}=\prod_{k=1}^n p_k^{1-\delta_k}(1-p_k)^{\delta_k}.
\]
The weighted finite Fourier evaluation matrix \(A_n\), with frequency rows and spatial-word columns, has entries
\[
(A_n)_{\boldsymbol\varepsilon,\boldsymbol\delta}=\sqrt{w_{\boldsymbol\delta}}\,e^{2\pi i\lambda_{\boldsymbol\varepsilon}x_{\boldsymbol\delta}}.
\]
Write \(N=2^n\) and \(s_j=|\sin(\pi d t_j/b)|\). If any \(s_j=0\), the matrix is singular. Otherwise \(G_n=A_n^*A_n\) is invertible and **every diagonal entry of its inverse** is exactly
\[
\boxed{\ (G_n^{-1})_{\boldsymbol\delta,\boldsymbol\delta}
=\frac1{N w_{\boldsymbol\delta}}\prod_{j=0}^{n-1}s_j^{-2}.\ }
\]
Thus the product of a cell's mass and its local inverse-Gram variance is independent of the cell. Summing gives the exact normalized inverse second moment (an A-optimal noise-amplification criterion):
\[
\boxed{\ \frac1N\operatorname{tr}(G_n^{-1})
=\prod_{j=0}^{n-1}\frac1{4p_{j+1}(1-p_{j+1})s_j^2}
=|\det A_n|^{-4/N}.\ }
\]
The final equality is an exceptional exact A–D spectral identity, not a generic identity for square matrices. Equivalently,
\[
|\det A_n|=\prod_{j=0}^{n-1}
\bigl(2\sqrt{p_{j+1}(1-p_{j+1})}\,s_j\bigr)^{N/2}.
\]

Let \(g=\gcd(b,d)\), \(q=b/g\), and
\[
S_q=\begin{cases}1,&q\text{ even},\\ \cos\bigl(\pi/(2q)\bigr),&q\text{ odd}.\end{cases}
\]
**Joint sharp optimality:** over every allowed frequency-step selection and every strictly positive product probability, the minimum of \(N^{-1}\operatorname{tr}(G_n^{-1})\) is exactly \(S_q^{-2n}\). All and only the minimizers satisfy \(p_k=1/2\) for every \(k\), together with the independent frequency-step congruences
\[
(d/g)t_j\equiv q/2\pmod q\quad(q\text{ even}),
\]
or
\[
(d/g)t_j\equiv (q-1)/2\ \text{or}\ (q+1)/2\pmod q\quad(q\text{ odd}).
\]
For these optimal matrices the same joint choice also minimizes the largest diagonal entry of \(G_n^{-1}\), with the same sharp value \(S_q^{-2n}\). In particular, for odd \(q\), every allowed weighted product design obeys
\[
\sigma_{\min}(A_n)^2\le S_q^{2n},\qquad
\operatorname{cond}_2(A_n)\ge S_q^{-n};
\]
these inequalities are obstructions, **not** claimed sharp singular-value formulas. At the standard middle-third design \((b,d)=(3,2)\), the optimal normalized inverse trace is exactly \((4/3)^n\). For even \(q\), optimal designs are unitary and the minimum equals one.

## Assumptions and scope
Every asserted depth is a positive integer. Both binary digit words range over all of \(\{0,1\}^n\); each frequency step is an integer strictly between zero and the base. The points and frequencies are distinct: the first differing spatial digit dominates its smaller-digit tail, and the frequency words are distinct by uniqueness of base-\(b\) digits. The weights are a strictly positive **product probability**, so their sum is one. All norms and the Gram matrix use ordinary unweighted Euclidean coordinates on the normalized spatial coefficient vector; the matrix already includes the square roots of the atomic masses in its columns. The noise interpretation refers to independent equal-variance noise in the Fourier measurements and the usual inverse estimator. Arbitrary nonproduct weights, redundant frequency sets, noninteger digit steps, and limiting infinite Cantor measures are outside the theorem.

## Proof
For \(n=0\), set \(A_0=(1)\). For positive depth, abbreviate \(p=p_n\), \(t=t_{n-1}\), \(\omega=e^{2\pi i dt/b}\), and \(B=A_{n-1}\). Order frequency rows by the top frequency bit and spatial columns by the last spatial bit. Put
\[
D=\operatorname{diag}_{\lambda'}\left(e^{2\pi i\lambda'd/b^n}\right),\qquad
H=\begin{pmatrix}\sqrt p&\sqrt{1-p}\\ \sqrt p&\omega\sqrt{1-p}\end{pmatrix}.
\]
Here \(\lambda'\) ranges over the depth-\(n-1\) frequencies. Because \(b^{n-1}x_{\delta_1,\ldots,\delta_{n-1}}\) is an integer and the weights factor by the final digit, direct substitution yields the exact block identity
\[
A_n=\begin{pmatrix}\sqrt p B&\sqrt{1-p}DB\\\sqrt p B&\omega\sqrt{1-p}DB\end{pmatrix}
=(H\otimes I)\operatorname{diag}(I,D)\operatorname{diag}(B,B).
\]
No approximation or asymptotic step occurs. The determinant of \(H\) is \(\sqrt{p(1-p)}(\omega-1)\); hence \(H\) is invertible precisely when \(\omega\ne1\), or \(s_{n-1}\ne0\). The block identity proves the singularity criterion by induction.

In the nonsingular case invert the factors:
\[
A_n^{-1}=\operatorname{diag}(B^{-1},B^{-1})
\operatorname{diag}(I,D^*) (H^{-1}\otimes I).
\]
For a row belonging to the last spatial digit \(r\in\{0,1\}\), each of its two frequency-bit subblocks is a scalar entry from row \(r\) of \(H^{-1}\) multiplying the same row of \(B^{-1}D_r^*\), where \(D_0=I\) and \(D_1=D\). Right multiplication by the diagonal unitary \(D_r^*\) preserves that row's Euclidean norm. Consequently, the squared norm of the entire row of \(A_n^{-1}\) is the product of the squared row norm of \(B^{-1}\) and the squared row norm of \(H^{-1}\). The squared row norm of an inverse matrix is the corresponding diagonal entry of its inverse Gram matrix.

A direct two-by-two inverse gives
\[
H^{-1}=\frac1{\sqrt{p(1-p)}(\omega-1)}
\begin{pmatrix}\omega\sqrt{1-p}&-\sqrt{1-p}\\-\sqrt p&\sqrt p\end{pmatrix},
\]
so its row-squared norms are
\[
\frac1{2p\sin^2(\pi dt/b)}\quad\text{and}\quad
\frac1{2(1-p)\sin^2(\pi dt/b)}.
\]
Multiplication of these factors over all digits yields the claimed spatially resolved inverse-Gram diagonal formula. This step proves an identity for **every** spatial word, stronger than a determinant or trace identity.

Summing the diagonal over the words and using
\[
\sum_{\boldsymbol\delta}w_{\boldsymbol\delta}^{-1}
=\prod_{k=1}^n\left(\frac1{p_k}+\frac1{1-p_k}\right)
=\prod_{k=1}^n\frac1{p_k(1-p_k)}
\]
gives the normalized inverse trace. On the other hand the block determinant recurrence, together with \(|\det D|=1\), gives
\[
|\det A_n|=\prod_{j=0}^{n-1}
\bigl(2\sqrt{p_{j+1}(1-p_{j+1})}\,s_j\bigr)^{N/2}.
\]
Comparing these **two independently established identities** proves the exact trace–determinant relation.

Since \(4p(1-p)\le1\) with equality only at \(p=1/2\), the trace product is minimized in the probabilities by uniform weights. Put \(q=b/\gcd(b,d)\). The residues of \((d/g)t\) modulo \(q\) as \(1\le t<b\) cover all residue classes, and the largest value of \(|\sin(\pi r/q)|\) is \(S_q\); precisely the stated residue classes attain it. The independent level factors prove both the optimum and its equality classification.

For the maximum diagonal criterion, the worst cell has the smallest mass. The minimum mass is at most \(1/N\), with equality only when every \(p_k=1/2\). Thus
\[
\max_{\boldsymbol\delta}(G_n^{-1})_{\boldsymbol\delta,\boldsymbol\delta}
=\frac{\prod s_j^{-2}}{N\min_{\boldsymbol\delta}w_{\boldsymbol\delta}}
\ge S_q^{-2n}
\]
with exactly the same equality conditions. Finally, the reciprocal squared singular values have mean at least \(S_q^{-2n}\), so their maximum is at least that large and \(\sigma_{\min}(A_n)^2\le S_q^{2n}\). Each frequency row has squared norm \(\sum w_{\boldsymbol\delta}=1\), so \(\|A_n\|_F^2=N\) and \(\sigma_{\max}(A_n)\ge1\); the condition-number inequality follows. All quantities are finite at the positive-probability optimizers.

## Verification
The accompanying standalone `CHECK.py` independently builds the complete complex Fourier matrices directly from the digit-coordinate definitions. It computes the inverse by numerical matrix algebra, checks every spatial row norm of the inverse against the local exact formula, compares the total squared Frobenius norm with the trace and determinant identities, tests normalization and general lower bounds, detects singular digit choices, and enumerates finite step optima for several bases. The complete program passed `INDEPENDENT_WEIGHTED_CANTOR_INVERSE_TRACE_CHECKS_PASSED 2045`. These floating-point tests are supplementary; the proof above is exact at all positive integer depths and admissible parameters.

## Relationship to prior work
The 2026 non-frame theorem of de Dios Pont, Liehr and Taylor motivates a quantitative look at finite odd-base approximants; its full publicly available text proves the absence of Fourier frames for the **infinite** odd-base Cantor measure using frame inequalities and a limiting contradiction, not an inverse-Gram diagonal or finite-stage A-optimality identity. Fu, Song and Wang address related infinite-measure non-frame obstructions.

The closest published **same finite digit-tower object**, *Exact Fourier volume and the parity barrier in binary Cantor digit towers* (published-finding corpus, 2026), already proves the all-depth determinant product and the frequency-digit congruences that maximize that determinant for uniform spatial weights, and it derives a weaker determinant-based least-singular-value obstruction. These discoveries are prior work, not claimed anew here. The present statement adds spatially resolved inverse-Gram diagonals at **arbitrary strictly positive product weights**, the exact inverse second spectral moment, its exceptional algebraic relation to the determinant, joint A- and maximum-coordinate optimality over weights and steps, and the stronger squared-exponent instability bound. The diagonal inverse-Gram identity is not logically supplied by a determinant alone; different Gram matrices can share a determinant and have different inverse diagonal and trace. Its proof uses a distinct rowwise inverse-block-norm invariant.

The compatible digit-pair and Fourier-basis theory of Łaba and Wang concerns orthogonal spectral measures, including the even-base endpoint. Lai and Wang develop almost-Parseval finite towers and general frame bounds, not the present inverse diagonal formula. Dutkay and Ranasinghe study weighted **exponential functions** and Parseval frames on self-affine measures; their frequency-side weights differ from the spatial product masses here. These works provide context but their inspected statements do not imply the local identity.

## Limitations
The result is an exact finite-dimensional theorem for square integer-frequency digit towers and spatial Bernoulli product masses. It neither proves nor contradicts nonexistence of any Fourier frame for the limiting odd-base Cantor measure, because arbitrary noninteger, nondigit-product or redundant frequency systems are not included. The derived least-singular-value and condition-number bounds are not asserted to be attained. It does not optimize the whole singular spectrum, and no statement about arbitrary correlated spatial weights is made. Older equivalent inverse-factorization formulas in finite Fourier-tower or optimal-design literature may remain unindexed; no claim of definitive worldwide publication priority is made.

## References
1. J. de Dios Pont, L. Liehr, M. A. Taylor, *Cantor measures with odd base do not admit Fourier frames*, first public 2026-07-09, arXiv:2607.08656, https://arxiv.org/abs/2607.08656; complete lawful public preprint text also at https://www.researchgate.net/publication/408699358_Cantor_measures_with_odd_base_do_not_admit_Fourier_frames.
2. X.-Y. Fu, Z.-J. Song, W.-J. Wang, *A Walsh--Quotient Obstruction for Fourier Frames on Odd Reciprocal-Power Bernoulli Convolutions*, first public 2026-07-12, arXiv:2607.10547, https://arxiv.org/abs/2607.10547.
3. *Exact Fourier volume and the parity barrier in binary Cantor digit towers*, published-finding corpus, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-fourier-volume-and-the-parity-barrier-in-binary-cantor-dig--078452622ace.
4. I. Łaba, Y. Wang, *On spectral Cantor measures*, 2001 preprint, arXiv:math/0109126, https://arxiv.org/abs/math/0109126.
5. C.-K. Lai, Y. Wang, *Non-spectral fractal measures with Fourier frames*, 2015 preprint, arXiv:1509.06855, https://arxiv.org/abs/1509.06855.
6. D. E. Dutkay, R. Ranasinghe, *Weighted Fourier frames on self-affine measures*, 2017 preprint, arXiv:1710.01224, https://arxiv.org/abs/1710.01224.
