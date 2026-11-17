# A sharp resonance transition for triangular conjugate-unitary multipliers

## Finding
Let \(H=L^2(\mathbb T,d\theta/2\pi)\), let \(U=M_{e^{i\theta}}\), and let \(b\in L^\infty(\mathbb T)\). Set
\[
F_b=\begin{pmatrix}U^*&M_b\\0&U\end{pmatrix},\qquad
\Phi(s)=\frac{s+\sqrt{s^2+4}}2\quad(s\ge0).
\]
Then \(\sigma(F_b)=\mathbb T\), and for every integer \(n\ge1\),
\[
\|F_b^n\|=\Phi\left(\operatorname*{ess\,sup}_{\theta\in[-\pi,\pi]}
|b(\theta)|\left|\frac{\sin(n\theta)}{\sin\theta}\right|\right).
\tag{1}
\]
Values of the quotient on its null denominator are defined by continuous extension. The following are equivalent:
\[
\sup_{n\ge1}\|F_b^n\|<\infty;\quad
\frac{b}{\sin\theta}\in L^\infty;\quad
F_b\text{ is similar to }U^*\oplus U;\quad
\sup_{|\lambda|>1}(|\lambda|-1)\|(\lambda I-F_b)^{-1}\|<\infty.
\tag{2}
\]
Whenever these hold, the norms of all powers converge, with the **exact limiting value**
\[
\lim_{n\to\infty}\|F_b^n\|=\Phi\left(\left\|\frac{b}{\sin\theta}\right\|_\infty\right).
\tag{3}
\]

For the natural vanishing-order family \(b_{\alpha,c}(\theta)=c|\sin\theta|^\alpha\), where \(c>0\) and \(\alpha\ge0\), write \(F_{\alpha,c}=F_{b_{\alpha,c}}\). For \(0\le\alpha<1\),
\[
\boxed{\lim_{n\to\infty}n^{\alpha-1}\|F_{\alpha,c}^n\|=cM_\alpha},\qquad
M_\alpha=\max_{x>0}\frac{|\sin x|}{x^{1-\alpha}}.
\tag{4}
\]
Here \(M_0=1\); for \(0<\alpha<1\), the maximizing \(x_\alpha\) is unique and lies in \((0,\pi/2)\), with \(x_\alpha\cot x_\alpha=1-\alpha\). At the threshold, \(\|F_{1,c}^n\|=\Phi(c)\) for every \(n\ge1\); above it, \(\lim_{n\to\infty}\|F_{\alpha,c}^n\|=\Phi(c)\).

The **sharp radial resolvent laws** at the spectral intersection \(1\) are
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{2-\alpha}
\|((1+\varepsilon)I-F_{\alpha,c})^{-1}\|
=cC_\alpha\quad(0\le\alpha<1)},
\tag{5}
\]
where \(C_0=1\) and
\[
C_\alpha=\max_{x\ge0}\frac{x^\alpha}{1+x^2}
=\frac12\alpha^{\alpha/2}(2-\alpha)^{1-\alpha/2}
\quad(0<\alpha<1).
\]
Exactly at and above the power-boundedness threshold, the constants **separate**:
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon
\|((1+\varepsilon)I-F_{\alpha,c})^{-1}\|=
\begin{cases}\sqrt{1+c^2/4},&\alpha=1,\\1,&\alpha>1.
\end{cases}}
\tag{6}
\]
Thus every exponent \(0<1-\alpha\le1\) occurs as a sharp power-growth exponent; its associated radial resolvent exponent is \(2-\alpha\), and the critical resolvent constant is neither the subcritical limit nor the ordinary normal-operator constant.

## Assumptions and scope
The circle has normalized Lebesgue measure, and the Hilbert space is complex. Multipliers are identified almost everywhere. For \(\alpha=0\), \(|\sin\theta|^0\) means the constant function one, including at its two zeros. At the finitely many singular angles in displayed formulas, the values are immaterial to essential suprema. \(\|\cdot\|\) is the Hilbert-space operator norm. The resolvent is considered along real \(1+\varepsilon\), with \(\varepsilon>0\). A Kreiss bound in (2) refers to the entire exterior disk, not just that ray.

