# Independent mathematical audit

## correctness

PASS

For x>=y>=0 the first folded component is x-h(y). Subtracting the second component yields either x-y+h(x)-h(y) or (x-h(x))+(y-h(y)), both nonnegative. Applying the ordered formula twice gives x-h(y)-h(|y-h(x)|). The subtracted sum is at least a(y+|y-h(x)|)>=a h(x)>=a²x. One-step nonincrease handles odd horizons. For h(t)=at, the boundary orbit maps (x,0) to (x,ax) and then ((1-a²)x,0), including a=1 with the zero-exponent convention. Continuity gives the positive-start supremum. For softplus, h(epsilon t)/epsilon tends to t/2 uniformly on bounded t; the rescaled starts (1,epsilon) and their fixed finite iterates stay bounded by the one-step estimate and converge to those of the linear corner orbit. At nonzero x, h(x)>x/2 makes the two-step estimate strictly smaller; at n=1 and positive inputs h(y)>0. In physical coordinates inverse logit has derivative at most 1/4; Satur's actual recurrence agrees exactly at alpha=2. The statement is toward the origin, not pairwise contraction.

## originality

PASS

The known fold and the local 3/4 mechanism are not new. The supported distinction is the sharp global every-horizon norm bound under a full interval of incremental slopes, together with its fixed-softplus specialization; neither geometric area decay nor the earlier orbit asymptotics supplies that uniform upper bound.

## value

PASS

The critical convergence problem needs a starting-state error certificate rather than an eventual orbit-by-orbit asymptotic. The estimate is usable at every horizon, is unimprovable even for the fixed smooth model, and identifies the sharp loss under only monotonicity and incremental slopes, including nondifferentiable feedbacks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
