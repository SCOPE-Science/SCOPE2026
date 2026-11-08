# Exact ternary valuation spectra of ternary Fuss–Catalan numbers

## Finding

For each integer \(r\ge0\), define the nonnegative-integer-valued ternary Fuss–Catalan counts \(C_n\) and their valuation polynomial \(P_r\) by

\[
C_n=\frac{1}{2n+1}\binom{3n}{n},\qquad
P_r(t)=\sum_{n=0}^{3^r-1}t^{\nu_3(C_n)}.
\]

The **full exact distribution**, simultaneously at every depth, has the rational bivariate generating function

\[
\boxed{\sum_{r\ge0}P_r(t)z^r=\frac{1-tz}{1-2(1+t)z+(1+t+t^2)z^2}.}
\]

In particular, \(P_0=1\), \(P_1=2+t\), and, for \(r\ge2\),

\[
P_r(t)=2(1+t)P_{r-1}(t)-(1+t+t^2)P_{r-2}(t).
\]

The first polynomials are

\[
\begin{aligned}
P_2(t)&=3+5t+t^2,\\
P_3(t)&=4+13t+9t^2+t^3,\\
P_4(t)&=5+26t+35t^2+14t^3+t^4.
\end{aligned}
\]

The number of indices \(n<3^r\) for which \(3\nmid C_n\) is \(r+1\); exactly one index has maximal valuation \(r\), and none has a higher valuation. For a uniformly chosen \(0\le n<3^r\), put \(V_r=\nu_3(C_n)\). Its exact mean and variance are

\[
\boxed{\mathbb E V_r=\frac r2-\frac14+\frac{1}{4\cdot3^r}},\qquad
\boxed{\operatorname{Var}(V_r)=\frac r6+\frac{1-3^{-2r}}{16}}.
\]

As \(r\to\infty\), the normalized valuation obeys the central limit law

\[
\frac{V_r-r/2}{\sqrt{r/6}}\ \xrightarrow{\ d\ }\ \mathcal N(0,1).
\]

## Assumptions and scope

The index \(n\) runs through all nonnegative integers less than the integer power \(3^r\), with \(r\in\mathbb Z_{\ge0}\). Here \(\nu_3\) is the usual additive valuation of a nonzero integer. All \(C_n\) are positive integers. The indeterminates \(t,z\) are formal for the rational-series identity. Probabilistic statements take \(n\) uniformly in the indicated finite interval. No assertion is made about other primes or about shorter intervals.

## Proof

**1. Valuation in ternary digits.** Let \(s_3(m)\) denote the sum of the ternary digits of \(m\). Legendre's formula \(\nu_3(m!)=(m-s_3(m))/2\), together with \(s_3(3n)=s_3(n)\), gives

\[
\nu_3\binom{3n}{n}=\frac{s_3(2n)}2,\qquad
\nu_3(C_n)=\frac{s_3(2n)}2-\nu_3(2n+1).
\]

Write \(j=\nu_3(2n+1)\) and \(2n+1=3^j(2a+1)\), where \(a\ge0\) is an integer and \(a\not\equiv1\pmod3\). This is a unique parametrization: the quotient \(2a+1\) is positive, odd, and prime to three. Because

\[
2n=3^j(2a)+(3^j-1),
\]

and the final \(j\) ternary digits of \(3^j-1\) are all \(2\), the two summands occupy disjoint ternary digit positions. Consequently

\[
s_3(2n)=s_3(2a)+2j,\qquad
\boxed{\nu_3(C_n)=\frac{s_3(2a)}2.}
\]

For \(0\le n<3^r\), the unique parameters obey \(0\le j\le r\) and \(0\le a<3^{r-j}\). Conversely, each such \((j,a)\) with \(a\not\equiv1\pmod3\) supplies exactly one \(n=(3^j(2a+1)-1)/2\) in the required interval. In the degenerate case \(r-j=0\) this means only \(a=0\), as required. Therefore, defining

\[
G_s(t)=\sum_{\substack{0\le a<3^s\\a\not\equiv1\pmod3}}
  t^{s_3(2a)/2},\qquad G_0(t)=1,
\]

we have \(P_r(t)=\sum_{s=0}^rG_s(t)\) and hence \(\sum_{r\ge0}P_r(t)z^r=(1-z)^{-1}\sum_{s\ge0}G_s(t)z^s\).

**2. Finite-state doubling and exact rationality.** Work temporarily with a formal variable \(q\) satisfying \(q^2=t\). Doubling \(a\) in base three from least to most significant digit has carries \(0,1\). A digit \(d=0,1,2\) with incoming carry \(c\) produces output digit congruent to \(2d+c\) modulo three, weighted by \(q\) to the power of that output digit, and outgoing carry \(\lfloor(2d+c)/3\rfloor\). Summing the weights over all three possible input digits yields the exact transition matrix

\[
M(q)=\begin{pmatrix}1+q^2&q\\q&1+q^2\end{pmatrix}.
\]

The excluded residue \(a\equiv1\pmod3\) requires that the least significant input digit be either \(0\) or \(2\), contributing the initial row \(u(q)=(1,q)\). At the end of the \(s\) input digits the remaining carry contributes the final column \(u(q)^{\mathsf T}\). Thus for every \(s\ge1\),

\[
G_s(q^2)=u(q)M(q)^{s-1}u(q)^{\mathsf T}.
\]

The matrix has eigenvalues \(\lambda_\pm=1+q^2\pm q\). Direct inversion of \(I-zM(q)\), or diagonalization, gives

