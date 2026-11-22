# Exact dyadic valuation distribution for the five-ary Fuss–Catalan numbers

## Finding
For every integer \(n\ge0\), let the five-ary Fuss–Catalan integer be
\[
C_5(n)=\frac{1}{4n+1}\binom{5n}{n},\qquad V(n)=\nu_2(C_5(n)).
\]
For every integer \(L\ge0\), put \(P_L(u)=\sum_{n=0}^{2^L-1}u^{V(n)}\), with \(u\) a formal indeterminate. The **complete exact valuation distribution for every dyadic block** is
\[
\boxed{\sum_{L\ge0}P_L(u)z^L=\frac{(1-uz)(1+z+(2-u)z^2+z^3)}{D(z,u)}},
\]
where
\[
\begin{aligned}
D(z,u)={}&1-(1+u)z+(-1+u+u^2-u^3)z^3\\
&+(-1+u-u^2+u^3-u^4)z^4+(u+u^4)z^5.
\end{aligned}
\]
All coefficients are exact nonnegative integers. For example,
\[
\begin{aligned}
P_0(u)&=1,\quad P_1(u)=2,\quad P_2(u)=4,\\
P_3(u)&=6+u+u^3,\\
P_4(u)&=9+3u+2u^3+2u^4.
\end{aligned}
\]
For \(N_L\) uniform on \(\{0,\ldots,2^L-1\}\), write \(X_L=V(N_L)\). Its mean is exactly
\[
\boxed{\mathbb E X_L=\frac L2-1+\frac{1+(-1)^{\lfloor L/2\rfloor}}{2^{L+1}}}\quad(L\ge0).
\]
Moreover,
\[
\boxed{\operatorname{Var}(X_L)=\frac{21}{20}L+O(1)},\qquad
\boxed{\frac{X_L-L/2}{\sqrt{21L/20}}\xrightarrow{\ d\ }\mathcal N(0,1)}.
\]
The rational identity specifies the entire distribution, not just the first moments.

## Assumptions and scope
All indices \(n,L\) are nonnegative integers. The denominator \(4n+1\) is odd and the Fuss–Catalan quotient is integral; the valuation is therefore finite. The generating-function identity holds formally in \(\mathbb Z[u][[z]]\); \(L\to\infty\) only in the limit law. It concerns contiguous initial dyadic index intervals, not arbitrary translated intervals, other primes or other Fuss orders. The count of zero-valuations (odd terms) was determined in prior work and is not claimed as new here.

## Proof
**1. A finite carry computation valid at every index.** Legendre's digit-sum formula, with \(s_2\) the binary one-count, yields
\[
V(n)=s_2(n)+s_2(4n)-s_2(5n)=2s_2(n)-s_2(5n).
\]
By Kummer's theorem, this equals the total number of outgoing carries, counted separately at each binary column, in adding \(n+4n\). Write \(n=\sum_{i=0}^{L-1}b_i2^i\), with \(b_i=0\) outside \(0\le i<L\). With \(b_{-1}=b_{-2}=0\), incoming carry \(c_0=0\), and \(c_i\in\{0,1\}\), the exact recurrence is
\[
c_{i+1}=\left\lfloor\frac{b_i+b_{i-2}+c_i}{2}\right\rfloor,
\quad V(n)=\sum_{i\ge0}c_{i+1}.
\]
All carries vanish after four additional zero input bits. No uncounted final carry is permitted.

**2. Eight-state transfer.** Before reading bit \(b_i\), use state \((x,y,c)=(b_{i-2},b_{i-1},c_i)\), initially \((0,0,0)\). On input \(b\in\{0,1\}\), put \(d=\lfloor(b+x+c)/2\rfloor\); the new state is \((y,b,d)\), with weight \(u^d\). Order the states lexicographically as
\[
(000),(001),(010),(011),(100),(101),(110),(111).
\]
The transfer matrix is
\[
M(u)=\begin{pmatrix}
1&0&1&0&0&0&0&0\\
1&0&0&u&0&0&0&0\\
0&0&0&0&1&0&1&0\\
0&0&0&0&1&0&0&u\\
1&0&0&u&0&0&0&0\\
0&u&0&u&0&0&0&0\\
0&0&0&0&1&0&0&u\\
0&0&0&0&0&u&0&u
\end{pmatrix}.
\]
Flushing four zero bits gives the terminal-weight column
\[
t(u)=(1,1,1,1,1,u,1,u^2)^{\mathsf T}.
\]
Therefore, for every \(L\ge0\), exactly
\[
P_L(u)=e_{000}^{\mathsf T}M(u)^L t(u),\qquad
\sum_{L\ge0}P_L(u)z^L=e_{000}^{\mathsf T}(I-zM(u))^{-1}t(u).
\]
The final equality is a formal series identity, so neither convergence nor extrapolation is involved.

**3. An exact algebraic identity.** Direct polynomial elimination of \((I-zM)q=t\) gives the stated numerator and denominator. For a coefficientwise certificate, the accompanying `verify.py` stores eight explicit integer-polynomial numerators \(Q_i(z,u)\) and \(D(z,u)\) and checks, by exact integer arithmetic, the polynomial identity
\[
(I-zM)Q=D\,t
\]
for all eight coordinates. Its first coordinate equals exactly \((1-uz)(1+z+(2-u)z^2+z^3)\). Since \(D(0,u)=1\), formal division by \(D\) is valid and uniquely proves the asserted rational series for every \(L\). This is an exact symbolic certificate, not evidence based on matching finitely many coefficients.

