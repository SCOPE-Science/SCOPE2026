# The first extra superspecial and maximal parameters in a genus-five Howe pencil

## Finding

Let \(k=\overline{\mathbb F}_p\), for a prime \(p\in\{7,23,31\}\). For every \(a\in k\setminus\{0,1\}\), let \(C_a\) be the smooth projective normalization of the fiber product of the two double covers of \(\mathbb P^1\)
\[
E_1:\ y^2=x^4-1,\qquad E_a:\ z^2=x^4-a.
\]
Each \(C_a\) is a geometrically connected Howe curve of genus five. Its Jacobian is superspecial exactly for the following *geometric coefficient parameters*:
\[
\begin{array}{c|c}p&\{a\in k\setminus\{0,1\}:J(C_a)\text{ superspecial}\}\\\hline
7&\{-1\}\\23&\{-1\}\\31&\{-1,14,20\}\end{array}.
\]
In particular, among the first three primes congruent to \(7\pmod8\), characteristic \(31\) is the first with superspecial members away from the canonical parameter \(a=-1\). In characteristic \(31\) the extra two parameters satisfy \(a^2-3a+1=0\), and are reciprocal.

For \(p=31\) and every \(a\in\mathbb F_{31}\setminus\{0,1\}\), the curve \(C_a\), with its displayed model over \(\mathbb F_{31}\), is **maximal over \(\mathbb F_{31^2}\)** if and only if \(a\in\{-1,14,20\}\). At precisely these three parameters,
\[
\#E_1(\mathbb F_{31^2})=\#E_a(\mathbb F_{31^2})=1024,\quad
\#H_a(\mathbb F_{31^2})=1148,\quad
\#C_a(\mathbb F_{31^2})=1272,
\]
where \(H_a:v^2=(x^4-1)(x^4-a)\) is the genus-three third quotient. The last count attains \(31^2+1+2\cdot5\cdot31=1272\).

Over \(\overline{\mathbb F}_{31}\), the two extra genus-three quotients \(H_{14}\) and \(H_{20}\) are isomorphic, but neither is isomorphic to \(H_{-1}\). The statement does not classify the genus-five curves up to geometric isomorphism: distinct coefficient parameters need not give distinct genus-five isomorphism classes.

## Assumptions and scope

All superspeciality assertions refer to geometric Jacobians over the algebraic closure and to the exact indicated primes. Superspeciality means that the abelian variety is isomorphic over the algebraic closure, as an unpolarized abelian variety, to a product of supersingular elliptic curves. The point-count and maximality assertions concern the **displayed** \(\mathbb F_{31}\)-models and their base changes to \(\mathbb F_{31^2}\). The parameter conditions \(a\ne0,1\) are essential for the two quartics to have eight distinct branch points in total.

## Proof

**Genus and quotient decomposition.** The covers \(E_1\to\mathbb P^1\) and \(E_a\to\mathbb P^1\) have disjoint sets of four simple branch points, provided \(a\notin\{0,1\}\). The two square classes are independent, so their fiber product is geometrically connected. Its normalization has a faithful Klein-four action. The degree-four map to \(\mathbb P^1\) has eight branch points, each with inertia of order two; Riemann–Hurwitz gives \(2g(C_a)-2=-8+8\cdot2=8\), hence \(g=5\). The three nontrivial quotient curves are \(E_1\), \(E_a\), and \(H_a\), of genera \(1,1,3\), respectively. The character idempotents of the Klein-four action yield an isogeny of degree a power of two
\[
J(C_a)\ \sim\ E_1\times E_a\times J(H_a).
\]
Thus the isogeny preserves the complete \(p\)-torsion group schemes for each of the odd characteristics under discussion and, in particular, preserves \(p\)-rank and Cartier \(a\)-number. Since \(p\equiv3\pmod4\), each elliptic quartic has zero Hasse invariant: \((x^4-b)^{(p-1)/2}\) has no term of degree \(p-1\). Therefore both elliptic factors are supersingular. Consequently, \(C_a\) is superspecial if and only if \(H_a\) is superspecial.

**Uniform symbolic criterion.** Write \(f_a(x)=(x^4-1)(x^4-a)\) and \(e=(p-1)/2\). In the regular-differential basis \(\{dx/v,x\,dx/v,x^2\,dx/v\}\), the Hasse–Witt matrix of \(H_a\) is given (up to the standard Frobenius-versus-Cartier convention) by the coefficients \(h_{ij}=[x^{pi-j}]f_a(x)^e\). Because \(p\equiv3\pmod4\), its only potentially nonzero entries are \((i,j)=(1,3),(2,2),(3,1)\). Put
\[
U_p(a)=[x^{p-3}]f_a^e,\quad V_p(a)=[x^{2p-2}]f_a^e,\quad W_p(a)=[x^{3p-1}]f_a^e.
\]
The genus-three Jacobian is superspecial if and only if its entire Cartier matrix vanishes, equivalently \(U_p=V_p=W_p=0\). The exact, monic polynomial greatest common divisors computed in \(\mathbb F_p[a]\) are
\[
\gcd(U_7,V_7,W_7)=a+1,\qquad
\gcd(U_{23},V_{23},W_{23})=a+1,
\]
\[
\gcd(U_{31},V_{31},W_{31})=(a+1)(a^2-3a+1).
\]
This is a statement over algebraic closures, not merely a check of parameters in the prime fields. The final quadratic has discriminant \(5\), with two roots \(14\) and \(20\) in \(\mathbb F_{31}\). All are admissible, and no other geometric roots exist. The standalone `verify_howe31.py` independently constructs the three coefficient polynomials by a binomial-convolution formula and by repeated multiplication in \(\mathbb F_p[a,u]\), with \(u=x^4\), and certifies the polynomial Euclidean algorithms.

