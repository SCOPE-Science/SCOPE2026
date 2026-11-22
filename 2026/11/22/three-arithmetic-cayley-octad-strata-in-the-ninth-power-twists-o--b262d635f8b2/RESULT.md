# Three arithmetic Cayley-octad strata in the ninth-power twists of the Picard quartic

## Finding

Let \(q\) be any **odd prime power with \(q\equiv1\pmod 9\)**, and set \(k=\mathbb F_q\). For each \(c\in k^\times\), let \(C_c\) be the smooth plane quartic
\[
C_c:\quad Y^3Z=X^4-cXZ^3.
\]
Count the coefficient-marked parameters \(c\) (without identifying isomorphic equations). The complete arithmetic classification is:

| Number of parameters \(c\) | Rational bitangents | Rational even theta characteristics / Cayley octads | Least extension degree admitting a symmetric linear determinant | Geometric Frobenius cycles, bitangents; octads |
|---:|---:|---:|---:|---|
| \((q-1)/9\) | \(28\) | \(36\) | \(1\) | \(1^{28};\ 1^{36}\) |
| \(2(q-1)/9\) | \(1\) | \(0\) | \(3\) | \(1^1 3^9;\ 3^{12}\) |
| \(6(q-1)/9\) | \(1\) | \(0\) | \(9\) | \(1^1 9^3;\ 9^4\) |

Here a symmetric linear determinant means an equation of the curve as the zero locus of the determinant of a symmetric \(4\times4\) matrix of ternary linear forms over the indicated field, considered up to ordinary symmetric determinantal equivalence. The Cayley octads are *unordered, unlabelled*, and correspond to the \(36\) even theta characteristics. In particular, for **every** such \(q\) there are \(6(q-1)/9\) equations with a rational bitangent but with **no symmetric linear determinantal representation over extensions of degrees less than nine**. The order-nine obstruction is thus geometrically realized, not merely a possible abstract symplectic permutation action.

For each row, the finite étale zeta functions of the bitangent scheme and the Cayley-octad scheme follow exactly from the cycles. In the three rows respectively, their denominators are
\[
(1-T)^{28},\ (1-T)^{36};\qquad
(1-T)(1-T^3)^9,\ (1-T^3)^{12};\qquad
(1-T)(1-T^9)^3,\ (1-T^9)^4.
\]

## Assumptions and scope

The characteristic is at least five, because \(q\) is odd and \(q\equiv1\pmod9\). A primitive ninth root \(\zeta\in k\) exists. All curves are considered over \(k\), and all geometric theta characteristics are defined over a fixed algebraic closure. A rational bitangent means a Galois-stable geometric bitangent line; it need not have both tangency points individually rational. Every even theta characteristic of a smooth plane quartic is non-effective. An object is said to descend to \(\mathbb F_{q^n}\) precisely when it is fixed by the \(n\)-th power of arithmetic Frobenius.

## Proof

**1. Smoothness, automorphism, and geometric triviality.** Write the defining polynomial as \(F=Y^3Z-X^4+cXZ^3\). On the affine chart \(Z=1\), \(F_Y=3Y^2\); setting \(Y=0\) and \(F=0\) forces \(X=0\) or \(X^3=c\), at which \(F_X=c\) and \(F_X=-3c\), respectively. Both are nonzero. The sole point at infinity is \([0:1:0]\), with \(F_Z=1\). Thus \(C_c\) is smooth of genus three and nonhyperelliptic.

Define
\[
\alpha:[X:Y:Z]\longmapsto[\zeta^3X:\zeta Y:Z].
\]
It preserves \(C_c\) and has order nine. If \(t^9=c\), the diagonal map \([X:Y:Z]\mapsto[t^3X:t^4Y:Z]\) identifies \(C_1\) with \(C_c\) over the algebraic closure. Thus these are ninth-power twists of one fixed geometric curve; no classification of arbitrary quartics is claimed.

