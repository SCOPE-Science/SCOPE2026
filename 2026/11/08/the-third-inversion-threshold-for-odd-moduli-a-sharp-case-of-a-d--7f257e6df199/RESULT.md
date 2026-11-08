# The third inversion threshold for odd moduli: a sharp case of a Dedekind-sum conjecture

## Finding

Let \(b\ge 7\) be odd and let \(J_b(a)\) be the number of inversions of the permutation \(j\mapsto aj\bmod b\), with \(1\le j\le b\) and \(\gcd(a,b)=1\). Represent \(a\) by its unique integer in \(1,\ldots,b-1\). Put
\[
T_b=\frac{(b+1)(b-2)}6,\qquad S_b=\frac{b^2-1}8.
\]
Then
\[
\boxed{J_b(a)\ge T_b\quad\text{for every unit }a\notin\{1,2,(b+1)/2\}.}
\]
Equality is possible **if and only if** \(b\equiv2\pmod3\). In that case, the complete set of equality multipliers is \(a\in\{3,(b+1)/3\}\). Furthermore, \(J_b(1)=0\) and \(J_b(2)=J_b((b+1)/2)=S_b<T_b\). Thus the **third distinct smallest** inversion number \(I_3(b)\) satisfies
\[
\boxed{I_3(b)\ge \frac{(b+1)(b-2)}6,\qquad
I_3(b)=\frac{(b+1)(b-2)}6\ \Longleftrightarrow\ b\equiv2\pmod3.}
\]
This proves the \(n=3\), odd-\(b\) portion of Chen–Dunn–Hewett–Silas Conjecture 2.7, including its predicted equality family and uniqueness of equality multipliers. No claim is made for even moduli or for \(n=4,5,6\).

## Assumptions and scope

All variables \(a,b,c\) are ordinary integers unless treated as real variables in concavity inequalities; \(b\) is odd and at least \(7\). Only reduced residues \(a\) with \(1\le a\le b-1\) and \(\gcd(a,b)=1\) are considered. The permutation has positions \(1,\ldots,b\), with \(b\) mapped to itself. The final fixed position does not affect inversions, so computational counting may equivalently use positions \(1,\ldots,b-1\). The third *distinct* minimum means the third smallest value in the set \(\{J_b(a):\gcd(a,b)=1\}\), not the third term in an ordered multiset counting repeated inversion values.

## Proof

