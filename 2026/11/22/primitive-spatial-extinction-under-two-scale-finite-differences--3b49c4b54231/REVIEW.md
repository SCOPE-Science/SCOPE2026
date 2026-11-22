# Review

## Correctness — PASS

For characteristic \(p\nmid n\), the cyclic shift polynomial \(z^d-1\) is squarefree at each \(d\mid n\). Counting the union of zero factors \(z^a-1\) and \(z^b-1\) proves the kernel dimension on every divisor-period subspace. Möbius inversion then gives the exact primitive count. The cyclotomic module decomposition proves the sharp existence criterion, and the constant-fiber map from the coprime-stride factors proves the factorization. The standalone checker directly enumerated 58,939 finite configurations over three prime fields and verified 110 complete instances, including the nontrivial six-cell case. The analytic proof, not enumeration, supports the unrestricted theorem.

## Originality — PASS (priority provisional)

Banda–Caughman–Lehman (2026, arXiv:2611.15751v1) prove stabilizer monotonicity and enumerate symmetry classes, but do not give the specific primitive-to-zero census or nonzero two-scale arithmetic boundary. Ninagawa (2013, arXiv:1307.3888) analyzes binary single-difference dynamics, specifically period-halving on dyadic rings; it does not establish the prime-to-characteristic mixed-stride criterion. Barbè–von Haeseler (2001) investigates periodic temporal traces at fixed sites rather than this one-step primitive spatial kernel. Related published results on single-difference first symmetry clocks involve one nilpotent factor with the remaining factor invertible, whereas neither factor here is invertible. The finite-field polynomial gcd and Möbius ingredients are classical and not themselves novel. Unexamined older general additive-cellular-automata classifications may imply this particular formula; that is a residual historical-priority risk.

## Mathematical value — PASS

The sharp all-length arithmetic boundary distinguishes when a genuinely nonzero finite-difference automaton erases maximum spatial asymmetry in one step. It identifies a different mechanism from characteristic-prime period loss: distinct, prime-to-characteristic spatial factors can disappear simultaneously. The explicit primitive-count formula and product formula determine the exact size of this extinction sector, including dependence on lattice arithmetic, and provide a reproducible benchmark for studying symmetry traps under equivariant dynamics. These are natural structural questions, not an arbitrary single ring or a numerical small gain.

## Limits and closest literature

The theorem requires \(p\nmid n\); the semisimple criterion does not purport to handle resonant ring lengths, other target patterns or nonlinear updates. The paper of Banda–Caughman–Lehman is the direct motivator; Ninagawa and Barbè–von Haeseler are narrower/different observables. Historical general linear-cellular-automata literature is extensive, and independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
