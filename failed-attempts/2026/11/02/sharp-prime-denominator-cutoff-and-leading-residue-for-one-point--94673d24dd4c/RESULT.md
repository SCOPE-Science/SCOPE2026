# Sharp prime-denominator cutoff and leading residue for one-point Hodge integrals

## Finding
For each integer \(g\ge 2\) and each prime \(p\ge5\) satisfying \(p\le2g+1\), put
\[
s=(p-1)/2,\qquad g=qs+r,\quad q\ge1,\quad0\le r<s,\quad m=q+r,\quad E=q+\nu_p(q!).
\]
For \(0\le i\le g\), define the one-point linear Hodge integral
\[
I_{g,i}=\int_{\overline{\mathcal M}_{g,1}}\psi_1^{2g-2+i}\lambda_{g-i}\in\mathbb Q.
\]
Here \(\nu_p\) denotes the prime-adic valuation, and \(\mathbb Z_{(p)}\) its valuation ring. Then \(p^E I_{g,i}\in\mathbb Z_{(p)}\) for all \(i\), and
\[
 p^E I_{g,i}\equiv0\pmod p\quad\text{for every }m<i\le g,
\]
whereas at the exact cutoff
\[
\boxed{p^E I_{g,m}\equiv
\frac{(-1)^{g+m+q}}{4^g\,r!\,6^r\,U_p(q!)}\not\equiv0\pmod p,}
\qquad U_p(q!)=q!/p^{\nu_p(q!)}.
\]
Thus the reduction of \(p^E\sum_{i=0}^g I_{g,i}x^i\) modulo \(p\) has degree **exactly** \(m=q+r\). Equivalently, among these integrals the smallest Hodge-class index \(g-i\) that realizes the full prime-power denominator \(p^E\) is \(g-m=q(s-1)\), and the displayed congruence gives its leading residue.

## Assumptions and scope
All integrals are rational intersection numbers on the Deligne--Mumford stack of complex stable one-pointed genus-\(g\) curves. Only \(g\ge2\), primes \(p\ge5\) with \(p\le2g+1\), and the specific family with one \(\lambda\)-class and one \(\psi\)-power are asserted. Every congruence between \(p\)-integral rationals is in \(\mathbb Z_{(p)}/p\mathbb Z_{(p)}\). The reduced prime denominator is the exponent \(E\) of the \(p\)-part of the genus-\(g\) Minkowski number, as in Holmes, Lemma 3.3. The statement does not classify every coefficient below the cutoff.

## Proof
Write \(R_g(z)=[t^{2g}](t/\sin t)^z\). By the Faber--Pandharipande identity, the polynomial of Hodge integrals is
\[
H_g(x)=\sum_{i=0}^gI_{g,i}x^i=4^{-g}R_g(x+1).
\]
Let \(z^{\overline j}=z(z+1)\cdots(z+j-1)\) for \(j\ge1\) and \(z^{\overline0}=1\). Expanding \((\sin t/t)^{-z}\) gives
\[
R_g(z)=\sum_{j=0}^gA_{g,j}z^{\overline j},\qquad
A_{g,j}=(-1)^{g+j}\sum_{\substack{\lambda:\ \sum_{a\ge1}a\lambda_a=g\\\sum_a\lambda_a=j}}
\frac1{\prod_{a\ge1}\lambda_a!\,((2a+1)!)^{\lambda_a}}.
\]
The partitions are multiplicity vectors of nonnegative integers, and all sums are finite.

For a partition \(\lambda\) define \(f=\sum_a\lambda_a\lfloor a/s\rfloor\le q\), \(t=q-f\), and \(D(\lambda)=\sum_a\nu_p(\lambda_a!)+\sum_a\lambda_a\nu_p((2a+1)!)\). The factorial bound \(\nu_p((2a+1)!)\le\lfloor a/s\rfloor\) and the multinomial valuation inequality yield
\[
D(\lambda)\le f+\nu_p(f!)+\nu_p((r+st)!).
\]
Indeed, the number of parts with \(a\ge s\) is at most \(f\), while the number of parts with \(a<s\) is at most their total weight, which is at most \(r+st\).

