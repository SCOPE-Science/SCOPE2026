# Independent mathematical audit

## correctness

PASS

The unwrapped density integrates to one, and summing the geometric series and its first-moment series over positive wrapping shifts gives the stated positive density on the fixed branch. Let F_t(λ)=1/(t+b_λ)−λ. The log-ratio derivative is F_t(λ₂)−F_t(λ₁). The λ-derivative of F_0 has the opposite sign to K(λ), since b²+b′=K/(exp(Lλ)−1). All terms of K′ are positive and K(0)=L(4−L)<0, proving the unique positive root and the sign switch. At the terminal point the numerator controlling ∂_λF_L is strictly negative because (b+L)²+b′=(λ+2)²+1+L exp(Lλ)[2(λ+2)+L]/(exp(Lλ)−1)>0. For λ≥λ*, ∂_λF_t<0 at all interior t: if b′≥0 this is immediate, and if b′<0 the relevant reciprocal-square term strictly decreases with t. For each smaller λ, continuity gives a positive initial log-ratio slope for nearby larger parameters, but the terminal slope is still negative. For any pair the slope is negative everywhere if b₂≥b₁; otherwise it is strictly decreasing in t, so D=0 still gives strict decrease on the open branch, and D>0 gives exactly one maximum. Independent interval arithmetic gave K(0.18008)∈[-700,-545]×10⁻⁶, K(0.18009)∈[652,777]×10⁻⁶ and D(0.10,0.11)∈[1088,1093]×10⁻⁶; numerical bisection gives angle 0.46901006. The test-region consequence is the simple-pair Neyman–Pearson rule; no general UMP statement follows.

## originality

PASS

The wrapped density and the unwrapped likelihood-ratio theorem are prior premises. The best-supported distinct content is the sharp parameter boundary plus the exact pairwise shape classification of likelihood ratios on the fixed angular branch. The literature and catalogue comparisons were bounded; no inspected statement gives this classification by specialization.

## value

PASS

Likelihood-ratio ordering has a concrete interpretation in testing and does not survive wrapping by a straightforward preservation rule. The exact fixed-origin threshold decides whether all higher-parameter alternatives have lower-angle likelihood-ratio regions, and the pair criterion identifies when interior regions replace that geometry. The result is a full boundary and classification for a published model, not a selected numerical example or a reinterpretation of the known density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
