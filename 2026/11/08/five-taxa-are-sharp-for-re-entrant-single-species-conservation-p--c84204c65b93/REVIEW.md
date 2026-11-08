# Scientific assessment

## Correctness: PASS

The exact identity \(G_i(p)=\sum_{e:i\in C_e}\ell_e(1-p)^{|C_e|}\) follows edge-by-edge from independent survival and a certain-survival intervention. Common ancestral terms cancel in pair comparisons. On up-to-four-tip binary trees, every least-common-ancestor split is either singleton versus a larger subtree (monotone after division by \(1-p\)) or two versus two (affine). On five-tip trees, only a two-versus-three split can generate a quadratic; the strict interior-root criterion is solved exactly. The explicit positive-length witness has difference \((1-p)((1-p)-1/5)((1-p)-4/5)\), and all competitor gains are strictly lower than one of the two focal gains. The standalone script independently checks rational expected PD, exact witness identities and tree topology enumeration. It does not stand in for the analytic universal proof.

## Originality: PASS within inspected evidence

Hartmann and Steel (2006) give the Noah's Ark objective, exact expected-PD inclusion formulas and greedy optimality results for restricted budget settings; Steel, Mimoto and Mooers (2007) give the HED formula and HEDGE variant; Faith (2008) gives the independent-extinction complementarity score, priority updates and examples. These are genuine broader methodological antecedents. Their inspected full texts do not give a sharp minimum number of taxa for a *double* common-probability priority switch, or the if-and-only-if quadratic criterion. A separate accessible equal-unit-edge case has a different hypothesis and does not dominate the variable-length case. Semantic searches included rank re-entry, dual complementarity, Noah's Ark, HED/HEDGE and expected-PD terminology, rather than title matching alone. Historical priority is provisional; mathematical deducibility from the already published formula is transparent and not misrepresented as a new optimization principle.

## Value: PASS

The exact smallest tree size and complete topological/algebraic characterization make the claim a natural finite structural boundary for conservation sensitivity analysis, not an arbitrary chosen parameter example. It exposes a genuine re-entry of the globally optimal *single action*, which cannot occur on smaller binary phylogenies, and distinguishes variable-length trees from the previously analyzed equal-unit-length regime. This aids interpretation of priority rankings under changing shared extinction risk. No empirical conservation recommendation or broad portfolio-optimality theorem is claimed.

## Closest sources and limits

- Hartmann and Steel, *Systematic Biology* 55 (2006), full author-hosted PDF, equations (1)–(2), Theorem 1 and small counterexample: prior objective, not this sensitivity transition.
- Steel, Mimoto and Mooers, *Evolutionary Bioinformatics* 3 (2007), full HTML, Theorems 3.1 and 4.1 plus proof: exact known ancestor formula, no size-optimal double switch.
- Faith, *Conservation Biology* 22 (2008), full HTML, expected-PD and priority section: dynamic conservation priority, but not uniform-risk five-taxon two-crossing characterization.

Residual risk: an unlocated earlier analysis could encode the same five-tip phase portrait; a parameterized algorithm can also compute this special case without presenting the sharp theorem. The proof's finite bound depends on a full-binary rooted tree and does not extend to correlated extinctions or larger action budgets by assertion.

Self-review: passed. Independent audit: not yet performed.
