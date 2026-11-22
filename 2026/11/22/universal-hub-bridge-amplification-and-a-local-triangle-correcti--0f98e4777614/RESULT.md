# Universal hub-bridge amplification and a local-triangle correction in two-community epidemic thresholds

## Finding
Let \(d\ge2\) be fixed. For every integer \(n>d\) for which a connected simple \(d\)-regular graph \(H\) on \(n\) vertices exists, choose any vertex \(v\) of \(H\). Form two connected graphs on two copies of \(H\), each with exactly \(n\) intercommunity edges: \(M\) uses a perfect matching between corresponding vertices, whereas \(F\) connects \(v\) in the first copy to all \(n\) vertices of the second copy. Write \(\rho(G)\) for the Perron root of a graph's adjacency matrix, and \(\tau(G)=1/\rho(G)\) for the homogeneous spectral SIS invasion threshold.

The matching construction has \(\rho(M)=d+1\), whereas the fan construction has the **unique** root \(\lambda>d\) of
\[
\lambda-d=n\langle e_v,(\lambda I-A_H)^{-1}e_v\rangle.
\]
If \(t_v=(A_H^3)_{vv}\), equivalently twice the number of triangles of \(H\) through \(v\), then uniformly over **all** such graphs and choices of \(v\), as \(n\to\infty\) with \(d\) fixed,
\[
\boxed{\rho(F)=\sqrt n+\frac d2+\left(\frac d2+\frac{d^2}{8}\right)n^{-1/2}+\frac{t_v-d^2}{2n}+O_d(n^{-3/2}).}
\]
Consequently \(\tau(M)=1/(d+1)\), \(\tau(F)\sim n^{-1/2}\), and \(\tau(M)/\tau(F)\sim\sqrt n/(d+1)\), although the **entire community-induced graphs, their local thresholds \(1/d\), community sizes, and total intercommunity edge counts are identical**. The first asymptotic coefficient that detects within-community structure beyond its regular degree is the local triangle count \(t_v\).

## Assumptions and scope
Graphs are finite, simple, unweighted, undirected, and connected. The two community-induced graphs are isomorphic to the same \(d\)-regular graph. Every edge carries the same homogeneous transmission parameter. The asserted threshold is the inverse adjacency Perron root used in an independent-neighbor or N-intertwined mean-field SIS linearization, **not** an exact almost-sure persistence threshold for a finite-state stochastic epidemic. The asymptotic is over arbitrary admissible sequences of \(d\)-regular graphs with \(d\) fixed and all hub vertices; the constant implicit in \(O_d\) depends only on \(d\).

## Proof
**1. Matched case.** The adjacency matrix of \(M\) is \(\begin{psmallmatrix}A_H&I\\I&A_H\end{psmallmatrix}\). Every row sums to \(d+1\); the constant positive vector is an eigenvector, and the row-sum spectral bound makes \(\rho(M)=d+1\).

**2. A scalar equation for the fan.** Let \(\mathbf1\in\mathbb R^n\) be the all-ones vector and \(e_v\) the selected coordinate. The fan adjacency matrix is
\[
B_F=\begin{pmatrix}A_H&e_v\mathbf1^{\mathsf T}\\\mathbf1e_v^{\mathsf T}&A_H\end{pmatrix}.
\]
Since \(F\) is connected, its Perron eigenvector \((x,y)\) is strictly positive. The fan contains each induced copy of \(H\) as a proper subgraph, so \(\lambda=\rho(F)>d\). The second block eigen-equation implies \((\lambda I-A_H)y=x_v\mathbf1\), hence \(y=x_v\mathbf1/(\lambda-d)\). Substitution into the first block gives \(x=(nx_v/(\lambda-d))(\lambda I-A_H)^{-1}e_v\). Its \(v\)-coordinate proves the displayed scalar equation. Conversely any \(\lambda>d\) satisfying that equation produces a strictly positive eigenvector by these same formulas, because the resolvent is a sum of nonnegative matrix powers and \(H\) is connected. Its eigenvalue must therefore be the Perron root. The function \(\lambda-d\) increases strictly, while \(n\langle e_v,(\lambda I-A_H)^{-1}e_v\rangle\) decreases strictly from infinity (its constant-mode residue is positive) to zero. Thus there is precisely one such root.

