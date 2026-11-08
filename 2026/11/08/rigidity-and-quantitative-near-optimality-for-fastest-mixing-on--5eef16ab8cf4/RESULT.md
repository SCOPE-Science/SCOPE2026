# Rigidity and quantitative near-optimality for fastest mixing on crown graphs

## Finding

Let \(n\ge3\) be an integer and let \(G_n=K_{n,n}\setminus M\), where \(M\) is a fixed perfect matching between two labelled parts \(\{a_1,\ldots,a_n\}\) and \(\{b_1,\ldots,b_n\}\). Among **all** real symmetric, entrywise nonnegative row-stochastic \(2n\)-by-\(2n\) matrices \(P\) with \(P_{a_i a_j}=P_{b_i b_j}=0\) for \(i\ne j\), \(P_{a_i b_i}=0\), and arbitrary nonnegative diagonal holding probabilities, let
\[
\mu(P)=\left\|P-\frac{\mathbf1\mathbf1^\top}{2n}\right\|_2.
\]
The minimum \(\mu_* =n/(3n-4)\) and a uniform optimal edge transition \(p_*=2/(3n-4)\) also follow from the established edge-transitive-graph fastest-mixing theorem [2]. The following **optimizer rigidity and quantitative stability** strengthen that symmetric-representative result:

**Rigidity.** The only globally minimizing \(P\), with no invariance condition imposed on competitors, is
\[
P_* =\begin{pmatrix} d_*I_n&p_*(J_n-I_n)\\ p_*(J_n-I_n)&d_*I_n\end{pmatrix},\qquad d_*=\frac{n-2}{3n-4}.
\]
In particular, no asymmetric perturbation of the allowed edge probabilities is another optimum.

**Near-optimal stability.** For every such feasible \(P\), writing \(w_{ij}=P_{a_i b_j}\), \(\delta=\mu(P)-\mu_*\ge0\), one has simultaneously, for all \(i\ne j\),
\[
\boxed{\left|w_{ij}-\frac{2}{3n-4}\right|\le
6\sqrt{(3n-4)\mu(P)\delta}+\frac{\delta}{n-2}.}
\]
This is a valid explicit global estimate, not an asserted best possible stability constant. Since all holding probabilities equal one minus the sum of their incident edge weights, the same result controls every matrix entry.

## Assumptions and scope

The graph has exactly \(2n\) vertices and all crossing edges except its diagonal perfect matching; \(n=2\) is excluded because the resulting graph is disconnected. No positive lower bound on allowed transition probabilities is assumed. The operator norm is Euclidean; symmetric stochasticity makes \(\mu(P)\) exactly the second-largest eigenvalue modulus counted on the orthogonal complement of \(\mathbf1\), including disconnected competitors. All optimization is over the full feasible set, **not** only automorphism-invariant transition kernels.

## Proof

Write the crossing block as a nonnegative \(n\)-by-\(n\) matrix \(W=(w_{ij})\) with \(w_{ii}=0\). Let \(D\) and \(E\) be diagonal matrices of row and column sums of \(W\), respectively. Stochasticity forces
\[
P=\begin{pmatrix}I_n-D&W\\ W^\top&I_n-E\end{pmatrix}.
\]
Set \(s=\sum_{i\ne j}w_{ij}\), and abbreviate \(\mu=\mu(P)\). The unit part-sign vector \(v=(\mathbf1,-\mathbf1)/\sqrt{2n}\) satisfies
\[
v^\top Pv=1-\frac{2s}{n}\ge-\mu,
\qquad s\le\frac{n(1+\mu)}2.\tag{1}
\]
Let \(x_1,\ldots,x_{n-1}\) be any orthonormal basis of \(\mathbf1^\perp\subset\mathbb R^n\), and \(u_\alpha=(x_\alpha,-x_\alpha)/\sqrt2\). Every \(u_\alpha\) lies in the mean-zero subspace of \(\mathbb R^{2n}\), hence \(u_\alpha^\top Pu_\alpha\le\mu\). The edge-energy identity gives
\[
u_\alpha^\top Pu_\alpha
=1-\frac12\sum_{i\ne j}w_{ij}(x_{\alpha,i}+x_{\alpha,j})^2.
\]
For \(i\ne j\), the squared norm of the projection of \(e_i+e_j\) onto \(\mathbf1^\perp\) is exactly \(2-4/n\). Summation over the basis therefore yields
\[
\sum_{\alpha=1}^{n-1}u_\alpha^\top Pu_\alpha
=(n-1)-\frac{n-2}{n}s\le(n-1)\mu,
\qquad s\ge\frac{n(n-1)(1-\mu)}{n-2}.\tag{2}
\]
Combining (1) and (2) gives \(n\le(3n-4)\mu\), or \(\mu\ge\mu_*\).

For \(p_*=2/(3n-4)\), all candidate diagonal entries \(d_*=1-(n-1)p_*\) are nonnegative. The four invariant eigenspaces of \(P_*\) have eigenvalues \(1\) (constant vector), \(-\mu_*\) (part-sign vector), \((n-4)/(3n-4)\) (same-sign mean-zero vectors, multiplicity \(n-1\)), and \(\mu_*\) (opposite-sign mean-zero vectors, multiplicity \(n-1\)). Since \(|n-4|\le n\) for \(n\ge3\), this feasible matrix attains the lower bound.

