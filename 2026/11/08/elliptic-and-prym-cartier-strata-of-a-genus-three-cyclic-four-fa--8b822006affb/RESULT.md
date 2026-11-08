# Elliptic and Prym Cartier strata of a genus-three cyclic-four family in characteristics seven and eleven

## Finding
Let \(p\in\{7,11\}\), let \(k=\overline{\mathbb F}_p\), and let \(c\in k\) satisfy \(c^2\ne4\). Denote by \(C_c\) the smooth projective completion of
\[
 C_c:\qquad z^2=w^8+c w^4+1.
\]
It is a genus-three hyperelliptic curve and a cyclic degree-four cover of \(\mathbb P^1\), equivalently birational to the inertia-\((1,1,3,3)\) cover \(y^4=x(x-1)(x-t)^3\) with \(t=(2-c)/4\). The involution \((w,z)\mapsto(-w,z)\) has elliptic quotient \(E_c:z^2=u^4+c u^2+1\); its connected Prym \(P_c\) has dimension two.

Let \(f_p\) be geometric \(p\)-rank and \(a\) the Cartier \(a\)-number. The following tables completely determine the arithmetic invariants of the Jacobian, the elliptic quotient, and the Prym at **every** smooth geometric coefficient parameter. Pairs in cells are \((f_p,a)\).

For \(p=7\):

| Parameter condition | \(J(C_c)\) | \(J(E_c)\) | \(P_c\) |
| --- | --- | --- | --- |
| \(c=0\) | \((0,3)\) | \((0,1)\) | \((0,2)\) |
| \(c^2=1\) | \((2,1)\) | \((0,1)\) | \((2,0)\) |
| \(c(c^2-1)\ne0\) | \((3,0)\) | \((1,0)\) | \((2,0)\) |

For \(p=11\):

| Parameter condition | \(J(C_c)\) | \(J(E_c)\) | \(P_c\) |
| --- | --- | --- | --- |
| \(c^2=5\) | \((1,2)\) | \((1,0)\) | \((0,2)\) |
| \(c(c^2-3)(c^2+1)=0\) | \((2,1)\) | \((0,1)\) | \((2,0)\) |
| Otherwise | \((3,0)\) | \((1,0)\) | \((2,0)\) |

All conditions are understood on the open parameter line \(c^2\ne4\); no listed exceptional points lie on that boundary. An abelian surface has \(a=2\) exactly when it is superspecial, so the Prym is superspecial exactly at \(c=0\) for \(p=7\) and at the two roots of \(c^2=5\) for \(p=11\). In characteristic eleven, the quotient is ordinary at both superspecial-Prym points, and the elliptic and Prym nonordinary loci are disjoint. In characteristic seven their nonordinary loci meet at \(c=0\), where the entire genus-three Jacobian is superspecial. The last observation for \(c=0\) alone is already encompassed by known superspecial-curve results, not claimed as independently new.

More precisely the Hasse determinant on this affine parameter line is a nonzero scalar times
\[
 \begin{cases}
 c^3(c^2-1),&p=7,\\
 c(c^2-3)(c^2+1)(c^2-5)^2,&p=11.
 \end{cases}
\]
Thus the nonordinary Cartier-divisor has multiplicities \(3,1,1\) in characteristic seven and multiplicities \(2,2,1,1,1,1,1\) in characteristic eleven. The locus of Cartier rank zero in characteristic seven has reduced defining ideal \((c)\), and the locus of Cartier rank at most one in characteristic eleven has reduced defining ideal \((c^2-5)\) on the smooth parameter line; by contrast the rank-at-most-two scheme is the generally nonreduced Hasse divisor itself. These are multiplicities in the stated coefficient-line trivialization; they are **not** asserted as moduli-stack intersection multiplicities.

## Assumptions and scope
Every geometric coefficient \(c\in k\) satisfying \(c^2\ne4\) is included. The field is algebraically closed, \(p=7\) or \(p=11\), and no claim is made about other primes. The smooth projective completion, not the affine plane model by itself, is meant. The quantities \(f_p\) and \(a\) are invariants of the indicated abelian varieties over \(k\); the number of coefficient parameters is not a count of geometric isomorphism classes. The Hasse divisor is calculated on the affine parameter base \(\operatorname{Spec}k[c,(c^2-4)^{-1}]\).

