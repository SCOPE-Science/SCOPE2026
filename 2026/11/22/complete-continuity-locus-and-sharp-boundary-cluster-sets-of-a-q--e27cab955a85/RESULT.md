# Complete continuity locus and sharp boundary cluster sets of a quadratic knapsack limiter

## Finding

Fix an integer \(n\ge 1\) and strictly positive box caps \(u=(u_1,\ldots,u_n)\). For \(a\in\mathbb R^n\) and \(b\in\mathbb R\) define
\[
T_u(a,b)=\underset{0\leq\theta\leq u,\ a^{\mathsf T}\theta\geq b}{\operatorname{argmin}}\ \frac12\|\theta\|_2^2,
\qquad m_u(a)=\sum_{a_i>0}u_i a_i.
\]
The data domain is exactly \(\mathcal F_u=\{(a,b):b\le m_u(a)\}\), and \(T_u\) is single-valued throughout this domain. Set \(Z(a)=\{i:a_i=0\}\). The following assertions hold with \(u\) held fixed:

1. **Complete continuity criterion.** Relative to \(\mathcal F_u\), the map \(T_u\) is continuous at \((a,b)\) if and only if either \(b<m_u(a)\), or \(b=m_u(a)\) and \(Z(a)=\varnothing\). Equivalently, its complete discontinuity set is \(\{(a,b):b=m_u(a),\ Z(a)\ne\varnothing\}\).
2. **Exact boundary cluster set.** At every point with \(b=m_u(a)\), all possible limits of \(T_u(a^{(k)},b^{(k)})\) along feasible data converging to \((a,b)\) constitute precisely the full face
\[
\mathcal C_u(a)=\left\{q\in[0,u]:q_i=u_i\ (a_i>0),\ q_i=0\ (a_i<0),\ 0\le q_i\le u_i\ (a_i=0)\right\}.
\]
Consequently the sharp largest limiting Euclidean jump from the value \(T_u(a,b)\) is
\[
\sup_{\substack{(a^{(k)},b^{(k)})\to(a,b)\\(a^{(k)},b^{(k)})\in\mathcal F_u}}
\limsup_k\|T_u(a^{(k)},b^{(k)})-T_u(a,b)\|_2
=\left(\sum_{i\in Z(a)}u_i^2\right)^{1/2}.
\]
3. **Fixed-threshold strengthening.** If \(b=m_u(a)>0\), every point of \(\mathcal C_u(a)\) can already be obtained while keeping \(b^{(k)}=b\) fixed. At the corner \(b=m_u(a)=0\), changing \(b\) can be essential.

In particular, for \(u=(1,1)\), \(b=1\), and \(a_0=(1,0)\), one has \(T_u(a_0,1)=(1,0)\), whereas
\[
T_u((1-\varepsilon,\varepsilon),1)=(1,1)
\quad(0<\varepsilon<1).
\]
Even along **strictly feasible** perturbed problems, one has
\[
T_u((1-\varepsilon/2,\varepsilon),1)=(1,1/2)
\quad(0<\varepsilon\le2/5).
\]
Thus the solution can jump by order one under vanishing input perturbations despite a strictly convex smooth objective and unique minimizers. Two coordinates are minimal for this phenomenon with a fixed positive threshold.

## Assumptions and scope

The caps \(u_i\) are fixed, finite and strictly positive. Data \((a,b)\) may vary jointly over the **feasible** domain \(\mathcal F_u\); no unfeasible-data optimizer is defined. The minimization has one scalar linear inequality and coordinatewise box bounds. The theorem describes the solution as a function of the optimization inputs, rather than claiming that every abstract input configuration is attained by a particular discretized PDE trajectory. Primary mathematical setting: parametric convex quadratic programming and limiter sensitivity.

## Proof

**Existence and uniqueness.** The maximum of \(a^{\mathsf T}\theta\) over \([0,u]\) is \(m_u(a)\); hence feasibility is equivalent to \(b\le m_u(a)\). The feasible subset is compact and convex. Strict convexity of the squared Euclidean norm gives a unique minimizer. When \(b\le0\), \(\theta=0\) is the minimizer. For \(b>0\), a sufficient optimality certificate is a multiplier \(\lambda\ge0\) with
\[
q_i=\min(u_i,\max(0,\lambda a_i)),\qquad a^{\mathsf T}q=b.
\]
Indeed, \(q\) uniquely minimizes \(\frac12\|\theta\|^2-\lambda a^{\mathsf T}\theta\) on the box, and feasibility of any competing \(\theta\) gives \(\frac12\|\theta\|^2\ge\frac12\|q\|^2\). This certificate also works for the explicit constructions below even at boundary data.

