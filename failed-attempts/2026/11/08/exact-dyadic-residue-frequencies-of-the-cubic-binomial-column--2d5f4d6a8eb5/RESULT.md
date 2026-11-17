# Exact dyadic residue frequencies of the cubic binomial column

## Finding

For every integer \(k\ge1\), put \(F(n)=\binom{n}{3}\) for \(n\ge0\), and, for each residue \(b\in\mathbb Z/2^k\mathbb Z\), define
\[
M_k(b)=\#\big\{0\le n<2^{k+1}: F(n)\equiv b\pmod{2^k}\big\}.
\]
Then \(2^{k+1}\) is the **least positive period** of \(F(n)\bmod 2^k\), and
\[
\boxed{M_1(0)=3,\quad M_1(1)=1;\qquad
M_k(b)=\begin{cases}5,&b\equiv0\pmod4,\\1,&b\not\equiv0\pmod4\end{cases}\ (k\ge2).}
\]
In particular, every residue occurs, but the multiples of four have five times the frequency of other residues. The natural density of indices attaining \(b\bmod2^k\) is \(M_k(b)/2^{k+1}\). If \(\lambda\) denotes normalized Haar measure on \(\mathbb Z_2\), the pushforward of \(\lambda\) under the continuous function \(F:\mathbb Z_2\to\mathbb Z_2\) is absolutely continuous with exact density
\[
\frac{d(F_*\lambda)}{d\lambda}(y)=\frac12+2\mathbf1_{4\mathbb Z_2}(y).
\]

## Assumptions and scope

All assertions concern the fixed lower binomial index three and powers of the prime two. The ordinary definition \(\binom{n}{3}=0\) for \(0\le n<3\) is used. The polynomial \(F(x)=x(x-1)(x-2)/6\) is integer-valued on \(\mathbb Z_2\); the denominators below are units in \(\mathbb Z_2\). Claims concern all exponents, not merely tested moduli. A period means the least positive \(T\) satisfying \(F(n+T)\equiv F(n)\pmod{2^k}\) for every \(n\ge0\).

## Proof

**1. Four isometric coordinate charts.** Write \(n=4t+r\), where \(t\ge0\) and \(r\in\{0,1,2,3\}\). Direct factorization gives
\[
\begin{aligned}
F(4t)&=4g_0(t),&g_0(t)&=\frac{t(2t-1)(4t-1)}3,\\
F(4t+1)&=2g_1(t),&g_1(t)&=\frac{t(4t-1)(4t+1)}3,\\
F(4t+2)&=4g_2(t),&g_2(t)&=\frac{t(2t+1)(4t+1)}3,\\
F(4t+3)&=1+2g_3(t),&g_3(t)&=\frac{11t+24t^2+16t^3}{3}.
\end{aligned}
\]
For every \(r\), \(g_r(t)\in\mathbb Z_2[t]\), its linear coefficient is odd, its constant term vanishes, and each coefficient of degree at least two is even. Therefore, for any distinct \(u,t\in\mathbb Z_2\),
\[
\frac{g_r(t)-g_r(u)}{t-u}\equiv1\pmod2,
\qquad \nu_2(g_r(t)-g_r(u))=\nu_2(t-u).
\]
(The displayed quotient is integral even at \(t=u\), where it means the divided-difference polynomial.) Thus \(g_r\) induces an injective self-map, hence a permutation, of \(\mathbb Z/2^m\mathbb Z\) for every \(m\ge1\). It also gives a measure-preserving isometry of \(\mathbb Z_2\).

**2. Exact preimages.** Fix \(k\ge2\). As \(n\) traverses \(0\le n<2^{k+1}\), each residue \(r\bmod4\) occurs with \(t\) traversing \(0\le t<2^{k-1}\). The \(r=0\) and \(r=2\) branches are supported exactly on \(b\equiv0\pmod4\). For each such \(b\), the bijectivity of \(g_r\bmod2^{k-2}\) gives \(2\) solutions for \(t\bmod2^{k-1}\) from each branch (for \(k=2\), use the one-element ring modulo \(1\)). The \(r=1\) branch is supported exactly on even \(b\), and contributes exactly one solution, since \(g_1\bmod 2^{k-1}\) is bijective. The \(r=3\) branch is supported exactly on odd \(b\), with one solution from \(g_3\). Consequently \(M_k(b)=2+2+1=5\) for multiples of four; for other even \(b\) it is one, and for odd \(b\) it is one. For \(k=1\), directly \(F(0),F(1),F(2),F(3)\equiv0,0,0,1\pmod2\).

