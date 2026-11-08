# Frobenius arithmetic and exceptional reductions of the \(28\)-bitangent divisor of the Fermat quartic

## Finding

Let \(k=\mathbb F_q\) have odd characteristic \(p\), and put
\[
C:\ X^4+Y^4+Z^4=0\subset\mathbb P^2_k.
\]
Let \(B\) be the reduced geometric union of all \(28\) bitangent lines of \(C\); because this collection is Galois stable, \(B\) is defined over \(k\). For every integer \(n\ge1\), set \(Q=q^n\). Its complete extension-field point count is
\[
\#B(\mathbb F_Q)=
\begin{cases}
28Q-305,&p\notin\{3,5,17\},\ Q\equiv1\pmod8,\\
16Q-65,&p\notin\{3,5,17\},\ Q\equiv5\pmod8,\\
4Q+1,&p\notin\{3,5,17\},\ Q\equiv3,7\pmod8,\\
28Q-161,&p=3,\ Q\equiv1\pmod8,\\
4Q+1,&p=3,\ Q\equiv3\pmod8,\\
28Q-289,&p=5,\ Q\equiv1\pmod8,\\
16Q-49,&p=5,\ Q\equiv5\pmod8,\\
28Q-257,&p=17.
\end{cases}
\]
There are precisely three odd characteristics in which the complex intersection lattice degenerates: \(3,5,17\). The geometric intersection profiles (number of points incident to exactly \(r\) lines) are:

| Characteristic | Double points | Triple points | Quadruple points |
| --- | ---: | ---: | ---: |
| \(p\notin\{2,3,5,17\}\) | 288 | 0 | 15 |
| \(p=3\) | 0 | 0 | 63 |
| \(p=5\) | 240 | 16 | 15 |
| \(p=17\) | 144 | 48 | 15 |

In particular, \(B(\mathbb F_q)=\mathbb P^2(\mathbb F_q)\) holds **exactly** for \(q\in\{3,5,9\}\). In the generic \(Q\equiv3,5,7\pmod8\) cases, there are exactly three rational quadruple intersection points through which **no rational component line passes**. The same phenomenon occurs in characteristics \(3\) and \(5\) when the extension degree over the prime field is odd.