**Continuity strictly inside feasibility.** Fix \((a,b)\) with \(b<m_u(a)\). Choose a box vertex \(v\) maximizing \(a^{\mathsf T}v=m_u(a)>b\). For any \(y\) feasible at the base data, the interpolant \(y_t=(1-t)y+tv\) has strict constraint slack whenever \(0<t\le1\). If feasible data \((a^{(k)},b^{(k)})\) approach \((a,b)\), each fixed \(y_t\) is feasible for all sufficiently large \(k\). The minimizers \(q^{(k)}\) lie in a common compact box. Every subsequential limit \(q\) is feasible at the base data and, using minimality against \(y_t\), obeys \(\|q\|^2\le\|y_t\|^2\). Letting \(t\downarrow0\) and taking \(y=T_u(a,b)\) shows that \(q\) is the unique base minimizer. All subsequences have that same limit; continuity follows.

**Boundary and outer inclusion.** Let \(b=m_u(a)\). The feasible set at the base data is exactly \(\mathcal C_u(a)\): every positive coefficient must use its upper cap, every negative coefficient must use zero, and zero-coefficient coordinates are unrestricted. The minimum-norm member \(q^0=T_u(a,b)\) sets the zero-coefficient coordinates to zero. For any converging feasible data, a cluster point \(q\) of the minimizers satisfies \(a^{\mathsf T}q\ge b=m_u(a)\), so necessarily \(q\in\mathcal C_u(a)\). This proves the outer inclusion of the claimed cluster set.

**Attainment of every point of the face.** Fix \(q\in\mathcal C_u(a)\), write \(Z=Z(a)\), and put \(S=\sum_{j\in Z}q_j^2\).

If \(m_u(a)>0\), choose an index \(i\) with \(a_i>0\). For small \(\varepsilon>0\), define \(a^{\varepsilon}\) by
\[
a_i^{\varepsilon}=a_i-\varepsilon S/u_i,
\qquad a_j^{\varepsilon}=\varepsilon q_j\quad(j\in Z),
\]
and leave all other coefficients unchanged; keep \(b^{\varepsilon}=b\). For sufficiently small \(\varepsilon\), every originally positive coefficient remains positive. The exact identities
\[
q=\operatorname{clip}_{[0,u]}(a^{\varepsilon}/\varepsilon),
\qquad (a^{\varepsilon})^{\mathsf T}q
=m_u(a)-\varepsilon S+\varepsilon\sum_{j\in Z}q_j^2=b
\]
give the certificate above with \(\lambda=1/\varepsilon\). Thus \(T_u(a^{\varepsilon},b)=q\) for **every sufficiently small** \(\varepsilon\), and \(a^{\varepsilon}\to a\).

If \(m_u(a)=0\), all \(a_i\le0\). Set \(a_j^{\varepsilon}=\varepsilon q_j\) on \(Z\), retain all negative coordinates, and choose \(b^{\varepsilon}=\varepsilon S\). Again the clipped-vector identity with \(\lambda=1/\varepsilon\) and the exact equality \((a^{\varepsilon})^{\mathsf T}q=b^{\varepsilon}\) certify \(T_u(a^{\varepsilon},b^{\varepsilon})=q\). This proves the reverse cluster-set inclusion.

**Continuity criterion and sharp jump.** At any boundary point the cluster set is the product face \(\mathcal C_u(a)\); it is a singleton exactly when \(Z=\varnothing\). This, together with interior continuity, proves the if-and-only-if criterion. The Euclidean distance from \(q^0\) to a member of the face is \((\sum_{j\in Z}q_j^2)^{1/2}\), maximized when all zero-coefficient coordinates equal their caps. That maximizer is attained along explicit data paths, proving the sharp bound.

