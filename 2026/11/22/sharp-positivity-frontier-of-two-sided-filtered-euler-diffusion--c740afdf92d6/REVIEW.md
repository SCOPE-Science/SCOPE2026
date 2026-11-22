# Scientific review

## Correctness (PASS)

The claim fixes the three-site weighted path, positive conductances, a matched symmetric resolvent splitting and every real nonnegative timestep. The three off-diagonal entries follow from an explicit inverse and a positive common determinant. The scalar multiplier \((1+y^2)/(1+y)^2\) lies in \([1/2,1]\), proving that no diagonal entry can be negative. The two sign-controlling quadratics can never be concave simultaneously and each has a unique positive zero exactly when its own edge is more than twice as strong as its neighbor. Their explicit roots produce the stated unique threshold. The independent exact-rational checker passes 3,586 checks; those checks corroborate, but do not replace, the universal algebraic proof.

## Originality (PASS; qualified priority assessment)

Wu--Shu establish the two-sided filtered step and its energy stability but not this nonnegative-cone classification. Published claims for the same first-order method on unweighted graphs cover the three-vertex unit-edge case and a four-vertex failure, plus a weighted-graph long-step pseudoinverse obstruction; none yields the explicit finite-\(\tau\) interval for a **heterogeneously weighted three-site path**. Records on the two-stage Gauss--Legendre method give the same all-step conductance-ratio dividing line, but use a different rational function; at \((a,b,\tau)=(3,1,6)\) Gauss is positive on the strong edge while the present method is negative. This supplies a concrete nonimplication for the sharper finite-step assertion. The identity with a square of the Crank--Nicolson step is a useful equivalence but alone supplies no sign classification.

A residual priority risk remains from unindexed or full-text-inaccessible specialist analyses of the same rational filter. The relevant Gauss record was inspected at the level of its public scientific summary, not its entire underlying manuscript; the comparison does not falsely treat that summary as a full-text exclusion.

## Value (PASS)

Three vertices are the smallest connected weighted-path size for which the stable filter can violate nonnegative-cone preservation; two-vertex paths cannot fail. The exact conductance-ratio dichotomy and nonreentrant safe-time interval quantify how heterogeneity, not stepwise energy instability, produces negative numerical heat transitions. This is a complete natural minimal-network classification, and the finite cutoff is operationally meaningful for positivity-sensitive graph diffusion discretizations. No general-PDE positivity, floating-point stability, or arbitrary-graph classification is claimed.

## Scientific limitations

Exact arithmetic; fixed splitting \(S=L\); only weighted three-site paths. Unindexed historical priority remains possible and one relevant public source was accessible only by its abstract-level record. Independent evaluation is outstanding.

Self-review: passed. Independent audit: not yet performed.
