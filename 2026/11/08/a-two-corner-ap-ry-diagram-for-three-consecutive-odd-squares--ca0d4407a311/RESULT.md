# A two-corner Apéry diagram for three consecutive odd squares

## Finding
For every odd integer \(n\ge 7\), consider the numerical semigroup
\[
S_n=\langle n^2,(n+2)^2,(n+4)^2\rangle.
\]
Put \(a=n^2\), \(b=(n+2)^2\), and \(c=(n+4)^2\). Define
\[
T_n=\{(x,y)\in\mathbb Z_{\ge0}^2:0\le x,y\le n+1,\ \text{not both }x\ge n-6\text{ and }y\ge(n+3)/2\}.
\]
Then the entire Apéry set is
\[
\operatorname{Ap}(S_n,a)=\{xb+yc:(x,y)\in T_n\}.
\]
It has precisely two maximal elements under the semigroup order. The complete pseudo-Frobenius set is
\[
\operatorname{PF}(S_n)=\left\{2n^3+5n^2-12,\ \frac{3n^3+17n^2+40n+24}{2}\right\}.
\]
Consequently \(S_n\) has type exactly \(2\) and genus
\[
g(S_n)=\frac{(n+1)(2n^2+5n+7)}2.
\]
Its Frobenius number is the larger of the two displayed pseudo-Frobenius numbers; explicitly it is \((3n^3+17n^2+40n+24)/2\) for \(n=7,9,11\), and \(2n^3+5n^2-12\) for every odd \(n\ge13\).

## Assumptions and scope
The integer \(n\) is odd and at least \(7\). All semigroup linear combinations have nonnegative integer coefficients. The Apéry set \(\operatorname{Ap}(S_n,a)\) contains the smallest member of \(S_n\) in each residue class modulo \(a\). The genus counts the nonnegative integers not in \(S_n\); a pseudo-Frobenius number is a gap \(f\) with \(f+s\in S_n\) for every nonzero \(s\in S_n\). The theorem makes no assertion about smaller odd \(n\), even \(n\), or longer runs of odd squares.

## Proof
Because \(n\) is odd, \(\gcd(a,b)=\gcd(n,n+2)^2=1\); hence \(S_n\) is a numerical semigroup. Three exact identities, valid for every odd \(n\), are
\[
(n+2)b=\frac{n+1}{2}c+\frac{n+3}{2}a,\qquad
(n+2)c=8b+(n+2)a,
\]
\[
(n-6)b+\frac{n+3}{2}c=\frac{3n+7}{2}a.
\]
All coefficients are nonnegative under the stated assumptions, and the coefficients of \(a\) on the right are strictly positive. Applied to \(xb+yc\), these identities permit reduction whenever \(x\ge n+2\), \(y\ge n+2\), or both \(x\ge n-6\) and \(y\ge(n+3)/2\), respectively. Each reduction preserves the residue modulo \(a\) and strictly decreases the residual \(b,c\)-weighted sum by a positive multiple of \(a\). There can be no infinite descent. Every nonnegative \((x,y)\) therefore reduces to an index in \(T_n\).

There are \((n+2)^2\) lattice points in the complete square \([0,n+1]^2\). The excluded upper-right rectangle has \(8\) columns and \((n+1)/2\) rows, so
\[
|T_n|=(n+2)^2-4(n+1)=n^2=a.
\]
Because \(b\) is invertible modulo \(a\), all \(a\) residues occur among the nonnegative monomials \(xb\) and thus, by reduction, among the \(a\) monomials indexed by \(T_n\). They must consequently occupy pairwise distinct residue classes. Every element of \(S_n\) is a nonnegative sum of \(a,b,c\), and removal of its \(a\)-part followed by the reductions yields the unique \(T_n\) representative in the same residue, no larger than the original element. This establishes the claimed Apéry set, not merely a candidate list.

