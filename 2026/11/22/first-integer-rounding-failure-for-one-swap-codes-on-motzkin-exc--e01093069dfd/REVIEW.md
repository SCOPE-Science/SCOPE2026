# Independent mathematical audit

## correctness

PASS

An at-most-one swap preserves symbol counts, so both packings add over the number k of U steps, also the number of D steps. Independently reconstructed the allowed excursions using an extendable nonnegative-prefix recursion, and constructed every unchanged or swapped output without applying a prefix test to outputs. Rebuilt output incidence and checked all explicit codebook, rational primal and rational dual inequalities and objective equalities for the 19 layers. For the integer upper bounds, independently used memoized recursion on surviving sources: at a common output of two or more surviving sources a packing chooses either none or exactly one of those sources. In the chosen branch remove that source and every source intersecting its ball; when no such output remains all remaining sources are jointly feasible. The alternatives are exhaustive, and in all layers the resulting exact maximum matches the codebook size. Source counts are 1,2,4,9,21,51,127; M is 1,2,2,4,7,14,28 and P is 1,2,2,4,7,71/5,5515/182. At n=6 the gap is 1/5 and the floor still equals 14; at n=7 it is 30, strictly above 28. In the length-seven layers k=0,1,2,3 the integer maxima are 1,6,14,7 and the fractional maxima 1,6,2785/182,8. Replay: python3 /workspace/review-evidence/channels.py swap; see swaps.log in the same directory. This examines only single adjacent exchanges through length seven.

## originality

PASS

The exact Resultary hit on the full table is the assigned record itself. There is material partial coverage: the no-horizontal layers are the same as previously indexed Dyck swap layers, and an unrestricted multipermutation result uses the same channel for one host composition. The initial gap and the first floor failure need the layers with horizontal steps that those results do not determine. The literature comparison is bounded and not a priority assertion.

## value

PASS

The comparison isolates a practical distinction for exact coding bounds: the first nonintegral relaxation advantage is small enough to disappear under flooring, whereas at the next length the floor exceeds the best code by two. The complete preceding lengths and preservation of the genuine receiver alphabet make this a sharp boundary for the natural packing model, not merely a fractional example with a cherry-picked source subset. The composition data locate which types of paths cause the failure and give a benchmark for stronger upper bounds, without implying a larger-length law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
