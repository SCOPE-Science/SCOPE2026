# A universal gcd-divisibility law for Euler characteristics of Hilbert schemes of points
## Finding
Let \(S\) be a smooth complex algebraic surface whose compactly supported Betti numbers are finite. Write \(e=\chi_c(S)\) and \(a_n=\chi_c(S^{[n]})\), where \(S^{[n]}\) is the Hilbert scheme of length-\(n\) zero-dimensional subschemes.

If \(e=0\), then \(a_n=0\) for every \(n\ge 1\). If \(e\neq0\), then for every \(n\ge1\),
\[
\frac{|e|}{\gcd(|e|,n)}\mid a_n.
\]
Equivalently, with \(\nu_p(0)=+\infty\), every prime \(p\) satisfies
\[
\nu_p(a_n)\ge \max\{0,\nu_p(e)-\nu_p(n)\}.
\]
The divisor is uniformly sharp as a theorem depending only on \(e\) and \(n\), since \(a_1=e\).

For a K3 surface, where \(e=24\), this gives
\[
\frac{24}{\gcd(24,n)}\mid \chi(S^{[n]}).
\]
Equivalently, \(\nu_2(\chi(S^{[n]}))\ge\max\{0,3-\nu_2(n)\}\), and if \(3\nmid n\) then \(3\mid\chi(S^{[n]})\). For example, odd \(n\) not divisible by \(3\) force divisibility by \(24\), while odd multiples of \(3\) force divisibility by at least \(8\).

## Assumptions and scope
The Euler characteristic is the compactly supported topological Euler characteristic. The argument applies to every smooth complex algebraic surface covered by the Göttsche--de Cataldo generating function, including smooth projective surfaces. It concerns only total Euler characteristics of Hilbert schemes of points; it does not assert divisibility of individual Betti or Hodge numbers.

## Proof
De Cataldo's Theorem 2.1 gives
\[
F(q):=\sum_{n\ge0}a_n q^n=\prod_{m\ge1}(1-q^m)^{-e}.
\]
If \(e=0\), then \(F(q)=1\), proving \(a_n=0\) for \(n\ge1\).

Assume \(e\neq0\). Logarithmic differentiation in the formal power-series ring gives
\[
\frac{qF'(q)}{F(q)}
=e\sum_{m\ge1}\frac{m q^m}{1-q^m}
=e\sum_{j\ge1}\sigma_1(j)q^j,
\]
where \(\sigma_1(j)\) is the sum of the positive divisors of \(j\). Multiplying by \(F(q)\) and comparing the coefficient of \(q^n\) yields
\[
n a_n=e\sum_{j=1}^n\sigma_1(j)a_{n-j}.
\]
The right-hand side is divisible by \(e\), hence \(e\mid n a_n\). Put \(g=\gcd(|e|,n)\), \(|e|=g e'\), and \(n=g n'\), so \(\gcd(e',n')=1\). From \(g e'\mid g n' a_n\) we obtain \(e'\mid n'a_n\), and Euclid's lemma gives \(e'\mid a_n\). Therefore \(|e|/\gcd(|e|,n)\mid a_n\).

Taking \(p\)-adic valuations gives the equivalent lower bound. At \(n=1\), the generating function has coefficient \(a_1=e\), so the universal divisor cannot be strengthened uniformly.

## Verification
The standalone script `verify_hilbert_divisibility.py` independently constructs truncated coefficients of \(\prod_{m\ge1}(1-q^m)^{-e}\) by multiplying the individual Euler factors, rather than using the logarithmic-derivative recurrence to generate them. It then verifies both the recurrence and the gcd-divisibility for \(e\in\{-12,-6,-4,3,4,6,8,9,12,18,24,30\}\) through \(n=120\), for 2,880 exact integer checks. It separately checks the K3 case \(e=24\) and the projective-plane case \(e=3\) through \(n=80\).

## Relationship to prior work
De Cataldo proves the generating function for \(\chi_c(S^{[n]})\) and notes that the projective case was first proved by Göttsche. A recent paper on strict log-concavity of \(k\)-coloured partitions explicitly identifies \(\chi(S^{[n]})\) with the \(\chi(S)\)-coloured partition number and studies inequalities and log-concavity, not this gcd-divisibility law. Chern--Fu--Tang likewise study multiplicative inequalities for coloured partition functions. Targeted statement-level searches did not locate the divisor \(|e|/\gcd(|e|,n)\) in the checked literature.

## Limitations
The theorem is a divisibility constraint on Euler characteristics, not a determination of their exact valuations. Extra divisibility can and does occur. No claim is made about singular surfaces, Hilbert schemes in dimensions other than two, individual cohomology groups, or refined genera. Although targeted searches did not find an equivalent statement, an equivalent arithmetic lemma may exist in partition-congruence literature under different notation.

## References
1. M. A. A. de Cataldo, *Hilbert schemes of a surface and Euler characteristics*, arXiv:math/9811150; Archiv der Mathematik 75 (2000), 59--64. Theorem 2.1 gives the Euler-characteristic product.
2. L. Göttsche, *The Betti numbers of the Hilbert scheme of points on a smooth projective surface*, Math. Ann. 286 (1990), 193--207.
3. K. Bringmann, B. Kane, A. Pahari, and L. Rolen, *Strict log-concavity of k-coloured partitions*, Proc. Roy. Soc. Edinburgh Sect. A (2026), DOI 10.1017/prm.2026.10154.
4. S. Chern, S. Fu, and D. Tang, *Some inequalities for k-colored partition functions*, arXiv:1709.06735; Ramanujan J. 46 (2018), 713--725.
