# Stabilized seven-adic zero counts and the valuation law for Padovan numbers

## Finding
Let \(P_0=P_1=P_2=1\) and \(P_{n+3}=P_{n+1}+P_n\) for every integer \(n\ge0\). For every integer \(k\ge1\), the least period of \((P_n\bmod 7^k)_{n\ge0}\) is
\[
L_k=48\cdot 7^{k-1}.
\]
The number of indices \(0\le n<L_k\) with \(P_n\equiv0\pmod{7^k}\) is exactly
\[
Z_k=\begin{cases}12,&k=1,\\30,&k=2,\\51,&k\ge3.\end{cases}
\]
Consequently the natural density \(d_k\) of indices for which \(7^k\mid P_n\) exists and is
\[
d_k=\begin{cases}\frac14,&k=1,\\\frac5{56},&k=2,\\\frac{17}{16\cdot7^{k-1}},&k\ge3.\end{cases}
\]
The complete limiting distribution of \(\nu_7(P_n)\) is
\[
\Pr(\nu_7(P_n)=j)=
\begin{cases}
\frac34,&j=0,\\
\frac9{56},&j=1,\\
\frac{53}{784},&j=2,\\
\frac{51}{8\cdot7^j},&j\ge3.
\end{cases}
\]
Here \(\Pr\) denotes the natural density of indices, not a random model. The stable count \(51\) comes from nine simple seven-adic zero branches and three singular branches that each split into two simple roots after division by \(49\).

## Assumptions and scope
The recurrence starts at index zero, with initial triple \((1,1,1)\); it is not the index convention \((1,0,0)\) used in some Padovan references. All congruences are over the ordinary integers. The result is for the fixed prime \(7\), every exponent \(k\ge1\), and the full least period, not a bounded collection of exponents. Because all \(P_n\) are positive, their seven-adic valuations are finite.

## Proof
Set
\[
T=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\qquad
v=(1,1,1)^{\mathsf T},\qquad K=T^{48},\qquad E=K-I.
\]
Then the first coordinate of \(T^n v\) is \(P_n\). Direct matrix multiplication gives \(T^{48}\equiv I\pmod7\), and the initial triple has least period \(48\) modulo \(7\): the triple does not return after either \(16\) or \(24\) steps, and every proper divisor of \(48\) divides one of these two integers. Also
\[
E/7\equiv
\begin{pmatrix}4&6&1\\1&5&6\\6&0&5\end{pmatrix}\pmod7,
\qquad Kv-v\equiv7(4,5,4)^{\mathsf T}\pmod{49}.
\]
The binomial expansion of \((I+E)^{7^a}\), using \(E\in7M_3(\mathbb Z)\), shows for every integer \(a\ge0\) that \((K^{7^a}-I)v\) has valuation exactly \(a+1\) in at least one coordinate, with leading vector \(7^{a+1}(4,5,4)^{\mathsf T}\) modulo \(7^{a+2}\). The same conclusion for \(K^{7^a u}-I\), where \(7\nmid u\), follows by expanding the \(u\)-th power. Therefore \(K^t v\equiv v\pmod{7^k}\) precisely when \(7^{k-1}\mid t\), and the least period is \(L_k\) as claimed.

For \(0\le i<48\), write
\[
F_i(t)=P_{i+48t}=\sum_{j\ge0}\binom tj c_{i,j},\quad
c_{i,j}=e_1^{\mathsf T}T^i E^jv,\qquad t\in\mathbb Z_{\ge0}.
\]
Every \(c_{i,j}\) is divisible by \(7^j\). As \(v_7(j!)\le(j-1)/6\), the same expression defines a convergent restricted seven-adic power series on \(\mathbb Z_7\); division by \(7\), or by \(49\) when all coefficients permit it, also gives restricted power series. Thus simple roots modulo \(7\) lift uniquely by Hensel's lemma.

The zero positions modulo \(7\), computed from the recurrence through index \(47\), are precisely
\[
\{8,12,13,15,24,28,29,31,40,44,45,47\}.
\]
Nine positions are *regular*. For these indices \(i\), put \(a_i=P_i/7\bmod7\) and \(b_i=(P_{i+48}-P_i)/7\bmod7\). The exact finite data are

| \(i\) | 8 | 12 | 13 | 24 | 28 | 29 | 40 | 44 | 45 |
|---|---|---|---|---|---|---|---|---|---|
| \(a_i\) | 1 | 3 | 4 | 4 | 5 | 2 | 5 | 1 | 6 |
| \(b_i\) | 3 | 2 | 5 | 6 | 4 | 3 | 5 | 1 | 6 |

For each of these nine positions, \(b_i\not\equiv0\pmod7\) and
\[
F_i(t)/7\equiv a_i+b_i t\pmod7.
\]
The higher binomial terms, after division by \(7\), have coefficients divisible by \(7\). Hensel's lemma therefore gives exactly one \(t\bmod 7^{k-1}\) satisfying \(7^k\mid F_i(t)\) for every \(k\ge2\). Each regular position contributes one index per period.

