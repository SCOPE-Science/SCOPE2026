# First parity-band breakdown in three-consecutive-coin \(p\)-gap sets

## Finding

Let \(a=2h\ge6\) be even, and for each integer \(n\ge0\) define the denumerant
\[
d_a(n)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^3: ax+(a+1)y+(a+2)z=n\}.
\]
For \(p\ge0\), write \(G_p(a)=\{n\ge0:d_a(n)\le p\}\), including zero when it meets the inequality. The following give complete sets, not merely the largest gaps.

For each \(t\in\{1,2,3\}\), put \(K_t=a(a+t)\). Then
\[
G_{h+t}(a)=\{0,1,\ldots,K_t-1\}\ \cup\ \{K_t+1,K_t+3,\ldots,K_t+a-1\}.
\]
The first three levels above \(h\) therefore have an initial interval and exactly \(h\) isolated terminal gaps.

At the **first structural breakdown**, \(p=h+4\), set \(K=a(a+3)\). One has the disjoint union
\[
\boxed{G_{h+4}(a)=\{0,\ldots,K+1\}\cup\{K+3,\ldots,K+a-1\}\cup\{K+a+1\}\cup\{K+a+5,K+a+7,\ldots,K+2a-1\}.}
\]
The interval in the second term has \(a-3\) elements, and the final progression has \(h-2\) elements. The terminal region now includes a second consecutive gap block; exactly \(h-1\) positive gaps are isolated, **one fewer than before**. The exact genus, largest gap, and sum of all gaps are
\[
\begin{aligned}
\#G_{h+4}(a)&=a(a+4)+h-2,\\
\max G_{h+4}(a)&=a(a+5)-1,\\
\sum_{n\in G_{h+4}(a)}n&=\frac{(K+1)(K+2)}2+(a-3)K+\frac{a(a-1)}2-3\\
&\qquad +(K+a+1)+(h-2)\left(K+\frac{3a+4}{2}\right).
\end{aligned}
\]
The largest-gap formula is already a consequence of an earlier known Frobenius phase; novelty here concerns the **full gap-set transition, exact genus and gap sum**.

## Assumptions and scope

All representation variables are ordered by their three labeled denominations and are nonnegative integers. Every stated quantifier is over an even integer \(a\ge6\) and, for the first family, \(t\in\{1,2,3\}\). Empty intervals are not needed for this range. \(G_p(a)\) includes all \(n\ge0\) with at most \(p\) representations. “Isolated” means a positive gap \(n\) whose integer neighbors \(n-1\) and \(n+1\) are not gaps. We make no claim for odd \(a\), for general steps between denominations, or for \(p>h+4\).

## Proof

Write \(n=aq+r\) with \(q\ge0\) and \(0\le r<a\). A representation with total coin count \(m=x+y+z\) has \(y+2z=n-am\). For any \(0\le s\le2m\), the number of \((y,z)\) with \(y+2z=s\) and \(y+z\le m\) is exactly
\[
C_m(s)=\left\lfloor\frac{\min(s,2m-s)}2\right\rfloor+1;
\]
it vanishes outside that range. Indeed, \(z\) runs from \(\max(0,s-m)\) to \(\lfloor s/2\rfloor\). Hence
\[
d_a(aq+r)=\sum_{j=0}^{q} C_{q-j}(aj+r).
\]
Adjoining one coin of size \(a\) gives an injection of representations at \(n\) into those at \(n+a\), so \(d_a(n+a)\ge d_a(n)\).

