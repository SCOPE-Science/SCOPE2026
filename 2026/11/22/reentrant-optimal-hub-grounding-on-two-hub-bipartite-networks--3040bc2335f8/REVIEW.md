# Review: Reentrant optimal hub grounding on two-hub bipartite networks

## Correctness — PASS

The grounded matrix is positive definite for any nonnegative budget allocation with positive total budget. Strict convexity in all individual diagonal gains establishes a unique unrestricted optimum, so bipartition symmetry forces gains to be constant within each part. The exact reciprocal eigenvalue decomposition gives
\[
F_q(x,y)=\frac1{q+x}+\frac{q-1}{2+y}+\frac{q+2+x+y}{2x+qy+xy}.
\]
Exact directional derivatives show that the peripheral-only boundary is never optimal, and that the hub-free boundary is optimal precisely when \(q(q-1)(B/q)\ge(2+B/q)^3\). The function \((t+2)^3/t\) has unique minimum 27 at \(t=1\), yielding hub reactivation exactly for integer \(q\ge6\). The limiting root equations give the two budget scales. The standalone checker passed 4,599 assertions; finite checks are corroboration, not the universal proof.

## Originality — PASS on inspected evidence, with residual risk

Lin, Fardad and Jovanović (arXiv:1302.0450) establish the trace-inverse objective and general leader-selection optimization framework. Zhou et al. (arXiv:1511.02012) address extremal-eigenvalue pinning speed rather than trace inverse. The related complete-bipartite heterogeneous-price result (2026 public note, inspected full result) maximizes the *smallest eigenvalue*, and the previously documented \(K_{2,q}\) cubic leader-allocation note addresses *discrete noise-free leader sets*. Neither has the continuous-gain trace-inverse KKT implication needed to give this exact two-threshold law. A previous star-network reentrance concerns a one-hub tree, whereas \(K_{2,q}\) is cyclic for \(q\ge2\). Unindexed literature can still contain an equivalent result; no absolute priority is claimed.

## Value — PASS

The natural two-hub complete bipartite network is a canonical redundant-bottleneck graph. Its independent continuous-gain noise-suppression objective exhibits a nonmonotone optimal support: two hubs turn off and then on as the budget increases, with a sharp first example at eight vertices and two different asymptotic budget scales. The complete classification is useful for control allocation and avoids numerical multidimensional convex solvers.

## Limitations

The result assumes unit graph-edge conductance, continuous independently adjustable diagonal gains, and one uniform unit price per actuator. It does not classify larger left bipartitions, heterogeneous prices, capped control, or fixed-cardinality perfect leaders. The calculations were checked here; independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
