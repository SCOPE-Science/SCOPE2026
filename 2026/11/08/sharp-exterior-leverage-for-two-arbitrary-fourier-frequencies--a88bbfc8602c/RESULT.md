# Sharp exterior leverage for two arbitrary Fourier frequencies

## Finding

Let \(\lambda_1,\lambda_2\in\mathbb R\) be distinct and \(f(t)=a e^{i\lambda_1t}+b e^{i\lambda_2t}\), with \((a,b)\ne(0,0)\). For every \(|x|\ge1\), the **exact frequency-uniform exterior evaluation constant** with the unaveraged Lebesgue norm is

\[
\sup_{\lambda_1\ne\lambda_2}\ \sup_{(a,b)\ne(0,0)}\frac{|f(x)|^2}{\int_{-1}^{1}|f(t)|^2\,dt}=\frac{1+3x^2}{2}.
\]

The supremum is **never attained** when the frequencies are distinct. Write \(d=|\lambda_2-\lambda_1|>0\) and \(s=\sin d/d\). For each *fixed gap* the exact optimal squared quotient is

\[
K_d(x)=\frac{1-s\cos(dx)}{1-s^2},
\]

and, for fixed \(|x|\ge1\), its sharp small-gap deficit is

\[
\frac{1+3x^2}{2}-K_d(x)
=\frac{15x^4+6x^2-5}{120}\,d^2+O_x(d^4).
\]

This coefficient is strictly positive on the entire exterior. Equivalently, the best *unsquared* extrapolation factor is \(\sqrt{(1+3x^2)/2}\). If the training norm uses uniform probability measure \(dt/2\), the squared constant is \(1+3x^2\).

## Assumptions and scope

Frequencies are arbitrary, distinct **real** numbers; coefficients are arbitrary nonzero pairs in \(\mathbb C^2\). No spectral separation or band limit is assumed. The time domain is precisely \([-1,1]\), the evaluation point is real with \(|x|\ge1\), and the norm is \(\|f\|^2=\int_{-1}^1|f(t)|^2dt\). At equal frequencies the function class collapses to one dimension and its evaluation quotient is \(1/2\), so equal frequencies are excluded. The result is a supremum across all distinct frequencies, not a maximum. A common real frequency shift only multiplies the sum by a unit-modulus factor, leaving both quantities unchanged.

## Proof

**1. Fixed-gap extremum.** Shift away a common carrier to take frequencies \(0,d\), where \(d>0\). The Gram matrix of the two exponential atoms over \([-1,1]\) is

\[
G=2\begin{pmatrix}1&s\\s&1\end{pmatrix},\qquad s=\frac{\sin d}{d}.
\]

Here \(|s|<1\) because \(d>0\), so \(G\) is positive definite. Apply Cauchy–Schwarz in the \(G\)-inner product to the evaluation vector \((1,e^{idx})\): its squared functional norm is

\[
(1,e^{idx})G^{-1}(1,e^{idx})^* = \frac{1-s\cos(dx)}{1-s^2}=K_d(x).
\]

Equality is achieved for a nonzero coefficient vector proportional to the corresponding \(G^{-1}\)-representer. Therefore the claimed fixed-gap quotient is exact, for every gap and evaluation point.

**2. Uniform upper bound for gaps at least two.** Put \(B(x)=(1+3x^2)/2\). For \(d\ge2\), \(|s|\le1/d\le1/2\), and

\[
K_d(x)\le\frac{1+|s|}{1-s^2}=\frac1{1-|s|}\le2\le B(x)\quad(|x|\ge1).
\]

Every inequality chain is strict at the relevant endpoint because \(|\sin d|<1\) when \(d=2\) and \(1/d<1/2\) when \(d>2\).

**3. Uniform upper bound for gaps less than two.** Suppose \(0<d<2\). Then \(0<s<1\). Since \(K_d\) and \(B\) are even functions of \(x\), take \(x\ge1\). Multiplication by the positive denominator shows \(K_d(x)\le B(x)\) is equivalent to

\[
F_d(x):=3x^2-1-(1+3x^2)s^2+2s\cos(dx)\ge0.
\]

At \(x=1\), set \(h(d)=d^2-2\sin^2d+d\sin d\cos d\); then \(F_d(1)=2h(d)/d^2\). Direct differentiation yields

\[
h(0)=h'(0)=0,\qquad h''(d)=4\sin d\,(\sin d-d\cos d)>0\quad(0<d<2).
\]

Indeed \(\sin d>0\) and \(\sin d-d\cos d>0\), since the latter vanishes at zero and has derivative \(d\sin d>0\). Hence \(F_d(1)>0\).

