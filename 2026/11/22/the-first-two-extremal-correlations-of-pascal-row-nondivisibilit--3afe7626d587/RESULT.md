# The second extremal correlation of Pascal-row nondivisibility at odd primes

## Finding

Fix an odd prime \(p\). Let \(F_p(n)\) be the number of entries in Pascal row \(n\) not divisible by \(p\). For \(X_L\) uniform on \(\{0,\ldots,p^L-1\}\) and a fixed shift \(h\ge0\), write \(C_p(h)\) for the limiting Pearson correlation of \(F_p(X_L)\) and \(F_p((X_L+h)\bmod p^L)\) as \(L\to\infty\). The rational carry recurrence and the first maximum at shifts \(p^k\) are known. Outside that family, the maximum is
\[
\max_{\substack{h\ge 1\\h\notin \{p^k:k\ge0\}}} C_p(h)
=\frac{4p^4+4p^3+11p^2+11p+18}{p(p+1)(2p+1)(2p+5)},
\]
and is attained **exactly** at \(h=2p^k\), \(k\ge0\). It is strictly below the first maximum \(2(p+1)/(2p+5)\). For \(p=3,5\) the second levels are \(97/154,186/275\), respectively.

## Assumptions and scope

The shift is fixed when taking the limit. The second row index is reduced cyclically modulo \(p^L\); the Pearson coefficient is centered and normalized by the common positive variance. The extremum is over the limiting correlations, not finite samples. No claim about a shift growing with the sample length is needed.

## Proof

Use the recurrence from [Sharp cyclic Pascal-row correlations at every odd prime](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-cyclic-pascal-row-correlations-at-every-odd-prime--fbb674004d64). In the notation here, let \(B=\sum_{i=1}^p i^2\) and, for \(0\le a<p\), let
\[
U_a=\sum_{i=1}^{p-a} i(i+a),\qquad V_a=\sum_{i=1}^{a} i(i+p-a).
\]
The recurrence is \(B C_p(a+pt)=U_a C_p(t)+V_a C_p(t+1)\), with \(C_p(0)=1\) and \(C_1:=C_p(1)=2(p+1)/(2p+5)\). It follows from the Lucas–Fine product by splitting the units digit into the cases without and with a carry, respectively. More precisely, the uncentered cyclic product sum obeys the same two branches with coefficients \(U_a,V_a\) and total square sum \(B^L\). Division by \(B^L\) gives the normalized mixed moment; the squared mean divided by the second moment is \([3(p+1)/(2(2p+1))]^L\to0\), so the limit is the Pearson limit. The lag-one recursion contracts since \(V_1/B<1\), and all remaining fixed shifts reduce to smaller shifts. The known first-tier bound gives \(C_p(h)\le C_1\) for \(h\ge1\).

Since \(U_0=B\), \(V_0=0\), one can strip all trailing zero base-\(p\) digits. For a one-digit shift \(1\le a<p\), the recurrence gives \(C_p(a)=(U_a+V_a C_1)/B\). Put \(C_2=C_p(2)\) and \(D=p(p+1)(2p+1)(2p+5)\). Summing the integer and square terms in \(U_a,V_a\) yields the displayed value of \(C_2\) and the identities
\[
D(C_1-C_2)=3(p-2)(2p^2+3p+3)>0,
\]
\[
D(C_2-C_p(a))=3(a-2)\big[2p^3+p^2-p-3-a^2-2a(p^2+p+1)\big]\quad(3\le a<p).
\]
The bracket decreases for \(a\ge0\) and at \(a=p-1\) equals \(p-2>0\). This range is empty for \(p=3\). Thus \(2\) is the unique runner-up among one-digit shifts.

If a reduced shift instead has the form \(a+pt\) with \(a\in[1,p-1]\) and \(t\ge1\), both input correlations are bounded by \(C_1\). The identity \(U_a+V_a=B-pa(p-a)/2\) and \(a(p-a)\ge p-1\) give
\[
C_p(a+pt)\le C_1(U_a+V_a)/B\le C_1(U_1+V_1)/B.
\]
The last bound is strictly below \(C_2\), since \(D[C_2-C_1(U_1+V_1)/B]=3(p^2+p+6)>0\). Therefore a maximizer outside the first tier must reduce to the single digit 2, and conversely all \(2p^k\) have value \(C_2\).

## Verification

`python3 check.py` checks exact finite cyclic moments, the Lucas–Fine row count and the bounded-shift ordering for several odd primes. These are finite checks; the symbolic inequalities and carry argument prove the unrestricted statement for fixed shifts and odd primes.

## Relationship to prior work

The cited odd-prime correlation result already gives the rational recurrence, the first-tier value and the classification of its equality cases. The additional claim here is the sharp **second** value and equality family: it needs a bound below the first tier that controls all shifts with more than one digit after removing trailing zeros, as well as the sharper one-digit comparison. The [binary Pascal-row result](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-shift-correlations-for-the-odd-entry-counts-in-binary-pasc--7be946ab1fa0) concerns a different prime and has no analogous digit \(2<p\). Fine's digit formula, discussed in [Rowland](https://arxiv.org/abs/1704.05872), supplies the one-row count. [Lane](https://arxiv.org/abs/2309.12942) studies row totals and residue distributions; [Mathonet, Rigo, Stipulanti and Zénaïdi](https://arxiv.org/abs/2201.06636) study digital encodings of whole rows.
