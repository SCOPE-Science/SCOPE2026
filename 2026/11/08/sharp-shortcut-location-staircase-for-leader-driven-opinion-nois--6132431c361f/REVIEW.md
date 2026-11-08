# Review of shortcut placement in leader-follower opinion paths

## Correctness (PASS)

The follower-grounded path Green matrix is directly verified by multiplication: its entries are \(\min(i,j)\). A rank-one Laplacian update gives the exact aggregate-variance reduction. The discrete differences are linear in the extra conductance, with strictly ordered positive threshold values; this proves the complete global optimizer and all exceptional ties without relying on experiments. Uniform rescaling of the closed-form formula and an elementary single-maximum derivative analysis prove the macroscopic transition. The fixed-strength large-path limit gives residual fraction \(1/4\). A standalone exact-rational verifier independently inverts the updated matrices and checks 60,096 identities and maximizers. Its finite range is corroborative, not a replacement for the all-size proof.

## Originality (PASS with priority risk)

The initiating 2023 primary paper by Xu and Zhang provides a general finite-conductance rank-one gain identity and greedy optimization algorithms. Its full relevant formulation, algorithm, and experiments do not supply the explicit rooted-path optimizer thresholds or their asymptotic law. A 2014 path leader-selection paper changes the leader set, not the attachment of a weighted edge to an existing leader. A 2023 grounded-Laplacian edge paper optimizes the smallest eigenvalue rather than aggregate variance. A 2026 grounded-path resistance work addresses degree-weighted aggregates, landmark selection, and removing an edge according to its public abstract, but its full text was not materially inspected; an implicit equivalent cannot be excluded. Semantic mathematical-result searches and accessible published research claims found no stronger covering theorem. These checks do not amount to global priority certification.

## Value (PASS)

The optimization problem is the one-edge exact instance of a published noisy social-network intervention model. All-size thresholds show that optimal social-contact placement depends sharply on contact strength; they prevent reliance on a universal location rule. The precise limiting attachment fraction and \(75\%\) reduction quantify a striking network-wide effect of only one intervention. These properties supply a benchmark for weighted-edge heuristics and for scaling intuitions about leader influence on sparse social networks. No arbitrary parameter slice or merely numerical observation is used.

## Scope and remaining scientific risks

The theorem assumes one noise-free leader, homogeneous unit path conductances, equal independent follower noises, and precisely one new weighted edge. No independent comparison across all possible related manuscripts has been performed. The 2026 grounded-path source is materially compared at abstract level only, leaving a specific possible-priority risk. No external certification is claimed.

Self-review: passed. Independent audit: not yet performed.
