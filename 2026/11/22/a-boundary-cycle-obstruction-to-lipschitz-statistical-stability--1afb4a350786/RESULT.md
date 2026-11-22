# A boundary-cycle obstruction to Lipschitz statistical stability of a planar tent map

## Finding

Let \(\Omega=\{(x,y)\in\mathbb R^2:0\le y\le x,\ x+y\le2\}\), a triangle of Euclidean area \(1\). The two-branch continuous map \(F_1:\Omega\to\Omega\) is
\[
F_1(x,y)=\begin{cases}
(x+y,x-y),&0\le x\le1,\\
(2-x+y,2-x-y),&1\le x\le2.
\end{cases}
\]
For \(\tau\le t\le1\), put \(F_t=tF_1\), where \(\tau=2^{-1/2}(1+\sqrt2)^{1/4}\). Denote by \(\mu_t=\rho_t\,dm\) the unique absolutely continuous invariant probability measure of \(F_t\), whose existence and uniqueness are established in the cited literature, and by \(m\) Euclidean area on \(\Omega\) (already a probability measure).

**Theorem.** The endpoint invariant density is \(\rho_1=1\). As \(t\uparrow1\),
\[
\boxed{\lim_{t\uparrow1}\frac{\|\rho_t-1\|_{L^1(\Omega)}}{1-t}=+\infty.}
\]
Indeed, for *every* sequence \(t_j\uparrow1\), the signed measures \(\eta_{t_j}=(\mu_{t_j}-m)/(t_j-1)\) admit no weak-* convergent subsequence in the space of finite signed Borel measures \(C(\Omega)^*\). In particular, there is no finite-measure-valued one-sided linear response at the full-height endpoint.

## Assumptions and scope

The parameter satisfies \(\tau\le t\le1\), with only the limit from below considered. The map is defined at the common branch boundary \(x=1\) by either formula; they agree. Absolute continuity and the unique stationary probability for this family are inputs from Pumariño--Rodríguez--Tatjer--Vigil (2015), as recalled by Alves--Etubi (2024). The theorem does not assume differentiability or regularity of \(\rho_t\) beyond integrability, and it does not claim a response derivative in a distribution space larger than finite measures.

## Proof

**1. The full-branch endpoint.** The two domains \(R_1=\Omega\cap\{x\le1\}\) and \(R_2=\Omega\cap\{x\ge1\}\) both map bijectively onto \(\Omega\) under their affine branches of \(F_1\), and the Jacobian determinants are \(-2\) and \(+2\), respectively. The Perron--Frobenius operator consequently takes constant density \(1\) to \(\tfrac12+\tfrac12=1\). The endpoint probability is therefore \(m\); uniqueness of the ACIP gives \(\mu_1=m\).

**2. The forcing from the moving image.** Since \(F_t(\Omega)=t\Omega\), every invariant probability \(\mu_t\) is supported on \(t\Omega\). More specifically, the pushforward of *unperturbed* area is
\[
\sigma_t=(F_t)_*m=t^{-2}\mathbf1_{t\Omega}m,
\]
where \(m(\Omega)=1\) and \(m(t\Omega)=t^2\). Define three finite positive measures, all of mass \(2\), by their actions on continuous \(\varphi:\Omega\to\mathbb R\):
\[
\begin{aligned}
\langle\nu_R,\varphi\rangle&=2\int_0^1\varphi(2-s,s)\,ds,\\
\langle\nu_B,\varphi\rangle&=\int_0^2\varphi(s,0)\,ds,\\
\langle\nu_L,\varphi\rangle&=2\int_0^1\varphi(s,s)\,ds.
\end{aligned}
\]
For every continuous \(\varphi\), use \(u=x+y\), \(v=y\), with Jacobian \(1\), to compute the shrinking cap:
\[
\begin{aligned}
\frac{1}{1-t}\int_{\Omega\setminus t\Omega}\varphi\,dm
&=\frac{1}{1-t}\int_{2t}^2\int_0^{u/2}\varphi(u-v,v)\,dv\,du\\
&\longrightarrow2\int_0^1\varphi(2-v,v)\,dv
=\langle\nu_R,\varphi\rangle.
\end{aligned}
\]
Since \(t^{-2}-1=2(1-t)+o(1-t)\), the signed measure
\[
B_t=\frac{(F_t)_*m-m}{t-1}
\]
converges weak-* to \(B=\nu_R-2m\). This is a finite signed measure, not merely a distribution.

**3. A persistent boundary cycle.** The branch formulas imply the following exact equalities of measures:
\[
(F_1)_*\nu_R=\nu_B,\qquad(F_1)_*\nu_B=\nu_L,\qquad(F_1)_*\nu_L=\nu_B.
\]
For the first, the right side is parametrized by \((2-s,s)\), which maps to \((2s,0)\). For the second, the two halves of the bottom side map onto the same diagonal, each with unit parameter density. For the third, \((s,s)\mapsto(2s,0)\). Also \((F_1)_*m=m\). Consequently,
\[
\frac1N\sum_{k=0}^{N-1}(F_1)_*^k B\longrightarrow
K=\frac12(\nu_B+\nu_L)-2m
\]
in total variation as \(N\to\infty\). The limiting signed measure \(K\) is nonzero: its boundary-supported part has mass \(2\), whereas \(2m\) gives the boundary zero mass (equivalently, test a nonnegative continuous function supported in the interior).

