# Exactly four symmetric semigroups among consecutive pentagonal triples

## Finding
For each integer \(n\ge2\), let \(P_n=n(3n-1)/2\) be the \(n\)-th pentagonal number and let
\[
S_n=\langle P_n,P_{n+1},P_{n+2}\rangle\subseteq\mathbb N_0.
\]
A numerical semigroup \(S\) is *symmetric* if its Frobenius number \(F\) satisfies \(z\in S\) if and only if \(F-z\notin S\) for every integer \(z\). Equivalently, its genus \(g\), the number of nonnegative gaps, satisfies \(2g=F+1\).

**Theorem.** For every integer \(n\ge2\), the semigroup \(S_n\) is symmetric if and only if \(n\in\{2,3,5,40\}\). These are also precisely the complete-intersection members of this family. Their complete invariants are

| \(n\) | minimal generators | Frobenius number | genus |
|---|---|---:|---:|
| \(2\) | \(5,12\) | \(43\) | \(22\) |
| \(3\) | \(12,22,35\) | \(133\) | \(67\) |
| \(5\) | \(35,51\) | \(1699\) | \(850\) |
| \(40\) | \(2380,2501,2625\) | \(258529\) | \(129265\) |

In particular, the index \(40\) supplies the sole three-generator exception beyond index \(3\). The infinite classification uses a proved cutoff of \(141\) followed by a complete, reproducible finite calculation.

## Assumptions and scope
All generators are positive integers and all coefficients in a semigroup expression are nonnegative integers. The theorem includes every \(n\ge2\); it makes no claim about arbitrary polygonal order, nonconsecutive indices, or shifted pentagonal sequences. Symmetry and complete intersection coincide for numerical semigroups of embedding dimension at most three, by the classical three-generator theorem (Herzog). The standard criterion used here says that a *minimally* three-generated numerical semigroup \(\langle a,b,c\rangle\) with overall greatest common divisor \(1\) is symmetric exactly when some pair, say \(a,b\), has \(d=\gcd(a,b)>1\) and its remaining generator \(c\) lies in \(\langle a/d,b/d\rangle\). The two-generator case is always symmetric.

## Proof
Write \(A=P_n\), \(B=P_{n+1}\), \(C=P_{n+2}\), so that \(B-A=3n+1\), \(C-B=3n+4\), and \(C-A=6n+5\).

**1. Greatest common divisors and embedding dimension.** One has
\[
\gcd(A,B)=\begin{cases}2,&n\equiv3\pmod4,\\1,&\text{otherwise},\end{cases}
\quad
\gcd(B,C)=\begin{cases}2,&n\equiv2\pmod4,\\1,&\text{otherwise},\end{cases}
\quad
\gcd(A,C)=\gcd(35,6n+5).
\]
For the last identity, observe that \(6n+5\) is relatively prime to \(24\) and \(24A=(6n)(6n-2)\equiv35\pmod{6n+5}\). For the first identity, any odd common divisor divides both \(A\) and \(3n+1\), hence divides \(6A=3n(3n-1)\equiv2\pmod{3n+1}\), an impossibility. The minimum of the two \(2\)-adic valuations is exactly \(1\) if \(n\equiv3\pmod4\), and otherwise at least one generator is odd; the second identity is the index-shifted version of the first. Thus \(\gcd(A,B,C)=1\): the family always consists of numerical semigroups.

The smallest cannot lie in the semigroup of the two larger generators. The middle generator cannot be obtained from the outer two either: for \(n\ge3\), one has \(A<B<2A\) and \(B<C\), whereas for \(n=2\) one has \(B=12\notin\langle5,22\rangle\). For \(n\ge6\), \(C<2A\), so \(C\) cannot be a sum of two or more generators \(A,B\); it is also different from either single generator. Direct comparison of the remaining four cases shows that \(C\in\langle A,B\rangle\) precisely for \(n=2\) and \(n=5\): \(22=2\cdot5+12\) and \(70=2\cdot35\). Therefore the embedding dimension is two exactly at these indices; these semigroups are symmetric. Every other index gives a minimal triple, to which the three-generator symmetry criterion applies.

**2. Adjacent pairs give only \(n=3\).** For the pair \((B,C)\), a nontrivial greatest common divisor can only be \(2\). Since \(A<B\), a representation \(A=x(B/2)+y(C/2)\) would have \(x+y\le1\), forcing \(2A=B\) or \(2A=C\). The former quadratic equation has no integer solution; the latter has the sole positive integer solution \(n=5\), where \(\gcd(B,C)=1\). Thus this pair gives no three-generator symmetry.

The pair \((A,B)\) has nontrivial gcd only for \(n\equiv3\pmod4\). For \(n\ge10\), the inequality \(3A>2C\), equivalent to \(3n^2-25n-20>0\), implies \(C<3(A/2)\). Hence any expression of \(C\) from \(A/2,B/2\) uses at most two terms, whose sum is at most \(B<C\), impossible. The only remaining indices for this pair are \(n=3,7\). At \(n=3\), \(35=4\cdot6+11\) proves symmetry. At \(n=7\), no nonnegative solution exists to \(117=35x+46y\) (reduce modulo \(35\) to obtain \(y\equiv17\pmod{35}\), whereas \(0\le y\le2\)).