**4. Exact mean.** Differentiating the proved series at \(u=1\) gives
\[
\sum_{L\ge0}P'_L(1)z^L
=\frac{z^3(3z-4)}{(z-1)(2z-1)^2(z^2+1)}.
\]
As \(P_L(1)=2^L\), partial fractions (or coefficient comparison) yield
\[
P'_L(1)=2^L\left(\frac L2-1\right)+\frac{1+(-1)^{\lfloor L/2\rfloor}}2.
\]
Division by \(2^L\) proves the exact mean formula, including \(L=0\).

**5. Variance and Gaussian law.** At \(u=1\), the characteristic polynomial of \(M\) is
\[
\det(\lambda I-M(1))=\lambda^3(\lambda-2)(\lambda-1)(\lambda+1)(\lambda^2+1).
\]
Thus the real eigenvalue \(2\) is simple and strictly dominates all other eigenvalues, whose absolute values are at most one. For \(u\) complex near one, analytic perturbation of this isolated eigenvalue gives a unique analytic \(\lambda(u)\) with \(\lambda(1)=2\) and a coefficient \(A(u)\) analytic and nonzero at one, such that \(P_L(u)=A(u)\lambda(u)^L+O(\rho^L)\) uniformly near one for some \(1<\rho<2\). The exact nonzero eigenvalue factor is
\[
\begin{aligned}
F(\lambda,u)={}&\lambda^5-(1+u)\lambda^4
-(u^3-u^2-u+1)\lambda^2\\
&-(u^4-u^3+u^2-u+1)\lambda+(u^4+u).
\end{aligned}
\]
At \((\lambda,u)=(2,1)\), implicit differentiation gives \(\lambda'(1)=1\) and \(\lambda''(1)=8/5\). For \(\psi(t)=\log(\lambda(e^t)/2)\), therefore \(\psi'(0)=1/2\) and \(\psi''(0)=21/20>0\). Since \(P_L(1)=2^L\), the cumulant generating function equals \(L\psi(t)+\log A(e^t)+o(1)\), uniformly and analytically for \(t\) near zero. It follows that \(\mathbb E X_L=L/2+O(1)\) and \(\operatorname{Var}(X_L)=21L/20+O(1)\). Evaluating the characteristic function at \(t=is/\sqrt{21L/20}\), subtracting the center \(L/2\), and using the Taylor expansion of \(\psi\) gives limit \(e^{-s^2/2}\). Lévy's continuity theorem proves the stated normal limit.

## Verification
Run `python3 verify.py` using Python 3 and no third-party libraries. The verifier checks the exact eight-coordinate polynomial identity \((I-zM)Q=D t\), and independently checks all valuation histograms over \(0\le n<2^L\) for every \(0\le L\le15\) by direct binary digit counts, with direct factorial/binomial computations at small indices. The output is `VERIFY_OK symbolic_polynomial_certificate=yes finite_histogram_lengths=16 factorial_checks=127`. These finite checks are corroboration; the recurrence and polynomial identity constitute the unrestricted proof. The eigenvalue derivatives can also be checked by direct differentiation of the displayed polynomial \(F\).

## Relationship to prior work
Sobolewski (2023) studies regularity of prime-adic valuations and final nonzero digits in the analytic setting, giving the contemporary number-theoretic motivation; it does not provide a five-ary Fuss–Catalan exact valuation histogram or the constants here. The classical digit-sum/Kummer identity and the use of transfer matrices are not new. A separate published five-ary Fuss–Catalan classification explicitly determines exactly which values are odd and the corresponding maximal even-run lengths; those results provide the \(u=0\) case, but they do not supply the full bivariate generating function or the nonzero valuation strata. A published ternary Fuss–Catalan theorem contains a complete analogous dyadic valuation histogram, with a different factor \(\binom{3n}{n}\) and Gaussian variance coefficient \(11/12\); it is neither algebraically identical to the five-ary case nor a stronger universal Fuss-order theorem. Earlier general modular-computation methods for recursive sequences can compute selected fixed-modulus questions, but do not state this explicit all-scale joint histogram and \(21/20\) variance. No priority claim is made for the known odd-support count or for general finite-state and spectral methods.

## Limitations
The claimed exact rational identity and Gaussian variance are specific to the five-ary sequence at the prime two, on initial dyadic index blocks. The normal limit is weak convergence, without a quantitative rate or local limit theorem. A previously unindexed formula in digit-carry or Fuss–Catalan literature could still match these conclusions; full global priority is not certified. Computational replay does not constitute independent mathematical auditing.

## References
1. B. Sobolewski, *On k-regularity of sequences of valuations and last non-zero digits*, Ramanujan Journal 61 (2023), 1151–1195; first public journal date 2023-04-06, DOI:10.1007/s11139-023-00710-8, primary MSC 11A63. https://link.springer.com/article/10.1007/s11139-023-00710-8
2. *Exact binary zero-run spectrum of the five-ary Fuss–Catalan numbers*, published research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-binary-zero-run-spectrum-of-the-five-ary-fuss-catalan-numb--74e266357ef1/RESULT.md
3. *Exact dyadic two-adic valuation spectra of ternary Fuss-Catalan numbers*, published research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-exact-dyadic-two-adic-valuation-spectra-of-ternary-fuss-catalan--02997d82d076/RESULT.md
4. M. Kauers, C. Krattenthaler, T. W. Müller, *A method for determining the mod-\(2^k\) behaviour of recursive sequences, with applications to subgroup counting* (2012), Section 13 (fixed-power congruences). https://www.algebra.uni-linz.ac.at/people/mkauers/publications/kauers12.pdf
5. E. E. Kummer, classical theorem on prime-adic binomial valuations (1852); the digit-carry step is classical, not newly claimed.
