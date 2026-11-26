# Four vertices first separate spectral and two-step randomized gossip design

## Finding

Let one edge of the unweighted four-vertex path \(P_4\) be selected independently in each of **two** successive rounds, with probabilities \(p_1,p_2,p_3\geq0\), \(p_1+p_2+p_3=1\). When edge \(i\) is selected, its two endpoint values are replaced by their arithmetic mean. For each deterministic nonconstant initial vector \(x\), let \(e_2\) be the disagreement vector after two rounds. Define the exact worst-initial-condition expected squared-disagreement factor
\[
\rho_2(p)=\max_{x\perp\mathbf1,\ \|x\|_2=1}\mathbb E_p\|e_2\|_2^2.
\]
There is a **unique global minimizer over all probability triples**, namely
\[
(p_1,p_2,p_3)=\left(\frac{1-b_*}{2},b_*,\frac{1-b_*}{2}\right),
\qquad b_*=0.39432184835338379\ldots.
\]
The number \(b_*\) is the unique stationary point on \((0,1)\) of
\[
F(b)=\frac{5b^2-7b+10+\sqrt{29b^4-150b^3+281b^2-132b+36}}{16};
\]
equivalently, it is the unique root in \((39/100,2/5)\) of
\[
116b^6-1760b^5+8175b^4-18554b^3+18203b^2-6396b+648=0.
\]
The sharp two-round factor is \(\rho_2^*=F(b_*)=0.77455285319149393\ldots\). By contrast, minimizing the sharp **single-round** expected squared-disagreement factor gives the unique law \((3/10,2/5,3/10)\). It incurs a strictly larger exact two-round factor
\[
F(2/5)=\frac12+\frac{\sqrt{754}}{100}=0.7745906043549196\ldots.
\]
The path \(P_4\) is the smallest path on which these one- and two-round optimal probability laws differ: on paths of two or three vertices, the two objectives have the same unique optimizer.

## Assumptions and scope

All states are real; vertex labels run from 1 to 4 and edge \(i\) joins \(i\) to \(i+1\). The two edge draws use the **same fixed law** \(p\), are independent and allow repetition; this is not a without-replacement schedule, adaptive edge choice, or a deterministic full sweep. Contacts are exact symmetric half-averages; no message noise, state-dependent choice, or additional edge is allowed. Initial disagreement is Euclidean, mean-zero, deterministic, and chosen adversarially before the random draws. Zero probabilities are admitted, but cannot be optimal. The theorem concerns the exact horizon \(2\); it does not assert an optimal policy for other horizons.

## Proof

Write \(h_i=e_i-e_{i+1}\) and \(W_i=I-h_ih_i^{\mathsf T}/2\), an orthogonal projection preserving the all-ones vector. Conditional on an initial mean-zero \(x\), two independent draws give
\[
\mathbb E\|W_jW_ix\|^2=x^{\mathsf T}M_2(p)x,
\qquad M_2(p)=\sum_{i,j=1}^3p_ip_jW_iW_jW_i.
\]
Thus \(\rho_2(p)\) is the largest eigenvalue of \(M_2(p)\) **restricted to** \(\mathbf1^\perp\) (the eigenvalue 1 of the full matrix on constants must not be included).

**First, symmetry is forced globally.** Parameterize every triple as
\(p=((1-b)/2+d,b,(1-b)/2-d)\), with \(0\le b\le1\) and \(|d|\le(1-b)/2\). Let \(R\) reverse the four vertices, and let \(M_s(b)=M_2((1-b)/2,b,(1-b)/2)\). Direct multiplication gives the exact identity
\[
\frac{M_2(p)+RM_2(p)R}{2}=M_s(b)+d^2C,
\quad C=\frac12(h_1h_1^{\mathsf T}+h_3h_3^{\mathsf T})\succeq0.
\]
Since \(RM_2(p)R\) has the same restricted spectrum as \(M_2(p)\), convexity of the largest eigenvalue yields \(\rho_2(p)\ge\lambda_{\max}(M_s(b)|_{\mathbf1^\perp}+d^2C|_{\mathbf1^\perp})\ge\rho_2((1-b)/2,b,(1-b)/2)\).

The orthonormal basis \(u=(1,0,0,-1)/\sqrt2\), \(v=(0,1,-1,0)/\sqrt2\), \(s=(1,-1,-1,1)/2\) of \(\mathbf1^\perp\) separates the reflection-odd 2-dimensional sector from the even sector. The restrictions of \(M_s(b)\) are exactly
\[
A(b)=\frac1{16}\begin{pmatrix}
3b^2+3b+10&5b^2-11b+6\\
5b^2-11b+6&7b^2-17b+10
\end{pmatrix},\qquad
S(b)=\frac{3b^2+3b+2}{8}.
\]
For \(0\le b<1\), \(A_{11}(b)-S(b)=3(1-b)(b+2)/16>0\), so the largest eigenvalue is always the larger eigenvalue of \(A(b)\), which is the displayed \(F(b)\). Its off-diagonal entry \((1-b)(6-5b)/16\) is positive and \(A_{11}-A_{22}=b(5-b)/4>0\) for \(0<b<1\). Consequently its unique unit top eigenvector \((\alpha,\beta)\) can be chosen with \(\alpha>\beta>0\). For the corresponding spatial vector \(z=\alpha u+\beta v\), \(z^{\mathsf T}Cz=(\alpha-\beta)^2/2>0\). Hence for \(0<b<1\), every \(d\ne0\) has \(\rho_2(p)>F(b)\). If \(b=0\) the graph of admissible contacts is disconnected and \(\rho_2=1\); if \(b=1\), then \(d=0\) and \(F(1)=1\). Since \(F(2/5)<1\), neither boundary can minimize. Global uniqueness therefore reduces to the scalar problem.

