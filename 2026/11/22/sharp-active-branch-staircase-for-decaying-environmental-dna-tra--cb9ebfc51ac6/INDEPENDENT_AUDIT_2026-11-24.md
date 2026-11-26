# Independent mathematical audit

## correctness

PASS

The passive-tracer benchmark assumes a constant source flux per active branch, not fixed inlet concentration or a fixed total source load independent of support. The transit-time scaling gives a=λℓA_c/Q, and g_a(0)=0 is the continuous extension. Compactness gives an optimizer. For a fixed pair total t>0, put b=a/t and r=(1-x)/x>1 for the normalized smaller share x. The log ratio of the positive derivative terms g_b'(x) and g_b'(1-x) is 2 log r-b(r-r^(-1)). Its sign is that of u/sinh(u)-b with u=log r. The ratio u/sinh(u) decreases strictly from 1 to 0 because u cosh(u)-sinh(u) has derivative u sinh(u)>0 and starts at 0. Thus as x increases toward 1/2, the pair objective either decreases throughout or first decreases and then increases; a noncentral interior stationary point is a strict minimum. Only the endpoints and equal split can maximize, with the pair tie at b=log 2. Unequal positive components in a simplex optimum would admit a strict pairwise improvement. Evaluating every equal k-support yields k exp(-ak), and the adjacent ratios ((k+1)/k)exp(-a) decrease strictly with k. Hence all the stated consecutive phases and only adjacent ties follow, with all optimizer permutations included. Replay: RESULT.md lines 27–49. The numerical checks in verify.py were inspected, not run. No empirical validation is inferred.

## originality

PASS

The inspected evidence covers the general optimization class and transport law, but supports the exact inverse-exponential equal-positive-support classification and its full logarithmic staircase as distinct. No historical-priority claim is made for sigmoidal resource allocation, eDNA attenuation, or the same-day analogues.

## value

PASS

The closed-form all-size staircase is a motivated structural benchmark for identical flow routes transporting a passive, first-order-decaying tracer. It answers when opening another route helps, whether a support count is skipped, and what happens at coexistence, none of which is given by a generic numerical solver or by the transport law alone. The equal-source-flux and fixed-geometry assumptions bound its interpretation; it does not prescribe management of natural rivers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