An Apéry element \(w\) is maximal for the semigroup order exactly when none of \(w+b\) and \(w+c\) belongs to the Apéry set: \(w+a\) never belongs by definition, and \(a,b,c\) generate the semigroup. For \(w=xb+yc\) indexed by \(T_n\), either neighboring index inside \(T_n\) produces another Apéry element, or the corresponding exterior index reduces strictly by a positive multiple of \(a\), so its value is not Apéry. The set \(T_n\) is the union of the horizontal-bottom rectangle and left vertical strip; its only coordinatewise maximal corners are
\[
P=(n-7,n+1),\qquad Q=(n+1,(n+1)/2).
\]
Thus exactly the two elements \(P\cdot(b,c)-a\) and \(Q\cdot(b,c)-a\) are pseudo-Frobenius numbers. Direct polynomial expansion gives respectively \(2n^3+5n^2-12\) and \((3n^3+17n^2+40n+24)/2\). They are distinct: their difference equals \((n^3-7n^2-40n-48)/2\), negative at \(n=7,9,11\) and positive for \(n\ge13\), since the cubic is strictly increasing for \(n\ge 13\) and positive at \(13\). This yields the type and piecewise Frobenius formula.

The exact coordinate sums over \(T_n\), computed by subtracting the excluded rectangle from the full square, are
\[
\sum_{(x,y)\in T_n}x=\frac{(n+1)(n^2-4n+24)}2,\qquad
\sum_{(x,y)\in T_n}y=\frac{(n+1)(n^2-2n-6)}2.
\]
Finally the Apéry genus identity
\[
g(S_n)=\frac1a\sum_{(x,y)\in T_n}(xb+yc)-\frac{a-1}{2}
\]
and substitution of the displayed sums simplify exactly to \((n+1)(2n^2+5n+7)/2\).

## Verification
Run the bundled standalone script with `python3 verify.py`. It first checks all three polynomial identities and cardinality and residue uniqueness, then independently constructs every Apéry residue minimum using a Dijkstra shortest-path computation on the residues modulo \(a\). It directly reconstructs the pseudo-Frobenius numbers from the computed minima and compares Frobenius numbers and genera. The finite check covers all odd \(n\) from \(7\) through \(99\), plus \(101,127,151,201,251\), a total of \(52\) cases. The infinite theorem follows from the proof above, not from the finite experiment.

## Relationship to prior work
Lepilov, O'Rourke and Swanson (2015), Theorem 3.1, give Frobenius formulas for three *ordinary consecutive squares*, \(\langle n^2,(n+1)^2,(n+2)^2\rangle\), not squares separated by two in their bases. Fel (2016) develops Frobenius/genus/minimal-relation formulas for the same ordinary-consecutive three-square family. Chomicz (2026) computes Apéry sets and invariants for *four ordinary consecutive squares* and triangular numbers. Hashuga, Herbine and Jensen (2020) study semigroups generated by *infinitely many* quadratic-sequence terms with initial term zero and explicitly distinguish finite-generator sequences as outside their scope. General Apéry and three-generator algorithms apply in principle but do not supply the displayed two-corner diagram and closed classification without a family-specific derivation. No directly covering result was located in the searched sources or mathematical-record results; absence from searches is not proof of historical priority.

## Limitations
The statement is confined to odd \(n\ge7\). It establishes neither a general fixed-spacing-square formula nor a classification for all finite quadratic sequences. An unindexed or inaccessible equivalent derivation is a residual originality risk. Computational checks are finite and are not a substitute for the exact reductions and cardinality proof. Independent external mathematical audit has not been conducted.

## References
1. K. Chomicz, *On numerical semigroups with embedding dimension four* (first posted 2026-04-28), arXiv:2604.25653, https://arxiv.org/abs/2604.25653.
2. M. Lepilov, J. O'Rourke, I. Swanson, *Frobenius numbers of numerical semigroups generated by three consecutive squares or cubes*, 2015; openly available full text: https://mikhail.lepilov.website/frobenius.pdf.
3. L. G. Fel, *Numerical semigroups generated by squares, cubes and quartics of three consecutive integers* (2016), arXiv:1608.08693, https://arxiv.org/abs/1608.08693.
4. M. Hashuga, M. Herbine, A. Jensen, *Numerical Semigroups Generated by Quadratic Sequences* (2020), arXiv:2009.01981, https://arxiv.org/abs/2009.01981.
