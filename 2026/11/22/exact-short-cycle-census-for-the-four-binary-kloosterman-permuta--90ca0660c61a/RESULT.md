# Exact short-cycle census for the four binary Kloosterman permutations

## Finding

For an integer \(n\geq1\), put \(E_n=\mathbb F_{2^n}\) and \(T_n=\{t\in E_n:\operatorname{Tr}_{E_n/\mathbb F_2}(t)=1\}\). For \(u\in\{0,3,6,10\}\) with \(0\leq u<2^n\), write its binary digits \(u=\sum_{i=0}^{n-1}u_i2^i\) and define the permutation

\[
F_u(t)=t+\sum_{i:u_i=1}t^{-2^i}\qquad(t\in T_n).
\]

Let \(N_1(n,u)\) denote its number of fixed points and \(N_2(n,u)\) its number of *unoriented*, primitive two-cycles. With \(\mathbf1[Q]\) denoting the indicator of condition \(Q\), their **complete** short-cycle census is

\[
\begin{array}{c|c|c}
u&N_1(n,u)&N_2(n,u)\\\hline
0&2^{n-1}&0\\
3&\mathbf1[n\text{ odd}]&\mathbf1[n\equiv2\pmod4]\\
6&\mathbf1[n\text{ odd}]&\mathbf1[n\equiv2\pmod4]+2\mathbf1[n\equiv4\pmod8]\\
10&\mathbf1[n\text{ odd}]+2\mathbf1[n\equiv2\pmod4]&5\mathbf1[n\equiv5\pmod{10}]+10\mathbf1[n\equiv10\pmod{20}]
\end{array}.
\]

In particular, there are at most ten primitive two-cycles, uniformly over every extension degree and every one of the four permutations; ten occur exactly for \(u=10\) and \(n\equiv10\pmod{20}\). The five- and ten-cycle-count resonances arise from the two irreducible factors of degree five and the two of degree ten in an exact second-iterate polynomial.

## Assumptions and scope

The permutation property for \(u=3,6,10\) follows from Hollmann–Xiang, Theorem 4.1, and \(u=0\) is the identity. The table applies only when the binary index is admissible: \(n\geq1\) for \(u=0\), \(n\geq2\) for \(u=3\), \(n\geq3\) for \(u=6\), and \(n\geq4\) for \(u=10\). It classifies only fixed points and primitive period-two orbits, not longer cycles or the entire functional graph. All traces here are absolute traces to \(\mathbb F_2\).

## Proof

First, if \(u\in\{3,6,10\}\), its binary weight is two, so \(\operatorname{Tr}(F_u(t))=\operatorname{Tr}(t)+2\operatorname{Tr}(t^{-1})=1\) for every \(t\in T_n\); therefore \(F_u(t)\ne0\), and all rational expressions below have nonzero denominators on this domain.

For each nonzero \(u\), set \(E(3)=\{1,2\}\), \(E(6)=\{2,4\}\), \(E(10)=\{2,8\}\), and \(k=\max E(u)\). Over \(\mathbb F_2[X]\), set

\[
Q=X^k,\qquad P=X^{k+1}+\sum_{e\in E(u)}X^{k-e},\qquad
H=P^{k+1}+\sum_{e\in E(u)}P^{k-e}Q^{e+1}+XQP^k.
\]

Thus \(F_u(X)=P/Q\) and

\[
F_u(F_u(X))+X=\frac{H(X)}{Q(X)P(X)^k}.
\]

The following **exact identities** in the polynomial ring over \(\mathbb F_2\) are the finite algebraic certificate; every factor is monic and irreducible, as independently checkable by polynomial gcd tests:

\[
\begin{split}
H_3&=(X+1)(X^2+X+1)^2,\\
H_6&=(X+1)^4(X^2+X+1)^2(X^4+X^3+1)^2,\\
H_{10}&=(X+1)^4(X^2+X+1)^4A_5^2B_5^2C_{10}^2D_{10}^2,
\end{split}
\]

where

\[
\begin{aligned}
A_5&=X^5+X^4+X^2+X+1,\\
B_5&=X^5+X^4+X^3+X^2+1,\\
C_{10}&=X^{10}+X^9+X^7+X^2+1,\\
D_{10}&=X^{10}+X^9+X^8+X^5+X^3+X+1.
\end{aligned}
\]