**Maximality in the prime-field parameter pencil.** Represent \(\mathbb F_{31^2}=\mathbb F_{31}[u]/(u^2+1)\); this is a field since \(-1\) is a nonsquare in \(\mathbb F_{31}\). Let \(\chi\) be its quadratic character, with \(\chi(0)=0\). Both quartic covers are unramified above infinity and each has two rational points there; the fiber product has four. Hence direct fiber counting gives the exact identity
\[
\#C_a(\mathbb F_{31^2})=4+\sum_{x\in\mathbb F_{31^2}}
(1+\chi(x^4-1))(1+\chi(x^4-a)).
\]
The verifier `verify_maximal.py` enumerates **all 961 field elements** for each of the 29 admissible prime-field parameters and verifies the expression exactly. The Hasse–Weil upper bound of \(1272\) is attained at exactly \(a=14,20,30=-1\). Independently, at each parameter it also counts the two elliptic quotients and genus-three quotient and checks
\[
\#C_a=\#E_1+\#E_a+\#H_a-2(31^2+1).
\]
The three quotient counts are \(1024,1024,1148\), giving \(1272\). No statistical sampling or extrapolation is used.

**The two geometric quotient types.** The substitution \(x\mapsto1/x\) identifies \(H_a\) with \(H_{1/a}\) over the algebraic closure after a scalar change of the square-root coordinate; thus \(H_{14}\cong H_{20}\). To distinguish these from \(H_{-1}\), compare the branch sets \(B_a=\{x:x^4\in\{1,a\}\}\) of their hyperelliptic maps. All eight points of each set lie in \(\mathbb F_{31^2}\). Any geometric isomorphism of genus-three hyperelliptic curves descends to a projective-linear transformation of their branch sets; because three distinct branch points determine such a transformation, every candidate is already defined over \(\mathbb F_{31^2}\). The exact verifier `verify_branch.py` enumerates the 336 distinct ordered triples of target branch points, solves their projective-linear interpolation equations, and checks every image. It finds 16 projective automorphisms of \(B_{-1}\), eight of \(B_{14}\), and no transformation \(B_{-1}\to B_{14}\). Thus the two genus-three quotient curves are not geometrically isomorphic.

## Verification

Run `python3 verify_howe31.py`, `python3 verify_maximal.py`, and `python3 verify_branch.py` in the directory containing these files. They use only the Python standard library. Each prints a unique `HOWE31_..._PASS` marker after successful exact assertions. The first computes identities in polynomial rings, not samples. The second enumerates the full finite field and every admissible rational coefficient parameter. The third enumerates every possible branch-set projectivity by three-point interpolation.

## Relationship to prior work

Kudo's 2024 work establishes explicit plane sextic models for the genus-five Howe construction of two elliptic double covers with disjoint branch sets and proposes applications to superspecial classifications. Earlier Moriya–Kudo work studies explicit genus-three quotient arithmetic, while Ohashi's work concerns superspecial hyperelliptic genus-three Howe curves, including known maximality phenomena. A 2025 paper by Ohashi, Onuki, Kudo, Yoshizumi, and Nuida counts geometric superspecial genus-three hyperelliptic isomorphism classes for small primes. Ohashi's 2026 work proves the existence of superspecial genus-five Howe-type curves in many characteristics by different decomposable constructions. None of the inspected theorem statements and tables supplies the exact first-extra-parameter locus for the present elliptic–elliptic pencil, the complete \(\mathbb F_{31^2}\) maximality classification of its prime-field coefficients, or this specific two-type quotient comparison.

The familiar superspecial parameter \(a=-1\), and the characteristic-seven calculation, are background rather than independent claims of novelty. A 2024 conference poster credited to Kudo, Moriya and Ohashi, *Explicit plane sextic models for genus-five Howe curves and enumeration of superspecial ones*, is cited by later papers, but full poster content could not be inspected. It remains a concrete historical-priority risk, especially for the exact characteristic-31 parameter identities.

## Limitations

This theorem is a complete classification only in the three indicated characteristics and, for maximality, only for the 29 parameters lying in \(\mathbb F_{31}\). It does not classify all genus-five Howe curves, give a new existence theorem for superspecial genus-five curves in characteristic 31, or classify genus-five curves up to geometric isomorphism. It does not establish the full \(p\)-rank stratification outside the superspecial locus. Independent external mathematical review and a comprehensive historical-priority certification have not been performed.

## References

- M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760, first posted 2024-01-01, https://arxiv.org/abs/2401.00760.
- T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926, first posted 2022-09-07, https://arxiv.org/abs/2209.02926.
- R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152, first posted 2021-12-21, https://arxiv.org/abs/2112.11152.
- R. Ohashi, H. Onuki, M. Kudo, R. Yoshizumi and K. Nuida, *Listing superspecial curves of genus three using Richelot isogeny graphs*, arXiv:2401.10500, first posted 2024-01-19, https://arxiv.org/abs/2401.10500.
- R. Ohashi, *Generalized Howe curves of genus 4, 5, and 6 with completely decomposable Jacobians*, arXiv:2604.18074, first posted 2026-04-20, https://arxiv.org/abs/2604.18074.
