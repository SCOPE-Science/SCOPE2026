# Equal unit groups and different Loewy lengths in two-variable complete intersections

## Finding

Let \(p\) be any odd prime and \(k=\mathbb F_{p^f}\) for any \(f\ge1\). The two rings
\[
R=k[x,y]/(x^{p-1},y^{2p}),\qquad
S=k[x,y]/(x^p,y^{2p-2})
\]
are local Gorenstein complete intersections of dimension \(2p(p-1)\) over the same residue field \(k\), with embedding dimension two and one-dimensional socle. Their full abstract unit groups are isomorphic:
\[
R^\times\cong S^\times\cong C_{p^f-1}\times (C_p)^{f(2p(p-1)-3)}\times(C_{p^2})^f,
\]
where \(C_n\) denotes the cyclic group of order \(n\). Their Loewy lengths are \(3p-2\) and \(3p-3\), respectively, so the rings are not isomorphic. Thus the unit group does not determine the Loewy length in this class, even with equal algebra dimensions and with a principal-unit group of exponent \(p^2\).

## Assumptions and scope

The group isomorphism is abstract, not a map of rings. The Loewy length of a finite local ring with maximal ideal \(\mathfrak m\) is the smallest positive \(L\) such that \(\mathfrak m^L=0\). The example is restricted to odd characteristic. No general unit-group classification or minimal collision dimension is claimed.

## Proof

Consider \(A=k[x,y]/(x^a,y^b)\) in the band \(2\le a\le p<b\le2p\). Its standard monomials \(x^iy^j\) with \(0\le i<a\), \(0\le j<b\) form a basis. The maximal ideal is \((x,y)\), which is nilpotent, and \(A^\times=k^\times\times U\) for the abelian principal-unit group \(U=1+\mathfrak m\). This group has order \(p^{f(ab-1)}\).

For \(u\in\mathfrak m\), let \(c_y\) be its coefficient of \(y\). Every monomial involving \(x\) has zero \(p\)-th power, as does every \(y^j\) with \(j\ge2\). In contrast \(y^p\ne0\). Therefore \((1+u)^p=1+c_y^p y^p\). Every value of \(c_y^p\) occurs because Frobenius permutes \(k\). Thus \(|U^p|=p^f\), and \(U^{p^2}=1\). The finite abelian group decomposition gives exactly \(f\) cyclic factors of order \(p^2\), and the total order gives \(f(ab-3)\) factors of order \(p\). This explains why within the band the unit group sees the product \(ab\), whereas the Loewy length sees the sum \(a+b\).

The two given exponent pairs lie in this band for every odd prime and both have product \(2p(p-1)\). Each is a complete intersection because the powers of the two distinct variables form a regular sequence in \(k[x,y]\). The classes of \(x\) and \(y\) modulo \(\mathfrak m^2\) are linearly independent, and the socle is precisely the span of \(x^{a-1}y^{b-1}\): to be annihilated by \(x\) and \(y\) requires support at both maximal exponents. This proves the Gorenstein assertion and also shows that the top nonzero radical degree is \(a+b-2\). The two sums give the claimed Loewy lengths. For example, at \(p=3\) the pairs are \((2,6)\) and \((3,4)\), with lengths 7 and 6, and the common group over \(\mathbb F_3\) is \(C_2\times C_3^9\times C_9\).

## Relationship to prior work

The principal-unit computation is an elementary application of Frobenius and the finite abelian group decomposition. More generally, dividing the standard monomials into primitive rays gives the classical one-variable principal-unit factors, consistent with the truncation-set Witt-vector splitting in Angeltveit–Gerhardt–Hill–Lindenstrauss, §2, Lemma 2.3 ([arXiv:1206.0247](https://arxiv.org/abs/1206.0247)). Their main \(K\)-theory results concern multirelative groups, not this reconstruction question. Chebolu–Corry–Grimm–Hatfield ([arXiv:2112.03853](https://arxiv.org/abs/2112.03853), Theorems 1.1 and 1.3) treat elementary abelian unit groups. The claim here is the explicit uniform pair with non-elementary principal units, matching the other listed invariants while differing in Loewy length. Priority for the particular counterexamples relative to unindexed examples is not asserted absolutely.
