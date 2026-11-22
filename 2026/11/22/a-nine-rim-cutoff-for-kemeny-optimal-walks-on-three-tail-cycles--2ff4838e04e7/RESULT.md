# A nine-rim cutoff for Kemeny-optimal walks on three-tail cycles

## Finding
For every integer \(m\ge 3\), attach a distinct three-edge path to each vertex of a unit combinatorial cycle \(C_m\). Among **all** irreducible symmetric nonnegative stochastic transition matrices supported on this \(4m\)-vertex graph, with self-loops allowed, there is exactly one minimizer of Kemeny's constant. Its transition probabilities are constant on the four edge orbits and have the following explicit form.

Put
\[
 A=\frac{3(4m-3)}4,\qquad C=2m-1,\qquad D=\frac{4m-1}4,\qquad B=\frac{m^2-1}3.
\]
Write \(a_1,a_2,a_3\) for transition probabilities along the first, second, and third edges of each pendant path, directed away from the cycle; write \(b\) for the probability along each cycle edge.

For \(3\le m\le8\), define
\[
 z=\frac{\sqrt{A+D}}{\sqrt{A+D}+\sqrt{C+2B}}.
\]
The unique optimum and its sharp Kemeny constant are
\[
 (a_1,a_2,a_3,b)=\left(z,1-z,z,\frac{1-z}{2}\right),
 \qquad \mathcal K_*=\left(\sqrt{A+D}+\sqrt{C+2B}\right)^2.
\]
For \(m\ge9\), define
\[
 x=\frac{\sqrt A}{\sqrt A+\sqrt{2B}},\qquad
 y=\frac{\sqrt C}{\sqrt C+\sqrt D}.
\]
Then the unique optimum and its sharp Kemeny constant are
\[
 (a_1,a_2,a_3,b)=\left(x,y,1-y,\frac{1-x}2\right),
\qquad \mathcal K_*=\left(\sqrt A+\sqrt{2B}\right)^2+\left(\sqrt C+\sqrt D\right)^2.
\]
In particular the optimal holding probability at the first pendant-path vertex is exactly zero for \(3\le m\le8\) and strictly positive for every \(m\ge9\). The transition between regimes is sharp: the competing unconstrained allocation crosses its vertexwise stochasticity boundary strictly between \(m=8\) and \(m=9\).

## Assumptions and scope
Let \(V=\{(i,j):i\in\mathbb Z/m\mathbb Z,\ j\in\{0,1,2,3\}\}\). The undirected edges are \(\{(i,0),(i+1,0)\}\) for each \(i\), and \(\{(i,j-1),(i,j)\}\) for \(j=1,2,3\). A feasible \(P\) is symmetric, entrywise nonnegative, row-stochastic, irreducible, and has \(P_{uv}=0\) whenever distinct \(u,v\) are not joined by an edge. Holding probabilities \(P_{uu}\) may be zero or positive. Let the nonzero eigenvalues of \(I-P\) be \(\lambda_2,\ldots,\lambda_{4m}\); define the zero-diagonal hitting-time convention
\[
\mathcal K(P)=\sum_{i=2}^{4m}\frac1{\lambda_i}
=\sum_v\frac1{4m}\mathbb E_u[T_v]
\]
for any start \(u\), where \(T_u=0\) if the target is the start. Neither periodicity nor extra laziness is required.

## Proof
**1. Global uniqueness and symmetry.** Let \(N=4m\), \(L=I-P\), and \(J=\mathbf1\mathbf1^\mathsf T\). For connected symmetric stochastic \(P\), \(L+J/N\) is positive definite and
\[
\mathcal K(P)=\operatorname{tr}(L+J/N)^{-1}-1.
\]
For a nonzero symmetric Laplacian perturbation \(H\), the second derivative of the trace along an admissible positive-definite segment is
\[
2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0,\qquad X=L+J/N.
\]
Indeed \(X^{-1/2}HX^{-1/2}\) is a nonzero symmetric matrix, whose square has positive trace against the positive-definite \(X^{-1}\). Thus the objective is strictly convex in all edge weights: distinct edge-weight vectors yield distinct Laplacians. The feasible closed stochastic polytope contains connected matrices; as a connected matrix approaches disconnection, some positive Laplacian eigenvalue tends to zero and \(\mathcal K\) diverges. Hence a unique connected optimum exists. Rotating an optimum gives another feasible optimum. Uniqueness makes it rotation invariant, yielding common cycle weight \(b\) and three common pendant weights \(a_1,a_2,a_3\). Therefore the reduction is global, not a restriction to symmetric candidate matrices.

**2. Exact objective.** With a uniform stationary distribution, effective resistance gives the Kirchhoff-index identity
\[
\mathcal K(P)=\frac1N\sum_{\{u,v\}\subset V} R_{uv}.
\]
Each pendant edge at depth \(j\) cuts off a tree of size \(s_j=4-j\). All cross-cut pairs contribute \(1/a_j\), giving \(m s_j(N-s_j)/a_j\) to the total unordered effective-resistance sum. For vertices belonging to different pendant trees, the root-to-root resistance is the corresponding cycle resistance, independent of attached trees. Four vertices per root give a multiplicity of \(16\); the cycle Kirchhoff index is \((m^3-m)/(12b)\). Thus
\[
\mathcal K(P)=\frac A{a_1}+\frac C{a_2}+\frac D{a_3}+\frac B b.
\]
All four coefficients are positive for \(m\ge3\). The stochasticity conditions at the root and the three pendant depths are, respectively,
\[
 a_1+2b\le1,\quad a_1+a_2\le1,\quad a_2+a_3\le1,\quad a_3\le1.
\]
Since the objective decreases strictly with \(b\) and \(a_3\), its optimum satisfies \(b=(1-a_1)/2\) and \(a_3=1-a_2\). Write \(x=a_1\), \(y=a_2\). The remaining strictly convex problem is
\[
 \min_{x>0,\,y>0,\,x+y\le1}
 F(x,y)=\frac A x+\frac{2B}{1-x}+\frac C y+\frac D{1-y}.
\]
The constraints and denominators imply \(x<1\), \(y<1\).