## Proof
**1. Two-by-two norm and power formula.** For \(|u|=|v|=1\), the matrix \(\bigl(\begin{smallmatrix}u&w\\0&v\end{smallmatrix}\bigr)\) is unitarily equivalent on its two sides to \(\bigl(\begin{smallmatrix}1&|w|\\0&1\end{smallmatrix}\bigr)\), whose largest singular value is \(\Phi(|w|)\). Multiplication operators on \(L^2(\mathbb T;\mathbb C^2)\) have norm the essential supremum of their fibre norms. For \(z=e^{i\theta}\), direct multiplication yields
\[
\begin{pmatrix}z^{-1}&b(\theta)\\0&z\end{pmatrix}^{n}
=\begin{pmatrix}z^{-n}&b(\theta)\sum_{k=0}^{n-1}z^{-(n-1-k)}z^k\\0&z^n\end{pmatrix}
=\begin{pmatrix}z^{-n}&b(\theta)\sin(n\theta)/\sin\theta\\0&z^n\end{pmatrix}.
\]
This proves (1). For \(|\lambda|\ne1\), the triangular fibre inverse is uniformly bounded, while for each \(\lambda\in\mathbb T\), normalized vectors supported where \(z^{-1}\) approaches \(\lambda\) make \(F_b-\lambda I\) fail to be bounded below. Hence \(\sigma(F_b)=\mathbb T\).

**2. Four equivalent conditions.** If \(g(\theta)=b(\theta)/\sin\theta\) is bounded, then the bounded shear
\[
S=\begin{pmatrix}I&M_{b/(2i\sin\theta)}\\0&I\end{pmatrix}
\]
satisfies \(F_b=S(U^*\oplus U)S^{-1}\), proving similarity, power boundedness, and the Kreiss condition. Conversely, the elementary pointwise fact
\[
\sup_{n\ge1}|\sin(n\theta)|\ge\sqrt3/2
\quad\text{for almost every }\theta
\]
follows from density of irrational rotations and the explicit maxima of rational rotations of denominator at least two. Since a countable supremum interchanges with essential suprema, uniform bounds in (1) force \(b/\sin\theta\in L^\infty\).

For the converse using only a Kreiss bound \(K\), the upper-right inverse entry at \(\lambda=1+\varepsilon\) has modulus \(|b(\theta)|/|1+\varepsilon-e^{i\theta}|^2\), so
\[
\varepsilon\frac{|b(\theta)|}{\varepsilon^2+2(1+\varepsilon)(1-\cos\theta)}\le K
\quad\text{a.e.}
\]
Apply the same bound at \(\lambda=-1-\varepsilon\) to control a neighborhood of \(\pi\). Taking rational \(\varepsilon\) and then using continuity in \(\varepsilon\) on their common full-measure set allows the choice \(\varepsilon=\operatorname{dist}(\theta,\pi\mathbb Z)\). Each denominator is at most three times the squared distance when that distance is small. Therefore \(|b(\theta)|\le3K\operatorname{dist}(\theta,\pi\mathbb Z)\) near the two crossings; away from them boundedness of \(b\) suffices. Since \(|\sin\theta|\) is comparable to this distance, \(g\in L^\infty\). This proves (2) without assuming either a converse Kreiss theorem or a similarity theorem.

**3. Exact limit in the bounded regime.** In (1), write the argument of \(\Phi\) as \(\|g(\theta)\sin(n\theta)\|_\infty\), at most \(G=\|g\|_\infty\). For \(\delta,\eta>0\), the measurable set \(E=\{|g|>G-\delta\}\) has positive measure when \(G>0\). The periodic set \(\{|\sin(n\theta)|>1-\eta\}\) intersects \(E\) in positive measure for all sufficiently large \(n\): approximate its periodic indicator by trigonometric polynomials, and use the Riemann–Lebesgue lemma for the integral against \(\mathbf1_E\); its asymptotic intersection measure is the product of two positive normalized measures. Thus \(\liminf_n\|g\sin(n\theta)\|_\infty\ge(G-\delta)(1-\eta)\). Let \(\delta,\eta\downarrow0\), apply continuity of \(\Phi\), and handle \(G=0\) directly. This proves (3).

