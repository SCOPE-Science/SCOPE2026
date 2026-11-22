# Unrestricted three-round Kaczmarz coupling is optimized by reshuffling on a symmetric path frame

## Finding

Let \(u_0,u_1,u_2\) be three linearly independent unit vectors in \(\mathbb R^3\) such that \(\langle u_0,u_2\rangle=0\) and \(|\langle u_0,u_1\rangle|^2=|\langle u_1,u_2\rangle|^2=q\), with \(0<q<1/2\). Let \(P_i=I-u_i u_i^{\mathsf T}\). For *every* joint law of \(I_1,I_2,I_3\in\{0,1,2\}\) with each of the three time marginals exactly uniform, allowing arbitrary temporal dependence and repeated rows, and an independent initial error \(e_0\) having second-moment matrix \(\mathbb E[e_0e_0^{\mathsf T}]=I_3\),
\[
\mathbb E\|P_{I_3}P_{I_2}P_{I_1}e_0\|_2^2\ge 2q+\frac{q^2}{3}.
\]
Equality holds **exactly** for joint laws supported on the six permutations of \((0,1,2)\) with uniform time marginals. In the order \((012),(021),(102),(120),(201),(210)\), all these laws have probabilities
\[
(1/3-v,\ v,\ v,\ 1/3-v,\ 1/3-v,\ v),\qquad 0\le v\le1/3.
\]
In particular, ordinary uniform random reshuffling is globally optimal among all feasible dependent three-round schedules; it is not the only optimum.

For the four-vertex unit path, normalized successive edge-difference constraints give \(q=1/4\), with the error restricted to the three-dimensional contrast subspace. The optimal isotropic expected squared consensus error is exactly \(25/48\), compared with \(235/216\) under three independent, uniform with-replacement edge draws, a relative improvement of \(49/94\).

## Assumptions and scope

All computations are in real Euclidean space with exact unit-normalized Kaczmarz projections. The three equations are consistent and linearly independent, so subtracting the common solution reduces each update to \(e\mapsto P_i e\). The schedule is selected independently of the initial error, and each individual time index is uniformly distributed over the three rows; the indices need not be mutually independent. Only \(\mathbb E[e_0e_0^{\mathsf T}]=I_3\) is needed, not Gaussianity or centering. The objective is expected squared Euclidean error **after exactly three row projections**, not the worst-direction risk or a multi-epoch asymptotic rate.

The unit-vector geometry exists exactly throughout \(0<q<1/2\): changing row signs permits the coordinate realization \(u_0=(1,0,0)^{\mathsf T}\), \(u_2=(0,1,0)^{\mathsf T}\), \(u_1=(\sqrt q,\sqrt q,\sqrt{1-2q})^{\mathsf T}\). Reflection exchanges outer indices \(0\) and \(2\).

## Proof

**1. Reduce to trace costs.** For any ordered triple \((i,j,k)\), define
\[
C_{ijk}=\operatorname{tr}\bigl((P_kP_jP_i)^{\mathsf T}(P_kP_jP_i)\bigr).
\]
Independence from \(e_0\) and its unit covariance imply \(\mathbb E_{e_0}\|P_kP_jP_i e_0\|^2=C_{ijk}\). All probabilities enter linearly, making the global scheduling problem a finite multi-marginal transport linear program. We give a pointwise dual certificate, valid for the complete \(3^3=27\) ordered triples.

**2. Exact certificate.** Set \(a_0=a_2=q/2\) and \(a_1=q\). Directly using \(P_i^2=P_i\), the stated Gram products, and cyclicity of the trace yields
\[
\boxed{C_{ijk}\ge a_i+a_j+a_k+q^2\mathbf 1_{\{j=1\}},}
\]
with equality **if and only if** the three indices are distinct. For auditability, here is an exhaustive list of representatives under reflection \(0\leftrightarrow2\) and reversal \((i,j,k)\leftrightarrow(k,j,i)\), showing their costs and their difference from the boxed bound. The classes have sizes \(2,4,4,2,4,2,2,4,2,1\), totaling \(27\).

| Representative | Cost \(C\) | Certificate slack |
|---|---|---|
| `000` | \(2\) | \(2-3q/2\) |
| `001` | \(1+q\) | \(1-q\) |
| `002` | \(1\) | \(1-3q/2\) |
| `010` | \(1+q^2\) | \(1-2q\) |
| `011` | \(1+q\) | \((q+2)(1-2q)/2\) |
| `012` | \(2q+q^2\) | \(0\) |
| `020` | \(1\) | \(1-3q/2\) |
| `021` | \(2q\) | \(0\) |
| `101` | \(1+q^2\) | \((2-q)(1-2q)/2\) |
| `111` | \(2\) | \(2-3q-q^2\) |