For \(q=a+j\) and \(0\le j\le5\), no index \(j'\ge3\) in the last sum can contribute: if it did, \(aj'+r\le2(a+j-j')\), so \((a+2)j'\le2a+2j-r\). But at \(j'=3\) this would require \(a+6\le2j-r\le10\), impossible for \(a\ge6\); larger \(j'\) are even less possible. Consequently only the last three total-coin layers matter. Direct substitution in \(C_m\) gives, for \(2\le j\le5\),
\[
\begin{split}
d_a\bigl(a(a+j)+r\bigr)
&=\left\lfloor\frac r2\right\rfloor+1
+\left\lfloor\frac{\min(a+r,a+2j-2-r)}2\right\rfloor+1\\
&\quad+\mathbf1_{r\le2j-4}\left(\left\lfloor\frac{2j-4-r}{2}\right\rfloor+1\right),
\qquad 0\le r<a.
\end{split}
\]
The possible index with one fewer total coin always contributes for these values of \(j\). The formula is valid also when the final indicator is zero. For the earlier rows \(q=a\) and \(q=a+1\), the same count yields, respectively,
\[
d_a(a^2+r)=h+\mathbf1_{r\text{ even}},\qquad
d_a(a(a+1)+r)=h+1+\mathbf1_{r\text{ even}}.
\]
Substitution for \(j=2\) gives \(d_a(a(a+2)+r)=h+2+\mathbf1_{r\text{ even}}\). For \(j=3\), the count is \(h+3\) when \(r\) is odd, \(h+5\) when \(r=2\), and \(h+4\) at all remaining even residues. For \(j=4\), every even residue has value at least \(h+5\), and all odd residues have value at least \(h+4\); the odd minimum \(h+4\) occurs exactly for \(r=1\) or odd \(r\ge5\). For \(j=5\), every residue has value at least \(h+5\). These are elementary parity evaluations of the displayed finite expression, including \(a=6\).

For \(p=h+t\) with \(1\le t\le3\), the rows \(q\le a+t-1\) all have at most \(p\) representations by monotonicity along classes modulo \(a\) and the displayed boundary counts. At \(q=a+t\), odd residues have exactly \(p\) representations and even residues have more. At \(q=a+t+1\), every residue has more than \(p\) representations, and monotonicity rules out any later gap. This proves the first formula.

For \(p=h+4\), the \(j=2\) row has all residues at most \(p\), so every earlier quotient row does too. At \(q=a+3\), every residue except \(r=2\) is a gap: \(r=0,1\) are gaps as well, while \(r=2\) is not. At \(q=a+4\), the gaps are precisely \(r=1\) and the odd residues \(r\ge5\). At \(q=a+5\) every residue has more than \(p\) representations, as do all later rows. Translating those rows into integers yields exactly the disjoint union in the finding.

Its cardinality is \((K+2)+(a-3)+1+(h-2)=K+a+h-2\), and its largest element is \(K+2a-1\). The sum follows from an initial interval, a consecutive interval, a singleton, and an arithmetic progression. In the terminal part the run from \(K+3\) to \(K+a-1\) has length \(a-3\ge3\), so its members are not isolated; the singleton at \(K+a+1\) and the \(h-2\) later progression elements are isolated. The initial gap interval is not isolated. The claimed structural transition and all formulas follow. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and no additional packages. The standalone exact-integer checker independently constructs the generating-function coefficients by coin-by-coin dynamic programming and compares the entire alleged gap sets at the first four post-boundary levels for every even \(a\) from \(6\) to \(200\). It checks the finite three-layer expression and the genus/largest-gap/isolated-gap claims, and separately enumerates actual triples for smaller bases. The observed checks were 5,817,672 dynamic-programming comparisons, 40,376 local formula comparisons, and 7,608 independently enumerated terms. These finite tests support but do not replace the all-parameter proof.

## Relationship to prior work

Komatsu and Ying's general arithmetic-progression theorem provides explicit \(p\)-Frobenius/genus formulas for \(0\le p\le\lfloor a/2\rfloor\) and asks for convenient extensions beyond this range; our statement concerns the **first change in the shape of the complete gap set above that range** for consecutive denominations and even \(a\). A separately available formula for the generalized Frobenius number of three consecutive denominations covers the **largest-gap value** used here, but does not give the full gap set or the new genus and sum. The \(t=1\) baseline is included for the exact first-break comparison and is not asserted to be new. Subwattanachai's conditional three-variable Frobenius formula requires a divisibility hypothesis absent for pairwise coprime consecutive triples. No checked source supplied this same all-even-base \(t=4\) topology change; this is a best-knowledge comparison, not a proof of universal priority.

## Limitations

The first four post-boundary levels, even \(a\ge6\), and step one only are addressed. Other levels and odd bases may exhibit additional phase changes. The result does not claim a new formula for the already-known largest gap. A full independent mathematical review has not been performed. Equivalent descriptions in less-indexed denumerant or restricted-partition literature remain a residual priority risk.

## References

[1] T. Komatsu and H. Ying, *The \(p\)-Numerical Semigroup of the Triple of Arithmetic Progressions*, first public arXiv version 27 June 2022, arXiv:2206.13052; *Symmetry* **15** (2023), 1328. https://arxiv.org/abs/2206.13052 ; https://doi.org/10.3390/sym15071328

[2] K. Subwattanachai, *Generalized Frobenius Number of Three Variables*, first public arXiv version 17 September 2023, arXiv:2309.09149, Theorem 1. https://arxiv.org/abs/2309.09149

[3] *Three exact phases of generalized Frobenius numbers for three consecutive denominations*, 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-three-exact-phases-of-generalized-frobenius-numbers-for-three-co--6dc430dbb315
