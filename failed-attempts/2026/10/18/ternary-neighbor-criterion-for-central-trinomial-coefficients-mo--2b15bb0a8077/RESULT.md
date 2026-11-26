# Ternary-neighbor criterion for central trinomial coefficients modulo nine

## Finding
Let \(T_n=[x^n](1+x+x^2)^n\) for each integer \(n\ge0\). Write the ternary expansion \(n=\sum_{i\ge0}d_i3^i\), where \(d_i\in\{0,1,2\}\) and all but finitely many digits vanish. For the ordinary \(3\)-adic valuation \(\nu_3\), the following is an exact classification:

\[
\nu_3(T_n)=0\quad\Longleftrightarrow\quad\text{no ternary digit equals }2.
\]

When a digit \(2\) occurs, \(\nu_3(T_n)=1\) **if and only if** there is exactly one such digit, at position \(j\), and either \(j=0\) or \(d_{j+1}=0\). In every remaining case, \(9\mid T_n\). More precisely, with a unique digit \(2\),

\[
T_n\equiv
\begin{cases}
3\pmod{9},&j=0,\ d_1=0,\\
6\pmod{9},&j=0,\ d_1=1,\\
6\pmod{9},&j\ge1,\ d_{j+1}=0,\\
0\pmod{9},&j\ge1,\ d_{j+1}=1.
\end{cases}
\]

For every integer \(L\ge2\), the complete finite census is

\[
\#\{0\le n<3^L:\nu_3(T_n)=1\}=(L+2)2^{L-2},\qquad
\#\{0\le n<3^L:9\nmid T_n\}=(L+6)2^{L-2}.
\]

At \(L=1\), the corresponding counts are \(1\) and \(3\); at \(L=0\), they are \(0\) and \(1\). In particular the set of indices with \(9\nmid T_n\) has natural density zero, but its count up to \(3^L\) has an additional factor proportional to \(L\) compared with the classical no-\(2\)-digit set.

## Assumptions and scope
All variables are ordinary nonnegative integers unless otherwise specified; \(\nu_3(m)\) is the largest nonnegative integer \(r\) such that \(3^r\mid m\) for \(m>0\). These central trinomial coefficients are positive. Digit indices increase from the least significant digit, and \(d_i=0\) for sufficiently large \(i\). No prime other than \(3\) or higher valuation layer is classified.

## Proof
Set \(f(x)=x^{-1}+1+x\) and \(h(x)=x^{-2}+2x^{-1}+2+2x+x^2\). The coefficient identity \(T_n=\operatorname{CT}(f(x)^n)\) follows by multiplying \((1+x+x^2)^n\) by \(x^{-n}\). Direct multiplication gives the exact Laurent-polynomial identity

\[
f(x)^3=f(x^3)+3h(x).
\]

Cubing a congruence modulo \(9\) eliminates every term involving a factor \(3h\), so induction gives, for each \(i\ge1\),

\[
f(x)^{3^i}\equiv f(x^{3^i})+3h(x^{3^{i-1}})\pmod{9}.
\]

Put \(f_i=f(x^{3^i})\) and \(h_i=h(x^{3^i})\). Multiplication of the digit powers, retaining all first-order corrections, now yields

\[
f(x)^n\equiv
\prod_{i\ge0}f_i^{d_i}
+3\sum_{i\ge1}d_i h_{i-1}f_i^{d_i-1}\prod_{k\ne i}f_k^{d_k}
\pmod{9}.
\tag{1}
\]

All products and sums in (1) are finite. To evaluate constant terms, note that a local factor \(f_i^{d_i}\) has exponents \(a_i3^i\) with \(-2\le a_i\le2\). In a zero-sum choice, reducing modulo \(3\) forces \(a_0=0\), then reducing after division by \(3\) forces \(a_1=0\), and so forth. Thus

\[
\operatorname{CT}\biggl(\prod_i f_i^{d_i}\biggr)
=\prod_i\operatorname{CT}(f_i^{d_i})=3^{s},
\]

