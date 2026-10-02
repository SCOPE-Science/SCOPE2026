# Prime-power witness densities in Fibonacci-totient residue classes

## Statement

Let \(F_n\) be the Fibonacci sequence, let \(z(N)\) denote the rank of apparition of \(N\), and let \(\pi(q)\) denote the Pisano period modulo a prime \(q\). For an odd prime \(q\), write
\[
S(q)=\{r\bmod \pi(q): q\mid \varphi(F_m)\text{ for every positive }m\equiv r\pmod{\pi(q)}\}.
\]
For an odd prime \(q\neq 5\), set
\[
P=\pi(q),\qquad z=z(q),\qquad e_q=v_q(F_z).
\]
Thus \(e_q\ge 2\) exactly when \(q\) is a Wall--Sun--Sun (Fibonacci--Wieferich) prime.

Fix a residue class \(r\bmod P\), choose \(0\le r_0<P\), and put \(m_t=r_0+tP\), omitting the single nonpositive term if \(r_0=0\). For \(a\ge1\), define
\[
\delta_{q,a}(r)
=
\lim_{T\to\infty}
\frac1T
\#\{0\le t<T:q^a\mid F_{m_t}\}.
\]

**Theorem.** The limit exists and
\[
\boxed{
\delta_{q,a}(r)=
\begin{cases}
0,&z(q)\nmid r,\\[2mm]
q^{-\max(a-e_q,0)},&z(q)\mid r.
\end{cases}}
\]

In particular, for square divisibility,
\[
\boxed{
\delta_{q,2}(r)=
\begin{cases}
0,&z(q)\nmid r,\\
1/q,&z(q)\mid r\text{ and }q\text{ is not Wall--Sun--Sun},\\
1,&z(q)\mid r\text{ and }q\text{ is Wall--Sun--Sun}.
\end{cases}}
\]

Consequently, if
\[
Q(q)=\{r\bmod P:q^2\mid F_m\text{ for every positive }m\equiv r\pmod P\},
\]
then
\[
\boxed{
Q(q)=
\begin{cases}
\varnothing,&q\text{ is not Wall--Sun--Sun},\\
\{r\bmod P:z(q)\mid r\},&q\text{ is Wall--Sun--Sun}.
\end{cases}}
\]

## Proof

The Fibonacci sequence is a divisibility sequence:
\[
N\mid F_m \quad\Longleftrightarrow\quad z(N)\mid m.
\]
For odd \(q\neq5\), \(z(q)\mid P\) and \(P\mid q^2-1\), hence \(q\nmid P\), and therefore also \(q\nmid z(q)\).

The standard lifting formula for Fibonacci numbers gives, whenever \(z=z(q)\mid n\),
\[
v_q(F_n)=v_q(F_z)+v_q(n/z)=e_q+v_q(n/z),
\]
while \(v_q(F_n)=0\) when \(z\nmid n\).

Because \(z\mid P\), the congruence class \(m_t=r_0+tP\) is either always divisible by \(z\) or never divisible by \(z\). If \(z\nmid r\), then \(q\nmid F_{m_t}\) for every \(t\), proving the first case.

Suppose \(z\mid r\). Write
\[
u=r_0/z,\qquad A=P/z.
\]
Then \(q\nmid A\), and
\[
v_q(F_{m_t})=e_q+v_q(u+tA).
\]
For each integer \(s\ge0\), the condition \(q^s\mid u+tA\) selects exactly one residue class of \(t\bmod q^s\), since \(A\) is invertible modulo \(q^s\). It therefore has natural density \(q^{-s}\). Taking
\[
s=\max(a-e_q,0)
\]
gives the stated formula.

For \(a=2\), \(e_q=1\) is exactly the non-Wall--Sun--Sun case and \(e_q\ge2\) is exactly the Wall--Sun--Sun case, yielding the trichotomy.

## Consequences for totient witnesses

Factor
\[
F_m=\prod_{\ell}\ell^{\alpha_\ell}.
\]
If \(q\mid\varphi(F_m)\), then either

1. \(q^2\mid F_m\), so the prime \(q\) itself supplies the factor \(q\) in \(\varphi(F_m)\); or
2. some prime divisor \(p\neq q\) of \(F_m\) satisfies \(p\equiv1\pmod q\).

Indeed,
\[
\varphi(F_m)=\prod_{\ell}\ell^{\alpha_\ell-1}(\ell-1),
\]
and if \(q^2\nmid F_m\), the \(\ell=q\) factor cannot supply a factor \(q\).

Hence, for a non-Wall--Sun--Sun prime \(q\neq5\) and \(r\in S(q)\), an external prime
\[
p\mid F_m,\qquad p\neq q,\qquad p\equiv1\pmod q
\]
is necessary on a set of terms \(m\equiv r\pmod P\) of density at least
\[
\boxed{
\begin{cases}
1,&z(q)\nmid r,\\
1-1/q,&z(q)\mid r.
\end{cases}}
\]
This strengthens an infinitude conclusion to an explicit positive-density conclusion under the correct non-Wall--Sun--Sun hypothesis.

