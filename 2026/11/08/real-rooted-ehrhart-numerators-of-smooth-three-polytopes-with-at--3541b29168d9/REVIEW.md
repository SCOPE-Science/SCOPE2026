# Review of the five-facet smooth-threefold real-rootedness theorem

## Correctness — PASS

The theorem quantifies over every full-dimensional smooth three-dimensional lattice polytope with four or five facets. The published Kleinschmidt normal forms reduce all five-facet cases to \((p,q)=(1,2)\) or \((2,1)\), with integral \(a,b\ge1\) and \(c_j\ge0\). The counting formulas are exact in the standard lattice. The complete rational polynomial certificates verify nonnegativity of every discriminant monomial after translating to \(A=a-1,B=b-1,C\ge0\), including the degree-drop cases. The four-facet simplex formula is verified separately. Stanley's theorem supplies nonnegative numerator coefficients; discriminant positivity and nonnegative coefficients force simple strictly negative roots. Exact arithmetic verification was run from the actual package sources.

## Originality — PASS, with historical-priority risk

The closest source (Liu–Tang–Tao–Zhang, arXiv:2610.27819) proves Ehrhart **coefficient** positivity and records the classification, not root-realness of Ehrhart numerators. Nill (arXiv:2608.03635) assumes sufficiently large lattice width, while this theorem includes width-one classes. Ohsugi–Tsuchiya (arXiv:2610.06419) concerns special pseudo-symmetric reflexive duals, not the full smooth five-facet normal forms. Liu (arXiv:2610.06338) states general Cayley-sum counting and failure of unconstrained root preservation, not this classification. Searches for smooth five-facet \(h^*\) real-rootedness and full-result database comparisons found no covering statement. No search establishes absolute historical uniqueness, and older toric-threefold literature remains a residual priority risk.

## Mathematical value — PASS

The result gives a uniform sharp low-facet structural regime for a stronger polynomial property than the newly studied Ehrhart coefficient positivity. It identifies real-rootedness, simplicity, and strict negativity of all zeros across infinitely many twisted smooth simplex bundles, even at bounded width. Root-realness implies coefficient log-concavity and unimodality for this entire class, but is not a routine consequence of coefficient positivity, smoothness, IDP, or a generic Cayley preservation theorem.

## Scientific limitations

The discriminant identities are finite exact polynomial certificates rather than a conceptual factorization; the SymPy-based recomputation is supplied for independent reproducibility of the algebra. The result does not treat nonsmooth lattice polytopes or those with six facets. No independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