For rigidity, suppose \(\mu=\mu_*\). Equations (1)–(2) then both attain equality and \(s=2n(n-1)/(3n-4)\). Put \(\mathcal U=\{(x,-x)/\sqrt2:\mathbf1^\top x=0\}\). On the mean-zero subspace, \(K=\mu_*I-P\) is positive semidefinite. Equation (2) forces \(\operatorname{tr}_{\mathcal U}K=0\), so \(Ku=0\) for every \(u\in\mathcal U\). Consequently, for every \(x\perp\mathbf1\),
\[
(D+W)x=(1-\mu_*)x,\qquad(E+W^\top)x=(1-\mu_*)x.\tag{3}
\]
A matrix annihilating \(\mathbf1^\perp\) has identical columns. The first relation in (3) makes all allowed off-diagonal entries of a fixed row of \(W\) equal; the second makes all allowed entries of each column equal. The incidence graph on allowable pairs \((i,j)\), \(i\ne j\), linked by shared rows or columns is connected for \(n\ge3\). Hence all allowed weights equal some \(p\); the forced sum \(s\) gives \(p=p_*\), and stochasticity fixes the diagonal. This proves **global** uniqueness.

For stability let \(\delta=\mu-\mu_*\) and retain \(K=\mu I-P\) on the mean-zero subspace, where \(0\preceq K\preceq2\mu I\). From (1) and the exact trace identity in (2),
\[
0\le\operatorname{tr}_{\mathcal U}K
=(n-1)(\mu-1)+\frac{n-2}{n}s
\le\frac{3n-4}{2}\delta.\tag{4}
\]
Thus for every unit \(u\in\mathcal U\), \(\|Ku\|_2^2\le 2\mu\,u^\top Ku\le\mu(3n-4)\delta\). Set \(x=(e_j-e_k)/\sqrt2\) with distinct \(i,j,k\), and \(u=(x,-x)/\sqrt2\). The \(i\)-th coordinate of the top block of \(Ku\) equals \((w_{ij}-w_{ik})/2\). Hence
\[
|w_{ij}-w_{ik}|\le2\sqrt{\mu(3n-4)\delta}.
\]
The bottom block analogously bounds pairs of weights sharing a column. Any two allowed pairs \((i,j)\) are joined by at most three row- or column-sharing steps (if the pairs are reciprocal, use a third index). Therefore their weights differ by at most \(6\sqrt{\mu(3n-4)\delta}\). Finally, (1)–(2) give
\[
\left|\frac{s}{n(n-1)}-p_*\right|\le\frac{\delta}{n-2}.
\]
Combining the weight spread with this average bound proves the stated stability inequality. No unproved limiting or numerical assertion enters the proof.

## Verification

Run `python verify.py` in a Python environment with NumPy. The self-contained script checks rational formulas exactly for \(3\le n\le19\), direct full-matrix spectra for the proposed optimum, exact trace identities, and deterministic random feasible full-matrix competitors for \(3\le n\le10\). The checked output is recorded in `VERIFICATION.md`. Finite tests corroborate the algebra; the proof above covers all \(n\ge3\) and all feasible real edge weights.

## Relationship to prior work

Boyd, Diaconis and Xiao [1] formulate the FMMC semidefinite program and explicitly note that global minimizers can be nonunique. Boyd, Diaconis, Parrilo and Xiao [2, Theorem 3.1] prove that an edge-transitive graph admits an optimal common-edge probability computable from extreme Laplacian eigenvalues. Applied to \(G_n\), their result already implies \(p_*\) and \(\mu_*\); **neither numerical value is claimed here as novel**. Their symmetry argument establishes existence of an invariant optimizer, not that **every** optimizer is invariant. The proof here uses two complementary extremal eigenspace trace inequalities to establish both complete optimizer rigidity and the explicit full-feasible-set near-optimality bound. Göring, Helmberg and Reiss [3] study a different fixed-total-weight Laplacian spectral-width program without vertex holding constraints; their graph-realization machinery is conceptually related but does not, in the inspected material, give the stated crown-graph rigidity and bound.

## Limitations

Publication priority remains unverified. The stability constant is explicit but not proved sharp. The conclusions concern symmetric stochastic kernels, uniform stationary distribution, permitted holding, and the specified deleted-perfect-matching graph; arbitrary nonreversible or nonuniform-stationary chains are not covered. Highly similar unindexed literature could still contain an equivalent rigidity or stability result.

## References

[1] S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf . Originally published electronically October 29, 2004 (first-page bibliographic note).

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first public September 6, 2007; later SIAM J. Optim. 20 (2009), 792–819. https://arxiv.org/abs/0709.0955 . Full readable version: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf .

[3] F. Göring, C. Helmberg, S. Reiss, *On Minimizing the Spectral Width of Graph Laplacians and Associated Graph Realizations*, TU Chemnitz preprint 2011-4 (February 10, 2011). https://www.tu-chemnitz.de/mathematik/preprint/2011/PREPRINT_04.pdf .
