# Exact critical-density exceptions for three consecutive non-square non-primitive elements

## Finding

Let \(q\) be an odd prime power, and let \(\theta_q=\varphi(q-1)/(q-1)\). An element of \(\mathbb F_q\) is *NSNP* if it is a non-square and not a primitive element of \(\mathbb F_q^\times\). A consecutive NSNP triple means \(x,x+1,x+2\) all satisfy this property, with addition in \(\mathbb F_q\).

**Theorem.** Suppose \(\theta_q=1/3\). There is a consecutive NSNP triple in \(\mathbb F_q\) if and only if
\[
q\notin\{7,13,19,25,37,49,73,97,109,163,487,577\}.
\]

Equivalently, for fields whose multiplicative group has precisely the distinct prime divisors \(2\) and \(3\), these twelve field orders are exactly those lacking three consecutive elements in the non-square cubic-residue coset. Both prime fields and non-prime fields occur in the exception list.

## Assumptions and scope

The field order \(q\) is any odd prime power satisfying the exact rational-density condition \(\varphi(q-1)/(q-1)=1/3\). No assertion is made for other values of this density. The root \(x\) of a triple may be any field element. Consecutiveness means field addition by the prime-field unit, not an ordering on a field extension. Non-square excludes zero, and primitive means multiplicative order exactly \(q-1\).

## Proof

**1. Critical-density reduction.** Because \(q\) is odd, \(2\mid(q-1)\). In the reduced rational product \(\varphi(n)/n=\prod_{p\mid n}(p-1)/p\), the largest prime \(P\) dividing \(n\) cannot cancel from the denominator: every numerator factor \(p-1\), for \(p\le P\), is strictly smaller than \(P\). Thus the largest prime dividing the reduced denominator is exactly \(P\). Applying this to \(n=q-1\) and \(\varphi(n)/n=1/3\), we obtain \(P=3\) and the prime support \(\{2,3\}\). Conversely every \(q-1=2^a3^b\) with integers \(a,b\ge1\) gives the specified density. Hence \(q=2^a3^b+1\) and \(\operatorname{char}\mathbb F_q\ge5\).