For \(x\ge1\), using \(|\sin(dx)|\le |dx|\) gives

\[
F_d'(x)=6x(1-s^2)-2ds\sin(dx)\ge2x\bigl(3(1-s^2)-d^2s\bigr).
\]

The alternating sine expansion on \([0,2]\) implies

\[
0<s\le u:=1-\frac{d^2}{6}+\frac{d^4}{120}.
\]

The function \(z\mapsto3(1-z^2)-d^2z\) is strictly decreasing for \(z>0\), and an exact polynomial calculation gives

\[
3(1-u^2)-d^2u=\frac{d^4(160-d^4)}{4800}>0\qquad(0<d<2).
\]

Thus \(F_d'(x)>0\) for \(x\ge1\), and so \(F_d(x)>F_d(1)>0\). This proves strictness for every distinct frequency pair, including \(x=\pm1\).

**4. Sharpness and collision deficit.** Fix any real \(|x|\ge1\). In the affine space spanned by \(1,t\) over \([-1,1]\), the evaluation representer is \(R_x(t)=\tfrac12+\tfrac32xt\). Its squared norm and its value at \(x\) both equal \(B(x)\). The genuine two-frequency functions

\[
f_\epsilon(t)=\frac12\cos(\epsilon t)+\frac{3x}{2}\,\frac{\sin(\epsilon t)}{\epsilon}
\]

have distinct frequencies \(\pm\epsilon\) for \(\epsilon>0\), and converge uniformly on every compact real interval to \(R_x(t)\). Their evaluation quotient tends to \(B(x)\). Combined with strictness, this proves the exact nonattained supremum. Finally, Taylor expansion of the explicit \(K_d\) at \(d=0\), with removable zero cancelled, gives

\[
K_d(x)=\frac{1+3x^2}{2}-\frac{15x^4+6x^2-5}{120}\,d^2+O_x(d^4).
\]

At \(|x|\ge1\), the correction coefficient is at least \(16/120>0\). All statements follow.

## Verification

The standalone Python 3 standard-library program `CHECK.py` verifies the rational polynomial certificate exactly, compares the Fourier Gram norm with independent numerical quadrature, tests the fixed-gap evaluation identity and strict exterior inequalities, and checks small-gap expansions and explicit confluent witnesses. Execute with `python CHECK.py` in the directory containing this result; the expected output is `TWO_FREQUENCY_EXTERIOR_CHECKS_PASSED 13160`. The finite tests are not the proof for all real gaps and exterior points; steps 1–4 provide the universal argument.

## Relationship to prior work

Zhang [1, Theorem 1.1 and Section 8.2] establishes the much broader \(k\)-sparse, no-separation exterior Fourier extrapolation and leverage framework, with nonexact Chebyshev-scale bounds. The exact all-exterior-point \(k=2\) constant, nonattainment, and quadratic gap law above are not among the statements inspected in that work. General Fourier-sparse leverage scores and sampling are treated in [2], without the exact global two-frequency exterior optimum. Borwein and Erdélyi [3] develop pointwise inequalities for real-exponent exponential sums, whereas the present frequencies are purely imaginary exponents and the evaluation is exterior. Classical endpoint Nikolskii and Turán estimates [4] overlap the endpoint theme, so novelty is asserted for the **joint sharp all-exterior profile and strict confluent gap**, not merely endpoint boundedness. A missing equivalent specialized two-atom inequality remains a publication-priority risk.

## Limitations

This determines evaluation at a **single exterior point**, not the sharp integrated transfer constant over an exterior interval or a sharp general \(k\)-frequency inequality for \(k\ge3\). The coefficient growth in the attaining sequence diverges as the frequencies collide, so the supremum is not attained by a pair of distinct real frequencies. No noise-robust estimation of the individual frequencies is established.

## References

[1] R. Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, first posted 2026-07-11, especially Theorem 1.1, Section 8.2 and Appendix A. https://arxiv.org/abs/2607.10501

[2] T. Erdélyi, C. Musco and C. Musco, *Fourier Sparse Leverage Scores and Approximate Kernel Learning*, arXiv:2006.07340 (2020). https://arxiv.org/abs/2006.07340

[3] P. Borwein and T. Erdélyi, *Pointwise Remez- and Nikolskii-type inequalities for exponential sums*, Mathematische Annalen 316 (2000), 39–60.

[4] T. Kós, *Two Turán type inequalities* (2008); see the historical endpoint discussion in [1, Appendix A].
