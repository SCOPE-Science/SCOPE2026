# Exact three-regime epidemic-size optimization for degree-one/three/five networks

## Finding

Consider independent bond transmission on a configuration-model contact network whose pre-transmission vertex degree \(D\) takes only values \(1,3,5\), with prescribed mean \(\mathbb E D=3\). All such laws have
\[
\mathbb P(D=1)=\mathbb P(D=5)=t,\qquad \mathbb P(D=3)=1-2t,\qquad 0\le t\le\tfrac12.
\]
The degree variance is exactly \(\operatorname{Var}(D)=8t\), so \(t\) is a mean-preserving heterogeneity knob spanning the entire family of distributions on the first three positive odd degrees. Retain each edge independently with probability \(T\in[0,1]\). Let \(\Xi(t,T)\) be the limiting fraction of vertices in the largest retained connected component. In the independent-transmission SIR interpretation, it is the final infected fraction conditional on a macroscopic outbreak, not the probability of such an outbreak and not the unconditional average from a single seed.

Define \(w_0\) as the unique root in \((1/2,1)\) of
\[
4w_0^3+w_0^2-1=0,
\]
and \(w_{1/2}\) as the unique root in \((1/2,1)\) of
\[
10w_{1/2}^6+5w_{1/2}^5+15w_{1/2}^4-5w_{1/2}-1=0.
\]
Put
\[
T_{\rm low}=\frac{6}{5(1+w_{1/2})(1+w_{1/2}^2)}
=0.503512762467307\ldots,\qquad
T_{\rm high}=\frac{1}{1+w_0}=0.642387380782454\ldots.
\]
The **complete global optimum** over every admissible \(t\) is:

- If \(0\le T\le 3/10\), then \(\Xi(t,T)=0\) for every \(t\), so all mixtures tie.
- If \(3/10<T\le T_{\rm low}\), then \(t=1/2\) is the unique maximizer.
- If \(T_{\rm low}<T<T_{\rm high}\), then a unique interior maximizer \(t_*(T)\in(0,1/2)\) exists; it is the unique solution of \(T=\mathcal T(t_*(T))\), where \(\mathcal T\) is explicitly defined below. It decreases continuously from \(1/2\) to \(0\) as \(T\) increases.
- If \(T_{\rm high}\le T\le1\), then \(t=0\) is the unique maximizer.

These cases include every equality boundary. Hence the degree spread which maximizes macroscopic epidemic size has exactly three positive-outbreak regimes: full, interior, and zero spread, with exact algebraic switching thresholds. This is optimization **within the stated odd-degree, mean-three family**, not among all degree laws.

## Assumptions and scope

The contact graph is the standard undirected configuration model on increasing vertex counts with an empirical degree distribution tending to the specified bounded-support law, with parity adjusted in the customary way. Edges are retained independently with a common probability \(T\). The result concerns the deterministic limit \(\Xi(t,T)\) of the largest retained component divided by vertex count; it does not assert exact formulas for a finite random graph, arbitrary dependent transmissions, degree correlations, or arbitrary degree distributions.