Choose a primitive element \(g\) of the cyclic multiplicative group. An element \(g^j\) is a non-square exactly when \(j\) is odd. With prime support \(\{2,3\}\), such an element is non-primitive precisely when \(3\mid j\). Therefore the NSNP set is exactly
\[
C_q=\{g^{6t+3}:0\le t<(q-1)/6\},
\]
which is also the set of non-square cubes. Write \(T(q)=\#\{x\in C_q:x+1,x+2\in C_q\}\).

**2. Bound reducing the problem to finitely many fields.** Take a multiplicative character \(\chi\) of order six, with every power including \(\chi^0\) extended to zero by the value zero. Then
\[
\mathbf1_{C_q}(z)=\frac16\sum_{j=0}^{5}(-1)^j\chi^j(z).
\]
Expanding three indicators at \(z=x,x+1,x+2\) gives \(216T(q)\) as a sum over \(216\) index triples \((i,j,k)\in\{0,\ldots,5\}^3\). The zero index triple contributes \(q-3\), since the three excluded roots \(0,-1,-2\) are distinct in characteristic at least five.

For any of the remaining \(215\) index triples, the associated polynomial \(X^i(X+1)^j(X+2)^k\) is not a sixth power, because at least one nonzero exponent lies between one and five. If exactly \(r\in\{1,2,3\}\) exponents are nonzero, the standard Weil multiplicative-character bound gives a complete sum of magnitude at most \((r-1)\sqrt q\); for \(r=1\) that sum vanishes. Restoring the missing restrictions at the roots of the factors with zero exponent changes the sum by at most \(3-r\). Thus the absolute contribution of every nonzero index triple is at most \(2\sqrt q+3\). By the triangle inequality,
\[
216T(q)\ge q-3-215(2\sqrt q+3)=q-648-430\sqrt q.
\]
For \(q>186624=432^2\), the right-hand side is positive: with \(y=\sqrt q>432\), the increasing expression \(y^2-430y-648\) exceeds its value \(216\) at \(y=432\). Therefore every field above the stated cutoff has a triple. The character-sum estimate is used as an *infinite* argument; it is not inferred from finite tests.

**3. Exact finite cutoff.** For \(q\le186624\), the relation \(q=2^a3^b+1\) forces \(1\le a\le15\) and \(1\le b\le10\). Iterate all those exponent pairs satisfying the bound, factor each candidate \(q\), and retain exactly the prime powers. There are \(31\):
\[
\begin{gathered}
7,13,19,25,37,49,73,97,109,163,193,289,433,487,577,769,\\
1153,1297,1459,2593,2917,3457,3889,10369,12289,17497,\\
18433,39367,52489,139969,147457.
\end{gathered}
\]
Of these, exactly three orders are composite: \(25=5^2\), \(49=7^2\), and \(289=17^2\). All three are included and checked as quadratic extension fields.

For prime \(q=p\), compute directly in \(\mathbb F_p\). For \(q=p^2\), represent the field as \(\mathbb F_p[t]/(t^2-d)\), where \(d\) is the least quadratic non-residue modulo \(p\), and enumerate the \(p^2\) pairs of coefficients. Find a generator \(g\) by requiring \(g^{(q-1)/2}\ne1\) and \(g^{(q-1)/3}\ne1\). These two tests suffice because \(q-1\) has no other prime factors. Enumerate \(g^{6t+3}\) for \(0\le t<(q-1)/6\). As an independent membership check, verify that this is exactly the set of nonzero \(z\) with \(z^{(q-1)/2}\ne1\) and \(z^{(q-1)/3}=1\), and exhaustively count the cases \(z+1,z+2\) inside it.

Exactly the twelve field orders displayed in the theorem give \(T(q)=0\). For the other nineteen orders in ascending order, the exact positive counts are
\[
\begin{array}{c|rrrrrrrrrr}
q&193&289&433&769&1153&1297&1459&2593&2917&3457\\
T(q)&2&2&2&8&4&4&4&14&20&16\\\hline
q&3889&10369&12289&17497&18433&39367&52489&139969&147457&\\
T(q)&18&46&64&66&90&152&230&652&640&
\end{array}
\]
The accompanying self-contained program `verify_triples.py` performs this finite exhaustive check, including the complete search for field orders. Its arithmetic is exact and uses only the Python standard library. Together with the preceding infinite character-sum bound, this proves the theorem for every eligible field.

## Verification

Execute `python3 verify_triples.py`. The program enumerates exactly \(31\) prime powers within the proven finite bound, verifies the primitive-generator coset against an independently computed power-membership set in each field, counts all triples in those fields, checks the twelve exceptions, and prints `CERTIFICATE_OK`. The program does not certify the Weil bound by enumeration; its use in the proof is an established theorem with hypotheses reconstructed above.

## Relationship to prior work

Cohen, arXiv:2604.21429v1 (2026), determines the existence of *pairs* of consecutive NSNP elements at the same critical density \(1/3\), with five exceptional fields. Zhou and Wu, arXiv:2607.17267v1 (2026), determine the sharp *general density threshold* \(4/15\) for triples, with three exceptions at that different boundary, and prove a character-sum existence bound. Their finite verification treats the regimes \(\theta_q<4/15\) and \(\theta_q=4/15\), not the disjoint slice \(\theta_q=1/3\). The present theorem determines the exact twelve exceptions in that latter slice; the preceding broad threshold theorem does not imply their classification. Cohen, arXiv:2402.10737v1 (2024), counts consecutive nonsquare triples without requiring each element to be non-primitive, and thus does not supply these cubic-coset exceptions.

## Limitations

The result is restricted to the rational-density class \(\theta_q=1/3\), not a new general density threshold. It relies on the standard Weil character-sum estimate for the infinite range and on exact finite arithmetic for the remaining thirty-one fields. A paper containing an unrecognized equivalent cyclotomic-number table could provide prior coverage; no assertion of independence or comprehensive literature uniqueness is made.

## References

1. Stephen D. Cohen, *Consecutive non-square non-primitive pairs in a finite field*, arXiv:2604.21429v1 (23 April 2026), https://arxiv.org/abs/2604.21429.
2. Juncheng Zhou and Hongfeng Wu, *Consecutive non-square non-primitive tuples in finite fields*, arXiv:2607.17267v1 (19 July 2026), https://arxiv.org/abs/2607.17267.
3. Stephen D. Cohen, *Triples and quadruples of consecutive squares or non-squares in a finite field*, arXiv:2402.10737v1 (16 February 2024), https://arxiv.org/abs/2402.10737.
