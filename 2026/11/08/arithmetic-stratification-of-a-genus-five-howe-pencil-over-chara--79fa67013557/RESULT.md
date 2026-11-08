# Arithmetic stratification of a genus-five Howe pencil over characteristic seven

## Finding
Let \(k=\overline{\mathbb F}_7\), let \(a\in k\setminus\{0,1\}\), and let \(C_a\) be the smooth projective normalization of the fiber product
\[
 y^2=x^4-1,\qquad z^2=x^4-a.
\]
It is a geometrically integral, non-hyperelliptic genus-five curve. The geometric Jacobian's \(7\)-rank \(f\) and Cartier \(a\)-number \(\alpha\) are exactly
\[
(f,\alpha)=\begin{cases}
 (0,5)&a=-1,\\
 (2,3)&a\in\{2,4\},\\
 (3,2)&a\notin\{0,1,-1,2,4\}.
 \end{cases}
\]
In particular, the pencil has exactly one superspecial coefficient parameter, \(a=-1\), over the algebraic closure.

For the five admissible parameters in \(\mathbb F_7\), write \(L_a(T)\) for the Hasse--Weil numerator of \(C_a/\mathbb F_7\). Define
\[
 U=1+7T^2,\qquad V_-=1-4T+7T^2,\qquad
 V_+=1+4T+7T^2,\qquad B=1+6T^2+49T^4.
\]
Their **complete zeta numerator classification** is

