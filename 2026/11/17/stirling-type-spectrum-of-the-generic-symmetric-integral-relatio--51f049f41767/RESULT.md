# Stirling type spectrum of the generic symmetric-integral relation-algebra atom structure

## Finding
Let \(L_{\mathrm{SI}}\) be Koussas's Fraïssé limit of \(\mathrm{FSIAS}_e\), the finite symmetric integral relation-algebra atom structures in the language \(\{f,e,T\}\), and let \(T_{\mathrm{SI}}=\operatorname{Th}(L_{\mathrm{SI}})\). The source proves that \(T_{\mathrm{SI}}\) is \(\aleph_0\)-categorical and eliminates quantifiers.

Write \(p_n=|S_n(T_{\mathrm{SI}})|\) for the number of complete \(n\)-types over \(\varnothing\). Then
\[
\boxed{p_n=\sum_{k=0}^n {n+1\brace k+1}\,2^{\binom{k+2}{3}}.}
\]
Thus
\[
(p_1,p_2,p_3,p_4,p_5,p_6)=(3,23,1135,1059247,34375535071,72058315739597647).
\]

The injective ordered \(n\)-tuple orbit count is
\[
\boxed{a_n=2^{\binom{n+2}{3}}+n\,2^{\binom{n+1}{3}}.}
\]
Consequently
\[
\frac{p_n}{2^{\binom{n+2}{3}}}\longrightarrow1
\qquad\text{and}\qquad
\frac{a_n}{p_n}\longrightarrow1.
\]
So, in the exact oligomorphic profile of this generic atom structure, asymptotically almost every orbit of ordered tuples is injective and avoids the distinguished identity atom.

There is also an exact finite-parameter consequence. If \(A\le L_{\mathrm{SI}}\) is a finite substructure with \(k\) diversity atoms (and hence also the distinguished atom \(e\)), then
\[
\boxed{|S_1(A)|=(k+1)+2^{\binom{k+2}{2}}.}
\]
The first summand gives the algebraic equality types; the second counts all one-point extensions outside \(A\).

## Why the formula holds
In \(\mathrm{FSIAS}_e\), the source has \(f=\mathrm{id}\). Its Peircean condition therefore makes every cycle the full permutation orbit of a triple. The identity axiom fixes exactly the identity cycles \([a,e,a]\). Hence, on a labeled set of \(k\) diversity atoms, the only free decisions are the diversity cycles, one for each unordered multiset of three diversity atoms. There are \(\binom{k+2}{3}\) such multisets, and each cycle is independently consistent or forbidden. Thus a labeled \(k\)-point diversity pattern has exactly \(2^{\binom{k+2}{3}}\) possibilities.

Now consider an ordered \(n\)-tuple. If it uses exactly \(k\) distinct diversity atoms and does not use \(e\), its equality pattern is a partition of \([n]\) into \(k\) blocks, giving \({n\brace k}\) possibilities. If \(e\) occurs, there are \(k\) diversity blocks plus one distinguished nonempty \(e\)-block, giving \((k+1){n\brace k+1}\) possibilities. For either case the free ternary pattern on the \(k\) diversity values contributes \(2^{\binom{k+2}{3}}\). Since
\[
{n\brace k}+(k+1){n\brace k+1}={n+1\brace k+1},
\]
summing over \(k\) gives the displayed formula for \(p_n\).

Ultrahomogeneity identifies tuples exactly when their generated finite substructures, with the tuple coordinates distinguished, are isomorphic; quantifier elimination and \(\aleph_0\)-categoricity identify these orbits with the complete \(\varnothing\)-types. For injective tuples, either all \(n\) entries are diversity atoms, or exactly one coordinate is \(e\), giving the formula for \(a_n\).

For the parameter formula, a new diversity point \(x\notin A\) has free cycles of the forms \([x,x,x]\), \([a,x,x]\), and \([a,b,x]\), where \(a,b\) range over the \(k\) old diversity atoms and repetition is allowed in the last pair. Their number is
\[
1+k+\binom{k+1}{2}=\binom{k+2}{2},
\]
and Koussas's one-point extension axioms realize every choice.

For the asymptotic statement, the \(k=n\) summand of \(p_n\) is \(2^{\binom{n+2}{3}}\). All other summands have exponent at most \(\binom{n+1}{3}\), while their Stirling coefficients sum to at most the Bell number \(B_{n+1}\le(n+1)^{n+1}\). Since
\[
\binom{n+2}{3}-\binom{n+1}{3}=\binom{n+1}{2},
\]
the ratio of the remainder to the leading term tends to zero.

## Assumptions and scope
This is a statement about the Fraïssé limit of the atom-structure class \(\mathrm{FSIAS}_e\) and its complete theory, not an enumeration of finite relation algebras themselves. The source supplies the atom-structure axioms, cycle calculus, amalgamation/Fraïssé construction, \(\aleph_0\)-categoricity, and quantifier elimination. The Stirling type-spectrum formula and exact one-point type count are the synthesis here.

General Stirling-transform formulas for orbit profiles of other homogeneous structures are known, so no novelty is claimed for the counting technique itself. The originality claim is structure-specific: the explicit profile above for Koussas's generic symmetric-integral relation-algebra atom structure.

## Source basis
James Mathew Koussas, “Finite Relation Algebras,” *Journal of Symbolic Logic* 88(2), 874–888, DOI:10.1017/jsl.2021.81. Cambridge University Press first published the article online on 19 October 2021. The publisher lists primary MSC 03G15. In the paper, Definition 7 and Proposition 10 describe \(\mathrm{FSIAS}_e\) and its cycles; Proposition 11 counts diversity cycles; Lemma 25 proves the Fraïssé property; Definition 26 names \(L_{\mathrm{SI}}\) and \(T_{\mathrm{SI}}\); and Corollary 27 gives \(\aleph_0\)-categoricity and quantifier elimination.

## Verification
The bundled exact replay independently enumerates Peircean cycle orbits, exhausts every admissible \(\mathrm{FSIAS}_e\) ternary table through three diversity atoms, checks the atom-structure axioms directly, enumerates set partitions against the Stirling recurrence, and verifies the displayed type and injective-orbit counts. Its recorded output ends with:

```text
VERIFY_OK 66247 exact assertions; all admissible FSIASe tables exhausted through 3 diversity atoms
```
