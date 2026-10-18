# Tree-plan counting polynomials are SU-rank partition functions

## Finding

Let \(\Gamma=(\Gamma,\lambda)\) be a finite tree plan and let \(M=\Gamma(\omega)\). Mirabi associates to \(\Gamma\) a counting polynomial \(P_\Gamma(x)\), a path degree \(\deg_\Gamma(\sigma'/\sigma)\), and a normalized asymptotic exponent
\[
\delta_\Gamma(\sigma'/\sigma)=\frac{\deg_\Gamma(\sigma'/\sigma)}{\deg(\Gamma)}.
\]
For a finite parameter set \(B\subseteq M\) and \(a\in M\), let
\[
e=[a\wedge B]=\max\{d\in\operatorname{tcl}(B):d\le a\}.
\]
Then
\[
\boxed{SU(a/B)=I(\Gamma,\pi(a))-I(\Gamma,\pi(e))
      =\deg_\Gamma(\pi(a)/\pi(e)).}
\]
Here \(I(\Gamma,\sigma)\) is the number of infinity-nodes on the plan path from the root to \(\sigma\). If \(a\in\operatorname{acl}(B)=\operatorname{tcl}(B)\), then \(e=a\) and both sides are zero. Consequently, whenever \(D=\deg(\Gamma)>0\),
\[
\boxed{\delta_\Gamma(\pi(a)/\pi(e))=\frac{SU(a/B)}{D}.}
\]
Thus every one-variable exponent in the tree-plan asymptotic calculus is exactly a normalized SU-rank, not merely an upper bound for one.

There is also a global generating-function identity. The parameter-free complete 1-types are indexed by plan nodes \(\sigma\in\Gamma\); write \(p_\sigma\) for the type of any element in the fiber \(P_\sigma\). Then
\[
SU(p_\sigma)=I(\Gamma,\sigma)
\]
and
\[
\boxed{P_\Gamma(x)=\sum_{\sigma\in\Gamma}x^{I(\Gamma,\sigma)}
      =\sum_{p\in S_1(\varnothing)}x^{SU(p)}.}
\]
If \(c_r=[x^r]P_\Gamma(x)\), then \(c_r\) is exactly the number of parameter-free 1-types of SU-rank \(r\).

For every integer \(m\ge1\), the finite approximation \(\Gamma(m)\) contains exactly
\[
\boxed{c_r m^r}
\]
elements whose corresponding limit 1-type has SU-rank \(r\). Hence for a uniformly chosen element of \(\Gamma(m)\), with \(R_m\) denoting that rank,
\[
\Pr(R_m=r)=\frac{c_r m^r}{P_\Gamma(m)},
\qquad
\mathbb E[R_m]=\frac{mP_\Gamma'(m)}{P_\Gamma(m)}.
\]
Also
\[
\operatorname{Var}(R_m)=
\frac{m^2P_\Gamma''(m)+mP_\Gamma'(m)}{P_\Gamma(m)}
-\left(\frac{mP_\Gamma'(m)}{P_\Gamma(m)}\right)^2.
\]
In particular the rank distribution concentrates on \(D=\deg(\Gamma)\): \(\Pr(R_m=D)\to1\).

## Assumptions and scope

The structure is Mirabi's pure tree-plan generic in the language with the plan-node predicates. The formula concerns singleton SU-rank over finite parameter sets. The normalized identity uses \(D>0\); when \(D=0\), the structure is finite/algebraic at the singleton level and the unnormalized rank formula still holds.

The finite statistic \(R_m\) is the SU-rank of the unique parameter-free type in the infinite generic having the same plan node as the sampled finite element. No SU-rank is being assigned intrinsically to the finite structure itself.

## Proof

Mirabi proves \(\operatorname{acl}=\operatorname{tcl}\). The tree closure contains the downward closure and then repeatedly adjoins all successors whose plan label is \(1\). Therefore, if \(e=[a\wedge B]\), the only nonalgebraic choices remaining on the path from \(e\) to \(a\) occur at infinity-nodes.

Let
\[
r_B(a)=|I(M)\cap(e,a]|.
\]
We prove \(SU(a/B)=r_B(a)\) by induction on \(r_B(a)\). If \(r_B(a)=0\), the entire path from \(e\) to \(a\) consists of forced \(1\)-successors, so \(a\in\operatorname{tcl}(B)=\operatorname{acl}(B)\), and the rank is zero.

Suppose \(r_B(a)>0\). For the lower bound, let \(d\) be the first infinity-node above \(e\) on the path to \(a\). Mirabi's dividing criterion (Proposition 8.2.1) says that \(\operatorname{tp}(a/Bd)\) divides over \(B\), because \(d\in I(M)\cap\operatorname{tcl}(Bd)\setminus\operatorname{tcl}(B)\) and \(e<d\le a\). Closing under the forced \(1\)-successors after \(d\) removes exactly this first unresolved infinity-node, so \(r_{Bd}(a)=r_B(a)-1\). Induction gives a forking extension of rank \(r_B(a)-1\), hence \(SU(a/B)\ge r_B(a)\).

For the upper bound, take any finite forking extension \(\operatorname{tp}(a/C)\) with \(B\subseteq C\). By the same dividing criterion, some new infinity-node \(d\in\operatorname{tcl}(C)\setminus\operatorname{tcl}(B)\) lies on \((e,a]\). Thus \([a\wedge C]\ge d\), so at least one unresolved infinity-node has disappeared and \(r_C(a)\le r_B(a)-1\). Induction yields \(SU(a/C)\le r_B(a)-1\). Finite character reduces arbitrary forking extensions to this finite case, giving \(SU(a/B)\le r_B(a)\).

Projecting the path to the finite plan shows
\[
r_B(a)=I(\Gamma,\pi(a))-I(\Gamma,\pi(e)),
\]
which is exactly Mirabi's definition of \(\deg_\Gamma(\pi(a)/\pi(e))\). This proves the local formula and the normalized exponent identity.

For the global statement, Mirabi's unary predicates distinguish different plan nodes, while elements in the same fiber have the same parameter-free type. Hence \(S_1(\varnothing)\) is indexed by \(\Gamma\), and the local formula over the empty set gives \(SU(p_\sigma)=I(\Gamma,\sigma)\).

Mirabi proves that the fiber over \(\sigma\) in \(\Gamma(m)\) has cardinality \(m^{I(\Gamma,\sigma)}\), and that \(|\Gamma(m)|=P_\Gamma(m)\). Summing the fibers gives, for infinitely many integers \(m\),
\[
P_\Gamma(m)=\sum_{\sigma\in\Gamma}m^{I(\Gamma,\sigma)}.
\]
Thus the two polynomials are identical. Grouping terms by rank gives the exact \(c_r m^r\) stratum count. The probability and moment formulas follow by differentiating the generating polynomial, and concentration at maximal rank follows by dividing by the leading term.

## Verification

The bundled standard-library checker exhausts 50,363 labeled finite tree plans of sizes at most seven. For every plan it independently computes the recursive counting polynomial, the node-rank enumerator, all comparable-node local degree differences, and the rank obtained from the recursive dividing rule that allows a forking step exactly when a new infinity-node on the path is absorbed. It also checks the finite rank-distribution moment identities. The run performs 2,399,626 assertions and prints `VERIFY_OK`.

This is a finite regression test, not a substitute for the model-theoretic proof.

## Relationship to prior work

Mirabi's 2023 tree paper supplies all of the tree-specific ingredients: the counting polynomial and local degrees, the exact fiber cardinalities, \(\operatorname{acl}=\operatorname{tcl}\), and the dividing criterion. It states the general asymptotic-class implication that SU-rank is at most the asymptotic dimension, but it does not identify its counting polynomial as an SU-rank enumerator or its normalized local exponents as normalized SU-ranks.

A later revision of Mirabi's coordinatization paper proves a broader additive SU-rank theorem for canonical tree products. That theorem independently supports the rank computation after specialization to pure equality components. Accordingly, originality is not claimed for the bare fact that infinity-coordinates contribute additively to SU-rank. The retained contribution is the exact bridge to the earlier finite counting apparatus: the identities with \(\deg_\Gamma\), \(\delta_\Gamma\), \(P_\Gamma\), the coefficientwise 1-type census, and the induced finite rank distribution and moments.

Targeted searches under exact-rank, normalized-exponent, generating-polynomial, coefficient, and finite-rank-distribution formulations did not locate this bridge. Because the deduction is short once the two Mirabi papers are read together, an uncatalogued folklore observation remains possible.

## Limitations

The result is for singleton types in the pure tree-plan generic. The tuple-rank analogue would require tracking shared infinity-coordinates and is not asserted here. The finite rank distribution is a distribution of limiting parameter-free types attached to finite elements, not an intrinsic rank theory of finite models. No independent audit has been performed.

## References

- Mostafa Mirabi, *Asymptotic Classes of Trees and \(\aleph_0\)-categoricity*, arXiv:2307.07899v1 (first public 2023-07-15), later published in *Notre Dame Journal of Formal Logic* 66 (2025), 455–476. Relevant items: Definitions 3.0.5 and 5.1.7, Lemmas 5.1.4 and 5.1.6, Theorem 5.3.1, Lemma 8.1.1, and Proposition 8.2.1.
- Mostafa Mirabi, *MS-measurability via Coordinatization*, arXiv:2109.11760, first public 2021-09-24; current v3 dated 2026-07-21. Theorem 6.2 gives the broader additive SU-rank computation for canonical tree products.
