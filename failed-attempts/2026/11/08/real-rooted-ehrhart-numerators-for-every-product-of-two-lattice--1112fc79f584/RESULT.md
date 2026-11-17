# Real-rooted Ehrhart numerators for every product of two lattice polygons

## Finding
Let \(P,Q\subset\mathbb R^2\) be arbitrary full-dimensional lattice polygons and \(T=P\times Q\subset\mathbb R^4\). Then **every zero** of the Ehrhart \(h^*\)-polynomial \(h_T^*(z)\) is real and strictly negative. The constant polynomial is treated as real-rooted by convention. No lattice-width condition, normal-fan condition, or individual real-rootedness assumption on either factor is necessary.

With \(I,J\) the numbers of interior lattice points and \(B,C\) the numbers of boundary lattice points of \(P,Q\), put \(b=B-3\) and \(c=C-3\). The exact numerator is
\[
\begin{aligned}
h_T^*(z)={}&1+A z+D z^2+E z^3+I J z^4,\\
A={}&I J+I c+3I+J b+3J+bc+3b+3c+4,\\
D={}&11I J+7I c+9I+7J b+9J+4bc+3b+3c+1,\\
E={}&11I J+4I c+4J b+bc.
\end{aligned}
\]
In particular this includes two factors that individually have nonreal numerator roots. For example, the lattice triangle with vertices \((0,0),(2,1),(1,2)\) has \(h_P^*(z)=1+z+z^2\), whereas
\[
h_{P\times P}^*(z)=(1+4z+z^2)(1+7z+z^2).
\]

## Assumptions and scope
A *lattice polygon* is a compact, full-dimensional convex hull of finitely many points of \(\mathbb Z^2\). Every such polygon has integer counts \(I\ge0\), \(B\ge3\). The product uses the product lattice \(\mathbb Z^4\). Its Ehrhart series is \(\sum_{n\ge0}|nT\cap\mathbb Z^4|z^n=h_T^*(z)/(1-z)^5\). A 'strictly negative zero' excludes zero itself; this follows because the constant coefficient equals one. Zeros are counted with multiplicities, but the proof gives distinct roots in the nontrivial exceptional cases.

## Proof
**1. Reduction to three exceptional polygon types.** Pick's formula gives
\[
L_P(n)=\bigl(I+B/2-1\bigr)n^2+(B/2)n+1,
\qquad h_P^*(z)=1+(I+B-3)z+I z^2.
\]
Its quadratic discriminant (when \(I>0\)) is \((I+B-3)^2-4I\). This is nonnegative whenever \(B\ge4\) (at least \((I-1)^2\)), or \(B=3\) and \(I\ge4\) (then \(I(I-4)\ge0\)). For \(I=0\) the degree drops and the numerator is real-rooted. Hence an individual polygon numerator is *not* real-rooted precisely when \(B=3\) and \(I\in\{1,2,3\}\). When both inputs are real-rooted, Wagner's Hadamard-product theorem proves real-rootedness of the product numerator. It remains to consider an exceptional first polygon.

**2. Exact product transformation.** For all \(n\ge0\), \(L_T(n)=L_P(n)L_Q(n)\). The fourth-dimensional finite-difference identity
\[
[z^k]h_T^*(z)=\sum_{j=0}^{k}(-1)^{k-j}\binom5{k-j}L_P(j)L_Q(j),\qquad 0\le k\le4
\]
yields the coefficients in the Finding. Set \(B=3\), \(I=i\in\{1,2,3\}\), and retain \(J\ge0,c=C-3\ge0\). The reduced quartic, with zero leading terms allowed, is
\[
H_i(z;J,c)=1+\bigl(3i+4+(i+3)(J+c)\bigr)z
+\bigl(9i+1+(11i+9)J+(7i+3)c\bigr)z^2
+\bigl(11iJ+4ic\bigr)z^3+iJz^4.
\]

**3. Exact discriminant certificate.** Let \(\operatorname{Disc}_z\) denote the standard polynomial discriminant (the resultant of a polynomial and its derivative with the conventional sign and leading-coefficient normalization). Direct expansion produces the following *finite algebraic identities*; the complete integer coefficients are in `DISCRIMINANT_CERTIFICATE.json`, and `verify.py` reconstructs the two-variable and univariate discriminants independently from the displayed \(H_i\). For \(J=1+u\), with indeterminates \(u,c\), the polynomial
\[
\operatorname{Disc}_z H_i(z;1+u,c)
=\sum_{\alpha+\beta\le6}d_{i,\alpha,\beta}u^\alpha c^\beta
\]
has **all 28 coefficients strictly positive**. Its lowest integer coefficient and its constant coefficient are:

