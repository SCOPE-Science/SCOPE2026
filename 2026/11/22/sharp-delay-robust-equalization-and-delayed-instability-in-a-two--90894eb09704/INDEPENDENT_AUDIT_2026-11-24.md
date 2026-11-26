# Independent mathematical audit

## correctness

PASS

Subtracting and adding the two unnormalized weights gives v−β(1−v²)w/4 and 1+(2c−β)(1−v²)/4, with w the delayed imbalance. Each weight stays positive because c−β>−1 and each opposing share is less than one. For β<c the absolute recurrence is bounded by the window maximum times q=[4+β(1−ρ²)]/[4+(2c−β)(1−ρ²)]<1, where ρ<1 is the initial maximum. Each step is nonexpansive and every entry in the next full window is reduced by q. At β=c the two signed weights are 1−h_t and −h_t with 0<h_t<1 and the norm is nonincreasing. In an orbit beginning with norm M>0, equality |v_j|=M for j≥1 requires |v_{j−1}|=M with the same sign and v_{j−1−τ} of opposite sign and magnitude M. If j≥τ+1, successive immediate predecessors back to time zero contradict that delayed sign. This verifies the critical equality exclusion in the omega-limit proof: a limiting history of positive norm L would retain L in every forward window, impossible after 2τ+1 steps. To obtain exponential convergence there, write the characteristic equation as r^τ(r−A)=−H. For |r|≥1 the left modulus is at least 1−A≥H; at β=c equality requires r=1, which fails the equation. Thus the critical map is locally exponentially stable and the already globally convergent orbit eventually enters that neighborhood. For c<β<2c, at τ=0 the sole root is (4−β)/(4+2c−β) in (0,1). With ε=1/τ and r=exp(ε z), the root equation is e^z(e^{ε z}−A)+H=0. At ε=0 the root log[β/(2c−β)]+iπ has derivative −H≠0 and positive real part. Analytic continuation and expansion prove eventual instability at all sufficiently large integer delays with the stated first-order term.

## originality

PASS

The supported distinct part is the sharp global two-agent all-delay boundary, including the nonlinear critical case, for Satur's delayed own-share normalization. The recurrence's large-delay linear mechanism uses standard methods and is not asserted as a general delay theorem. Inspected prior models do not imply this nonlinear all-interior history statement.

## value

PASS

The model was already proposed with delayed feedback but explored numerically. A sharp boundary independent of finite lag, global convergence on the boundary, and demonstrable loss of linear stability beyond it answer a motivated qualitative question that static convergence and finite simulations cannot settle. The result does not offer an empirical prediction or assert a post-instability attractor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
