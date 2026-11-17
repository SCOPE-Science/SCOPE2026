# Tangent filling and blocking among smooth binary plane quartics

## Finding

Consider all nonzero homogeneous quartic equations \(F\in\mathbb F_2[X,Y,Z]_4\) whose plane curves \(C_F=V(F)\subset\mathbb P^2_{\mathbb F_2}\) are geometrically smooth. Define **tangent-filling** to mean that the union of the tangent lines \(T_Q C_F\), over \(Q\in C_F(\mathbb F_2)\), contains every point of \(\mathbb P^2(\mathbb F_2)\). Define **blocking** to mean that \(C_F(\mathbb F_2)\) intersects every \(\mathbb F_2\)-rational line.

**Theorem.** The exact joint distribution of these properties among geometrically smooth binary plane quartic equations is:

| Tangent-filling | Blocking | Equations | \(\operatorname{PGL}_3(\mathbb F_2)\)-classes |
| --- | --- | ---: | ---: |
| Yes | Yes | 2,040 | 14 |
| Yes | No | 616 | 6 |
| No | Yes | 1,848 | 11 |
| No | No | 6,416 | 47 |
| **Total** | | **10,920** | **78** |

In particular, precisely \(2,656\) smooth equations, forming \(20\) projective classes, are tangent-filling. For the uniform distribution on geometrically smooth quartic equations over \(\mathbb F_2\),

\[
\Pr(\text{tangent-filling}\mid\text{geometrically smooth})
=\frac{2656}{10920}=\frac{332}{1365}.
\]

Neither property implies the other. The exact distribution by number of rational points is:

