# Tribonacci enumeration of monic Stern polynomials and a power-saving reciprocal bound

## Finding
For the Stern polynomials \(B_0(t)=0\), \(B_1(t)=1\), \(B_{2n}(t)=tB_n(t)\) and \(B_{2n+1}(t)=B_n(t)+B_{n+1}(t)\), define, for every integer \(k\ge1\),
\[
U_k=\#\{2^{k-1}\le n<2^k:\operatorname{LC}(B_n)=1\},\qquad
V_k=\#\{2^{k-1}\le n<2^k:\ n\text{ odd},\ \operatorname{LC}(B_n)=1\}.
\]
Here \(\operatorname{LC}\) denotes the leading coefficient. Then
\[
\sum_{k\ge1}U_kz^k=\frac{z(1+z)}{1-z-z^2-z^3},\qquad
\sum_{k\ge1}V_kz^k=\frac{z(1-z^2)}{1-z-z^2-z^3}.
\]
Thus \((U_1,U_2,U_3)=(1,2,3)\), \((V_1,V_2,V_3)=(1,1,1)\), and \(U_k=U_{k-1}+U_{k-2}+U_{k-3}\), \(V_k=V_{k-1}+V_{k-2}+V_{k-3}\) for every \(k\ge4\).

Let \(\lambda\) be the real root greater than one of \(x^3-x^2-x-1=0\), and put \(\theta=\log_2\lambda\approx0.8791464216\). For the reciprocal-index set
\[
\mathcal R=\{n\ge1:B_n(t)=t^{\deg B_n}B_n(t^{-1})\},
\]
one has, for every real \(X\ge2\),
\[
\#(\mathcal R\cap[1,X])=O(X^{\theta}).
\]
In particular, \(\mathcal R\) has natural density zero. This is a power-saving bound, not the polylogarithmic bound proposed by Gawron.

## Assumptions and scope
All polynomial coefficients are nonnegative integers. For \(n\ge1\), let \(d(n)=\deg B_{n+1}-\deg B_n\), let \(a(n)\in\{0,1\}\) indicate whether \(B_n\) is monic, and let \(b(n)\in\{0,1\}\) indicate whether \(B_{n+1}\) is monic. The theorem counts leading-coefficient-one polynomials, including the constant polynomial \(B_1=1\); it makes no claim that every monic Stern polynomial is reciprocal. The stated bound is asymptotic as \(X\to\infty\).

## Proof
**1. Exact binary state update.** Set \(s(n)=(d(n),a(n),b(n))\). Because
\(\deg B_{2n}=1+\deg B_n\) and
\(\deg B_{2n+1}=\max(\deg B_n,\deg B_{n+1})\),
\[
 d(2n)=\max(0,d(n))-1,\qquad
 d(2n+1)=1+d(n)-\max(0,d(n)).
\]
From \(d(1)=1\), induction gives \(d(n)\in\{-1,0,1\}\) for all \(n\ge1\). Set
\[
c(d,a,b)=\begin{cases}a,&d=-1,\\0,&d=0,\\b,&d=1.\end{cases}
\]
If the consecutive degrees are distinct, the leading coefficient of their sum equals the leading coefficient of the higher-degree summand. If they coincide, the leading coefficient is a sum of two positive integers, hence is at least two. Therefore the exact state transitions are
\[
 T_0(d,a,b)=(\max(0,d)-1,a,c(d,a,b)),
\quad T_1(d,a,b)=(1+d-\max(0,d),c(d,a,b),b).
\]
They encode \(s(2n)=T_0(s(n))\), \(s(2n+1)=T_1(s(n))\), with \(s(1)=(1,1,1)\). Their reachable states are exactly the ten states in the table below; closure is verified by applying both transitions to each row.

**2. Rational transfer certificate.** Define \(Q(z)=1-z-z^2-z^3\), \(R(z)=(1-z)Q(z)\). For each reachable state \(s\), let \(W_s(z)\) count, by binary-word length, descendants whose first monicity indicator is one, and let \(C_s(z)\) count descendants \(u\) for which the first monicity indicator of \(T_1(u)\) is one:
\[
W_s(z)=a+z\bigl(W_{T_0(s)}(z)+W_{T_1(s)}(z)\bigr),
\]
\[
C_s(z)=c(s)+z\bigl(C_{T_0(s)}(z)+C_{T_1(s)}(z)\bigr).
\]
These are uniquely defined as formal power series (their constant terms are fixed and coefficients are recursively determined). The following table gives **polynomial numerators** \(N_s\) and \(H_s\) with \(W_s=N_s/R\) and \(C_s=H_s/R\):

| \(s=(d,a,b)\) | \(N_s(z)\) | \(H_s(z)\) |
|---|---|---|
| \((-1,0,0)\) | \(0\) | \(0\) |
| \((-1,1,0)\) | \(1-z^2-z^3\) | \(1-z\) |
| \((-1,1,1)\) | \(1-z^2\) | \(1-z+z^2-z^3\) |
| \((0,0,0)\) | \(0\) | \(0\) |
| \((0,0,1)\) | \(z^2\) | \(z-z^2\) |
| \((0,1,0)\) | \(1-z-z^3\) | \(z-z^2\) |
| \((0,1,1)\) | \(1-z+z^2-z^3\) | \(2z-2z^2\) |
| \((1,0,0)\) | \(0\) | \(0\) |
| \((1,0,1)\) | \(z\) | \(1-z\) |
| \((1,1,1)\) | \(1-z^2\) | \(1-z+z^2-z^3\) |