**2. The centralizer is exactly the ninth-order cyclic subgroup.** Let \(J=\operatorname{Jac}(C_1)\) and \(V=J[2](\overline{k})\), a six-dimensional symplectic vector space over \(\mathbb F_2\). The action of \(\alpha\) on \(V\) has order nine: automorphisms of a positive-genus curve act faithfully on its Jacobian, and the kernel of reduction from its integral two-adic Tate-module automorphisms to \(\operatorname{GL}(V)\) is pro-two, hence has no nontrivial element of odd order. Since \(\operatorname{ord}_9(2)=6\), an order-nine semisimple operator in dimension six has irreducible characteristic polynomial
\[
\Phi_9(U)=U^6+U^3+1.
\]
Identify \(V\) with \(\mathbb F_{64}\), so that \(\alpha\) acts as multiplication by a primitive ninth root \(a\in\mathbb F_{64}\). The centralizer in the full linear group consists of multiplications by \(b\in\mathbb F_{64}^{\times}\). The nondegenerate \(\alpha\)-invariant alternating Weil form is, up to a scalar, of the shape \(B(x,y)=\operatorname{Tr}_{\mathbb F_{64}/\mathbb F_2}(\beta xy^8)\), with \(\beta\in\mathbb F_8^\times\). Multiplication by \(b\) preserves it if and only if \(b^9=1\). Consequently
\[
C_{\operatorname{Sp}_6(\mathbb F_2)}(\alpha)=\langle\alpha\rangle\cong C_9.
\]
Frobenius on \(C_1\) commutes with \(\alpha\), because \(\zeta\in k\). Its action on \(V\) must therefore be \(\alpha^e\), for some \(e\in\mathbb Z/9\mathbb Z\). No knowledge of \(e\) is necessary for the global count.

**3. Ninth-power characters distribute Frobenius uniformly.** For \(c=t^9\), transport Frobenius from \(C_c\) to \(C_1\) using the diagonal isomorphism. Put \(t^{q-1}=c^{(q-1)/9}=\zeta^{j(c)}\). On affine coordinates, the transport multiplies \(X\) by \(\zeta^{3j(c)}\) and \(Y\) by \(\zeta^{4j(c)}\); this is exactly \(\alpha^{4j(c)}\). Thus the mod-two Frobenius on \(C_c\), after identification, is
\[
\rho_c=\alpha^{e+4j(c)}.
\]
The ninth-power character \(c\mapsto c^{(q-1)/9}\) maps \(k^\times\) surjectively onto \(\mu_9\), with \((q-1)/9\) preimages for each value. Multiplication by four permutes the exponents modulo nine. Hence the nine powers of \(\alpha\) occur equally often: one identity, two elements of order three, and six of order nine, each weighted by \((q-1)/9\).

**4. Odd and even theta cycles.** The \(64\) theta characteristics form an affine torsor under \(V\), split into \(28\) odd and \(36\) even. Since \(\alpha^3-I\) is invertible on \(V\) (all eigenvalues of \(\alpha^3\) have exact order three), its affine action on all theta characteristics has precisely one fixed point. That point is also \(\alpha\)-fixed, because \(\alpha\) commutes with \(\alpha^3\). It cannot be even: the stabilizer of an even theta characteristic is \(S_8\), which has no element of order nine. It is therefore the unique fixed odd theta characteristic, corresponding geometrically to the hyperflex bitangent \(Z=0\).

For any nonidentity order-three power of \(\alpha\), the remaining \(27\) odd theta characteristics form nine three-cycles and the \(36\) even ones form twelve three-cycles. For any order-nine power, the remaining \(27\) odd characteristics form three nine-cycles and the even ones four nine-cycles. The identity fixes all. These are precisely the claimed Frobenius cycles.

**5. Determinantal descent.** On a smooth nonhyperelliptic genus-three curve every even theta characteristic is ineffective. The symmetric linear determinantal correspondence identifies such a characteristic over a field of characteristic not two with a symmetric \(4\times4\) linear matrix representation of its canonical quartic. Over a finite field, vanishing of the Brauer group removes any obstruction to descending a Frobenius-stable geometric theta line bundle. Therefore the minimum extension degree for a symmetric linear determinant is the shortest Frobenius cycle on the \(36\) even characteristics, respectively \(1\), \(3\), or \(9\). Combining with step 3 proves the table and all finite étale zeta formulas.