**Second, the scalar minimizer is unique.** The function \(F\) is smooth on \((0,1)\), with \(F'(0)=-9/8\) and \(F'(1)=9/16\). Hence an interior stationary point exists. For any such point \(b_0\), choose the positive unit top eigenvector \(z_0=(\alpha,\beta)\) of \(A(b_0)\). The Rayleigh polynomial \(q(b)=z_0^{\mathsf T}A(b)z_0\) is a strictly convex quadratic because its second derivative is
\[
q''(b)=\frac{3\alpha^2+10\alpha\beta+7\beta^2}{8}>0.
\]
The simple-eigenvalue derivative formula gives \(q'(b_0)=F'(b_0)=0\). For any \(b\ne b_0\), \(F(b)\ge q(b)>q(b_0)=F(b_0)\). Thus **every interior stationary point is the unique global minimizer**, so there is exactly one. Write \(Q(b)=29b^4-150b^3+281b^2-132b+36\) for the radicand and \(P(b)\) for the displayed sextic. On \([39/100,2/5]\), \(7-10b>0\) and \(Q'(b)=116b^3-450b^2+562b-132>0\), the latter by bounding the quadratic term at \(2/5\) and the linear term at \(39/100\) and dropping the positive cubic term. Therefore the sign of \(F'(b)\) there is the sign of \(Q'(b)^2-4(7-10b)^2Q(b)=16P(b)\), with no extraneous roots from squaring. The latter expression takes values \(-1178977249431/15625000000\) and \(1589184/15625\) at the respective endpoints, giving the isolating interval and unique root as claimed. At \(2/5\), \(F'(2/5)=-3/16+441\sqrt{754}/60320>0\), proving the strict mismatch; direct substitution gives the exact benchmark value.

**Third, the one-round and minimality assertions hold.** On the reflection-symmetric four-path, the odd-sector top eigenvalue of \(M_1(p)=\sum_i p_iW_i\) is
\[
G(b)=\frac{3-b+\sqrt{5b^2-2b+1}}4,
\]
and it dominates the even-sector eigenvalue \((1+b)/2\) for \(b<1\). Differentiation gives its unique minimum \(G(2/5)=9/10\). Reflection averaging never raises the largest eigenvalue; at an asymmetric law with \(0<b<1\), its odd top vector has unequal positive coefficients and \(W_1-W_3\) couples that vector nontrivially into the even sector. Therefore the asymmetric law strictly increases the top eigenvalue, and \((3/10,2/5,3/10)\) is globally unique. On \(P_3\), writing the two probabilities \((1/2+d,1/2-d)\), reflection averaging of the two-round error operator gives its equal-probability operator plus \(d^2C_3\), where \(C_3\) has eigenvalues \(0,3/8,9/8\); the two strictly positive eigenvalues act on mean-zero inputs. Hence equal sampling is the unique two-round optimum. Its one-round factor is \((1+\sqrt{1-3p_1p_2})/2\), also uniquely minimized by equal sampling. On \(P_2\) there is only one contact. This proves minimality.

## Verification

Run `python verify.py` with Python, SymPy, NumPy and SciPy available. It reconstructs projection matrices from the path, exactly checks the reflection average identity, the invariant blocks, the radical and sextic, the one-step benchmark, and the three-vertex positive-definite minimality certificate. It also replays 300 deterministic-seed supplementary random law comparisons using an independent numerical matrix-product evaluation. The exact symbolic identities and the analytic Rayleigh-polynomial argument establish the theorem; random tests are not substitutes for the proof. Verified outputs include \(b_*=0.394321848353384\) and \(F(b_*)=0.774552853191494\).

## Relationship to prior work

Boyd, Ghosh, Prabhakar and Shah (2004, 2006) establish the random pairwise averaging model and optimize the **one-round spectral/averaging-time bound** through semidefinite programming, rather than the exact fixed-two-round worst-input expected squared error. Their full papers supply the model and one-step comparison, but neither inspected paper states the exact four-path two-step minimizer or the minimal four-vertex separation proved here. Mangoubi, Mou, Liu and Morse (2013) compare **contact averaging weights**, notably for deterministic periodic gossip; the variable optimized here is instead the **edge-selection law** for two independent fixed half-averaging updates. The general second-moment recursion alone does not imply the displayed optimum, uniqueness, or minimality without the reflection positivity and scalar certificate.

## Limitations

The numerical improvement over applying the unique one-round-optimal law for two draws is approximately \(3.7751\times10^{-5}\) in the squared-disagreement factor, so the immediate performance gain in this small network is modest. The mathematical point is the first exact failure of the common one-round surrogate on paths at horizon two, not a claimed large-scale speedup. This does not optimize a random stopping time, a high-probability mixing bound, a nonidentically distributed two-round policy, or the long-run mean-square exponent. The literature comparison is not an exhaustive priority determination.

## References

1. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Analysis and Optimization of Randomized Gossip Algorithms*, 43rd IEEE Conference on Decision and Control, December 14–17, 2004. DOI: 10.1109/CDC.2004.1429652. Accessible text: https://web.stanford.edu/~balaji/papers/04analysisand.pdf
2. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Randomized Gossip Algorithms*, IEEE Transactions on Information Theory 52 (2006), 2508–2530. DOI: 10.1109/TIT.2006.874516. Accessible text: https://web.stanford.edu/~boyd/papers/pdf/gossip.pdf
3. O. Mangoubi, S. Mou, J. Liu, A. S. Morse, *Towards Optimal Convex Combination Rules for Gossiping*, American Control Conference (2013), 1261–1265. DOI: 10.1109/ACC.2013.6580009. Author-uploaded text: https://www.researchgate.net/publication/261162372_Towards_optimal_convex_combination_rules_for_gossiping
