# A uniform spectral gap for spherical two-design curves on the two-sphere

## Finding

Let \(\gamma\) be any nonconstant closed rectifiable curve on the unit sphere \(S^2\subset\mathbb R^3\), with normalized arclength measure integrating every polynomial of total degree at most two exactly as uniform spherical area measure. Then its length \(L\) obeys
\[
L\ \ge\ 2\pi\sqrt{\frac{1971-180\sqrt{47}}{363}}\ =\ 8.9527209263\ldots .
\]
The previously established universal spectral bound in this case is \(2\pi\sqrt 2=8.8857658763\ldots\). The present inequality proves a **uniform, explicitly quantified nonattainment gap** above this bound for the sphere \(S^2\). The displayed new constant is a rigorous lower bound, **not asserted to be sharp**.

## Assumptions and scope

A spherical two-design curve is a closed rectifiable curve of positive finite length \(L\) whose normalized arclength measure has first moment zero and second-moment matrix \(I_3/3\). The result includes curves with corners and repeated traversals, and does not assume embeddedness or smoothness. Reparameterize by constant speed on \([0,2\pi]\), so \(|\gamma'(u)|=L/(2\pi)\) almost everywhere; this can be done for every rectifiable curve. Set \(F(u)=\sqrt3\,\gamma(u)\), with normalized average \(\langle h\rangle=(2\pi)^{-1}\int_0^{2\pi}h(u)\,du\). The exact moment and sphere identities are
\[
\langle F\rangle=0,\qquad \langle FF^{\mathsf T}\rangle=I_3,\qquad |F(u)|^2=3,\qquad
\langle|F'|^2\rangle=3\bigl(L/(2\pi)\bigr)^2.
\]
All Fourier projections are in the periodic Sobolev space \(H^1\), so Parseval and the ensuing inequalities remain valid without smoothness.

## Proof

Decompose the mean-zero real vector function as \(F=F_1+F_2+R\), where \(F_j\) is the orthogonal projection onto Fourier frequency \(j\), and \(R\) consists of all frequencies at least three. Let
\[
a=\langle|F_1|^2\rangle,\quad b=\langle|F_2|^2\rangle,\quad c=\langle|R|^2\rangle,\quad
U=\langle F_1F_1^{\mathsf T}\rangle,\quad K=\langle F_2F_2^{\mathsf T}\rangle,\quad H=\langle RR^{\mathsf T}\rangle.
\]
Orthogonality and the design identity give \(U+K+H=I_3\) and \(a+b+c=3\). Both \(U\) and \(K\) are positive semidefinite of rank at most two. Consequently \(a\le2\). Define the nonnegative spectral excess
\[
\varepsilon=3\bigl(L/(2\pi)\bigr)^2-6.
\]
By Parseval and the minimum frequency in the tail,
\[
6+\varepsilon=\langle|F'|^2\rangle\ge a+4b+9c
=6+3(2-a)+5c.
\tag{1}
\]
In particular \(3(2-a)+5c\le\varepsilon\), \(c\le\varepsilon/5\), and \((2-a)+c\le\varepsilon/3\).

Write \(F_2(u)=\sqrt2\,(C\cos2u+D\sin2u)\) with vectors \(C,D\in\mathbb R^3\). Then \(K=CC^{\mathsf T}+DD^{\mathsf T}\), \(b=|C|^2+|D|^2\), and the fourth-frequency sinusoidal amplitude of \(|F_2|^2\) is
\[
A_4=\sqrt{(|C|^2-|D|^2)^2+4(C\cdot D)^2}=\lambda_1(K)-\lambda_2(K)=b-2\lambda_2(K),
\tag{2}
\]
where the ordered eigenvalues of \(K\) are \(\lambda_1\ge\lambda_2\ge\lambda_3=0\). Choose any two-dimensional subspace \(W\subset\mathbb R^3\) containing the range of \(U\). Taking traces of \(K+H=I_3-U\) on \(W\) yields \(\operatorname{tr}_W K\le2-a\). The minimum trace of a rank-at-most-two positive matrix on a two-plane equals its second eigenvalue; hence \(\lambda_2(K)\le\operatorname{tr}_W K\le2-a\). Combining with (1) and (2),
\[
A_4\ge b-2(2-a)=1-(2-a)-c\ge1-\varepsilon/3.
\tag{3}
\]

The product \(|F_1+F_2|^2\) has fourth Fourier harmonic precisely the one in \(|F_2|^2\), because \(|F_1|^2\) has frequencies zero and two and \(F_1\cdot F_2\) has frequencies one and three. Let \(B=F_1+F_2\). As \(|F|^2=3\), the fourth Fourier component of \(|B|^2\) is canceled by the fourth component of \(2B\cdot R+|R|^2\). The amplitude of the fourth harmonic of a real integrable scalar function \(g\) is \(2|\langle g\,e^{-4iu}\rangle|\), which is bounded by \(2\langle|g|\rangle\). Cauchy--Schwarz, \(\langle|B|^2\rangle=3-c\), and (1) imply
\[
A_4\le 4\sqrt{(3-c)c}+2c
\le4\sqrt{3\varepsilon/5}+2\varepsilon/5.
\tag{4}
\]
Combining (3) and (4) gives
\[
1\le\frac{11}{15}\varepsilon+4\sqrt{\frac{3\varepsilon}{5}}.
\tag{5}
\]
The right side is strictly increasing for \(\varepsilon\ge0\). Its unique nonnegative equality point is
\[
\varepsilon_0=\frac{1245-180\sqrt{47}}{121}=0.0907617514695\ldots>0.
\]
Thus \(\varepsilon\ge\varepsilon_0\). Substitution into the definition of \(\varepsilon\) gives the advertised bound, since \((6+\varepsilon_0)/3=(1971-180\sqrt{47})/363\). This proves the theorem.

## Verification

The standalone program `verify.py` reproduces the exact radical identity in rational arithmetic (by checking a squared polynomial and the positive root condition), the lower-bound comparison, and deterministic numerical tests of the Fourier-covariance lemma using positive-semidefinite matrices with two-dimensional frequency subspaces. It is run with `python3 verify.py` in the same directory. The proof above, not the finite tests, establishes the universal quantifiers.

## Relationship to prior work

King and Mixon, *Short spherical t-design curves* (arXiv:2607.15386; publicly posted July 16, 2026), prove the general spectral length bound. Their specialization to degree two on \(S^2\) is \(L\ge2\pi\sqrt2\), and their study proposes an unproved candidate optimizer; their Theorem 9 asymptotic even-dimensional estimate derives from the same spectral bound. The new inequality instead uses both \(|F|^2=3\) and the rank-two structure of the first two Fourier bands to give an explicit uniform positive gap in the first nonsaturating sphere dimension. Ehler, *Optimal asymptotic bounds for design curves on manifolds* (arXiv:2611.01895; November 1, 2026), concerns the related asymptotic length problem.

## Limitations

No optimality of the new numerical constant is claimed, and no minimizer is identified. The bound may be improved by using additional Fourier constraints. The result concerns exact degree-two designs with arclength weighting, not approximate designs, arbitrary non-arclength weights, or higher-strength designs. Historical originality remains subject to comprehensive independent literature review; a relevant primary PDF could not be obtained in full through available access, although its indexed theorem statements and relevant sections were examined.

## References

1. E. J. King and D. G. Mixon, *Short spherical t-design curves*, arXiv:2607.15386 (first posted 2026-07-16), https://arxiv.org/abs/2607.15386 .
2. M. Ehler, *Optimal asymptotic bounds for design curves on manifolds*, arXiv:2611.01895 (first posted 2026-11-01), https://arxiv.org/abs/2611.01895 .
3. M. Ehler and K. Gröchenig, *t-design curves and mobile sampling on the sphere*, arXiv:2306.13152 (first posted 2023-06-19), https://arxiv.org/abs/2306.13152 .
