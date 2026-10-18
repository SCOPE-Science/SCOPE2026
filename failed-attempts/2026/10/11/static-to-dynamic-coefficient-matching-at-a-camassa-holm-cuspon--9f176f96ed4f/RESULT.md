# Static-to-dynamic coefficient matching at a Camassa–Holm cuspon birth
## Finding
Consider the conservative Camassa–Holm solution in the generic first-breaking regime studied by Kim and Kwon. Let \(t_*\) and \(x_*\) denote the first breaking time and position, and let \(a_-(t)<a_+(t)\) be the two Lagrangian zeros born immediately after breaking. Their Eulerian images \(x_-(t)<x_+(t)\) are the anticuspon and cuspon locations. Define
\[
W(t)=x_+(t)-x_-(t),\qquad H(t)=u(x_+(t),t)-u(x_-(t),t).
\]
Let \(C_*>0\) be the sharp coefficient of the first-breaking cusp, meaning
\[
|u(x,t_*)-u(x_*,t_*)|=C_*|x-x_*|^{3/5}+o(|x-x_*|^{3/5}).
\]
Then, with \(\delta=t-t_*\downarrow0\),
\[
W(t_*+\delta)=\sqrt{\frac{216}{3125}}\,C_*^{5/2}\,\delta^{5/2}+o(\delta^{5/2}),
\]
\[
H(t_*+\delta)=\frac52\sqrt{\frac{216}{3125}}\,C_*^{5/2}\,\delta^{3/2}+o(\delta^{3/2}).
\]
In particular,
\[
\lim_{\delta\downarrow0}\frac{\delta H(t_*+\delta)}{W(t_*+\delta)}=\frac52.
\]
Thus the static leading coefficient of the \(C^{3/5}\) breaking cusp determines both leading post-breaking geometric opening coefficients of the \(C^{2/3}\) singularity pair.

