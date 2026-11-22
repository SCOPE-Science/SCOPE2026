# Arbitrarily high adaptive entropy despite instantaneous frozen mixing and a unique attracting equilibrium

## Finding

For every integer \(m\ge2\), there is a continuous, piecewise-affine family of **strictly positive two-state Markov kernels** and a fixed, uniformly \(1\)-strongly convex quadratic observation loss whose unit-step coupled distribution–parameter dynamics has all of the following properties:

1. Every frozen Markov kernel sends **every** starting distribution to its unique stationary distribution in exactly one step; all transition probabilities lie in \([1/8,7/8]\).
2. There is exactly **one** adaptive equilibrium, and it is locally exponentially attracting.
3. A compact invariant subsystem has **exact topological entropy** \(\tfrac12\log m\). In particular the entire adaptive map has entropy at least \(\tfrac12\log m\), with no finite uniform bound as \(m\) varies.

The entropy conclusion is about the deterministic coupled evolution of the *probability distribution and the controller*, not randomness along a sample trajectory of a frozen two-state chain.

## Assumptions and scope

Write \(x\in[0,1]\) for the probability of state \(1\) and \(\theta\in[0,1]\) for the controller. Put
\[
L=[1/8,1/4],\quad R=[3/4,7/8],\quad a=1/8,\quad b=1/4,\quad c=3/4,\quad d=7/8.
\]
Define \(q_m:[0,1]\to[1/8,7/8]\) by the following continuous piecewise-affine recipe. On \(L\), partition into \(m\) equal closed intervals \(L_j=[a+(b-a)j/m,a+(b-a)(j+1)/m]\), indexed \(j=0,\ldots,m-1\). On each \(L_j\), let \(q_m\) map affinely onto \(R\), increasing if \(j\) is even, decreasing if \(j\) is odd. On \(R\), put \(q_m(t)=1-t\). On \([0,a]\) put \(q_m(t)=c\), and on \([d,1]\) put \(q_m(t)=a\). On \([3/8,5/8]\), put
\[
q_m(t)=1/4+t/2.
\]
Fill the two remaining intervals \([b,3/8]\) and \([5/8,c]\) by the affine interpolants between their already prescribed endpoint values. The formulas agree at all endpoints and make \(q_m\) continuous; the parity of \(m\) affects only the left interpolant endpoint.

For each \(\theta\), let the two-by-two transition matrix \(P_\theta\) have both rows equal to \((1-q_m(\theta),q_m(\theta))\). For observation \(i\in\{0,1\}\) use loss \(\ell(i,\theta)=\tfrac12(\theta-i)^2\). Take the deterministic averaged-gradient step \(\delta=1\), without projection (the map preserves the controller interval). Explicitly,
\[
G(x,\theta)=\theta-x,\qquad
(x',\theta')=(q_m(\theta),\theta-G(x,\theta))=(q_m(\theta),x)=:F_m(x,\theta).
\]
The state space is the compact square \([0,1]^2\), and entropy uses the usual compact-space topological entropy of continuous maps.

## Proof

**Frozen maximal mixing.** For fixed \(\theta\), multiplying any row probability \((1-x,x)\) by \(P_\theta\) yields \((1-q_m(\theta),q_m(\theta))\), independently of \(x\). Hence the stationary distribution is unique and reached in a single transition; all entries are between \(1/8\) and \(7/8\). Every frozen instantaneous loss has \(\partial_\theta^2\ell=1\).

**Unique attracting equilibrium.** On \([0,1/2)\), \(q_m(t)>t\): this holds on \(L\) because \(q_m(L)=R\), on \([0,a]\) by constancy, and on \([b,3/8]\) by interpolation between two strictly positive endpoint differences. On \([3/8,1/2)\) it follows from \(q_m(t)-t=1/4-t/2>0\). By the symmetric endpoint-difference argument, \(q_m(t)<t\) on \((1/2,1]\). At \(t=1/2\), \(q_m(t)=t\). Therefore \(q_m\) has exactly one fixed point, \(t=1/2\), and \(F_m(x,\theta)=(x,\theta)\) holds exactly at \((1/2,1/2)\). Near this point the Jacobian is
\[
D F_m=\begin{pmatrix}0&1/2\\1&0\end{pmatrix},
\]
whose eigenvalues are \(\pm1/\sqrt2\). Thus the unique equilibrium is locally exponentially attracting.

