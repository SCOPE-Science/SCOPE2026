# Sharp Kemeny regret and optimal stochastic walks on transitive leaf coronas

## Finding
Let \(H\) be a finite connected simple graph on \(m\ge3\) vertices that is both vertex-transitive and edge-transitive, of degree \(d\), and let \(G=H\circ K_1\) be formed by attaching one private pendant leaf to each vertex of \(H\). Write \(L_H\) for the unweighted combinatorial Laplacian of \(H\), and define
\[
T_H=\operatorname{tr}(L_H^+)=\sum_{j=2}^{m}\lambda_j(L_H)^{-1},\qquad B=2dT_H,\qquad C=m-\tfrac12.
\]
Among **all** irreducible symmetric nonnegative stochastic transition matrices \(P\) supported on \(G\), with self-loops allowed, the unique minimizer of the zero-diagonal Kemeny constant is the matrix assigning the common transition probabilities
\[
a_*=\frac{\sqrt C}{\sqrt B+\sqrt C}\quad\text{to each pendant edge},\qquad
b_*=\frac{\sqrt B}{d(\sqrt B+\sqrt C)}\quad\text{to each core edge}.
\]
It has zero holding probability at every core vertex and the exact minimum
\[
\boxed{\mathcal K_*=(\sqrt B+\sqrt C)^2.}
\]
Furthermore, for every admissible \(P\), let \(a_i=P_{i,i'}\) denote the transition probability from core vertex \(i\) to its pendant leaf \(i'\) and set \(\bar a=m^{-1}\sum_{i=1}^m a_i\). Then \(0<\bar a<1\) and the following **sharp global performance certificate** holds without assuming any symmetry of the candidate transition weights:
\[
\boxed{\mathcal K(P)-\mathcal K_*\ \ge\
\frac{\bigl(\sqrt B\,\bar a-\sqrt C(1-\bar a)\bigr)^2}{\bar a(1-\bar a)}.}
\]
Equality holds if and only if all pendant edges have transition probability \(\bar a\) and all core edges have transition probability \((1-\bar a)/d\). Hence the lower bound is attained for every prescribed mean pendant probability strictly between zero and one.

In particular, for the sunlet \(G=C_m\circ K_1\), \(m\ge3\), one has \(d=2\), \(T_H=(m^2-1)/12\) and
\[
B=(m^2-1)/3,\quad C=m-\tfrac12,\quad
\mathcal K_* = \left(\sqrt{(m^2-1)/3}+\sqrt{m-\tfrac12}\right)^2.
\]
Its optimal pendant probability satisfies \(a_*\sim\sqrt{3/m}\) as \(m\to\infty\). The equal-edge-probability walk \(a=b=1/3\) has
\[
\mathcal K_{\mathrm{equal}}=\frac{m^2-1}{2}+3m-\frac32,
\qquad\lim_{m\to\infty}\frac{\mathcal K_{\mathrm{equal}}}{\mathcal K_*}=\frac32.
\]

## Assumptions and scope
The base graph is finite, connected, simple, vertex-transitive, and edge-transitive. The stochastic matrices are real, symmetric, nonnegative, irreducible and supported on existing graph edges and the diagonal; no positive holding probability is required. The uniform distribution is stationary. \(L_H^+\) is the Moore–Penrose pseudoinverse. The *zero-diagonal* Kemeny normalization takes the hitting time from a state to itself to be zero:
\[
\mathcal K(P)=\sum_{\lambda\in\operatorname{spec}(P),\lambda\ne1}(1-\lambda)^{-1}
=\operatorname{tr}\bigl((I-P+J/(2m))^{-1}\bigr)-1.
\]
The alternative return-time-on-the-diagonal convention adds the constant one and does not change any optimizer or regret inequality. The theorem is not asserted for nonreversible, nonuniform-stationary, or asymmetric transition matrices.

## Proof
**1. Weighted-corona trace identity.** For an arbitrary connected weighted core \(H\) with positive edge conductances and positive pendant conductances \(a_1,\ldots,a_m\), let \(R_H(i,j)\) denote core effective resistance. Attaching dangling leaves does not change \(R_H(i,j)\). Any resistance path from a leaf to another vertex adds \(1/a_i\); each pendant edge separates one vertex from the other \(2m-1\) vertices. For each core pair \(i<j\), the four pairs among \(i,i',j,j'\) contribute four copies of \(R_H(i,j)\). The Kirchhoff identity \(\sum_{u<v}R_G(u,v)=2m\operatorname{tr}(L_G^+)\) therefore yields
\[
\operatorname{tr}(L_G^+)=2\operatorname{tr}(L_H^+)+\frac{2m-1}{2m}\sum_{i=1}^{m}\frac1{a_i}.
\]
This resistance identity is used as a known structural principle; its specialization is not the originality claim.

**2. Strict convexity and averaging.** For every connected feasible transition network, \(L=I-P\) is a weighted Laplacian and
\[
\mathcal K(P)=\operatorname{tr}\bigl((L+J/(2m))^{-1}\bigr)-1.
\]
The map \(A\mapsto\operatorname{tr}(A^{-1})\) is strictly convex on positive definite symmetric matrices: along any nonzero symmetric direction \(H\), the second directional derivative equals \(2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0\). Different edge weights give different Laplacians, so the objective is strictly convex in edge weights on its connected feasible domain. Averaging \(P\) over all automorphisms of \(H\), extended to its private leaves, cannot increase \(\mathcal K\), with equality only when \(P\) is already invariant. The automorphism group acts transitively on core edges and on pendant edges; the average therefore has common positive rates \(a=\bar a\) and \(b>0\), obeying \(a+db\le1\).

**3. Exact invariant reduction.** If all core edges have conductance \(b\), then the core Laplacian is \(bL_H\). Step 1 gives
\[
\mathcal K(a,b)=\frac{2T_H}{b}+\frac C a.
\]
For fixed \(a\), this decreases strictly in \(b\); its minimum occurs at \(b=(1-a)/d\). Consequently, for any original feasible \(P\),
\[
\mathcal K(P)\ge \mathcal K(\bar a,\bar b)\ge f(\bar a),
\qquad f(a)=\frac B{1-a}+\frac Ca.
\]
Both inequalities are strict unless, respectively, all weights are invariant and all core holding probabilities vanish.

**4. Exact optimum and regret.** For \(0<a<1\), Cauchy–Schwarz or direct expansion gives
\[
f(a)=(\sqrt B+\sqrt C)^2+
\frac{(\sqrt B\,a-\sqrt C(1-a))^2}{a(1-a)}.
\]
The second term vanishes exactly at \(a=a_*\); the corresponding \(b_*= (1-a_*)/d\) is positive, feasible, and irreducible. Combining with Step 3 gives the claimed global lower bound, exact equality cases and uniqueness.

**5. Cyclic specialization.** The cycle's nonzero Laplacian eigenvalues are \(4\sin^2(\pi j/m)\) for \(j=1,\ldots,m-1\). Using \(\sum_{j=1}^{m-1}\csc^2(\pi j/m)=(m^2-1)/3\) gives \(T_H=(m^2-1)/12\). Substitution proves the finite formulas; leading-term expansion proves \(a_*\sim\sqrt{3/m}\) and the \(3/2\) asymptotic performance ratio.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The script independently computes exact rational inverses of \(L+J/N\) on finite weighted coronas, checks the weighted-core identity with heterogeneous conductances, checks cyclic spectral specializations and global sharp regret for asymmetric feasible transition choices, and checks the closed-form minimum and positivity over a range of core sizes. Passing these finite tests supports the derivation but does not replace the universal strict-convexity and resistance arguments above.

## Relationship to prior work
The convex stochastic Kemeny formulation is established by Agharkar, Patel, and Bullo (2014); the graph-automorphism reduction for the different fastest-spectral-mixing objective appears in Boyd, Diaconis, Parrilo, and Xiao (2007/2009). Kirchhoff-index identities for corona constructions precede this theorem, notably Liu (2016, 2020), so no novelty is claimed for resistance summation itself. The contribution here is a globally sharp **fixed-uniform-stationary Kemeny design and regret classification**, against all nonuniform edge allocations on every transitive core, with a concrete asymptotic sunlet comparison. In particular, fastest-spectral-mixing and continuous-time spectral-gap designs solve different optimization problems and neither objective by itself implies the Kemeny certificate.

## Limitations
The primary result requires both vertex- and edge-transitivity of the core. For a general asymmetric core, the weighted-corona identity remains valid but the universal two-probability optimizer need not. Optimization is restricted to symmetric stochastic kernels, not arbitrary reversible kernels with nonuniform stationary masses. The closed-form optimizer is a one-step transition-design statement, not an assertion about finite-time mixing or computational cost. Although the inspected primary works do not state this exact all-core optimality/regret theorem, unindexed equivalent results and prior combinations of convexity with corona resistance formulas remain publication-priority risks; no independent mathematical audit has been performed.

## References
1. P. Agharkar, R. Patel, F. Bullo, “Robotic surveillance and Markov chains with minimal first passage time,” IEEE CDC (2014), DOI: 10.1109/CDC.2014.7040425, full manuscript https://motion.me.ucsb.edu/pdf/2014b-apb-conference.pdf.
2. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, “Fastest mixing Markov chain on graphs with symmetries,” arXiv:0709.0955 (first posted 2007-09-06), https://arxiv.org/abs/0709.0955.
3. Q. Liu, “Resistance distance and Kirchhoff index in corona and edge corona of two graphs,” Journal of Donghua University (Natural Science) 33 (2016), 411–413, cited in the following generalization.
4. Q. Liu, “Resistance Distance and Kirchhoff Index of the Diamond Hierarchical Graph and the Generalized Corona Graph,” IAENG International Journal of Applied Mathematics 50 (2020), 878–882, https://www.iaeng.org/IJAM/issues_v50/issue_4/IJAM_50_4_22.pdf.
5. F. Durastante, M. Gnazzo, B. Meini, “Kemeny’s constant minimization for reversible Markov chains via structure-preserving perturbations,” BIT Numerical Mathematics 66 (2026), article 59, https://doi.org/10.1007/s10543-026-01152-6.
