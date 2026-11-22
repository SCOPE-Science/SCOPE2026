# Zeta function, Picard rank ten, and height two for a binary space-filling K3 quartic

## Finding
Let \(X\subset\mathbb P^3_{\mathbb F_2}\) be the smooth quartic
\[
\begin{aligned}
0=F={}&X_0^3X_3+X_0^2X_1^2+X_0X_1^3+X_0X_3^3\\
&+X_1^2X_2^2+X_1X_2^3+X_2^2X_3^2+X_2X_3^3.
\end{aligned}
\]
Write \(Z(X,T)=\exp(\sum_{r\ge1}\#X(\mathbb F_{2^r})T^r/r)\). Then
\[
Z(X,T)=\frac{1}{(1-T)(1-4T)(1-2T)^6(1+4T^2)^2Q(T)},
\]
where the irreducible polynomial \(Q\in\mathbb Z[T]\) is
\[
\begin{aligned}
Q(T)={}&1+2T+2T^2+12T^3+32T^4+48T^5+96T^6\\
&+192T^7+512T^8+768T^9+512T^{10}\\
&+2048T^{11}+4096T^{12}.
\end{aligned}
\]
The geometric Picard number is \(\rho(X_{\overline{\mathbb F}_2})=10\), with
\(\rho(X_{\mathbb F_{2^r}})=6\) if \(4\nmid r\) and \(10\) if \(4\mid r\).
The formal Brauer group has height \(2\). The entire second crystalline Newton slope multiset is
\(\{(1/2)^2,1^{18},(3/2)^2\}\), with exponents indicating multiplicities.

## Assumptions and scope
The ground field is exactly \(\mathbb F_2\); all point counts are for the smooth projective surface \(X\), not its affine chart or a resolution of a singular model. This is the \(q=2\), \(b=1\) member of the companion-matrix construction in Bourgeois-Conti--Moon--Perez--Warren, Section 9: \(F=X_1\phi_{01}+X_2\phi_{12}+X_3\phi_{23}+(X_0+X_3)\phi_{30}\), with \(\phi_{ij}=X_i^2X_j-X_iX_j^2\). Their Lemma 9.2 proves geometric smoothness, and the Frobenius-vanishing presentation proves that \(X\) contains all \(15\) points of \(\mathbb P^3(\mathbb F_2)\). A smooth projective quartic in \(\mathbb P^3\) is a K3 surface.

## Proof
**1. Exact finite-field point count.** On \(X_3=1\), put \((x,y,z)=(X_0,X_1,X_2)\). Its equation is
\[
x^3+y^2x^2+(y^3+1)x+(y^2+1)z^2+yz^3+z=0.
\]
For every \(q=2^r\), define
\[
h_y(c)=\#\{x\in\mathbb F_q:x^3+y^2x^2+(y^3+1)x=c\}.
\]
Thus this chart contributes the **exhaustive finite sum**
\[
A_r=\sum_{y,z\in\mathbb F_q}h_y((y^2+1)z^2+yz^3+z).
\]
On the disjoint boundary \(X_3=0\), the chart \(X_2=1\) contributes the solutions of \(x^2y^2+xy^3+y^2+y=0\), and the remaining charts \(X_2=0,X_1=1\) and \(X_2=X_1=0,X_0=1\) contribute respectively \(2\) and \(1\). Hence
\[
\#X(\mathbb F_q)=A_r+\sum_{x,y\in\mathbb F_q}
\mathbf1_{x^2y^2+xy^3+y^2+y=0}+3.
\]
The attached standalone \(\texttt{verify_points.cpp}\) evaluates these *complete* sums, with no random sampling. It constructs each field by a polynomial basis and verifies that its chosen generator has multiplicative order \(2^r-1\), which simultaneously certifies that the quotient is a field. It tabulates the cubic values in \(O(q^2)\) field operations rather than scanning \(q^3\) triples. The exact outputs are:

| \(r\) | \(\#X(\mathbb F_{2^r})\) |
|---:|---:|
|1|15|
|2|25|
|3|81|
|4|377|
|5|1185|
|6|4273|
|7|17473|
|8|66849|
|9|266625|
|10|1052865|
|11|4207361|
|12|16821377|
|13|67169793|

The last two counts are redundant verification rather than input for polynomial reconstruction. A second verifier \(\texttt{verify_frobenius.py}\) independently evaluates the original homogeneous quartic at *every* normalized projective point over the five smallest fields, by a different bit-polynomial multiplication algorithm.

**2. Recovering the complete Frobenius polynomial.** By smooth quartic K3 cohomology, \(H^1=H^3=0\), \(\dim H^2=22\), and the trace formula says
\[
s_r:=\operatorname{Tr}(\operatorname{Frob}_2^r\mid H^2)=\#X(\mathbb F_{2^r})-1-2^{2r}.
\]
For \(P_2(T)=\det(1-T\operatorname{Frob}_2\mid H^2)=\sum_{i=0}^{22}a_iT^i\), Newton's identities \(ka_k=-\sum_{i=1}^k a_{k-i}s_i\) give
\[
(a_0,\ldots,a_{11})=(1,-10,46,-132,248,-224,-288,1408,-1920,-2048,16384,-43008).
\]
Poincare duality gives \(a_{22-i}=\epsilon 2^{22-2i}a_i\) for \(0\le i\le11\), where \(\epsilon\in\{\pm1\}\). Since \(a_{11}\ne0\), necessarily \(\epsilon=+1\), determining **all** coefficients. Exact integer multiplication then gives \(P_2(T)=(1-2T)^6(1+4T^2)^2Q(T)\). The resulting polynomial independently predicts the recorded counts for \(r=12,13\).

**3. Irreducibility and algebraic classes.** Set \(f(U)=U^{12}Q(1/U)\). Reducing \(f\) modulo \(13\), exact polynomial arithmetic certifies
\[
U^{13^{12}}\equiv U\pmod f,\quad
\gcd(f,U^{13^6}-U)=\gcd(f,U^{13^4}-U)=1
\]
in \(\mathbb F_{13}[U]\). By the finite-field irreducibility criterion for degree \(12\), \(f\) and \(Q\) are irreducible over \(\mathbb Q\). The coefficient of \(T^2\) in \(Q(T/2)\) is \(1/2\), so \(Q(T/2)\) is not cyclotomic. Irreducibility rules out every root of unity among its normalized reciprocal roots. The other normalized eigenvalues are six \(1\)'s and two each of \(+i\) and \(-i\). The Tate conjecture for K3 surfaces in characteristic two, proved by Kim--Madapusi Pera, identifies the dimensions of the algebraic Frobenius sectors, giving the stated geometric and extension-field Picard numbers.

**4. Formal Brauer height.** The valuations of coefficients of \(f(U)\), from leading to constant, are \((0,1,1,2,5,4,5,6,9,8,9,11,12)\). Their lower Newton polygon has successive slopes \(1/2\) twice, \(1\) eight times, \(3/2\) twice. The remaining ten second-cohomology roots all have slope \(1\). For a K3 surface of finite formal Brauer height \(h\), the extremal slopes are \(1-1/h\) and \(1+1/h\), each of multiplicity \(h\); therefore \(h=2\).

## Verification
Compile and run from the directory containing both attached source files:

```sh
g++ -O3 -std=c++17 verify_points.cpp -o verify_points
./verify_points > point_counts.txt
python3 verify_frobenius.py
```

The second script checks the thirteen point counts, independent direct evaluations for the first five fields, Newton identities, the full degree-22 polynomial, two redundant extension traces, irreducibility modulo \(13\), and the Newton slopes. Both files require only standard C++17 and Python 3; no proprietary computer algebra is used. The source files and the count table are embedded alongside this result.

## Relationship to prior work
Bourgeois-Conti, Moon, Perez and Warren prove existence and smoothness of the companion-matrix quartic (arXiv:2611.15768v1, Section 9); their treatment does not compute its zeta function or Picard group. The Tate and formal-Brauer interpretations use established theorems rather than new ones. Existing zeta computations for other characteristic-two quartic surfaces do not give this specific smooth companion-matrix model's degree-twelve transcendental factor.

## Limitations
This result treats **one explicit** quartic over \(\mathbb F_2\); it does not classify all space-filling quartic surfaces or determine the integral Neron--Severi intersection lattice. The computations prove the finite sums with executable exhaustive algorithms, not an independent formal proof of the implemented software. An equivalent historical presentation of this particular K3 surface under change of projective coordinates has not been ruled out exhaustively. Independent mathematical audit has not been performed.

## References
1. V. Bourgeois-Conti, H.-B. Moon, E. Perez, A. Warren, *Space-Filling Hypersurfaces*, arXiv:2611.15768v1 (first posted 2026-11-11), https://arxiv.org/html/2611.15768v1.
2. W. Kim and K. Madapusi Pera, *2-adic integral canonical models and the Tate conjecture in characteristic 2*, arXiv:1512.02540, https://arxiv.org/abs/1512.02540.
3. N. Nygaard and A. Ogus, *Tate's conjecture for K3 surfaces of finite height*, Annals of Mathematics 122 (1985), 461--507, https://annals.math.princeton.edu/1985/122-3/p01.
4. G. van der Geer and T. Katsura, *On a Stratification of the Moduli of K3 Surfaces*, arXiv:math/9910061, https://arxiv.org/abs/math/9910061.