We invoke two established identities and one established inequality from Chen–Dunn–Hewett–Silas [1, Propositions 2.6 and (3.2)]. For coprime \(1\le a<b\), put \(r=b\bmod a\) and \(C_b=(b-1)(b-2)/2\). Inversion reciprocity and reversal are
\[
aJ_b(a)+bJ_a(r)=\frac{(a-1)(b-1)(a+b-1)}4,
\qquad J_b(b-a)=C_b-J_b(a).
\]
The second identity follows by reversing all relative order comparisons among the \(b-1\) nonzero residues. In particular, \(0\le J_a(r)\le(a-1)(a-2)/2\). Proposition 2.6, applied to any coprime \(2\le r\le a-2\), additionally supplies
\[
J_a(r)\le U(a):=\frac{3a^2-12a+9}{8}.
\]
Define rational auxiliary functions
\[
A_b(t)=\frac{(t-1)(b-1)(t+b-1)}{4t},\qquad
L_b(t)=A_b(t)-\frac{b(t-1)(t-2)}{2t}.
\]
Reciprocity implies \(L_b(a)\le J_b(a)\le A_b(a)\). Equality on the left requires \(J_a(r)=(a-1)(a-2)/2\), which happens exactly when \(r=a-1\); equality on the right requires \(r=1\) (for \(a\ge3\)). The derivative \(A_b'(t)=(b-1)(1+(b-1)/t^2)/4\) is positive for all \(t>0\).

**Small multipliers.** For \(3\le a\le(b+1)/3\), direct factorization gives
\[
L_b(a)-T_b=\frac{(a-3)(b+1)(b+1-3a)}{12a}\ge0.
\]
Equality of \(J_b(a)\) with \(T_b\) forces \(a=3\) or \(a=(b+1)/3\), as well as \(r=a-1\). The latter condition for either endpoint is precisely \(b\equiv2\pmod3\), and it is then attained by both \(a=3\) and \(a=(b+1)/3\). These are units and are distinct for \(b\ge 7\).

**Large multipliers.** For \(2b/3\le a\le b-1\), write \(c=b-a\), so \(1\le c\le b/3\). Reversal and reciprocity give
\[
J_b(a)\ge C_b-A_b(c).
\]
To show strict inequality with \(T_b\), clear denominators:
\[
\begin{aligned}
N_b(c)&:=12c(C_b-A_b(c)-T_b)\\
&=-3(b-1)c^2+(b^2-7b+10)c+3(b-1)^2.
\end{aligned}
\]
For each \(b\ge7\), \(N_b\) is strictly concave on \([1,b/3]\). Its endpoints satisfy
\[
N_b(1)=4(b-2)^2>0,\qquad
N_b(b/3)=\frac{3b^2-8b+9}{3}>0.
\]
A concave function on a compact interval is bounded below by the smaller endpoint value. Therefore \(J_b(a)>T_b\) throughout this large-multiplier range, including \(a=b-1\).

**Middle multipliers.** Suppose \((b+1)/3<a<2b/3\). We have \(a\ge3\). If \(r=a-1\), then \(a\mid b+1\), and \(1<(b+1)/a<3\), forcing \(a=(b+1)/2\), one of the excluded multipliers. If \(r=1\), reciprocity gives \(J_b(a)=A_b(a)\), whose monotonicity yields
\[
J_b(a)-T_b>A_b(b/3)-T_b
=\frac{2b^3-17b^2+28b-9}{12b}
=\frac{(b-7)(2b^2-3b+7)+40}{12b}>0.
\]
In the only remaining case, \(2\le r\le a-2\), Proposition 2.6 gives \(J_b(a)\ge A_b(a)-bU(a)/a\). The exact factorization is
\[
24a\left(A_b(a)-\frac b a U(a)-T_b\right)
=P_b(a),
\]
where
\[
P_b(a)=-3(b+2)a^2+(2b^2+22b+20)a-6b^2-15b-6.
\]
This is strictly concave on \([b/3,2b/3]\); its endpoints are
\[
P_b(b/3)=\frac{b^3+2b^2-25b-18}{3}
=\frac{(b-7)(b^2+9b+38)+248}{3}>0,
\]
\[
P_b(2b/3)=\frac{18b^2-5b-18}{3}>0.
\]
Hence \(J_b(a)>T_b\) for all middle multipliers other than the excluded inverse of \(2\).

Finally, the exact identities already established in [1, Proposition 2.6] give \(J_b(1)=0\) and \(J_b(2)=J_b((b+1)/2)=S_b\); moreover
\[
T_b-S_b=\frac{(b-5)(b+1)}{24}>0.
\]
For \(b\ge7\), \(1,2,(b+1)/2\) are distinct units. The three ranges above cover every remaining unit (with harmless overlap at endpoints). There is at least one inversion value larger than \(S_b\) because \(a=b-1\) is a unit with \(J_b(b-1)=C_b>S_b\). Thus the third distinct minimum exists and is at least \(T_b\). For \(b\equiv2\pmod3\), the exhibited \(a=3,(b+1)/3\) attain \(T_b\), proving sharpness; the prior strict inequalities prove exclusivity. \(\square\)

## Verification

The included standalone `verify.py` requires only Python 3 (no third-party packages). Running `python3 verify.py` independently computes inversion numbers by reciprocity for every unit of every odd modulus from \(7\) through \(1001\), checks the third distinct minimum and all equality multipliers, and cross-checks direct permutation inversion enumerations for all odd moduli through \(103\). Expected output begins with `VERIFY_OK`, reports 498 odd moduli, 203374 unit entries, 2202 direct computations, and 332 equality cases. Exact polynomial identities and endpoint inequalities in the proof can also be checked symbolically. Finite experiments are supplementary; the unrestricted conclusion follows from the case analysis and the cited published inequality.

## Relationship to prior work

Chen–Dunn–Hewett–Silas [1] formulated the third-rank inequality as the \(n=3\) instance of Conjecture 2.7. They proved the second-rank bound in Proposition 2.6 and the inversion reciprocity and reversal identities, all of which are used here. Their text presents the higher-rank claims as conjectures, not theorems. Jabuka–Robins–Wang [2] and Girstmair [3] study equality or congruence of Dedekind sums rather than sharp ordering of the third distinct inversion value; their reported conclusions do not imply the inequality above. No assertion is made that the conjecture for all six ranks or for even moduli has been resolved.

## Limitations

The proof relies explicitly on the previously published Proposition 2.6; its verification is in [1] and its proof was materially inspected. The statement concerns odd moduli \(b\ge7\) only, not odd \(b=5\) or even moduli. Independent mathematical review and a definitive historical-priority audit have not been performed; an unlocated earlier proof of the odd-modulus case remains possible. Computational checks do not establish uniqueness beyond their finite range; global uniqueness is proved by the inequalities.

## References

[1] Y. Chen, N. Dunn, C. Hewett, S. Silas, *On the Inversion Polynomial for Dedekind Sums*, first public preprint November 15, 2014, arXiv:1411.4092v1; journal version *Dedekind sums s(a,b) and inversions modulo b*, International Journal of Number Theory 11 (2015), 2325–2339, DOI: 10.1142/S1793042115501067. Full openly accessible journal manuscript: https://icerm.brown.edu/summerug/2014/DedekindSumspaper.pdf.

[2] S. Jabuka, S. Robins, X. Wang, *When are two Dedekind sums equal?*, arXiv:1103.0370 (2011).

[3] K. Girstmair, *A criterion for the equality of Dedekind sums mod Z*, International Journal of Number Theory 10 (2014), 565–568, DOI: 10.1142/S179304211350108X; first public manuscript arXiv:1304.4716 (2013).
