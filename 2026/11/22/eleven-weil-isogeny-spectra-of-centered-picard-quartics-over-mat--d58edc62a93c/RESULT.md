# Eleven Weil-isogeny spectra of centered Picard quartics over \(\mathbb F_5\)

## Finding
Let \(a,b,c\in\mathbb F_5\), and let \(C_{a,b,c}\) denote the smooth projective model of
\[
 C_{a,b,c}:\quad y^3=x^4+a x^2+b x+c.
\]
Restrict to coefficient triples for which the degree-four polynomial on the right is squarefree. There are exactly \(100\) such marked triples, and every curve has genus \(3\). Their complete Hasse--Weil numerators are precisely the following eleven distinct polynomials:
\[
 L_A(T)=1+A T^2+5A T^4+125T^6
       =(1+5T^2)(1+(A-5)T^2+25T^4),
\]
with the indicated exhaustive marked-parameter multiplicities.

| \(A\) | \(\#C_{a,b,c}(\mathbb F_{25})\) | Number of marked triples | Jacobian \(5\)-rank |
|---:|---:|---:|---:|
| -3 | 20 | 10 | 2 |
| -2 | 22 | 4 | 2 |
| 0 | 26 | 12 | 0 |
| 1 | 28 | 8 | 2 |
| 3 | 32 | 20 | 2 |
| 6 | 38 | 8 | 2 |
| 7 | 40 | 12 | 2 |
| 9 | 44 | 16 | 2 |
| 10 | 46 | 4 | 0 |
| 12 | 50 | 4 | 2 |
| 13 | 52 | 2 | 2 |
| **Total** | | **100** | |

In particular all these Jacobians share a supersingular elliptic *isogeny factor* with Weil polynomial \(1+5T^2\), even though the curves need not admit a common elliptic quotient map. Their Jacobians occupy exactly eleven distinct \(\mathbb F_5\)-isogeny classes; the two rank-zero types comprise \(16\) marked equations, and the remaining nine types comprise \(84\). For every positive odd integer \(n\), all admitted curves have \(5^n+1\) points over \(\mathbb F_{5^n}\). The classification is of **marked coefficient presentations and their Weil polynomials**, not of abstract curve-isomorphism classes.

## Assumptions and scope
The base field is exactly \(\mathbb F_5\); the monic centered quartic is part of the marking. The nonsingularity condition is that \(f=x^4+a x^2+b x+c\) have no multiple geometric roots, equivalently \(\gcd(f,f')=1\). No restriction is placed on the parameters except squarefreeness. The polynomial \(L_C(T)\) is normalized by \(Z(C,T)=L_C(T)/((1-T)(1-5T))\) and \(L_C(0)=1\). The \(5\)-rank means the dimension of geometric \(5\)-torsion over \(\mathbb F_5\). Counts in the table include different marked triples even when their curves are isomorphic.

## Proof
**Genus and smooth parameter count.** The superelliptic degree-three map \(x:C_{a,b,c}\longrightarrow\mathbb P^1\) is tame and has five totally ramified geometric branch points: four distinct finite roots of \(f\) and infinity. Riemann--Hurwitz gives \(2g-2=3(-2)+5(3-1)=4\), hence \(g=3\). There are \(5^4-5^3=500\) monic squarefree quartic polynomials over \(\mathbb F_5\). Translation of the variable has a unique choice eliminating the cubic coefficient, since \(4\) is invertible in \(\mathbb F_5\), and each centered quartic has exactly five translates. Thus precisely \(100\) monic centered quartics are squarefree, independently of the direct computation below.

**Odd extensions and the numerator.** For every odd \(n\ge1\), \(5^n-1\) is coprime to \(3\). Thus the cube map on \(\mathbb F_{5^n}\) is a bijection. For each affine \(x\), exactly one affine \(y\) satisfies the equation, and the smooth projective model has exactly one point at infinity; therefore \(\#C(\mathbb F_{5^n})=5^n+1\). The standard logarithmic identity for zeta functions, \(\log L_C(T)=\sum_{n\ge1}(\#C(\mathbb F_{5^n})-5^n-1)T^n/n\), shows that \(\log L_C\) is even and hence \(L_C(T)\) itself is even. Since \(\deg L_C=6\), write \(L_C(T)=1+A T^2+B T^4+125T^6\). The genus-three functional equation \(L_C(T)=125T^6 L_C(1/(5T))\) gives \(B=5A\). Comparing the coefficient of \(T^2\) in \(\log L_C\) gives \(A=(\#C(\mathbb F_{25})-26)/2\), which is an integer. Algebraic division proves the displayed factorization by \(1+5T^2\). That degree-two factor is the Weil polynomial of a supersingular elliptic curve over \(\mathbb F_5\); by the finite-field isogeny classification, it is a common elliptic isogeny factor of the Jacobians, but no morphism from the curves to that elliptic curve is asserted.

**Complete coefficient enumeration.** In the finite field \(\mathbb F_{25}=\mathbb F_5[z]/(z^2-2)\), the multiplicative group has order \(24\). The number of solutions of \(y^3=v\) is \(1\) for \(v=0\), \(3\) for nonzero \(v\) satisfying \(v^8=1\), and \(0\) otherwise. Hence the finite, exact formula
\[
 \#C_{a,b,c}(\mathbb F_{25})
 =1+\sum_{x\in\mathbb F_{25}}\left(\mathbf1_{f(x)=0}+3\mathbf1_{f(x)\ne0\ \text{and}\ f(x)^8=1}\right).
\]
Enumerate every one of the \(125\) coefficient triples; reject the \(25\) with \(\gcd(f,f')\ne1\). For the remaining \(100\), the formula yields exactly the eleven rows displayed above. The complete standalone `verify_picard_f5.py` independently checks the same \(100\) cases in two incompatible polynomial bases of \(\mathbb F_{25}\), compares direct cube-fiber enumeration with the eighth-power criterion, tests squarefreeness by Euclidean gcd and an explicit quartic discriminant, and asserts the complete frequency table. The computation is **exhaustive over the explicitly finite set of marked triples**, not an extrapolation from sample data.

**Isogeny strata and ranks.** Different values of \(A\) give different characteristic polynomials of Frobenius; by the finite-field isogeny theorem, they give different Jacobian isogeny classes. Reducing the displayed \(L_A(T)\) modulo \(5\) gives \(1+A T^2\); its degree is \(2\) when \(5\nmid A\), and \(0\) otherwise. The degree is the geometric \(5\)-rank of the Jacobian, so the marked rank-zero total is \(12+4=16\), and the other nine strata contain \(84\) presentations. The rank-two Newton slopes are \((0,0,\tfrac12,\tfrac12,1,1)\); for the rank-zero types all six slopes are \(\tfrac12\), as also follows directly from the Newton polygon of the even polynomial. This agrees, non-circularly, with the known rank-zero coefficient equation \(c^2+a^2c+ab^2=0\), which the verifier checks independently for every admitted triple.

## Verification
Run `python3 verify_picard_f5.py` using the Python 3 standard library. The checker reconstructs both fields, certifies the two polynomial presentations by their finite-field arithmetic and the order-24 structure, counts each smooth marked curve over the quadratic extension by two independent methods, checks the discriminant and Euclidean gcd tests agree, and tests the entire eleven-stratum table and rank comparison. It returns `PICARD_F5_11_WEIL_TYPES_VERIFIED smooth=100 singular=25 types=11 rank0=16 rank2=84` on success. All identities about the genus, odd extensions, Weil polynomial shape, isogeny factors, and the interpretation of \(5\)-ranks are justified algebraically above; the exact finite frequency table is certified by the complete enumerator.

## Relationship to prior work
Bouw--Koutsianas--Sijsling--Wewers (arXiv:1902.09624v1, 2019-02-25) establish the Picard-curve normal forms and study conductor/discriminant questions, principally over characteristic-zero arithmetic fields, not the entire \(\mathbb F_5\) marked Weil spectrum. Nourozi--Rahmati (arXiv:2306.07823v1, 2023-06-13) investigate Cartier ranks and \(a\)-numbers and include a characteristic-five example, but their inspected theorem does not tabulate the eleven rational isogeny types. Laga--Shnidman (arXiv:2308.15297, 2023) develop the bielliptic Picard subfamily, a proper sublocus of this three-parameter space. Kazemifard--Tafazolian (2015, DOI:10.1016/j.ffa.2014.12.002) investigate selected Picard curves, not this exhaustive coefficient table.

Previously published mathematical records independently determine the entire family-wide \(5\)-rank and \(a\)-number, including its \(16\)-presentation rank-zero locus; that result is credited, not claimed as new: see *A split-point census of the nonordinary divisor of characteristic-five Picard curves*, at https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-split-point-census-of-the-nonordinary-divisor-of-characteristi--a210d5dbee0c . Another earlier record, *Constant Newton polygon and ordinary Pryms in the characteristic-five bielliptic Picard family*, at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-constant-newton-polygon-and-ordinary-pryms-in-the-characteristic--37c60ad9976f , proves uniform Newton and Prym properties for the \(b=0\) slice. These do not imply the present complete eleven-type Weil spectrum. The assessed new fact is the exact distribution of full Frobenius polynomials and its common elliptic factor, with the proof specialized to \(\mathbb F_5\).

## Limitations
This is a complete finite-field marked-parameter census, not an abstract or geometric isomorphism-class census. A common elliptic *isogeny* factor does not by itself produce an elliptic quotient of each curve. The general Picard-curve rank classification and rank-zero frequency were already known. Historical priority cannot be certified absolutely: earlier unindexed computational tables, the inaccessible full text of Estrada-Sarlabous's 1991 article, and databases of finite-field zeta functions remain possible overlap sources. No formal or independent mathematical audit has been performed.

## References
1. I. I. Bouw, A. Koutsianas, J. Sijsling, and S. Wewers, *Conductor and discriminant of Picard curves*, arXiv:1902.09624v1, first public 2019-02-25, https://arxiv.org/abs/1902.09624 .
2. V. Nourozi and F. Rahmati, *The Rank of the Cartier Operator on Picard Curves*, arXiv:2306.07823v1, first public 2023-06-13, https://arxiv.org/abs/2306.07823 .
3. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297 (2023), https://arxiv.org/abs/2308.15297 .
4. A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, *Finite Fields Appl.* 34 (2015), 107--122, https://doi.org/10.1016/j.ffa.2014.12.002 .
5. J. Estrada-Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic* \(p>0\), *Math. Nachr.* 152 (1991), 329--340, https://doi.org/10.1002/mana.19911520125 (full text not inspected).
