# Nine \(\mathrm{GL}(5,2)\)-plus-linear classes of ordered-separating cubic Boolean functions

## Finding

Set \(V=\mathbb F_2^5\). For every square-free Boolean polynomial \(\alpha:V\to\mathbb F_2\) of exact algebraic degree three and \(\alpha(0)=0\), write
\[
D_2\alpha(x,z)=\alpha(x+z)+\alpha(x)+\alpha(z).
\]
Call \(\alpha\) *ordered-separating* when, for each ordered pair of distinct nonzero \(x,y\in V\), some \(z\in V\) satisfies \(D_2\alpha(x,z)=1\) and \(D_2\alpha(y,z)=0\).

**Theorem.** Exactly \(690432\) ordered-separating degree-three polynomials exist modulo adding arbitrary linear functions, or \(22093824\) when all linear parts are counted. The equivalence
\[
\alpha\sim_{\mathrm{lin}}\alpha\circ T+\ell,\qquad T\in\mathrm{GL}(5,2),\ \ell\in V^*,
\]
partitions their linear-quotient classes into exactly nine orbits. Their sizes and canonical representatives in the explicit binary encoding below are:

| Minimum mask | Number of classes | Stabilizer order | \(\dim\operatorname{Rad}(D_3\alpha)\) |
|---:|---:|---:|---:|
| 1536 | 69440 | 144 | 2 |
| 1543 | 9920 | 1008 | 2 |
| 20480 | 13888 | 720 | 0 |
| 20484 | 208320 | 48 | 0 |
| 20640 | 8680 | 1152 | 0 |
| 20644 | 52080 | 192 | 0 |
| 20650 | 5208 | 1920 | 0 |
| 20652 | 156240 | 64 | 0 |
| 20784 | 166656 | 60 | 0 |

Here the stabilizer orders equal \(9999360\) divided by the corresponding orbit sizes. The published symmetric \(M\) and \(O\) functions lie in orbits 20480 and 20650; the recently published five-variable counterexample \(\delta\) lies in orbit 20484; the ternary-cubic-plus-quadratic-block construction lies in orbit 1536.

## Assumptions and scope

Every Boolean function has a unique square-free algebraic normal form modulo the relations \(x_i^2=x_i\). There are ten degree-two monomials and ten degree-three monomials on five variables. Linear terms do not affect \(D_2\), and every linear-equivalence class has a unique representative whose linear terms vanish. Write each representative as
\[
\alpha(x)=\sum_{j=0}^{19}\epsilon_j m_j(x),\qquad \epsilon_j\in\mathbb F_2,
\]
where \(m_0,\ldots,m_9\) enumerate the degree-two square-free monomials in increasing binary support-mask order, and \(m_{10},\ldots,m_{19}\) do likewise for degree three. Encode it by the integer \(\sum_j2^j\epsilon_j\). Exact cubic degree means at least one of bits 10 through 19 is set. The canonical representative of an orbit is the **least integer mask** occurring in that orbit, not a minimum-complexity polynomial.

Input equivalence is linear only; allowing a linear output correction is essential. The theorem does not identify ungraded algebra-isomorphism classes or classify all degree-three forms in larger dimensions.

## Proof

**Step 1: Exact membership test.** For every nonzero \(x\in V\), form its second-polar row as a support set
\[
R_x=\{z\in V:D_2\alpha(x,z)=1\}.
\]
Ordered separation is equivalent to \(R_x\not\subseteq R_y\) for every pair of distinct nonzero \(x,y\). Testing both orders is equivalent to demanding that the 31 nonzero-indexed rows form an antichain of nonempty subsets of the 32-element space \(V\). This is a direct equivalence of quantified statements, not a heuristic.

For each of the twenty monomials \(m_j\), compute the 31 row-support bitmasks by the explicit formula
\[
D_2m_j(x,z)=m_j(x+z)+m_j(x)+m_j(z).
\]
Because the second polar is linear in \(\alpha\), the row of a coefficient vector is the bitwise exclusive-or of its selected monomial rows. The attached `check_cubic_orbits.cpp` visits all \(2^{20}\) coefficient words in Gray-code order, updating exactly one selected monomial's rows per step. It discards precisely the \(2^{10}\) words having zero cubic coefficient block. For all remaining \(1047552\) words, it implements the complete 31-row antichain criterion, producing exactly \(690432\) accepted coefficient words. Adding arbitrary five-bit linear output parts gives \(32\cdot690432=22093824\) polynomials.

