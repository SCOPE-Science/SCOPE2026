# Exact five-cycle Legendre–Alltop ambiguity minimax

## Finding

Let \(\omega=e^{2\pi i/5}\), let \(\chi\) be the quadratic character on \(\mathbb F_5\) extended by \(\chi(0)=0\), and for every real \(t\ge0\) set
\[
 b_t(j)=(1+t\chi(j))\omega^{j^3}\qquad(j\in\mathbb F_5).
\]
Define the discrete self-ambiguity coefficients and the normalized minimum by
\[
 A_t(k,\ell)=\sum_{j\in\mathbb F_5}\overline{b_t(j)}\omega^{\ell j}b_t(j-k),\qquad
 \alpha(t)=\min_{k,\ell\in\mathbb F_5}\frac{|A_t(k,\ell)|}{\|b_t\|_2^2}.
\]
There is exactly one maximizing parameter \(t_*>0\) in this entire nonnegative-amplitude-perturbation family. It is the unique root in \((3/8,2/5)\) of
\[
 (11\sqrt5-5)t^3-(30+2\sqrt5)t^2-5(1+\sqrt5)t+10=0.
\]
The exact sharp margin is
\[
 \boxed{\max_{t\ge0}\alpha(t)
 =\frac{2\sqrt5\,t_*-t_*^2}{5+4t_*^2}
 =0.2780211461\ldots.}
\]
Furthermore, the six and only six active ambiguity indices at \(t=t_*\) are
\[
 (0,\pm1),\qquad (1,\pm2),\qquad (-1,\pm2)
 \quad\text{in }\mathbb F_5^2.
\]
In contrast, the fixed parameter \(t=1/12\) yields \(\alpha(1/12)=0.0727425848\ldots\), so the exact optimal margin is more than three times as large. The positive margin gives injectivity of the full five-cycle Gabor intensity map by the standard nonvanishing-ambiguity criterion, without asserting a full-spark property for this unregularized window.

## Assumptions and scope

All indices and exponents are reduced modulo five; the ambiguity convention is \(T_k f(j)=f(j-k)\), \(M_\ell f(j)=\omega^{\ell j}f(j)\). The norm \(\|b_t\|_2\) uses counting measure, so \(\|b_t\|_2^2=5+4t^2\). The theorem optimizes over **every real \(t\ge0\)** and only this one-parameter Legendre-weighted cubic-chirp family. It does not optimize over arbitrary Gabor windows, negative parameters, or further algebraic full-spark perturbations. The parameter \(t_*\) is algebraic, not a rational parameter or an assumed full-spark certificate.

## Proof

**1. Exact cyclotomic reduction.** The character values in order \(0,1,2,3,4\) are \((0,1,-1,-1,1)\). Expanding gives
\[
 A_t(k,\ell)=\sum_{j=0}^{4}(1+t\chi(j))(1+t\chi(j-k))
 \omega^{(j-k)^3-j^3+\ell j}.
\]
Let \(u=\omega^2+\omega^3=-(1+\sqrt5)/2\). Conjugation and \(1+\omega+\omega^2+\omega^3+\omega^4=0\) give the following complete classification of the squared magnitudes \(P_{k,\ell}(t)=|A_t(k,\ell)|^2\); the notation \(\pm\) means both residues and is used only for the indicated indices:

| \(k\) | \(\ell\) | \(P_{k,\ell}(t)\) |
|---|---|---|
| \(0\) | \(0\) | \((5+4t^2)^2\) |
| \(0\) | \(\pm1\) | \((2\sqrt5\,t-t^2)^2\) |
| \(0\) | \(\pm2\) | \((2\sqrt5\,t+t^2)^2\) |
| \(\pm1\) | \(0\) | \((5-2u)t^4+10ut^3+(6+2u)t^2-10ut+5\) |
| \(\pm1\) | \(\pm1\) | \((4+u)t^4-(6+2u)t^3+(1-3u)t^2+5\) |
| \(\pm1\) | \(\pm2\) | \(t^4-(4+3u)t^3+(6+2u)t^2+5ut+5\) |
| \(\pm2\) | \(0\) | \((7+2u)t^4+(10+10u)t^3+(4-2u)t^2-(10+10u)t+5\) |
| \(\pm2\) | \(\pm1\) | \((3-u)t^4+(4-2u)t^3+(4+3u)t^2+5\) |
| \(\pm2\) | \(\pm2\) | \(t^4+(1-3u)t^3+(4-2u)t^2+(5+5u)t+5\) |

Here all four choices in a row with two \(\pm\) signs are covered. The accompanying exact-arithmetic checker independently regenerates all 25 polynomials by multiplication in \(\mathbb Z[\omega]/(1+\omega+\cdots+\omega^4)\); the table is thus a finite, explicitly reproducible algebraic identity rather than a floating-point enumeration.