| \(\#C_F(\mathbb F_2)\) | All smooth equations | Tangent-filling smooth equations |
| ---: | ---: | ---: |
| 0 | 165 | 0 |
| 1 | 1,008 | 0 |
| 2 | 2,646 | 0 |
| 3 | 3,360 | 364 |
| 4 | 2,541 | 1,260 |
| 5 | 1,008 | 840 |
| 6 | 168 | 168 |
| 7 | 24 | 24 |

Hence rational-point cardinality alone does not determine tangent-filling, even among smooth quartics with three, four, or five rational points.

## Assumptions and scope

The base field is exactly \(\mathbb F_2\). Equations are counted as coefficient vectors, not abstract isomorphism classes; since \(\mathbb F_2^\times=\{1\}\), each nonzero coefficient vector determines a distinct equation modulo nonzero scalar multiplication. A projective class means an orbit under \(\operatorname{PGL}_3(\mathbb F_2)=\operatorname{GL}_3(\mathbb F_2)\), which has order \(168\). Geometric smoothness is tested over an algebraic closure, not just at rational points. All geometrically smooth plane quartics are geometrically integral of genus \(3\).

For clarity, let \(\mathcal P=\mathbb P^2(\mathbb F_2)\) and \(\mathcal L\) be its seven lines. For a smooth quartic \(F\), let

\[
\mathcal T(F)=\{\,[F_X(Q):F_Y(Q):F_Z(Q)]\in\mathcal L:Q\in C_F(\mathbb F_2)\,\}.
\]

The gradient is nonzero at each rational point because the curve is geometrically smooth. Tangent-filling means \(\bigcup_{\ell\in\mathcal T(F)}\ell(\mathbb F_2)=\mathcal P\). Blocking means \(\ell(\mathbb F_2)\cap C_F(\mathbb F_2)\ne\varnothing\) for every \(\ell\in\mathcal L\).

## Proof

**Complete parameter space.** There are \(\binom{6}{2}=15\) degree-four monomials in three variables, hence \(2^{15}-1=32,767\) nonzero quartics. Encode a coefficient vector by an integer between \(1\) and \(32,767\), with one bit for each monomial in decreasing first exponent and then decreasing second exponent. Each of the \(168\) invertible binary matrices acts by exact polynomial substitution. The verifier computes all orbits, marking every element of each orbit, and checks that the orbits partition exactly those \(32,767\) vectors.

**Geometric smoothness.** Let \(F_X,F_Y,F_Z\) denote the formal partial derivatives in characteristic two. A plane quartic is geometrically singular if and only if \(F=F_X=F_Y=F_Z=0\) has a projective solution over an algebraic closure. The three affine charts \(X=1\), \(Y=1\), \(Z=1\) cover projective space. On each chart, the four specialized polynomials generate the unit ideal over \(\mathbb F_2\) precisely when their common zero set over the algebraic closure is empty (the weak Nullstellensatz). Thus checking a reduced Gröbner basis equals \(\{1\}\) on all three charts is an **exact** geometric smoothness test, not an extension-field experiment. Smoothness is invariant under invertible projective substitutions.

The complete orbit enumeration gives \(279\) orbits among all nonzero quartics, of which \(78\) are geometrically smooth. Summing the sizes of the latter orbits yields exactly \(10,920\) smooth coefficient vectors. These counts are obtained by the supplied standalone verifier and are not premises imported from a published list.

**Rational tangent and blocking incidence.** Represent every rational projective point by its unique nonzero binary vector \(p\in\mathbb F_2^3\); represent each rational line by a nonzero linear functional \(\ell\in\mathbb F_2^3\). The incidence condition is the binary dot product \(\ell\cdot p=0\). For each smooth orbit representative, the verifier evaluates \(F\) at all seven points to find \(C_F(\mathbb F_2)\). At each of those points it evaluates \((F_X,F_Y,F_Z)\) to recover the rational tangent line. It then tests coverage by the union of those tangent lines, and separately tests whether each of the seven rational lines meets the rational curve point set. Both properties are projectively invariant, so the representative's result is assigned to its entire orbit.

**Exact counting and cross-check.** The orbit-weighted four-category counts are \(2,040\), \(616\), \(1,848\), and \(6,416\), respectively. The corresponding numbers of orbits are \(14\), \(6\), \(11\), and \(47\). The verifier separately iterates over **all** \(10,920\) smooth coefficient vectors, recomputes the rational incidences without orbit weights, and checks agreement with the orbit-weighted counts. It also independently reevaluates the monomials and partial derivatives using a second literal arithmetic formulation for every smooth coefficient vector. The resulting point-count table and all four-category totals agree. The asserted probability follows by division.

**Explicit non-implications.** The geometrically smooth quartic

\[
X^3Y+XZ^3+Y^4=0
\]

has the three rational points represented by the binary vectors \(1,4,6\) (coordinate bits \(X,Y,Z\)), whose tangent-line functionals are \(4,2,6\). These are the three lines through a common rational point and together cover all seven points. However, the rational line with functional \(5\) misses all three curve points, so the curve is tangent-filling but not blocking. Conversely,

\[
X^3Y+X^3Z+X^2Y^2+XZ^3+Y^4=0
\]

is geometrically smooth and blocking with rational points \(1,4,5\), but its tangent-line functionals \(4,3,2\) cover only six rational points. Both smoothness assertions and all incidences are included in the exhaustive certificate. This proves that neither property implies the other.

## Verification

Run the included Python program in an environment with Python 3.10 or later and SymPy:

```bash
python3 verify_binary_quartic_tangents.py
```

It prints the exact \(32,767\)-equation, \(279\)-orbit, \(78\)-smooth-orbit, and \(10,920\)-smooth-equation counts, both weighted and direct joint incidence tallies, the point-count distributions, and the success sentinel `BINARY_QUARTIC_TANGENT_BLOCKING_CENSUS_PASS`. It checks geometric smoothness by Gröbner bases over all projective charts, so no bound on the degree of a possible singular geometric point is assumed. Every group transformation is explicitly enumerated, and all smooth equations are checked a second time for incidence. The program requires no external dataset.

## Relationship to prior work

Asgarli and Ghioca introduced tangent-filling for plane curves over finite fields (arXiv:2302.13420, first public 2023-02-26). They characterize it as coverage by rational tangents and relate it to blocking in the dual plane; their results concern general bounds and constructions, not this conditional quartic census. They also note the exceptional smooth conic behavior in characteristic two, which is separate from the degree-four classification here.

Nart and Ritzenthaler (arXiv:math/0312366, first posted in 2003) classify smooth nonhyperelliptic genus-three quartics in characteristic two by normal forms, bitangents, and Newton strata. Their classification provides an important pre-existing framework for the \(78\) classes but does not tabulate the rational tangent-covering property or its joint distribution with blocking. Lomont (arXiv:math/0105262) computed large-extension point counts for binary plane curves of degrees below seven, again with different invariants. Asgarli, Ghioca, and Yip (arXiv:2211.08523) compute unconditional blocking proportions and a Fano-plane line-union table; these do not supply the smooth degree-four tangent/point incidence distribution. The new information is the exact derivative-sensitive joint distribution, not a new classification of quartic isomorphism types.

## Limitations

This is an exhaustive theorem for one field and one degree, not a general formula for variable \(q\) or \(d\). Projective equivalence is over \(\mathbb F_2\); there is no assertion about geometric equivalence over extensions. The finite computation is exhaustive because the whole coefficient space and its exact projective orbits are traversed; mere finite-field sampling would not prove geometric smoothness. Earlier quartic classifications may encode enough information for an indirect recomputation, and an unindexed older tangent-incidence census remains a historical-priority risk. No independent audit or independent validation is claimed.

## References

1. Shamil Asgarli and Dragos Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, first posted 2023-02-26, https://arxiv.org/abs/2302.13420 .
2. Enric Nart and Christophe Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366, https://arxiv.org/abs/math/0312366 .
3. Shamil Asgarli, Dragos Ghioca, and Chi Hoi Yip, *Most plane curves over finite fields are not blocking*, arXiv:2211.08523, https://arxiv.org/abs/2211.08523 .
4. Chris Lomont, *Yet More Projective Curves Over F2*, arXiv:math/0105262, https://arxiv.org/abs/math/0105262 .