**4. Exact power-growth transition.** For \(b_{\alpha,c}\), the argument in (1) is
\[
c\operatorname*{ess\,sup}_{\theta}\left(|\sin\theta|^{\alpha-1}|\sin(n\theta)|\right).
\]
For \(\alpha<1\), the contribution from any fixed compact interval avoiding the zeros of \(\sin\theta\) is \(O(1)\), negligible after division by \(n^{1-\alpha}\). Near either zero, put \(x=n\operatorname{dist}(\theta,\pi\mathbb Z)\); the normalized integrand converges locally uniformly for positive \(x\) to \(x^{\alpha-1}|\sin x|\). Uniform tail control follows from \(|\sin\theta|\ge(1-o(1))\operatorname{dist}(\theta,\pi\mathbb Z)\) near the crossings and the envelope \(x^{\alpha-1}\) for large \(x\). At \(\alpha=0\), the function extends continuously with value one at zero; for \(\alpha>0\), its zero limit is zero. Hence the supremum tends to \(M_\alpha\), and \(\Phi(s)/s\to1\) as \(s\to\infty\), proving (4). At \(\alpha=1\), the argument of \(\Phi\) equals \(c\) at every positive integer power. For \(\alpha>1\), (3) applies with \(\|g\|_\infty=c\).

For \(0<\alpha<1\), the maximum cannot occur after the first positive half-wave, since \(x^{\alpha-1}\) decreases and the value at \(\pi/2\) exceeds every value for \(x\ge\pi\). On \((0,\pi)\), the logarithmic derivative vanishes precisely at \(x\cot x=1-\alpha\). This function decreases strictly from one to zero on \((0,\pi/2)\), proving uniqueness. For \(\alpha=0\), \(|\sin x|\le x\) gives \(M_0=1\).

**5. Exact resolvent constants.** For real \(\lambda=1+\varepsilon\), both fibre diagonal denominators have modulus
\[
d_\varepsilon(\theta)=\sqrt{\varepsilon^2+2(1+\varepsilon)(1-\cos\theta)}.
\]
Taking the inverse of each fibre, then using the same two-by-two norm, gives the **exact identity**
\[
\|((1+\varepsilon)I-F_b)^{-1}\|
=\operatorname*{ess\,sup}_\theta\frac1{d_\varepsilon(\theta)}
\Phi\left(\frac{|b(\theta)|}{d_\varepsilon(\theta)}\right).
\tag{7}
\]
The inequalities \(s\le\Phi(s)\le1+s\) imply
\[
\sup_\theta\frac{|b(\theta)|}{d_\varepsilon(\theta)^2}
\le\|((1+\varepsilon)I-F_b)^{-1}\|
\le\frac1\varepsilon+\sup_\theta\frac{|b(\theta)|}{d_\varepsilon(\theta)^2}.
\]
For \(0\le\alpha<1\), rescale \(\theta=\varepsilon x\). Uniform convergence on bounded \(x\)-intervals and an elementary tail bound give
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{2-\alpha}
\sup_\theta\frac{c|\sin\theta|^\alpha}{d_\varepsilon(\theta)^2}
=c\max_{x\ge0}\frac{x^\alpha}{1+x^2}.
\]
The additive diagonal contribution vanishes after scaling. Differentiation yields \(x^2=\alpha/(2-\alpha)\) for \(0<\alpha<1\), and the maximum at zero for \(\alpha=0\), proving (5).

