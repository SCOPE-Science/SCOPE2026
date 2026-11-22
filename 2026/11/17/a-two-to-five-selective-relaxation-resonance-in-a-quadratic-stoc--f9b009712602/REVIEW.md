# Independent mathematical audit

## correctness

PASS

PASS. The coordinates t=x3 and s=x1−x2 make the exact simplex map triangular: t'=1−2t+5t²/4 and s'=δt²−2ts (δ=c−d). Scalar fixed-point equation has physical root t*=2/5 only (other root t=2), then s*=4δ/45 uniquely, including boundary δ=±3/4. For y=t−2/5∈[−2/5,3/5], y'=-y(1−5y/4), whose bracket stays positive. Two iterations give y_{n+2}=y_n[1−(25/16)y_n²(2−5y_n/4)], with the bracket in (0,1) for every y≠0 in the entire physical interval; hence y→0 globally, signs alternate, and inverse squares w_m=y_{2m}^{−2} have increments tending 25/4. Cesàro yields n y_n²→8/25 and the signed sqrt-n amplitude 4/(5sqrt2). Subtract K y from z=s−4δ/45 with K=−28δ/9, obtaining exact r' =−(4/5+2y)r+(100δ/9)y². Stable-convolution theory yields r=O(1/n) and nr→160δ/81 from the limiting affine recurrence. Consequently only K=±1, i.e. δ=∓9/28, cancel the corresponding x1 or x2 oscillation, giving n times deviation −20/63; δ coefficients are feasible with c,d≥0. At t0=2/5 the purely stable s-direction is geometric. Independently checked the symbolic identities and long finite trajectories (120000 iterations) at both special ratios. Source verifier also checks them; finite paths do not replace the two-step proof.

## originality

PASS

Best-of-knowledge PASS for the exact three-component asymptotic amplitude, universal transverse 1/n coefficient and selective 2:5 / 5:2 admissible cancellations in this Hardin–Rozikov non-Volterra map. Hardin–Rozikov's primary theorem at e=1/4 proves qualitative global convergence, but does not quantify the vector rates or identify inheritance ratios that annihilate a single coordinate's square-root term. Scalar critical flip theory already explains exponent 1/2 and is credited. General resonance normal forms might implicitly contain the mechanism but do not provide this model's coefficient classification without actual algebra.

## value

PASS

PASS. The coefficient ratio at which one physical species relaxes at order n^{-1} while the others oscillate at order n^{-1/2} is a concrete, model-intrinsic critical phenomenon, not a generic restatement of the flip exponent. The exact feasible 2:5 and 5:2 ratios, -20/63 constant and universal transverse 160δ/81 expose selective cancellation useful for interpreting critical stochastic population trajectories. The zero-critical-hyperplane exception is fully classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
