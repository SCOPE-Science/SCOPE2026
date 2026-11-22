# Exact 2–3-smooth equidistribution of normalized primitive Pythagorean areas

## Finding

Let \(\mathcal T(X)\) be the set of **unordered** primitive positive integral right triangles with hypotenuse \(c\le X\). Let \(A=ab/2\) be the integer area, and write \(J=A/6\), which is an integer. For each integer modulus \(Q\ge1\) and residue \(t\pmod Q\), define

\[
N_Q(t;X)=\#\{T\in\mathcal T(X):J(T)\equiv t\pmod Q\}.
\]

**Theorem (complete uniform-modulus classification).** The values of \(N_Q(t;X)\) are asymptotically equidistributed among all residues \(t\pmod Q\) if and only if \(Q=2^a3^b\) with \(a,b\ge0\). For every such \(Q\), uniformly over the finitely many residues,

\[
N_Q(t;X)=\frac{X}{2\pi Q}+O_Q\!\left(\sqrt X\log(2X)\right).
\]

The positive result rests on the following **exact, all-level** local statement. Put \(M=6Q\). Among all ordered pairs \((m,n)\pmod M\) satisfying \(m+n\) odd and \((m,n)\not\equiv(0,0)\pmod3\), each congruence

\[
mn(m^2-n^2)\equiv6t\pmod M
\]

has exactly \(16Q\) solutions, independently of \(t\pmod Q\).

For every prime \(p\ge5\), a different exact local count yields