**3. Least period.** The four branch factorizations show that replacing \(n\) with \(n+2^{k+1}\) leaves its image modulo \(2^k\) unchanged for each \(k\ge1\), so \(2^{k+1}\) is a period. For \(k\ge2\), take \(n=3\) and the shift \(2^k\). The isometry of \(g_3\) gives
\[
\nu_2\big(F(3+2^k)-F(3)\big)
=1+\nu_2\big(g_3(2^{k-2})-g_3(0)\big)=k-1.
\]
Hence \(2^k\) is not a period. Since every period of a periodic integer sequence is a multiple of its least period, and its least period divides \(2^{k+1}\), the least period is \(2^{k+1}\). For \(k=1\) the four displayed initial values show that the period is \(4\), not \(2\).

**4. Densities and two-adic law.** Periodicity gives the density \(M_k(b)/2^{k+1}\) for every residue \(b\). Relative to Haar density \(2^{-k}\) per residue, the Radon–Nikodym factor is \(5/2\) on multiples of four and \(1/2\) elsewhere, simultaneously for every \(k\ge2\). These consistent cylinder measures define the asserted pushforward. Equivalently, it follows by conditioning Haar measure on the four classes modulo four and using the isometries of \(g_r\).

## Verification

Run the standalone standard-library script `verify.py` with Python 3. It independently enumerates the exact residue counts at all \(2^k\) for \(1\le k\le13\), checks least periods, verifies chart factorizations and bijections, and compares the uniform law of the two lower binomial columns. This is a finite corroboration, not an infinite proof. The infinite proof consists of the four polynomial factorizations and odd divided differences above.

## Relationship to prior work

Sun and Zhang established the density of fixed-index binomial coefficient values in the two-adic integers and gave an induction that constructs residue witnesses (Theorem 1.1 and Corollary 1.2 of [1]). That implies the **image** here is all residues, so surjectivity is not claimed as new. The proof's unit-slope lifting construction is related, but the statement and proof inspected do not specify the complete fiber counts, their five-to-one imbalance, or the minimum period for the fixed index three.

Barat and Grabner [2] study residue and valuation distributions of **two-parameter families** of binomial coefficients throughout Pascal's triangle; their Sections 3 and 4 sum over varying upper and lower indices. Those asymptotic statements are not identical to, nor do they directly specify, the fixed-column Haar pushforward here.

For comparison, the columns \(\binom n1\) and \(\binom n2\) are exactly uniform modulo \(2^k\) for every \(k\): the first is the identity, while the two branches \(\binom{2t}{2}=t(2t-1)\) and \(\binom{2t+1}{2}=t(2t+1)\) are each two-adic isometries. The present result therefore identifies the earliest fixed lower index with nonuniform dyadic residue frequencies. An overlooked equivalent result remains a historical-priority risk.

## Limitations

No analogous claim is made for a different prime or an arbitrary fixed lower binomial index. This result does not assert a general classification theorem for all fixed columns, and gives no lower bound on discrepancy outside periodic residues. Priority is qualified by the possibility of an unlocated equivalent treatment. Only self-review has been performed; independent audit has not yet been performed.

## References

[1] Zhi-Wei Sun and Wei Zhang, *Binomial coefficients and the ring of \(p\)-adic integers*, arXiv:0812.3089 (first public version 16 December 2008), especially Theorem 1.1, Corollary 1.2 and Section 2. https://arxiv.org/abs/0812.3089

[2] Guy Barat and Peter J. Grabner, *Distribution of binomial coefficients and digital functions*, Journal of the London Mathematical Society 64 (2001), 523–547, DOI:10.1112/S0024610701002630; author's lawful full text https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf
