# Infinitely many prime-index sharp ternary valuations for tagged odd-part partitions

## Finding

Write \(T(n)=\mathrm{PDO}_{\mathrm t}(n)\) for the total number of designated (tagged) parts in partitions of \(n\) into odd parts with designated summands. For integers \(m\ge0\), let
\[
S_m=\{n\ge1:\nu_3(T(8\cdot3^m n))=m+2\}.
\]
There is an infinite set of primes \(\mathcal P\), each \(p\equiv1\pmod{54}\), such that
\[
T(8p)\equiv72\pmod{108},\qquad
\nu_3(T(8\cdot3^m p))=m+2\quad
\text{for all }m\ge0.
\]
In fact the sharpness sets themselves coincide:
\[
S_0=S_1=S_2=\cdots.
\]
An explicit description of their common support is
\[
S_0=\{n\ge1:[q^n]H(q)\not\equiv0\pmod{3}\},\quad
H(z)=\frac{\eta(2z)^8\eta(3z)^7}{\eta(z)^{13}}.
\]
The conclusion is an existence theorem for infinitely many primes, not a statement that every prime in the specified residue class works.

## Assumptions and scope

All variables \(n,m\) are nonnegative integers unless explicitly positive; \(p\) denotes a rational prime; \(q=e^{2\pi i z}\) for \(z\) in the upper half-plane; \(\eta\) is the Dedekind eta function and \(E_4(z)=1+240\sum_{n\ge1}\sigma_3(n)q^n\). As usual, \(\nu_3(0)=+\infty\). The finite congruences are ordinary integer congruences. This theorem concerns the multiples-of-eight branch of the tagged-part function, not the separate multiples-of-twelve branch. The motivating paper was publicly posted on 2026-11-11.

## Proof

**Step 1: the normalized initial series.** The exact identity quoted by Li and Tang from Lin is
\[
\sum_{n\ge0}T(8n)q^n=36H(q),\qquad
H(q)=q\frac{E(q^2)^8E(q^3)^7}{E(q)^{13}},
\]
where \(E(q)=\prod_{j\ge1}(1-q^j)\). Hence \(T(8n)/36=[q^n]H\in\mathbb Z\) and
\[
\nu_3(T(8n))=2\quad\Longleftrightarrow\quad[q^n]H\not\equiv0\pmod{3}.
\]

**Step 2: a holomorphic modular lift with nonzero first coefficient.** Set
\[
A(z)=E_4(z)-81E_4(3z),\qquad F(z)=H(z)A(z).
\]
Since \(A(z)\equiv1\pmod{3}\) coefficientwise, \(F\equiv H\pmod{3}\). The eta exponents of \(H\) at divisors \(1,2,3\) are \((-13,8,7)\); their sum is \(2\), their exponent-weighted sum is \(24\), and at level \(18\) the second modularity sum is \(-120\). Thus the eta transformation criterion makes \(H\) a meromorphic modular form of weight \(1\) on \(\Gamma_0(18)\) with quadratic character \(\chi_{-3}\).

For cusp denominator \(d=1,2,3,6,9,18\), Ligozat's formula yields the exact order sequence
\[
\operatorname{ord}_d(H)=(-5,2,1,1,1,1).
\]
Now \(A\) is holomorphic modular of weight \(4\) at level \(3\), and the weight-four Fricke transform is
\[
(A|_4W_3)(z)=9(E_4(3z)-E_4(z))=-2160q+O(q^2).
\]
Consequently \(A\) has a simple zero at the level-three cusp \(0\). Under passage to level \(18\), the cusp widths above \(0\) give vanishing orders \(6\) and \(3\) for denominators \(1\) and \(2\), respectively; at denominators divisible by \(3\), \(A\) is holomorphic with nonzero leading term. Hence
\[
\operatorname{ord}_d(F)=(1,5,1,1,1,1).
\]
All cusp orders are positive and the functions have no upper-half-plane poles. Therefore
\[
F\in S_5(\Gamma_0(18),\chi_{-3})\subseteq M_5(\Gamma_1(18)),
\]
with integral Fourier coefficients. Since \(H=q+O(q^2)\) and \(A=-80+O(q)\), one has \([q]F=-80\equiv1\pmod{3}\).

**Step 3: infinitely many sharp prime indices.** Apply the Deligne--Serre prime-Hecke congruence theorem (as reproduced in the referenced 2020 paper) for the odd prime modulus \(3\), modular weight \(5\), and level \(18\). It supplies infinitely many primes \(p\equiv1\pmod{3\cdot18}\) for which, for the above \(F\),
\[
[q^p]F\equiv2[q]F\equiv2\pmod{3}.
\]
Because \(F\equiv H\pmod{3}\), these primes satisfy \([q^p]H\equiv2\pmod{3}\). Step 1 then gives
\[
T(8p)=36[q^p]H\equiv72\pmod{108}
\]
and \(\nu_3(T(8p))=2\).