\[
\lim_{X\to\infty}\frac{\#\{T\in\mathcal T(X):p\mid J(T)\}}{\#\mathcal T(X)}=\frac4{p+1}>\frac1p.
\]

Thus any modulus with such a prime factor fails equidistribution.

## Assumptions and scope

Every triangle is counted once, irrespective of the order of its legs. The standard Euclidean parametrization gives a bijection between these triangles and integer pairs \(m>n>0\), with \(\gcd(m,n)=1\), \(m+n\) odd and \(m^2+n^2\le X\). The legs are \(m^2-n^2\) and \(2mn\), the hypotenuse is \(m^2+n^2\), and the area is

\[
F(m,n)=mn(m^2-n^2)=mn(m-n)(m+n).
\]

The divisibility \(6\mid F(m,n)\) follows from the opposite-parity condition and the fact that every nonzero pair modulo three lies on one of the four lines \(m=0\), \(n=0\), \(m=n\), or \(m=-n\). The word *uniform* refers to the limiting frequency when triangles are ordered by increasing hypotenuse, not to equal counts at finite \(X\). All error constants may depend on fixed \(Q\).

## Proof

**1. Dyadic exact fibers.** For \(e\ge1\), fix an odd \(m\) and take even \(n,n'\) modulo \(2^e\). Direct factorization gives

\[
F(m,n)-F(m,n')=m(n-n')\bigl(m^2-n^2-nn'-n'^2\bigr).
\]

The factor multiplying \(n-n'\) is odd. Consequently, the map \(n\mapsto F(m,n)\) is an isometry of the even residue classes modulo \(2^e\), hence permutes them. Each even output has one preimage for every odd \(m\), giving \(2^{e-1}\) pairs in this parity branch. The branch with even \(m\) and odd \(n\) has the same count by antisymmetry \(F(n,m)=-F(m,n)\). Every even residue has therefore exactly \(2^e\) opposite-parity preimages, and every odd residue has none.

**2. Ternary exact fibers.** Let \(e\ge1\). Every pair \((m,n)\not\equiv(0,0)\pmod3\) lies on exactly one of the four zero-lines of \(F\) in the projective line over \(\mathbb F_3\). Thus \(F\equiv0\pmod3\). Its gradient

\[
\left( n(3m^2-n^2),\ m(m^2-3n^2)\right)
\]

is nonzero modulo three at every such pair: if \(n\) is a unit, the first component is \(-n^3\), while if \(n\equiv0\), the second is \(m^3\). Given any lift of an admissible pair from modulus \(3^j\) to \(3^{j+1}\), the first-order change in \(F\) is a nonzero linear functional of the two new base-three digits. Therefore exactly three of the nine lifts hit a prescribed next digit of a target divisible by three. Since there are eight admissible pairs modulo three, every target divisible by three has exactly \(8\cdot3^{e-1}\) primitive-mod-three preimages modulo \(3^e\). No other target occurs.

**3. Chinese remaindering and the exact certificate.** Write \(Q=2^a3^b\) with \(a,b\ge0\), so that \(M=2^{a+1}3^{b+1}\). The two local results and the Chinese remainder theorem give, for each \(t\pmod Q\),

\[
\underbrace{2^{a+1}}_{\text{mod }2^{a+1}}
\underbrace{(8\cdot3^b)}_{\text{mod }3^{b+1}}
=16Q
\]

locally admissible pairs with \(F\equiv6t\pmod M\). There are exactly \(16Q^2\) locally admissible parameter pairs modulo \(M\) in total.

**4. Archimedean counting with coprimality.** Let \(\mathcal S_X=\{(m,n)\in\mathbb R^2:0<n<m,\ m^2+n^2\le X\}\). Its area is \(\pi X/8\), and its boundary has length \(O(\sqrt X)\). In any fixed residue class modulo \(M\), the lattice count in \(\mathcal S_{X/d^2}\) is

\[
\frac{\pi X}{8M^2d^2}+O_M(\sqrt X/d+1).
\]

For a locally admissible pair modulo \(M\), any common divisor \(d\) must be coprime to six. Apply Möbius inversion over \(d\le\sqrt X\), using that multiplication by the inverse of \(d\) permutes the locally admissible classes and preserves the congruence after the original variables are restored. Summing over the \(16Q\) classes giving a fixed target, and using

\[
\sum_{\substack{d\ge1\\(d,6)=1}}\frac{\mu(d)}{d^2}
=\prod_{p\ge5}\left(1-\frac1{p^2}\right)=\frac9{\pi^2},
\]

produces

\[
\frac{16Q}{(6Q)^2}\cdot\frac{\pi X}{8}\cdot\frac9{\pi^2}
=\frac{X}{2\pi Q}.
\]

The boundary errors and the tail of the absolutely convergent divisor sum total \(O_Q(\sqrt X\log(2X))\). The same argument without a prescribed target gives \(\#\mathcal T(X)=X/(2\pi)+O(\sqrt X\log(2X))\).

**5. Sharp necessity.** For each prime \(p\ge5\), the admissible Euclidean parameter pairs modulo \(p\) are all \(p^2-1\) nonzero pairs. As \(6\) is invertible, \(p\mid J\) is equivalent to \(F\equiv0\pmod p\). The four distinct lines \(m=0\), \(n=0\), \(m=n\), and \(m=-n\) contribute exactly \(4(p-1)\) nonzero pairs. The same congruence-class Möbius argument shows that the limiting probability is \(4(p-1)/(p^2-1)=4/(p+1)\), unlike \(1/p\). If \(p\mid Q\), uniformity modulo \(Q\) would force uniformity modulo \(p\), a contradiction. Therefore no additional prime is allowed, completing the classification.

## Verification

The companion `check_area.py` uses independent exhaustive congruence enumeration at dyadic depths one through seven, ternary depths one through five, multiple composite moduli up to \(6\cdot2^a3^b\le500\), and primes five through seventeen. It also enumerates primitive right triangles under a finite hypotenuse cutoff to check the predicted local support and approximate equal frequencies. The program reports `CHECK_OK 41 test families`. These tests are finite consistency checks; the all-modulus and asymptotic conclusions follow from the preceding proofs, not enumeration.

## Relationship to prior work

Euclid's parametrization is classical. Romik (2004, §§1 and 4.2) studies expansions and angular statistics of primitive Pythagorean triangles and proves an asymptotic primitive-pair lattice density. Liu (2010, Theorems 1.1–1.3 and §§2,4) studies global hypotenuse/perimeter/area-cutoff counts, not the residual distribution of \(A/6\). Buckley (2012, pp. 6–8) proves compulsory divisibility of triangle area by six, without an all-level local fiber law. Kontorovich–Oh (2010, §§2.3 and 5.2) discuss prime divisors and four-component local sieve obstructions for the normalized area in thin Pythagorean orbits; this already anticipates the odd-prime obstruction, but does not supply the uniform 2- and 3-adic pushforward or the complete maximal-modulus classification for the full primitive family. The new distinction is the exact local flatness at every 2- and 3-adic depth and the resulting if-and-only-if congruence classification under hypotenuse ordering.

## Limitations

The error bound is for each *fixed* modulus; no uniform-in-\(Q\) range is claimed. The theorem concerns primitive integral triangles counted with multiplicity as triangles, not distinct numerical area values. It does not claim equidistribution modulo primes five and above, and in fact proves an explicit obstruction. Exhaustive finite checks cannot prove an infinite statement. Historical priority may be affected by implicit equivalent local-density calculations in general sieve or congruence literature; no independent verification has been performed.

## References

1. D. Romik, *The dynamics of Pythagorean triples*, arXiv:math/0406512 (first public version 25 June 2004), https://arxiv.org/abs/math/0406512.
2. K. Liu, *On the distribution of primitive Pythagorean triangles*, Acta Arithmetica **144** (2010), 135–150, DOI: 10.4064/aa144-2-3, https://www.impan.pl/shop/publication/transaction/download/product/82319.
3. W. Buckley, *A note on the area and volume of right-angled triangles with integer sides*, Notes on Number Theory and Discrete Mathematics **18** (2012), 6–8, https://nntdm.net/papers/nntdm-18/NNTDM-18-1-06-08.pdf.
4. A. Kontorovich and H. Oh, *Almost prime Pythagorean triples in thin orbits*, arXiv:1001.0370 (3 January 2010), https://arxiv.org/abs/1001.0370.
