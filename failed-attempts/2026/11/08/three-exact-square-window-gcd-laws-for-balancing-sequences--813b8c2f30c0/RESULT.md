# Three exact square-window GCD laws for balancing sequences

## Finding

Let \(B_0=0,B_1=1\), \(C_0=1,C_1=3\), and \(c_0=-1,c_1=1\). For each of these three sequences \(X\), every subsequent term satisfies \(X_{n+2}=6X_{n+1}-X_n\). For each positive integer \(k\), define the infinite sliding-square GCD
\[
\mathcal G_X(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}X_{n+j}^{\,2}\right),
\]
using the nonnegative GCD convention. **For every integer \(k\ge1\)** the following simultaneous, exact formulas hold:
\[
\boxed{\displaystyle
\mathcal G_B(k)=\begin{cases}
\gcd(k,B_k),&k\text{ odd},\\[2pt]
\frac12\gcd(k,B_k),&k\text{ even},
\end{cases}\quad
\mathcal G_C(k)=\gcd(k,B_k),\quad
\mathcal G_c(k)=\begin{cases}
\gcd(k,3B_k),&k\text{ odd},\\[2pt]
\gcd(k,B_k),&k\text{ even}.
\end{cases}}
\]
In particular, these formulas prove both numerical relations for the squared balancing and Lucas-balancing families and for the squared Lucas-balancing and Lucas-cobalancing families reported in Mbirika--Schrader--Spilker, Question 30: \(\mathcal G_B(k)=\mathcal G_C(k)/2\) for even \(k\) and \(\mathcal G_B(k)=\mathcal G_C(k)\) for odd \(k\); moreover \(\mathcal G_c(k)=3\mathcal G_C(k)\) precisely when \(k\equiv3\pmod6\), and the two are equal otherwise.

## Assumptions and scope

All indices are ordinary integer indices, with \(n\ge0\) for starting positions and \(k\ge1\) for window lengths. The sequence \(B\) is the standard balancing sequence, \(C\) its Lucas-balancing companion, and \(c\) the Lucas-cobalancing sequence with the stated \(c_0=-1\) convention. The formula makes no claim about the squared cobalancing sequence \(b\), which obeys an inhomogeneous recurrence. An expression such as \(\gcd(k,B_k)\) is a fully specified finite integer operation, not a prime-factorization-free closed product.

## Proof

**1. Algebraic identities and strong divisibility.** Let \(u=3+2\sqrt2\) and \(u^{-1}=3-2\sqrt2\). The recurrence and initial values give
\[
B_n=\frac{u^n-u^{-n}}{4\sqrt2},\qquad C_n=\frac{u^n+u^{-n}}2.
\]
These expressions imply
\[
C_n^2-8B_n^2=1,\qquad B_{2n}=2B_nC_n,\qquad
B_{2n+1}=2B_nC_{n+1}+1,
\]
and the difference identities, for all integer \(a\ge0\) and \(k\ge1\),
\[
B_{a+2}-B_a=2C_{a+1},\qquad C_{a+2k}-C_a=16B_kB_{a+k}.
\]
The standard addition relation \(B_{r+s}=B_rB_{s+1}-B_{r-1}B_s\) for \(r\ge1,s\ge0\) and the elementary fact \(\gcd(B_j,B_{j+1})=1\) imply \(\gcd(B_r,B_s)=B_{\gcd(r,s)}\) for positive \(r,s\), by the Euclidean algorithm. Hence
\[
\gcd_{n\ge0} B_{t+2n}=B_{\gcd(t,2)}=\begin{cases}1,&t\text{ odd},\\6,&t\text{ even}.
\end{cases}
\]
The Lucas-cobalancing Binet form \(c_j=((1+\sqrt2)^{2j-1}-(1+\sqrt2)^{-(2j-1)})/2\) holds for all \(j\ge0\). It yields, along with the preceding identities,
\[
B_j^2=\frac{C_{2j}-1}{16},\qquad
C_j^2=\frac{C_{2j}+1}{2},\qquad
c_j^2=\frac{C_{2j-1}-1}{2}\quad(j\ge1).
\]

