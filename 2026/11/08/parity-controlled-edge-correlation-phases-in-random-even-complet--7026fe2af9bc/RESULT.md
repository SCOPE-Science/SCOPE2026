# Parity-controlled edge-correlation phases in random even complete graphs

## Finding

Let \(n\ge4\) and \(0<p<1\). Draw \(G\sim G(n,p)\), conditional on all its degrees being even. For two distinct possible edges \(e,f\) write \(X_e=\mathbf1\{e\in E(G)\}\). Then the complete finite-order sign classification is:

* For **disjoint** \(e,f\), \(\operatorname{Cov}(X_e,X_f)>0\) whenever \(p\ne\tfrac12\), and the covariance is zero at \(p=\tfrac12\).
* For **incident** \(e,f\), if \(n\) is even, the covariance is positive for \(p<\tfrac12\), zero at \(p=\tfrac12\), and negative for \(p>\tfrac12\).
* For **incident** \(e,f\), if \(n\) is odd, the covariance is positive for every \(p\ne\tfrac12\), and zero at \(p=\tfrac12\).

Thus density beyond one half creates negative local dependence at a shared endpoint **exactly for even vertex order**, whereas disjoint edges remain positively dependent. All inequalities stated as strict are strict for finite \(n\).

## Assumptions and scope

The graph is labeled, simple and complete before independent edge thinning. The conditioning event (every degree even) has strictly positive probability for \(0<p<1\). Every covariance refers to the conditional law, **not** unconditioned \(G(n,p)\). By edge-permutation symmetry the answer depends only on whether the edges share a vertex. The theorem covers all \(n\ge4\) and all real \(p\in(0,1)\), including the central point. It does not assert a general sign law for arbitrary host graphs.

Put \(t=p/(1-p)\). For an even-cardinality vertex set \(A\subseteq[n]\), let
\[
Z_A(t)=\sum_{F\subseteq E(K_n):\,\partial F=A}t^{|F|},
\]
where \(\partial F\) is the set of vertices of odd degree in \(F\). Write \(r_2=Z_{\{1,2\}}(t)/Z_\varnothing(t)\) and \(r_4=Z_{\{1,2,3,4\}}(t)/Z_\varnothing(t)\). These ratios are well-defined and strictly positive.

For \(t\ne1\), the exact covariance kernels are
\[
C_{\rm incident}=\frac{t^2}{(1-t^2)^2}\,r_2(1-r_2),\qquad
C_{\rm disjoint}=\frac{t^2}{(1-t^2)^2}\,(r_4-r_2^2).
\]

## Proof

**1. Source-sector representation and the covariance kernel.** Introduce independent edge fugacities \(t_e>0\), and the polynomial
\[
Z_\varnothing(\boldsymbol t)=2^{-n}\sum_{\sigma\in\{-1,1\}^n}\prod_{ij\in E(K_n)}(1+t_{ij}\sigma_i\sigma_j).
\]
Expanding the product and summing spins eliminates every term whose odd-degree boundary is nonempty, giving precisely the even-subgraph partition function. Under fugacity weights, the indicator mean is \(t_e\partial_{t_e}\log Z_\varnothing\), and the covariance for different edges is \(t_et_f\partial_{t_e}\partial_{t_f}\log Z_\varnothing\). At equal fugacity \(t\ne1\), the algebraic identity
\[
\frac{\sigma_i\sigma_j}{1+t\sigma_i\sigma_j}=\frac{\sigma_i\sigma_j-t}{1-t^2}
\]
reduces the mixed derivative to \(t^2/(1-t^2)^2\) times the connected spin-products formed by the two marked edges. The signed spin sum represents \(Z_A(t)/Z_\varnothing(t)\), irrespective of whether \(t<1\) or \(t>1\). Incident edges have symmetric-difference boundary of size two; disjoint edges have size four. The displayed exact kernels follow.

**2. Ferromagnetic complete-graph moments for \(0<t<1\).** Put \(\beta=\operatorname{arctanh}(t)>0\). Then \(1+t\sigma_i\sigma_j\) is a constant multiple of \(e^{\beta\sigma_i\sigma_j}\), yielding the zero-field Curie--Weiss Ising law. The identity
\[
\sum_{i<j}\sigma_i\sigma_j=\frac12\bigl[(\sum_i\sigma_i)^2-n\bigr]
\]
and a one-dimensional Gaussian integral give a real latent field \(H\), whose density is proportional to
\[
\exp\!\left(-\frac{h^2}{2\beta}\right)(2\cosh h)^n.
\]
Conditional on \(H=h\), the spins are independent with mean \(\tanh h\). Therefore for every fixed even set \(A\), \(Z_A(t)/Z_\varnothing(t)=m_{|A|/2}\), where
\[
Y=\tanh^2 H,\qquad m_j=\mathbb E[Y^j].
\]
The random variable \(Y\) is nonconstant with \(0\le Y<1\) almost surely and \(\mathbb P(Y>0)>0\). Hence \(0<m_1<1\) and \(m_2>m_1^2\), by strict variance. Both covariances are strictly positive when \(p<\tfrac12\).

