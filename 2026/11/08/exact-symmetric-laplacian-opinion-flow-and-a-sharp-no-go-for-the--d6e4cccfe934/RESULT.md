# Exact symmetric-Laplacian opinion flow and a sharp no-go for the directed FJ reduction

## Finding

For the finite-network Lindblad opinion system with the spin-exchange jumps and rates printed in Chu (2026, Eq. 14), the expected opinions satisfy an **exact closed classical equation without any product-state or independence approximation**. Its social term is a *symmetric* graph Laplacian, not the directed Friedkin–Johnsen (FJ) term reported in that work (Eq. 34). The two vector fields are identical for every possible initial opinion vector **if and only if every social-exchange rate is zero**. In particular, correlations can affect higher joint moments but cannot feed back into expected opinions for these jump operators.

For an unanchored connected network, the genuine Lindblad flow converges in first moments to the **arithmetic** average of initial opinions, irrespective of directionality of the given row-stochastic influence matrix. A three-agent directed example instead has FJ-predicted consensus \(-3/5\), whereas the full Lindblad equation gives exactly \(-1/3\). A separate anchored, three-agent example gives distinct stationary opinion vectors.

## Assumptions and scope

Let \(n\ge 2\). Let \(W=(w_{ij})\) be nonnegative, row-stochastic and zero-diagonal, representing directed influences; a term \((i,j)\) is included whenever \(w_{ij}>0\). Let \(0\le\lambda_i\le1\) be stubbornness parameters and \(-1\le s_i\le1\) anchor opinions. On \((\mathbb C^2)^{\otimes n}\), write \(O_i=|0\rangle_i\langle0|-|1\rangle_i\langle1|\) and \(\sigma_i^+=|0\rangle_i\langle1|\), \(\sigma_i^-=|1\rangle_i\langle0|\). The density matrix is any physical density operator, including entangled states. Its generator is

\[
\mathcal L(\rho)=-i[H,\rho]+\sum_{i\ne j}(1-\lambda_i)w_{ij}\bigl(\mathcal D[\sigma_i^+\sigma_j^-](\rho)+\mathcal D[\sigma_i^-\sigma_j^+](\rho)\bigr)+\sum_i\lambda_i\bigl(\tfrac{1+s_i}{2}\mathcal D[\sigma_i^+](\rho)+\tfrac{1-s_i}{2}\mathcal D[\sigma_i^-](\rho)\bigr),
\]

where \(\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}\) and \(H=-\sum_{i\ne j}w_{ij}O_iO_j\), exactly the diagonal Ising form in the source. Nothing depends on the numerical value of the diagonal Ising couplings as long as \([H,O_i]=0\). Define \(x_i(t)=\operatorname{Tr}(\rho(t)O_i)\), \(\Lambda=\operatorname{diag}(\lambda_i)\), and symmetric conductances

\[
c_{ij}=(1-\lambda_i)w_{ij}+(1-\lambda_j)w_{ji}\quad(i\ne j),\qquad c_{ii}=0.
\]

The symmetric Laplacian has \((L_c)_{ii}=\sum_{j\ne i}c_{ij}\) and \((L_c)_{ij}=-c_{ij}\) when \(i\ne j\). No restriction on initial coherences or correlations is required.

## Proof

**1. Exact observable identity.** For an ordered pair \((i,j)\), set \(L^+=\sigma_i^+\sigma_j^-\), \(L^-=\sigma_i^-\sigma_j^+\). The adjoint dissipator is \(\mathcal D[L]^*(A)=L^\dagger AL-\tfrac12\{L^\dagger L,A\}\). Directly on the four computational-basis vectors of the two qubits, the sum of the two adjoint dissipators satisfies the *operator identities*

\[
\bigl(\mathcal D[L^+]^*+\mathcal D[L^-]^*\bigr)(O_i)=O_j-O_i,\qquad
\bigl(\mathcal D[L^+]^*+\mathcal D[L^-]^*\bigr)(O_j)=O_i-O_j.
\]

For every other site \(k\), the sum annihilates \(O_k\). These identities hold on the entire tensor-product Hilbert space, not just on product states: the two jumps exchange the opposite-bit configurations, each at the same rate. The two single-site anchor dissipators give

\[
\left(\tfrac{1+s_i}{2}\mathcal D[\sigma_i^+]^*+\tfrac{1-s_i}{2}\mathcal D[\sigma_i^-]^*\right)(O_i)=s_i I-O_i.
\]

Since \([H,O_i]=0\), taking the trace against an arbitrary \(\rho(t)\) yields

\[
\boxed{\ \dot x_i=\lambda_i(s_i-x_i)+\sum_{j\ne i}c_{ij}(x_j-x_i),\qquad \dot x=-(\Lambda+L_c)x+\Lambda s.\ }
\]

This derivation uses neither factorization nor neglect of two-agent covariances.

**2. Exact no-go for the claimed reduction.** The directed FJ equation reported in Chu (2026, Eq. 34) is

\[
\dot x_i^{\rm FJ}=\lambda_i(s_i-x_i)+\sum_{j\ne i}(1-\lambda_i)w_{ij}(x_j-x_i).
\]

For each \(i\ne j\), the off-diagonal coefficient of \(x_j\) in the difference between the actual and stated linear vector fields is precisely \((1-\lambda_j)w_{ji}\). Therefore the two vector fields agree as functions of \(x\in[-1,1]^n\) if and only if \((1-\lambda_j)w_{ji}=0\) for every \(i\ne j\), that is, if and only if all social-exchange rates vanish. The necessity follows from comparison of coefficients on a set with nonempty interior; sufficiency is immediate. For a zero-diagonal row-stochastic \(W\), equality thus requires \(\lambda_i=1\) for all \(i\).

