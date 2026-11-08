# Sharp coexistence threshold for two flip attractors in two-token self-attention

## Finding
Consider the normalized discrete-time attention dynamics with two tokens on the unit circle and a symmetric value matrix with eigenvalues \(a>0\) and \(-b<0\). For finite positive inverse temperature \(\beta\) and positive residual step \(\eta\), the synchronized sign-flip orbit and the antipodal token-exchange orbit are **both hyperbolic attracting period-two orbits** if and only if
\[
 b\tanh\beta>a,\qquad \eta>\frac{2}{b\tanh\beta-a}.
\]
Their complete two-step tangent multiplier spectra are given below. The boundary is sharp for the hyperbolic attraction of these two specified orbits; no global attractor classification is asserted.

## Assumptions and scope
Let \(e_1=(1,0)\) and \(e_2=(0,1)\). For \(a,b,\beta,\eta>0\), put \(V=\operatorname{diag}(a,-b)\). For two tokens \(x_1,x_2\in S^1\), define
\[
 A_{ij}(X)=\frac{\exp(\beta\langle x_i,x_j\rangle)}{\exp(\beta\langle x_i,x_1\rangle)+\exp(\beta\langle x_i,x_2\rangle)},\quad
 \mathcal F_i(X)=\frac{x_i+\eta V\sum_{j=1}^2 A_{ij}(X)x_j}{\left\|x_i+\eta V\sum_{j=1}^2 A_{ij}(X)x_j\right\|}.
\]
The map is considered on the open subset where both denominators are nonzero. It has query and key matrices \(\sqrt\beta I_2\) and value matrix \(V\), corresponding to the full-softmax, residual and Euclidean-normalization model. It is smooth near all orbits in the theorem.

Write \(t=\tanh\beta\in(0,1)\). The two candidate periodic orbits (with ordered, individually labelled tokens) are
\[
 C:\quad (e_2,e_2)\longleftrightarrow(-e_2,-e_2),\qquad
 B:\quad (e_2,-e_2)\longleftrightarrow(-e_2,e_2).
\]
The assertion concerns hyperbolic attraction in the full two-dimensional manifold \(S^1\times S^1\), not just within invariant axes or quotient dynamics.

## Proof
At any configuration \(X=(s_1e_2,s_2e_2)\), with \(s_i\in\{\pm1\}\), the weights depend only on the signs. For \(C\), the attention matrix is \(A_C=\frac12\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\), and for \(B\) it is
\[
 A_B=\frac12\begin{pmatrix}1+t&1-t\\1-t&1+t\end{pmatrix}.
\]
The two unnormalized outputs are respectively \((1-\eta b)s_ie_2\) and \((1-\eta bt)s_ie_2\). Thus \(C\) and \(B\) are genuine period-two sign-flip orbits precisely when \(\eta b>1\) and \(\eta bt>1\), respectively. They never meet the undefined-normalization set under these strict conditions. Moreover \(\mathcal F(-X)=-\mathcal F(X)\), so both steps have the same linearization in horizontal tangent coordinates.

