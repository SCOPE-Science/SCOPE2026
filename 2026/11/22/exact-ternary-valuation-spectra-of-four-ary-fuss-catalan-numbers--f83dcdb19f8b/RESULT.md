# Exact ternary valuation spectra of four-ary Fuss–Catalan numbers

## Finding

For every integer \(n\ge0\), the four-ary Fuss–Catalan number is
\[
C_4(n)=\frac{1}{3n+1}\binom{4n}{n}\in\mathbb Z_{>0}.
\]
For every \(r\ge0\), define the complete valuation enumerator
\[
P_r(t)=\sum_{0\le n<3^r}t^{\nu_3(C_4(n))}.
\]
Then the following rational generating function is an exact identity of formal power series over \(\mathbb Z[t]\):
\[
\boxed{\sum_{r\ge0}P_r(t)z^r=\frac{(1-tz)(1+(1-t)z-z^2)}{D(t,z)},}
\]
where
\[
\boxed{D(t,z)=1-2(1+t)z+(-1+4t-t^2)z^2
 +(1+t+t^2+t^3)z^3-t(1+t+t^2)z^4.}
\]
Thus the coefficient of \(t^j\) in \(P_r\) is exactly the number of indices with valuation \(j\), simultaneously for every \(r,j\ge0\).

For a uniformly chosen integer \(n\) from \(0\le n<3^r\), let \(V_r=\nu_3(C_4(n))\). Its exact mean and variance are
\[
\boxed{\mathbb E V_r=\frac{r-1}{2}+\frac{1+(-1)^r}{4\cdot3^r},}
\]
\[
\boxed{\operatorname{Var}(V_r)=\frac{2r}{3}-\frac34+
 \frac{5+3(-1)^r}{8\cdot3^r}-\frac{(1+(-1)^r)^2}{16\cdot9^r}.}
\]
Moreover,
\[
\frac{V_r-r/2}{\sqrt{2r/3}}\ \xrightarrow{\ d\ }\mathcal N(0,1)
\qquad (r\to\infty).
\]
For \(r\ge2\), the maximum valuation is exactly \(r\). Write \(e_r=[t^r]P_r(t)\) for the number of maximizers. The multiplicities obey
\[
\boxed{\sum_{r\ge2}e_rz^r=\frac{z^2(2-z)}{1-2z-z^2+z^3}},
\]
so \(e_2,e_3,e_4,e_5,e_6=2,3,8,17,39\), and \(e_r=2e_{r-1}+e_{r-2}-e_{r-3}\) for \(r\ge5\). This sharply differs from the single maximal-valuation index in the ternary-arity comparison family.

## Assumptions and scope

All indices are nonnegative integers, \(r\ge0\), and \(\nu_3\) is the exact exponent of the prime three in a nonzero integer. The polynomial variable \(t\) is formal; \(z\) marks ternary index length. Probabilities use the uniform distribution over exactly \(3^r\) indices, not over arbitrary initial intervals. The endpoint \(r=0\) consists of \(n=0\) alone. The exponent-zero counts are consequences of previously known no-carry digit conditions and are not claimed independently as new.

## Proof

**1. Kummer and the high-end carry.** Since \(3n+1\equiv1\pmod3\), Kummer's carry theorem gives
\[
\nu_3(C_4(n))=\nu_3\binom{4n}{n}
 =\text{number of carries when adding \(n\) and \(3n\) in base three}.
\]
Write \(n=\sum_{i=0}^{r-1}a_i3^i\), with digits \(a_i\in\{0,1,2\}\) and leading zero digits permitted. Set \(a_{-1}=0\) and \(c_0=0\). The ordinary addition recursion is
\[
\begin{aligned}
 b_i&=a_i+a_{i-1}+c_i,\\
 c_{i+1}&=\lfloor b_i/3\rfloor\in\{0,1\},\\
 \nu_3(C_4(n))&=\sum_{i=0}^{r-1}c_{i+1}
  +\lfloor(a_{r-1}+c_r)/3\rfloor.
\end{aligned}
\]
Here for \(r=0\), the last term is stipulated zero. The last displayed carry is essential: after the \(r\) input digits, the high digit of \(3n\) is \(a_{r-1}\), and the incoming carry can produce exactly one further carry. No more digits contribute. These formulas hold for every \(r,n\) in the scope.

