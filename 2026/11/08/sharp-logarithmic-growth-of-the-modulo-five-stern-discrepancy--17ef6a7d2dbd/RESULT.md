# Sharp logarithmic growth of the modulo-five Stern discrepancy

## Finding

Let Stern's diatomic sequence be defined by \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\) for \(n\geq1\). Define, for every integer \(N\geq0\),
\[
\Delta(N)=\#\{0\leq n<N:s(n)\equiv1\pmod5\}-\#\{0\leq n<N:s(n)\equiv4\pmod5\}.
\]
For \(r\geq0\) put \(\ell_r=\min_{0\leq N\leq2^r}\Delta(N)\) and \(u_r=\max_{0\leq N\leq2^r}\Delta(N)\). Then **for every integer \(r\geq16\)**,
\[
\boxed{\ell_{r+12}=\ell_r-4,\qquad u_{r+12}=u_r+4.}
\]
The values \((\ell_r,u_r)\) for the twelve base levels \(r=16,17,\ldots,27\), in order, are
\[
(-4,9),(-4,9),(-5,9),(-5,9),(-5,11),(-5,11),(-6,11),(-6,11),(-6,12),(-6,12),(-8,12),(-8,12).
\]
Together with the initial values below, this is an exact formula for both extrema at **every dyadic scale**. In particular,
\[
\boxed{\max_{0\leq N\leq X}|\Delta(N)|=\frac13\log_2 X+O(1)\qquad(X\to\infty),}
\]
so the residue-one versus residue-four counting discrepancy is unbounded, although it grows only logarithmically. At \(r=24\), explicit witnesses are \(\Delta(2190712)=-6\) and \(\Delta(8693112)=12\).

## Assumptions and scope

The index, prefix length, and dyadic exponent are nonnegative integers. The extrema include the empty prefix \(N=0\) and the full prefix \(N=2^r\). Congruences are in \(\mathbb Z/5\mathbb Z\). No claims are made about discrepancies for other moduli or any finite uniform bound for the individual residue counts.

## Proof

**1. Binary state representation.** Set \(\mathcal P=\{(a,b)\in\mathbb F_5^2:(a,b)\ne(0,0)\}\), which has 24 elements. The coprimality of \(s(n)\) and \(s(n+1)\) ensures that every consecutive-value pair has a residue in \(\mathcal P\). Directly from Stern's recursion, the pair \((s(n),s(n+1))\) transforms upon appending a binary zero or one, respectively, by
\[
L(a,b)=(a,a+b),\qquad R(a,b)=(a+b,b).
\]
Both maps preserve \(\mathcal P\); start from \((0,1)\). In lexicographic order, all binary words of length \(r\), including leading zeros, represent \(n=0,\ldots,2^r-1\) and their first state coordinates are \(s(n)\pmod5\). Put \(w(a,b)=\mathbf1_{a=1}-\mathbf1_{a=4}\).

**2. Exact finite-state extrema.** For each state \(q\in\mathcal P\), let \(S_r(q)\) be the total \(w\)-weight of all length-\(r\) continuations, and \(A_r(q),B_r(q)\) the minimum and maximum of their **prefix sums**, including the empty and full prefixes. At level zero,
\[
S_0(q)=w(q),\quad A_0(q)=\min(0,w(q)),\quad B_0(q)=\max(0,w(q)).
\]
Splitting the ordered words into the \(L\) block followed by the \(R\) block gives, for every \(r\ge0\) and \(q\in\mathcal P\), the exact identities
\[
\begin{aligned}
S_{r+1}(q)&=S_r(Lq)+S_r(Rq),\\
A_{r+1}(q)&=\min\bigl(A_r(Lq),\ S_r(Lq)+A_r(Rq)\bigr),\\
B_{r+1}(q)&=\max\bigl(B_r(Lq),\ S_r(Lq)+B_r(Rq)\bigr).
\end{aligned}
\]
There are no omitted states and no limiting or numerical approximation: these are recurrences for three vectors of 24 integers. In particular, \(\ell_r=A_r(0,1)\) and \(u_r=B_r(0,1)\).

**3. Finite certificate and induction.** Evaluating the displayed recurrences over the 24 explicitly listed states yields three componentwise identities:
\[
\boxed{S_5=S_1,\qquad A_{28}=A_{16}-4\mathbf1,\qquad B_{28}=B_{16}+4\mathbf1.}
\]
Here \(\mathbf1\) is the 24-entry constant-one vector. For additional transparent check data, list the rows of the 5-by-5 tables by first coordinate \(a=0,1,2,3,4\) and the columns by second coordinate \(b=0,1,2,3,4\), with \(*\) denoting the excluded \((0,0)\):

