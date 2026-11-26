# Sharp three-character fourth-moment constants on compact Abelian groups

## Finding
Let \(G\) be a compact Abelian group with normalized Haar measure, and let \(\chi:G\to\mathbb T\) be a continuous character whose order \(m\) is an integer at least three, or is infinite. For complex coefficients \(a,b,c\), consider \(T=a+b\chi+c\chi^2\). The exact squared-normalization-independent fourth-moment constants are
\[
\sup_{T\ne0}\frac{\|T\|_{L^4(G)}^4}{\|T\|_{L^2(G)}^4}
=\begin{cases}
3,&m=3,\\
\frac73,&m=4,\\
\frac{15}{7},&m\ge5\text{ or }m=\infty.
\end{cases}
\]
Equivalently, the sharp operator norm of three-character synthesis from Euclidean coefficient space to \(L^4(G)\) is the fourth root of the displayed number. Every maximizer, and only the maximizers, is described below, up to nonzero complex scalar \(\rho\):
\[
(a,b,c)=\begin{cases}
\rho(1,\zeta,\zeta^2),&m=3,\ \zeta^3=1,\\
\rho(1,\zeta,\zeta^2),&m=4,\ \zeta^4=1,\\
\rho(\sqrt2,\sqrt3\zeta,\sqrt2\zeta^2),&m\ge5\text{ or }m=\infty,\ |\zeta|=1.
\end{cases}
\]
This includes every compact Abelian group and all cyclic quotients carrying a character of the specified order; no assumption that \(G\) itself is cyclic is necessary.

## Assumptions and scope
The Haar measure of \(G\) has total mass one, and the four-norm means \(\|T\|_4^4=\int_G|T(x)|^4\,dx\). Distinct powers of \(\chi\) are orthogonal in \(L^2(G)\). Writing \(A=|a|^2+|b|^2+|c|^2\), one has \(\|T\|_2^2=A\). Thus all ratios are unchanged when the coefficient triple is multiplied by a nonzero scalar. For the proof it suffices to consider \(A=1\). The order-three boundary is treated separately because the fourth-moment Fourier frequencies alias modulo three; order four aliases one opposite pair; starting at order five, the frequencies \(0,\pm1,\pm2\) are all distinct.

## Proof
Let \(C_r\) denote the coefficient of \(\chi^r\) in \(|T|^2\), with exponents interpreted modulo the order when finite. Haar orthogonality gives \(\|T\|_4^4=\sum_r|C_r|^2\).

For \(m\ge5\), including infinite order, the only nonzero coefficients are
\[
C_0=A,\quad C_1=b\bar a+c\bar b,\quad C_2=c\bar a,
\quad C_{-r}=\overline{C_r}\ (r=1,2),
\]
so
\[
\|T\|_4^4=A^2+2|b\bar a+c\bar b|^2+2|c\bar a|^2.
\]
Normalize \(A=1\), and write \(s=|a|^2+|c|^2\), \(q=|a||c|\). Then \(0\le s\le1\), \(0\le q\le s/2\), and
\[
\|T\|_4^4\le1+2(1-s)(s+2q)+2q^2
\le1+4s-\frac72s^2
=\frac{15}{7}-\frac72\left(s-\frac47\right)^2.
\]
The first equality condition requires that \(b\bar a\) and \(c\bar b\) have the same argument when nonzero. The second requires \(|a|=|c|\); the third requires \(s=4/7\). In the extremal case these conditions give precisely \(|a|=|c|=\sqrt{2/7}\), \(|b|=\sqrt{3/7}\), and \(2\arg b=\arg a+\arg c\) modulo \(2\pi\). Consequently the stated high-order family exhausts equality; direct substitution attains \(15/7\).

More quantitatively, when the three coefficients are nonzero define \(\delta=\arg a+\arg c-2\arg b\). The preceding proof gives the **exact nonnegative deficit identity**
\[
\frac{15}{7}-\|T\|_4^4
=\frac72\left(s-\frac47\right)^2
+\left(\frac{s}{2}-q\right)\left[4(1-s)+2\left(\frac s2+q\right)\right]
+4(1-s)q(1-\cos\delta).
\]
For zero coefficients the last term is interpreted as zero; continuity extends the identity. This decomposes loss of sharpness into incorrect central mass, unbalanced endpoints, and phase misalignment.

