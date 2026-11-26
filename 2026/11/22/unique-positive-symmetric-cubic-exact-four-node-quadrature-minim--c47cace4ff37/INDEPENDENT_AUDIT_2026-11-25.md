# Independent mathematical audit

## correctness

PASS

For pointwise Jordan BV, decompose into two monotone functions whose variations sum to the total; layer sets are open or closed tails, so both one-sided CDF discrepancies are needed and their maximum is the exact dual norm. Reflection and the ordered offsets give max(1/2-b,b-v,v-a,a). Formal intermediate jumps at coincident nodes lie between the actual one-sided limits since the weights are nonnegative; endpoint jumps and zero weights are covered. Each actual atom weighs at most 2d, so d>=1/8. Cubic exactness reduces to the centered second moment 1/12. If d<=d*, the discrepancy bounds give a<=d, b<=3d, b>=1/2-d>d, and v>=b-d. Substitution bounds the moment by b^2-2(b-d)(b^2-d^2), strictly increasing in b up to 3d since d<1/7. The resulting 9d^2-32d^3 is strictly increasing from 1/8 to 1/7 in the argument d. Equality forces (a,b,v)=(d*,3d*,2d*), which is admissible and has discrepancy d*. Both strict-tail steps have error -d*. Reviewed the frozen checker as text, including its optional Gauss comparison. The independent replay `python /workspace/branches/review_recomputation.py` uses exact rational signs at the bracket endpoints and computes d*=0.132165520748966582568063 and Gauss discrepancy 0.169990521792428132401333. Those computations support the displayed numbers, not the universal proof.

## originality

PASS

Best of the inspected evidence, the moment-constrained four-node extremizer is distinct. The classical BV-discrepancy equivalence and neighboring three-node and Gaussian comparisons are not credited as new. The closest inaccessible literature leaves a bounded historical priority risk, not evidence of coverage.

## value

PASS

This determines the exact BV robustness cost of retaining the first nontrivial even moment under a natural symmetric four-evaluation budget. The unconstrained midpoint design attains 1/8 but has centered second moment 5/64 rather than 1/12; the sharp moment envelope quantifies the obstruction and identifies its only saturating admissible design. This is useful without suggesting a general improvement over Gauss rules when higher-degree exactness matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