**3. The natural interior optimum and its feasibility.** Without the coupling constraint \(x+y\le1\), each coordinate has a unique minimizer,
\[
 x_0=\frac{\sqrt A}{\sqrt A+\sqrt{2B}},\qquad
 y_0=\frac{\sqrt C}{\sqrt C+\sqrt D}.
\]
A direct comparison shows
\[
 x_0+y_0\le1\quad\Longleftrightarrow\quad AC\le 2BD.
\]
Multiplying the difference by 12 gives the integer cubic
\[
12(AC-2BD)=H(m)=-8m^3+74m^2-82m+25.
\]
Here \(H(3)=229\), \(H(4)=369\), \(H(8)=9\), and \(H(9)=-551\). Also \(H''(m)=148-48m<0\) for \(m\ge4\), so concavity between 4 and 8, and the endpoint signs, show positivity for each integer \(3\le m\le8\). Since \(H'(8)=-434<0\) and \(H''<0\) for \(m\ge8\), the cubic stays negative for all \(m\ge9\). Therefore the interior optimum is feasible precisely for \(m\ge9\), with \(x_0+y_0<1\); its objective is the sum of the two stated square-root expressions.

**4. The active face.** For \(3\le m\le8\), the unconstrained minimizer violates \(x+y\le1\). Strict convexity implies the constrained optimum lies on the active face \(x+y=1\): an interior constrained minimizer would have to coincide with the infeasible unconstrained stationary point. On that face set \(x=z\), \(y=1-z\), obtaining
\[
 F(z,1-z)=\frac{A+D}{z}+\frac{C+2B}{1-z}.
\]
Strict convexity and the Cauchy--Schwarz inequality give the unique minimizer \(z=\sqrt{A+D}/(\sqrt{A+D}+\sqrt{C+2B})\) and the stated optimum. The second and third pendant edges and cycle edges are positive in both regimes, so irreducibility holds. The first pendant vertex holds with probability \(1-x-y\), which is exactly zero on the active face and strictly positive in the interior regime. All equality cases have therefore been included.

**5. Large-cycle shape.** From the explicit formula, as \(m\to\infty\), \(a_1\sim3/\sqrt{2m}\), \(a_2\to\sqrt2/(1+\sqrt2)\), \(a_3\to1/(1+\sqrt2)\), and \(b\to1/2\). Thus the zero-to-positive holding transition persists for all larger cycles; the limiting holding probability at the first pendant vertex is \(1/(1+\sqrt2)\).

## Verification
The attached `verify.py` constructs the exact weighted Laplacian, inverts \(L+J/N\) using SymPy rational arithmetic, and checks equality between the resulting spectral trace and the resistance-based formula for several distinct admissible rational weights on cycles of lengths 3, 4, 5, and 9. It verifies the cubic identity symbolically and checks the discrete phase comparison for integers from 3 to 79. A further independent floating-point eigenvalue check was performed for every integer \(m\) from 3 through 15 at its analytically specified optimizer; it agreed with the closed-form Kemeny value within \(3\times10^{-12}\). Neither finite check substitutes for the proof for every integer \(m\ge3\).

## Relationship to prior work
The symmetric stochastic graph-design setting and symmetry reduction are classical in Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955, 2007), which optimizes second-largest eigenvalue modulus, not this Kemeny criterion. Faught, Kempton and Knudson (arXiv:2108.01061, 2021) develop effective-resistance calculations for Kemeny's constant of simple random walks on graphs with cut vertices, with degree-weighted stationary law rather than optimized uniform-stationary transition probabilities. Durastante, Gnazzo and Meini (2026) study reversible Kemeny minimization with sparsity constraints and optimization algorithms; its inspected full-text formulation and examples do not give this three-tail cycle classification. The result here is a closed-form global optimizer, exact integer phase boundary, and all equality conditions for a distinct natural graph family and objective. General convexity/symmetry and resistance identities are not claimed as new.

## Limitations
The theorem concerns the zero-diagonal stationary-target mean hitting time under symmetric, discrete-time, uniform-stationary stochastic transitions, **not** SLEM-optimal mixing, degree-normalized simple random walks, a nonuniform stationary law, or arbitrary pendant lengths. The optimization includes positive holding probabilities where permitted, but assumes no constraints on them beyond stochasticity. Its result has not received independent mathematical validation. Primary-literature inspection and semantic database searches provide no proof of publication priority: unindexed or unpublished equivalent classifications may exist.

## References
1. Boyd, S., Diaconis, P., Parrilo, P. A., Xiao, L. *Fastest mixing Markov chain on graphs with symmetries*. arXiv:0709.0955v1, first public 2007-09-06. https://arxiv.org/abs/0709.0955
2. Faught, N., Kempton, M., Knudson, A. *A 1-Separation Formula for the Graph Kemeny Constant and Braess Edges*. arXiv:2108.01061v1, first public 2021-08-02. https://arxiv.org/abs/2108.01061
3. Durastante, F., Gnazzo, M., Meini, B. *Kemeny's constant minimization for reversible Markov chains via structure-preserving perturbations*. BIT Numerical Mathematics 66 (2026), article 59, published 2026-09-23. https://doi.org/10.1007/s10543-026-01152-6
