# Scientific review

## Correctness (PASS)

The defined five-vertex death–Birth chain lumps exactly to twelve \((i,j)\) states because each vertex in a given bipartition part has precisely the same neighbors. The actual ten transient backward equations and two absorbing boundary values are stated explicitly. The seven-degree integer polynomial certificate solves every backward equation identically in the indeterminate \(r\), and the positive denominator plus finite-state absorption establish that these are the unique fixation probabilities for every \(r>0\). All three sign differences are identically checked. Two have strictly positive numerator coefficients. The third has exactly one positive zero by a single Descartes sign change and an opposite-sign evaluation. The delivered independent 30-state solver checks an additional 240 exact rational comparisons but is not used to prove the all-fitness theorem. Domain excludes \(r=0\), and no fixation-time conclusion is made.

## Originality (PASS, subject to stated priority risk)

The initiating paper Durocher–Karras–Pavlogiannis–Tkadlec, *Invasion Dynamics in the Biased Voter Process* (arXiv:2201.08207, §§2–5), provides general biased-voter initial-seed maximization, already notes fitness-dependent seed rankings, and proves complexity and submodularity statements, but gives no exact \(K_{2,3}\) two-seed crossover. Thus novelty is solely the explicit complete analytic three-profile formula and unique degree/mixing threshold. Zhang et al.'s exact complete-bipartite formulas use birth–death updating; de Souza–Neves analyze star topology; Brewster et al. analyze neutral bidegreed and star/cycle settings rather than arbitrary-fitness two-seed \(K_{2,3}\). Petsinis et al. optimize placement of bias rather than placement of initial mutants. Research-record searches of the precise objects, update convention, graph, parameter and crossover did not return a covering theorem. Residual risk: an unindexed calculation or general theorem might imply this specific five-vertex result. Negative search results alone do not prove novelty.

## Value (PASS)

On a smallest unequal nonstar biclique, each of the three possible two-mutant orbit types represents a biologically meaningful choice between concentrating seeds on central individuals and distributing them across degree classes. Neutral theory favors high-degree concentration, while this theorem proves that at sufficiently high fitness spatial mixing strictly dominates it and pins down the exact threshold. The whole positive-fitness classification gives a concrete nontrivial benchmark for influence and evolutionary seeding; it is not a mere relabeling or arbitrary numerical slice. The five-vertex model is limited in scale and no claim of universality across graph sizes is made.

## Scope and outstanding limits

No independent external validation has been performed. Source comparisons address published text and available research records but cannot exclude inaccessible or unpublished equivalents. Exact linear algebra is certified in the accompanying standard-library checker; finite test points are supplemental to polynomial identity proofs.

Self-review: passed. Independent audit: not yet performed.
