# Frobenius point counts and zeta functions of the Komiya–Kuribayashi bitangent divisor

## Finding
Let \(p\ge7\) be prime, let \(q=p^m\) with \(m\ge1\), and let \(D_p\subset\mathbb P^2_{\mathbb F_p}\) be the reduced union of the 28 geometric bitangents to the smooth plane quartic
\[
 C_p:\quad X^4+Y^4+Z^4+3(X^2Y^2+X^2Z^2+Y^2Z^2)=0.
\]
This divisor is defined over \(\mathbb F_p\), although its component lines need not be. Define
\[
 c_p=\begin{cases}299,&p\in\{7,29,41,101\},\\311,&p\in\{13,61,109\},\\323,&\text{otherwise},\end{cases}
\]
and write \(\chi_p\) for the Legendre symbol. Define the integer pairs \((\ell_p,b_p)\) by
\[
(\ell_p,b_p)=\begin{cases}
 (4,1),&\chi_p(-1)=-1,\\
 (16,-71),&p=13,\\
 (16,-83),&\chi_p(-1)=1,\ \chi_p(5)=-1,\ p\ne13,\\
 (28,-c_p),&\chi_p(-1)=\chi_p(5)=1.
\end{cases}
\]
Then the **complete finite-extension point count** is
\[
 \boxed{\#D_p(\mathbb F_{p^m})=\begin{cases}
 \ell_p p^m+b_p,&m\ \text{odd},\\
 28p^m-c_p,&m\ \text{even}.
 \end{cases}}
\]
In particular, the Hasse–Weil zeta function of this reduced, generally reducible projective curve is
\[
\boxed{Z(D_p,T)=\frac{(1-T)^{(c_p-b_p)/2}(1+T)^{(c_p+b_p)/2}}{(1-pT)^{(28+\ell_p)/2}(1+pT)^{(28-\ell_p)/2}}.}
\]
All exponents are nonnegative integers. An illustrative arithmetic phenomenon occurs at \(p=7\): the geometric line-intersection arrangement acquires 24 triple points while the ground-field point count stays \(\#D_7(\mathbb F_7)=4\cdot7+1=29\), the same form as nonsplit generic primes. The jump becomes visible over its quadratic extension, where \(\#D_7(\mathbb F_{49})=28\cdot49-299\).

The geometric intersection-multiplicity distributions \((n_2,n_3,n_4)\) behind this formula are exactly

| Prime conditions | \(n_2\) | \(n_3\) | \(n_4\) |
| --- | ---: | ---: | ---: |
| \(p\in\{7,29,41,101\}\) | 252 | 24 | 9 |
| \(p\in\{13,61,109\}\) | 288 | 12 | 9 |
| All other \(p\ge7\) | 324 | 0 | 9 |

Every intersection point is defined over \(\mathbb F_{p^2}\). No two bitangent components coalesce for any \(p\ge7\).

## Assumptions and scope
All assertions concern the displayed integral quartic, the **reduced union of its geometric bitangent lines**, and the prime field of characteristic \(p\ge7\) together with all its finite extensions. Geometric bitangents include fourth-order-contact (hyperflex) lines; they are counted as single irreducible components. This is **not** a point count of the smooth quartic itself, nor of the tangency-point scheme. Only residue characteristics at least seven are asserted; characteristic five is excluded because this quartic degenerates. The component and intersection support are finite étale as reduced geometric point sets, but their incidence scheme changes at the seven specified primes.

## Proof
**1. Exact lines and good reduction.** Work in the biquadratic number field \(K=\mathbb Q(i,r)\), with \(i^2=-1\) and \(r^2=5\). The 28 explicit coefficient triples in `kkcore.py` are integer-scaled versions of the twenty-eight bitangent equations of Janasz–Pokora–Zieliński, Table 8, with line indices retained. An independent symbolic check (`verify_bitangents.py`) substitutes every line in the quartic and factors its restricted binary quartic as the square of a quadratic up to a scalar. Its coefficients have only powers of two and five as potential denominators, so these identities remain bitangencies over algebraic closures of every characteristic \(p\ge7\).

For \(p\ge7\), the quartic is smooth: if exactly two projective coordinates are nonzero, the equations from partial derivatives have nonzero determinant \(4^2-6^2=-20\); with three nonzero coordinates the linear system in their squares has eigenvalues \(16,-2,-2\), also invertible; one nonzero coordinate is impossible. The 28 line equations remain pairwise distinct: the finite determinant enumeration below yields no proportional pair at any such prime. The classical 28 odd-theta-characteristic theorem therefore shows these are all geometric bitangents.

**2. All primes and all geometric intersection points.** For each unordered triple of coefficient vectors \(v_a,v_b,v_c\in K^3\), calculate its determinant \(\Delta_{abc}\). Exactly 36 of the 3276 determinants are identically zero; the others are nonzero algebraic integers. For \(u=A+Bi+Cr+Dir\in\mathbb Z[i,r]\), its absolute field norm is
\[
N_{K/\mathbb Q}(u)=\bigl(A^2-B^2-5(C^2-D^2)\bigr)^2+4(AB-5CD)^2.
\]
Exact factorization of the 3240 nonzero determinant norms shows that the **complete union of their rational prime divisors** is
\[
\{2,3,5,7,13,29,41,61,101,109\}.
\]
Thus no new triple concurrence is possible outside the seven listed primes in characteristic at least seven. For each of those seven primes, reduce \(i,r\) in the explicitly constructed field \(\mathbb F_{p^2}\) and, for every pair of distinct lines, gather precisely the lines whose triple determinant with that pair vanishes. This creates one incidence set for each distinct geometric crossing point. An exhaustive exact finite calculation gives the three rows of the displayed \((n_2,n_3,n_4)\) table and confirms that their maximum multiplicity is four. In every row, \(n_2+3n_3+6n_4=378=\binom{28}{2}\). The generic row is already known over the complex numbers; the reductions are computed independently, not inferred by lifting complex point counts.

**3. Frobenius on components and crossings.** Frobenius acts on the field coefficients by the two sign choices \(i\mapsto\chi_p(-1)i\) and \(r\mapsto\chi_p(5)r\). Applying these signs to each of the 28 coefficient triples induces a well-defined permutation of the 28 lines. Each geometric crossing is identified by its **full incident-line subset**, so Frobenius acts by permuting the indices in that subset. In all characteristics considered, this action has order at most two. The exact fixed-crossing distributions and fixed-component counts are:

| Regime | Fixed lines | Fixed double | Fixed triple | Fixed quadruple |
| --- | ---: | ---: | ---: | ---: |
| Generic, \(\chi_p(-1)=-1\) | 4 | 0 | 0 | 9 |
| Generic, \((\chi_p(-1),\chi_p(5))=(1,-1)\) | 16 | 84 | 0 | 9 |
| Generic, \((\chi_p(-1),\chi_p(5))=(1,1)\) | 28 | 324 | 0 | 9 |
| \(p=7\) | 4 | 0 | 0 | 9 |
| \(p=13\) | 16 | 48 | 12 | 9 |
| \(p\in\{29,41,101\}\) | 28 | 252 | 24 | 9 |
| \(p\in\{61,109\}\) | 28 | 288 | 12 | 9 |

For generic primes, the fixed-incidence results depend only on the two signs: the determinant-norm sieve ensures that the crossing support and all incident-line labels are unchanged after reduction. The four generic sign cases were independently sampled in exact finite fields with prime representatives \(11,17,23,89\), and the explicit sign permutations exhaust the four possibilities. All seven exceptional primes were directly enumerated with the same exact field construction.

**4. Rational points and zeta.** At a rational crossing \(P\), let \(s_P\) be the number of rational component lines passing through it. A rational point of the union either lies on a rational line or is a crossing of conjugate nonrational lines. Hence the exact inclusion–exclusion identity is
\[
\#D_p(\mathbb F_p)=\ell_p(p+1)+\sum_{P\text{ Frobenius-fixed}}(1-s_P).
\]
For either generic nonsplit regime with four rational lines, the nine rational quadruple crossings comprise six meeting two rational lines and three meeting none. The correction is \(-3\), giving \(4p+1\); the same calculation holds at \(p=7\). In the generic regime with 16 rational lines, 84 rational nodes each meet two rational lines and the nine rational quadruples comprise six meeting four rational lines and three meeting none. The correction is \(-99\), giving \(16p-83\). At \(p=13\), there are instead 48 fixed nodes and 12 fixed triple points, all meeting respectively two and three rational lines, and the same six-plus-three quadruple distribution; the correction is \(-87\), giving \(16p-71\).

When all 28 lines split, every intersection point is rational and inclusion–exclusion yields
\[
 \#D_p(\mathbb F_p)=28(p+1)-(n_2+2n_3+3n_4)=28p-c_p.
\]
Over every even extension degree all 28 lines and crossings split, giving \(28p^m-c_p\). For odd extension degrees the original Frobenius permutations persist, and the ground-field correction applies with \(p\) replaced by \(p^m\). This proves the complete point-count formula. Finally, the logarithmic definition \(Z(D_p,T)=\exp(\sum_{m\ge1}\#D_p(\mathbb F_{p^m})T^m/m)\), separated into even and odd terms, gives the displayed rational zeta function and integer exponents.

## Verification
Run `python verify.py` with Python 3 and SymPy (used for exact integer factorization), accompanied by `kkcore.py` in the same directory. The computation checks 3276 triple determinants, their complete prime-factor support, all seven exceptional primes, one representative of each generic Frobenius-sign case, and every incidence/Frobenius correction in the table; the final marker is `KK_BITANGENT_ZETA_ALL_PRIME_CLASSES_OK`. Run `python verify_bitangents.py` for independent symbolic square-restriction checks of all 28 lines. Run `python verify_direct.py` for a separate direct enumeration of rational points on the union in projective planes over seven prime fields; this returns counts \(29,45,137,189,513,509,2169\) at primes \(7,11,13,17,29,37,89\), matching the formula. These are *exact finite calculations* with a proved reduction to finitely many cases; numerical tests alone are not used as infinite-prime proofs.

## Relationship to prior work
Plaumann–Sturmfels–Vinzant (first arXiv version dated 2010-08-24) study the 28-bitangent structure and exact symbolic computation for smooth quartics. Janasz–Pokora–Zieliński (2023) give precisely the Komiya–Kuribayashi 28-line equations and the **complex** intersection profile \((324,0,9)\), explicitly limiting their paper to characteristic zero. Previously published work on the Ciani pencil gives a full *complex* triple-concurrence discriminant, including the parameter factors which specialize at the coefficient \(\lambda=3\) to the seven primes here. Thus **the prime list as a naked substitution is not claimed to be an independent new discovery**. Published results also classify the 4/16/28 finite-field rational-bitangent counts for the Ciani pencil and the biquadratic splitting cover. Neither supplies the rational-intersection incidence corrections, the exceptional arithmetic crossing strata, or the full extension-field point counts/zeta of the **28-line union** at this quartic. These distinctions concern statement implication, not merely differing titles. A result for Fermat-quartic bitangent divisors treats a different member of the Ciani pencil; its formula does not imply the present counts. Detailed comparisons and residual priority risk are in `AUDIT.json` and `REVIEW.md`.

## Limitations
The result treats one integral plane quartic and its 28-line union, not the full Ciani pencil, its smooth-curve zeta function, the branch/tangency scheme, or characteristics below seven. It does not determine integral generalized-Jacobian character lattices or all analytic types of singularities of the union. Finite calculations are reproducible but have not been independently audited. The originality assessment is provisional, especially against any unindexed geometric-arithmetic treatments of this exact bitangent divisor.

## References
1. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104, first posted 2010-08-24, https://arxiv.org/abs/1008.4104.
2. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first posted 2023-08-31, §3.3 and Tables 8–10, https://arxiv.org/abs/2308.16514.
3. A. Kuribayashi, K. Komiya, *On Weierstrass points and automorphisms of curves of genus three*, Lecture Notes in Mathematics 732 (1979), 253–299, cited by reference 2.
4. Published mathematical record, *Triple-concurrence discriminant of the Ciani quartic bitangents*, 2026-10-25, exact universal complex parameter factors (identified in `AUDIT.json`).
5. Published mathematical records, *Biquadratic bitangent splitting cover and arithmetic profiles of the Ciani pencil* (2026-10-12) and *Quadratic splitting and three rational-bitangent strata in the Ciani quartic pencil* (2026-11-08), finite-field line rationality but not point counts on their union.
