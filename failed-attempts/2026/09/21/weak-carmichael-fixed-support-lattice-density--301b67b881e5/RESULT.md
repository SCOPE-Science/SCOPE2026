# Fixed-support exponent lattices and primitive density for weak Carmichael numbers

## Statement

A composite positive integer \(n\) is a **weak Carmichael number** if it satisfies the standard weak-Carmichael congruence. By the Borwein--Wong criterion, equivalently
\[
p-1\mid n-1\qquad\text{for every prime }p\mid n.
\]
Meštrović calls a weak Carmichael number **primitive** if it is not \(m^f\) for any weak Carmichael number \(m\) and any integer \(f\ge2\).

Fix a set of \(s\ge2\) distinct odd primes
\[
S=\{p_1,\dots,p_s\}.
\]
Call \(S\) **admissible** if
\[
p_j\nmid p_i-1\qquad(i\ne j).
\]
This is exactly the known support condition for the existence of weak Carmichael numbers with prime support \(S\).

For admissible \(S\), define
\[
G_S=\prod_{i=1}^s (\mathbb Z/(p_i-1)\mathbb Z)^\times
\]
and the homomorphism
\[
\Psi_S:\mathbb Z^s\longrightarrow G_S,
\qquad
\Psi_S(e_1,\dots,e_s)_i
=
\prod_{j\ne i}p_j^{e_j}\pmod{p_i-1}.
\]
Let
\[
\Lambda_S=\ker\Psi_S,
\qquad
I_S=[\mathbb Z^s:\Lambda_S]=|\operatorname{im}\Psi_S|.
\]

### Theorem 1: exponent-lattice structure

The weak Carmichael numbers having **exactly** the prime support \(S\) are in bijection with
\[
\Lambda_S\cap\mathbb Z_{>0}^s
\]
through
\[
(e_1,\dots,e_s)\longmapsto \prod_{i=1}^s p_i^{e_i}.
\]
Thus the exponent vectors for a fixed admissible support form the positive part of a full-rank finite-index lattice.

Moreover, such a weak Carmichael number is primitive if and only if its exponent vector is a primitive vector of the lattice \(\Lambda_S\), meaning
\[
e\notin f\Lambda_S\qquad\text{for every }f\ge2.
\]
Equivalently, if \(b_1,\dots,b_s\) is any \(\mathbb Z\)-basis of \(\Lambda_S\) and
\[
e=c_1b_1+\cdots+c_sb_s,
\]
then primitiveness is exactly
\[
\boxed{\gcd(c_1,\dots,c_s)=1.}
\]

### Theorem 2: universal primitive density at fixed support

Let \(W_S(X)\) be the number of weak Carmichael numbers \(n\le X\) with prime support exactly \(S\), and let \(P_S(X)\) count the primitive ones. Then, as \(X\to\infty\),
\[
\boxed{
W_S(X)=
\frac{(\log X)^s}
{s!\,I_S\prod_{i=1}^s\log p_i}
+O_S((\log X)^{s-1}).
}
\]
Also
\[
\boxed{
P_S(X)=
\frac{1}{\zeta(s)}
\frac{(\log X)^s}
{s!\,I_S\prod_{i=1}^s\log p_i}
+
\begin{cases}
O_S(\log X\log\log X),&s=2,\\
O_S((\log X)^{s-1}),&s\ge3.
\end{cases}
}
\]
Consequently,
\[
\boxed{
\frac{P_S(X)}{W_S(X)}\longrightarrow\frac1{\zeta(s)}.
}
\]
The limiting primitive proportion depends only on the number \(s\) of distinct prime factors, not on the particular admissible prime support.

## Proof of Theorem 1

For
\[
n(e)=\prod_{j=1}^s p_j^{e_j},\qquad e_j\ge1,
\]
the Borwein--Wong criterion says that \(n(e)\) is weak Carmichael if and only if
\[
n(e)\equiv1\pmod{p_i-1}\qquad(1\le i\le s).
\]
Since \(p_i\equiv1\pmod{p_i-1}\), the \(i\)-th congruence is
\[
\prod_{j\ne i}p_j^{e_j}\equiv1\pmod{p_i-1},
\]
which is exactly \(\Psi_S(e)=1\). Hence the exponent vectors are precisely
\[
\Lambda_S\cap\mathbb Z_{>0}^s.
\]
Because \(G_S\) is finite, \(\Lambda_S\) has finite index and full rank. Admissibility guarantees that every displayed residue is a unit. Conversely, if \(p_j\mid p_i-1\) for some \(i\ne j\), then any integer divisible by \(p_j\) is \(0\pmod{p_j}\), so it cannot be \(1\pmod{p_i-1}\); this recovers the known support obstruction.