The remaining indices are \(i=15,31,47\). At each, both \(P_i\) and \(P_{i+48}-P_i\) are divisible by \(49\). Therefore \(F_i(t)/49\) is a restricted seven-adic power series. Let
\[
A_i=P_i/49,\quad B_i=(P_{i+48}-P_i)/49,\quad
C_i=(P_{i+96}-2P_{i+48}+P_i)/49.
\]
The coefficients of all remaining terms, after division by \(49\), are divisible by \(7\). Direct recurrence arithmetic gives the following complete finite table:

| \(i\) | \((A_i,B_i,C_i)\bmod7\) | \(F_i(t)/49\bmod7\) | roots \(t\bmod7\) |
|---|---|---|---|
| 15 | \((1,2,2)\) | \(t^2+t+1\) | \(2,4\) |
| 31 | \((6,3,4)\) | \(2t^2+t+6\) | \(4,6\) |
| 47 | \((3,4,1)\) | \(4t^2+3\) | \(1,6\) |

All six roots are simple: the respective polynomial derivatives are nonzero at the displayed roots modulo \(7\). Hence for every \(k\ge3\), exactly two residue classes \(t\bmod7^{k-2}\) solve \(F_i(t)/49\equiv0\pmod{7^{k-2}}\). Each has seven extensions \(t\bmod7^{k-1}\), so each exceptional index contributes \(14\) positions to \(Z_k\). For \(k=2\), all seven classes \(t\bmod7\) work in each exceptional branch. Thus
\[
Z_1=12,\qquad Z_2=9+3\cdot7=30,\qquad
Z_k=9+3\cdot14=51\quad(k\ge3).
\]
The density formula follows by dividing by the least period. The valuation masses are \(\Pr(\nu_7(P_n)=j)=d_j-d_{j+1}\) for \(j\ge1\), with \(d_0=1\), and the displayed formulas follow by subtraction. Since \(d_k\to0\), these masses sum to one.

## Verification
Run `python3 check.py` (standard-library Python only). The program recomputes all twelve zero classes modulo \(7\), the nine regular finite coefficients, the three singular quadratic polynomials and their simple roots, the matrix lift, and the least-period certificates. It separately enumerates whole periods modulo \(7^k\) for \(1\le k\le6\), obtaining \(12,30,51,51,51,51\), and cross-checks selected recurrence values by matrix exponentiation. These finite checks verify the numerical premises of the all-level argument; they are not a substitute for the Hensel and binomial proofs above.

## Relationship to prior work
Nacin's *Van der Laan Sequences and a Conjecture on Padovan Numbers* (first publicly verified December 30, 2022) studies structural recurrences and linear combinations, rather than prime-power zero frequencies; its Padovan indexing \((1,0,0)\) differs from the \((1,1,1)\) normalization used here by five places. Deveci and Karaduman analyze modular periods of related Padovan families, providing important period-lifting context but not these zero-incidence counts. Bravo and Irmak analyze shifted quantities at the prime two. Bravo's June 2026 study uses certain seven-adic congruences for \(P_m\pm1\) along a restricted progression and the known periods \(48\) and \(336\), but does not imply the complete unshifted seven-adic valuation distribution. Related modular zero-hit results at primes two and twenty-three or for averages over recurrence orbits likewise do not determine the fixed standard Padovan orbit at seven.

## Limitations
This theorem concerns only the prime \(7\) and the exact zero-value fibers, not a full residue-frequency table modulo \(7^k\). It supplies a self-review and finite replayable evidence, not independent certification. Bibliographic searches cannot exclude an uncatalogued equivalent theorem; material from some tangential earlier modular-period papers was available only through abstracts.

## References
- D. Nacin, *Van der Laan Sequences and a Conjecture on Padovan Numbers*, Journal of Integer Sequences 26, Article 23.1.2 (online December 30, 2022), https://cs.uwaterloo.ca/journals/JIS/VOL26/Nacin/nacin5.pdf.
- Ö. Deveci and E. Karaduman, *On the Padovan p-numbers*, Hacettepe Journal of Mathematics and Statistics 46 (2017), 579–592, https://doi.org/10.15672/HJMS.20174622760.
- E. Bravo and N. Irmak, *The 2-adic valuation of shifted Padovan and Perrin numbers and applications*, Turkish Journal of Mathematics 48 (2024), 1183–1196, https://doi.org/10.55730/1300-0098.3568.
- E. F. Bravo, *On Brocard's problem with Padovan and Perrin numbers*, arXiv:2606.28577 (June 26, 2026), https://arxiv.org/abs/2606.28577.
- E. F. Bravo, J. J. Bravo and F. Luca, *On the Multiplicities of Padovan-Type Sequences*, Bulletin of the Brazilian Mathematical Society 53 (2022), 1519–1549, https://doi.org/10.1007/s00574-022-00315-7.
