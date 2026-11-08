# Scientific review: irreversible monomer adsorption on two strongly regular graphs

## Correctness
PASS. The two explicit adjacency relations realize the same \((16,6,2,2)\) parameters. A graph-theoretic reduction after two accepted sites gives nine residual choices: on the rook graph all are four-cycles; on the Shrikhande graph three are four-cycles and six are diamonds. This proves the complete terminal distribution. The time-dependent difference follows from the exact 16-site subset recurrence, and all Bernstein coefficients were checked as reduced rational numbers. `verify_terminal.py` constructs the full probability measure on terminal labeled sets; `verify_kinetics.py` independently computes the expected-occupancy coefficients and exhaustively checks every four-vertex arrival ordering for the first differing term.

## Originality
PASS on accessible comparison, with an explicit historical risk. Dhara, van Leeuwaarden and Mukherjee study random-graph large-network limits; Krivelevich and coauthors develop locally convergent graph methods and tree inequalities. The closest published same-graph comparison provides independence complexes and static independent-set polynomials, which do not encode random-priority output weights. Pippenger (1989) studies adsorption on regular graphs; its complete text could not be checked, so priority cannot be regarded as independently established. The actual claim is the per-terminal-state law and all-positive-time expected-coverage comparison, not the previously established nonisomorphism, spectra, independent-set counts or existence of general RSA methods.

## Mathematical value
PASS. This exact dynamical example separates a canonical strongly regular, cospectral pair by a physically natural irreversible-adsorption observable. The all-time inequality, a fourth-order first kinetic distinction, and individually resolved terminal probabilities give a reproducible small-system benchmark, rather than only restating known static graph data.

## Limitations
Only the two specified sixteen-site graphs and independent uniform rate-one first attempts are treated. The comparison establishes a strict expectation inequality, not stochastic or pathwise domination; no thermodynamic-limit result is claimed. Historical literature not available in full remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
