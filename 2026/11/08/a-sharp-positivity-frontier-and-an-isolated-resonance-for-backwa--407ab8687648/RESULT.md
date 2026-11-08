# A sharp positivity frontier and an isolated resonance for backward-Euler-started BDFL32

## Finding
For the three-step, second-order BDFL32 formula applied with a constant step to the positive scalar decay equation, two backward-Euler startup steps yield **strict positivity at every subsequent index if and only if** the dimensionless decay step obeys \(0\le r\le 15/16\) **or** \(r=3\). For every \(r>15/16\) other than \(3\), the numerical sequence has infinitely many positive and infinitely many negative terms. At the isolated step \(r=3\) the entire numerical sequence is exactly \(4^{-n}\), even though all nearby steps above \(15/16\) eventually lose positivity.

This all-index classification concerns positivity of a generated trajectory, not the standard absolute-stability criterion of a multistep method. It exhibits an isolated cancellation of the dominant oscillatory modes in an otherwise sign-changing regime.

## Assumptions and scope
Let \(\lambda>0\), \(h\ge0\), \(r=h\lambda\), and \(y(0)=1\) for \(y'=-\lambda y\). For \(h=0\), the recurrence is understood algebraically with \(r=0\). Put \(d=1+3r/5\). The fixed-step BDFL32 recurrence is
\[
dy_{n+3}=\frac32y_{n+2}-\frac35y_{n+1}+\frac1{10}y_n,\qquad n=0,1,2,\ldots,
\]
with **two backward-Euler startup steps** \(y_0=1\), \(y_1=(1+r)^{-1}\), and \(y_2=(1+r)^{-2}\). All quantities and conclusions are exact real arithmetic. BDFL32 is also called BDF2OPT(4) in earlier numerical-flow work; the method itself is not claimed new.

## Proof
**1. Root geometry.** The characteristic polynomial is
\[p_d(z)=dz^3-\tfrac32z^2+\tfrac35z-\tfrac1{10}.\]
Its discriminant is \(-27(5d^2-14d+10)/500<0\), since the quadratic factor is strictly positive for every real \(d\). Thus there is exactly one real simple root \(s>0\), and the remaining roots form a nonreal conjugate pair \(z=u+iv,\overline z\), with \(v>0\). Because \(p_d(0)<0\), \(p_d(1)=d-1\ge0\), we have \(0<s\le1\).

Define
\[Q=15s^2-6s+1,\quad D=5s^2-4s+1,\quad T=8s^2-4s+1,\quad N=10s^2-5s+1,\quad H=Q-4s^3.\]
The characteristic equation yields \(10ds^3=Q\) and \(H=6s^3(1+r)>0\). By Vieta,
\[\rho^2:=|z|^2=\frac{s^2}{Q},\qquad u=\frac{s(6s-1)}{2Q},\qquad v^2=\frac{3s^2T}{4Q^2}.\]
All \(Q,D,T,N,7s^2-2s+1\) are strictly positive for real \(s\), by their negative quadratic discriminants and positive leading coefficients. The modulus ordering \(\rho\le s\) is equivalent to \(Q\ge1\), and therefore to \(s\ge2/5\) for \(0<s\le1\). Since \(p_d(2/5)=3(16r-15)/1250\) and the real root is unique, \(s\ge2/5\) if and only if \(r\le15/16\). Thus the real root dominates exactly on the claimed interval.

**2. Exact residue dominance below the frontier.** Write \(t=(1+r)^{-1}=6s^3/H\). Since the roots are distinct, unique coefficients \(A\in\mathbb R\) and \(B\in\mathbb C\) satisfy
\[y_n=As^n+2\operatorname{Re}(Bz^n),\quad n\ge0.\]
Solving the three startup equations gives
\[
A=\frac{t^2-2ut+\rho^2}{s^2-2su+\rho^2}
 =\frac{(7s^2-2s+1)N^2}{3DH^2}>0.
\]
The remaining startup equations say \(2\Re B=1-A\) and \(2v\Im B=(1-A)u-(t-As)\). Eliminating \(B\) using these equalities and \(v^2=3s^2T/(4Q^2)\) yields
\[
A^2-4|B|^2=-\frac{(7s^2-2s+1)N^2P_{12}(s)}{3D^2TH^4},
\]
where
\[
\begin{aligned}
P_{12}(s)={}&24000s^{12}-146400s^{11}+393500s^{10}-616752s^9\\
&+627756s^8-439920s^7+219004s^6-78528s^5\\
&+20235s^4-3668s^3+444s^2-32s+1.
\end{aligned}
\]
To prove \(P_{12}(s)<0\) throughout \([2/5,1]\), let \(x=(5s-2)/3\). The Bernstein coefficients of \(-P_{12}(2/5+3x/5)\) in the degree-12 basis \(\binom{12}{j}x^j(1-x)^{12-j}\), \(0\le j\le12\), are, in order,
\[
\begin{gathered}
7443/78125,\ 66879/390625,\ 6964047/21484375,\ 68301756/107421875,\\
27477198/21484375,\ 2251386/859375,\ 6547437/1203125,\\
78516/6875,\ 825543/34375,\ 68319/1375,\ 27081/275,\ 954/5,\ 360.
\end{gathered}
\]
Every number is strictly positive, so their Bernstein combination is strictly positive for \(0\le x\le1\), including endpoints. Consequently \(A>2|B|\) for \(2/5\le s\le1\). Together with \(\rho\le s\), this gives for every integer \(n\ge0\)
\[y_n\ge As^n-2|B|\rho^n\ge(A-2|B|)s^n>0.\]
This proves sufficiency for every \(r\le15/16\), including the root-modulus tie at the boundary.

**3. Oscillations and the isolated cancellation above the frontier.** If \(r>15/16\), then \(\rho>s\). The coefficient \(B\) vanishes if and only if the first three values already form a pure geometric sequence \(1,t,t^2\) with \(t=s\). Equivalently \(p_d(t)=0\). Direct substitution gives the exact identity
\[p_d((1+r)^{-1})=-\frac{r^2(r-3)}{10(1+r)^3}.\]
For positive \(r\), this is zero only at \(r=3\). At this step, \(t=s=1/4\), so \(y_n=4^{-n}>0\) for all indices.

Otherwise \(B\ne0\). Writing \(z=\rho e^{i\theta}\), with \(0<\theta<\pi\), gives \(y_n=As^n+2|B|\rho^n\cos(n\theta+\phi)\). If \(\theta/(2\pi)\) is irrational, the phases are dense on the circle and the cosine takes signs bounded away from zero infinitely often. If rational, one finite orbit repeats, has mean zero because \(e^{i\theta}\ne1\), and is nonzero at some index; hence it contains a positive and a negative term, repeating infinitely often. Since \((s/\rho)^n\to0\), the real-root contribution cannot prevent either eventual sign subsequence. Thus there are infinitely many strictly negative and strictly positive numerical values for every \(r>15/16\), \(r\ne3\). This completes the equivalence and all boundary cases.

## Verification
The standalone Python 3 checker `verification/verify.py` uses only exact rational polynomial arithmetic. It checks the rational formulas for \(v^2\), \(A\), and \(A^2-4|B|^2\); calculates all 13 degree-12 Bernstein coefficients and verifies their strict positivity with minimum \(7443/78125\); reproduces the exact \(r=3\) resonance through index 100; and confirms first negative iterates at indices 30, 10, and 7 for \(r=1,2,4\) respectively. Run with `python3 verification/verify.py` after extracting both this document and the checker. The infinite-index and irrational-rotation statements follow from the displayed analytic argument, not from the finite tests.

## Relationship to prior work
Jensen, Lóczi and Ketcheson (first public version, October 15, 2026) optimize and analyze BDFL32 for stiff systems and study absolute stability and errors. Vatsa, Carpenter and Lockard (2010) analyze the older equivalent BDF2OPT(4) formula in computational fluid dynamics. Hundsdorfer, Ruuth and Spiteri (2002) develop general monotonicity-preserving multistep theory, with particular older BDF-family illustrations. These sources motivate the positivity question but the inspected portions do not give this fixed-step, backward-Euler-started all-index if-and-only-if classification or the isolated \(r=3\) resonance. General absolute stability does not imply nonnegative iterates; likewise, failure of an unrestricted strong-stability-preserving coefficient condition does not by itself classify one fixed scalar trajectory. Historical overlap remains possible, particularly in older recurrence/positivity literature.

## Limitations
The theorem assumes a scalar homogeneous negative real eigenmode, exact arithmetic, fixed steps, and two *specific* backward-Euler starting values. It does not prove positivity for arbitrary starting values, multidimensional positive systems, nonlinear reactions, spatial discretizations, or finite-precision implementations. The exceptional positive trajectory at \(r=3\) is not robust to perturbing the step or initial values. Search and comparison support a qualified novelty assessment; they do not establish global historical priority. No independent mathematical audit has been performed.

## References
1. T. Jensen, L. Lóczi, D. I. Ketcheson, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1, October 15, 2026, https://arxiv.org/abs/2610.22685 .
2. V. N. Vatsa, M. H. Carpenter, D. P. Lockard, *Re-evaluation of an Optimized Second Order Backward Difference (BDF2OPT) Scheme for Unsteady Flow Applications*, AIAA 2010-0122, https://ntrs.nasa.gov/api/citations/20100002944/downloads/20100002944.pdf?attachment=true .
3. W. Hundsdorfer, S. J. Ruuth, R. J. Spiteri, *Monotonicity-preserving linear multistep methods*, CWI Report MAS-R0210, April 2002, https://ir.cwi.nl/pub/4231/04231D.pdf .
