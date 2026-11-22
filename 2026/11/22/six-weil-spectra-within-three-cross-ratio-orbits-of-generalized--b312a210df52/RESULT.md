# Six Weil spectra within three cross-ratio orbits of generalized Legendre quartics over \(\mathbb F_{13}\)

## Finding

For every \(\lambda\in\mathbb F_{13}\setminus\{0,1\}\), the smooth plane quartic
\[
C_\lambda:\quad Y^4=XZ(X-Z)(X-\lambda Z)
\]
has genus three. Across the eleven coefficient-marked curves, exactly **six distinct Hasse–Weil numerator polynomials** occur. More precisely, if \(Q_t(T)=1-tT+13T^2\), the entire classification is:

| Marked parameters \(\lambda\) | \(N_1\) | \(N_2\) | \(N_3\) | Numerator \(L_{C_\lambda}(T)\) |
|---|---:|---:|---:|---|
| \(2,12\) | 8 | 140 | 2216 | \(Q_{-6}Q_6^2\) |
| \(3,5,9,11\) | 16 | 172 | 2128 | \(Q_{-6}Q_{-2}Q_6\) |
| \(4\) | 28 | 172 | 2092 | \(Q_{-6}^2Q_{-2}\) |
| \(6,8\) | 12 | 212 | 2268 | \(Q_{-4}Q_2Q_4\) |
| \(7\) | 20 | 180 | 2180 | \(Q_{-6}Q_{-4}Q_4\) |
| \(10\) | 4 | 172 | 2164 | \(Q_{-2}Q_6^2\) |