The Hasse--Weil zeta function is explicit. Writing \(Z(B/k,T)=\exp(\sum_{n\ge1}\#B(\mathbb F_{q^n})T^n/n)\), the possibilities are
\[
\begin{array}{c|c}
\text{base-field condition} & Z(B/k,T)\\ \hline
p\notin\{3,5,17\},\ q\equiv1\pmod8 &(1-T)^{305}/(1-qT)^{28}\\
p\notin\{3,5,17\},\ q\equiv5\pmod8 &(1-T)^{185}(1+T)^{120}/((1-qT)^{22}(1+qT)^6)\\
p\notin\{3,5,17\},\ q\equiv3,7\pmod8 &(1-T)^{152}(1+T)^{153}/((1-qT)^{16}(1+qT)^{12})\\
p=3,\ q\equiv1\pmod8 &(1-T)^{161}/(1-qT)^{28}\\
p=3,\ q\equiv3\pmod8 &(1-T)^{80}(1+T)^{81}/((1-qT)^{16}(1+qT)^{12})\\
p=5,\ q\equiv1\pmod8 &(1-T)^{289}/(1-qT)^{28}\\
p=5,\ q\equiv5\pmod8 &(1-T)^{169}(1+T)^{120}/((1-qT)^{22}(1+qT)^6)\\
p=17 &(1-T)^{257}/(1-qT)^{28}.
\end{array}
\]

## Assumptions and scope

All schemes and rational points are over finite fields of odd characteristic, and all intersection multiplicities in this statement count **distinct geometric lines** through a geometric point, not scheme-theoretic multiplicities of the plane divisor. A rational singular point may have zero rational normalization branches. The curve \(C\) is smooth for all odd \(p\), including \(p=3\). The claim is for the reduced union \(B\), **not** for rational points of the Fermat quartic \(C\) itself.

Choose a primitive eighth root of unity \(\zeta\), with \(\zeta^4=-1\). The \(28\) lines are the twelve lines
\[
X_i-\zeta^aX_j=0\quad (\{i,j\}\in\{\{0,1\},\{0,2\},\{1,2\}\},\quad a\in\{1,3,5,7\})
\]
and the sixteen lines
\[
Z-\zeta^{2a}X-\zeta^{2b}Y=0\quad(a,b\in\{0,1,2,3\}).
\]
The normalizations of all \(28\) components are projective lines. These \(28\) distinct lines are all the bitangents over an algebraic closure in odd characteristic: the first twelve have contact order four, while the remaining sixteen restrict the quartic equation to twice the square of a quadratic. In characteristic three that quadratic itself is a square, so the latter become hyperflex lines as well. The standard odd-theta-characteristic count for a smooth plane quartic in characteristic different from two gives exactly \(28\).

## Proof

**1. Explicit bitangents and their field of definition.** Put \(u=\zeta^{2a}X\), \(v=\zeta^{2b}Y\) along a line \(Z=u+v\). Since \(u^4=X^4\) and \(v^4=Y^4\), one has the polynomial identity
\[
X^4+Y^4+Z^4=u^4+v^4+(u+v)^4=2(u^2+uv+v^2)^2.
\]
On a line \(X_i=\zeta^a X_j\) with odd \(a\), the remaining fourth power vanishes to order four at its unique intersection with \(C\). Since \(2\) is a unit, these are the required bitangents. Distinctness follows from the separability of \(t^8-1\). Frobenius acts on every label by \(\zeta\mapsto\zeta^Q\), so all lines split over \(\mathbb F_{q^2}\).

**2. Exhaustive geometric incidence and the exceptional-prime certificate.** Work integrally in
\[
A=\mathbb Z[t]/(t^4+1),
\]
where \(t\) represents \(\zeta\). For each of the \(\binom{28}{2}=378\) line pairs, form the cross product of their coefficient vectors and determine its complete support of vanishing line equations. In characteristic zero the resulting \(303\) supports have sizes \(2\) (\(288\) supports) and \(4\) (\(15\) supports). Thus \(288+6\cdot15=378\), agreeing with the known complex arrangement.

For all \(\binom{28}{3}=3276\) triples, take the determinant of their three coefficient vectors in \(A\). For nonzero determinants compute the **absolute field norm** by the exact determinant of the associated multiplication map \(A\to A\) on the integral basis \(1,t,t^2,t^3\). The complete set of nonzero absolute norm values is
\[
\{1,2,4,8,9,16,17,32,36,64,256,400\}.
\]
The only possible odd prime divisors are therefore \(3,5,17\). The numbers of nonzero characteristic-zero triple determinants divisible by these primes are \(384,32,192\), respectively. Since all \(28\) lines remain pairwise distinct modulo any odd prime, all other odd reductions preserve exactly the characteristic-zero concurrence relations. No inference from a finite sample of prime fields is used in this step.

For \(p=3,5,17\), all eighth roots are contained in \(\mathbb F_{p^2}\). Direct exact projective normalization of all \(378\) pairwise cross products, together with the full vanishing-line support test, gives the exceptional profiles in the table. The second incidence computation checks every point against **all** \(28\) lines rather than estimating multiplicities from the number of pairs. Every exceptional intersection point lies in \(\mathbb F_{p^2}\); no further geometric intersections exist.

**3. Rational branches and the finite-étale scissors identity.** Let \(\mathcal L\) denote the finite étale scheme of \(28\) component lines, \(\mathcal P\) the reduced finite étale scheme of distinct geometric singular points of their union, and \(\mathcal I\) the finite étale incidence scheme of pairs (singular point, component line through it). The normalization and the complement of the singular locus give in the Grothendieck ring
\[
[B]=(\mathbb L+1)[\mathcal L]-[\mathcal I]+[\mathcal P],
\qquad \mathbb L=[\mathbb A^1].
\]
Indeed each component is a projective line over its finite field of definition; at each singular geometric point there is one normalization preimage for each incident line. Taking rational points gives
\[
\#B(\mathbb F_Q)=\#\mathcal L(\mathbb F_Q)(Q+1)-\#\mathcal I(\mathbb F_Q)+\#\mathcal P(\mathbb F_Q).
\]
Frobenius-invariant supports give the following *complete* table. The pair \((m,r)\) means \(m\) geometric branches at a rational singular point, of which \(r\) are rational; \((m,r):s\) means exactly \(s\) such rational points.

| Condition on \(Q\) | Rational component lines | Rational singular-point types \((m,r):s\) |
| --- | ---: | --- |
| \(p\notin\{3,5,17\},\ Q\equiv1\pmod8\) | 28 | \((2,2):288;\ (4,4):15\) |
| \(p\notin\{3,5,17\},\ Q\equiv3,7\pmod8\) | 4 | \((4,0):3;\ (4,2):6\) |
| \(p\notin\{3,5,17\},\ Q\equiv5\pmod8\) | 16 | \((2,2):48;\ (4,0):3;\ (4,4):12\) |
| \(p=3,\ Q\equiv3\pmod8\) | 4 | \((4,0):3;\ (4,2):6\) |
| \(p=3,\ Q\equiv1\pmod8\) | 28 | \((4,4):63\) |
| \(p=5,\ Q\equiv5\pmod8\) | 16 | \((3,3):16;\ (4,0):3;\ (4,4):12\) |
| \(p=5,\ Q\equiv1\pmod8\) | 28 | \((2,2):240;\ (3,3):16;\ (4,4):15\) |
| \(p=17\) | 28 | \((2,2):144;\ (3,3):48;\ (4,4):15\) |

For the generic rows, the Frobenius action is computed on the characteristic-zero incidence supports by multiplying eighth-root exponents by \(Q\pmod8\); the norm certificate proves that these supports remain valid after all nonexceptional odd reductions. For the exceptional rows, direct Frobenius action on the point coordinates over \(\mathbb F_{p^2}\) verifies the table. Substituting its entries in the scissors formula yields the stated point counts.

**4. Zeta functions and plane-filling cases.** For each fixed \(q\), the preceding counts depend only on \(q^n\) and on the parity of \(n\). Write each count as an integral linear combination of \(q^n\), \((-q)^n\), \(1\), and \((-1)^n\). Summing \(\sum_{n\ge1}a^nT^n/n=-\log(1-aT)\) proves each displayed zeta factorization. Direct substitution gives full-plane point coverage for \(q=3,5,9\). For \(q\ge29\), the union of \(28\) projective lines has at most \(28(q+1)<q^2+q+1\) rational points; for \(q\in\{7,11,13,17,19,23,25,27\}\), the exact formulas show strict inequality. Those are all remaining odd prime powers below \(29\).

## Verification

Execute with ordinary Python 3 and no third-party packages:

```console
python3 verify_incidence.py
python3 verify_direct.py
```

The first script enumerates all \(378\) line pairs and all \(3276\) triples over the exact cyclotomic order; computes complete supports and the norm set; enumerates each exceptional characteristic over a splitting field; and checks all rational-singularity tables. The second script independently enumerates every rational projective point over the thirteen prime fields \(3,5,7,11,13,17,19,23,29,31,37,41,43\) and three quadratic-extension fields \(\mathbb F_9,\mathbb F_{25},\mathbb F_{49}\), comparing actual union membership against the formulas. The first script provides the all-characteristic algebraic certificate; the second is a separate finite-range check, not a replacement for the proof.

Expected assertion lines are `VERIFY_DYCK_INCIDENCE_OK 28_LINES 3276_TRIPLES 3_5_17_EXCEPTIONAL`, `VERIFY_DYCK_DIRECT_OK 13_PRIME_FIELDS`, and `VERIFY_DYCK_DIRECT_EXTENSION_OK F9_F25_F49`.

## Relationship to prior work

Janasz--Pokora--Zieliński, *On arrangements of smooth plane quartics and their bitangents*, first posted August 31, 2023 (arXiv:2308.16514, Section 3.2, Proposition 3.2, Tables 5--7), explicitly determines the \(288\)-double/\(15\)-quadruple **complex** incidence pattern and prints the bitangent lines; neither that pattern nor the existence and equations of the \(28\) lines are claimed as new. The result here is the **integral exceptional-reduction classification** and **uniform finite-field arithmetic of the reduced union**, including nonrational branches over rational singularities, all extension counts, and the zeta functions.

Dolgachev, *Automorphisms of del Pezzo surfaces in odd characteristic* (2024, Section 4), describes the exceptional characteristic-three symmetry of the Fermat quartic, including its Hermitian behavior and vanishing Hessian. This supports the special role of characteristic three but does not supply the bitangent divisor's general arithmetic classification. Betten--Kaplan--Karaoglu, *Classification of Quartic Curves Over Small Finite Fields* (October 29, 2021), tabulate special quartics and their \(28\) bitangents, including the characteristic-three \(63\)-quadruple-point phenomenon over \(\mathbb F_9\). The isolated finite-field table entry is acknowledged, not claimed as a new observation.

## Limitations

The theorem excludes characteristic two, where the standard 28-bitangent description changes. It concerns the **reduced divisor**, not embedded scheme-theoretic intersection multiplicities, freeness, or resolution invariants; the first-publication priority of the complete arithmetic calculation is not independently established. The direct second verifier samples finitely many prime fields, but the all-characteristic statement is justified by the exact determinant-norm certificate and the complete geometric/Frobenius enumeration. Independent mathematical review has not been performed.

## References

1. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514v1 (2023-08-31), especially Section 3.2 and Proposition 3.2; subsequent revised version in *Fundamenta Mathematicae* 268 (2025), 151--170. https://arxiv.org/abs/2308.16514
2. I. Dolgachev, *Automorphisms of del Pezzo surfaces in odd characteristic*, *Journal of the London Mathematical Society* (2024), DOI:10.1112/jlms.12905, Section 4. https://doi.org/10.1112/jlms.12905
3. A. Betten, N. Kaplan, F. Karaoglu, *Classification of Quartic Curves Over Small Finite Fields*, published online October 29, 2021. https://www.math.colostate.edu/~betten/mathdata/quartic_curves.html
