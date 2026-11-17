# No reciprocal two-cycles for the sixth cyclotomic polynomial

## Finding
Write \(F(t)=t^2-t+1=\Phi_6(t)\). For **every** pair of positive integers \(a,b\),
\[
a\mid F(b)\ \text{and}\ b\mid F(a)\quad\Longleftrightarrow\quad a=b=1.
\]
Thus, for distinct primes \(p,q\), the simultaneous relations \(p\mid F(q)\) and \(q\mid F(p)\) are impossible. This rules out the entire squarefree two-prime cycle configuration considered in Proposition 1 of De Koninck--Letendre (2026); it does not rule out their mixed prime-square configurations.

Define \(\mathcal H(n)=\sum_{j=1}^{n}\gcd(n,j)^{-1}\). If \(n>1\) is **squarefree** and \(\mathcal H(n)\) is an integer, then every prime factor of \(n\) is \(1\pmod6\), and \(\omega(n)\ge3\). In the directed graph with vertices the primes dividing \(n\) and edges \(p\to q\) whenever \(p\mid F(q)\), every vertex has an outgoing edge, but loops and two-cycles are absent. Hence any directed cycle has length at least three.

## Assumptions and scope
All divisibility relations are in positive integers. The two-cycle statement applies to *all* positive integer pairs, prime or composite. The corollary about \(\mathcal H(n)\) requires squarefreeness; no conclusion is claimed for prime-square factors or the full set of integer-valued \(\mathcal H\) at nonsquarefree arguments. The condition that all prime factors are \(1\pmod6\) is necessary but not sufficient for integrality.

## Proof
**Step 1 (coprimality and a fixed integer).** Assume \(a\mid F(b)\) and \(b\mid F(a)\). Any common divisor \(d\) of \(a,b\) also divides \(F(a)\equiv1\pmod d\), so \(\gcd(a,b)=1\). Put
\[
M=\frac{F(a)+F(b)-1}{ab}=\frac{a^2+b^2-a-b+1}{ab}.
\]
The numerator is \(0\pmod a\) because \(F(a)\equiv1\pmod a\) and \(a\mid F(b)\); likewise it is \(0\pmod b\). Coprimality makes \(M\) a positive integer. Moreover
\[
M=1+\frac{(a-b)^2+(a-1)(b-1)}{ab},
\]
so \(M=1\) is possible only for \(a=b=1\).

**Step 2 (strict descent preserving \(M\)).** If \(a=b\), then \(a\mid F(a)\equiv1\pmod a\), hence \(a=b=1\). Otherwise interchange variables so \(1\le a<b\). Since \(b\mid F(a)\), the integer
\[
r=\frac{F(a)}b
\]
is positive. As \(F(a)=a^2-a+1<ab\) for \(1\le a<b\), one has \(1\le r<a\). The defining identity for \(M\) can be read as a monic quadratic with root \(b\):
\[
z^2-(Ma+1)z+F(a)=0.
\]
By the product-of-roots identity, \(r\) is its second root. Therefore
\[
r^2-(Ma+1)r+F(a)=0,
\]
which rearranges to \(F(r)+F(a)-1=Mar\). Furthermore \(br=F(a)\equiv1\pmod a\), so \(\gcd(a,r)=1\). The last equality implies \(a\mid F(r)\) and \(r\mid F(a)\), and the new pair \((r,a)\) has the same integer \(M\). Its maximum has strictly decreased from \(b\) to \(a\).

Repeated descent of a nontrivial pair would end at an equal positive pair, necessarily \((1,1)\), but the preserved integer would then be \(M=1\), contradicting the strict positivity of \((a-b)^2+(a-1)(b-1)\) at the initial nontrivial pair. Thus only \((1,1)\) satisfies the reciprocal divisibilities, and that pair clearly does.

**Step 3 (squarefree reciprocal-gcd sums).** For squarefree \(n\), the multiplicative identity established in De Koninck--Letendre gives
\[
\mathcal H(n)=\frac{\prod_{p\mid n}F(p)}n.
\]
If \(\mathcal H(n)\) is integral, each prime \(p\mid n\) divides \(F(q)\) for some other prime \(q\mid n\), because \(F(p)\equiv1\pmod p\). For \(p>3\), a root \(x\pmod p\) of \(F(x)\) has multiplicative order exactly six: \((x+1)F(x)=x^3+1\equiv0\pmod p\), but \(x\not\equiv-1\pmod p\) as \(F(-1)=3\), so \(x^3=-1\) and \(x^6=1\) with order six. Hence \(p\equiv1\pmod6\). The prime \(2\) is impossible as \(F(x)\) is always odd. If \(3\mid n\), some distinct \(q\mid n\) would satisfy \(F(q)\equiv0\pmod3\), requiring \(q\equiv2\pmod3\). Such a prime cannot belong to \(n\): the prime \(2\) was already excluded, and each odd prime \(q\equiv2\pmod3\) has no incoming \(F\)-divisibility by the order-six argument. This contradicts integrality. Thus all prime factors are \(1\pmod6\).

Finally choose, for each prime \(p\mid n\), one outgoing edge \(p\to q\) with \(p\mid F(q)\). A finite functional digraph contains a directed cycle. There are no loops because \(p\nmid F(p)\), and no two-cycles by Steps 1--2. Therefore every cycle has length at least three and \(\omega(n)\ge3\).

## Verification
A standalone exact-arithmetic checker `verify.py` checks reciprocal divisibility over all positive first coordinates up to \(5000\) and all divisors of their cyclotomic values; verifies \(\mathcal H(n)=h(n)/n\) by direct rational summation for \(1\le n\le350\); and checks the published example \(614341=7\cdot13\cdot43\cdot157\). It prints `VERIFY_OK` on success. The infinite conclusions follow from the descent and order arguments, not finite enumeration.

## Relationship to prior work
De Koninck and Letendre, *The Integer Values of ...* (arXiv:2610.10572v1, first posted 2026-10-04), establish the reciprocal-gcd-sum identity and analyze functional graphs of divisibility. Their Section 5, Proposition 1, bounds the number of prime pairs satisfying precisely the reciprocal sixth-cyclotomic divisibilities, but does not state that this subcase is empty. The present result gives a structural nonexistence theorem in that subcase, not an improvement to the paper's overall \(X^{2/3+o(1)}\) count. The OEIS entry A317480 records the underlying integer-valued set, not this exclusion. Lemmermeyer (arXiv:2601.15229v1) discusses Vieta jumping for other quadratic conics, not the inhomogeneous equation \(a^2+b^2-a-b+1=Mab\). The use of Vieta jumping itself is classical and not claimed as novel.

## Limitations
This is a special, elementary rigidity theorem, not a determination of whether infinitely many integers have integral \(\mathcal H(n)\). It does not exclude two-cycles involving valuations \(p^2\) or prove that squarefree examples need four primes. No independent audit or exhaustive historical-priority certification has been made. Older literature on reciprocal divisibility and quadratic descent may contain equivalent statements.

## References
1. J.-M. De Koninck and P. Letendre, *The Integer Values of the Sum of Reciprocal GCDs*, arXiv:2610.10572v1 (2026-10-04). https://arxiv.org/html/2610.10572v1
2. F. Lemmermeyer, *Vieta jumping and small norms in quadratic number fields*, arXiv:2601.15229v1 (2026-01-21). https://arxiv.org/html/2601.15229v1
3. OEIS A317480, *Numbers m such that Sum of reciprocal gcds is an integer*. https://oeis.org/A317480
