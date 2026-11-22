# Exact joint mod-five image and sharp conditional mixing for two level-14 Apéry-like sequences

## Finding

Let \(P_n=T_{14B}(n)=T_9(n)\) and \(Q_n=T_{14A}(n)=T_5(n)\) denote the integral level-14 Apéry-like sequences with the normalization and recurrence below. Write
\[
N_L(a,b)=\#\{n:0\le n<5^L,\ P_n\equiv a,\ Q_n\equiv b\pmod5\}\qquad (L\ge0).
\]
All joint residues lie in the eleven-element set
\[
\mathcal S=G\cup\{(0,0),(0,1),(0,4)\},\qquad
G=\langle u=(3,4),v=(4,4)\rangle\le (\mathbb F_5^\times)^2\cong C_4\times C_2.
\]
In particular, \(G=\{(1,1),(3,4),(4,1),(2,4),(4,4),(2,1),(1,4),(3,1)\}\), and no pair outside \(\mathcal S\) ever occurs. The complete frequencies are
\[
N_L(0,0)=5^L-4^L;
\]
for every \(L\ge1\),
\[
N_L(0,1)=\frac{4^L-3^L+(-1)^{L+1}}2,\quad
N_L(0,4)=\frac{4^L-3^L-(-1)^{L+1}}2;
\]
and, for \(0\le j<4\), \(0\le h<2\),
\[
N_L(u^jv^h)=\sum_{\substack{r,s\ge0,\ r+s\le L\\ r\equiv j\ (\mathrm{mod}\ 4),\ s\equiv h\ (\mathrm{mod}\ 2)}}\frac{L!}{r!s!(L-r-s)!}.
\]
The same eight counts are the coefficients of \((1+X+Y)^L\) in the quotient ring \(\mathbb Z[X,Y]/(X^4-1,Y^2-1)\), mapping \(X\) to \(u\) and \(Y\) to \(v\). Every member of \(\mathcal S\) is represented for each \(L\ge4\), and each appears infinitely often as \(n\) varies.

There is also the exact quantitative identity
\[
\boxed{\sum_{g\in G}\left(N_L(g)-\frac{3^L}{8}\right)^2=\frac{2\cdot5^L+5}{8}}\qquad (L\ge0).
\]
Thus, conditionally on both entries being nonzero among the \(3^L\) admissible digit strings, the maximum absolute discrepancy from the uniform probability \(1/8\) is \(\Theta((\sqrt5/3)^L)\). This exponent is sharp for the maximum over the eight cells; no assertion is made that every individual cell has this exponent.

## Assumptions and scope

Let \(\eta(\tau)=q^{1/24}\prod_{m\ge1}(1-q^m)\), with \(q=e^{2\pi i\tau}\), and set
\[
W(q)=\left(\frac{\eta(\tau)\eta(14\tau)}{\eta(2\tau)\eta(7\tau)}\right)^4,
\quad t_+(q)=\frac{W(q)}{(1+W(q))^2},\quad t_-(q)=\frac{W(q)}{(1-W(q))^2}.
\]
The coefficients are specified by formal power-series identities
\[
\sum_{n\ge0}P_nt_+(q)^n=\frac{\eta(\tau)\eta(2\tau)\eta(7\tau)\eta(14\tau)}{t_+(q)},\quad
\sum_{n\ge0}Q_nt_-(q)^n=\frac{\eta(\tau)\eta(2\tau)\eta(7\tau)\eta(14\tau)}{t_-(q)}.
\]
The right sides have constant coefficient one, and each \(t_\pm=q+O(q^2)\), so these uniquely define integral series. Cooper's 2023 paper denotes the sequences by \(T_{14B}\) and \(T_{14A}\), respectively, and gives the independent integer-coefficient recurrence check below. The proven all-prime Lucas property of both sequences is invoked only at the prime five (Beukers--Tsai--Ye, Theorem 1.2). No unproved Lucas conjecture is used.