At an axial sign configuration, a tangent variation is \(\delta x_i=u_ie_1\); all dot-product derivatives vanish because \(\langle e_1,e_2\rangle=0\). Therefore the derivative of each softmax weight vanishes to first order. Writing \(u=(u_1,u_2)^\mathsf T\), the derivative of the unnormalized horizontal output is \((I_2+\eta a A_C)u\) or \((I_2+\eta a A_B)u\). Since the unnormalized vertical output is nonzero and the normalized derivative of a horizontal perturbation divides by its absolute length, the one-step tangent matrices on the two flip orbits are
\[
 J_C=\frac{I_2+\eta a A_C}{\eta b-1},\qquad
 J_B=\frac{I_2+\eta a A_B}{\eta bt-1}.
\]
The vectors \((1,1)^\mathsf T\) and \((1,-1)^\mathsf T\) diagonalize both matrices. Accordingly the two-step Floquet multipliers are
\[
 \operatorname{spec}(D\mathcal F^2|_C)=
 \left\{\left(\frac{1+\eta a}{\eta b-1}\right)^2,\left(\frac1{\eta b-1}\right)^2\right\},
\]
\[
 \operatorname{spec}(D\mathcal F^2|_B)=
 \left\{\left(\frac{1+\eta a}{\eta bt-1}\right)^2,\left(\frac{1+\eta at}{\eta bt-1}\right)^2\right\}.
\]
Both numerators are positive and the first eigenvalue is larger in each expression (strictly for \(B\), since \(t<1\)). Hence, conditional on being a genuine flip orbit, \(C\) is hyperbolically attracting exactly when \(\eta(b-a)>2\), and \(B\) is hyperbolically attracting exactly when \(\eta(bt-a)>2\). Because \(t<1\), the second condition implies the first as well as both sign-flip inequalities. It is therefore necessary and sufficient for coexistence. Written as \(bt>a\) and \(\eta>2/(bt-a)\), this is the stated boundary. At equality at least one multiplier has modulus one, so the hyperbolic-attraction statement remains sharp without making a nonlinear assertion about the boundary. For strict inequalities, standard linearization of a smooth finite-dimensional return map gives open attracting neighborhoods of both distinct cycles. \(\square\)

## Verification
The standalone program `check.py` symbolically checks both characteristic polynomials for the displayed one-step tangent matrices, compares those matrices with centered finite differences of the full normalized softmax map, iterates small perturbations around both cycles, and verifies strictness on either side of the exact step-size boundary. Run with `python check.py` using NumPy and SymPy. The analytic argument proves the statement for all positive parameters; the finite checks are supplementary.

As a concrete admissible instance, \(a=1\), \(b=3\), \(\beta=1\), \(\eta=3\) satisfies the strict criterion and has both distinct attracting period-two orbits. No conclusion about additional attractors or basins away from these neighborhoods follows.

## Relationship to prior work
Altafini (2026) formulates this exact normalized, residual, full-softmax discrete attention map and analyzes equilibria and their linear stability, principally in the small-step setting. The present result instead locates two nonstationary, simultaneous hyperbolic sinks, gives the exact joint threshold, and computes their two-step Floquet multipliers when the symmetric value matrix has a positive principal eigenvalue and a more strongly negative second eigenvalue. The source’s Section V-B on longer step sizes contains a short discussion of sufficient equilibrium-stability conditions, not a period-two classification; its Section IV-B studies Jacobians at fixed points. Thus the exact two-cycle coexistence threshold is not stated there. This does not establish priority against all other literature.

Gao, Yang and Chen (2026) study cluster-flip and exchange regimes in a distinct repulsive model with \(V=-I\). Their negative-definite value matrix is not the mixed-sign \(\operatorname{diag}(a,-b)\) case here. Their work establishes that attention-driven flip dynamics are not a new general phenomenon. The specific exact mixed-sign simultaneous-attraction boundary is the limited contribution claimed here.

## Limitations
The theorem concerns two labelled tokens in two dimensions, Euclidean normalization, the given state-independent value matrix and softmax similarity, and **local hyperbolic** attraction. The update can be undefined elsewhere when an unnormalized output vanishes. There is no global basin classification, no assertion about nonhyperbolic threshold dynamics, and no claim that more complicated orbits are impossible. The available literature search and incomplete access to some primary full texts do not establish definitive historical priority. Independent review has not been performed.

## References
1. C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1, first posted 9 October 2026, https://arxiv.org/abs/2610.13518.
2. Q. Gao, Z. Yang and X. Chen, *Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality*, arXiv:2609.28448, first posted 23 September 2026, https://arxiv.org/abs/2609.28448.
3. C. Kuehn and J. Yoon, *Spectral Selection in Symmetric Self-Attention Dynamics*, arXiv:2604.26085, first posted 28 April 2026, https://arxiv.org/abs/2604.26085.