An irreducible monic polynomial of degree \(m\) over \(\mathbb F_2\) with coefficient of \(X^{m-1}\) equal to one has roots of absolute trace one in \(\mathbb F_{2^m}\). All seven distinct factors above have that property. A degree-\(m\) root belongs to \(\mathbb F_{2^n}\) precisely if \(m\mid n\); its trace in \(\mathbb F_{2^n}\) is \((n/m)\bmod2\). Consequently a given factor contributes all its \(m\) roots to \(T_n\) precisely when \(m\mid n\) and \(n/m\) is odd, and contributes zero otherwise.

The fixed-point equations \(F_u(X)=X\) have respective numerators

\[
X+1,\qquad X^2+1=(X+1)^2,\qquad
X^6+1=(X+1)^2(X^2+X+1)^2
\]

for \(u=3,6,10\). Hence the linear factor always supplies fixed points when \(n\) is odd; for \(u=10\), the quadratic factor additionally supplies two fixed points when \(n\equiv2\pmod4\). No other listed factor has fixed roots. All other roots in \(T_n\) of \(H_u\) are primitive period-two points: by the nonvanishing denominators above, they satisfy \(F_u^{\circ2}(t)=t\), while the fixed roots have just been excluded. Dividing their number by two gives the table. The identity case is immediate. The congruence classes for the two distinct five- and ten-degree factors are disjoint, so their maximum total is ten two-cycles.

The identity of \(H_u\) with the factored forms, the irreducibility tests, and the fixed-point factorizations may all be reproduced directly from `hx_two_cycle_checker.py` without external packages. The trace criterion uses the standard fact that, for a root of a monic irreducible polynomial, its trace is the coefficient immediately below the leading term (sign is immaterial in characteristic two).

## Verification

Run `python3 hx_two_cycle_checker.py` with Python 3. The program builds the second-iterate numerator by exact polynomial arithmetic over \(\mathbb F_2\), verifies each displayed factorization, tests irreducibility of all seven distinct factors using the finite-field criterion \(X^{2^m}\equiv X\pmod f\) and appropriate gcd checks, and checks the fixed-point numerator identities. It independently builds a finite-field representation in every degree \(1\leq n\leq15\), enumerates its entire trace-one fiber, and compares both observed cycle counts to the stated expressions, also checking bijectivity. It completes 32,767 trace-one inputs across those extension degrees; the infinite-degree result follows from the exact factorization and trace argument, **not** from this finite enumeration.

## Relationship to prior work

Hollmann–Xiang (2004, Theorem 4.1) proves that the three nonidentity maps permute the trace-one fiber and establishes associated Kloosterman-sum identities; its proof relies on off-diagonal injectivity, not the second-iterate factorization or these cycle counts. Yi Li (arXiv:2611.13848v1, first public November 10, 2026) proves their necessity conjecture by moments and explains that these are the basic index patterns; the present short-cycle census is not a corollary of the classification alone. Gerike–Kyureghyan (2020) analyzes cycle structure for another family \(X+\gamma f(X)\) in which \(f\) has values in a subfield; that hypothesis does not cover the present inverse-Frobenius maps. Bartoli–Li–Zhou (2025) addresses asymptotic classification of which index patterns are permutations, but full-text comparison was unavailable here and is a residual priority risk.

## Limitations

Only the four basic maps are considered. The theorem does not transfer automatically to their compositions with other linearized permutations, because such a composition need not preserve the cycle counts. No classification of primitive cycles of length at least three is asserted. The full text of one relevant 2025 classification article was inaccessible in this review; an unindexed prior derivation of the cycle census cannot be ruled out, so priority is not independently certified. The finite checker supports, but does not replace, the exact symbolic identities and trace proof.

## References

1. H. D. L. Hollmann and Q. Xiang, *Kloosterman sum identities over \(\mathbb F_{2^m}\)*, Discrete Mathematics **279** (2004), 277–286, DOI: https://doi.org/10.1016/S0012-365X(03)00275-9 . Public manuscript: https://bpb-us-w2.wpmucdn.com/sites.udel.edu/dist/a/6387/files/2017/08/Henk_Xiang_Kloos-1w8md32.pdf .
2. Yi Li, *A Moment Proof of the Hollman-Xiang Conjectures on Kloosterman Polynomials*, arXiv:2611.13848v1 (submitted November 10, 2026), https://arxiv.org/abs/2611.13848 .
3. D. Gerike and G. M. Kyureghyan, *Permutations on finite fields with invariant cycle structure on lines*, Designs, Codes and Cryptography **88** (2020), 1723–1740, https://doi.org/10.1007/s10623-020-00721-2 .
4. D. Bartoli, K. Li and Y. Zhou, *On the asymptotic classification of Kloosterman polynomials*, Proceedings of the American Mathematical Society (2025), https://doi.org/10.1090/proc/15483 (abstract consulted; full text not inspected).