| \(i\) | positive coefficients | smallest coefficient | constant coefficient |
|---:|---:|---:|---:|
| 1 | 28 | 9216 | 43740 |
| 2 | 28 | 206400 | 5718996 |
| 3 | 28 | 1492992 | 79627752 |

Consequently its discriminant is strictly positive for every \(J\ge1\), \(c\ge0\). To rule out the alternative of no real zeros, note \(H_i(0;J,c)=1\), its leading coefficient \(iJ\) is positive, and the following evaluations are strictly negative (using \(u=J-1\ge0\)):
\[
\begin{aligned}
H_1(-1/5;1+u,c)&=-\frac{54u+270c+54}{625},\\
H_2(-1/6;1+u,c)&=-\frac{47u+258c+137}{648},\\
H_3(-1/8;1+u,c)&=-\frac{645u+1632c+1413}{4096}.
\end{aligned}
\]
There is therefore one zero between that negative evaluation point and zero, and another between minus infinity and that point. A real quartic with positive discriminant has either zero or four distinct real roots; it follows that all four are real. All coefficients of \(H_i\) are positive, so no root is nonnegative.

**4. Degree-drop boundaries.** For \(J=0\) and \(c>0\), \(H_i\) is cubic with leading coefficient \(4ic>0\). Its cubic discriminant is a polynomial in \(c\) with the following coefficient lists in ascending powers, all strictly positive:
\[
\begin{array}{c|l}
i&\text{coefficients of }\operatorname{Disc}_zH_i(z;0,c)\\\hline
1&(900,2952,3780,2304,576)\\
2&(8664,22416,25065,13638,3225)\\
3&(44688,96816,95472,46656,10368).
\end{array}
\]
Thus the cubic has three distinct real, necessarily negative roots. Finally \(J=c=0\) gives a quadratic with discriminant \(9,24,57\), respectively for \(i=1,2,3\), hence two negative roots. The proof covers all integer polygon parameters and both exceptional-factor permutations.

## Verification
The included `verify.py` runs exact integer/rational polynomial arithmetic using SymPy, verifies the universal numerator identity against Pick's two Ehrhart polynomials, recomputes every coefficient of the three quartic and three cubic discriminants, checks their complete values against the companion `DISCRIMINANT_CERTIFICATE.json`, checks all 28 coefficient-positivity conditions in each quartic case, and checks the negative witnesses and degree-drop discriminants. This is a **finite algebraic certificate of polynomial identities**, not a sampling argument. Execute from a directory containing the two companion files: `python verify.py`. An exact-arithmetic computation does not independently certify the literary priority of the result.

## Relationship to prior work
Wagner (1992) proves real-rootedness of the Ehrhart numerator under Cartesian products **when both input numerators are real-rooted**; Ferroni–Higashitani (2023/2024, Section 3.1) and Feihu Liu (arXiv:2610.06338, 2026, Theorem 2.2(i), Section 2) state this hypothesis explicitly. The present classification additionally treats all products containing a planar nonreal-rooted factor, which precisely consist of the three exceptional Pick-data types. Yanxin Liu–Mao (arXiv:2609.11589, Section 5) establish product preservation of log-concavity when both inputs are log-concave, a distinct and weaker conclusion. In contrast, the present statement concludes real-rootedness **without any hypothesis on factor numerator roots**.

## Limitations
This concerns full-dimensional **two-dimensional lattice polygon factors only**. It does not assert real-rootedness for arbitrary products with a higher-dimensional factor, arbitrary lattice four-polytopes, or general products of non-real-rooted numerator polynomials. The discriminant identities are supplied in full and checked by reproducible exact algebra, but there has been no independent expert review. Older work could contain an equivalent special-case classification; absence from the inspected literature is not an absolute priority proof.

## References
1. Feihu Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338, first public 2026-10-05, especially Theorem 2.2(i) and Section 2. https://arxiv.org/abs/2610.06338
2. Luis Ferroni and Akihiro Higashitani, *Examples and Counterexamples in Ehrhart Theory*, arXiv:2307.10852, first public 2023-07-20; Section 3.1 and Theorem 3.3. https://arxiv.org/abs/2307.10852
3. Yanxin Liu and Jianxi Mao, *Preservation of Log-Concavity under Hadamard Products*, arXiv:2609.11589, first public 2026-09-10; Section 5. https://arxiv.org/abs/2609.11589
4. David G. Wagner, *Total Positivity of Hadamard Products*, Journal of Mathematical Analysis and Applications 163 (1992), 459–483, Theorem 0.2 (as stated in references 1 and 2).
5. Georg A. Pick, *Geometrisches zur Zahlenlehre*, Sitzungsberichte des deutschen naturwissenschaftlich-medicinischen Vereines für Böhmen 'Lotos' 19 (1899), 311–319.
