# Curvature heterogeneity permits an interior-optimal two-stage stochastic-extragradient coupling

## Finding

In scalar two-component stochastic extragradient with uniform stage marginals, an **interior** within-step sample correlation can uniquely minimize the limiting mean-squared error about the mean operator's root, outperforming same-sample reuse, independent sampling, and complementary (antithetic) sampling simultaneously. The phenomenon occurs even when *each* component is strongly monotone and *every* possible update map is a strict contraction. In contrast, with equal positive component slopes, same-sample reuse is always the unique stationary-risk minimizer if the component roots differ.

Precisely, let \(F_1(x)=x-3\), \(F_2(x)=3(x+1)\), \(\eta=3/10\), and use at every iteration a fresh pair \((I,J)\) having both marginals uniform on \(\{1,2\}\), with \(\Pr(I=J)=u\in[0,1]\). Define
\[
\widehat X_k=X_k-\eta F_{I_k}(X_k),\qquad
X_{k+1}=X_k-\eta F_{J_k}(\widehat X_k).
\]
The mean operator \((F_1+F_2)/2=2x\) has root \(x_\star=0\). Every coupling admits a unique stationary law, and its stationary root mean-squared error (without a square root) is exactly
\[
R(u)=\lim_{k\to\infty}\mathbb E|X_k-x_\star|^2
=\frac{27(1248u^2-3018u+2357)}{(11-6u)(1537-624u)}.
\]
Its unique global minimum over *all fixed uniform-marginal pair couplings, independently resampled over time*, is at
\[
u_\star=\frac{2459}{1758}-\frac{\sqrt{966408430}}{45708}
\approx0.718624521934934,
\quad R(u_\star)\approx3.08796289521227.
\]
By exact comparison,
\[
R(0)=\frac{63639}{16907},\quad R(1/2)=\frac{783}{245},\quad R(1)=\frac{15849}{4565},
\qquad R(u_\star)<\min\{R(0),R(1/2),R(1)\}.
\]
The optimal stationary mean is \(\mathbb E_\pi X=9(2u_\star-1)/(11-6u_\star)\ne0\), whereas independent sampling has zero stationary mean. Thus the interior optimum is a genuine stationary bias--variance tradeoff. The existence of strictly interior minimizers persists under sufficiently small changes of the two curvatures and stepsize.

## Assumptions and scope

For two scalar affine operators \(F_i(x)=a_i(x-c_i)\) with \(a_i>0\), fix \(\eta>0\) and a constant \(u\in[0,1]\). The index-pair law is
\[
\Pr(I=1,J=1)=\Pr(I=2,J=2)=u/2,\quad
\Pr(I=1,J=2)=\Pr(I=2,J=1)=(1-u)/2.
\]
Every IID-in-time coupling with these two uniform stage marginals has exactly this form. All probabilities, means, and risk statements refer to fresh independent copies of this pair on successive iterations. We optimize stationary squared distance to the unique zero of the mean operator, *not* a gap bound, conditional unbiasedness of the second stage, finite-horizon risk, or pathwise convergence to a noise-free point.

For the equal-curvature boundary, assume \(a_1=a_2=a>0\), distinct \(c_1\ne c_2\), and \(t=\eta a\in(0,1)\). No equal-curvature assertion is made for other stepsizes. For the heterogeneous example, all four exact update multipliers are strictly between zero and one, ensuring the necessary stationary laws.

## Proof

**Affine reduction.** Writing \(F_i(x)=a_i x+b_i\) with \(b_i=-a_i c_i\), the two-stage update is exactly
\[
X_{k+1}=A_{I_kJ_k}X_k+B_{I_kJ_k},\quad
A_{ij}=1-\eta a_j+\eta^2a_i a_j,\quad
B_{ij}=\eta^2 a_j b_i-\eta b_j.
\]
With independently refreshed index pairs, put \(\bar A=\mathbb EA\), \(\bar B=\mathbb EB\), \(\overline{A^2}=\mathbb EA^2\), \(\overline{AB}=\mathbb EAB\), and \(\overline{B^2}=\mathbb EB^2\). Independence of the fresh pair from \(X_k\) gives *identities*, not approximations,
\[
m_{k+1}=\bar A m_k+\bar B,\qquad
s_{k+1}=\overline{A^2}s_k+2\overline{AB}m_k+\overline{B^2},
\]
where \(m_k=\mathbb EX_k\), \(s_k=\mathbb EX_k^2\). Whenever all \(|A_{ij}|<1\), the four-map iterated-function system contracts samplewise under a common sequence of pairs. It has a unique invariant law with finite moments, independent of the initial finite-second-moment distribution, and therefore
\[
m_\infty=\frac{\bar B}{1-\bar A},\qquad
s_\infty=\frac{2\overline{AB}m_\infty+\overline{B^2}}{1-\overline{A^2}}.
\]

**Equal-curvature rigidity.** Write \(m=(c_1+c_2)/2\), \(d=(c_1-c_2)/2\ne0\); let the sample signs \(S_I,S_J\in\{-1,1\}\) encode the centers. With \(Y=X-m\), direct substitution yields
\[
Y_{k+1}=(1-t+t^2)Y_k+td(S_J-tS_I),\qquad \mathbb ES_IS_J=2u-1.
\]
Since \(0<1-t+t^2<1\), the stationary mean of \(Y\) vanishes. The exact stationary risk about the mean-operator root \(m\) is
\[
R_{\rm equal}(u)=\frac{t^2d^2(1+t^2-2t(2u-1))}{1-(1-t+t^2)^2}.
\]
Its derivative with respect to \(u\) is \(-4t^3d^2/[1-(1-t+t^2)^2]<0\); hence \(u=1\) uniquely minimizes risk. The unequal-root assumption matters: if \(d=0\), every coupling has zero stationary risk.