## Proof
**Geometry and cyclic-cover identification.** Set \(h_c(w)=w^8+c w^4+1\). In odd characteristic, \(h_c'(w)=4w^3(2w^4+c)\). Since \(h_c(0)=1\), a common root of \(h_c\) and \(h'_c\) must satisfy \(w^4=-c/2\), and then \(h_c(w)=1-c^2/4\). Thus \(h_c\) is squarefree precisely when \(c^2\ne4\). A degree-eight squarefree hyperelliptic polynomial defines a smooth genus-three completion. The relation \(y^4=x(x-1)(x-t)^3\), upon setting \(w=y/(x-t)\), becomes \(x^2-(1+w^4)x+t w^4=0\); its quadratic discriminant is \(w^8+(2-4t)w^4+1\). Hence setting \(c=2-4t\) gives the stated birational equivalence. The map \((w,z)\mapsto(u=w^2,z)\) is a degree-two quotient to a smooth genus-one quartic with a rational point \((u,z)=(0,1)\). The involution fixes the two points over \(w=0\) and the two points at infinity, consistently giving four branch points and an elliptic quotient. Its Prym has dimension \(3-1=2\).

**Cartier matrix.** The regular differentials \(dw/z,w\,dw/z,w^2\,dw/z\) are a basis. For \(h_c(w)^{(p-1)/2}=\sum_n b_n(c)w^n\), the modified Cartier (or dual Hasse--Witt) matrix has entry \(b_{pi-j}(c)\), for \(1\le i,j\le3\). Only exponents divisible by four occur in this power. Direct multinomial extraction, with coefficients read modulo \(p\), gives
\[
 M_7(c)=\begin{pmatrix}0&0&3c\\0&c(c^2-1)&0\\3c&0&0\end{pmatrix},
 \qquad
 M_{11}(c)=\begin{pmatrix}0&0&5-c^2\\0&c(c^2-3)(c^2+1)&0\\5-c^2&0&0\end{pmatrix}.
\]
For example, each coefficient is the finite sum
\[
 b_n(c)=\sum_{\substack{a,b\ge0\\a+b\le m\\8a+4b=n}}
 \frac{m!}{a!\,b!\,(m-a-b)!}\,c^b\quad(\bmod p),\qquad m=(p-1)/2.
\]
This formula supplies a reproducible exact certificate for every displayed entry and for the vanishing of every unlisted one.

**Rank and semilinear stability.** Both matrices have shape \(\bigl(\begin{smallmatrix}0&0&A\\0&B&0\\A&0&0\end{smallmatrix}\bigr)\). The first and third basis vectors form a Cartier-stable two-dimensional subspace on which the operator, when \(A\ne0\), is an invertible semilinear map; when \(A=0\), its Cartier action is identically zero. The middle basis vector has an invertible one-dimensional semilinear action precisely when \(B\ne0\). Therefore **every iterate** preserves the same stable rank, namely \(2\mathbf1_{A\ne0}+\mathbf1_{B\ne0}\). The geometric \(p\)-rank equals that stable rank, while the Cartier \(a\)-number is \(3-(2\mathbf1_{A\ne0}+\mathbf1_{B\ne0})\). Substitution gives the Jacobian entries in both tables. The roots of \(A\) and \(B\) are disjoint in characteristic eleven: \(c^2=5\) implies \(c(c^2-3)(c^2+1)=12c=c\ne0\). In characteristic seven their unique common root is \(c=0\). The other claimed roots are simple because the factors in each polynomial are squarefree and mutually coprime, with nonzero scalar derivatives at their roots.

**Elliptic and Prym factors.** The quotient involution acts by \((-1,+1,-1)\) on the displayed differential basis, so the middle one-form \(w\,dw/z\) is the pullback, up to a factor \(2\), of \(du/z\) on \(E_c\). The elliptic Cartier scalar is therefore \(B(c)\), and its \(p\)-rank and \(a\)-number are \((\mathbf1_{B\ne0},\mathbf1_{B=0})\). For a separable degree-two cover in odd characteristic, the pullback/norm decomposition gives an isogeny \(J(E_c)\times P_c\to J(C_c)\) of degree a power of two, hence prime to \(p\). It identifies the respective \(p\)-divisible groups, making both \(p\)-rank and \(a\)-number additive. Subtracting the elliptic invariants from those of \(J(C_c)\) gives the Prym entries. In dimension two the equality \(a(P_c)=2\) characterizes superspeciality. This proves the stated elliptic--Prym separation.