```
S_1 = S_5:
 *   1   0   0  -1
 2   1   1   0   1
 0   0  -1   0   1
 0  -1   0   1   0
-2  -1   0  -1  -1

A_16:
 *  -4  -6  -6  -9
-6  -6  -6  -5  -4
-5  -7  -7  -6  -6
-7  -6  -6  -6  -7
-7  -8  -7  -8  -6

B_16:
 *   9   6   6   4
 7   6   8   7   8
 7   7   6   6   6
 5   6   6   7   7
 6   4   5   6   6
```

The same finite recurrence gives \(A_{28}\) by subtracting 4 from every displayed valid entry of \(A_{16}\), and \(B_{28}\) by adding 4 to every valid entry of \(B_{16}\); the attached standalone verifier checks both entire vectors, rather than checking only the root entry. From \(S_5=S_1\) and the linear \(S\)-recurrence we infer \(S_{r+4}=S_r\) for every \(r\ge1\). Suppose, for some \(r\ge16\), that \(A_{r+12}=A_r-4\mathbf1\) and \(B_{r+12}=B_r+4\mathbf1\). Since also \(S_{r+12}=S_r\), the minimum and maximum recurrences give the analogous identities at \(r+1\). The base \(r=16\) therefore proves the identities for **every** \(r\ge16\). Evaluating the root \((0,1)\) completes the dyadic assertion.

**4. The logarithmic asymptotic.** For \(r=16+12t+j\), where \(t\ge0\) and \(0\le j<12\), the formulas are \(\ell_r=\ell_{16+j}-4t\) and \(u_r=u_{16+j}+4t\). Hence \(\max_{N\le2^r}|\Delta(N)|=r/3+O(1)\). The maximum of absolute values over prefixes is nondecreasing in its upper limit. For \(2^{r-1}\le X<2^r\), it lies between the two consecutive dyadic maxima, giving the claimed \(\frac13\log_2 X+O(1)\) for all real \(X\ge1\).

The initial pairs \((\ell_r,u_r)\) for \(0\le r\le15\) are
\[
(0,0),(0,1),(0,2),(0,3),(0,4),(0,4),(0,4),(0,5),(-1,7),(-1,7),(-2,7),(-2,7),(-2,8),(-2,8),(-4,8),(-4,8).
\]

## Verification

Run `python3 verify_stern5_discrepancy.py` using the attached standalone file. It enumerates precisely the 24 states, generates the three integer-vector recurrences through \(r=28\), and asserts all 24 entries of each finite certificate identity. It independently generates Stern's recurrence and checks every prefix through \(2^{18}\), then directly counts residues through the explicit \(r=24\) extremal witnesses. It also reconstructs extremal prefix indices by dynamic programming rather than an exponential search. No external packages, datasets, arbitrary precision assumptions, or unverified precomputed logs are used.

The finite computation in Step 3 is a **proved finite reduction**; the unrestricted conclusion follows from the stated induction, not from extrapolating a finite experiment. Since the proof uses a finite integer certificate, independent code and hand verification of the certificate remain possible and desirable.

## Relationship to prior work

Reznick, *Regularity properties of the Stern enumeration of the rationals* (first publicly posted 2006-10-19, arXiv:math/0610601v1), proves modular-pair equidistribution and the bounded discrepancy \(T(N;3,1)-T(N;3,2)\in\{0,1,2,3\}\). Its final discussion explicitly reports **no result for modulus five** and only a finite examination giving \(-5\le T(N;5,1)-T(N;5,4)\le11\) for \(N\le2^{19}\). Our theorem provides the exact and unbounded maximum/minimum law for the object that discussion singles out. Reznick's primitive-pair transition framework is acknowledged and used; it does not by itself state the 24-state max-plus periodicity certificate.

Anders, Dennison, Reznick and Weber, *Congruence properties of binary partition functions* (arXiv:1102.5355v1, 2011), analyze parity and eventual periodicity of binary partition representation functions, not extremal five-residue prefix differences. Lansing's 2014 thesis, *On the Stern sequence and a related sequence*, Chapter 4.4, studies distributions of numerical magnitudes of Stern values rather than five-residue prefix extrema. These distinctions concern the statements and implications, not merely their titles.

## Limitations

The result concerns only the difference between residues one and four modulo five, not every pair of residues and not the rate of equidistribution of each residue separately. The exact finite identities are reproducible but have not received an independent human audit. A publicly unavailable 2012 collection of related lecture notes and unlocated later proofs represent possible historical-priority risks; failed searches alone do not establish priority. This result makes no independent-certification claim.

## References

1. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, arXiv:math/0610601v1 (first submitted 2006-10-19), especially Section 5 and its final discussion. https://arxiv.org/abs/math/0610601
2. K. Anders, M. Dennison, B. Reznick and J. Weber, *Congruence properties of binary partition functions*, arXiv:1102.5355v1 (first submitted 2011-02-25). https://arxiv.org/abs/1102.5355
3. J. Lansing, *On the Stern sequence and a related sequence*, Ph.D. thesis, University of Illinois at Urbana-Champaign (2014), particularly Section 4.4. https://hdl.handle.net/2142/49483
