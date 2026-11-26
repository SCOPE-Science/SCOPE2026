# Independent mathematical audit

## correctness

PASS

With d open neighbors and s agreeing ones, the closed-neighborhood rule flips iff 2s≥d, increasing the cut by 2s−d. With hub fixed, a blade's optimal partition has k_i∈{a_i−1,a_i} for even r_i=2a_i (a_i≥1), or k_i=a_i for odd r_i=2a_i+1, including r_i=1. Out-of-range k_i can be corrected by choosing an active private vertex on the oversized side; this realizes a finite positive-probability path to the cut maxima from every state. At those maxima the odd-blade contribution 2k_i−r_i=−1, or a lower even level's −2, prevents hub flipping, since the hub needs 1+∑(2k_i−r_i)>0. It may flip only when all blades are even at the upper level, and then complements each agreeing set but leaves the levels unchanged. Hence the maximum-cut set is closed and almost surely reached (finite state space). For a fixed hub, each even blade's two-layer inclusion graph is connected by insert/delete exchanges, while every odd blade is individually frozen; the even-layer Cartesian product yields the exact class sizes and the odd choices and hub spin index the classes. In the all-even case the upper-level hub flips join the two hub-spin halves. The transitions reverse at equal probability 1/N, giving uniform stationarity on each class; an inactive-vertex self-loop establishes aperiodicity. Pascal's identity counts w_i per fixed hub and preserves this count under the one-vertex parity switch; it does not identify trajectories across graphs. In the all-even class the independent upper-layer fractions under stationarity give the claimed p_h. Kac recurrence applied to stationary directed transitions marked by a hub flip gives the event-to-event mean 1/p_h (not the residual time from a uniform observation instant). Starting from the stationary law conditioned on spin 0 gives density at most two at every step, so the union bound for 0→1 crossings is at most t p_h. Testing the hub-spin event gives TV≥1/2−t p_h; by convexity some point start is at least as far, proving the ceiling bound. A fresh finite check using all bit configurations, closed-neighborhood updates, cut sizes and closed strongly connected components matched six examples: in particular (4,4) has one class of 200 and hub flux 1/25, (4,5) has 20 classes of 10, (2,2,2) one class of 54 and flux 8/189, and (2,3) six classes of three. These checks are not the all-size proof. Frozen check_scc.py, check_local.py and captured outputs were inspected without executing them.

## originality

PASS

The supported contribution is the coupled arbitrary-size shared-hub classification, particularly mixed-parity pinning and exact fragmentation and flux for this family. It is not the monotonicity of the generic minority dynamics, the one-blade classification, the friendship-graph case by itself, or the general conductance method. Distinct indexed records cover parts of the story, not the full result in the compared statements.

## value

PASS

This is an exact attractor classification for a natural shared-articulation graph family, where global maximum cuts are not implied by cut monotonicity alone. One added vertex can freeze the hub and split the recurrent set into many distinct classes while preserving its labelled-state count. When there is no odd blade, the explicit crossing flux explains slow mixing as more blades are added; its product form is meaningful for heterogeneous cliques.

The dated certificate retains the supplied scientific assessment, sources and limitations.