Equivalently, for either \(\epsilon\in\{9,5\}\), define \(T_\epsilon(0)=1\), \(T_\epsilon(-1)=T_\epsilon(-2)=0\) and, for every integer \(n\ge0\),
\[
\begin{aligned}
(n+1)^3T_\epsilon(n+1)={}&(2n+1)\big((2\epsilon-7)(n^2+n)+\epsilon-4\big)T_\epsilon(n)\\
&-n\big((6\epsilon^2-42\epsilon+13)n^2+\epsilon^2-8\epsilon+11\big)T_\epsilon(n-1)\\
&+n(2n-1)(n-1)(2\epsilon^3-21\epsilon^2+13\epsilon+224)T_\epsilon(n-2).
\end{aligned}
\]
The domain is the complete intervals \(0\le n<5^L\), not arbitrary cutoffs, and residue pairs are ordered as \((P_n,Q_n)\).

## Proof

**Digit reduction.** Cooper's recurrence or formal eta-product expansion yields
\[
(P_d,Q_d)\bmod5=(1,1),(0,1),(3,4),(4,4),(0,0)\quad\text{for }d=0,1,2,3,4.
\]
The full Lucas congruences for each integral level-14 sequence, proved by Beukers, Tsai and Ye, imply that for every \(n=\sum_{i\ge0}d_i5^i\),
\[
(P_n,Q_n)\equiv\prod_i(P_{d_i},Q_{d_i})\pmod5,
\]
with coordinatewise multiplication. Exactly \(L\) base-five digits, including leading zeros, enumerate the desired range without changing this product.

