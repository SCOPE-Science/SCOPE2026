# Global two-channel endemic uniqueness and asymmetric immune-escape limits in the prevalence-driven SIRCm system

## Finding

**Theorem.** In the prevalence-driven SIRCm model of [1], the endemic equilibrium is unique for every pair of independently varying nonnegative immune-feedback strengths, rather than only in weak or strong diagonal regimes. Its infection prevalence is strictly increasing in the first feedback strength, and in the second strength whenever cross-immunity is incomplete (\(\sigma<1\)). If \(\sigma=1\), the second strength leaves equilibrium prevalence exactly unchanged. The two one-channel strong-feedback limits are different from one another and, when \(\sigma<1\), neither reaches the joint strong-feedback SIS prevalence. Both channels must diverge for the SIS limit, independently of their relative rates.

Specifically, let \(s=(\mu+\alpha)/\beta\) and \(L=1-s\). With one feedback channel strong and the other fixed, the limiting prevalences \(I_1\) and \(I_2\) are the unique positive solutions of
\[
I_1+\frac{(1-\sigma)\alpha I_1}{\mu+\gamma+(\sigma\beta+\gamma\varepsilon_2)I_1}=L,
\qquad
I_2+\frac{\alpha I_2}{\mu+\delta+\delta\varepsilon_1 I_2}=L.
\]
For \(\sigma<1\), both are strictly below \(L\). For \(\sigma=1\), \(I_1=L\) but its limit still has a positive cross-immune class. If both strengths tend to infinity along *any* path, \(I^*\to L\) and the remaining immune compartments vanish at rates described below.

## Assumptions and scope

The normalized model has four fractions \((S,I,R,C)\) summing to one. Its differential equations, precisely the prevalence-driven specialization \(g(S,I)=I\) of [1, Eq. (1)], are
\[
\begin{aligned}
\dot S&=\mu(1-S)-\beta SI+\gamma(1+\varepsilon_2 I)C,\\
\dot I&=\beta SI+\sigma\beta CI-(\mu+\alpha)I,\\
\dot R&=(1-\sigma)\beta CI+\alpha I-\mu R-\delta(1+\varepsilon_1I)R,\\
\dot C&=\delta(1+\varepsilon_1I)R-\beta CI-\mu C-\gamma(1+\varepsilon_2I)C.
\end{aligned}
\]
Throughout, \(\mu,\beta,\alpha,\delta,\gamma>0\), \(0\le\sigma\le1\), \(\varepsilon_1,\varepsilon_2\ge0\), and \(\beta>\mu+\alpha\). An endemic equilibrium is a stationary state with \(I>0\) and all four fractions nonnegative, summing to one. No claim is made about global dynamics, local asymptotic stability, or the distinct transmission-driven model.

## Proof

**Step 1 — exact scalar elimination.** At an endemic equilibrium, the infected equation yields \(S+\sigma C=s\), so mass conservation gives \(I+R+(1-\sigma)C=L\). Introduce the positive quantities
\[
\begin{split}
a(I)&=\delta(1+\varepsilon_1I),\qquad b(I)=\gamma(1+\varepsilon_2I),\\
d(I)&=\beta I+\mu+b(I),\qquad e(I)=\sigma\beta I+\mu+b(I),\\
D(I)&=\mu d(I)+a(I)e(I),\qquad N(I)=d(I)+(1-\sigma)a(I).
\end{split}
\]
The stationary recovered and cross-immune equations are an invertible positive linear system at every \(I\ge0\). Its unique solution is
\[
R(I)=\frac{\alpha I d(I)}{D(I)},\qquad C(I)=\frac{\alpha I a(I)}{D(I)}.
\]
Therefore equilibrium prevalence is exactly a root of
\[
F(I):=I+\alpha\frac{IN(I)}{D(I)}=L.
\tag{1}
\]

