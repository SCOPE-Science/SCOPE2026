# Independent mathematical audit

## correctness

PASS

Normalize the first three ordered markings to infinity, 0, 1. After the relabelling their values are 0, 1, u, so the normalizing map is x ↦ u(x−1)/((u−1)x). The fixed equation for the last marking sets v=u/(u−1); substituting into the other yields −(u²−u−1)/(u−1). In the quotient u(u−1)=1, v=u+1=u² and u−v=−1, so all the deleted factors remain units; this proves an equalizer, not merely an equation on geometric points. A stable genus-zero tree with five markings has at most two nodes, hence at most two boundary divisors through any geometric point, whereas every pair-of-labels divisor is in a free orbit of five. No boundary point can belong to the equalizer in any fiber. The quadratic is monic of rank two and has discriminant five; modulo five it is (u−3)². The Jacobian at (3,4) has rows (2,4) and (1,0) modulo five. Its nilpotent part has rank one and square zero. Conjugacy would identify the completed equalizers, but the tangent model fixes a formal line whereas the actual equalizer has local length two. Independently replayed elimination, the reduced Jacobian and boundary-label permutation with `python3 branches/independent_replay.py 5` from the workspace root.

## originality

PASS

The two complex fixed points and the order-five automorphism itself are established prior work. The supported distinct contribution is the entire integral equalizer with no boundary support, its isolated length-two fiber in characteristic five, and the resulting obstruction to formal linearization for this action. Earlier explicit coordinate maps make the elimination short, and the obstruction method is general, but the checked sources neither assert this invariant nor give a general fixed-scheme theorem whose specialization states it.

## value

PASS

For the canonical five-cycle on the split quintic del Pezzo surface, the integral equalizer is a natural invariant. It determines that the tame fixed points merge rather than disappear or enter the boundary, specifies the wild fixed algebra, and answers whether one can replace the wild local action by its linear representation. Neither the arithmetic degeneration nor the distinction between tangent and actual fixed dimensions is captured by just counting geometric points or quoting the automorphism group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