For \(0\le u\le1\), write
\[
G_0(u)=t u+(1-2t)u^3+t u^5=u^3+t u(1-u^2)^2,
\]
\[
G_1(u)=\frac{G'_0(u)}{3}=u^2+\frac t3(1-u^2)(1-5u^2).
\]
Let \(u=u(t,T)\) be the smallest solution in \([0,1]\) of \(u=1-T+TG_1(u)\). The standard configuration-model branching relation gives
\[
\Xi(t,T)=1-G_0(u(t,T)).
\]
This relation is established in the cited work on thinned configuration graphs and is used here as a premise; the optimization and its exact thresholds are proved below.

## Proof

**1. Epidemic onset and physical root.** The excess-degree mean is
\[
G_1'(1)=\frac{6+8t}{3}.
\]
Consequently the giant component exists precisely when \(T>3/(6+8t)\). The threshold is minimized over the permitted \(t\) at \(t=1/2\), where it equals \(3/10\).

For a nontrivial root \(u<1\), cancellation of \(1-u\) in the branching equation yields
\[
\frac1T=\Psi(u,t):=(1+u)\left(1+\frac t3(5u^2-1)\right).
\tag{1}
\]
Here
\[
\partial_u\Psi(u,t)=1+\frac t3(15u^2+10u-1)\ge\frac56>0
\quad(0\le u,t\le1,\ t\le1/2).
\]
Thus \(\Psi\) is strictly increasing in \(u\). At supercritical parameters equation (1) has one root in \([0,1)\), equal to the physical smallest branching root. At or below the percolation threshold, \(u=1\) and \(\Xi=0\).

**2. The exact derivative.** On the supercritical region implicit differentiation in (1) gives
\[
\frac{\partial u}{\partial t}=-\frac{\Psi_t}{\Psi_u},\qquad
\Psi_t=\frac{(1+u)(5u^2-1)}3.
\]
Since \(\Xi=1-u^3-tu(1-u^2)^2\), straightforward factorization yields
\[
\boxed{\frac{\partial\Xi}{\partial t}=\frac{(1+u)P(u,t)}{3\Psi_u(u,t)}}
\tag{2}
\]
where
\[
P(u,t)=10tu^6+5tu^5+(12-9t)u^4+(3-6t)u^3+(t-3)u-t.
\tag{3}
\]
The identity follows exactly by expanding
\[
-u(1-u^2)^2\Psi_u+\bigl(3u^2+t(1-6u^2+5u^4)\bigr)\Psi_t
=\frac{1+u}{3}P(u,t).
\]

**3. Exactly one stationary crossing at each degree spread.** For every \(t\in(0,1/2]\), the nonzero polynomial coefficients of \(P(\cdot,t)\), in descending order, have one sign change: the coefficients at powers \(6,5,4\) are positive, that at power \(3\) is nonnegative, and the coefficients at powers \(1,0\) are negative. Descartes' rule therefore gives precisely one positive root, counted with multiplicity. For \(t=0\), \(P(u,0)=3u(4u^3+u^2-1)\) also has exactly one positive root. Moreover
\[
P(1/2,t)<0,\qquad P(1,t)=12>0.
\]
Write \(z(t)\in(1/2,1)\) for this unique simple positive root. The factorization
\[
\partial_tP(u,t)=(u^2-1)Q(u),\quad
Q(u)=10u^4+5u^3+u^2-u+1>0
\tag{4}
\]
holds for \(0<u<1\), since \(Q(u)\ge u^2-u+1>0\). Hence \(P(\cdot,t)\) decreases strictly with \(t\) on \((0,1)\), so its sole positive root \(z(t)\) increases strictly and continuously on \([0,1/2]\).

Define the stationary transmission frontier
\[
\mathcal T(t)=\frac1{\Psi(z(t),t)}.
\tag{5}
\]
Because \(z(t)>1/2\), both \(\Psi_t(z(t),t)>0\) and \(\Psi_u(z(t),t)>0\). Therefore \(\mathcal T(t)\) decreases strictly and continuously with \(t\). At the two endpoints, \(P(z(0),0)=0\) and \(P(z(1/2),1/2)=0\) give precisely the displayed defining polynomials and
\[
\mathcal T(0)=T_{\rm high},\qquad \mathcal T(1/2)=T_{\rm low}.
\]

**4. Global optimization including the zero-outbreak region.** On the supercritical branch, \(P(u,t)\) has the sign of \(u-z(t)\). Since \(\Psi\) is increasing, equation (1) shows
\[
\operatorname{sgn}\frac{\partial\Xi}{\partial t}
=\operatorname{sgn}(\mathcal T(t)-T).
\tag{6}
\]
When subcritical, \(\Xi=0\) instead. For \(T>3/10\), the right endpoint \(t=1/2\) has strictly positive giant size. If \(T\le T_{\rm low}\), equation (6) makes \(\Xi\) strictly increasing wherever positive, and the unique maximum occurs at \(1/2\). If \(T_{\rm low}<T<T_{\rm high}\), the continuous strictly decreasing frontier \(\mathcal T\) crosses \(T\) once, yielding increase followed by decrease, and hence a unique interior maximum. If \(T\ge T_{\rm high}\), equation (6) makes \(\Xi\) strictly decreasing from \(t=0\); its unique maximum is \(0\). The endpoint equalities follow by the same one-sided monotonicity. Finally if \(T\le3/10\), no mixture is supercritical and all have zero giant size. This proves the theorem.

## Verification

The standalone standard-library Python program `verify.py` reproduces the branching-equation factorization, the differentiated polynomial identity, the parameter-slope identity, stationary-root brackets and numerical global maximizers. It also independently compares the physical branching root found from the canceled equation with fixed-point iterations of the original generating-function equation. Execution reports `PASS 26587 assertions` and numerical endpoints
\[
T_{\rm low}=0.503512762467308\ldots,\qquad T_{\rm high}=0.642387380782455\ldots.
\]
Exact rational identity checks and numerical sampling are consistency checks, not replacements for the all-parameter proof above.

## Relationship to prior work

Leibenzon and Assaf (2023) identify a qualitative transition in which network heterogeneity can enhance final SIR outbreak size; their analysis includes general generating functions, correlated networks and large-degree asymptotics. The present result deliberately isolates uncorrelated, independent-edge transmission, and proves the *complete exact global optimizer* on the bounded three-degree family with mean three, including two finite-degree algebraic thresholds. The paper's qualitative transition does not provide this all-parameter classification.

Britton and Trapman (2010 preprint; subsequently published) prove that an unrestricted fixed-mean maximizer for thinned configuration models can be chosen supported on zero and two consecutive positive degrees. Their global structure theorem does not order the constrained distributions supported precisely on \(1,3,5\), which exclude degree zero and all intermediate even degrees. Deijfen, Rosengren and Trapman (2017 preprint; subsequently published) derive broad component-size bounds and illustrate changing small-degree masses, without stating the present two-threshold all-transmissibility optimizer. The standard branching generating-function identity is prior work, not claimed as new.

## Limitations

This is a restricted-family optimization, not a statement that these degree distributions are globally optimal among all degree laws with mean three. It concerns the asymptotic giant fraction for independent bond transmission, not the unconditional expected outbreak from one initial infective, nor a finite-network expectation or a Markov infection process with correlated outgoing transmissions. The theorem does not identify optimal distributions once degrees other than \(1,3,5\) are admitted. Its priority is based on specified accessible sources and mathematical-record comparisons, not an exhaustive literature certification; independent review has not been performed.

## References

1. A. Leibenzon and M. Assaf, *Heterogeneity can markedly increase final outbreak size in the SIR model of epidemics*, first public arXiv version 15 June 2023, https://arxiv.org/abs/2306.09024 .
2. T. Britton and P. Trapman, *Maximizing the size of the giant*, first public preprint 4 October 2010, https://arxiv.org/abs/1010.0524 .
3. M. Deijfen, S. Rosengren and P. Trapman, *The Tail does not Determine the Size of the Giant*, first public preprint 3 October 2017, https://arxiv.org/abs/1710.01208 .
4. M. E. J. Newman, *Spread of epidemic disease on networks*, Phys. Rev. E 66, 016128 (2002), https://doi.org/10.1103/PhysRevE.66.016128 .
