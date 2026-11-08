# Exact path-law duality and observable information in heterochaos baker centers

## Finding

For the generalized two-dimensional heterochaos baker map with integer branch count \(M\geq2\), let \(0<a<1/M\), \(p=Ma\) and \(q=1-p\). Under invariant normalized planar Lebesgue measure, write \(Y_t\) for the center coordinate at time \(t\). The following are simultaneous, exact statements.

1. The stationary process \((Y_t)_{t\geq0}\) is a Markov chain on \([0,1)\) with uniform one-time marginal and transition kernel
   \[
   K_p(y,\mathrm dz)=\frac pM\sum_{k=0}^{M-1}\delta_{(y+k)/M}(\mathrm dz)+q\,\delta_{\{My\}}(\mathrm dz).
   \]
   For every integer \(n\geq1\), the consecutive observed pairs \((Y_t,Y_{t+1})\), \(0\leq t<n\), almost surely determine **all** the independent branch decisions: the \(M\) contraction labels and the expanding label.
2. If \(P_p^{(n)}\) is the distribution of \((Y_0,\ldots,Y_n)\), and \(N_n\) counts observed contracting steps, then for any \(p,p'\in(0,1)\), writing \(q'=1-p'\),
   \[
   \frac{\mathrm dP_p^{(n)}}{\mathrm dP_{p'}^{(n)}}
      =\left(\frac p{p'}\right)^{N_n}
        \left(\frac q{q'}\right)^{n-N_n}\quad P_{p'}^{(n)}\text{-almost surely}.
   \]
   Consequently, the exact finite-sample quantities are
   \[
   D(P_p^{(n)}\|P_{p'}^{(n)})
     =n\left[p\log\frac p{p'}+q\log\frac q{q'}\right],
   \]
   \[
   \operatorname{TV}(P_p^{(n)},P_{p'}^{(n)})
     =\frac12\sum_{j=0}^{n}\binom nj
        \left|p^jq^{n-j}-(p')^j(q')^{n-j}\right|,
   \]
   and
   \[
   \int\sqrt{\mathrm dP_p^{(n)}\,\mathrm dP_{p'}^{(n)}}
      =\bigl(\sqrt{pp'}+\sqrt{qq'}\bigr)^n.
   \]
   The count \(N_n\sim\operatorname{Bin}(n,p)\) is sufficient for \(p\), and the information of the observed center path equals that of \(n\) independent Bernoulli trials, with Fisher information \(n/(pq)\). The infinite center-path laws for any two distinct parameters are mutually singular, although all their one-time marginals are Lebesgue measure.
3. Under path reversal \(R_n(y_0,\ldots,y_n)=(y_n,\ldots,y_0)\),
   \[
   (R_n)_*P_p^{(n)}=P_q^{(n)}.
   \]
   Hence the stationary center process is reversible if and only if \(p=q=1/2\), equivalently \(a=1/(2M)\). Its finite-path log-reversal likelihood, \(S_n=\log[\mathrm dP_p^{(n)}/\mathrm d((R_n)_*P_p^{(n)})]\), has the **exact** law
   \[
   S_n=(2N_n-n)\log(p/q),\qquad N_n\sim\operatorname{Bin}(n,p).
   \]
   In particular \(\mathbb E S_n=n(p-q)\log(p/q)\), \(S_n/n\to(p-q)\log(p/q)\) almost surely, and, for attainable values \(s\),
   \[
   \frac{\mathbb P(S_n=s)}{\mathbb P(S_n=-s)}=e^s.
   \]
   The reversal-entropy rate vanishes **exactly** where the known central Lyapunov exponent \((q-p)\log M\) vanishes.

## Assumptions and scope

Take \([0,1)\) with Lebesgue probability \(\lambda\); all interval boundaries are assigned a fixed half-open convention. Let \(\tau_a\) have \(M+1\) full branches: for \(k\in\{0,\ldots,M-1\}\), the branch \(x\in[ka,(k+1)a)\) maps to \((x-ka)/a\); the remaining branch \(x\in[Ma,1)\) maps to \((x-Ma)/(1-Ma)\). The two-dimensional map is
\[
 f_a(x,y)=\begin{cases}
 (\tau_a(x),(y+k)/M),&x\in[ka,(k+1)a),\quad 0\leq k<M,\\
 (\tau_a(x),\{My\}),&x\in[Ma,1).
 \end{cases}
\]
Start \((X_0,Y_0)\sim\lambda\otimes\lambda\). This is an invariant probability for \(f_a\); no uniqueness of stationary law is asserted. All path claims are under this initial distribution. Exact identities apply for every \(M\geq2\), every \(0<p,p'<1\), and every \(n\geq1\), not only asymptotically. Boundary parameters \(p=0,1\) are excluded; the exceptional countable set of branch-boundary or coincident-graph trajectories is null.

## Proof

**Independent driver.** On each full branch of \(\tau_a\), the conditional image of a uniform point is uniform on \([0,1)\), and the branch length is its selection probability. Inductively, successive base branch labels are independent, with probabilities \(a=p/M\) for each contracting branch and \(q\) for the single expanding branch. The entire sequence of these labels is independent of \(Y_0\). Therefore the center coordinate obeys the claimed Markov kernel.

**Stationarity and adjoints.** Set \(T(y)=\{My\}\), \(U\varphi(y)=\varphi(Ty)\), and \(L\varphi(y)=M^{-1}\sum_{k=0}^{M-1}\varphi((y+k)/M)\). By substituting \(z=(y+k)/M\) on each branch, for bounded measurable \(\varphi,\psi\),
\[
 \int\varphi L\psi\,\mathrm d\lambda
 =\int (U\varphi)\psi\,\mathrm d\lambda.
\]
Thus \(U^*=L\), \(L^*=U\) on \(L^2(\lambda)\), and \(U1=L1=1\). Accordingly \(K_p=pL+qU\) preserves \(\lambda\), and its stationary reverse kernel is \(K_p^*=pU+qL=K_q\). Inducting on the Markov finite-dimensional distributions proves \((R_n)_*P_p^{(n)}=P_q^{(n)}\).

**Almost-sure recovery from the observed path.** A contraction step has \(Y_{t+1}=(Y_t+k)/M\) for exactly one \(k\in\{0,\ldots,M-1\}\); an expansion step has \(Y_{t+1}=T(Y_t)\). The contraction graphs are mutually disjoint. For a contraction graph and the expansion graph to intersect, \(Y_t\) must solve \((Y_t+k)/M=MY_t-j\) for some integers \(0\leq j,k<M\), hence \(Y_t=(Mj+k)/(M^2-1)\). This is a finite set. Because each \(Y_t\) has law \(\lambda\), it is avoided at every integer time almost surely. Thus all branch labels up to time \(n-1\) are measurable functions of \((Y_0,\ldots,Y_n)\).

**Exact likelihood and information.** A path is the measurable image of \((Y_0,B_0,\ldots,B_{n-1})\), where \(Y_0\sim\lambda\) is parameter-independent and the \(B_t\) are independent categorical labels with respective probabilities \(p/M,\ldots,p/M,q\). The almost-sure recovery just proved shows this mapping has an inverse, modulo common null sets, on its image. Therefore it preserves all likelihood ratios and all \(f\)-divergences of the two experiments. Multiplying categorical likelihood ratios gives the displayed Radon–Nikodym derivative; integrating its logarithm gives the relative entropy. Conditional on contraction, the label is uniformly distributed, independently of \(p\), so \(N_n\) is sufficient. Grouping the product masses by the binomial count gives the exact total-variation expression and Hellinger affinity. Differentiating the log likelihood gives score \(N_n/p-(n-N_n)/q\) and variance \(n/(pq)\), establishing the Fisher information. The strong law gives \(N_n/n\to p\) almost surely. These almost-sure limit events are disjoint for distinct \(p\), proving singularity of the infinite path laws.

**Time reversal and fluctuation identity.** Apply the likelihood formula with \(p'=q\) and use the already proved reversal identity. This gives \(S_n=(2N_n-n)\log(p/q)\). Since \(\mathbb P(N_n=j)=\binom nj p^jq^{n-j}\), taking the ratio of the probabilities of \(j\) and \(n-j\) gives \((p/q)^{2j-n}=e^{S_n}\). The strong law and expectation provide the entropy rate. If \(p=q\), the reverse kernel equals the forward kernel. If \(p\ne q\), the path likelihoods differ on a positive-probability event already at one step (and their mean entropy is strictly positive), so the stationary chain is not reversible. Finally the center derivative is \(1/M\) on contracting steps and \(M\) on expanding steps, giving Lyapunov exponent \((q-p)\log M\). Its only zero is also the only zero of the entropy-production rate.

## Verification

The attached pure-standard-library `check.py` uses rational arithmetic. For \(M\in\{2,3,4,6,8\}\), and probabilities \(p\in\{1/5,1/3,1/2,3/4,9/10\}\), it checks the adjoint identities and stationarity against all polynomial monomials of degrees at most five, categorical normalization of all driver words of lengths one through four, exact binomial fluctuation ratios, and distinct branch outputs at a generic rational input. It additionally traces 450 exact-rational initial states through eight deterministic iterations and verifies the branch-label decoding whenever the transition graphs do not coincide. Run `python check.py`. These finite checks test implementations and special cases; the proof above establishes the universal statements without reliance on numerical sampling.

## Relationship to prior work

Homburg and Kalle (arXiv:2207.09987, §§1–2) give the closely related random expanding/contracting interval system, prove Lebesgue stationarity, and analyze the two-point dynamics. Takahasi (arXiv:2307.08119, §1) defines the generalized heterochaos baker map and establishes mixing properties. Saiki, Takahasi, Yamamoto and Yorke (arXiv:2401.00836, §§1–2) review its center Lyapunov phase transition. Takahasi and Tsujii (arXiv:2408.16618, §§1–2) study center-coordinate transfer operators and sharp critical correlation decay. These works supply the map and known one-time and correlation properties; their inspected statements do not give the observed-center path-law likelihood equivalence, complete parameter comparison, or the exact reversal duality. The fluctuation-ratio step itself is an application of established detailed-balance/entropy-production principles, not a new general fluctuation theorem.

## Limitations

Only the stationary center coordinate is observed, under the specified Lebesgue initial law and the symmetric choice of contraction probabilities. The full planar map need not be reversible even when the center-coordinate path is. One-time marginal equality does not imply equality of path laws. The assertions do not extend as stated to arbitrary dependent switching, arbitrary initial distributions, different expansion bases, or observation corrupted by noise. A general independent full-text or publication-priority audit is not supplied; an equivalent path-law computation in unindexed literature is possible.

## References

- A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, arXiv:2207.09987v1, 2022-07-20, §§1–2. https://arxiv.org/abs/2207.09987
- H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119v1, 2023-07-16, §1 and main mixing results. https://arxiv.org/abs/2307.08119
- Y. Saiki, H. Takahasi, K. Yamamoto and J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836v1, 2024-01-01, §§1–2. https://arxiv.org/abs/2401.00836
- H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, arXiv:2408.16618v1, 2024-08-29, §§1–2. https://arxiv.org/abs/2408.16618
- R. J. Martin and I. J. Ford, *Stochastic entropy production in diffusive systems*, Journal of Physics A **53** (2020) 255001, for the general path-reversal entropy framework; no novelty in the general fluctuation identity is claimed.