**Divisors and boundary.** The determinant of each matrix is \(-A(c)^2B(c)\). In characteristic seven it is a unit times \(c^3(c^2-1)\); in characteristic eleven it is a unit times \((c^2-5)^2 c(c^2-3)(c^2+1)\). The roots have the asserted multiplicities. For rank zero at \(p=7\), the ideal of all matrix entries is \((c,c(c^2-1))=(c)\). For rank at most one at \(p=11\), the ideal of all \(2\)-minors is \((A^2,AB)=A(A,B)=(A)=(c^2-5)\), since \(A\) and \(B\) are coprime. In contrast, the rank-at-most-two scheme has ideal \((\det M)\), with nonreduced structure at the higher-multiplicity points. None satisfies \(c^2=4\), so all belong to the smooth family. In characteristic eleven the five roots of \(B\) are \(c=0\), the two roots of \(c^2=3\), and the two roots of \(c^2=-1\). Thus the list is exhaustive even over the algebraic closure.

## Verification
The self-contained standard-library programs `verify_multinomial.py` and `verify_extension.py` provide two mathematically different finite checks. Run `python3 verify_multinomial.py` to reconstruct each Cartier entry from integer multinomial coefficients reduced modulo the prime. Run `python3 verify_extension.py` to expand powers directly over quadratic extension fields using polynomial convolution and check all non-singular coefficient parameters, including roots invisible over the prime field. The latter also computes matrix ranks by explicit minors. Expected finite-extension rank histograms are \((\text{rank }0:1,\text{rank }2:2,\text{rank }3:44)\) over \(\mathbb F_{49}\), and \((\text{rank }1:2,\text{rank }2:5,\text{rank }3:112)\) over \(\mathbb F_{121}\). Each extension field contains all exceptional roots; the universality of the classification nevertheless follows from the displayed factored matrix identities, not from finite enumeration alone.

## Relationship to prior work
Cavalieri and Pries (arXiv:2308.14891, first public 2023-08-28) study Hasse divisors and weighted nonordinary mass in one-dimensional cyclic-cover families. Their Section 6 covers general four-branch cyclic mass formulae, but it does not state the present parameterwise Cartier/Prym table. Their Section 7 applies to \(d\ge3\) **odd**, and therefore does not cover this \(d=4\) case, despite using the analogous hyperelliptic normalization for odd degrees. Moriya and Kudo (arXiv:2209.02926, first public 2022-09-07) give general decomposed Richelot methods and superspecial genus-three algorithms, not this characteristic-seven/eleven stratification. Ohashi and collaborators (arXiv:2401.10500, first public 2024-01-19), Theorem 4.3(3), already record the known criterion for \(y^2=x^8-1\) to be superspecial; over the algebraic closure that curve is equivalent to the single point \(c=0\) here in characteristic seven. That *individual* superspeciality claim is expressly not claimed as novel. Frei (arXiv:1703.03516) provides general bounds on large hyperelliptic \(a\)-numbers, not this exact parameterwise genus-three classification. A 2020 paper by Boix--Noordman--Top on levels of polynomial pairs discusses the special trinomial at the exceptional coefficient, but no accessible material inspected provided this complete family stratification. The potential for an older equivalent calculation in another parameterization remains a residual priority risk.

## Limitations
These are exact invariants only for the displayed smooth one-parameter family and the primes \(7\) and \(11\). Other primes, complete Newton polygons, isomorphism-class counts, geometric moduli intersection multiplicities, and full Hasse--Weil zeta functions are not classified. Although the Prym surface is superspecial when its Cartier \(a\)-number is two, the genus-three Jacobian is not claimed to have any additional isogeny decomposition beyond the stated prime-to-characteristic elliptic/Prym isogeny. All finite checks are verification aids to the algebraic proof; they cannot establish historical priority. An independent mathematical audit has not been performed.

## References
1. R. Cavalieri and R. Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (first public 2023-08-28). https://arxiv.org/abs/2308.14891
2. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926 (first public 2022-09-07). https://arxiv.org/abs/2209.02926
3. R. Ohashi, H. Onuki, M. Kudo, R. Yoshizumi and K. Nuida, *Listing superspecial curves of genus three by using Richelot isogeny graph*, arXiv:2401.10500 (first public 2024-01-19). https://arxiv.org/abs/2401.10500
4. S. Frei, *The a-number of hyperelliptic curves*, arXiv:1703.03516 (first public 2017-03-10). https://arxiv.org/abs/1703.03516
5. A. F. Boix, M. P. Noordman and J. Top, *The level of pairs of polynomials*, Communications in Algebra 48 (2020), 4235--4248. https://doi.org/10.1080/00927872.2020.1759614
