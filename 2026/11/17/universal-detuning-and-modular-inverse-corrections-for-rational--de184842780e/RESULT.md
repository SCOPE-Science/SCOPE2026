# Universal detuning and modular-inverse corrections for rational sigmoid rotations

## Finding

Fix coprime integers \(1\le k<n\), \(n\ge4\), and consider the real sigmoid interval map
\[
F_{a,b}(x)=x+b-\frac{1}{1+e^{-ax}},\qquad a>0,\quad 0<b<1.
\]
Write \(q_a=e^{-a/(2n)}\), fix \(S>0\), and set \(b_a(\sigma)=k/n+\sigma q_a/n\) for \(|\sigma|\le S\). Define \(J=\{k-n,\dots,k-1\}\). Starting at \(m_0=0\), traverse the cyclic permutation
\[
m_{j+1}=\begin{cases}m_j+k,&m_j<0,\\m_j+k-n,&m_j\ge0,\end{cases}\qquad 0\le j<n.
\]
Then \(m_0,\dots,m_{n-1}\) enumerate \(J\) exactly once and \(m_n=0\). Put \(p_j=(m_j+1/2)/n\). The index \(t_*\in\{1,\dots,n-1\}\) defined by \(m_{t_*}=-1\) is equivalently the unique solution of \(k t_*\equiv-1\pmod n\). Set
\[
z(\sigma)=\operatorname{arsinh}(\sigma/2),\qquad C(\sigma)=\cosh z(\sigma)=\sqrt{1+\sigma^2/4}.
\]

**Detuned rational-cycle theorem (including arithmetic fine structure).** For each fixed \(n,k,S\) and every sufficiently large \(a\), uniformly over \(|\sigma|\le S\), there is exactly one primitive period-\(n\) orbit with points \(x_{a,j}\) in the fixed local windows \(\lvert a(x_{a,j}-p_j)\rvert\le U\), for any prescribed \(U>\operatorname{arsinh}(S/2)+1\). Its itinerary is \(F_{a,b_a(\sigma)}(x_{a,j})=x_{a,j+1}\), cyclically. It is locally attracting, and its coordinates admit the **uniform two-scale expansion**
\[
\boxed{x_{a,j}=p_j+\frac{z(\sigma)}a+q_a B_j(\sigma)
+O_{n,k,S,U}\left(\frac{q_a}{a}+a q_a^2\right),\qquad 0\le j<n,}
\]
where
\[
\boxed{
B_j(\sigma)=
-\frac{1+\dfrac{t_*\sigma}{n}e^{z(\sigma)}}{2C(\sigma)}
+\frac{j\sigma}{n}
+\mathbf 1_{\{j\ge1\}}e^{-z(\sigma)}
-\mathbf 1_{\{j>t_*\}}e^{z(\sigma)}.
}
\]
Here \(\mathbf1\) is the indicator function. In particular the coefficient \(B_j\), not just an unspecified error term, is resolved at the exponentially small spatial scale \(q_a\), and it records the modular inverse of the rotation numerator.

