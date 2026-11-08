# Scientific review: depth-driven influence cutoff in multiplex DeGroot chains

## Correctness — PASS

The stated matrices are row-stochastic, preserve uniform opinion vectors and yield the scalar one-direction chain recursion. Its first-layer coordinate is the probability that independent geometric sojourns in the successive topic layers have all ended by the specified time. This proves the exact convolution and binomial-tail claims without an approximation. For constant bridge rate, binomial CLT gives the Gaussian window; with rates in a fixed compact subset of \((0,1)\), Lyapunov CLT applies because all third moments are uniformly bounded and total variance is of order depth. Block triangularity supplies the exact characteristic polynomial, and a length-\(d\) Jordan block exists on the uniform-layer subspace. In the single-weak-bridge model, the other \(d-1\) waiting times obey the law of large numbers; the exceptional geometric wait yields the necessary-and-sufficient criterion \(d b_{1,d}\to\infty\) and the two exponential bottleneck limits. The bounded finite rational replay in `check.py` verifies the exact recursion and binomial reduction for small cases, not the asymptotic statements.

## Originality — PASS, with identified residual risk

The motivating acyclic multiplex DeGroot article establishes convergence and ultimate source-influence formulas, not the specific transient hierarchy-depth law or exact critical single-bridge phase transition. Related convergence-time work in DeGroot social networks uses community-network spectrum or asynchronous clocks rather than this synchronous, growing-depth chain. A 2020 hierarchical-influence paper concerns stochastic majority-rule, not the deterministic linear update. Classical birth-death/pure-birth probability and geometric/negative-binomial distributions plainly contain the calculational ingredients; no originality is attributed to those general methods. The mathematical contribution evaluated here is the combined *multiplex-network transient* result, its fixed spectral-radius delayed-response obstruction, and the exact bottleneck cutoff transition. A broader unindexed equivalent in absorbing Markov chains or hierarchy transfer remains a substantive risk; no independent literature certification is claimed.

## Value — PASS

The motivating acyclic multiplex framework assures eventual consensus but leaves a natural and consequential transient question: when does a remote, steady source reach the start of a long directed topic chain? The theorem quantifies a sharp \(O(d)\) delay and \(O(\sqrt d)\) transition window, proves why a depth-independent subdominant eigenvalue cannot serve as a uniform estimate, and identifies the precise \(1/d\) bridge scale separating concentrated and random macroscopic arrival times. The result gives a meaningful structural benchmark for hierarchical opinion exchange, while deliberately separating mathematical influence from empirical causation.

## Closest literature and limits

Zender et al., *DeGroot Dynamics on Multiplex Networks with Directed and Acyclic Interlayer Connectivities*, arXiv:2610.27198v1 (first public 19 October 2026): model and eventual consensus. *The Impact of Community Structure on the Convergence Time of Opinion Dynamics* (2017): different social graph spectral estimates. *The asynchronous DeGroot dynamics* (2024): different updating clocks. *Organisational Social Influence on Directed Hierarchical Graphs, from Tyranny to Anarchy* (2020): different majority-rule process. Diaconis–Saloff-Coste (2007): general Markov-chain separation cutoff background, not claimed new here.

The theorem assumes uniform within-layer initial states, row-stochastic nonnegative influence, acyclic chain interlayer structure, and one specified weak bridge for the sharp transition. It does not establish a generic limit for all multiplex networks. Finite exact checks are not infinite proofs. An independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