## Verification

Two standalone checkers are included. The first, `verify_picard_theta.cpp`, builds \(\operatorname{Sp}_6(\mathbb F_2)\) from symplectic transvections, exhausts all \(1{,}451{,}520\) group elements, independently finds an order-nine matrix, checks that its symplectic centralizer has order nine, and computes the cycle partitions of all nine powers on \(28\) odd and \(36\) even theta characteristics. The second, `verify_picard_lines.cpp`, directly tests the binary-quartic restriction of every \(\mathbb F_{19}\)-line against the square-of-a-quadratic condition for each of the \(18\) coefficient-marked curves over \(\mathbb F_{19}\).

Run them from a directory containing the two source files:

```sh
g++ -std=c++17 -O2 verify_picard_theta.cpp -o theta_check && ./theta_check
g++ -std=c++17 -O2 verify_picard_lines.cpp -o lines_check && ./lines_check
```

The first finds odd cycles \(1^1 9^3\), even cycles \(9^4\), and centralizer order nine; its third and sixth powers have odd cycles \(1^1 3^9\), even cycles \(3^{12}\). The second identifies exactly two coefficients, \(c=4,15\), with \(28\) rational bitangents over \(\mathbb F_{19}\), and one rational bitangent for every other coefficient. Choosing \(\zeta=4\in\mathbb F_{19}\), this fixes the Frobenius shift and gives the complete illustrative degree distribution: \(d=1\) for \(c=4,15\), \(d=3\) for \(c=6,9,10,13\), and \(d=9\) for the other twelve coefficients. The infinite family theorem is proved by the preceding algebraic argument, not by these finite checks.

## Relationship to prior work

The geometric order-nine automorphism and its explicit bitangent configuration were studied by Liang. The order-nine action on geometric bitangents and the induced \(9\)-cycles on Cayley octads have also been recorded in earlier work; they are **not** claimed as new. Bergvall develops Cayley-octad markings and their \(S_8\) stabilizers, while Elsenhans–Jahnel treat Galois-invariant Cayley octads and Galois constructions over infinite fields. Earlier abstract symplectic cycle spectra also encompass the three permutation patterns appearing here.

The assessed addition is the **uniform coefficient-by-coefficient ninth-power twist classification for every odd finite field containing the ninth roots of unity**, including explicit existence and frequency of quartics with a rational hyperflex but no symmetric determinant until the ninth extension. Unlike the abstract cycle-spectrum statements, this specifies a concrete family and exhibits the sharp obstruction in every permitted field. The existence of an equivalent older arithmetic twist calculation cannot be excluded.

## Limitations

The result concerns precisely the coefficient-marked family displayed above; it does not count all isomorphism classes of plane quartics or classify twists outside this presentation. It does not assert that a canonical rational bitangent yields a rational Cayley octad. No explicit symmetric determinant matrix over the ninth extension is supplied: existence follows from the theta correspondence. The checkers independently test the finite group combinatorics and one sample field, not every field. Independent external mathematical validation has not been performed.

## References

- A.-S. Elsenhans and J. Jahnel, *On plane quartics with a Galois invariant Cayley octad*, arXiv:1710.07279 (first publicly posted 19 October 2017), https://arxiv.org/abs/1710.07279.
- O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, arXiv:2106.13072 (first publicly posted 24 June 2021), https://arxiv.org/abs/2106.13072.
- D. Liang, *Invariants, bitangents, and matrix representations of plane quartics with 3-cyclic automorphisms*, New York J. Math. 26 (2020), 636–655, https://nyjm.albany.edu/j/2020/26-29v.pdf.
- Y. Ishitsuka and T. Ito, *The local-global principle for symmetric determinantal representations of smooth plane curves*, arXiv:1412.8336 (background theorem on theta characteristics and symmetric determinants), https://arxiv.org/abs/1412.8336.
- ATLAS of Finite Group Representations, the \(36\)-point \(\operatorname{Sp}_6(2)\) action, https://brauer.maths.qmul.ac.uk/Atlas/v3/permrep/S62G1-p36B0.
