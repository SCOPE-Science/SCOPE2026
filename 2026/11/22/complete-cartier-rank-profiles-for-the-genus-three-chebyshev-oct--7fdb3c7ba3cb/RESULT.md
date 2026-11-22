# Complete Cartier rank profiles for the genus-three Chebyshev octic

## Finding

Let \(p\ge5\) be a prime, and let \(C_p\) be the smooth projective curve over \(\overline{\mathbb F}_p\) with affine equation
\[
y^2=\varphi_8(x)=x^8-8x^6+20x^4-16x^2+2,
\]
where \(\varphi_8\) is the monic Dickson–Chebyshev polynomial characterized by \(\varphi_8(t+t^{-1})=t^8+t^{-8}\). The curve has genus \(3\). For its Cartier operator \(\mathcal C\) on regular differentials, the complete ranks of the first three iterates, the geometric Jacobian \(p\)-rank \(f\), and the Jacobian \(a\)-number are as follows:

| \(p\bmod16\) | \(\operatorname{rank}\mathcal C\) | \(\operatorname{rank}\mathcal C^2\) | \(\operatorname{rank}\mathcal C^3\) | \(f\) | \(a\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(1\) | 3 | 3 | 3 | 3 | 0 |
| \(3\) | 2 | 1 | 1 | 1 | 1 |
| \(5\) | 1 | 0 | 0 | 0 | 2 |
| \(7\) | 2 | 2 | 2 | 2 | 1 |
| \(9\) | 1 | 1 | 1 | 1 | 2 |
| \(11\) | 2 | 1 | 1 | 1 | 1 |
| \(13\) | 1 | 0 | 0 | 0 | 2 |
| \(15\) | 0 | 0 | 0 | 0 | 3 |

All ranks for powers \(\mathcal C^m\), \(m\ge3\), equal the third-power rank. In particular, the Jacobian is ordinary exactly when \(p\equiv1\pmod{16}\), and superspecial exactly when \(p\equiv15\pmod{16}\). The two rank-zero classes \(p\equiv5,13\pmod{16}\) are **not superspecial**, since their Cartier rank is one. Among rank-one reductions, the classes \(p\equiv3,11\pmod{16}\) have \(a=1\), while \(p\equiv9\pmod{16}\) has \(a=2\).

## Assumptions and scope

All curves are considered over an algebraic closure of the prime field. The assumption \(p\ge5\) ensures an odd characteristic and avoids the small-characteristic boundary of the initiating Kummer automorphism study. The discriminant of \(\varphi_8\) equals \(2^{31}\), so it is separable for every such prime. The standard degree-eight hyperelliptic model therefore has genus three. The \(a\)-number is \(\dim\ker\mathcal C=3-\operatorname{rank}\mathcal C\), and the \(p\)-rank is the stable rank of the (semilinear) Cartier iterates. These numerical invariants do not by themselves determine every Newton slope or the full Ekedahl–Oort type.

## Proof

**1. A tame degree-two quotient.** Let \(k=\overline{\mathbb F}_p\) and consider the smooth genus-seven curve
\[
F:\quad w^2=z^{16}+1.
\]
The involution \(\tau(z,w)=(z^{-1},w/z^8)\) has order two. The invariant rational functions
\[
x=z+z^{-1},\qquad y=w/z^4
\]
satisfy \(y^2=z^8+z^{-8}=\varphi_8(x)\). Since \(z\) obeys \(z^2-xz+1=0\) and \(w=yz^4\), the degree of the function-field extension is two, and \(C_p\) is the quotient \(F/\langle\tau\rangle\). As \(p\ne2\), this quotient is separable and tame.

For \(1\le n\le7\), put \(\omega_n=z^{n-1}dz/w\). These form the standard basis of \(H^0(F,\Omega^1)\), and direct substitution gives
\[
\tau^*\omega_n=-\omega_{8-n}.
\]
The invariant differential space, and equivalently by Serre duality the invariant first-cohomology space, has dimension three and is represented by the pairs
\[
(1,7),\qquad(2,6),\qquad(3,5).
\]
The differential \(\omega_4\) is anti-invariant. Tame descent identifies these invariant spaces with those of \(C_p\).

**2. Exact support and nonvanishing of the Hasse–Witt map.** Write \(h=(p-1)/2\). The defining polynomial of \(F\) satisfies
\[
(z^{16}+1)^h=\sum_{k=0}^{h}\binom hk z^{16k}.
\]
In the standard hyperelliptic Hasse–Witt coefficient rule, a row indexed by \(i\) and column indexed by \(j\), with \(1\le i,j\le7\), can be nonzero only if
\[
p i-j=16k,\qquad 0\le k\le h.
\]
Whenever \(p i\equiv j\pmod{16}\) and \(1\le i,j\le7\), this range holds for \(p\ge5\). To see it directly, \(pi-j\) is a multiple of 16 greater than \(-7\), hence nonnegative. The bound \(pi-j\le8(p-1)\) follows for \(i\le6\) immediately, and for \(i=7\) when \(p\ge7\); the only remaining prime \(p=5\) has the congruent pair \((i,j)=(7,3)\), for which \(k=2=h\). All the resulting binomial coefficients are nonzero modulo \(p\), since \(h<p\).

The two members \(i,8-i\) of each invariant pair map to the two members \(j,8-j\) of another invariant pair or both map to zero. The corresponding exponents \(k\) and \(h-k\) have equal nonzero binomial coefficients. Thus restriction to invariant cohomology neither introduces cancellation nor creates a zero coefficient. Every surviving arrow is determined exactly by
\[
n\longmapsto \min(j,8-j),\qquad j\equiv pn\pmod{16},
\]
for \(n=1,2,3\), **provided** \(j\in\{1,2,3,5,6,7\}\); otherwise that basis vector maps to zero. Here a residue \(j\) is chosen in \(\{0,\ldots,15\}\). Reversal of all arrows under the dual Cartier convention leaves all iterate ranks unchanged.

**3. The eight residue classes.** Omitting nonzero scalar multipliers, the arrows on the three invariant directions are:

| \(p\bmod16\) | Nonzero arrows |
| --- | --- |
| \(1\) | \(1\to1,\ 2\to2,\ 3\to3\) |
| \(3\) | \(1\to3,\ 2\to2\) |
| \(5\) | \(1\to3\) |
| \(7\) | \(1\to1,\ 3\to3\) |
| \(9\) | \(2\to2\) |
| \(11\) | \(2\to2,\ 3\to1\) |
| \(13\) | \(3\to1\) |
| \(15\) | none |

Each nonzero arrow has an invertible coefficient, so a power has rank equal to the number of directed paths of that length; these are \((3,3,3)\), \((2,1,1)\), \((1,0,0)\), \((2,2,2)\), \((1,1,1)\), \((2,1,1)\), \((1,0,0)\), and \((0,0,0)\), in the row order above. Because the coefficients lie in \(\mathbb F_p\), Frobenius semilinearity does not affect ranks or the nonzero paths. The stable rank is the Jacobian \(p\)-rank, and \(a=3-\operatorname{rank}\mathcal C\). Vanishing Cartier in genus three gives a superspecial Jacobian; in all other rows \(a<3\). This proves the table and its consequences for every prime in the stated domain.

## Verification

The file `check_chebyshev_octic.py` provides two independent finite checks. First, it derives all eight directed-arrow diagrams purely from multiplication of residues modulo 16. Second, for every prime \(5\le p<200\), it expands \(\varphi_8(x)^{(p-1)/2}\) with exact modular integer coefficients, constructs the independent genus-three Hasse–Witt matrix, and checks the ranks of its first three powers and the \(a\)-number against the theorem. All 44 prime tests passed. Run it with `python3 check_chebyshev_octic.py`. This finite replay tests the implementation; the preceding quotient-and-binomial proof establishes the unbounded prime statement.

## Relationship to prior work

Kazemifard and Tafazolian [1] classify geometric automorphism groups of the Chebyshev–Kummer family, which includes this degree-eight genus-three curve. They do not state its Cartier or Jacobian rank profile. Tafazolian and Top [2] prove maximality conditions for even Chebyshev curves. Their \(p\equiv15\pmod{16}\) case already implies superspeciality through the established maximal-curve Cartier-vanishing criterion; **this isolated last row is not asserted as independently new**. The full rank profile in the other seven congruence classes, including nonmaximal rank-zero yet nonsuperspecial cases and a-number distinctions at fixed positive \(p\)-rank, is not determined by those maximality statements. The subsequent full maximality classification [3] is also about maximal extension fields, not the exact Cartier ranks in nonmaximal characteristics. The intervening CM-theoretic study of exactly the same Chebyshev family [7] investigates maximality and Newton slopes, especially in odd prime degrees, but does not give this degree-eight nonmaximal Cartier-iterate table.

Kodama, Top and Washio [4] study other genus-three Fermat-quotient curves (notably \(y^2=x^8+1\)), and the standard Fermat Hasse–Witt calculation [5] supplies an important general ingredient. Neither cited work states the eight-class profile for the different curve \(y^2=\varphi_8(x)\). A related exact Cartier profile of the curve \(y^2=(x+2)D_7(x)\) [6] uses the analogous quotient method but has a different defining curve, modulus 14 and rank pattern; it does not imply this degree-eight result. The contribution is the exact restriction of the monomial Frobenius support to this new involution-invariant subspace and its eight arithmetic regimes. General Fermat-character methods and potentially unindexed calculations are residual publication-priority risks.

## Limitations

The result fixes the degree-eight Chebyshev curve and applies to primes \(p\ge5\). It gives no assertion for varying Chebyshev degree, higher-genus analogues, complete Newton polygons, full Ekedahl–Oort types, or exact zeta numerators. The rank-zero cases \(p\equiv5,13\pmod{16}\) are proved nonsuperspecial but their precise Newton slopes are not determined here. Some extremal implications were already known through maximality results, as explicitly acknowledged. Independent mathematical validation has not been carried out.

## References

[1] A. Kazemifard and S. Tafazolian, *Automorphisms of Kummer and Artin–Schreier Curves Defined by Chebyshev Polynomials*, arXiv:2611.10255v1, first public 2026-11-06, primary MSC2020 14H37. https://arxiv.org/html/2611.10255v1

[2] S. Tafazolian and J. Top, *On certain maximal hyperelliptic curves related to Chebyshev polynomials*, arXiv:1902.06262, 2019, especially Theorem 1.5. https://arxiv.org/abs/1902.06262

[3] S. Tafazolian and J. Top, *A Complete Classification of Maximal Hyperelliptic Curves Related to Chebyshev Polynomials*, arXiv:2611.14198v1, 2026-11-10, Theorem 1.3 and Section 6. https://arxiv.org/abs/2611.14198

[4] T. Kodama, J. Top and T. Washio, *Maximal hyperelliptic curves of genus three*, Finite Fields Appl. 15 (2009), 392–403. https://doi.org/10.1016/j.ffa.2009.02.002

[5] T. Kodama and T. Washio, *Hasse-Witt matrices of Fermat curves*, Manuscripta Math. 60 (1988), 185–195. https://doi.org/10.1007/BF01161928

[6] *Complete Cartier rank profiles for the genus-three Dickson–Chebyshev quotient*, research record (2026-11-08). https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-cartier-rank-profiles-for-the-genus-three-dickson-cheby--b5ac04c241b2/RESULT.md

[7] S. Tafazolian and J. Top, *CM theory, maximal hyperelliptic curves, and Chebyshev polynomials*, arXiv:2509.00273v1, 2025-08-29, Sections 2–4. https://arxiv.org/html/2509.00273v1