For \(\alpha=1\), the same scaling in (7), now without discarding the diagonal, yields
\[
\lim_{\varepsilon\downarrow0}\varepsilon\|((1+\varepsilon)I-F_{1,c})^{-1}\|
=\sup_{x\ge0}\frac1{\sqrt{1+x^2}}\Phi\left(\frac{cx}{\sqrt{1+x^2}}\right).
\]
The tails in \(x\) vanish uniformly; contributions away from \(\theta=0\) vanish as well. With \(y=x/\sqrt{1+x^2}\), differentiate \(\sqrt{1-y^2}\Phi(cy)\) on \([0,1]\). Its unique maximizing point satisfies \(y^2=c^2/(2(c^2+2))\), and the maximum equals \(\sqrt{1+c^2/4}\). When \(\alpha>1\), \(\varepsilon|b|/d_\varepsilon^2=o(1)\) uniformly, as follows by splitting near \(\theta=0\) and its complement and using \(d_\varepsilon^2\gtrsim\varepsilon^2+\theta^2\) locally. Formula (7) and \(\varepsilon/d_\varepsilon\le1\) give an upper limit of one, achieved by taking \(\theta\to0\). This proves (6).

## Verification
The accompanying `checker.py` tests fibre powers against independent direct matrix multiplication and singular-value calculations; tests the exact resolvent formula against direct matrix inversion; and samples the critical scales in (4)–(6) with explicit tolerances. Its successful finite output is supplementary evidence only. All universal assertions for arbitrary measurable symbols, all equivalences, and all limits are proved in Steps 1–5, independently of finite experiments.

## Relationship to prior work
Nag and Golla, *Norm and Minimum Attainment of Foguel-Type Operators* (2026), prove the one-step block-norm and attainment results for arbitrary isometric diagonals. The present \(\Phi\) formula uses that established norm calculation and **does not claim it as new**. The focus here is instead exact growth of **every power**, full power-boundedness/similarity/Kreiss equivalence for commuting multiplication couplings, and sharp polynomial growth and radial resolvent constants with a critical jump.

Chalmoukis and Marano, *Generalized Foguel-Hankel operators* (2026), address Hardy-space multipliers paired with Hankel corners and prove Kreiss/power-boundedness implications, but their Hankel symbols and unilateral nonunitary setting do not cover these arbitrary measurable multiplication corners on bilateral unitary copies. The published finding *A complete singular spectral normal form for generalized Foguel operators* covers the **one-step modulus** of more general block operators, not their powers or radial resolvent asymptotics. *Upper Banach means govern power growth of positive-coupling shift blocks* proves an exact **linear** coefficient for positive diagonal corners of unilateral shift/adjoint blocks, whereas the present unitary-multiplier family has a continuum of fractional exponents and an exact Kreiss transition. These comparisons are based on their mathematical statements and inspected proofs, not mere title matching.

## Limitations
The exponents and constants (4)–(6) are established only for the given vanishing-order family, although the boundedness equivalences and norm limit (1)–(3) hold for every bounded measurable symbol. Only the outward radial resolvent at \(1\) receives a full sharp asymptotic profile; no analogous formula for general approach paths or noncommuting couplings is claimed. The scalar-matrix and harmonic-analysis ingredients are classical, so an earlier equivalent synthesis for commuting triangular operators remains a publication-priority risk. Mathematical priority has not been independently certified; numerical diagnostics do not replace proofs.

## References
1. P. Nag and R. Golla, *Norm and Minimum Attainment of Foguel-Type Operators*, arXiv:2610.42102v1, first posted 2026-10-30. https://arxiv.org/abs/2610.42102
2. N. Chalmoukis and G. Marano, *Generalized Foguel-Hankel operators*, arXiv:2601.19599v1, first posted 2026-01-27. https://arxiv.org/html/2601.19599v1
3. S. R. Garcia, *The norm and modulus of a Foguel operator*, Indiana Univ. Math. J. 58 (2009), 2305–2316; arXiv:0908.0479. https://arxiv.org/abs/0908.0479
4. *A complete singular spectral normal form for generalized Foguel operators* (2026), mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-complete-singular-spectral-normal-form-for-generalized-foguel--528ccf5ad5d1
5. *Upper Banach means govern power growth of positive-coupling shift blocks* (2026), mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-upper-banach-means-govern-power-growth-of-positive-coupling-shif--14662ba542a1