If \(t\ge1\), then \(r+st<(p-1)t\), so Legendre's bound gives \(\nu_p((r+st)!)\le t-1\). Consequently
\[
D(\lambda)\le q+\nu_p(q!)-1=E-1.
\]
If \(t=0\), then \(r<s<p\) implies \(\nu_p(r!)=0\), so the same bound gives \(D(\lambda)\le E\). This proves \(p^EA_{g,j}\in\mathbb Z_{(p)}\) for every \(j\).

If \(t=0\), the number of parts of size at least \(s\) is at most \(q\), and the number below \(s\) is at most \(r\). Therefore the total length \(j\) is at most \(m=q+r\). Equality forces the unique partition \(\lambda^*\) with \(\lambda^*_s=q\), \(\lambda^*_1=r\), and every other multiplicity zero: otherwise one of these two cardinality bounds would be strict, or the total weight would exceed \(qs+r\). Thus every term in \(A_{g,j}\) with \(j>m\), and every term in \(A_{g,m}\) except \(\lambda^*\), has valuation strictly greater than \(-E\).

The unique extremal term has coefficient
\[
\frac{(-1)^{g+m}}{q!\,r!\,(p!)^q\,6^r}.
\]
Since \((p!)/p=(p-1)!\equiv-1\pmod p\), Wilson's theorem gives
\[
p^EA_{g,m}\equiv
\frac{(-1)^{g+m+q}}{r!\,6^r\,U_p(q!)}\not\equiv0\pmod p.
\]
Every rising factorial \(z^{\overline j}\) is monic of degree \(j\), with integer coefficients. Hence the reduced \(p^ER_g(z)\) has degree exactly \(m\), with the displayed leading coefficient. Translation \(z=x+1\) preserves that leading coefficient and degree, and multiplication by \(4^{-g}\) is invertible modulo \(p\). The asserted vanishing, sharp cutoff, and residue follow.

## Verification
The standalone standard-library script `CHECK.py` reconstructs the coefficients of \((\sin t/t)^{-z}\) by exact rational convolutions, changes to the \(x\)-basis, and compares the claimed vanishing and residue in 206 prime/genus combinations (nine primes from \(5\) through \(31\), genera through \(30\)). Running `python CHECK.py` produced `VERIFY_OK 206`. This independent finite calculation tests algebraic normalizations and boundary cases but cannot prove the infinite theorem; the partition argument above is the proof.

## Relationship to prior work
Faber--Pandharipande established the Hodge generating identity. Holmes (2026), Lemmas 3.3--3.5 and Proposition 3.7, computes the global prime-power denominator and proves existence of at least one extremal coefficient. Its proof singles out the partition \(\lambda^*\) at length \(m=q+r\), but its stated conclusion does not identify the largest index of an extremal one-point Hodge integral or its leading residue. The present result upgrades existence to an exact Hodge-degree threshold and unit formula by proving that **all larger lengths** have strictly smaller prime denominators. The extension shares most of its valuation framework with Holmes and could be implicit in prior work; independent priority checking remains needed. Adelberg's work on Nørlund polynomials is a plausible additional source of equivalent arithmetic information and has not been ruled out via full-text comparison.

## Limitations
No statement is made for primes \(2\) or \(3\), or for primes \(p>2g+1\) where the extremal exponent vanishes. The values and prime-denominator behavior for indices below \(m\), all multipoint intersections, and other products of Hodge classes are unclassified. The calculation does not independently validate the Faber--Pandharipande identity or the historical originality of the result.

## References
- Daniel Holmes, *Denominators of Hodge integrals and Minkowski numbers* (2026), arXiv:2610.30274v1, §§3.1--3.2, https://arxiv.org/html/2610.30274v1 .
- Carel Faber and Rahul Pandharipande, *Hodge integrals and Gromov--Witten theory*, Invent. Math. 139 (2000), 173--199, arXiv:math/9810173, https://arxiv.org/abs/math/9810173 .
- Arnold Adelberg, *Arithmetic properties of the Nörlund polynomial*, Discrete Math. 204 (1999), 5--13, DOI:10.1016/S0012-365X(98)00363-X .