## Assumptions and scope
The hypotheses are the generic first-breaking assumptions used in arXiv:2610.01109v1: there is a unique breaking label \(a_*\); the breaking-time map \(\tau\) satisfies \(\tau(a_*)=t_*\), \(\tau'(a_*)=0\), and \(\tau''(a_*)>0\); and the regular Lagrangian factor \(R\) is positive and continuous near \((a_*,t_*)\). The source supplies the exact variables \(Q\), \(R\), the identities
\[
\eta_a=\frac{Q^2R}{1+Q^2},\qquad U_a=\frac{QR}{1+Q^2},
\]
and the post-breaking zero curves \(a_-(t)\), \(a_+(t)\). No assertion is made for nongeneric multiple breaking, vanishing quadratic curvature, or higher-order terms beyond the displayed asymptotics.

## Proof
Set
\[
\kappa=-Q_{aa}(a_*,t_*)>0,\qquad R_*=R(a_*,t_*)>0.
\]
The source identities \(Q_a(a,\tau(a))=-\tau'(a)/2\) and \(Q_t(a,\tau(a))=1/2\) imply
\[
\tau(a)=t_*+\kappa(a-a_*)^2+o((a-a_*)^2).
\]
For \(\delta=t-t_*>0\) and \(|a-a_*|=O(\sqrt\delta)\), continuity of \(Q_t\) yields the uniform expansion
\[
Q(a,t_*+\delta)=\frac12\bigl(\delta-\kappa(a-a_*)^2\bigr)+o(\delta).
\]
Consequently
\[
a_\pm(t_*+\delta)=a_*\pm\sqrt{\frac{\delta}{\kappa}}+o(\sqrt\delta).
\]
Since \(R=R_*+o(1)\) and \((1+Q^2)^{-1}=1+o(1)\) on this shrinking interval, put \(a-a_*=\sqrt{\delta/\kappa}\,y\). Then
\[
W(t_*+\delta)=\int_{a_-}^{a_+}\eta_a\,da
=\frac{R_*\delta^{5/2}}{4\sqrt\kappa}\int_{-1}^1(1-y^2)^2\,dy+o(\delta^{5/2}).
\]
Because \(\int_{-1}^1(1-y^2)^2\,dy=16/15\),
\[
W(t_*+\delta)=\frac{4R_*}{15\sqrt\kappa}\delta^{5/2}+o(\delta^{5/2}).
\]
Likewise,
\[
H(t_*+\delta)=\int_{a_-}^{a_+}U_a\,da
=\frac{R_*\delta^{3/2}}{2\sqrt\kappa}\int_{-1}^1(1-y^2)\,dy+o(\delta^{3/2}),
\]
so
\[
H(t_*+\delta)=\frac{2R_*}{3\sqrt\kappa}\delta^{3/2}+o(\delta^{3/2}).
\]
This gives \(\delta H/W\to5/2\).

At \(t=t_*\), the same source formulas give
\[
Q(a,t_*)=-\frac\kappa2(a-a_*)^2+o((a-a_*)^2).
\]
Therefore
\[
|U(a,t_*)-U(a_*,t_*)|=\frac{R_*\kappa}{6}|a-a_*|^3+o(|a-a_*|^3),
\]
while
\[
|\eta(a,t_*)-\eta(a_*,t_*)|=\frac{R_*\kappa^2}{20}|a-a_*|^5+o(|a-a_*|^5).
\]
Hence
\[
C_*^5=\frac{20^3}{6^5}\frac{R_*^2}{\kappa}.
\]
If \(A=4R_*/(15\sqrt\kappa)\), then
\[
\frac{C_*^5}{A^2}=\frac{3125}{216}.
\]
Thus \(A=\sqrt{216/3125}\,C_*^{5/2}\), and the height coefficient is \((5/2)A\).

## Verification
Every limit follows from the source's exact Lagrangian identities plus Taylor expansion at the generic quadratic minimum of \(\tau\). The two polynomial integrals are exact. Exact rational arithmetic gives
\[
\frac{20^3}{6^5}\bigg/\frac{16}{225}=\frac{3125}{216}.
\]
No finite experiment is used to infer an infinite statement. Only the leading asymptotic orders and coefficients are proved.

## Relationship to prior work
Kim and Kwon prove dynamic creation of an anticuspon–cuspon pair after first wave breaking and provide the exact Lagrangian identities and zero-curve asymptotics used here. Their paper states the \(C^{3/5}\) regularity at first breaking and the \(C^{2/3}\) post-breaking singularity type, but it does not state the Eulerian width law, the height-gap law, their universal \(5/2\) ratio, or the elimination of local Lagrangian parameters in favor of \(C_*\).

Li and Zhang's 2017 generic-regularity theorem gives local \(C^{3/5}\) and \(C^{2/3}\)-type normal forms for conservative Camassa–Holm singularities. The full theorem and its proof leave the relevant Taylor coefficients as independent unspecified constants. They therefore do not imply the parameter-free coefficient matching proved here. Kim, Kwon, and Yoon's earlier work establishes the sharp first-breaking \(C^{3/5}\) cusp but does not provide the post-breaking pair needed for this cross-time relation.

## Limitations
The result is local in time near a generic first breaking and concerns the leading pair width and profile-height gap only. It does not determine higher-order corrections, later interaction of the singularities, or degenerate cases. An equivalent identity could exist under different normal-form coordinates; the closest inspected generic normal-form source does not state or force the invariant coefficient relation.

## References
1. Y. Kim and B. Kwon, *Emergence of Cuspons through Wave Breaking*, arXiv:2610.01109v1, first public 2026-10-01.
2. M. Li and Q. Zhang, *Generic Regularity of Conservative Solutions to Camassa–Holm Type Equations*, SIAM Journal on Mathematical Analysis 49 (2017), 2920–2949, DOI 10.1137/16M1063009.
3. Y. Kim, B. Kwon, and J. Yoon, *Sharp regularity of gradient blow-up solutions in the Camassa-Holm equation*, arXiv:2412.00558.
