# Independent mathematical audit

## correctness

PASS

The stated equilibrium is mathematically correct for finite uncapped parallel links with positive affine slopes and the fleet's own-cost objective. The gradient components a_i+b_i(S_i+C_i) and a_i+b_i(S_i+2C_i) come from the asserted strictly convex potential. Its classwise variational inequalities sum to the potential minimization condition on the product of demand simplices; hence existence and uniqueness include boundary supports and zero-demand classes. Under L=S, H=S+2C the Hessian separates and the two nonnegative Wardrop solves satisfy L≤H by monotonicity at all demands, including activation ties. Independently, for 0<α<1 the equalities on used H and L can be checked directly: the fleet marginal cost is a_i+b_i H_i, and the selfish cost is the mean of a_i+b_i L_i and a_i+b_i H_i, each at least its corresponding Wardrop level and both equal to their levels on L_i>0. A positive L_i strictly increases by the higher demand, giving positive fleet flow there. At α=0 this is ordinary Wardrop, and at α=1 the fleet alone has marginal link cost a_i+2b_i C_i, so 2C=W(2D). In the two-road example the upper demand always uses both links; the lower demand stops using link 2 at 1−α=τ. Completing the total-cost square about F1=(τ+2β)/(2(1+β)) gives exactly min(τ,1−α)^2/[4(1+β)]. This is an all-parameter analytical check; the published rational checker was inspected, not executed, and is not needed for the proof.

## originality

FAIL

No explicit symmetric notation was located, but prior work covers the substance. Wan (2012), Eqs. (2.3)–(2.4) and Lemma 3.2, gives the classwise equilibrium inequalities, nested supports and strict ordering of the two marginal levels for the same game in the broader convex parallel-link setting. The frozen shifted-demand identities are an immediate algebraic consequence in the affine single-coalition case, not an independent uncovered classification; the appendix-like two-road example is a direct specialization and a quadratic completion. This is verified prior implication, not a conclusion from an unavailable source.

## value

FAIL

Two ordinary Wardrop solves are useful as an implementation shorthand. As a distinct mathematical finding, however, the frozen result is an immediate affine re-expression of the established composite-equilibrium conditions and support theorem. The two-link plateau and quadratic gap use only substitution in those thresholds and completing the square, and the record supplies no independent structural or exact quantitative remainder beyond that routine deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