Each nonzero slack is strictly positive for \(0<q<1/2\); for the final row \(2-3q-q^2>2-3/2-1/4=1/4\). These cases exhaust all three-row sequences, so this is an infinite-parameter proof, not a numerical enumeration of selected couplings.

**3. Average the dual using all marginal constraints.** Since each time marginal is uniform,
\[
\mathbb E(a_{I_1}+a_{I_2}+a_{I_3})=a_0+a_1+a_2=2q,
\qquad \mathbb P(I_2=1)=1/3.
\]
Consequently the expected certificate gives the stated bound \(2q+q^2/3\). Every permutation achieves equality pointwise, and every repeated-row sequence has strictly positive slack, proving the sharp support characterization.

**4. Identify every optimal joint law.** Write the six nonnegative permutation masses in the order stated in the finding. The nine uniform-marginal equations reduce to rank five; solving them yields exactly the displayed one-parameter family. Its nonnegativity conditions are \(0\le v\le1/3\). In particular, equal masses \(1/6\) correspond to \(v=1/6\).

**5. Four-vertex path consequence.** On the contrast subspace of \(\mathbb R^4\), take \(u_i=(e_i-e_{i+1})/\sqrt2\), \(i=0,1,2\). Then \(u_0\perp u_2\) and the two adjacent squared overlaps are \(1/4\). Every projection averages a neighboring vertex pair. The formula evaluates to \(25/48\); exact independent sampling over the \(27\) triples gives \(235/216\). Their ratio is \(45/94\), hence the improvement is \(49/94\). This comparison assumes initial isotropic covariance on the contrast subspace, not one particular deterministic initial vector.

## Verification

Run `python verify.py` with Python 3 and SymPy to construct the projections, multiply all \(27\) ordered products symbolically, verify each certificate slack and its strict sign at \(q=1/4\), check the marginal equations and their rank, and check the exact independent and reshuffled path values. The program reports a successful symbolic comparison. The general strict slack inequalities and equality classification are proved above rather than inferred from a finite experiment. The source of this file is complete and standalone apart from the declared SymPy dependency.

## Relationship to prior work

Han and Xie [1] prove convergence rates for randomized reshuffling Kaczmarz, but their examined results concern permutations and convergence bounds, not global three-marginal coupling optimization allowing repeated rows. Jeong and Needell [2] analyze reshuffling with sparse constraints, a structurally different setting. Ferreira, Acebrón and Monteiro [3] survey many row-selection choices, but their inspected comparisons do not give this exact unrestricted temporal-dependence lower bound. Prior published exact three-row planar tight-frame work [4] concerns redundant rank-two geometry, relaxation and multiple-epoch minimax factors rather than a three-dimensional independent system with unrestricted fixed marginals. Published two-row relaxed-coupling work [5] optimizes two updates in the worst initial direction and allows an optimal repeat–alternate transition; its different dimension, objective and number of steps cannot imply the present three-round certificate without a separate argument.

The novelty asserted is the **global three-round uniform-marginal optimal-transport certificate and complete optimizer family for the specified independent symmetric path frame**, not the idea of randomized reshuffling, marginal constraints, or orthogonal projections. The prior literature gives important context but absence of an exact match in searched sources is not proof of publication priority.

## Limitations

This result is restricted to three independent unit rows with symmetric path Gram geometry, exact unrelaxed projections, three updates, equal marginal sampling, and isotropic initial second moment. It does not establish optimality for other row geometries, nonuniform marginals, adaptive feedback, relaxed updates, deterministic initial data in every direction, arbitrary number of epochs, or exact arithmetic accuracy under floating-point computation. Further historical comparison and independent scientific review remain outstanding.

## References

[1] D. Han and J. Xie, *A simple linear convergence analysis of the reshuffling Kaczmarz method*, first public arXiv submission 2024-10-02, https://arxiv.org/abs/2410.01140 .

[2] J. Jeong and D. Needell, *Linear Convergence of Reshuffling Kaczmarz Methods with Sparse Constraints*, first public arXiv submission 2023-04-20, https://arxiv.org/abs/2304.10123 .

[3] I. A. Ferreira, J. A. Acebrón and J. Monteiro, *Survey of a Class of Iterative Row-Action Methods: The Kaczmarz Method*, arXiv 2024, https://arxiv.org/html/2401.02842v2 .

[4] *Sharp cyclic–reshuffling rate reversal for a three-line tight Kaczmarz frame* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-cyclic-reshuffling-rate-reversal-for-a-three-line-tight-ka--9dbaf46096e3 .

[5] *A sharp repeat–alternate transition for two-step relaxed Kaczmarz coupling* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-repeat-alternate-transition-for-two-step-relaxed-kaczmar--98f608901237 .