**3. Uniform large-size expansion.** The fan contains a star with \(n\) leaves; the remaining edges form the disjoint union of two \(d\)-regular graphs. By spectral-radius monotonicity and the operator-norm triangle inequality,
\[
\sqrt n\le\lambda\le\sqrt n+d.
\]
For all sufficiently large \(n\) relative only to \(d\), the uniformly convergent Neumann expansion, with \(\|A_H\|_2=d\), gives
\[
\langle e_v,(\lambda I-A_H)^{-1}e_v\rangle
=\lambda^{-1}+d\lambda^{-3}+t_v\lambda^{-4}+O_d(\lambda^{-5}).
\]
Here the coefficient of \(\lambda^{-2}\) vanishes because the graph is loopless, \((A_H^2)_{vv}=d\), and \((A_H^3)_{vv}=t_v\). These coefficients and the remainder are bounded using only \(d\). Multiplying the exact root equation by \(\lambda\), we obtain
\[
\lambda^2-d\lambda=n\bigl(1+d\lambda^{-2}+t_v\lambda^{-3}+O_d(\lambda^{-4})\bigr).
\]
Set \(s=\sqrt n\), and substitute the ansatz \(\lambda_0=s+a+b/s+c/s^2\). Matching the coefficients of \(s\), \(1\), and \(s^{-1}\) gives, respectively,
\[
a=d/2,\qquad b=d/2+d^2/8,\qquad c=(t_v-d^2)/2.
\]
At \(\lambda_0\) the original scalar equation has residual \(O_d(s^{-3})\), equivalently the equation multiplied by \(\lambda\) has residual \(O_d(s^{-2})\). For the original form \(f(\lambda)=\lambda-d-nR_v(\lambda)\) we have \(f'(\lambda)=1+n\langle e_v,(\lambda I-A_H)^{-2}e_v\rangle\ge1\). On the relevant interval \(f'(\lambda)\) is bounded below by a positive constant and \(\lambda\asymp s\); the multiplied equation's derivative is \(\asymp_d s\). Therefore the mean-value theorem yields \(\lambda-\lambda_0=O_d(s^{-3})\), as claimed. Uniformity holds because all diagonal closed-walk counts satisfy \(0\le(A_H^k)_{vv}\le d^k\).

**4. Separation and the triangle term.** Inverting the Perron roots yields the claimed spectral thresholds. For illustration of the local correction with identical degree and order, set \(n\) to a multiple of \(12\), large enough to ensure each cycle factor has at least four vertices. The \(4\)-regular graphs \(C_{n/4}\mathbin{\square}C_4\) and \(C_{n/3}\mathbin{\square}C_3\) have, respectively, \(t_v=0\) and \(t_v=2\) at every vertex. Their fan Perron roots therefore differ by \(n^{-1}+O(n^{-3/2})\). The community and intercommunity edge budgets in the two configurations remain identical.

## Verification
Run `python3 VERIFY.py` from the extracted package. The standalone standard-library checker independently constructs finite matched and fan contact networks, computes the fan Perron root using positive power iteration, computes it again from the scalar resolvent equation, and tests the expansion for nine cycle and Cartesian-cycle examples, including same-order triangle-free and triangle-containing regular graphs. These numerical tests are not substituted for the uniform proof above.

## Relationship to prior work
Dung and Phuc (2026) define the community-local threshold set and prove the general comparison \(\tau(G)\le\tau(C_g)\). Sahneh, Scoglio, and Chowdhury (2012) supply broader resolvent-based epidemic coupling theory. Wang et al. (2013) analyze arbitrary interconnection matrices and explicitly establish the matching-eigenvalue formula used in Step 1, plus bounds and perturbations. Those earlier formulas and spectral modeling conventions are **not** claimed as new. The added result is the explicit, all-regular-communities bridge-concentration asymptotic with its universal \(n^{-1/2}\)-threshold regime and the first motif-sensitive coefficient \(t_v/(2n)\), under a strictly matched intercommunity edge budget.

## Limitations
All results are for the **spectral linearization** and fixed bounded regular degree. Actual finite-state stochastic SIS epidemics become extinct almost surely in finite time. These asymptotics neither control true stochastic extinction times nor the size of a nonlinear endemic state. The fan concentrates \(n\) intercommunity contacts on one vertex, so the result does not apply to uniformly bounded total degrees across both layers. Historical priority is bounded by the cited source inspection and searches, not independently certified.

## References
1. Hoang Phi Dung and Nguyen Hong Phuc, *An Epidemic Threshold Set for Networks* (first public version July 15, 2026), https://arxiv.org/abs/2607.14048 .
2. Faryad Darabi Sahneh, Caterina Scoglio, and Fahmida N. Chowdhury, *Effect of Coupling on the Epidemic Threshold in Interconnected Complex Networks: A Spectral Analysis* (2012), https://arxiv.org/abs/1212.4194 .
3. Huijuan Wang, Qian Li, Gregorio D'Agostino, Shlomo Havlin, H. Eugene Stanley, and Piet Van Mieghem, *Effect of the Interconnected Network Structure on the Epidemic Threshold* (2013), https://arxiv.org/abs/1303.0781 .
4. *Measure-theoretic bounds on the spectral radius of graphs from walks* (2021), https://doi.org/10.1016/j.laa.2021.04.023 .