**3. Dynamics and variational structure.** The exact equation is a Euclidean gradient flow for

\[
\mathcal E(x)=\frac12\sum_i\lambda_i(x_i-s_i)^2+\frac12\sum_{i<j}c_{ij}(x_i-x_j)^2.
\]

Indeed \(\nabla\mathcal E=(\Lambda+L_c)x-\Lambda s\), and for every real \(v\),

\[
v^T(\Lambda+L_c)v=\sum_i\lambda_i v_i^2+\sum_{i<j}c_{ij}(v_i-v_j)^2\ge0.
\]

The matrix is positive definite precisely when every connected component of the undirected support graph \(c_{ij}>0\) contains at least one site with \(\lambda_i>0\). In this case the equilibrium \(x_*=(\Lambda+L_c)^{-1}\Lambda s\) is unique, and deviations decay at least at the smallest eigenvalue of \(\Lambda+L_c\); when all \(\lambda_i>0\) a simpler lower bound is \(\min_i\lambda_i\). These are assertions about expected opinions, not independence or convergence of the full density matrix.

If all \(\lambda_i=0\), then \(\sum_i\dot x_i=0\). If the conductance graph is connected, \(L_c\) has one zero eigenvalue and all others positive, so \(x(t)\to\bar x(0)\mathbf1\), where \(\bar x(0)=n^{-1}\sum_i x_i(0)\), exponentially on the zero-sum subspace. Thus a directed input \(W\) cannot induce a directed FJ stationary weighting in this exchange model.

**4. Exact witnesses.** First take

\[
W=\begin{pmatrix}0&1&0\\0&0&1\\1/2&1/2&0\end{pmatrix},\qquad \lambda_i=0,\qquad x(0)=(1,-1,-1)^T.
\]

The symmetric conductance graph is connected, so the actual opinion limit is \((-1/3)\mathbf1\). Directed FJ instead has the normalized left stationary vector \(\pi=(1/5,2/5,2/5)^T\) for \(W\), giving limit \((\pi^Tx(0))\mathbf1=(-3/5)\mathbf1\). These limits differ by \(4/15\) at every vertex.

Second take the three-cycle row-stochastic \(W\) with \(w_{12}=w_{23}=w_{31}=1\) and all other entries zero. Let every \(\lambda_i=1/2\) and \(s=(1,0,-1)^T\). The exact generator has \(c_{ij}=1/2\) for every unordered pair and gives \(x_*=(1/4,0,-1/4)^T\), whereas the reported directed FJ equation gives \((3/7,-1/7,-2/7)^T\). Both examples obey the stated parameter ranges.

## Verification

The included standard-library Python file `verify.py` reconstructs the full classical \(2^n\)-configuration Markov generator induced by the quantum dissipators (equivalent to the exact diagonal dynamics) and checks by rational arithmetic, configuration by configuration, the identity

\[
D Q=-(\Lambda+L_c)D+(\Lambda s)\mathbf1^T,
\]

where \(D_{i,b}=1-2b_i\). It verifies both exact three-agent witnesses and tests 48 additional deterministic pseudo-random parameter matrices with \(2\le n\le5\). The all-dimension theorem follows from the operator proof, not the finite tests. To reproduce, run `python3 verify.py` with the standard library; success prints `VERIFICATION PASSED`.

## Relationship to prior work

Chu, *A quantum model of opinion dynamics on networks*, arXiv:2607.01452 (first public version July 1, 2026), gives precisely the two-body exchange Lindblad equation above (Eq. 14), the exact diagonal Markov interpretation (Eqs. 17–28), the claimed directed FJ reduction (Eqs. 32–34), and a numerical discrepancy attributed to correlation feedback (Section 4.1.1). The present finding corrects the **model-specific inference**: incoming exchange operations were omitted from the reduced single-site equation, and all first moments actually close exactly. The source's statement about covariance generation is not contradicted; only the proposed causal feedback into these first moments is.

Symmetric exclusion on arbitrary weighted undirected graphs and exclusion with reservoirs are classical processes, including the general treatment by Schulman and Sinclair (arXiv:2607.22991, 2026), and the spin/exclusion correspondence studied by Mendonça (arXiv:1207.4106, 2012). Their framework explains the mathematical form of the corrected Laplacian dynamics; **no novelty is claimed for general exclusion-process moment closure or graph heat flow**. The claimed contribution is the specific correction/no-go in the cited new opinion model and the explicit disagreement in its predicted consensus selection and anchored equilibrium.

## Limitations

The conclusion applies to the literal pair-exchange jumps and rates in Eq. 14, not to a modified one-site influence generator which might truly realize directed FJ dynamics. It does not determine two-body covariances, coherent phases, quantum mutual information, or the entire stationary density matrix. The counterexample with no anchors concerns the accessible first moments and does not imply a unique stationary density matrix. The general mathematics of symmetric exclusion is established prior theory; independent evaluation of the specific model-comparison finding is not claimed here.

## References

1. W. Chu, *A quantum model of opinion dynamics on networks*, arXiv:2607.01452, first posted 2026-07-01. https://arxiv.org/abs/2607.01452
2. L. J. Schulman and A. Sinclair, *Mixing times and spectra of non-equilibrium symmetric exclusion processes on general graphs*, arXiv:2607.22991, first posted 2026-07-25. https://arxiv.org/abs/2607.22991
3. J. R. G. Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs*, arXiv:1207.4106, 2012. https://arxiv.org/abs/1207.4106
