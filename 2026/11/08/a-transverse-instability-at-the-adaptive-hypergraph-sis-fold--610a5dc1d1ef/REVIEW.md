# Scientific review

## Correctness — PASS

The positive stationary equations reduce to a strictly convex cubic; imposing a double root gives the exact fold. Differentiating the full two-dimensional update gives the stated Jacobian, whose second multiplier at the fold is an explicit expression. A rational admissible parameter set gives a strictly superunit eigenvalue and a unit fold eigenvalue, verified exactly. Continuity plus the implicit-function theorem makes two nearby positive fixed points unstable on an open set with \(\beta<1\). The result does not assert global convergence, stochastic extinction or absence of periodic attractors.

## Originality — PASS (qualified)

Li et al. (arXiv:2606.15578), Sections 2.1 and 2.3, supply the underlying updates and the implicit stationarity threshold; they do not present the additional transverse fold multiplier or a regime with two unstable endemic fixed points. Jhun et al. (arXiv:1910.00375) concern static scale-free hypergraphs; Higham–de Kergorlay (2022) concern different dynamic hypergraph infection laws. Searches of accessible published research records for the precise second-multiplier mechanism returned no equivalent claim; indexing gaps remain possible. The strongest overlap is the original stationary fixed-point formula, which does **not alone classify stability** of the second dynamical coordinate.

## Mathematical value — PASS

A saddle-node in a two-dimensional epidemic-adaptation model need not imply coexistence of an attracting endemic equilibrium with an attracting disease-free equilibrium. The result provides the missing transverse multiplier and a feasible exact certificate; this changes the interpretation of homogeneous threshold diagrams and identifies when fixed-point census overstates stable endemic persistence.

## Limits and evidence

The full homogeneous-model equations, threshold theorem and conclusion of the motivating primary paper were inspected in accessible HTML. Related older-paper descriptions establish different model classes; their full texts were not used to certify whole-document absence. Exact algebra and checks are reproduced by `fold_check.py`. An unindexed equivalent and other nonlinear attractors remain open questions.

Self-review: passed. Independent audit: not yet performed.