Conversely, if \(q\) is Wall--Sun--Sun, then for every class \(r\) divisible by \(z(q)\),
\[
q^2\mid F_m\qquad\text{for every }m\equiv r\pmod P,
\]
so
\[
\boxed{\{r\bmod P:z(q)\mid r\}\subseteq S(q)}
\]
and in particular
\[
|S(q)|\ge P/z(q),\qquad S(q)\neq\varnothing.
\]
Thus a hypothetical Wall--Sun--Sun prime supplies a second, purely prime-power mechanism for nonemptiness of \(S(q)\), separate from the fixed-prime mechanism \(p\equiv1\pmod q\).

## Relation to the 2026 Sophie-Germain/totient paper

Goel's arXiv:2604.17847v3 defines \(S(q)\) and, in Lemma 4.3, attempts to rule out \(q^2\mid F_m\) as the sole witness on an entire residue class. The displayed proof states, for an arbitrary odd prime \(q\neq5\), that \(q\) is not a Wall--Sun--Sun prime because no such primes are known in a large computational range, and then uses
\[
z(q^2)=qz(q).
\]
Absence of known examples does not establish that an arbitrary prime is non-Wall--Sun--Sun.

The theorem above isolates the exact missing case:

- if \(q\) is non-Wall--Sun--Sun, the \(q^2\)-witness occurs with density \(0\) or \(1/q\), so Lemma 4.3's intended conclusion follows and is strengthened to the density bound above;
- if \(q\) is Wall--Sun--Sun and \(z(q)\mid r\), then \(q^2\mid F_m\) for every term of the class, so the proof strategy cannot rule out the prime-power witness.

This does **not** prove that the conclusion of Lemma 4.3 is false for a hypothetical Wall--Sun--Sun prime: external primes \(p\equiv1\pmod q\) may still occur. It shows that the published proof does not establish the unconditional statement and gives the exact prime-power behavior that a corrected argument must accommodate.

The same distinction matters for Conjecture 4.4 of that paper. If Conjecture 4.4 is true as stated, then every hypothetical Wall--Sun--Sun prime \(q\neq5\) must, despite already having the prime-power mechanism above, also admit a fixed prime \(p\equiv1\pmod q\) with \(z(p)\mid\pi(q)\).

## Originality and limitations

The prime-power lifting relation itself is classical. The contribution here is its application to the residue-class set \(S(q)\): the exact \(q^a\)-witness density formula, the Wall--Sun--Sun/non-Wall--Sun--Sun dichotomy for entire classes, and the resulting correction and positive-density strengthening of the recent Fibonacci-totient argument.

To the best of our knowledge, searches for equivalent formulations using "Wall--Sun--Sun", "Fibonacci--Wieferich", ranks of apparition, Fibonacci totients, \(S(q)\), and residue-class witnesses did not identify this density statement or this correction. Bragman--Rowland's work on limiting densities of residues attained by Fibonacci numbers modulo powers of a prime studies a different density problem (density in the residue image as the modulus power grows), not the density of indices inside a fixed Pisano-period class.

The principal residual originality risk is unindexed contemporaneous commentary or corrections to the very recent arXiv paper. No inaccessible paper was identified whose title or available description specifically suggests the same \(S(q)\) prime-power density theorem.

No existence of a Wall--Sun--Sun prime is asserted. No claim is made that Conjecture 4.4 is false, nor that external witnesses fail in the Wall--Sun--Sun case. The result concerns the exact frequency with which the prime \(q\) itself can witness \(q\mid\varphi(F_m)\) through \(q^2\mid F_m\).

## References

1. A. Goel, *Sophie Germain Primes and the Totient of Fibonacci Numbers*, arXiv:2604.17847v3 (2026). https://arxiv.org/abs/2604.17847
2. D. D. Wall, *Fibonacci Series Modulo m*, Amer. Math. Monthly 67 (1960), 525--532. https://doi.org/10.1080/00029890.1960.11989541
3. J. Vinson, *The Relation of the Period Modulo m to the Rank of Apparition of m in the Fibonacci Sequence*, Fibonacci Quarterly 1 (1963), 37--46. https://doi.org/10.1080/00150517.1963.12431578
4. C. Sanna, *The p-Adic Valuation of Lucas Sequences*, Fibonacci Quarterly 54 (2016), 118--124. https://doi.org/10.1080/00150517.2016.12427821
5. R. J. McIntosh and E. L. Roettger, *A search for Fibonacci-Wieferich and Wolstenholme primes*, Math. Comp. 76 (2007), 2087--2094. https://doi.org/10.1090/S0025-5718-07-01955-2
6. N. Bragman and E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, Research in Number Theory 11 (2025), 88. https://doi.org/10.1007/s40993-025-00667-1