where \(s=\#\{i:d_i=2\}\), since the three local constant terms are \(1,1,3\).

For a correction at index \(i\ge1\), the factors at indices below \(i-1\) must independently have zero exponent, by the same base-three reduction. The combined exponents from \(h_{i-1}f_{i-1}^{d_{i-1}}f_i^{d_i-1}\) have absolute value at most \(7\cdot3^{i-1}<3^{i+1}\), so their sum must be zero in order to balance the factors at indices above \(i\). The remaining higher-digit contributions also vanish independently, giving

\[
\operatorname{CT}\biggl(h_{i-1}f_i^{d_i-1}\prod_{k\ne i} f_k^{d_k}\biggr)
=J_{d_{i-1},d_i}\prod_{k\notin\{i-1,i\}}\operatorname{CT}(f_k^{d_k}),
\]

where \(J_{a,b}=\operatorname{CT}(f(x)^a h(x)f(x^3)^{b-1})\). The exact local table, for rows \(a=0,1,2\) and columns \(b=1,2\), is

\[
(J_{a,b})=\begin{pmatrix}2&2\\6&8\\16&24\end{pmatrix}.
\tag{2}
\]

If \(s=0\), equation (1) gives \(T_n\equiv1\pmod{3}\). If \(s\ge1\), it gives \(T_n\equiv0\pmod{3}\). This recovers the established digit criterion for divisibility by \(3\).

If \(s=1\) with its unique digit \(2\) at position \(j\), then modulo \(9\) all corrections vanish except possibly those at indices \(j\) and \(j+1\). When \(j\ge1\), the correction at \(j\) contributes \(3\cdot2 J_{d_{j-1},2}\equiv3\pmod{9}\), since \(d_{j-1}\) is \(0\) or \(1\) and \(J_{0,2}=2, J_{1,2}=8\). At index \(j+1\), a contribution is possible only if \(d_{j+1}=1\); it is \(3J_{2,1}\equiv3\pmod{9}\). The uncorrected term equals \(3\). For \(j=0\), the first correction is absent; the same possible \(j+1\) contribution remains. These cases yield exactly the displayed residues.

If \(s\ge2\), the uncorrected term is divisible by \(9\). In any correction, a digit \(2\) outside the two local positions makes the term divisible by \(9\). Otherwise, exactly two digits \(2\) must occur at adjacent local positions; then the factor \(J_{2,2}=24\) is divisible by \(3\), so that correction is again zero modulo \(9\). This establishes the full classification.

To count \(\nu_3(T_n)=1\) in a digit word of length \(L\ge2\), one digit \(2\) at the units position gives \(2^{L-1}\) choices; at the top position it gives another \(2^{L-1}\); at each of the \(L-2\) interior positions the next higher digit is forced to be \(0\), leaving \(2^{L-2}\) choices. The sum is \((L+2)2^{L-2}\). Exactly \(2^L\) words contain no digit \(2\); adding that count gives \((L+6)2^{L-2}\). Dividing these counts by \(3^L\) and squeezing intermediate cutoffs between adjacent powers of three proves the zero natural density.

## Verification
The standalone `verify.py` recomputes the Laurent-polynomial identity and all six entries in (2) over exact integers. It independently constructs all \(19{,}683\) central trinomial coefficients with indices \(0\le n<3^9\) from the integer recurrence

\[
nT_n=(2n-1)T_{n-1}+3(n-1)T_{n-2},\quad T_0=T_1=1,
\]

and compares every residue modulo \(9\) with the digit formula. It also checks the two exact counting identities at every ternary length through \(9\). All tests passed. These finite tests corroborate rather than replace the unlimited Laurent-polynomial proof.

Run: `python3 verify.py`.

## Relationship to prior work
Deutsch and Sagan established the modulo-\(3\) digit criterion, and Noe generalized related prime-divisibility statements to other central trinomial sequences; their identified statements do not give the modulo-\(9\) first-valuation layer or these finite censuses. Rowland and Zeilberger gave a general constant-term algorithm for prime-power congruence automata, which ensures such questions are algorithmically approachable; their inspected paper does not state this explicit neighbor condition or the closed counts. Rampersad and Shallit revisit the central trinomial sequence modulo \(3\) and modulo \(5\) without deriving the present modulo-\(9\) classification. Mikić's later valuation results concern other generalized parameters, the Delannoy numbers, and the Schröder numbers, not this ordinary sequence and first valuation layer. OEIS A002426 records the classical modulo-\(3\) criterion, but no equivalent first modulo-\(9\) census was identified in the inspected entry.

## Limitations
The theorem determines the first nonzero \(3\)-adic valuation layer, not the exact valuation for terms divisible by \(9\). The literature comparison cannot prove universal novelty: a stronger published automaton or an unstated specialization of general constant-term methods might imply the closed formulas. No independent mathematical audit has been performed.

## References
1. E. Deutsch and B. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326v1 (publicly posted 2004-07-19), Section 4, Theorem 4.7. https://arxiv.org/pdf/math/0407326
2. T. D. Noe, *On the Divisibility of Generalized Central Trinomial Coefficients*, Journal of Integer Sequences 9 (2006), Article 06.2.7, Theorem 8.5. https://cs.uwaterloo.ca/journals/JIS/VOL9/Noe/noe35.pdf
3. E. Rowland and D. Zeilberger, *A Case Study in Meta-AUTOMATION: Automatic Generation of Congruence Automata for Combinatorial Sequences*, arXiv:1311.4776v1 (2013). https://arxiv.org/pdf/1311.4776
4. N. Rampersad and J. Shallit, *Congruence Properties of Combinatorial Sequences via Walnut and the Rowland–Yassawi–Zeilberger Automaton*, arXiv:2110.06244, Section 3. https://arxiv.org/pdf/2110.06244
5. J. Mikić, *On New Divisibility Properties of Generalized Central Trinomial Coefficients and Legendre Polynomials*, arXiv:2311.14623, Theorems 5–8. https://arxiv.org/pdf/2311.14623
6. OEIS A002426, *Central trinomial coefficients*. https://oeis.org/A002426