Here \(N_n=\#C_\lambda(\mathbb F_{13^n})\), and products \(Q_{t_1}Q_{t_2}Q_{t_3}\) mean evaluation at the common variable \(T\). In particular, every Jacobian is isogenous over \(\mathbb F_{13}\) to a product of three elliptic curves, and each displayed factor is an elliptic Weil polynomial.

The natural anharmonic cross-ratio group, generated on the marked parameter line by \(\lambda\mapsto1-\lambda\) and \(\lambda\mapsto\lambda^{-1}\), has precisely three orbits:
\[
\{2,7,12\},\qquad\{3,5,6,8,9,11\},\qquad\{4,10\}.
\]
**Each orbit supports exactly two distinct Weil polynomials.** In particular, the two equianharmonic presentations \(\lambda=4\) and \(\lambda=10\) lie in one geometric branch-configuration orbit but have respectively \(28\) and \(4\) rational points. The statement concerns marked equations and their zeta functions, not a classification of unmarked arithmetic isomorphism classes.

## Assumptions and scope

All coefficients belong to the prime field \(\mathbb F_{13}\). Since the branch points \(0,1,\lambda,\infty\) are distinct and the characteristic does not divide four, the homogeneous quartic is nonsingular and has genus \(3\). There is exactly one rational point above infinity, over every extension. The phrase *Weil type* refers to equality of complete genus-three Hasse–Weil numerator polynomials, equivalently the \(\mathbb F_{13}\)-isogeny class of the Jacobian by Tate's theorem. The group orbits classify ordered-branch presentations up to the six classical anharmonic parameter transformations; they need not enumerate all curve automorphisms.

## Proof

**Exact point-count identity.** For \(n\in\{1,2,3\}\) put \(q=13^n\), \(f_\lambda(x)=x(x-1)(x-\lambda)\), and let \(R_q\) be the nonzero fourth powers of \(\mathbb F_q\). Since \(4\mid q-1\), each nonzero element of \(R_q\) has exactly four fourth roots and other nonzero elements have none. Thus the exact finite identity
\[
N_n(\lambda)=1+\#\{x\in\mathbb F_q:f_\lambda(x)=0\}
   +4\#\{x\in\mathbb F_q:f_\lambda(x)\in R_q\}
\]
holds. The leading \(1\) is the rational point at infinity; the sets on the right are disjoint.

**Exhaustive evaluation.** The attached standard-library program constructs two independent polynomial presentations of each of \(\mathbb F_{13^2}\) and \(\mathbb F_{13^3}\), checks irreducibility (no root for monic degree two or three), exhausts all field elements and all eleven admissible parameters, and obtains the three point counts in the table. Its independent fourth-power predicates (a set of fourth powers and an exponent test) agree at every tested field element. Agreement between both field presentations and all six frequency groups is asserted in executable checks, not merely an execution summary.

**Reconstruction of the full numerator.** Write \(s_n=q+1-N_n\), where in this sentence \(q=13^n\), so that \(s_n\) is the sum of the \(n\)-th powers of the six reciprocal Frobenius roots. Newton's identities give
\[
e_1=s_1,\quad e_2=(s_1^2-s_2)/2,\quad
e_3=(s_1^3-3s_1s_2+2s_3)/6.
\]
The genus-three functional equation forces
\[
L(T)=1-e_1T+e_2T^2-e_3T^3
   +13e_2T^4-169e_1T^5+2197T^6.
\]
The same verifier reconstructs all coefficients from the independently counted \(N_1,N_2,N_3\), then performs an integer polynomial multiplication check for each displayed factorization \(L=Q_{t_1}Q_{t_2}Q_{t_3}\). It exhausts all integral trace triples satisfying the genus-one Hasse bound \(|t_i|\le7\) and confirms uniqueness of the displayed unordered triple for each \(\lambda\). Since each of the six factors \(Q_t\) has an admissible elliptic Frobenius trace, the isogeny decomposition follows by the elliptic case of Honda–Tate together with Tate's isogeny criterion.

**Cross-ratio orbits.** Apply the two generators to the eleven nonexcluded parameters modulo thirteen until each orbit closes. The resulting disjoint orbits are the three listed above. Substituting their parameters into the six-type table exhibits exactly two different numerator polynomials in every orbit. Standard linear-fractional coordinate changes on the four branch points provide geometric isomorphisms of the cyclic cover after adjoining a fourth root of the corresponding scalar; therefore the \(4\)-versus-\(28\) example distinguishes arithmetic Frobenius behavior within one geometric branch-configuration class, without asserting a complete descent classification.

## Verification

Run `python3 verify_legendre_f13.py` in a standard Python 3 environment. It uses no external libraries or precomputed finite-field tables. The two independent extension-field models are generated by \(u^2+2\), \(u^3+4u+1\) and by \(u^2+5\), \(u^3+2u+2\), respectively; each polynomial's irreducibility is independently checked by exhaustive evaluation at all thirteen base-field elements. The checker reconstructs every point count and every Frobenius polynomial, verifies its unique decomposition into elliptic factors, and enumerates all anharmonic orbits. Expected final success line:

`GENERALIZED_LEGENDRE_F13_SIX_WEIL_SPECTRA_VERIFIED smooth=11 spectra=6 cross_ratio_orbits=3 two_spectra_per_orbit=3 independent_field_models=2`

The proof is finite and exhaustive only because the scope is the eleven prime-field marked parameters. No inference from a finite sample to all characteristics or all extension-field parameters is made.

## Relationship to prior work

Goodson [1, Sections 5.1–5.3] introduced and investigated this **identical** genus-three generalized Legendre quartic family, its period functions, and point-count formulas. The genus and fourth-power character-count identity are classical and are not claimed as new. Li–Mantovan–Pries–Tang [2] address the Newton polygons possible in special cyclic-cover families, while Cavalieri–Pries [3] study nonordinary mass and Cartier information for four-branch cyclic-cover families. An earlier arithmetic analysis [4] treats the *same* pencil for primes congruent to three modulo four, where the geometric Prym behavior is different, and explicitly does not provide zeta functions. None of the published material inspected supplies the **six-row characteristic-thirteen full Weil polynomial classification with its two-to-one distribution across every rational anharmonic orbit**. It is this exact arithmetic refinement, not the generic geometry, elliptic quotients, character-sum formula, or ordinary/supersingular dichotomy, that is the claimed contribution.

## Limitations

The classification is for the eleven coefficient-marked curves over \(\mathbb F_{13}\). It does not classify all cyclic-quartic genus-three covers, all twists, unmarked isomorphism classes, or other characteristics. The branch-configuration orbit relation does not itself prove arithmetic isomorphism. The exact finite arithmetic is reproducible, but independent mathematical review has not occurred. Earlier unindexed computational tables could conceivably contain the same six-type census; the closest adjacent mass-formula and Newton-polygon works were inspected at the abstract and topical level, and their complete appendices were not used to assert an exhaustive negative comparison.

## References

[1] H. Goodson, *Hypergeometric Properties of Genus 3 Generalized Legendre Curves*, arXiv:1705.02404, first public May 5, 2017. https://arxiv.org/abs/1705.02404

[2] W. Li, E. Mantovan, R. Pries, Y. Tang, *Newton Polygons Arising for Special Families of Cyclic Covers of the Projective Line*, arXiv:1805.06914, May 17, 2018. https://arxiv.org/abs/1805.06914

[3] R. Cavalieri, R. Pries, *Mass Formula for Non-Ordinary Curves in One Dimensional Families*, arXiv:2308.14891, August 28, 2023. https://arxiv.org/abs/2308.14891

[4] *The reduced superspecial divisor of the cyclic-quartic genus-three pencil at inert primes* (2026), publicly available scientific result: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-reduced-superspecial-divisor-of-the-cyclic-quartic-genus-thr--8c80d021706e