**2. Replace an infinite GCD by two explicit integers.** Set \(S_X(n)=\sum_{j=1}^kX_{n+j}^2\). The elementary identity \(\gcd_{n\ge0} S_X(n)=\gcd(S_X(0),S_X(1)-S_X(0),S_X(2)-S_X(1),\ldots)\) follows by successive subtraction. The identities in Step 1, telescoped over \(j=1,\ldots,k\), give
\[
S_B(0)=\frac{B_kC_{k+1}-k}{16},\quad
S_C(0)=\frac{B_kC_{k+1}+k}{2},\quad
S_c(0)=\frac{B_kC_k-k}{2}.
\]
For every \(n\ge0\), the consecutive differences are, respectively,
\[
S_B(n+1)-S_B(n)=B_kB_{2n+k+2},
\]
\[
S_C(n+1)-S_C(n)=8B_kB_{2n+k+2},\qquad
S_c(n+1)-S_c(n)=8B_kB_{2n+k+1}.
\]
Strong divisibility therefore reduces the three target GCDs *exactly* to
\[
\begin{aligned}
\mathcal G_B(k)&=\gcd\left(\frac{B_kC_{k+1}-k}{16},\ (6\text{ if }2\mid k\text{ else }1)B_k\right),\\
\mathcal G_C(k)&=\gcd\left(\frac{B_kC_{k+1}+k}{2},\ (48\text{ if }2\mid k\text{ else }8)B_k\right),\\
\mathcal G_c(k)&=\gcd\left(\frac{B_kC_k-k}{2},\ (8\text{ if }2\mid k\text{ else }48)B_k\right).
\end{aligned}
\]
All displayed quotients are integers by the preceding sum identities.

**3. Congruence facts.** The recurrences immediately give \(B_m\equiv m\pmod{16}\) for odd \(m\), and
\[
C_m\equiv\begin{cases}1\pmod{16},&m\text{ even},\\3\pmod{16},&m\text{ odd}.\end{cases}
\]
For the first fact, use \(B_1=1\), \(B_{m+2}-B_m=2C_{m+1}\), and \(C_{m+1}\equiv1\pmod{16}\) for odd \(m\). Also \(B_m\) is odd exactly when \(m\) is odd. Writing even \(k=2^am\) with \(a\ge1\) and odd \(m\), repeated doubling gives
\[
B_k=2^a B_m\prod_{j=0}^{a-1}C_{2^jm},\qquad \nu_2(B_k)=a=\nu_2(k).
\]
The product is \(3\pmod{16}\). Since \(B_m\equiv m\pmod{16}\), the numerators in Step 2 have the exact valuations
\[
\nu_2(B_kC_{k+1}-k)=a+3,\quad
\nu_2(B_kC_{k+1}+k)=a+1,\quad
\nu_2(B_kC_k-k)=a+1.
\]
Consequently, for even \(k\), the initial sums \(S_B(0),S_C(0),S_c(0)\) have \(2\)-adic valuations \(a-1,a,a\), respectively.

For the prime \(3\), the recurrences modulo \(3\) yield \(3\mid B_k\) whenever \(k\) is even, \(3\nmid B_k\) whenever \(k\) is odd, and \(3\mid C_{k+1}\) for even \(k\). The triple-angle identity
\[
B_{3t}=B_t(4C_t^2-1)=B_t(3+32B_t^2)
\]
shows that if \(t\) is even, then \(\nu_3(B_{3t})=\nu_3(B_t)+1\), since \(3\mid B_t\) and \(3+32B_t^2\) is divisible by \(3\) but not \(9\). Factoring even \(k\) into its \(3\)-power and a still-even part gives
\[
\nu_3(B_k)\ge\nu_3(k)+1,\qquad
\nu_3(B_kC_{k+1})\ge\nu_3(k)+2.
\]
Thus for even \(k\) the three initial sums in Step 2 all have \(3\)-adic valuation precisely \(\nu_3(k)\). Finally, modulo \(3\) the sequence \(c_j\) always equals \(\pm1\), so \(c_j^2\equiv1\pmod3\) and \(S_c(0)\equiv k\pmod3\).