**3. Nonadjacent pair and an infinite cutoff.** Put \(d=\gcd(A,C)=\gcd(35,6n+5)\). If \(d>1\), then \(d\in\{5,7,35\}\). A gluing along \((A,C)\) requires \(B=x(A/d)+y(C/d)\) with \(x,y\ge0\). With \(h=x+y\), this is equivalent to
\[
(h-d)A+y(6n+5)=d(3n+1).
\]
Because \(B<C\), necessarily \(0\le y<d\). For \(n\ge142\), direct polynomial calculation gives \(A>35(6n+5)\ge d(6n+5)\). Consequently \(\lvert d(3n+1)-y(6n+5)\rvert<A\), so the displayed identity forces \(h=d\). It follows that
\[
y=\frac{d(3n+1)}{6n+5}.
\]
But since \(d\) is odd and at most \(35\), for every \(n\ge142\) this value lies strictly between the consecutive half-integer bounds \((d-1)/2\) and \(d/2\). In particular it is not an integer. Thus no nonadjacent-pair gluing exists at or above \(142\).

**4. Complete finite range.** Only \(2\le n\le141\) remains. The executable `check.py` verifies the gcd formulas at every index and examines every pair with gcd greater than one. For the nonadjacent pair it sets \(a=A/d\), \(c=C/d\), and calculates
\[
y_0=(B\,c^{-1})\bmod a,\quad 0\le y_0<a,
\]
with \(y_0=0\) if \(a=1\). Because \(\gcd(a,c)=1\), an expression \(B=xa+yc\) with nonnegative integers exists **if and only if** \(y_0\le\lfloor B/c\rfloor\). The script proves this test agrees in each finite case with a second, direct scan over all possible \(y\). Exactly \(44\) indices in the finite range have \(d>1\); their complete residue certificate is `finite_residue_certificate.csv`. Only \(n=5,40\) pass the nonadjacent test. At \(n=40\), \(d=35\), \(A/d=68\), \(C/d=75\), and \(2501=7\cdot68+27\cdot75\). Together with Steps 1–2, this proves the complete list \(\{2,3,5,40\}\).

**5. Frobenius numbers and genera.** The two-generator formula gives \(F(2)=5\cdot12-5-12=43\) and \(F(5)=35\cdot51-35-51=1699\). For the gluing cases, the standard formula
\[
F(da,dc,b)=d(ac-a-c)+(d-1)b
\]
applies because \(\gcd(a,c)=1\), \(\gcd(d,b)=1\), and \(b\in\langle a,c\rangle\). At \(n=3\), use \((d,a,c,b)=(2,6,11,35)\) to get \(F=133\); at \(n=40\), use \((35,68,75,2501)\) to get \(F=258529\). Symmetry gives \(g=(F+1)/2\) in all four cases. This also determines the complete-intersection members by Herzog's classical equivalence.

## Verification
Run `python3 check.py` with Python 3.8 or later. It uses only the standard library; no internet, computer algebra package, data download, or unavailable binary dependency is needed. It checks all \(140\) bounded indices; cross-checks modular inversion against independent exhaustive representations; writes the \(44\)-row CSV certificate; checks the finite gluing list; and independently computes the Apéry sets, Frobenius numbers and genera for all four exceptional semigroups by shortest paths modulo their multiplicity. The exact stdout is in `check_output.txt`. The infinite cutoff is proved in Step 3; the script does not purport to certify infinitely many indices.

## Relationship to prior work
Robles-Pérez and Rosales (2017, arXiv:1706.04378) show that consecutive triangular and tetrahedral sequences have telescopic structures, with Frobenius formulas. Their theorems use those different figurate sequences and do not imply the exceptional pentagonal symmetry classification. The OEIS sequence A069757, initiated in 2002, tabulates Frobenius numbers for **the exact pentagonal family** (including \(F(40)=258529\)); those numerical values are prior knowledge and are **not** claimed new. The present theorem instead classifies symmetry and complete intersection for *all* indices, with a proved finite cutoff and exact exceptional genera. The distinction is substantive: the table has the odd Frobenius number \(F(4)=287\), but an independent Apéry calculation gives \(g(4)=145\), so this index is **not** symmetric. García-Sánchez, González and Planas-Vilanova (2024, arXiv:2404.06358) analyze factorization lengths for triples of consecutive **integers**; no result there covers consecutive values of the quadratic pentagonal polynomial. The general three-generator criterion and the Frobenius gluing formula are classical and are not claimed as contributions.

## Limitations
This result only covers the unshifted ordinary pentagonal sequence and three consecutive indices. The 44-case exact calculation is a finite component of the proof after a symbolic infinite cutoff, not a proof by extrapolation. A presently unindexed equivalent classification is possible; the available inspected literature, historic arithmetic data and targeted mathematical search did not identify one. The scientific assessment has not been independently audited.

## References
- A. M. Robles-Pérez and J. C. Rosales, *The Frobenius number for sequences of triangular and tetrahedral numbers*, first public arXiv version 2017-06-14, arXiv:1706.04378, https://arxiv.org/abs/1706.04378.
- V. A. Sapko and contributors, OEIS A069757, *Frobenius number of the numerical semigroup generated by three consecutive pentagonal numbers*, https://oeis.org/A069757; full prior table https://oeis.org/A069757/b069757.txt.
- P. A. García-Sánchez, L. González, F. Planas-Vilanova, *Elements with unique length factorization of a numerical semigroup generated by three consecutive numbers*, arXiv:2404.06358, first public 2024-04-09, https://arxiv.org/abs/2404.06358.
- J. Herzog, *Generators and relations of abelian semigroups and semigroup rings*, Manuscripta Math. (1970), classical symmetric/complete-intersection criterion in embedding dimension three.
