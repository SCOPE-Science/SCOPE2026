# Scientific review

## Correctness — PASS

The assertion is for a single explicitly defined autonomous two-species ODE with all displayed ecological parameters positive, \(0<c\le1\), and coexistence iff \(b>m/(cU)\). A monotone predator nullcline and a strictly decreasing prey nullcline imply a unique positive equilibrium. The determinant of the per-capita Jacobian is positive, yielding strict monotonicity of prey abundance in effective attack intensity. Eliminating that intensity produces a positive smooth predator curve \(v=h(u)\) on \(0<u<U\) that vanishes at both endpoints. Its second derivative is strictly negative at **every** stationary point because \(f_{uu}<0\) and \(f_v<0\). This proves existence and uniqueness of its nondegenerate maximum and the refuge classification. Independently derived exact-rational witness identities and an extracted local checker agree. Numerical sweeps are not relied upon for the general quantifier.

## Originality — PASS (bounded literature assessment)

The closest same-model primary source is Ramraj and Poornima, *Frontiers in Artificial Intelligence* (2026), DOI 10.3389/frai.2026.1868693, sections 2, 4, 6 and Figure 3. It gives the model, equilibrium and local stability, and displays monotone parameter responses only in its chosen ranges. Its displayed results do not prove an all-positive-parameter unique predator maximum or exact refuge optimization. Indexed work titled “Fear changes the critical predator-extinction clock without moving the invasion boundary” and “A sharp global predator–prey threshold and universal critical extinction law under fear and refuge” treats global convergence and invasion criticality, which do not order equilibrium predator abundances across varying attack intensities.

The general ecological **overexploitation hump is prior art**: Holt and Hochberg (2001), Figure 2.2, describe a predator maximum at intermediate attack for a logistic prey–Lotka–Volterra example; Barbier, Wojcik and Loreau (2021), DOI 10.1111/oik.08043, analyze additional predation-density forms. The new statement is not the existence of such a phenomenon in ecology: it is its exact, universal, unique, nondegenerate parameter curve for the combined 2026 rational fear/crowding and predator-interference model. The older examples and general ecological discussion do not subsume this precise all-parameter theorem by logical implication. Some related full texts were not accessible and historical priority is not guaranteed.

## Value — PASS

A universal single maximum, its exact characterization and the complete refuge boundary-versus-interior decision are substantive properties of a recent ecological model. They resolve the difference between the original paper's restricted numerical trends and arbitrary high attack intensity, and give a precise parameter criterion for when additional refuge increases instead of decreases predator equilibrium abundance. An exact example makes this reversal reproducible without numerical simulation. No applied management or welfare recommendation is inferred.

## Limits and closest literature

This is an equilibrium-ranking result, not a new global-convergence theorem or an ecological experiment. The 2001 and 2021 predecessors establish the broad overexploitation mechanism. Full historic-priority completeness cannot be asserted from these searches. The original model's unobserved high-attack numerical regimes are mathematical parameter extrapolations, not empirical evidence.

Self-review: passed. Independent audit: not yet performed.