**Two-dimensional strict-feasibility path.** For \(a=(1-\varepsilon/2,\varepsilon)\), \(b=1\), \(u=(1,1)\), take \(q=(1,1/2)\) and \(\lambda=1/(2\varepsilon)\). The second clipped coordinate equals \(1/2\); the first clips to 1 when \(\varepsilon\le2/5\); and \(a^{\mathsf T}q=1\). Meanwhile \(m_u(a)=1+\varepsilon/2>1\). This certifies the announced strictly feasible jump. In one dimension with \(b>0\) fixed, a feasible boundary requires \(a>0\), hence has no zero coefficient and cannot produce this discontinuity.

## Verification

The accompanying `verify.py` uses only the standard library and exact rational arithmetic. Run `python3 verify.py` in the directory containing this file. It checks the fixed-threshold discontinuity, the strict-feasibility path, a large finite family of prescribed cluster-face points with mixed signs and multiple zero coefficients, the zero-margin case, and a sharp maximal jump. Every nontrivial constructed solution is checked by exact primal equality and the clipped-multiplier certificate, **not** by a numerical optimizer or tolerance. Observed result: `VERIFY_OK 3512 exact_rational_checks`. The arbitrary-dimensional continuity and cluster-set conclusions are proved above, not inferred from these finite checks.

## Relationship to prior work

Christner and Chan, *Entropy Stable Nodal Discontinuous Galerkin Methods via Quadratic Knapsack Limiting*, arXiv:2507.14488, §3.2, introduce precisely the box/halfspace minimum-norm problem, establish the clipped-multiplier solver and state that its solution is continuous in the input parameters. Their displayed examples vary parameters away from the vanishing-coefficient feasibility boundary. The present theorem delimits that qualitative statement: continuity is valid in the strict-feasibility region and at nondegenerate boundary points, but fails at exactly the stated zero-coefficient boundary points. The solver reduction and smoothness of the objective remain valid and are not disputed.

The public `QuadraticKnapsack.jl` README describes the same continuous quadratic-knapsack structure, with optional positive objective weights, but presents an algorithm rather than a parametric solution-map classification. Lee, Tam and Yen (2006) study quadratic-program solution continuity under *linear-part* perturbations, a different parameter regime that does not hold the constraint-normal vector fixed in the present problem. A standard box/halfspace projection reduction already establishes the clipped-multiplier formula; the novelty claim here is confined to the precise feasibility-boundary discontinuity locus, full attainable cluster face, and sharp jump for this limiter family. These statements may be viewed as a special explicit sensitivity theorem in the broad framework of parametric optimization; no claim is made to priority for the general phenomenon of loss of constraint qualification.

## Limitations

All box caps are fixed positive numbers; varying or vanishing caps are not classified. The theorem concerns the optimization map's inputs and does not establish an actual PDE trajectory crossing a discontinuity or any loss of time accuracy in a specific DG implementation. Along individual solution trajectories, the feasible-data domain may obey additional restrictions absent here, and a positive feasibility margin prevents the classified jump. The result does not replace or refute the paper's entropy conservation, positivity bounds, solver algorithm or empirical numerical performance. No independent audit has been performed.

## References

1. B. Christner and J. Chan, *Entropy Stable Nodal Discontinuous Galerkin Methods via Quadratic Knapsack Limiting*, arXiv:2507.14488, original public version July 19, 2025, revision November 4, 2026, especially §3.2, Eq. (3.9), Theorem 3.3. https://arxiv.org/abs/2507.14488 ; readable PDF: https://arxiv.cnoctave.top/pdf/2507.14488
2. *QuadraticKnapsack.jl*, public package README, https://github.com/atEchoOff/QuadraticKnapsack.jl .
3. G. M. Lee, N. N. Tam and N. D. Yen, *Continuity of the Solution Map in Quadratic Programs under Linear Perturbations*, Journal of Optimization Theory and Applications **129** (2006), 415–423. https://doi.org/10.1007/s10957-006-9076-x . The accessible abstract does not provide a full-text equivalence check.
4. *Orthogonal Projection onto the Intersection of a Box and a Half Space*, Mathematics Stack Exchange discussion, July 16, 2024, https://math.stackexchange.com/questions/4946681/orthogonal-projection-onto-the-intersection-of-a-box-and-a-half-space . Discusses the standard clipped-multiplier representation, not the claimed boundary sensitivity classification.