| \(a\) | \(L_a(T)\) | \(\#C_a(\mathbb F_7)\) | \(\#C_a(\mathbb F_{49})\) |
| --- | --- | ---: | ---: |
| \(2\) or \(4\) | \(U^3V_-V_+\) | 8 | 88 |
| \(3\) | \(U^2V_-B\) | 4 | 88 |
| \(5\) | \(U^2V_+B\) | 12 | 88 |
| \(6=-1\) | \(U^5\) | 8 | 120 |

Consequently \(C_6\) is maximal over \(\mathbb F_{49}\), attaining the genus-five Weil upper bound \(49+1+10\cdot7=120\); it is the only maximal member among these five rational parameters.

## Assumptions and scope
All geometric rank statements are over the algebraic closure in characteristic seven. The zeta statements concern precisely the five \(\mathbb F_7\)-rational parameters \(a\in\{2,3,4,5,6\}\), with the displayed coefficient-defined models; no assertion is made for other coefficient fields or for distinct curve isomorphism classes. The normalization is essential to the complete curve, although the affine fiber product is smooth for these parameters.

## Proof
**Genus and elliptic quotients.** The two quartics have four distinct zeros apiece, and their geometric branch divisors are disjoint when \(a\ne0,1\). Their quadratic function-field extensions are independent. The degree-four map from the normalization to \(\mathbb P^1\) is ramified at eight geometric base points, with two points above each and ramification index two. Riemann--Hurwitz gives \(2g-2=-8+16=8\), hence \(g=5\). The standard branch-intersection criterion for generalized Howe curves yields non-hyperellipticity, as the number of shared branch points is zero. The Klein-four quotient isogeny, of degree a power of two, is
\[
 J(C_a)\longrightarrow E_1\times E_{2,a}\times J(D_a),\quad
 E_1:y^2=x^4-1,\quad E_{2,a}:z^2=x^4-a,\quad
 D_a:w^2=(x^4-1)(x^4-a).
\]
The elliptic curves both have geometric \(j\)-invariant \(1728\): the second is a fourth-root coordinate rescaling of the first over \(k\). In characteristic seven they are supersingular (and each has \((7\text{-rank},a\text{-number})=(0,1)\)). Since the isogeny is prime to seven, the \(7\)-rank and the Cartier \(a\)-number are additive under this decomposition.

**Exact Cartier computation.** The hyperelliptic genus-three quotient \(D_a\) has squarefree monic octic \(F_a(x)=(x^4-1)(x^4-a)\). In the differential basis \(dx/w,x\,dx/w,x^2\,dx/w\), the Cartier--Manin (or transposed Hasse--Witt) coefficient matrix is \(M_{ij}=[x^{7i-j}]F_a(x)^3\) for \(1\le i,j\le3\); whether transposed does not affect its rank or its nonzero-pattern cycles. Exact polynomial expansion in \(\mathbb F_7[a]\) gives
\[
 M_a=\begin{pmatrix}
 0&0&-3a^2(a+1)\\
 0&-(a-2)(a+1)(a+3)&0\\
 -3(a+1)&0&0
 \end{pmatrix}.
\]
For \(a\ne0,1\), the first and last off-diagonal entries vanish simultaneously, and only at \(a=-1\). The central entry vanishes exactly at \(a\in\{-1,2,4\}\). Every remaining nonzero one- or two-cycle stays invertible under semilinear Frobenius iteration, so the *stable* Frobenius rank equals \(\operatorname{rank}M_a\). Thus \(D_a\)'s \(7\)-rank is respectively \(0,2,3\) and its \(a\)-number respectively \(3,1,0\), in the three cases. Adding the two supersingular elliptic factors proves the geometric classification. An abelian variety of dimension five with \(a\)-number five is superspecial, proving the unique superspecial-parameter assertion.

**Zeta numerators.** For every extension \(K=\mathbb F_{7^n}\) and \(a\in\mathbb F_7\setminus\{0,1\}\), let \(\chi_K:K\to\{-1,0,1\}\) denote the quadratic character extended by zero. There are four \(K\)-rational points of \(C_a\) and two of \(D_a\) above infinity because both quartics are monic. Therefore
\[
 \#C_a(K)=4+\sum_{x\in K}(1+\chi_K(x^4-1))(1+\chi_K(x^4-a)),
\]
\[
 \#D_a(K)=2+\sum_{x\in K}\bigl(1+\chi_K((x^4-1)(x^4-a))\bigr).
\]
The exhaustive evaluations at extension degrees \(n=1,2,3\), independently repeated with two irreducible field presentations for \(n=2,3\), are

| \(a\) | \((\#D_a(\mathbb F_7),\#D_a(\mathbb F_{49}),\#D_a(\mathbb F_{343}))\) | \((\#C_a(\mathbb F_7),\#C_a(\mathbb F_{49}),\#C_a(\mathbb F_{343}))\) |
| --- | --- | --- |
| \(2\) | \((8,60,344)\) | \((8,88,344)\) |
| \(3\) | \((4,60,364)\) | \((4,88,364)\) |
| \(4\) | \((8,60,344)\) | \((8,88,344)\) |
| \(5\) | \((12,60,324)\) | \((12,88,324)\) |
| \(6\) | \((8,92,344)\) | \((8,120,344)\) |

Both elliptic factors have trace zero over \(\mathbb F_7\), because their \(j=1728\) curves are supersingular in characteristic seven and the integer trace is divisible by seven but has absolute value at most \(2\sqrt7<7\). Their common zeta factor is \(U\). For the genus-three quotient, writing \(s_n=7^n+1-\#D_a(\mathbb F_{7^n})\), Newton's identities give the first three coefficients of \(L_{D_a}(T)\): \(c_1=-s_1\), \(c_2=(s_1^2-s_2)/2\), and \(c_3=(-s_1^3+3s_1s_2-2s_3)/6\). The genus-three functional equation gives \(c_{6-j}=7^{3-j}c_j\) for \(j=0,1,2\). Substitution and exact factorization yield
\[
 \begin{aligned}
 L_{D_2}=L_{D_4}&=UV_-V_+,\\
 L_{D_3}&=V_-B,\\
 L_{D_5}&=V_+B,\\
 L_{D_6}&=U^3.
 \end{aligned}
\]
Multiplication by \(U^2\) proves the displayed classification. For \(a=6\), \(L_{C_6}=U^5\) implies \(\#C_6(\mathbb F_{49})=49+1+70=120\). The other four members have 88 points over that field, hence uniqueness within the rational parameter set.

## Verification
Execute `python verify_cartier.py` and `python verify_zeta.py` (Python 3, standard library only). The first independently expands \(F_a^3\), checks the three critical coefficient polynomials and all prime-field strata, including stable rank. The second exhaustively evaluates both quadratic-character formulas over \(\mathbb F_7\), \(\mathbb F_{49}\), and \(\mathbb F_{343}\), using two different irreducible binomials for each nonprime extension; it reconstructs the six-degree zeta numerators through Newton's identities and checks every factorization. These are finite exhaustive checks for the five rational parameters, while the geometric all-parameter classification follows from the symbolic coefficient factorizations.

## Relationship to prior work
Kudo's 2024 paper establishes plane-sextic models and geometric singularities for genus-five generalized Howe curves arising from two elliptic quartic covers with disjoint branch sets; the model, genus and quotient framework are prior art. Katsura--Takashima (2021) establish the general decomposed Richelot isogeny framework, and Moriya--Kudo (2022) give genus-three decomposition/arithmetic methods. Moriya--Kudo (2023) treat the complementary genus-two-pair plane sextic. Ohashi (2026) discusses previously reported superspecial genus-five constructions in characteristic seven and develops a different completely decomposable Jacobian approach in larger characteristics. These general results neither report the five exact zeta numerators of the displayed coefficient family nor its full geometric characteristic-seven rank stratification. The general isogeny, supersingularity of \(j=1728\) elliptic curves, and known existence of superspecial genus-five curves are not asserted as new.

## Limitations
The coefficient classification is not a classification of distinct isomorphism classes of curves. The zeta formulas cover only \(\mathbb F_7\)-rational parameters. No enumeration of all maximal genus-five curves or generalized Howe curves is claimed. Source retrieval and statement comparisons reduce but cannot eliminate the risk of older unindexed equivalent arithmetic computations. Independent mathematical audit has not been performed.

## References
1. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1 (first public 2024-01-01), especially Introduction, Sections 2--3 and concluding discussion.
2. T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993v1 (first public 2023-10-24).
3. T. Katsura and K. Takashima, *Decomposed Richelot isogenies of Jacobian varieties of hyperelliptic curves and generalized Howe curves*, arXiv:2108.06936 (first public 2021-08-16), especially Theorem 3.
4. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926 (first public 2022-09-07).
5. R. Ohashi, *Generalized Howe curves of genus 4, 5, and 6 with completely decomposable Jacobians*, arXiv:2604.18074 (first public 2026-04-20), especially Sections 2 and 4.
