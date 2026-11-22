# Scientific review: fractional Markovian repair of antagonistic complete networks

## Correctness
PASS. The signed row-sum Laplacian is diagonalized on a constant mode, within-block mean-zero spaces and their orthogonal complement. Direct entries of its spectral power give an exact necessary-and-sufficient Metzler criterion. The heat-kernel entries reduce positivity to a strictly convex scalar exponential crossing, with a unique positive root precisely above the critical exponent. The row-sum identity gives exact endpoint norms; local Taylor expansion at the crossing establishes the linear onset and quadratic norm-amplification laws. The near-degenerate scaling follows from the root equation. The independent finite diagnostic script returned `VERIFICATION_OK 2941`, but it is not used to establish the all-parameter theorem.

## Originality
PASS on the inspected evidence, not an assertion of exhaustiveness. Chen et al. prove a general signed-Laplacian semidefiniteness/eventual-positivity link, and Fontan–Altafini treat pseudoinverses; neither states fractional Markov restoration with these thresholds. A directly related public result on fractional graph heat treats **nonnegative** edge weights and forces the universal critical exponent one. A result on block-homogeneous complete networks uses a **rational Gauss–Legendre discretization** with nonnegative within-block weights, not the fractional continuous semigroup. A general sharp spectral-window envelope optimizes over matrices, not the individually structured signed-network kernel. The exact lower critical exponent, entrywise horizon and norm expansion are not implications of those statements. Searches may miss prior work under signed consensus, Bernstein matrix functions, or eventual positivity terminology.

## Mathematical value
PASS. Signed positive-semidefinite Laplacians generate eventual rather than immediate positive evolution, a meaningful issue in signed consensus and nonlocal graph diffusion. The theorem gives a complete, parameter-dependent boundary for when fractionalization repairs genuine Markov positivity, characterizes the entire time set of entrywise nonnegativity when it does not, and quantifies linear recovery delays versus quadratic transient amplification. All negative-clique blocks may have different weights and sizes. This is a structural network family, not an arbitrary numerical slice.

## Limitations and review state
The result concerns a homogeneous positive background with disjoint homogeneous negative blocks and a strictly positive complementary spectrum. The proof supplies no graph-size-uniform error estimates or fully general signed-graph criterion. It does not settle absolute historical priority; the relevant search avenues and specific remaining risks are recorded in the structured review. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