Now suppose \(n(e)=m^f\) with \(f\ge2\) and \(m\) a weak Carmichael number. Unique factorization forces \(m\) to have the same prime support and exponent vector \(e/f\in\mathbb Z_{>0}^s\). The first part then says that \(m\) is weak Carmichael exactly when
\[
e/f\in\Lambda_S,
\]
i.e. exactly when \(e\in f\Lambda_S\). This proves the lattice-primitivity criterion.

Finally, after choosing a \(\mathbb Z\)-basis of \(\Lambda_S\), membership in \(f\Lambda_S\) is equivalent to divisibility of every basis coordinate \(c_i\) by \(f\). Thus no such \(f\ge2\) exists exactly when \(\gcd(c_1,\dots,c_s)=1\).

## Proof of Theorem 2

Put
\[
a_i=\log p_i,\qquad L=\log X.
\]
Then \(n(e)\le X\) is equivalent to
\[
a_1e_1+\cdots+a_se_s\le L.
\]
Hence \(W_S(X)\) counts points of the fixed full-rank lattice \(\Lambda_S\) in the expanding simplex
\[
\mathcal R_L=
\{x\in\mathbb R^s:x_i\ge1,\ a_1x_1+\cdots+a_sx_s\le L\}.
\]
The lattice covolume is \(I_S\). The standard Lipschitz lattice-point estimate (applied after translating by \((1,\dots,1)\)) gives the uniform form
\[
\#(\Lambda_S\cap\mathcal R_Y)
=
\frac{\operatorname{vol}(\mathcal R_Y)}{I_S}
+O_S(Y^{s-1}+1)
\qquad(Y\ge0).
\]
Taking \(Y=L\) yields the required count.
The translation \(x_i\ge1\) changes only lower-order terms, while
\[
\operatorname{vol}(\mathcal R_L)
=
\frac{L^s}{s!\prod_i a_i}+O_S(L^{s-1}).
\]
This proves the formula for \(W_S(X)\).

For a nonzero vector \(e\in\Lambda_S\), let its lattice content be the largest positive integer \(d\) such that \(e\in d\Lambda_S\). By Theorem 1, primitive weak Carmichael numbers correspond exactly to lattice content \(1\). Möbius inversion therefore yields
\[
P_S(e^L)=
\sum_{d\ge1}\mu(d)\,W_S(e^{L/d}),
\]
where only \(d=O_S(L)\) contribute. Substituting the first asymptotic gives the main term
\[
\frac{L^s}{s!I_S\prod_i a_i}
\sum_{d\ge1}\frac{\mu(d)}{d^s}
=
\frac{1}{\zeta(s)}
\frac{L^s}{s!I_S\prod_i a_i}.
\]
For \(s=2\), summing the boundary error gives \(O_S(L\log L)\). For \(s\ge3\), the series \(\sum d^{1-s}\) converges, giving \(O_S(L^{s-1})\). Truncating the absolutely convergent main series contributes only a smaller \(O_S(L)\) term. This proves the primitive asymptotic and the ratio limit.

## Explicit two-prime corollary

Let \(p<q\) be odd primes with \(p\nmid q-1\), and set
\[
u=\operatorname{ord}_{q-1}(p),
\qquad
v=\operatorname{ord}_{p-1}(q).
\]
Meštrović's Proposition 2.36 gives
\[
p^a q^b\text{ weak Carmichael}
\iff
u\mid a\text{ and }v\mid b.
\]
Here
\[
\Lambda_{\{p,q\}}=u\mathbb Z\times v\mathbb Z,
\qquad I_{\{p,q\}}=uv.
\]
Therefore
\[
\boxed{
p^{ur}q^{vs}\text{ is primitive weak Carmichael}
\iff \gcd(r,s)=1.}
\]
In particular,
\[
P_{p,q}(X)
=
\frac{3(\log X)^2}{\pi^2uv\log p\log q}
+O_{p,q}(\log X\log\log X),
\]
and primitive numbers form asymptotic proportion \(6/\pi^2\) among the weak Carmichael numbers on that support.

For \((p,q)=(3,5)\), one has \((u,v)=(2,1)\). Thus all fixed-support weak Carmichael numbers are \(3^{2r}5^s\), and primitiveness is exactly \(\gcd(r,s)=1\). This explains, for example,
\[
45=3^2\cdot5\quad\text{and}\quad225=3^2\cdot5^2
\]
as primitive, while
\[
2025=3^4\cdot5^2=45^2
\]
is not; meanwhile
\[
18225=3^6\cdot5^2
\]
is primitive because \(\gcd(3,2)=1\).

