# Self-review

## Correctness — PASS

The exact stopped generator and moment recursions are verified directly, as is the coupling that orders hitting times by initial sign. The sharp necessity proof integrates a nonnegative weighted orientation difference and uses a uniform telegraph-martingale lower bound on quadratic-scale passage times. The sharp sufficiency proof employs a separate explicit Lyapunov function at each moment order and a compact-set regeneration argument. With existence established independently, the exact tail integral gives the coefficient induction and subleading sign gap. The accompanying executable checks 34 generator and algebraic identities and supplies bounded-domain numerical diagnostics. Those diagnostics do not replace the analytic infinite-domain arguments.

## Originality — PASS (qualified)

The 2024 primary study provides a general backward-moment recursion and the mean, while an earlier result already gives the second-moment threshold and its leading large-distance coefficient. The new assertion is the all-integer-order necessity and sufficiency for orders three and above, the explicit product for all high orders, and the first-orientation-gap asymptotic. The related passive Brownian logarithmic-potential first-passage distribution is not a finite-velocity-jump solution. Searches for the active logarithmic model, telegraph analogues, moment phase hierarchy, and parameter aliases in accessible scientific records did not locate a stronger published covering statement. No finite search certifies uniqueness or publication priority.

## Mathematical value — PASS

High first-passage moments test whether intermittent large excursions dominate fluctuations even when mean and variance are finite. The full \(\beta=2n-1\) threshold ladder is a natural physical classification and answers the higher-moment problem explicitly left open by the source's recursion. The positive orientation-gap coefficient also quantifies persistent launch-orientation information absent from the common leading moment. This is structural information, not a single unmotivated additional moment or mere reparameterization.

## Closest literature and limitations

Guéneau–Majumdar–Schehr, arXiv:2409.16951v1, Sections II.1 and IV plus Appendix B, supply the model, mean and formal recursion. Earlier result `e8413b50-16ce-49db-b2a6-b85eb1f6a2df` already establishes the second moment's threshold and large-start coefficient. Radice, arXiv:2307.12699v2, analyzes Brownian logarithmic-potential functionals rather than finite-speed RTP. An alternative general result for persistent walks or a less accessible indexing source might subsume the derived hierarchy; independent publication-priority examination remains necessary. The theorem assumes a fixed positive integer order, athermal velocities, constant flip rate and a strictly above-turning-point starting position.

Self-review: passed. Independent audit: not yet performed.
