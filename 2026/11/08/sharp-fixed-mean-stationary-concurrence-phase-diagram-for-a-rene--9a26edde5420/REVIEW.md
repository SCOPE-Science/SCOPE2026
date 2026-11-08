# Scientific review: stationary concurrence under fixed-mean renewal resetting

## Correctness — PASS

The stationary-age measure \(\mathbb P(T>a)da/\mu\) is normalized by finite mean and valid even for lattice laws. The exact unitary path occupies only the \(|00\rangle,|11\rangle\) block; Wootters concurrence on this block equals twice the off-diagonal modulus. Fubini gives \(\mathbb E\sin(\Omega B)=\mathbb E(1-\cos\Omega T)/(\Omega\mu)\ge0\). The supporting function built from a tangent line, a concave half-cosine arc, and a constant segment is globally concave and dominates \(1-\cos x\). Jensen, equality geometry, and explicit two-point laws prove all upper and lower endpoint claims. A finite checker tests 1466 conditions including independent spin-flip calculations; no finite computation is substituted for proof.

## Originality — PASS, qualified

The 2023 Kulkarni–Majumdar two-spin concurrence result is explicitly Poissonian and uses a different spin Hamiltonian; it neither quantifies fixed-mean renewal protocols nor classifies all maximizing reset clocks. The 2022 Sevilla–Valdés-Hernández work gives the general stationary renewal quantum state and coherence/purity/fidelity but not this two-qubit concurrence phase diagram. The 2024 Wald and collaborators work treats discrete gates, resonances and selected non-Poissonian existence questions rather than the continuous-time all-clock fixed-mean optimum. A known fixed-mean *qubit purity* envelope is not an implication covering this concurrence theorem: purity optimizers are deterministic up to a different threshold, while concurrence exhibits an early nonattained randomization plateau. Generic convex-analysis tools are credited. Unindexed specialized quantum-control or moment-problem comparisons are a remaining priority risk, not evidence of coverage.

## Mathematical value — PASS

At a fixed average intervention frequency, the exact achievable stationary entanglement is a natural resource invariant. The switch from optimal randomization to optimal deterministic resetting at \(\xi=2.331122\ldots\) is an actual protocol-design boundary; the limiting concurrence \(\sin\xi\approx0.724611\) exceeds the best possible Poisson-clock value \(1/2\). The classified equality cases and zero-concurrence threshold distinguish mixed-state entanglement from trajectory averages and from the previously solved purity question.

## Scope and residual risks

The interaction is the exactly solvable continuous-time coupling \(H=(\hbar\Omega/2)\sigma_x\otimes\sigma_x\); reset events are instantaneous and complete. For clocks with fixed periods, the equilibrium age ensemble is not necessarily the limit from a time-zero synchronized reset. The sharp fast-reset supremum uses arbitrarily short intervals, with no physical minimum-duration constraint. A more general unpublished or unindexed theorem could cover the envelope, although no inspected primary result gives this classification.

Self-review: passed. Independent audit: not yet performed.