For three or more primes, lattice primitiveness can differ substantially from ordinary gcd of the standard exponents. For example, on support \(\{3,11,17\}\), the vector \((2,2,6)\) lies in \(\Lambda_S\) and is primitive in that lattice. Hence
\[
3^2\,11^2\,17^6
\]
is a primitive weak Carmichael number even though it is a perfect square: its square root has exponent vector \((1,1,3)\), which does not lie in \(\Lambda_S\).

## Exact bounded verification

The standalone script `artifacts/verify.py` checks the weak-Carmichael congruences directly on exponent vectors for five admissible supports. Across 2,184 bounded exponent vectors it finds 508 weak Carmichael vectors and 363 primitive ones. For the two two-prime supports it separately checks the normalized-gcd criterion above and reports zero mismatches.

The script also computes the finite image size \(I_S\) from coordinate periods and compares exact logarithmic-height counts with the predicted leading lattice-volume term and primitive proportions for \(S=\{3,5\}\) and \(S=\{3,11,17\}\). The observed ratios move toward \(1/\zeta(2)\) and \(1/\zeta(3)\), respectively. These finite checks support the formulas but are not used in place of the proofs.

## Literature context and originality

The Borwein--Wong criterion, as restated by Meštrović, characterizes weak Carmichael numbers by \((p-1)\mid(n-1)\) for every prime divisor. Meštrović's 2013 paper also records the pairwise support obstruction/construction, introduces primitive weak Carmichael numbers, and gives the exact two-prime exponent divisibility criterion in Proposition 2.36. Those ingredients are prior work and are not claimed here.

The contribution here is the fixed-support **kernel-lattice formulation for arbitrary support**, its exact interpretation of Meštrović primitiveness as lattice primitiveness, and the resulting logarithmic-height asymptotics showing the universal fixed-support primitive proportion \(1/\zeta(s)\). The explicit normalized-gcd criterion for two-prime support is a concrete corollary.

Targeted searches for weak Carmichael exponent lattices, primitive weak Carmichael density, fixed-prime-support asymptotics, and zeta-density formulations did not locate these statements. The 2013 primary source was checked at its weak-Carmichael criterion, support construction, primitive definition, and two-prime proposition. A 2026 Meštrović preprint on weak Carmichael numbers was also checked; searches within its accessible full text did not locate `lattice`, `primitive weak`, `zeta`, or a fixed-support asymptotic. Current OEIS A225498 and A087442 were checked as well. The current SCOPE archive showed no semantic overlap. Accordingly, originality is claimed only **to the best of our knowledge**.

The most relevant source not fully inspected is E. Wong's 1997 Simon Fraser University MSc thesis *Computations on Normal Families of Primes*. Meštrović attributes the general support construction to its §2.5.3, so it is the clearest residual prior-art risk for an exponent-structure observation. An archived thesis link is recorded by OEIS A050474, but the thesis text was not inspected here. The published Borwein--Wong survey and the later Meštrović papers substantially reduce, but do not eliminate, the possibility of an older equivalent formulation. No evidence of the \(1/\zeta(s)\) primitive-density theorem was found.

## Limitations

The asymptotic is for a **fixed admissible prime support** while the exponents vary. It does not count weak Carmichael numbers when the prime support itself varies, and it does not address Meštrović's global conjectures on weak Carmichael counts. The constants implicit in the error terms depend on the fixed support. The lattice-point argument is classical and elementary; the claimed novelty is its application and synthesis in this weak-Carmichael setting.

## References

1. J. M. Borwein, E. W. M. Wong, *A survey of results relating to Giuga's conjecture on primality*, CRM Proceedings & Lecture Notes 11 (1997), 13--27. DOI: 10.1090/crmp/011/02.
2. R. Meštrović, *Generalizations of Carmichael numbers I*, arXiv:1305.1867 [math.NT], 2013.
3. R. Meštrović, *Weak Carmichael Numbers*, preprint, April 2026.
4. OEIS A225498, *Weak Carmichael numbers*.
5. OEIS A087442, *Non-prime-power weak Carmichael numbers*.
6. E. Wong, *Computations on Normal Families of Primes*, MSc thesis, Simon Fraser University, 1997. The thesis was not fully inspected; it is listed here because Meštrović attributes a directly relevant support construction to it.

## Reproducibility

Run
```text
python artifacts/verify.py
```
from the record directory. The expected deterministic output is stored in `artifacts/verification.txt`.
