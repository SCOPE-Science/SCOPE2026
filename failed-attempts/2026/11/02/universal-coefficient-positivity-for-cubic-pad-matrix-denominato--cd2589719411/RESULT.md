# Universal coefficient positivity for cubic Padé matrix denominators

## Finding

For every integer \(k\geq0\), let \(q_{k,3}\) be the normalized denominator of the \([k/3]\) Padé approximant to the exponential. Then **every** coefficient of its reciprocal is strictly positive:
\[
\frac1{q_{k,3}(z)}=\sum_{n=0}^{\infty}c_n(k)z^n,
\qquad c_n(k)>0\quad(k,n\in\mathbb Z_{\ge0}).
\]
More quantitatively, the unique positive pole \(R\) is the pole of smallest modulus, and the proof gives an explicit strict bound \(c_n(k)\ge(A-2|B|)R^{-n}>0\), with \(A,B,R\) defined below. This settles the cubic-denominator, all-numerator-degree case of the reciprocal-positivity question for exponential Padé approximants.

A direct matrix-function consequence is that, for any finite entrywise-nonnegative real matrix \(X\), the series representing \(q_{k,3}(X)^{-1}\) converges **exactly** when \(\rho(X)<R\). Throughout this range the inverse is entrywise nonnegative, and it is strictly positive if \(X\) is irreducible. At \(\rho(X)=R\), the denominator matrix is singular.

## Assumptions and scope

The Padé denominator is normalized by \(q_{k,3}(0)=1\) and has the explicit form
\[
q_{k,3}(z)=1-\frac{3z}{k+3}
+\frac{3z^2}{(k+3)(k+2)}
-\frac{z^3}{(k+3)(k+2)(k+1)}.
\]
Here \(k,n\) range independently over all nonnegative integers, while \(z\) is complex within the Taylor disk. Matrices in the corollary are finite square real matrices with nonnegative entries; \(\rho\) is spectral radius. The matrix statement applies to the **denominator inverse**, not automatically to arbitrary Padé numerators or to matrices with signed entries.

For comparison with numerical matrix-function algorithms, \(k=3+p\), \(p\ge0\), is precisely the \([3+p/3]\) denominator degree appearing in Padé-based matrix \(\varphi\)-function recovery. The associated 2025 numerical work explicitly classifies its preprint under MSC 65F60 and derives backward errors using these rational denominators.

## Proof

**1. An exact cubic root reduction.** Put \(t=k+1\ge1\) and \(d=t(t+1)(t+2)\). Direct multiplication gives
\[
-dq_{k,3}(z)=z^3-3tz^2+3t(t+1)z-t(t+1)(t+2).
\]
Substituting \(z=t+w\) reduces the root equation to
\[
w^3+3tw-2t=0.
\]
This strictly increasing real cubic has a unique real solution \(r\), and its values at \(1/2\) and \(2/3\) have opposite signs. Consequently
\[
\tfrac12<r<\tfrac23,\qquad t=\frac{r^3}{2-3r}.
\]
Factoring the depressed cubic gives the three distinct poles
\[
R=t+r,\qquad W=t-\tfrac r2+ib,\qquad\overline W,
\qquad b^2=3t+\tfrac34r^2>0.
\]
The squared distances satisfy
\[
|W|^2=t^2-tr+3t+r^2,\quad |W-R|^2=3(t+r^2),
\quad |W|^2-R^2=3t(1-r)>0.
\]
Thus \(R>0\) is the unique nearest pole and the Taylor radius is exactly \(R\).

**2. A uniform residue-majorization inequality.** Because \(q(0)=1\), factor
\[
\frac1{q_{k,3}(z)}=\frac{1}{(1-z/R)(1-z/W)(1-z/\overline W)}
=\frac{A}{1-z/R}+\frac{B}{1-z/W}+\frac{\overline B}{1-z/\overline W}.
\]
Evaluation at the simple poles gives
\[
A=\frac{|W|^2}{|W-R|^2}>0,
\qquad |B|=\frac{R|W|}{2b|W-R|}.
\]
It therefore suffices to prove \(|W|b>R|W-R|\). The exact squared difference is
\[
\begin{split}
|W|^2b^2-R^2|W-R|^2
&=\frac{9r^4(1-r)}{4(2-3r)^2}
\left(r^3-4r^2+10r-4\right).
\end{split}
\]
The factor in parentheses is positive for \(r\in(1/2,2/3)\): its derivative is \(3r^2-8r+10>0\) on the real line, and its value at \(r=1/2\) is \(1/8\). Every other factor is strictly positive. This establishes \(A>2|B|\).