**Zero-coordinate strata.** A digit \(4\) forces \((0,0)\); there are \(5^L-4^L\) strings containing this digit. Among strings from \(\{0,1,2,3\}\) without digit \(4\), those with a digit \(1\) force the first component to zero while the second stays in \(\{1,4\}\). Their total count is \(4^L-3^L\). The difference of the two second-coordinate counts is the signed sum of \((-1)^{\#\{i:d_i=2\text{ or }3\}}\) over words containing a digit one. For \(L\ge1\) that signed sum equals \((2-2)^L-(1-2)^L=(-1)^{L+1}\). Solving for the two counts proves both zero-first-coordinate formulas. The formulas for \(L=0\) are separately \(N_0(1,1)=1\) and all other counts zero.

**The eight nonzero pairs.** The only digit choices that preserve both nonzero coordinates are \(0,2,3\), of multipliers \(1,u,v\). Directly, \(u\) has exact order four, \(v\) has exact order two, and \(u^jv^h=1\) for the ranges \(0\le j<4\), \(0\le h<2\) only at \((j,h)=(0,0)\). Hence \(G\cong C_4\times C_2\). An \(L\)-digit word containing \(r\) digits \(2\), \(s\) digits \(3\) and \(L-r-s\) digits \(0\) produces \(u^rv^s\), with multinomial multiplicity. Grouping exponents modulo four and two proves all eight formulas. These and the zero strata are disjoint and exhaustive, accounting for \(5^L\) total words.

**Attainability and infinitely many indices.** For every \(g=u^jv^h\in G\), at most \(j+h\le4\) nontrivial digits suffice; this realizes all eight members for \(L\ge4\). The two pairs \((0,1)\) and \((0,4)\) are respectively obtained from digit words \(1\) and \(12\) (digit order arbitrary), and \((0,0)\) from digit \(4\). To obtain infinitely many distinct indices for a fixed \(g\in G\), insert four copies of digit \(2\) in arbitrarily high, initially vacant base-five positions: their product is \(u^4=1\). For \((0,1)\) or \((0,4)\), insert a single digit \(1\) in arbitrarily high positions; for \((0,0)\), insert a high digit \(4\). None of these insertions changes its indicated output pair.

**Sharp mixing.** The character group of \(G\cong C_4\times C_2\) has eight characters \(\chi_{a,b}\), with \(\chi_{a,b}(u)=i^a\) and \(\chi_{a,b}(v)=(-1)^b\) for \(0\le a<4\), \(0\le b<2\). The Fourier transform of the coefficient vector of \((1+u+v)^L\) at this character is \((1+i^a+(-1)^b)^L\). The trivial character gives \(3^L\). For the seven nontrivial characters, the squared moduli of the one-step eigenvalues are \(5,5,1,1,1,1,1\). Finite-group Fourier orthogonality (Parseval), subtracting the trivial Fourier component, gives
\[
\sum_{g\in G}(N_L(g)-3^L/8)^2=\frac18\big(2\cdot5^L+5\big).
\]
The maximum cell deviation lies between \(1/\sqrt8\) and \(1\) times the Euclidean norm of the eight deviations. Dividing by the number \(3^L\) of admissible nonzero-pair words therefore yields the claimed sharp \(\Theta((\sqrt5/3)^L)\) maximum conditional discrepancy. This completes all quantifiers and boundary cases.

## Verification

The accompanying standalone `verify.py` (Python standard library) reconstructs both sequence definitions two ways, using Cooper's recurrence and exact integer eta-product series reversion. It matches the first thirteen coefficients of each series and Cooper's first eleven published terms, checks 400 recurrence coefficients of each, checks the digit rule at 400 indices, and compares the exact frequency formulas against every integer in the blocks of sizes \(5^L\) for \(0\le L\le7\). It checks the full sharp Parseval identity at 24 distinct values of \(L\). These are finite cross-checks; the infinite theorem rests on the cited Lucas theorem and the displayed combinatorial/Fourier proof.

For \(L=4\), the counts are \(N_4(0,0)=369\), \(N_4(0,1)=87\), \(N_4(0,4)=88\), and the eight nonzero-pair counts, ordered by \((a,b)\), are
\[
\begin{array}{c|rrrrrrrr}
(a,b)&(1,1)&(1,4)&(2,1)&(2,4)&(3,1)&(3,4)&(4,1)&(4,4)\\
N_4(a,b)&9&12&16&4&4&16&12&8
\end{array}.
\]
Their sum with the three zero-first-coordinate counts is \(625\), as required.

## Relationship to prior work

Cooper and Ye (2016) established the relevant level-14 modular constructions, differential equations and identities; these are not claimed here. Cooper (arXiv:2302.00757, first public 1 February 2023), Section 7, derived the explicit integral coefficients and four-term recurrences and conjectured their Lucas congruences. Beukers, Tsai and Ye (arXiv:2408.16616, first public 29 August 2024), Theorem 1.2, proved those congruences; this is the indispensable input to the present result. Neither of the inspected level-14 statements supplies the evaluated simultaneous five-adic digit-product histogram or its exact spectral discrepancy. The present contribution is that joint classification, not the known Lucas theorem or the standard character-orthogonality technique.

Related complete residue results for other Apéry-type or binomial sequences do not imply this particular ordered-pair distribution because their base-five digit multipliers and the resulting finite semigroups are different. The algebra \(C_4\times C_2\) and all its evaluated frequencies are specific to this natural pair.

## Limitations

The theorem is confined to the two integral level-14 sequences at the prime five. The analogous irrational level-14 sequences have different Lucas-prime conditions and are not covered. The exact frequencies concern powers-of-five index cutoffs, although every attainable pair is represented infinitely many times. The conditional mixing is only over the eight nonzero-coordinate cells; unconditioned frequencies concentrate at \((0,0)\). Standard Lucas machinery, finite multinomial counting, and finite-group Fourier analysis all predate this calculation. Unlocated earlier evaluations or implicit equivalents remain a possible priority issue, and no independent expert audit has been conducted.

## References

1. S. Cooper and D. Ye, *Level 14 and 15 analogues of Ramanujan's elliptic functions to alternative bases*, Transactions of the AMS 368 (2016), 7883–7910, DOI: 10.1090/tran6658. Author-supplied full text: https://www.researchgate.net/publication/276369530_Level_14_and_15_analogues_of_Ramanujan%27s_elliptic_functions_to_alternative_bases.
2. S. Cooper, *Apéry-like sequences defined by four-term recurrence relations*, arXiv:2302.00757v1 (1 February 2023), especially Section 7, Equation (7.9), Table 5, and Conjecture 7.3. https://arxiv.org/abs/2302.00757.
3. F. Beukers, W.-L. Tsai, D. Ye, *Lucas congruences using modular forms*, arXiv:2408.16616v1 (29 August 2024), especially Conjecture 1.1(2), Theorem 1.2, and its proof. https://arxiv.org/abs/2408.16616.