**Step 2: All linear-equivalence orbits.** Four adjacent swaps of the five input variables, together with the elementary transvection \(x_1\mapsto x_1+x_2\), generate \(\mathrm{GL}(5,2)\): adjacent swaps generate all permutations, and conjugating this transvection supplies every elementary off-diagonal transvection; Gaussian elimination decomposes every invertible matrix into those generators. Each generator acts on the twenty-dimensional coefficient space modulo linear terms. For each of its twenty monomial basis vectors, the attached checker evaluates the transformed Boolean truth table on all 32 points and applies the full 32-point binary Möbius inversion to recover the coefficient vector. Consequently every generator image is computed exactly, including lower-degree quadratic terms induced by substitutions into cubics.

For each of the five generators and each accepted coefficient word, the checker computes its transformed word, verifies that it remains in the accepted set, and unites the two words in a disjoint-set structure. Since the five generators generate the complete group, the connected components are **exactly**, not merely subsets of, \(\mathrm{GL}(5,2)\)-orbits. The resulting disjoint-set components have precisely the nine minimum representatives and cardinalities in the theorem; their cardinalities sum to \(690432\). This proves completeness and inequivalence simultaneously. Their stabilizers follow from orbit–stabilizer and
\[
|\mathrm{GL}(5,2)|=(2^5-1)(2^5-2)(2^5-4)(2^5-8)(2^5-16)=9999360.
\]

**Step 3: Published exemplars and third-polar radicals.** The polynomial with all ten cubic terms and no quadratics is mask 1047552; adding all ten quadratics gives mask 1048575. The five-variable construction \(x_2x_3+x_1x_2x_5+x_1x_3x_4\) is mask 20484. The cubic-block extension \(x_1x_2x_3+x_4x_5\) is mask 1536. Their generator-components are, respectively, 20480, 20650, 20484, 1536. Contracting each representative's alternating third polar against each of the five basis vectors gives the radical dimensions in the table; only the cubic part affects this contraction. An independent direct truth-table check of all 930 ordered nonzero pairs for each of the nine representatives confirms that each has a separating witness.

All bounds in the proof are finite and explicit. Executing the complete exact loops in the accompanying standalone source is the exhaustive certificate for the two numerical claims.

## Verification

From a C++17 compiler, run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra check_cubic_orbits.cpp -o check_cubic_orbits
./check_cubic_orbits
```

The checker requires no external data, packages, or randomness. It asserts \(1047552\) tested degree-three masks, \(690432\) passing masks, zero missing images for every group generator, nine components, the exact nine orbit-size/minimum-mask pairs, and all published exemplar memberships. It also independently reconstructs the full Boolean truth tables of all nine representatives and checks each ordered pair against all 32 witnesses. Successful execution prints `CUBIC_FIVE_ORBIT_CENSUS_OK` and the complete table.

## Relationship to prior work

Morier-Genoud and Ovsienko introduced the relevant cubic generating functions and proposed their symmetric normal-form characterization. Pineda Montoya (2026) disproved the characterization with analytic infinite families; their Section 9 explicitly does **not** classify all ordered-separating cubics and identifies quadratic extensions of a fixed third polar as a separate issue. The present result provides a complete five-variable orbit census in precisely that quadratic-sensitive sense.

Khoruzhii, Gelß and Pokutta (2026) classify *pure cubic-layer* forms, equivalently alternating trilinear forms, up to linear change of basis, discarding quadratic coefficients. Their cubic-layer classification does **not** imply the nine-orbit count here: distinct second polars and ordered-separation outcomes can occur over the same cubic third polar. The two positive-dimensional-radical orbits and seven radical-zero orbits are refined further by these quadratic parts.

## Limitations

The theorem is limited to five variables, exact degree three, and the specified \(\mathrm{GL}\)-plus-output-linear equivalence. It does not prove that nine ungraded twisted-quasialgebra isomorphism classes exist. The counts depend on an exhaustive integer-and-bitwise computation whose full standalone source is supplied; the proof of completeness is algorithmic, not a closed noncomputational orbit formula. Historical priority cannot be guaranteed against unindexed classifications. Independent external auditing remains outstanding.

## References

1. S. Pineda Montoya, *Counterexamples to a Cubic Nondegeneracy Conjecture*, arXiv:2611.02544v1 (first posted November 2, 2026), https://arxiv.org/html/2611.02544v1.
2. S. Morier-Genoud and V. Ovsienko, *A Series of Algebras Generalizing the Octonions and Hurwitz–Radon Identity*, arXiv:1003.0429v4, https://arxiv.org/pdf/1003.0429.
3. K. Khoruzhii, P. Gelß and S. Pokutta, *Classification of Boolean Cubic Forms in Ten Variables*, arXiv:2606.28473v1 (2026), https://arxiv.org/pdf/2606.28473.
