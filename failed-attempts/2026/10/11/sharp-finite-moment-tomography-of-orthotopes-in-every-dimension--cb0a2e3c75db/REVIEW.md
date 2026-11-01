# Independent mathematical audit

## correctness

PASS

Verified the exact statement for all fixed d≥2, positive side lengths and Haar sphere U. For q_i=∏_{j≠i}a_j>0, the orthotope facet formula gives B_Q(U)=Σq_i|U_i| and the positive bijection a_i=(∏q_j)^{1/(d−1)}/q_i. Gaussian polar independence G=RU yields h_k=E||G||^k m_k, with E||G||^k=2^{k/2}Γ((d+k)/2)/Γ(d/2). For half-normal X=|N(0,1)|, log M_X(z)=z²/2+log(1+tF(z)), t=√(2/π) transcendental and F(z)=z+O(z³)∈Q[[z]]; the k-th cumulant has nonzero degree-k coefficient (−1)^{k−1}(k−1)!t^k, proving κ_k≠0 for EVERY k without extrapolation. Cumulant additivity gives K_k=κ_k Σq_i^k; Newton identities recover all positive q roots from the first d moments. Constant-term perturbations of distinct-root polynomials yield continuous positive noncongruent q families with identical first d−1 moments. Smooth bounded moment-to-coefficient conversion plus the polynomial-root matching theorem/Rouché argument yield a uniform 1/d Hölder bound on side intervals [ℓ,L]; Vandermonde invertibility yields local Lipschitz at distinct facets; scaled pairs near q=(1,…,1) with equal lower symmetric functions and differing e_d by Θ(ε^d) force optimal exponent exactly 1/d. All normalization, repeated-root cases, and side-bound dependences are consistent. Independent symbolic checker confirmed 11 leading half-normal cumulant coefficients, the positive facet/side inverse for dimensions 2..8, a real cubic constant-term perturbation, and reconstructed the exact seven-entry Git source tree; these bounded checks are not proofs of universal statements.

## originality

FAIL

A genuinely prior primary paper by Omri Abas (arXiv:2608.06348v1, submitted 2026-08-06) proves essentially the same all-dimensional finite moment reconstruction and generic sharp moment count, plus the SAME all-order nonvanishing of standard half-normal cumulants by the transcendence-of-pi highest-degree polynomial argument. By exact zonotope/Cauchy facet formula B_Q(U)=sum_i q_i|U_i|=W_q(U), with q_i=prod_{j!=i}a_j and a_i=(prod_j q_j)^(1/(d−1))/q_i, the submitted brightness distribution is the previously solved orthotope width distribution under a smooth bijective parameter change. Abas Theorem 3.5 proves first d moments recover q; Proposition 3.6 proves d−1 fail generically. The remaining compact-uniform 1/d Hölder continuity and simple-root Lipschitz property follow from classical polynomial-root perturbation estimates (Ostrowski, documented by Beauzamy 1999), and its near-cube optimality from the same scaled constant-term perturbation. Thus no independently novel final all-dimensional tomography theorem survives. This is demonstrated implication, not inference from shared titles or search absence.

## value

FAIL

Reconstructing a positive d-parameter orthotope from d isotropic scalar moments and quantifying near-cube instability are natural inverse-geometry questions. However this precise first-d reconstruction, generic d−1 sharpness and the critical half-normal cumulant nonvanishing proof are all established in the earlier Abas 2026 all-dimensional width paper, whose random observable is EXACTLY the same after an invertible facet-area substitution. The residual 1/d continuity is a standard Ostrowski degree-d polynomial-root bound following mechanically from that published reconstruction, and local simple-root Lipschitz continuity is equally standard. The near-cube exponent witness is a routine scaled version of the published constant-term perturbation. There is no independently undetermined exact invariant, motivated structural lemma or new boundary theorem remaining to carry mathematical value as a research claim; correctness and reproducibility alone do not change this. The result remains a valid restatement/conditioning exercise useful for exposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