For \(m=4\), the residue-two coefficient is self-conjugate: \(C_2=c\bar a+a\bar c=2\operatorname{Re}(c\bar a)\). All other coefficients retain their preceding formulas. Hence
\[
\|T\|_4^4=A^2+2|b\bar a+c\bar b|^2+4\bigl(\operatorname{Re}(c\bar a)\bigr)^2.
\]
For \(A=1\) and the same \(s,q\), this implies
\[
\|T\|_4^4\le1+2(1-s)(s+2q)+4q^2
\le1+4s-3s^2
=\frac73-3\left(s-\frac23\right)^2.
\]
Equality requires \(|a|=|b|=|c|=1/\sqrt3\), aligned neighboring products, and \(c\bar a\) real; these conditions are equivalent to a geometric coefficient progression with fourth-root ratio. Such progressions attain \(7/3\).

For \(m=3\), the image of \(\chi\) consists of all three cubic roots of unity with Haar mass \(1/3\) each. Put \(u_j=T(x_j)\) for one representative of each character value. Orthogonality gives \(A=\frac13\sum_{j=0}^2|u_j|^2\), and therefore
\[
\|T\|_4^4=\frac13\sum_{j=0}^2|u_j|^4
\le\frac13\left(\sum_{j=0}^2|u_j|^2\right)^2=3A^2.
\]
Equality holds exactly when one \(u_j\) is nonzero and the other two vanish. Inverse discrete Fourier transformation says exactly that the three coefficients are a nonzero scalar multiple of \((1,\zeta,\zeta^2)\) for a cubic root \(\zeta\). This completes the proof of all constants and equality families.

## Verification
A Python 3 standard-library program in `verify.py` performs exact rational computations for the three sharp ratios, for the square-completion identities, and for a grid of admissible coefficient masses and endpoint products. It separately checks all four allowed phase ratios in the order-four case. Run `python3 verify.py` from the extracted file's directory. The full proof above establishes all infinitely many character orders and all compact Abelian groups; finite computations are only consistency checks.

At orders at least five, the normalized fourth-moment quotient of the equal-coefficient Dirichlet sum \(1+\chi+\chi^2\) is \(19/9\), while the sharp value is \(15/7\), a strict gain of \(2/63\). This explicitly distinguishes the complete nonlinear extremizer from a default equal-coefficient choice.

## Relationship to prior work
Gorbachev's September 2026 survey of sharp Bernstein–Nikolskii inequalities emphasizes that finite-exponent sharp constants are poorly understood in general. It does not give the displayed exact three-character \(L^2\)-to-\(L^4\) synthesis norm or its finite-torsion equality classification. The April 2026 article of Ling, Geng, Li, and Wang concerns **average** Nikolskii factors of random trigonometric polynomials, not worst-case sharp constants or complete extremizers. The publicly available mathematical note *Exact three-frequency Fourier projection norm on every cyclic group* computes endpoint \(L^1\)- and \(L^\infty\)-projection norms by sampled absolute Dirichlet sums; it is a different input-output operator and does not imply the nonlinear \(L^2\)-to-\(L^4\) synthesis bound here. Nor do three-sparse Fourier-support spectra, which classify zeros rather than extremal fourth moments, imply the theorem. Searches for synonymous \(\Lambda(4)\), Nikolskii, and Fourier-restriction formulations did not locate covering results. Non-detection is not a proof of historical novelty.

## Limitations
The theorem concerns exactly three consecutive powers of one character. It does not cover arbitrary three-character sets, four or more terms, all exponent pairs, or the unrestricted sharp Nikolskii problem. The constant \(15/7\) is not the full unrestricted degree-dependent sharp norm. Existing elementary treatments of short polynomial fourth moments may contain an equivalent formula under older terminology; the prior-art search cannot exclude that risk. Independent external mathematical auditing has not been carried out.

## References
1. D. V. Gorbachev, *Sharp Bernstein–Nikolskii inequalities for polynomials and entire functions of exponential type*, arXiv:2609.32072v1, first public 2026-09-25. https://arxiv.org/html/2609.32072v1
2. Y. Ling, J. Geng, J. Li, H. Wang, *Average Nikolskii factors for random trigonometric polynomials*, arXiv:2503.16786, first public 2025-03-21; *Journal of Inequalities and Applications* 2026, article 78, DOI:10.1186/s13660-026-03484-x.
3. *Exact three-frequency Fourier projection norm on every cyclic group*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242