**3. Complementation and the two high-density parity regimes.** For any \(A\), complementing edge sets gives the exact identity
\[
Z_A(t)=t^{\binom n2}Z_{A\triangle\partial K_n}(t^{-1}).
\]
If \(n\) is odd, \(\partial K_n=\varnothing\). Thus for \(t>1\), the ratios \(r_2,r_4\) coincide with their values at \(t^{-1}<1\), and the same positive signs hold.

If \(n\) is even, \(\partial K_n=[n]\). Use the latent law from step 2 at \(s=t^{-1}\), and put \(j=(n-2)/2\ge1\). Complementation gives
\[
r_2=\frac{m_j}{m_{j+1}}>1,\qquad
r_4=\frac{m_{j-1}}{m_{j+1}}.
\]
The strict inequality uses \(Y<1\) with positive mass away from zero. The incident-edge kernel is therefore strictly negative. For disjoint edges,
\[
r_4-r_2^2=\frac{m_{j-1}m_{j+1}-m_j^2}{m_{j+1}^2}>0.
\]
The numerator is strictly positive by Cauchy--Schwarz applied to \(Y^{(j-1)/2}\) and \(Y^{(j+1)/2}\), with strictness because \(Y\) is nonconstant. This proves the claimed disjoint-edge positivity.

**4. The central point.** At \(p=\tfrac12\), the even subgraphs form a uniform binary cycle space. Every one-edge or two-edge coordinate projection is uniform: its dual orthogonal space is the cut space, and the minimum nonzero cut size in \(K_n\) is \(n-1\ge3\). Thus distinct edge indicators are pairwise independent, so both covariance types are zero. This also handles the singular-looking denominators in the formulas from step 1 without taking any limit.

## Verification

The standalone `verify_even_graphs.py` independently enumerates the binary cycle space for \(n=4,5,6,7\), evaluates exact rational conditional probabilities at seven rational choices of \(p\), and cross-checks each covariance against a separate finite character-sum partition function. It performs 112 exact identity and sign assertions. These finite checks are not used to prove the all-order result. The proof rests on the spin expansion, Gaussian mixture, complementation, and strict moment inequalities above.

To replay: `python3 verify_even_graphs.py` using Python 3's standard library.

## Relationship to prior work

Grimmett and Janson's *Random even graphs* (first arXiv posting 2007-09-19) defines the same even-subgraph measure and proves its connection with Ising and random-cluster laws; its finite-graph sections develop the cycle-space representation and both low- and high-density sampling regimes. That established material supplies the model and foundational identities, not a stated all-order pair-edge covariance sign classification by edge incidence and parity.

Grimmett and Janson's *Random graphs with forbidden vertex degrees* (first arXiv posting 2007-12-03) treats \(G(n,p)\) conditioned on degree restrictions, with primary attention to sparse asymptotics, empirical degree distributions, and giant components. Its finite-order local edge covariance sign pattern was not located in the inspected primary text. The displayed sign laws combine a complete-graph latent moment representation with the complement-induced odd-source comparison; they are not claims about a new random-graph model.

## Limitations

This is a same-source-model mathematical derivation, not an independently audited priority determination. Search and full-text comparison did not establish exhaustive historical uniqueness; a broader unpublished or unlocated covariance formula might subsume it. Only two distinct edges are classified. The method uses complete-graph vertex exchangeability and need not extend to general host graphs. No bounds on covariance magnitude or large-order scaling are asserted.

## References

1. G. Grimmett and S. Janson, *Random even graphs*, arXiv:0709.3039, first submitted 2007-09-19; subsequently *Electronic Journal of Combinatorics* 16(1), R46 (2009), https://arxiv.org/abs/0709.3039.
2. G. Grimmett and S. Janson, *Random graphs with forbidden vertex degrees*, arXiv:0712.0270, first submitted 2007-12-03; subsequently *Random Structures & Algorithms* 37, 137--175 (2010), https://arxiv.org/abs/0712.0270.