\[
\sum_{s\ge0}G_s(q^2)z^s
 =1+zu(q)(I-zM(q))^{-1}u(q)^{\mathsf T}
 =\frac{(1-z)(1-q^2z)}{1-2(1+q^2)z+(1+q^2+q^4)z^2}.
\]

Divide by \(1-z\) and replace \(q^2\) with \(t\) to prove the stated generating function as a formal identity. The matrix expression is manifestly a polynomial in integer digit weights; hence all coefficient counts are nonnegative integers despite the subtractive recurrence.

**3. Extremal frequencies.** The generating identity at \(t=1\) yields \(P_r(1)=3^r\) as a consistency check. At \(t=0\), it reduces to \((1-z)/(1-2z+z^2)=(1-z)^{-1}\), whose \(z^r\) coefficient is \(r+1\). The recurrence and induction show \(\deg P_r=r\) with leading coefficient \(1\): it holds for \(r=0,1\), and for \(r\ge2\) the coefficient of \(t^r\) is twice the leading coefficient of \(P_{r-1}\) minus that of \(P_{r-2}\), namely \(2-1=1\). Thus there are exactly \(r+1\) valuation-zero indices, one valuation-\(r\) index and none with valuation greater than \(r\).

**4. Exact moments and Gaussian asymptotics.** For \(t\) in a complex neighborhood of one, choose the analytic square root taking value one at \(t=1\). Partial fractions in \(z\) give

\[
P_r(t)=\frac{1+t^{-1/2}}2\,(1+t+\sqrt t)^r
       +\frac{1-t^{-1/2}}2\,(1+t-\sqrt t)^r.
\]

Differentiate at \(t=1\) and divide by \(P_r(1)=3^r\). Using the standard identities \(\mathbb{E}[V_r]=P_r'(1)/P_r(1)\) and \(\mathbb{E}[V_r(V_r-1)]=P_r''(1)/P_r(1)\), simplification yields the exact displayed mean and variance, including \(r=0\).

For the limiting law, set \(t=e^w\), where \(w\) is small and complex, and note that the second eigenvalue is exponentially smaller than the first. The logarithm of the normalized moment-generating function satisfies, uniformly for \(w\) in a sufficiently small fixed neighborhood of zero,

\[
\log\frac{P_r(e^w)}{3^r}
=r\log\!\left(\frac{1+e^w+e^{w/2}}3\right)
+\log\!\left(\frac{1+e^{-w/2}}2\right)
+O(\rho^r |w|),\quad 0<\rho<1.
\]

Here the analytic expansion of the first logarithm is \(w/2+w^2/12+O(w^3)\). Substituting \(w=i\theta\sqrt{6/r}\), removing the centering phase \(i\theta(r/2)\sqrt{6/r}\), and letting \(r\to\infty\) yields the characteristic-function limit \(e^{-\theta^2/2}\), uniformly for each fixed real \(\theta\). Lévy's continuity theorem proves the stated Gaussian convergence.

## Verification

The accompanying standard-library script `verify_ternary_fuss_3adic.py` computes ternary Fuss–Catalan valuations by both a separate factorial-valuation method and the derived digit formula. It compares the full histogram with the rational-recurrence coefficients for every \(0\le r\le9\), covering \(29{,}524\) index tests, and also checks \(150\) exact large binomial integers plus the displayed moment formulas. Run `python3 verify_ternary_fuss_3adic.py` from the directory containing this document. The resulting checks are finite corroboration, not a replacement for the all-depth proof above.

## Relationship to prior work

Barat and Grabner studied the distribution of binomial coefficients across the full Pascal triangle, developing general tools for digital block functions. Their enumerated objects and theorem statements are distinct from the single-index ternary Fuss–Catalan valuation polynomials and their precise limiting law here. Classical Legendre/Kummer digit formulas are used, not presented as new. Krattenthaler and Müller's work on prime-power congruences of Fuß–Catalan coefficients provides an algorithmic coefficient-level theory and already describes small valuation layers; it does not state the all-depth bivariate histogram or its precise moments. OEIS A003462 already identifies exactly which ternary Fuss–Catalan indices give valuation zero; that previously known component is explicitly not claimed as novel. The prime-two and prime-three carry transformations are structurally different; no cross-prime substitution supplies the present theorem.

## Limitations

The claim is restricted to the ternary Fuss–Catalan family, the prime three, and initial intervals of length a power of three. The Gaussian assertion is an asymptotic distribution of valuation under uniform index sampling, not a normal approximation uniform across all tails. Exact small-depth counts and the verifier are not certificates of the infinite statement. While the specific all-depth formula was not identified in the inspected primary literature and data sources, unlocated equivalent work remains a historical-priority risk. Independent mathematical validation has not been performed.

## References

1. Guy Barat and Peter J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, Journal of the London Mathematical Society 64 (2001), 523–547, DOI 10.1112/S0024610701002630; author-hosted full text: https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf ; verified public online record: https://www.cambridge.org/core/journals/journal-of-the-london-mathematical-society/article/abs/distribution-of-binomial-coefficients-and-digital-functions/59BEA01A925CA294F5A691D50F634A75 .
2. C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(p^k\) behaviour of recursive sequences*, arXiv:1508.02580v1 (2015); full journal text: https://link.springer.com/article/10.1007/s00010-025-01195-0 .
3. OEIS A001764, ternary Fuss–Catalan enumeration: https://oeis.org/A001764 .
4. OEIS A003462, historical nondivisibility observation dated January 14, 2003: https://oeis.org/A003462 .
5. Classical factorial valuation identity of Legendre and carry criterion of Kummer (used as standard antecedents).