**Heterogeneous exact example.** For the specified two operators and stepsize the complete multiplier and offset tables (rows indexed by \(I\), columns by \(J\)) are
\[
(A_{ij})=\frac1{100}\begin{pmatrix}79&37\\97&91\end{pmatrix},\qquad
(B_{ij})=\frac1{100}\begin{pmatrix}63&-171\\117&-9\end{pmatrix}.
\]
Thus \(0<A_{ij}\le97/100\). Averaging against the coupling law gives
\[
\bar A=\frac{67+18u}{100},\quad \bar B=\frac{27(2u-1)}{100},\quad
\overline{A^2}=\frac{5389+1872u}{10000},\quad
\overline{AB}=\frac{27(93-16u)}{10000},\quad
\overline{B^2}=\frac{81(53-48u)}{2000}.
\]
The moment identities then give \(m_\infty=9(2u-1)/(11-6u)\) and the stated rational expression for \(R=s_\infty\). Exact differentiation yields
\[
R'(u)=-\frac{2592(91416u^2-255736u+136569)}{(11-6u)^2(1537-624u)^2}.
\]
The numerator polynomial \(p(u)=91416u^2-255736u+136569\) is strictly decreasing on \([0,1]\), because \(p'(u)=182832u-255736<0\). Also \(p(0)=136569>0\) and \(p(1)=-27751<0\). It follows that \(R'\) changes exactly once from negative to positive, and its unique zero is \(u_\star\) above. The exact stationary comparisons and radical expression for its risk follow by substitution. In particular the strict inequalities exclude all three customary couplings.

**Robustness.** More generally, perturb the two positive slopes, both component roots and stepsize independently: \((a_1,a_2,c_1,c_2,\eta)\) may vary near \((1,3,3,-1,3/10)\). The mean-operator root \(x_\star=(a_1c_1+a_2c_2)/(a_1+a_2)\) varies smoothly. All four affine multipliers remain strictly contractive in a sufficiently small neighborhood. After centering the moment recurrences at this changing root, the stationary root risk is a smooth rational function of \((u,a_1,a_2,c_1,c_2,\eta)\), with denominators uniformly nonzero for \(u\in[0,1]\). At the displayed example the endpoint derivatives have strict signs \(R'(0)<0<R'(1)\), and hence they retain these signs throughout a small open neighborhood. A risk minimizer exists by continuity and compactness, and neither endpoint can be one; thus at least one strictly interior optimal coupling persists. No claim of uniqueness after perturbation is needed.

## Verification

A standalone symbolic checker is included as `verify.py`. Run `python verify.py` with SymPy installed. It checks exact rational affine maps, all five moments, the stationary-risk identity, derivative sign polynomial, radical optimizer, endpoint values and comparisons, and the equal-curvature derivative. The proof also supplies the uniform affine-contraction argument needed to lift the moment recurrences to actual unique invariant distributions; computer algebra alone is not used as an infinite-state convergence certificate.

## Relationship to prior work

Yoon and Loizou (2026), *On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities* (arXiv:2608.06182, §1.1 and §§3–4), distinguish fully shared from independent stage sampling and prove convergence, gap and impossibility results. They do not in the inspected article establish the optimality of a **strictly interior** fixed-marginal two-stage coupling for stationary squared error on non-interpolating scalar affine components. The new statement compares *all* within-step uniform-marginal couplings, whose interior parameter is distinct from either of their two standard variants.

Emmanouilidis, Vidal and Loizou (2024), *Stochastic Extragradient with Random Reshuffling* (arXiv:2403.07148, Algorithms 1–3), study temporal sample order while reusing a component at both stages of each iteration. That sampling constraint does not imply an optimum over the present within-iteration coupling parameter. Published mathematical findings about stage coupling on homogeneous bilinear games treat multiplicative linear dynamics with a shared root; there is no nonzero affine forcing or stationary bias--variance tradeoff in their recorded claims. These differences are substantive, not merely a change of parameter names.

## Limitations

The claim is a two-component scalar classification at equal slopes plus a specific, open family of heterogeneous examples; it does not assert a global classification for all heterogeneous components, all stepsizes, nonlinear operators, dimensions above one, time-correlated or state-adaptive sample coupling. Couplings other than independence may violate conditional second-stage unbiasedness assumptions of generic independent-sampling convergence theorems. The iterates have a stationary noise floor and do not converge to the root almost surely. The algebra proves a new stated property but does not establish historical priority beyond the cited primary literature and available comparable records. Independent mathematical review has not been performed.

## References

1. TaeHo Yoon and Nicolas Loizou, *On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities*, arXiv:2608.06182, original preprint August 6, 2026, https://arxiv.org/abs/2608.06182 .
2. Konstantinos Emmanouilidis, René Vidal and Nicolas Loizou, *Stochastic Extragradient with Random Reshuffling: Improved Convergence for Variational Inequalities*, arXiv:2403.07148, 2024, https://arxiv.org/abs/2403.07148 .
