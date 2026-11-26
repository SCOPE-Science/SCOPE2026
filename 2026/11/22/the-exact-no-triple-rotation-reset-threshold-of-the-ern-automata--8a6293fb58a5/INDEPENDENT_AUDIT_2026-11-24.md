# Independent mathematical audit

## correctness

PASS

Read RESULT.md:5–93 against the right-rotation action, left-to-right words and contiguous `aaa`. Initial rotations fix the full set, terminal rotations preserve rank, and adjacent `b`s collapse without creating `aaa`. The final rank-reducing `b` gives image 0. After the initial `b`, the domain is S of size N=n-1, and A=ab and B=aab are the stated block maps of costs 2 and 3. B acts as a two-step cyclic shift followed by identification of target 1 with 0; its full inverse on an interval duplicates the fiber over 0 and omits the fiber over 1. Exactly one of 0 and 1 is present only at r=0 (growth) or r=w (shrink), which gives the three endpoint cases, including the empty shrink at w=1. Independently, among nonwrapping width-preserving descents of distance r, a path with x one-steps and y two-steps costs (3r+x)/2. If r is odd one one-step suffices: put it first for odd w and last for even w. If r is even, zero one-steps suffices unless w is even and 2<=w<=r, when all two-steps must hit the forbidden shrinking edge. In that case two one-steps suffice, at the start and end. This gives exactly g_w(r). It is nondecreasing, so wrapping steps cannot improve the potential; at r=w>=2 the source potential is at most H_w and the shrink destination at least 3+H_w. Growth has equality by the H recurrence. Telescoping gives the global lower bound even on paths that wrap or shrink, and the descending path with growth only at endpoint 0 attains it. Adding the initial b and evaluating the parity sum gives the claimed floor; the n=3 witness `baab` has length four. Both included checkers were read, not run. Their previously recorded finite ranges are corroboration only; the all-order result does not depend on a numerical computation.

## originality

PASS

The exact even-order formula is materially covered by a distinct same-day record and is not credited as distinct content. All-order feasibility with rotation runs of two is also covered. The supported distinct contribution is exact optimal length at all odd orders plus a unified all-order inverse-interval optimality certificate and matching construction. The even theorem and the feasibility bound do not imply the odd optimum; intra-day priority and exhaustive historical priority are not certified.

## value

PASS

Forbidden consecutive rotations are a natural regular constraint in the canonical slow synchronization family. The result computes the optimum, and not merely a feasible schedule, at the previously unaccounted-for odd orders. The sharp potential converts the problem to a small interval geometry while proving global optimality against detours and shrink steps. This completes the natural parity classification and supplies an explicit optimal construction; it is not valued as a recomputation of the known even-only expression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