**High-entropy subsystem.** Put \(K=L\cup R\), a compact invariant set for \(q_m\), with \(q_m(L)=R\) and \(q_m(R)=L\). Since \(q_m|_R(t)=1-t\), the second iterate \(q_m^2|_L\) has exactly \(m\) full affine branches from each \(L_j\) onto \(L\), with absolute slope \(m\). The standard separated-itinerary estimate gives
\[
h_{\rm top}(q_m^2|_L)=\log m.
\]
For completeness, an exact elementary argument uses the \(m^n\) monotonic full branches of \((q_m^2)^n|_L\). Their lap growth gives the lower entropy bound, while the uniform Lipschitz bound \(m\) for \(q_m^2|_L\) gives the reverse bound (e.g. through Bowen separated sets). The restrictions \(q_m^2|_L\) and \(q_m^2|_R\) are conjugate by the affine homeomorphism \(q_m|_R:R\to L\). Therefore the entropy of \(q_m^2|_K\) is \(\log m\), and the iterate identity yields \(h_{\rm top}(q_m|_K)=\tfrac12\log m\).

Finally,
\[
F_m^2(x,\theta)=(q_m(x),q_m(\theta)).
\]
The compact set \(K\times K\) is invariant under \(F_m\); by product additivity and the iterate identity,
\[
h_{\rm top}(F_m|_{K\times K})
=\tfrac12 h_{\rm top}((q_m|_K)\times(q_m|_K))
=h_{\rm top}(q_m|_K)=\tfrac12\log m.
\]
Monotonicity of entropy under restriction gives the asserted lower bound for the full adaptive map.

## Verification

The independent exact-rational program `CHECK.py` verifies the construction's endpoint continuity, ranges, strict fixed-point sign at every affine breakpoint, the central derivative, each second-iterate branch's two endpoint images, and explicit primitive \(2k\)-periodic witnesses for \(2\le m\le18\), \(1\le k\le8\). The program uses \(\mathbb Q\), not floating-point numerical approximations, and reports the number of checks. These finite checks support the formulas but are not a proof for unbounded \(m\); the full-branch and fixed-point arguments above prove the infinite statement.

## Relationship to prior work

Galatolo and Lippi (2026) define the same type of coupled frozen-Markov transfer / averaged-gradient update and establish equilibrium reduction and local convergence for sufficiently small positive learning rates. Their paper also describes finite-rate oscillations numerically; it does not state this maximal-mixing/unbounded-entropy result. Piliouras and Yu (2022) already establish Li–Yorke chaos in performative prediction, even for a single agent at sufficiently large influence; therefore **chaos itself is not a novelty claim here**. The distinct quantitative assertion is unbounded *topological entropy in a two-state system with one-step exactly mixing frozen kernels*, despite uniform frozen convexity and a unique *locally attracting* equilibrium. Known general full-branch interval-map entropy formulas are used as standard tools and are not claimed as new.

## Limitations

The kernel family is continuous piecewise affine, not differentiable at finitely many controller values, and its parameter sensitivity grows with \(m\). Thus uniform positivity and instantaneous frozen mixing do not imply any uniform parameter-Lipschitz bound. The result does not assert that the unique equilibrium attracts almost all initial conditions, nor does it compute the entropy of the *entire* square (only an exact invariant-subsystem entropy and a global lower bound). The example uses an infinite-batch expected gradient and unit learning step, not stochastic finite-sample gradient descent. It does not rule out global stability under the stronger small-feedback hypotheses of the literature. Historical priority of an equivalent explicit embedding remains a risk.

## References

1. S. Galatolo and V. Lippi, *Autonomous Neural Adaptive Control as a Self-Consistent Transfer Operator*, arXiv:2611.15649v1 (first posted 2026-11-11), https://arxiv.org/html/2611.15649v1.
2. G. Piliouras and F.-Y. Yu, *Multi-agent Performative Prediction: From Global Stability and Optimality to Chaos*, arXiv:2201.10483v1 (first posted 2022-01-25), https://arxiv.org/html/2201.10483v1.
3. Standard topological-entropy identities for iterates, products, invariant subsets and full-branch interval maps (used in the proof, not asserted as new).