**4. Impossibility of a finite signed derivative.** Suppose for a contradiction that there exists a sequence \(t_j\uparrow1\) for which
\[
\eta_{t_j}=\frac{\mu_{t_j}-m}{t_j-1}\overset{*}{\rightharpoonup}\eta
\]
for some finite signed measure \(\eta\). Since \(\Omega\) is compact, Banach--Steinhaus gives \(\sup_j\|\eta_{t_j}\|_{\rm TV}<\infty\). Invariance of \(\mu_t\) and \(m\) yields the exact identity
\[
\eta_t=(F_t)_*\eta_t+B_t.
\]
Because \(F_t\to F_1\) uniformly and \(\eta_{t_j}\) have bounded total variation, \((F_{t_j})_*\eta_{t_j}\overset{*}{\rightharpoonup}(F_1)_*\eta\). Passing to the limit produces the measure cohomological equation
\[
(I-(F_1)_*)\eta=B.
\]
Apply Cesàro averages of \((F_1)_*^k\) to this equation. The left side telescopes:
\[
\frac1N\sum_{k=0}^{N-1}(F_1)_*^k B
=\frac{\eta-(F_1)_*^N\eta}{N}.
\]
Its total variation is at most \(2\|\eta\|_{\rm TV}/N\), so it must tend to zero. Step 3 gives the nonzero limit \(K\), a contradiction. Thus no sequence of difference quotients can have a finite signed measure weak-* limit.

**5. Divergence of the density quotient.** If \(\|\rho_t-1\|_1/(1-t)\) failed to tend to infinity, there would be a sequence \(t_j\uparrow1\) along which these ratios were bounded. That is precisely a total-variation bound on \(\eta_{t_j}\). Because \(\Omega\) is a compact metric space, its space of finite signed measures has weak-* sequential compactness on bounded sets (by Banach--Alaoglu and separability of \(C(\Omega)\)). A subsequence would converge, contradicting Step 4. This proves the theorem.

## Verification

All nonstandard steps are explicit measure identities: the two branch Jacobians and full-image geometry, the moving-cap weak-* limit, the boundary pushforward three-step pattern, and the total-variation Cesàro obstruction. They require no floating-point computation. The accompanying `CHECK.py` verifies the map Jacobians and the three boundary pushforward identities on all coordinate monomials of total degree at most \(8\) using exact rational arithmetic. These finite checks are consistency tests, not replacements for the preceding all-observable proof. The existence of \(\mu_t\) is taken from the cited primary work rather than reproved.

## Relationship to prior work

Alves and Etubi's 2024 preprint (arXiv:2409.18805, initial version dated 2024-09-27; revised title and journal version in 2025) established continuity estimates for the densities and entropy of this family and explicitly raised the linear-response question. Their continuity theorem does not imply the present divergent Lipschitz quotient. Pumariño and collaborators (2015) established the ACIP framework, not the non-Lipschitz boundary obstruction. Earlier one-dimensional tent-map linear-response failures use different critical-orbit hypotheses and do not imply this specific two-dimensional boundary-cycle argument. The known exact entropy formula in this family is compatible with the failure of measure-valued response.

A completed 2025 thesis titled *On linear response for tent maps* under José Ferreira Alves's supervision is bibliographically relevant; its full text was not accessible for statement-level comparison. Its possible coverage of the specific finite-measure derivative obstruction remains an unresolved publication-priority risk. Also, a published indexed result about the full-height triangular map's stationary Gaussian fluctuations concerns correlations at a fixed parameter, not variation of stationary probabilities.

## Limitations

This is a theorem on a one-sided endpoint, not a claim that no differentiable response exists for all parameters, for each smooth test function, or in spaces of distributions of positive order. The result proves divergence of the \(L^1\)-difference quotient without an asymptotic rate. It relies on the published existence and uniqueness of the ACIP throughout the specified parameter range. Novelty is established relative to material inspected, not guaranteed against inaccessible theses or unindexed literature; no independent scientific audit has been performed.

## References

1. J. F. Alves and O. R. Etubi, *Hölder continuity of invariant density and entropy for piecewise expanding maps*, arXiv:2409.18805v1, first posted 2024-09-27. https://arxiv.org/abs/2409.18805
2. J. F. Alves and O. Etubi, *Modulus of continuity of invariant densities and entropies for piecewise expanding maps*, *Ergodic Theory and Dynamical Systems*, published online 2025-04-07, DOI:10.1017/etds.2025.12. https://doi.org/10.1017/etds.2025.12
3. A. Pumariño, J. Á. Rodríguez, J. C. Tatjer and E. Vigil, *Chaotic dynamics for two-dimensional tent maps*, *Nonlinearity* 28 (2015), 407--434, DOI:10.1088/0951-7715/28/2/407.
4. L. H. S. L. R. Pereira, *On linear response for tent maps*, master's thesis, University of Porto, defended 2025-07-24. Bibliographic record: https://sigarra.up.pt/fcup/en/teses.lista_teses?p_curso=878&p_record_set_size=10&p_tipo_lista=T . Full thesis text was not accessible for inspection.