The period-return multiplier \(\Lambda_a(\sigma)=(F_{a,b_a(\sigma)}^n)'(x_{a,j})\) and the fixed-\(a\) parameter sensitivities satisfy
\[
\boxed{1-\Lambda_a(\sigma)=2a q_a C(\sigma)+O_{n,k,S}(a^2q_a^2),}
\]
\[
\boxed{
\frac{a q_a}{n}\frac{\partial x_{a,j}}{\partial b}\bigg|_{b=b_a(\sigma)}
=\frac{1}{2C(\sigma)}+O_{n,k,S}(a q_a),\qquad
(1-\Lambda_a)\frac{\partial x_{a,j}}{\partial b}
=n+O_{n,k,S}(a q_a).
}
\]
Both \(0<\Lambda_a(\sigma)<1\) and the differentiability of the local periodic branch hold for all sufficiently large \(a\).

For example, at denominator \(n=4\), numerator \(k=1\) gives \(t_*=3\), while numerator \(k=3\) gives \(t_*=1\). Their universal leading shift \(z(\sigma)/a\) is identical, but their first cyclically labeled coefficient \(B_0\) differs by \(-\sigma e^{z(\sigma)}/(4C(\sigma))\), nonzero whenever \(\sigma\ne0\).

## Assumptions and scope

Every assertion is for fixed integers \(n\ge4\), coprime \(1\le k<n\), fixed \(S>0\), and \(a\to+\infty\); all remainders are uniform for \(|\sigma|\le S\) and \(j\in\{0,\ldots,n-1\}\). The map parameter \(b_a(\sigma)\) lies in \((0,1)\) eventually. Orbit labels follow the reference rotation starting at \(p_0=1/(2n)\), not spatial ordering. A local window is prescribed in the phase variable \(u=a(x-p)\); its radius \(U\) is fixed and independent of \(a\). For the derivative \(\partial_b x_{a,j}\), \(a\) is held fixed and the smooth periodic branch is varied in \(b\). These claims neither classify all possible nonattracting periodic orbits nor establish global attraction at the moving parameter.

The quadratic-order remainder in the spatial expansion is an absolute error \(O(q_a/a+a q_a^2)\). In particular \((x_{a,j}-p_j-z/a)/q_a\to B_j\) for every fixed \(\sigma\), uniformly on compact detuning intervals.

## Proof

**Step 1: a uniformly differentiable return map.** Fix \(L>\operatorname{arsinh}(S/2)+1\) and write \(h=1/(2n)\), \(q=e^{-ah}\), \(b=k/n+\sigma q/n\), and \(x_0=h+u/a\) for \((u,\sigma)\in[-L,L]\times[-S,S]\). Set \(g_a(x)=(1+e^{-ax})^{-1}\) and compare \(F_{a,b}\) with the piecewise translation
\[
G_b(x)=x+b-\mathbf1_{\{x>0\}},\qquad
e_a(x)=F_{a,b}(x)-G_b(x)
=\begin{cases}1-g_a(x),&x>0,\\-g_a(x),&x<0.\end{cases}
\]
For fixed \(n,k,L,S\), induction along the reference sites \(p_j\) keeps every iterate \(x_j=F_{a,b}^j(x_0)\) at \(p_j+u/a+O_{n,k,L,S}(q)\). Thus all \(x_j\) have the sign of \(p_j\) for large \(a\). Only \(p_0=h\) and \(p_{t_*}=-h\) are at distance \(h\) from the origin; every other site has absolute value at least \(3h\), with tail \(O(q^3)\).

The positive-site correction is, with uniform first derivatives in \(u,\sigma\),
\[
e_a(x_0)=q e^{-u}-q^2e^{-2u}+O_{L}(q^3).
\]
Before the negative-site visit, the only tail of size \(q\) was at time zero. Consequently
\[
x_{t_*}=-h+\frac ua
+q\left(e^{-u}+\frac{t_*\sigma}{n}\right)
+O_{n,k,L,S}(q^2),
\]
also in the \(C^1\) sense (the derivatives of a bounded \(q^2\) correction are at most of order \(a q^2\), which is accommodated in the following error). Expanding the negative logistic tail then gives
\[
e_a(x_{t_*})=
-qe^u-aq^2\left(1+\frac{t_*\sigma}{n}e^u\right)
+q^2e^{2u}
+O_{n,k,L,S}(a^2q^3).
\]
All other \(n-2\) tails contribute \(O_{n,k,L,S}(q^3)\). The branch translations sum to \(nb=k+\sigma q\), and exactly \(k\) reference sites are positive. Hence the normalized \(n\)-step displacement
\[
H_a(u,\sigma)=
\frac{F_{a,b_a(\sigma)}^n(h+u/a)-(h+u/a)}q
\]
obeys the uniform differentiated expansion
\[
\boxed{
H_a(u,\sigma)=
\sigma-2\sinh u
+q\left(2\sinh(2u)-a\left[1+\frac{t_*\sigma}{n}e^u\right]\right)
+O_{n,k,L,S}(a^2q^2),
}
\]
including first derivatives in \(u,\sigma\). In particular
\[
\partial_uH_a=-2\cosh u+O(aq),\qquad
\partial_\sigma H_a=1+O(aq).
\]
All derivatives are ordinary finite compositions of analytic logistic terms on a fixed compact phase rectangle; differentiation of their exponential tails is controlled by \(a q\to0\). Thus the differentiated error bounds are legitimate.

**Step 2: existence, uniqueness, primitive period and leading phase.** The limiting displacement \(\sigma-2\sinh u\) is positive at \(u=-L\) and negative at \(u=L\) for every \(|\sigma|\le S\); its \(u\)-derivative is at most \(-2\). The uniform \(C^1\) expansion implies that, for large \(a\), \(H_a(\cdot,\sigma)\) decreases strictly and has exactly one zero \(u_a(\sigma)\in(-L,L)\). This gives a smooth periodic branch. Its \(n\) sites are separated by at least \(1/n+o(1)\), so the least period is exactly \(n\). The mean-value theorem yields
\[
u_a(\sigma)=z(\sigma)+O_{n,k,S}(a q).
\]

**Step 3: arithmetic fine structure.** Keeping the next return term and expanding about \(z=z(\sigma)\), where \(\sigma=2\sinh z\), gives
\[
u_a=z-\frac{a q}{2C}\left(1+\frac{t_*\sigma}{n}e^z\right)
+\frac{q\sinh(2z)}{C}+O_{n,k,S}(a^2q^2).
\]
Dividing by \(a\) in \(x_{a,0}=h+u_a/a\) proves the displayed \(B_0\), since the second correction above is \(O(q/a)\). The cycle recurrence on the fixed sign itinerary is
\[
x_{a,j+1}=x_{a,j}+\frac{k}{n}-\mathbf1_{\{x_{a,j}>0\}}+\frac{\sigma q}{n}+e_a(x_{a,j}).
\]
Along one traversal the order-\(q\) corrections are exactly \(+q e^{-z}\) at time \(j=0\), \(-q e^z\) at time \(j=t_*\), and zero at all other times, with accumulated error \(O_{n,k,S}(a q^2)\). The resulting coordinate formula is
\[
x_{a,j}=p_j+\frac{z}{a}
+q\left[-\frac{1+(t_*\sigma/n)e^z}{2C}
+\frac{j\sigma}{n}+\mathbf1_{\{j\ge1\}}e^{-z}
-\mathbf1_{\{j>t_*\}}e^{z}\right]
+O_{n,k,S}\left(\frac q a+a q^2\right).
\]
At \(\sigma=0\) it reduces to the previously established fixed-rational half-grid sign profile; the new information is the *detuning-dependent* modular-inverse coefficient for all denominators \(n\ge4\).

**Step 4: multiplier and response.** Differentiating the definition of \(H_a\) yields the exact identity
\[
(F_{a,b}^n)'(x_{a,0})-1=a q\,\partial_uH_a(u_a,\sigma).
\]
It follows that \(\Lambda_a=1-2aq C+O(a^2q^2)\), with \(0<\Lambda_a<1\) for large \(a\). Every constituent derivative \(1-a g_a(x_{a,j})(1-g_a(x_{a,j}))\) also lies strictly between zero and one, confirming local attraction. Implicit differentiation of \(H_a(u_a(\sigma),\sigma)=0\) gives
\[
\frac{du_a}{d\sigma}
=-\frac{\partial_\sigma H_a}{\partial_u H_a}
=\frac{1}{2C}+O(aq).
\]
Because \(db_a/d\sigma=q/n\) and \(x_{a,0}=h+u_a/a\),
\[
\frac{\partial x_{a,0}}{\partial b}=\frac{n}{2a q C}\left(1+O(aq)\right).
\]
For the other points, the differentiated finite recurrence has constituent derivatives \(1+O(aq)\) and direct \(b\)-derivative \(1\), so \(\partial_b x_{a,j}=\partial_b x_{a,0}(1+O(aq))+O_{n,k}(1)\). Multiplication by \(1-\Lambda_a=2aq C+O(a^2q^2)\) yields both claimed response formulas for each \(j\), with uniform errors.

## Verification

The included standalone `verify_eos_general_detuning.py` uses 105-digit `mpmath` arithmetic to solve the *original nonlinear* \(n\)-step periodicity equation, follow each exact itinerary, check the primitive period and local multipliers, and compare the universal phase, multiplier, \(\partial_bF^n\) response and arithmetic next-order position coefficients. It runs 40 parameter cases: \(n=4\) with \(k=1,3\); \(n=5\) with \(k=1,2,3,4\); and \(n=7\) with \(k=2,3\), each at five detunings \(\sigma\in\{-3,-1,0,1,3\}\). Run `python verify_eos_general_detuning.py` with `mpmath` installed. The successful check prints `EOS_ALL_DENOMINATOR_DETUNING_OK cases=40`. These finite tests corroborate but do not constitute proofs of the uniform infinite-parameter statements.

## Relationship to prior work

Bielawski et al. [1] prove existence and almost-everywhere attraction for fixed rational \(b=k/n\) and explain the numerically observed similarity across rotation numerators. Their later study [2] describes steep parameter-response phenomena, primarily numerically, motivating a quantitative two-parameter analysis. The published note [3] already establishes the precise \(q_a\)-order half-grid corrections and multiplier gap for arbitrary fixed rational \(b=k/n\). They are not claimed as new here, including their \(\sigma=0\) specializations. Published results [4,5] already give the inverse-hyperbolic-sine detuning crossover and susceptibility for \(n=3\); thus simply announcing such a function for three-cycles is not new. The distinct statement here is a uniform detuning theorem for **every coprime numerator at fixed denominator \(n\ge4\)**, which resolves the previously unspecified, exponentially small *parameter-dependent* first-order correction \(B_j(\sigma)\) and its explicit modular-inverse dependence. Neither the fixed-parameter result [3] nor the period-three laws [4,5] state or imply this arithmetic correction for \(n\ge4\) without a new calculation.

## Limitations

Uniformity is for fixed \(n,k\) and bounded \(\sigma\), not for denominators increasing with \(a\) or detunings growing with \(a\). Local periodic-orbit uniqueness does not classify remote cycles or imply a uniform global basin-entry time. The result is an asymptotic description, not a finite-\(a\) explicit threshold. The \(\sigma=0\) fixed-rational formulas and the \(n=3\) arcsinh profile are previously published and are specifically excluded as originality claims. Although highly relevant accessible source texts and mathematical finding summaries were compared, equivalence under an unindexed general perturbation theorem cannot be ruled out; independent historical-priority review has not been performed.

## References

[1] J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Interval maps mimicking circle rotations*, arXiv:2411.01495v1, first public 2024-11-03, especially Sections 3–5. https://arxiv.org/html/2411.01495v1

[2] The same authors, *Strange bifurcation diagrams*, arXiv:2605.19756v1 (2026-05-19), hopping discussion. https://arxiv.org/abs/2605.19756

[3] *Singular half-grid selection and exponentially weak attraction in rational EOS maps* (2026), full result. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-singular-half-grid-selection-and-exponentially-weak-attraction-i--b03eb35b1a55/RESULT.md

[4] *An inverse-hyperbolic-sine resonance profile for a hopping period-three EOS attractor* (2026), full result. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-an-inverse-hyperbolic-sine-resonance-profile-for-a-hopping-perio--ea5af59d59ba/RESULT.md

[5] *An inverse-hyperbolic-sine crossover law for hopping three-cycles in a sigmoid interval map* (2026), full result. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-an-inverse-hyperbolic-sine-crossover-law-for-hopping-three-cycle--ba8f0a397403/RESULT.md