For every row and each of its two transition targets, direct polynomial addition verifies the finite identities
\[
N_s=aR+z(N_{T_0(s)}+N_{T_1(s)}),\qquad
H_s=c(s)R+z(H_{T_0(s)}+H_{T_1(s)}).
\]
These twenty exact polynomial identities are a standalone finite algebraic certificate for the rational generating functions; the included verifier checks all twenty with integer arithmetic. In particular, at \(s_0=(1,1,1)\),
\[
 W_{s_0}(z)=\frac{1+z}{Q(z)},\qquad C_{s_0}(z)=\frac{1+z^2}{Q(z)}.
\]

Every integer in \([2^{k-1},2^k)\) has binary expansion consisting of a leading digit one followed by exactly \(k-1\) binary digits. Thus
\[
 \sum_{k\ge1}U_kz^k=zW_{s_0}(z)=\frac{z(1+z)}{Q(z)}.
\]
For \(k=1\), the only index is the odd monic index \(n=1\). For \(k\ge2\), an odd index has final binary digit one; before that digit there are \(k-2\) unrestricted digits. Hence
\[
 \sum_{k\ge1}V_kz^k=z+z^2C_{s_0}(z)=\frac{z(1-z^2)}{Q(z)}.
\]
Coefficient extraction proves both asserted Tribonacci recurrences and initial values.

**3. Reciprocity and power saving.** For every positive even index, \(B_{2n}(t)=tB_n(t)\) has zero constant term and nonzero leading coefficient, hence cannot equal its reciprocal polynomial. For every positive odd index, the constant term is one, by the recurrence and induction from \(B_1(0)=1\); therefore a reciprocal odd-index polynomial necessarily has leading coefficient one. Consequently the reciprocal indices lie in the odd monic set counted by the \(V_k\).

The positive root \(\lambda\) of \(x^3-x^2-x-1\) lies strictly between one and two. The other two characteristic roots are conjugate with modulus \(\lambda^{-1/2}<1\) (the cubic has only one real root and product of its three roots is one). The exact generating function therefore yields \(V_k=O(\lambda^k)\). If \(X<2^K\), summing \(V_k\) for \(1\le k\le K\) gives \(O(\lambda^K)=O(X^{\log_2\lambda})\), since one can take \(K=\lceil\log_2(X+1)\rceil\). Because \(\lambda<2\), this is a genuine power saving, establishing density zero.

## Verification
Run `python3 verification/verify.py` with Python 3 and no external libraries. The verifier checks all ten reachable states, the twenty rational-transfer numerator identities exactly, Tribonacci block counts through binary length twenty-two, and independently constructs the integer-coefficient Stern polynomials through index \(32768\), comparing their leading-coefficient flags, degree differences and odd-index block totals with the binary-state machine. The proof above, not the finite tests, establishes the unrestricted statement.

## Relationship to prior work
Gawron's 2014 article gives explicit families of reciprocal Stern polynomials, proves a polylogarithmic lower bound for their count, and proposes a polylogarithmic upper bound (Conjecture 4.3). The current result gives an intermediate power-saving upper bound through a complete enumeration of the larger monic set; it does not settle Gawron's conjecture. Schinzel's 2015 article classifies reciprocal Stern polynomials in certain binary forms and gives an algebraic criterion in other forms. The inspected theorem statements do not yield the present exact all-index monicity distribution or an overall reciprocal-index density bound. Schinzel's 2016 chapter expresses leading coefficients through binary expansions. Only the chapter's abstract was accessible; it is a meaningful outstanding historical-priority uncertainty and might offer an alternative route to the monicity count. OEIS A186890 lists reciprocal indices, but not the asserted complete generating functions or power-saving theorem. These comparisons do not certify historical uniqueness.

## Limitations
The reciprocal-index bound may be far from optimal: the conjectured upper order is polylogarithmic, not \(X^\theta\). The exact Tribonacci enumeration applies to the *superset* of monic Stern polynomials, not to the reciprocals themselves. The unread full text of Schinzel's 2016 leading-coefficient chapter leaves a concrete priority risk; no claim is made that its methods are unavailable or inapplicable.

## References
1. M. Gawron, *A note on the arithmetic properties of Stern Polynomials*, arXiv:1401.3553v1 (posted January 15, 2014), especially Section 4, Corollary 4.2 and Conjecture 4.3. https://arxiv.org/pdf/1401.3553
2. A. Schinzel, *Reciprocal Stern Polynomials*, Bulletin of the Polish Academy of Sciences Mathematics 63 (2015), 141–147, DOI:10.4064/ba63-2-4. https://www.impan.pl/shop/en/publication/transaction/download/product/91253
3. A. Schinzel, *The Leading Coefficients of Stern Polynomials*, in *From Arithmetic to Zeta-Functions* (2016), 427–434, DOI:10.1007/978-3-319-28203-9_25 (abstract inspected; full text not obtained).
4. OEIS A186890, indices of self-reciprocal Stern polynomials. https://oeis.org/A186890