**2. Six-state transfer and rational identity.** Order the six states \((a_{i-1},c_i)\) as
\((0,0),(0,1),(1,0),(1,1),(2,0),(2,1)\).
Give each input choice \(a_i\) weight \(t^{c_{i+1}}\) and transition to \((a_i,c_{i+1})\). Summing over the three input digits gives
\[
M(t)=\begin{pmatrix}
1&0&1&0&1&0\\
1&0&1&0&0&t\\
1&0&1&0&0&t\\
1&0&0&t&0&t\\
1&0&0&t&0&t\\
0&t&0&t&0&t
\end{pmatrix}.
\]
The initial row vector is \(u=(1,0,0,0,0,0)\); the terminal column is \(v(t)=(1,1,1,1,1,t)^{\mathsf T}\), since only state \((2,1)\) yields the final carry. Therefore
\[
P_r(t)=uM(t)^rv(t),\qquad
\sum_{r\ge0}P_r(t)z^r=u(I-zM(t))^{-1}v(t).
\]
The identity follows by straightforward integer-polynomial expansion of the \(6\times6\) determinant and numerator of the indicated matrix resolvent; explicitly,
\(\det(I-zM(t))=D(t,z)\) and the indicated scalar numerator is
\((1-tz)(1+(1-t)z-z^2)\). This is an exact finite symbolic identity, and the matrix is sufficient to reconstruct it without relying on numerical coefficient matching. At \(t=1\), the resulting series equals \((1-3z)^{-1}\), confirming \(P_r(1)=3^r\).