**2. The two competing values.** Put \(Q(t)=(2\sqrt5\,t-t^2)^2\) and \(P(t)=P_{1,2}(t)\). Then
\[
 P(t)=t^4+\frac{3\sqrt5-5}{2}t^3+(5-\sqrt5)t^2
 -\frac{5(1+\sqrt5)}2t+5,
\]
so \(P(t)-Q(t)\) equals
\[
 H(t)=\frac{11\sqrt5-5}{2}t^3-(15+\sqrt5)t^2
 -\frac{5(1+\sqrt5)}2t+5.
\]
Exact rational bounds on \(\sqrt5\) show \(H(3/8)>0\), \(H(2/5)<0\), and \(H'(t)<0\) throughout \([3/8,2/5]\). Consequently exactly one \(t_*\) lies in the stated interval with \(H(t_*)=0\). A sharper exact interval certificate locates \(0.378494<t_*<0.378495\).

**3. Attainment and equality indices.** At that root \(P(t_*)=Q(t_*)\). For each of the 19 indices other than \((0,\pm1)\) and \((\pm1,\pm2)\), direct substitution of the table and exact rational interval arithmetic on \(0.378494<t<0.378495\) gives \(P_{k,\ell}(t)-Q(t)>0\). Indeed the exact checker certifies a common lower bound greater than \(0.96\) for those 19 unnormalized squared-magnitude differences. This verifies both attainment and the complete equality-index classification.

**4. Global optimality.** For \(0\le t<t_*\),
\[
 \alpha(t)\le f_0(t):=\frac{2\sqrt5\,t-t^2}{5+4t^2}.
\]
The numerator of \(f_0'(t)\), after multiplication by the positive squared denominator, is \(10\sqrt5-10t-8\sqrt5\,t^2>0\) on \([0,2/5]\); hence \(\alpha(t)<f_0(t_*)\).

For \(t>t_*\), put \(M=f_0(t_*)^2\) and
\[
 J(t)=M(5+4t^2)^2-P(t).
\]
The exact bounds \(t_*>3/8\) and monotonicity of \(f_0\) give \(M>3/40\). Differentiating and using \(11/5<\sqrt5<9/4\) gives, for every \(t\ge0\),
\[
 J'(t)>\frac45t^3-\frac{21}{8}t^2+\frac25t+8
 \ge 8-\frac{8575}{2048}>0.
\]
(The last inequality is the exact minimum of the first two monomials on the nonnegative half-line.) As \(J(t_*)=0\), for all \(t>t_*\) we have
\[
 \alpha(t)\le \frac{\sqrt{P(t)}}{5+4t^2}<\sqrt M=f_0(t_*).
\]
This proves the stated strict uniqueness and the global sharp constant without any extrapolation from finite sampling.

## Verification

Run `python3 checker.py` in a directory containing the supplied standalone `checker.py`. It requires only the Python standard library. Its exact rational calculations regenerate all 25 squared ambiguity polynomials in \(\mathbb Q(\sqrt5)[t]\), bracket the unique cubic root, prove the 19 strict inactive inequalities, and check the rational inequalities in the global proof. Numerical values above are explanatory and not proof premises. The independent classical criterion for the phase-retrieval consequence applies because the certified optimal margin is strictly positive.

## Relationship to prior work

Dongwei Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations* (arXiv:2609.09614, first submitted September 9, 2026), Section 3.1, uses the same Legendre-weighted cubic-chirp seed but fixes \(\delta=1/12\) to obtain dimension-uniform lower estimates; Remark 3.4 allows other sufficiently small parameters through a Weil-type lower bound. Neither the general bound nor its fixed choice determines the exact unrestricted nonnegative-parameter five-cycle optimum, the cubic equalization point, or the six active time-frequency shifts. The present theorem does not imply the new optimizer is full spark and does not replace that paper's simultaneous algebraic construction.

Bojarovska and Flinth, *Phase Retrieval from Gabor Measurements* (arXiv:1503.05800, 2015; J. Fourier Anal. Appl. 2016), Theorem 2.2, supplies the nonvanishing-ambiguity phase-retrieval implication and Theorem 2.3 its lifted measurement framework. Those general implications do not optimize any seed amplitude. Existing published prime-cycle Gabor chirp and one-impulse designs concern different window families or nonsharp bounds for this exact minimax problem.

## Limitations

The claim is restricted to one specifically motivated five-dimensional one-parameter family. It is not a global Grassmannian packing bound, not a general prime-dimensional margin formula, not a full-spark assertion for the unregularized optimizer, and not a claim of optimal perturbation size after an additional algebraic regularization. Numerical approximations are secondary to the exact algebraic and interval proof. A previously unindexed equivalent one-parameter calculation remains a bibliographic possibility; the stated originality assessment is relative to the inspected sources.

## References

1. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (2026), Sections 2–5 and Appendix A. https://arxiv.org/abs/2609.09614
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (2015), especially Theorems 2.2–2.3. https://arxiv.org/abs/1503.05800