**4. Prime-by-prime determination of the three GCDs.** For an odd prime \(p\) dividing \(B_k\), each initial-sum numerator in Step 2 is congruent to either \(k\) or \(-k\) modulo every power of \(p\) dividing \(B_k\); the denominators \(2\) and \(16\) are invertible. Hence the \(p\)-part of the GCD equals the \(p\)-part of \(\gcd(k,B_k)\), except potentially for the additional factor \(3\) in the difference GCD. At even \(k\), Step 3 shows the initial sum has \(3\)-adic valuation \(\nu_3(k)\), so even the extra factor \(3\) does not enlarge the result. At odd \(k\), \(3\nmid B_k\), and the factor \(3\) occurs only in the Lucas-cobalancing difference GCD; because \(S_c(0)\equiv k\pmod3\), it contributes exactly one factor \(3\) when \(3\mid k\). For odd \(k\), the initial sums for \(C\) and \(c\) are odd (each term in those sequences is odd), so their difference GCDs contribute no power of \(2\); the \(B\) difference GCD equals the odd integer \(B_k\). For even \(k\), Step 3 gives the exact \(2\)-adic valuations of the initial sums as \(\nu_2(k)-1,\nu_2(k),\nu_2(k)\), while the respective difference GCDs have strictly larger valuations. Thus their GCDs have precisely these powers of \(2\). These exhaustive prime comparisons establish all three formulas.

## Verification

The standalone standard-library Python 3 program `verify_balancing_square_gcd.py` checks all three GCD identities directly from recurrence-generated sequence terms for every \(1\le k\le260\), using 48 consecutive starting positions per case, and checks the algebraic identities and applicable dyadic/ternary valuations. Its actual execution output is in `verification_output.txt`. The program uses exact integers, not floating point. The 48-start computation is a regression check only; Step 2 supplies the proof that the infinite GCD reduces to the stated finite difference GCD.

## Relationship to prior work

Mbirika, Schrader, and Spilker (2023), Section 6.1, Question 30, asks for formulas for consecutive-square GCDs of the balancing, Lucas-balancing, cobalancing, and Lucas-cobalancing sequences. The paper reports the two relationships proved here only as Mathematica observations, and supplies direct formulas for squared Pell and associated Pell sequences but not these three families. The present result makes the two observations rigorous and gives one explicit finite GCD formula for each of three of the four requested families. Mbirika and Spilker (2022) study squared sliding-window GCDs for recurrence \(G_{n+2}=G_{n+1}+G_n\) with arbitrary initial conditions; that theorem does not directly apply to these \(6,-1\) recurrence families. Fiebig, Mbirika, and Spilker (2024) study Lucas-sequence periods, entry points, and modular patterns, not this three-sequence squared-window GCD formula.

## Limitations

The result does **not** supply a prime-factorization-free evaluation of \(\gcd(k,B_k)\) for arbitrary \(k\); the broader question of a gcd-free closed product remains open here. The analogous formula for squared cobalancing numbers is outside scope. The present review is not an independent audit. The literature comparisons are bounded and an equivalent unindexed or later result may exist. No claim of universal priority is made.

## References

1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4. First public arXiv version, January 13, 2023: https://arxiv.org/abs/2301.05758 ; full published paper: https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf . See Definitions 6--7 and Section 6.1, Question 30.
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, first public version April 26, 2022: https://arxiv.org/abs/2204.12626 . The generalized Fibonacci recurrence there is different from the present recurrence.
3. Morgan Fiebig, aBa Mbirika, and Jürgen Spilker, *Period patterns, entry points, and orders in the Lucas sequences: theory and applications*, first public version August 26, 2024: https://arxiv.org/abs/2408.14632 .
