# Sharp throughput-allocation switch in a bidirectional two-lane exclusion gas

## Finding

In a two-lane periodic exclusion process with a lane-symmetric, product-form invariant measure and positive forward/backward hopping rates, fix the uncoupled rightward bias to one. Let the signed additional bias per occupied site on the other lane be \(q/2\), with \(q\in\mathbb R\). If the two stationary lane densities \(u,v\in[0,1]\) can be chosen independently before operation, the maximal total **signed rightward stationary current** has an exact allocation switch.

Define
\[
F_q(u,v)=u(1-u)(1+qv)+v(1-v)(1+qu),\qquad
C(q)=\max_{0\le u,v\le1} F_q(u,v).
\]
Let \(q_*\) denote the unique real zero in \((-3/2,-1)\) of
\[
32q^3+85q^2+80q+32=0,
\qquad q_*=-1.357003205304976\ldots .
\]
For \(q\ne0\), put
\[
x_q=\frac{q-1+\sqrt{q^2+q+1}}{3q},\quad x_0=\frac12,
\qquad S(q)=2x_q(1-x_q)(1+qx_q).
\]
Then the exact capacity and *all* its maximizers are
\[
C(q)=\begin{cases}
1/4,&q<q_*,\\
1/4=S(q),&q=q_*,\\
S(q),&q>q_*,
\end{cases}
\]
with maximizer set \(\{(1/2,0),(0,1/2)\}\) below \(q_*\), these two points together with \((x_{q_*},x_{q_*})\) at \(q_*\), and only \((x_q,x_q)\) above \(q_*\). Thus optimal lane imbalance jumps from \(0\) to \(1/2\) at a sharp negative-coupling threshold. The capacity is continuous but has a corner: its left derivative at \(q_*\) is zero, while its right derivative is \(2x_{q_*}^2(1-x_{q_*})>0\). No dynamical spontaneous symmetry breaking is asserted; the switch concerns optimization over externally selected conserved densities.

## Assumptions and scope

There are two periodic rings with the same \(L\ge3\) sites, each with hard-core occupations \(\eta_i,\zeta_i\in\{0,1\}\), no interlane hopping, and independent occupation-number conservation. At a bond \((i,i+1)\), a particle on either lane jumps right/left into an empty site at strictly positive rates \(r(d)\) and \(\ell(d)\), where \(d\in\{0,1,2\}\) is the sum of the two occupations on the other lane at that bond. Assume
\[
r(d)-\ell(d)=1+qd/2.
\]
Every real \(q\) is realizable: choose \(R>\max_{d\in\{0,1,2\}}|1+qd/2|\) and let \(r(d)=(R+1+qd/2)/2\), \(\ell(d)=(R-1-qd/2)/2\). The symmetric parts of the rates affect fluctuations but not the mean stationary current. Stationary densities are externally specified and, because particle numbers are conserved, are not dynamically selected by this closed process. Current means signed right jumps minus left jumps per bond per unit time, summed across lanes; it is not the sum of absolute flux magnitudes.

The displayed \(F_q\) is exact in the product Bernoulli stationary ensemble on a periodic ring, not a mean-field approximation. For the uniform canonical sector containing exactly \(n\) and \(m\) particles on respective rings, the exact currents instead obey \(J_{1,L}=\frac{n(L-n)}{L(L-1)}(1+qm/L)\) and \(J_{2,L}=\frac{m(L-m)}{L(L-1)}(1+qn/L)\). At fixed rational-density sequences, their limit is \(F_q\), and the finite-volume factor is common to both lane contributions. Only the continuum density optimization on \([0,1]^2\) is classified; it is not claimed that the finite integer-grid maximizers equal the continuum maximizers for every \(L\).

## Proof

**Exact invariant measure and current.** Write the two lane occupations on one bond as \((\eta_i,\eta_{i+1})\) and \((\zeta_i,\zeta_{i+1})\). For a fixed configuration, the total outgoing-minus-incoming rate of lane-one moves on this bond is
\[
(\eta_i-\eta_{i+1})\left[1+\frac q2(\zeta_i+\zeta_{i+1})\right],
\]
and the corresponding lane-two contribution is the expression with \(\eta,\zeta\) interchanged. Summing these differences over all periodic bonds telescopes: the uncoupled terms sum to zero, while the cross terms sum to \(q\sum_i(\eta_i\zeta_i-\eta_{i+1}\zeta_{i+1})=0\). Therefore each fixed-particle-number sector has an invariant uniform distribution; strict positivity of both directions also makes it irreducible. Any mixture of these sector measures, including the independent Bernoulli product measure, is invariant. In that product measure \(\mathbb E[\eta_i(1-\eta_{i+1})]=u(1-u)\) and \(\mathbb E[(\zeta_i+\zeta_{i+1})/2]=v\), with independence between lanes, giving \(J_1=u(1-u)(1+qv)\), \(J_2=v(1-v)(1+qu)\). Sampling distinct sites without replacement instead gives the stated canonical correction.