**Step 4: sharpness persists at every level.** Li and Tang's Theorem 1.2(i) asserts that, for every \(m\ge1\), there is an integer \(\lambda_m\) coprime to \(3\) with
\[
T(8\cdot3^{m+1}n)\equiv3\lambda_mT(8\cdot3^m n)\pmod{3^{4m+3}}.
\]
Together with their \(3^{m+2}\)-divisibility theorem, division by \(3^{m+3}\) yields
\[
\frac{T(8\cdot3^{m+1}n)}{3^{m+3}}
\equiv\lambda_m\frac{T(8\cdot3^m n)}{3^{m+2}}\pmod{3}.
\]
Thus \(S_m=S_{m+1}\) for each \(m\ge1\). To connect \(m=0\) and \(m=1\), their explicit initial coefficient vector in Theorem 3.1 gives
\[
\sum_{n\ge0}\frac{T(24n)}{27}q^n\equiv2\rho(q)\xi(q)\pmod{3},
\]
where \(\rho=E(q^2)^{10}E(q^3)^9/(E(q)^{11}E(q^6)^6)\) and
\(\xi=qE(q^2)E(q^6)^5/(E(q)^5E(q^3))\). The identity
\[
\frac{\rho\xi}{H}=
\frac{E(q^2)^3E(q^3)}{E(q)^3E(q^6)}\equiv1\pmod{3}
\]
follows from \(E(q)^3\equiv E(q^3)\) and \(E(q^2)^3\equiv E(q^6)\). As \(T(8n)/9=4[q^n]H\), we obtain
\[
\frac{T(24n)}{27}\equiv
-\frac{T(8n)}9\pmod{3}.
\]
Hence \(S_0=S_1\), completing the uniform sharpness and common-support claims.

## Verification

The accompanying standalone Python checker reconstructs the two infinite-product series using the exact logarithmic-derivative recurrence (only a finite number of coefficients are tested), verifies the \(8n\) dissection and the first normalized \(24n\) comparison, checks the eta cusp-order arithmetic with rational numbers, and tests sample primes in \(1\pmod{54}\). Its test results are supporting diagnostics, not a proof that infinitely many primes work; that part invokes the precise Deligne--Serre theorem and modular-lift argument above.

## Relationship to prior work

Li--Tang, arXiv:2611.15164v1, establishes the lower valuations, the base dissection and the internal congruences used here. Its statements do not prove the existence of infinitely many *prime-index* sharpness witnesses. Barman--Singh--Singh (2024), Theorem 1.3, proves that \(T(n)\) is lacunary modulo every power of \(3\). Therefore any zero-natural-density assertion for \(S_m\) is ALREADY IMPLIED by their theorem and is not asserted as a new contribution. Their results do not imply any prime-index nondivisibility. The finding supplies the separate prime-witness result by an explicit holomorphic weight-five lift and a prime-Hecke theorem. Existing generic modular-form Hecke theorems are used as mathematical inputs, not claimed as original.

## Limitations

The infinite prime set is not explicitly listed or proved to contain *every* prime in \(1\pmod{54}\); a density among primes is not established here. The theorem does not classify all nonprime sharpness indices or higher residual digits at each scaling level. Modular Hecke and eta-quotient transformation theorems are cited as established external inputs; finite coefficient tests alone cannot establish these infinite facts. General lacunarity of \(T\) was known independently of this result. An unindexed specialized prime-sharpness theorem could constitute prior coverage.

## References

1. X. Li and D. Tang, *Congruence properties modulo powers of 3 for designated summands in partitions into odd parts*, arXiv:2611.15164v1 (publicly posted 2026-11-11), https://arxiv.org/pdf/2611.15164.
2. R. Barman, G. Singh and A. Singh, *Divisibility of the partition function PDOt(n) by powers of 2 and 3*, Bull. Aust. Math. Soc. 109 (2024), 14--25, https://doi.org/10.1017/S0004972723000199.
3. *Nonholomorphic Ramanujan-type congruences for Hurwitz class numbers*, Proc. Natl. Acad. Sci. USA (2020), Section C, Theorem 1.1 (Deligne--Serre/Serre prime-Hecke theorem), https://doi.org/10.1073/pnas.2005984117.
4. Standard eta-quotient transformation and Ligozat cusp-order criteria, as reproduced in the modular-form preliminaries of Reference 2; see also https://doi.org/10.1007/s00209-024-03672-9.
