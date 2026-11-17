# Independent mathematical audit

## correctness

PASS

For dot u=0,dot z=sum_{edge}u_i u_j, F_h is exact and designed G_h scales u by 1+delta. With C_S(u) the cut quadratic, direct evaluation yields F-S=(-delta Q_Su,h C_S(u)) and F-H=(-delta Q_Su,0). Subtract old/new first-time-point defect at u=(1+delta)1 and u=1 to get errors (-delta^2 1_Sc,h(2delta+delta^2)b_G(S)) and (-delta^2 1_Sc,0). Orthogonal coordinate and scalar parts imply exact squared gap. At h=1 minimizing squared error over |S|=n/2 is precisely minimum bisection; NP membership and the standard min-bisection hardness premise yield NP-completeness, while cardinality-indexed rooted forest dynamic programming yields polynomial optimization. Independent rational direct propagation passed 240 test cases. Only two coarse intervals/one correction and coordinate projectors are covered.

## originality

PASS

PASS qualified. Tan-Xu-Zhang-Su already define both nonlinear projected parareal updates and prove general error order contrasts. They do not derive graph-cut exact-error identities, balanced-coordinate NP-hardness or the forest optimization frontier in their inspected full HTML. Classical minimum bisection is prior; the reduction embedding its objective in parareal error is not a mere restatement.

## value

PASS

PASS: projector choice is a genuine algorithmic design problem for projection-based parareal. An elementary smooth quadratic globally soluble ODE and a valid order-p coarse map already encode NP-complete coordinate selection, while forests give an exact tractable subclass; this is a meaningful mathematical obstruction and boundary, not a renamed graph-cut exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