**All global maximizers.** Set \(s=(u+v)/2\), \(d=(u-v)/2\). The feasible domain is \(0\le s\le1\), \(|d|\le\min(s,1-s)\), and exact expansion gives
\[
F_q=2s(1-s)(1+qs)+2\big[q(s-1)-1\big]d^2. \tag{1}
\]
For \(q\ge0\), the second coefficient is strictly negative, so the global maximizer lies on \(d=0\). For \(q<0\), a hypothetical interior maximizer with \(d\ne0\) would satisfy \(q(s-1)=1\) from the derivative in \(d\). At such a point the Hessian has \(\partial_{dd}F_q=0\) and \(\partial_{sd}F_q=4qd\ne0\), so its determinant is negative; it is a saddle, not a local maximum. Thus for negative \(q\) all maximizers lie on the diagonal or on the boundary of the density square. On \(u=0\) the current is \(v(1-v)\) and its unique maximum is \(1/4\) at \(v=1/2\); similarly on \(v=0\). On \(u=1\) or \(v=1\), the current is \((1+q)w(1-w)\), whose maximum is no greater than \(1/4\) for \(q<0\). The only boundary maximizers when the boundary capacity wins are therefore \((1/2,0)\) and \((0,1/2)\).

Along the diagonal the objective is \(f_q(s)=2s(1-s)(1+qs)\). It is positive on \(0<s<\min(1,-1/q)\) for \(q<0\), and on \(0<s<1\) for \(q\ge0\). On this positive interval the logarithm is strictly concave as a sum of \(\log s\), \(\log(1-s)\), and \(\log(1+qs)\), and the function vanishes at its endpoints. It therefore has one positive maximum. The derivative equation
\[
1-2s+q(2s-3s^2)=0
\]
gives exactly \(s=x_q\) as specified. Hence \(C(q)=S(q)\) for nonnegative \(q\) and \(C(q)=\max\{S(q),1/4\}\) for negative \(q\).

The function \(S(q)\) is strictly increasing in \(q\), because the objective at any interior maximizing density increases strictly with \(q\). As \(q\to-\infty\), positive diagonal flux requires \(s<-1/q\), so \(S(q)\to0\); also \(S(-1)=8/27>1/4\) and \(S(-3/2)<1/4\). Thus there is a unique crossing \(q_*\in(-3/2,-1)\). Eliminating \(s\) from the derivative equation and \(2s(1-s)(1+qs)=1/4\) gives
\[
q(32q^3+85q^2+80q+32)=0.
\]
The root \(q=0\) is extraneous to the simultaneous equations, since \(S(0)=1/2\); uniqueness of the crossing selects the stated cubic root. The strict Hessian argument and strict diagonal maximizer uniqueness give the complete optimizer sets. Finally the envelope derivative is \(S'(q)=2x_q^2(1-x_q)>0\), proving the one-sided corner claim.

## Verification

The file `verify_capacity.py` independently checks the polynomial identities, the elimination polynomial, every configuration in every two-lane particle sector for ring lengths \(L=3,4,5\) at seven rational couplings, and exact canonical currents from direct enumeration. It also tests a bounded dense grid of \(81\times81\) density pairs at twelve couplings on both sides of the threshold. Its recorded execution passed 88,775 deterministic checks. The proof, not the sampled grid, establishes the all-real-parameter optimization; the symbolic and enumerative checks guard against algebraic and normalization errors. Run `python verify_capacity.py` with Python 3 and SymPy; `requirements.txt` specifies the dependency.

## Relationship to prior work

Popkov's 2026 work [1] proves Bernoulli stationarity and the multi-lane current formula, explicitly allowing signed interaction parameters because backward rates are available. Those dynamical premises are used here, not claimed as new. The same current polynomial occurs in the one-directional family examined by Popkov and colleagues in 2015 [2], but when the baseline forward bias is fixed at one, nonnegative forward-only rates force \(q\ge-1\); the capacity switch is at \(q_*<-1\), inaccessible to that one-directional realization. The new assertion is a complete *optimization* classification of the expanded bidirectional parameter regime.

Spohn's 2025 preprint [3] concerns a different reflection-symmetric two-lane family with opposite directed mean currents and investigates flux-Jacobian degeneracies. Pronina and Kolomeisky [4] analyze boundary-coupled lanes and genuine boundary-induced stationary symmetry breaking, whereas the present result has homogeneous bulk interlane coupling and no stationary symmetry breaking: density allocation is chosen before a closed-system experiment. Neither supplies the stated signed-throughput capacity threshold.

## Limitations

There is no assertion of dynamic density selection or of a thermodynamic phase transition; the capacity kink is an optimal-design transition over conserved density sectors. The theorem optimizes signed total forward current, not entropy production, electrical work, absolute current, or throughput with fixed total particle number. It is not a finite-size discrete-grid classification, and it does not imply that open boundary reservoirs choose one of these densities. Mathematical originality is conditional on coverage by other relevant two-lane transport-optimization literature; no independent audit has been performed.

## References

1. V. Popkov, *Multilane Asymmetric Exclusion Process with stationary Bernoulli measure*, first publicly posted 7 May 2026, arXiv:2605.06949v1, https://arxiv.org/html/2605.06949.
2. V. Popkov, A. Schadschneider, J. Schmidt, G. M. Schütz, *Fibonacci family of dynamical universality classes*, PNAS 112 (2015), 12645–12650, https://pmc.ncbi.nlm.nih.gov/articles/PMC4611608/.
3. H. Spohn, *The Popkov–Schütz two-lane lattice gas: universality for general jump rates*, arXiv:2510.12678, https://arxiv.org/html/2510.12678.
4. E. Pronina, A. B. Kolomeisky, *Spontaneous Symmetry Breaking in Two-Channel Asymmetric Exclusion Processes with Narrow Entrances*, arXiv:cond-mat/0611472, https://arxiv.org/pdf/cond-mat/0611472.
