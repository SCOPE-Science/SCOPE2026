# Complete coefficient positivity for cubic exponential Padé denominators

## Finding

Let \(q_{k,m}\) be the denominator, normalized by \(q_{k,m}(0)=1\), of the \([k/m]\) Padé approximant of \(e^z\). **For every integer \(k\ge0\), all coefficients of the Maclaurin expansion of \(q_{k,3}^{-1}\) are strictly positive:**

\[
\frac1{q_{k,3}(z)}=\sum_{n=0}^{\infty}c_n(k,3)z^n,
\qquad c_n(k,3)>0\quad(n\ge0).
\]

This settles the entire cubic-denominator case of the coefficient-positivity question motivated by Fasi and Higham's Conjecture 3.2, including nondiagonal Padé approximants. The result includes a strict, explicit, pole-residue lower bound valid simultaneously for every coefficient order. The result does **not** assert the original conjecture for all odd denominator degrees: counterexamples for denominator degree five were published in 2026.

## Assumptions and scope

Throughout \(k,n\) are arbitrary nonnegative integers. Put \(t=k+1\ge1\) and

\[
q_{k,3}(z)=1-\frac{3}{t+2}z+\frac{3}{(t+1)(t+2)}z^2-\frac{1}{t(t+1)(t+2)}z^3.
\]

The formula uses the standard exponential Padé normalization, with exact scalar arithmetic. The coefficient statement is about the power series at the origin, not about matrix-entrywise positivity or finite-precision evaluation. For \(k=0\) the result includes the reciprocal of the cubic Taylor polynomial of \(e^{-z}\).

Let \(u\) denote the unique positive solution of \(u^3+3tu=2t\), and define

\[
R=t+u,\quad v=\sqrt{3t+\tfrac34u^2},\quad Z=t-\tfrac12u+iv,
\quad s=|Z|,\quad d=|R-Z|.
\]

Then \(1/2<u<2/3\), the zeros of \(q_{k,3}\) are \(R,Z,\overline Z\), and \(s>R\).

## Proof

**1. Exact cubic root geometry.** Multiplying the denominator by \(t(t+1)(t+2)\) and translating \(z=t+x\) gives

\[
t(t+1)(t+2)q_{k,3}(t+x)=2t-3tx-x^3.
\]

The increasing cubic \(x^3+3tx\) takes values below \(2t\) at \(x=1/2\), because \(1/8+3t/2<2t\) for \(t\ge1\), and above \(2t\) at \(x=2/3\), because \(8/27+2t>2t\). Therefore \(1/2<u<2/3\). Factoring the depressed cubic yields the three simple zeros stated above. Direct calculation gives

\[
s^2-R^2=3t(1-u)>0,
\qquad d^2=3(t+u^2)>0.
\]

**2. Exact residues.** Because \(q_{k,3}(0)=1\), the factorization is

\[
q_{k,3}(z)=(1-z/R)(1-z/Z)(1-z/\overline Z).
\]

Its partial fractions can be written

\[
\frac1{q_{k,3}(z)}=\frac A{1-z/R}+\frac B{1-z/Z}
  +\frac{\overline B}{1-z/\overline Z},
\]

where

\[
A=\frac{s^2}{d^2}>0,\qquad
B=\frac{R\overline Z}{(R-Z)(\overline Z-Z)},
\qquad 2|B|=\frac{Rs}{vd}.
\]

Thus \(A>2|B|\) is equivalent to \(sv>Rd\).

**3. Uniform strict residue dominance.** Squaring positive quantities and expanding yields

\[
\begin{aligned}
s^2v^2-R^2d^2
&=\frac94\left[t(1-u)(4t+u^2)-u^2(t+u)^2\right]\\
&=\frac{9u^4(1-u)}{4(2-3u)^2}
\left(u^3-4u^2+10u-4\right),
\end{aligned}
\]

where the last equality uses \(t=u^3/(2-3u)\). The factor \(1-u\) is positive. The cubic \(f(u)=u^3-4u^2+10u-4\) satisfies \(f(1/2)=1/8\) and \(f'(u)=3u^2-8u+10>0\) for all real \(u\) (its quadratic discriminant is negative). Hence every factor on the right is positive. Therefore \(sv>Rd\) and \(A>2|B|\).

**4. Every Taylor coefficient.** Expanding the three geometric series, permissible near the origin, gives for every \(n\ge0\)

\[
\begin{aligned}
c_n(k,3)&=AR^{-n}+2\operatorname{Re}(BZ^{-n})\\
&\ge R^{-n}\left(A-2|B|(R/s)^n\right)\\
&\ge R^{-n}(A-2|B|)>0.
\end{aligned}
\]

This includes \(n=0\) and every higher coefficient without an index cutoff. As a quantitative corollary, \(R^nc_n(k,3)\to A\) as \(n\to\infty\), since \(R/s<1\). No finite calculation is needed for the universal conclusion.

## Verification

The standalone standard-library program `verify.py` computes exact rational recurrence coefficients using

\[
c_0=1,\qquad
c_n=\frac{3}{t+2}c_{n-1}
-\frac{3}{(t+1)(t+2)}c_{n-2}
+\frac{1}{t(t+1)(t+2)}c_{n-3},
\]

with negative-index coefficients set to zero. It compares exact rational coefficients for many \(k,n\) and samples the explicit root/residue inequality; execute `python verify.py` to obtain `VERIFY_OK`. These finite tests check the algebra only. The proof of strict positivity for **all** \(k,n\) is the symbolic residue-dominance argument above. The program has no nonstandard dependencies.

## Relationship to prior work

Fasi and Higham (2019, Conjecture 3.2) proposed positivity of all coefficients of \(q_{k,m}^{-1}\) for odd \(m\). Scardino (first public arXiv version October 28, 2026) proves positivity when \(k=0\), and positivity sufficiently far in the coefficient index under a spectral-minimality condition. That work supplies counterexamples at odd denominator degrees five, seven and nine and a general Hermite-limit mechanism; its statements do not give complete coefficient positivity for every \(k,n\) at fixed \(m=3\). Its general partial-fraction identity is compatible with the present argument, whose additional ingredient is **uniform dominance of the real-pole residue over the combined moduli of the two complex residues**. Classical cubic root calculations alone do not imply that inequality.

For context, the published degree-five counterexample \(c_{38}(66,5)<0\), combined with the trivial degree-one case and the present theorem, places the first possible odd-denominator failure at degree five. This observation is an implication of existing work plus the stated cubic theorem, not a separate new claim. General prior-art completeness has not been independently certified.

## Limitations

No assertion is made for denominator degrees other than three; the broad odd-degree conjecture is false. Strict coefficient positivity does not imply entrywise positivity of matrix Padé approximants or guarantee numerical stability. For large \(k\), the residue gap \(A-2|B|\) is positive but the relative gap tends to zero; the bound is not proposed as a floating-point evaluation algorithm. Historical priority against an unlocated equivalent cubic reciprocal-series identity remains a risk. Independent review has not been conducted.

## References

1. M. Fasi and N. J. Higham, "An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential," *SIAM Journal on Matrix Analysis and Applications* **40** (2019), 1233–1256, Conjecture 3.2. https://doi.org/10.1137/18M1228876
2. F. Scardino, "On a positivity conjecture of Fasi and Higham for Padé approximants to the matrix exponential," arXiv:2610.39051v1, first posted 2026-10-28. https://arxiv.org/abs/2610.39051