**3. Positivity for every Taylor order.** Partial fractions and \(|W|>R\) now yield, for each \(n\ge0\),
\[
\begin{aligned}
c_n(k)&=AR^{-n}+2\operatorname{Re}(BW^{-n})\\
&\ge AR^{-n}-2|B||W|^{-n}\\
&\ge(A-2|B|)R^{-n}>0.
\end{aligned}
\]
The first inequality is a triangle bound, and the second uses \(|W|>R\). This is an infinite-order proof; finite coefficient calculations are not needed for the conclusion.

**4. Positive matrix inverse and exact convergence boundary.** Let \(X\ge0\) entrywise. For \(\rho(X)<R\), standard matrix power-series convergence gives
\[
q_{k,3}(X)^{-1}=\sum_{n=0}^{\infty}c_n(k)X^n\ge0
\]
entrywise. For irreducible \(X\), every ordered pair of indices is connected by a positive power, so each entry of this sum is strictly positive. Conversely, the nonnegative Perron eigenvector for \(\rho(X)\ge R\), together with \(c_n(k)\ge(A-2|B|)R^{-n}\), shows that the matrix series cannot converge. If \(\rho(X)=R\), Perron–Frobenius also gives a positive eigenvalue at a zero of \(q_{k,3}\), hence \(q_{k,3}(X)\) is singular. This proves the sharp radius assertion.

## Verification

Run `python3 verify.py` with SymPy installed. The verifier independently checks the cubic shift, exact residue-factor identity, the positive polynomial derivative and endpoint, thousands of exact-rational reciprocal recurrence identities and strictly positive coefficients across a finite test grid, and small nonnegative matrix inverses. A successful result reports `VERIFY_OK 15914 exact checks, with symbolic cubic and residue identities`. The all-integer and all-order conclusions follow from the displayed proof, **not** from numerical enumeration.

The coefficient recurrence, useful for independent checks, is \(c_0=1\), \(c_n=0\) for \(n<0\), and
\[
c_n=\frac{3}{t+2}c_{n-1}
-\frac{3}{(t+2)(t+1)}c_{n-2}
+\frac1{t(t+1)(t+2)}c_{n-3},\quad n\ge1.
\]

## Relationship to prior work

The 2025 preprint by Al-Mohy and Liu develops scaling/recovery for matrix \(\varphi\)-functions, with the \([m+p/m]\) exponential Padé denominator as a central numerical component; its first version lists MSC 65F60 as primary. This work motivates the numerical-matrix interpretation, but its analysis concerns approximation and backward error, not coefficientwise positivity of the cubic reciprocal.

Fasi and Higham's 2019 paper explicitly poses reciprocal-denominator positivity for odd denominator degree as Conjecture 3.2. The degree-one case is immediate, whereas the present proof establishes the degree-three case for **every** numerator degree. A subsequent preprint by Scardino (posted October 28, 2026) proves positivity for numerator degree zero, and eventual positivity subject to a spectral condition, while exhibiting counterexamples for denominator degree five. The latter results do not imply the all-order, all-\(k\), degree-three statement proved here. Standard partial-fraction decompositions and Perron–Frobenius theory are used as tools, not claimed as new.

## Limitations

The claim concerns the inverse normalized cubic **denominator**, not positivity of the full rational matrix exponential approximation for arbitrary matrices, error constants, stability with rounding, or odd degrees above three. The matrix corollary requires entrywise nonnegativity and a spectral-radius restriction. An older equivalent special-case identity could exist in historical Padé polynomial or linear-recurrence literature; the originality comparison is limited to the sources named below and searchable research records.

## References

1. A. H. Al-Mohy and X. Liu, *Computing Matrix \(\varphi\)-Functions Arising in Exponential Integrators*, arXiv:2506.01193v1, first publicly submitted June 1, 2025. https://arxiv.org/html/2506.01193v1
2. M. Fasi and N. J. Higham, *An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential*, SIAM J. Matrix Anal. Appl. **40** (2019), 1233–1256; Conjecture 3.2. https://eprints.maths.manchester.ac.uk/2721/1/fahi19.pdf
3. F. Scardino, *On a Positivity Conjecture of Fasi and Higham for Padé Approximants to the Matrix Exponential*, arXiv:2610.39051v1, posted October 28, 2026. https://arxiv.org/html/2610.39051v1
4. K. A. Driver and N. M. Temme, *Asymptotics and Zero Distribution of Padé Polynomials Associated with the Exponential Function*, J. Comput. Appl. Math. **89** (1998), 97–114. https://ir.cwi.nl/pub/108