**3. Moments.** Differentiate the rational generating function at \(t=1\) to obtain the exact factorial-moment generating series:
\[
\sum_{r\ge0}P_r'(1)z^r
=\frac{z^2(3z-5)}{(z-1)(z+1)(3z-1)^2},
\]
\[
\sum_{r\ge0}P_r''(1)z^r
=-\frac{2z^2(6z^4-17z^3+6z^2-z+2)}{(z-1)^2(z+1)^2(3z-1)^3}.
\]
Partial-fraction expansion yields
\[
P_r'(1)=\frac{r-1}{2}\,3^r+\frac{1+(-1)^r}{4}
\]
and
\[
P_r''(1)=\frac{r(3r-4)}{12}\,3^r+
 \frac{(2r+1)+(2r-1)(-1)^r}{8}.
\]
Since \(\mathbb E V_r=P_r'(1)/3^r\) and
\(\operatorname{Var}(V_r)=(P_r''(1)+P_r'(1))/3^r-(P_r'(1)/3^r)^2\), the two exact formulas follow.

**4. Highest valuation and its exact multiplicity.** In the addition in step 1, \(c_1=0\); at most the remaining \(r-1\) input positions and the final position can carry. Thus \(\nu_3(C_4(n))\le r\) for \(r\ge1\). When \(r\ge2\), choosing every ternary digit equal to two attains \(r\) carries. For any path attaining the maximum, the carry at input digit \(1\) must be one and all subsequent carries must remain one, with a final carry. The initial adjacent-digit condition is \(a_0+a_1\ge3\); subsequent digit pairs must satisfy \(a_{i-1}+a_i\ge2\), and the final input digit must be two. Hence, for \(r\ge2\), the exact maximizer count is
\[
e_r=\mathbf1^{\mathsf T}BA^{r-2}e_2,
\quad B=\begin{pmatrix}0&0&0\\0&0&1\\0&1&1\end{pmatrix},
\quad A=\begin{pmatrix}0&0&1\\0&1&1\\1&1&1\end{pmatrix},
\quad e_2=\begin{pmatrix}0\\0\\1\end{pmatrix}.
\]
Because \(\det(\lambda I-A)=\lambda^3-2\lambda^2-\lambda+1\), exact inversion of \(I-zA\) gives the stated extremal generating function and recurrence. For \(r=1\) all three values have valuation zero; the stated maximal law is intentionally restricted to \(r\ge2\).

**5. Gaussian law.** The nonnegative matrix \(M(1)\) is irreducible and aperiodic: each state reaches \((0,0)\), which has a self-loop and reaches every other state. Its characteristic polynomial gives one simple dominant eigenvalue \(3\) and all remaining eigenvalues of modulus at most one. By analytic perturbation of this isolated eigenvalue, \(P_r(e^w)\) has an analytic exponential representation \(c(w)\lambda(e^w)^r(1+O(\rho^r))\) for \(w\) in a small complex neighborhood of zero, with \(0<\rho<1\) and \(c(0)=1\). The derivatives of its logarithm at zero, computed from the exact moment identities above, have asymptotic first coefficient \(1/2\) and second coefficient \(2/3\). Taylor expansion with \(w=i\theta/\sqrt{2r/3}\) then gives convergence of the centered characteristic functions to \(e^{-\theta^2/2}\). Levy's continuity theorem proves the displayed normal limit. The finite variance formula is not by itself the proof of this limit; spectral separation supplies the required control of higher cumulants.

## Verification

Run `python3 verify.py` (Python standard library only). It independently computes each ternary addition carry count for every \(n<3^r\) through \(r=9\), compares with the six-state transfer histogram, and checks the rational generating identity by exact polynomial convolution. It also compares factorial valuations of actual binomial integers for small indices, factorial-exponent computations at very large indices, the exact moment formulas, and the extremal recurrence. Expected output: `VERIFY_OK checks=29824 depths=0..9 max_depth=9`. These tests are finite corroboration of the fully stated proof, not infinite certificates.

Illustrative initial polynomials are
\[
P_0=1,\quad P_1=3,\quad P_2=6+t+2t^2,\quad
P_3=14+2t+8t^2+3t^3.
\]

## Relationship to prior work

Kummer's valuation theorem and Stănică's archival work provide carry and divisibility tools. Stănică's arity \(p^q\) investigations include arity four at the prime two, not the present prime-three, arity-four complete valuation histogram. Sury's 2009 prime-arity result and Krattenthaler–Müller's prime-power-arity congruence results similarly do not provide this all-depth enumerator. The closest published prime-relative Fuss–Catalan study includes **exactly this arity and prime** as the specialization \(p=3\) but determines only valuation-zero indices and their p-adic dimension. Its digit inequality is the zero-weight shadow of the present more informative six-state, carry-weighted transfer. A published ternary valuation spectrum for **ternary arity three** has a different rational generating function, variance \(r/6+O(1)\), and a unique maximal valuation index; these do not imply the present arity-four spectrum, variance \(2r/3+O(1)\), or its nontrivial extremal multiplicities. Barat–Grabner's general digital-block methods motivate the analytic approach but concern different Pascal-triangle counting problems and do not state the explicit present matrix, rational function, exact moments, or extremal law.

## Limitations

The classification concerns precisely the \(3\)-adic valuations of the four-ary Fuss–Catalan numbers over full ternary index intervals. It does not determine their unit residues, arbitrary shorter-interval histograms, or all other primes. The leading variance coefficient and normal limit are asymptotic as \(r\to\infty\), not an error-controlled normal approximation for every tail. The valuation-zero criterion and general Kummer digit method are prior knowledge, not novel components. Originality is a best-effort statement about inspected sources; unlocated equivalent formulas or generic carry specializations remain a historical-priority risk. No independent mathematical audit has been performed.

## References

1. P. Stănică, *\(p^q\)-Catalan Numbers and Squarefree Binomial Coefficients*, arXiv:math/0010148v1 (first public 2000-10-15), https://arxiv.org/abs/math/0010148 .
2. G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, Journal of the London Mathematical Society 64 (2001), 523–547, author manuscript https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf .
3. B. Sury, *Generalized Catalan Numbers: Linear Recursion and Divisibility*, Journal of Integer Sequences 12 (2009), Article 09.7.5, https://cs.uwaterloo.ca/journals/JIS/VOL12/Sury/sury31.pdf .
4. M. Kauers, C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(2^k\) behaviour of recursive sequences, with applications to subgroup counting*, arXiv:1107.2015 (first public 2011-07-11), https://arxiv.org/abs/1107.2015 .
5. C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(p^k\) behaviour of recursive sequences*, arXiv:1508.02580 (2015), journal open text https://link.springer.com/article/10.1007/s00010-025-01195-0 .
6. *Prime-relative Fuss–Catalan nondivisibility: exact spectra and p-adic dimension*, publicly available result at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-prime-relative-fuss-catalan-nondivisibility-exact-spectra-and-p--fca5ba9f3d60 .
7. *Exact ternary valuation spectra of ternary Fuss–Catalan numbers*, publicly available result at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-ternary-valuation-spectra-of-ternary-fuss-catalan-numbers--38f9bdc99cfd .
