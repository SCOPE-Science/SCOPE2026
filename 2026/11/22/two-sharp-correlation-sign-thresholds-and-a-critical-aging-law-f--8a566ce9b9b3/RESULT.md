# Two sharp correlation-sign thresholds and a critical aging law for mixed-urn draws

## Finding

In a balanced two-color Friedman–Pólya urn whose independently selected replacement rule is Friedman with probability \(p\), the signs of correlations between sampled colors exhibit **two distinct sharp thresholds**. Below the first, correlations are positive; between them, correlations at early sampling ages are negative but at later ages become positive; above the second, they remain negative. The crossover age diverges by a sharp fractional power as the second threshold is approached.

Write \(B=a+b\), where \(0<a<b\). Define
\[
p_0=\frac{a+b}{2b},\qquad p_*=\frac{a+3b}{4b},\qquad p_0<p_*<1.
\]
For all distinct draw times \(1\le i<j\), the exact correlation sign depends only on the earlier index \(i\), not on \(j\). More precisely:

- If \(0<p<p_0\), all correlations are strictly positive.
- If \(p=p_0\), correlations from the first draw are zero and those from all later draws are strictly positive.
- If \(p_0<p<p_*\), their signs, as \(i\) increases, pass exactly once from negative to positive, with possibly one zero at the boundary.
- If \(p_*\le p<1\), all are strictly negative.

In the intermediate regime, define \(n_p=\min\{n\ge0:W_n+h\ge0\}\) using the definitions below. Then, as \(p\uparrow p_*\),
\[
n_p\sim \left(\frac{K_*(b-a)}{8bp_*}\right)^{(a+b)/(2b)}(p_*-p)^{-(a+b)/(2b)},
\qquad K_*=\frac{\Gamma(t+1)}{\Gamma(t+(a-b)/(a+b))},\quad t=\frac{T_0}{a+b}.
\]
At the second threshold, adjacent-draw correlations decay at the strictly faster rate
\[
\lim_{i\to\infty}i^{1+2b/(a+b)}\operatorname{Cov}(S_i,S_{i+1})
=\frac{(a-b)K_*}{2(a+b)}<0.
\]
For \(p\ne p_*\) in the negative-drift regime, adjacent-draw covariances instead have a generally nonzero \(i^{-1}\) leading term, whose sign is that of \(p_*-p\).

## Assumptions and scope

Start with \(m\) balls of each of two colors, where \(m\) is an integer and \(T_0=2m\ge2(a+b)\). Let \(a,b\) be positive integers satisfying \(a<b\). On each step, draw one ball uniformly and return it; independently select the Friedman rule with fixed probability \(p\in(0,1)\), adding \(a\) balls of the drawn color and \(b\) of the opposite color, or select the Pólya rule with probability \(1-p\), adding \(B=a+b\) balls of the drawn color. Let \(S_i=+1\) or \(-1\) encode the sampled color at step \(i\), and \(D_n\) be the difference between the two color populations after step \(n\). Then \(T_n=T_0+nB\), and by color-exchange symmetry \(\mathbb ES_i=0\). Since \(S_i\) has unit variance, every covariance below also equals the Pearson correlation.

Put
\[
h=B-2bp,\qquad q=p(a-b)^2+(1-p)B^2=B^2-4abp,
\qquad W_n=\frac{\mathbb E D_n^2}{T_n},\qquad W_0=0.
\]
For each \(1\le i<j\), the **finite-time exact formula** is
\[
\operatorname{Cov}(S_i,S_j)=\frac{h+W_{i-1}}{T_{j-1}}
\prod_{r=i+1}^{j-1}\left(1+\frac{h}{T_{r-1}}\right).
\]
The empty product is one. This formula, the sign classification, the crossover exponent and the critical decay are the single finding.

## Proof

**Conditional drift and second moment.** The independent replacement increment \(J_i\) is \(a-b\) with probability \(p\) and \(B\) otherwise, and \(D_i=D_{i-1}+J_iS_i\). Since
\[
\mathbb E[S_i\mid\mathcal F_{i-1}]=\frac{D_{i-1}}{T_{i-1}},
\quad \mathbb EJ_i=h,\quad \mathbb EJ_i^2=q,
\]
we obtain
\[
\mathbb E[D_i\mid\mathcal F_{i-1}]
=\left(1+\frac h{T_{i-1}}\right)D_{i-1},
\qquad \mathbb E D_i^2
=\left(1+\frac{2h}{T_{i-1}}\right)\mathbb E D_{i-1}^2+q.
\]
Consequently
\[
W_i=W_{i-1}+\frac{q-(B-2h)W_{i-1}}{T_i}.
\]
When \(h<0\), put \(d=B-2h>0\) and
\[
G_n=\prod_{k=1}^n\frac{T_0+(k-1)B+2h}{T_0+kB},\quad G_0=1.
\]
All factors are strictly between zero and one by the stated bounds on \(T_0\) and \(h\), and the recurrence solves to
\[
W_n=\frac qd(1-G_n).
\]
Thus \(W_n\) increases strictly to \(q/d\). The convergence \(G_n\to0\) follows either by logarithms or from the gamma-ratio identity below, since \(h<0\) gives a positive decay exponent.

