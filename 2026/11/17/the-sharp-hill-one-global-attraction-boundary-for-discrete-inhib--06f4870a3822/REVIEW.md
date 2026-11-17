# Scientific review

## Correctness — PASS

For the map displayed in RESULT.md, one iterate enters the strictly positive invariant box \(K\). In logarithmic coordinates its exact Jacobian row-sum majorant is \(1-\alpha_i[1+(1-h)S_i]/[(1+S_i)^2F_i(x)]\), which is at most \(1-\delta<1\) on \(K\). Banach contraction gives the unique positive equilibrium and the stated geometric estimate. The scalar flip construction checks \(H(0)>0\), \(H(t)=0\), and \(H'(t)>0\), which forces a prime-two orbit when \(h>1\). The two-gene dimer orbit has exact full-plane two-step multipliers \(4/a^2\) and \(4(1-2\varepsilon)^2/a^2\), both below one for \(a>2\). The checker confirms the key symbolic identities; finite examples do not substitute for the general proof.

## Originality — PASS within inspected evidence

The 2026 Falęcki–Rosman–Palczewski–Pilarczyk–Bartłomiejczyk paper (arXiv:2603.03850v1), fully inspected via its online HTML article, studies finite-resolution Conley–Morse dynamics at exponent \(h=3\), and does not imply a global no-cycle theorem for arbitrary nonnegative inhibitory networks with \(h\le1\). The 2024/2025 Rosman–Palczewski–Pilarczyk–Bartłomiejczyk paper (arXiv:2411.16699v2), fully inspected, proves an absorbing-box statement across integer exponents and numerically explores higher exponents, but not the logarithmic contraction or sharp parameter-free exponent boundary. Neunhäuserer's 2025 full-text article (arXiv:2509.11881) treats chaos for \(h\ge3\), and explicitly characterizes \(h=1,2\) as seemingly nonchaotic rather than proving global attraction. The 2023 Subramani et al. article's full HTML studies bifurcations and fractional variants. Closest known standard method is contraction in logarithmic coordinates; its classical availability does not by itself cover the exact model, network-uniform classification and sharp dimer construction. Search results and prior result records did not show covering implications. Historical priority remains provisional due to incomplete access to some older articles.

## Value — PASS

In the biologically motivated reciprocal-Hill inhibitory motif, the theorem determines a precise all-parameter boundary between guaranteed monostability and the possible onset of cyclic behavior. It is global in phase space and general in network dimension, interaction topology, and magnitudes, while yielding an explicit reproducible convergence factor. The exact attracting two-gene dimer orbit shows the threshold is not merely a local-spectral artifact. This resolves a natural gap left by numerical multimerization studies and can guide interpretation of gene-circuit simulations. The result does not imply behavior for other repression laws or complex regulatory biology.

## Closest literature and limitations

The source studies' absorbing bounds and high-Hill chaos are acknowledged rather than relabeled. The primary 2007 source and an older 2019 study were not fully inspectable; these are residual historical risks rather than evidence of absence. The sharpness assertion is existential above \(h=1\), and the rate depends on upper bounds for the chosen initial state. This is a proof-level self-review, not external validation.

Self-review: passed. Independent audit: not yet performed.