**Step 2 — strict global monotonicity.** Write \(a(I)=a_0+a_1I\), \(b(I)=b_0+b_1I\), with \(a_0=\delta>0\), \(a_1=\delta\varepsilon_1\ge0\), \(b_0=\gamma>0\), and \(b_1=\gamma\varepsilon_2\ge0\). Then \(N=n_0+n_1I\) and \(D=d_0+d_1I+d_2I^2\), where
\[
\begin{aligned}
n_0&=\mu+b_0+(1-\sigma)a_0, & n_1&=\beta+b_1+(1-\sigma)a_1,\\
d_0&=(\mu+a_0)(\mu+b_0),&d_1&=\mu(\beta+b_1)+a_0(\sigma\beta+b_1)+a_1(\mu+b_0),\\
d_2&=a_1(\sigma\beta+b_1).
\end{aligned}
\]
Direct differentiation gives
\[
\frac{d}{dI}\left(\frac{IN}{D}\right)=
\frac{n_0d_0+2n_1d_0I+QI^2}{D(I)^2},\quad
Q=n_1d_1-n_0d_2,
\]
and a cancellation expands \(Q\) into a sum of manifestly nonnegative terms:
\[
\begin{aligned}
Q={}&\mu(\beta+b_1)^2+a_0(\beta+b_1)(\sigma\beta+b_1)\\
&+(1-\sigma)a_1[\beta(\mu+b_0)+\mu(\beta+b_1)+a_1(\mu+b_0)]>0.
\end{aligned}
\]
Thus \(F'(I)>1\) for \(I\ge0\). Since \(F(0)=0\), \(L>0\), and \(F(L)>L\), there is one and only one solution \(I^*\in(0,L)\) to (1). Reconstruct \(R^*,C^*>0\) by the formulas above and set \(S^*=s-\sigma C^*\). The mass and infected equations, together with the already satisfied recovered and cross-immune equations, imply \(\dot S=0\). But if \(S^*\le0\), its differential equation would give \(\dot S=\mu(1-S^*)-\beta S^*I^*+b(I^*)C^*>0\), a contradiction. Therefore \(S^*>0\); the reconstructed state lies in the interior of the simplex and is the unique endemic equilibrium.

**Step 3 — monotonic response to each independent channel.** For fixed \(I>0\), regard \(a,b\) as independent variables. Differentiation of the ratio in (1) yields
\[
\frac{\partial (N/D)}{\partial a}
=-\frac{d\,[b+\sigma(\beta I+\mu)]}{D^2}<0,
\qquad
\frac{\partial (N/D)}{\partial b}
=-\frac{(1-\sigma)a(\beta I+\mu+a)}{D^2}\le0.
\]
Because \(a=\delta(1+\varepsilon_1I)\) and \(b=\gamma(1+\varepsilon_2I)\), the left-hand side of (1) decreases strictly with \(\varepsilon_1\) and, for \(\sigma<1\), strictly with \(\varepsilon_2\), holding \(I>0\) fixed. Since it increases strictly with \(I\), the unique solution \(I^*\) increases strictly in those feedback parameters. At \(\sigma=1\), the exact cancellation \(N/D=1/(\mu+a)\) makes the endemic prevalence independent of \(\varepsilon_2\).

**Step 4 — sharp asymmetric limits.** Adding the stationary recovered and cross-immune equations shows
\[
\alpha I=\mu R+[\mu+b(I)+\sigma\beta I]C.
\tag{2}
\]
Since \(I+R+(1-\sigma)C=L\), equation (2) gives the feedback-uniform lower bound
\[
\frac{\mu L}{\mu+\alpha}\le I^*<L.
\tag{3}
\]
At fixed \(\varepsilon_2\), letting \(\varepsilon_1\to\infty\) makes \(a(I^*)\to\infty\) uniformly by (3), while \(d,e\) remain bounded and strictly positive. The formulas in Step 1 imply \(R^*\to0\) and \(C^*\to\alpha I_1/[\mu+\gamma+(\sigma\beta+\gamma\varepsilon_2)I_1]\). The scalar equation (1) converges to the displayed equation for \(I_1\). Its left-hand side is strictly increasing in \(I\) because its derivative is \(1+(1-\sigma)\alpha(\mu+\gamma)/[\mu+\gamma+(\sigma\beta+\gamma\varepsilon_2)I]^2>0\). It has exactly one positive root, below \(L\) when \(\sigma<1\) and equal to \(L\) when \(\sigma=1\).

At fixed \(\varepsilon_1\), letting \(\varepsilon_2\to\infty\) instead makes \(b(I^*)\to\infty\), hence \(C^*\to0\), \(R^*\to\alpha I_2/[\mu+\delta+\delta\varepsilon_1I_2]\). The limiting scalar equation is the displayed equation for \(I_2\); its left-hand derivative equals \(1+\alpha(\mu+\delta)/[\mu+\delta+\delta\varepsilon_1I]^2>0\), and its unique positive root is strictly below \(L\) for every \(\sigma\).

If both parameters diverge, (3) gives \(a(I^*)\ge\delta\varepsilon_1\mu L/(\mu+\alpha)\) and \(b(I^*)\ge\gamma\varepsilon_2\mu L/(\mu+\alpha)\). The recovered equilibrium equation yields \(R^*\le[\alpha+(1-\sigma)\beta]/[\mu+a(I^*)]=O(\varepsilon_1^{-1})\), while (2) yields \(C^*\le\alpha/[\mu+b(I^*)]=O(\varepsilon_2^{-1})\). Consequently, without assuming a finite feedback ratio,
\[
0\le L-I^*=R^*+(1-\sigma)C^*=O(\varepsilon_1^{-1}+\varepsilon_2^{-1})\to0.
\]
This concludes the theorem.

## Verification

The standalone `verify.py` script tests the exact polynomial coefficient identity, the derivative and parameter-sign identities, a baseline rational specialization, both one-axis limiting roots, and the four reconstructed equilibrium equations at an independently chosen asymmetric finite parameter pair. Running `python verify.py` with Python 3 and SymPy prints `VERIFY_OK`. Those checks support but do not substitute for the all-parameter analytic proof above.

For example, set \(\mu=\alpha=\delta=\gamma=1\), \(\beta=4\), \(\sigma=1/2\). The no-feedback prevalence is \((3\sqrt{41}-7)/40\). When only \(\varepsilon_1\to\infty\) at fixed \(\varepsilon_2=0\), prevalence tends \((\sqrt{41}-3)/8\); when only \(\varepsilon_2\to\infty\) at fixed \(\varepsilon_1=0\), it tends \(1/3\). When both tend to infinity, it tends \(1/2\). These are genuinely different limiting infection fractions, all verified by exact substitutions.

## Relationship to prior work

Ramírez-Gutiérrez and coauthors [1] establish endemic equilibrium existence for general feedback, then analyze uniqueness and stability in weak and strong *single-parameter/diagonal* feedback regimes. Their Appendix 8 reconstructs the compartments and displays two-dimensional prevalence and stability computations, without an all-strength independent-two-parameter uniqueness classification or the distinct one-axis limits proved here. The zero-feedback classical SIRC model [2] is a boundary case, not a theorem for arbitrary prevalence-coupled feedback. The simple diagonal monotonicity calculation is also a specialization of the present theorem and is not presented as independently new. The contribution here is the exact global two-parameter uniqueness and comparative statics, including the singularly different coordinate-axis limits.

## Limitations

This is a statement only about stationary endemic equilibria for \(g(S,I)=I\), with the strict supercritical condition \(\mathcal R_0>1\). It does not prove local or global stability; indeed the motivating paper exhibits unstable regimes away from the equal-feedback diagonal. It neither establishes analogous uniqueness for \(g(S,I)=SI\) nor describes oscillatory solutions. The antecedent literature includes inaccessible full texts, and unindexed overlap cannot be ruled out by database searches; independent scientific audit has not been performed.

## References

[1] D. R. Ramírez-Gutiérrez, L. Lóczi, C. Muñoz-Moncayo, D. I. Ketcheson, *Compartmental epidemiological models with infection-driven immune escape*, arXiv:2610.01111v1 (first public release 2026-10-01). https://arxiv.org/html/2610.01111v1 . Relevant locations: Eq. (1), Eq. (3), Theorem 3.1, Proposition 4.2, Proposition 4.8, Appendix 8.

[2] R. Casagrandi, L. Bolzoni, S. A. Levin, V. Andreasen, *The SIRC model and influenza A*, Mathematical Biosciences 200 (2006), 152–169, DOI: 10.1016/j.mbs.2005.12.029. https://pubmed.ncbi.nlm.nih.gov/16504214/ . Only public abstract and bibliographic material were inspected for this comparison.