**Two-time covariance.** Directly from the sampling formula and independence of \(J_i\),
\[
\mathbb E[S_iD_i]=\mathbb E[D_{i-1}^2/T_{i-1}]+h=W_{i-1}+h.
\]
Iterating conditional expectation of \(D_k\) from time \(i\) to \(j-1\), then conditioning the \(j\)-th draw, produces the displayed exact covariance formula. Every prefactor apart from \(W_{i-1}+h\) is positive; hence the sign depends only on \(i\).

**Sharp phases.** If \(h>0\), \(W_n\ge0\) gives positive signs. If \(h=0\), only \(W_0+h=0\), whereas \(W_n>0\) for \(n\ge1\). These cases correspond exactly to \(p<p_0\) and \(p=p_0\). For \(h<0\),
\[
W_n+h=\frac{q+hd}{d}-\frac qd G_n,
\quad q+hd=2bp(a+3b-4bp)=8b^2p(p_*-p).
\]
At \(p<p_*\), this quantity starts negative and approaches a strictly positive limit, crossing once monotonically (possibly through zero). At \(p\ge p_*\), it starts negative and never reaches zero. This proves all phases, for all finite times and all lags.

**Critical crossing and decay.** For \(h<0\), set \(t=T_0/B\) and \(\delta(p)=1-2h/B>0\). Euler's gamma identity gives the exact formula
\[
G_n=\frac{\Gamma(t+1)\Gamma(n+t+2h/B)}
{\Gamma(t+2h/B)\Gamma(n+t+1)}
\sim K(p)n^{-\delta(p)},\qquad
K(p)=\frac{\Gamma(t+1)}{\Gamma(t+2h/B)}.
\]
The gamma-ratio equivalence is locally uniform in \(p\) near \(p_*\), because its arguments remain a fixed positive distance from the gamma poles. The sign crossing occurs at the first \(n\) with
\[
G_n\le\varepsilon_p:=\frac{q+hd}{q}
=\frac{8b^2p(p_*-p)}q.
\]
As \(p\uparrow p_*\), \(q\to q_*=b(b-a)\), \(h\to h_*=(a-b)/2\), \(K(p)\to K_*\), and \(\delta(p)\to\delta_*=2b/B\). Monotonicity of \(G_n\), the uniform gamma estimate, and \((p_*-p)\lvert\log(p_*-p)\rvert\to0\) yield
\[
n_p\sim\left(\frac{K_*q_*}{8b^2p_*}\right)^{1/\delta_*}
(p_*-p)^{-1/\delta_*},
\]
which simplifies to the asserted constant. Exactly at \(p_*\), \(W_n+h_*=h_*G_n\); dividing by \(T_i\sim Bi\) proves the critical adjacent-covariance constant. For other \(h<0\), \(W_{i-1}+h\to(q+hd)/d\), giving
\[
\lim_{i\to\infty}i\operatorname{Cov}(S_i,S_{i+1})
=\frac{8b^2p(p_*-p)}{B(B-2h)}.
\]

## Verification

The self-contained Python checker `checker.py` uses exact rational arithmetic and finite-state distribution propagation, not simulation, to check the population imbalance moments and independently propagated one-step and separated-time draw correlations. It also tests the strict sign thresholds and monotonic signs in finite instances. Run `python3 checker.py` using Python's standard library. The packaged version returned **470 passed exact-rational assertions and finite-distribution checks**. Numerical evaluation of the explicit crossing constant for \(a=1,b=3,T_0=8\) approaches the predicted exponent \(2/3\) as \(p\uparrow5/6\); this is only a supplementary finite diagnostic. The theorem for infinitely many ages follows from the displayed recurrences and gamma-ratio argument, not from bounded enumeration.

## Relationship to prior work

Alves and Rosales, *Friedman vs. Pólya* (first public version 2025-02-24), study almost-sure convergence of color proportions under the same mixed replacement mechanism. Shi, Yin and Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model* (first public version 2026-05-26), study asymptotic fluctuations of proportions and related limit theorems. Both full texts were compared with the exact sampled-color two-time correlation and its two-threshold sign classification; those papers supply important population-dynamics context, but the inspected statements and proofs do not give this sign-phase diagram or the sharp critical crossover age. General reinforced-urn autocorrelation literature provides contextual precedents and may contain implicit reductions; priority beyond the inspected literature is not certified.

## Limitations

The phase diagram is for a constant Friedman selection probability and an initially color-symmetric balanced two-color urn with \(0<a<b\), \(T_0\ge2(a+b)\). It makes no claim about asymmetric initial compositions, unequal total replacement sizes, random environmental mixing probabilities or other urn rules. Correlations are for **sampled colors**, not populations or aggregated occupancy counts. No independent mathematical audit was performed. General textbook moment identities may provide the recurrence, but their availability does not in itself establish the complete derived sign and critical-aging result.

## References

1. R. Alves and R. A. Rosales, *Friedman vs. Pólya*, arXiv:2502.16768 (v1 submitted 24 February 2025), https://arxiv.org/abs/2502.16768 .
2. J. Shi, Q. Yin, and Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669 (v1 submitted 26 May 2026), https://arxiv.org/html/2605.26669v1 .
3. S. Mori, M. Hisakado, and K. Nakayama, *Pólya urn with memory kernel and asymptotic behaviours of autocorrelation function*, arXiv:2105.10653 (2021), https://arxiv.org/abs/2105.10653 .
