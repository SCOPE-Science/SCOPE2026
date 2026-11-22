# Finite-horizon optimal coordinate sampling on weakly coupled star quadratics

## Finding
Fix integers \(m\ge2\) and \(T\ge1\). For \(0<\delta<1\), let
\[
A_\delta=\begin{pmatrix}1&-\sqrt{\delta/m}\,{\bf1}^{\mathsf T}\\-\sqrt{\delta/m}\,{\bf1}&I_m\end{pmatrix}\succ0.
\]
Start the exact randomized single-coordinate descent method on \(f(x)=\tfrac12 x^{\mathsf T}A_\delta x\). Independently at each iteration choose coordinate \(i\in\{0,1,\ldots,m\}\) with a **fixed**, otherwise arbitrary probability vector \(p\) in the simplex, and replace \(x_i\) by the exact coordinate minimizer. The sharp \(T\)-update worst-start expected energy retention is
\[
R_T(p,\delta)=\sup_{x\ne0}\frac{\mathbb E_p[x_T^{\mathsf T}A_\delta x_T\mid x_0=x]}{x^{\mathsf T}A_\delta x}.
\]
Write \(u=(m+1)^{-1}\), \(r=m/(m+1)\), and \(s=(m-1)/(m+1)\). **Every** global minimizing probability vector \(p^{(T)}(\delta)\) satisfies, as \(\delta\downarrow0\) with \(m,T\) fixed,
\[
\boxed{\begin{aligned}
p^{(T)}_0(\delta)&=u+k_{m,T}\sqrt\delta+o(\sqrt\delta),\\
p^{(T)}_i(\delta)&=u-\frac{k_{m,T}}m\sqrt\delta+o(\sqrt\delta),\quad 1\le i\le m,\\
k_{m,T}&=\frac{(m-1)m^{3/2}}{(m+1)^2}\,\frac{1-(1-1/m)^T}{T}.
\end{aligned}}
\]
No symmetry restriction on the competing sampling vectors is assumed. In addition,
\[
\boxed{\min_p R_T(p,\delta)=r^T+\frac{2\sqrt m}{m+1}(r^T-s^T)\sqrt\delta+o(\sqrt\delta).}
\]
The leading hub-bias coefficient obeys the strict horizon law
\[
\boxed{\frac{k_{m,T}}{k_{m,1}}=\frac1T\sum_{j=0}^{T-1}(1-1/m)^j<1\quad (T\ge2),}
\]
and decreases strictly with \(T\). In particular the fixed iid law minimizing the sharp **one-step** contraction fails to minimize the sharp \(T\)-step retention for every fixed \(T\ge2\) and all sufficiently small positive \(\delta\).

## Assumptions and scope
All arithmetic and coordinate updates are exact. The objective is a strictly convex real quadratic (the Schur complement of \(A_\delta\) is \(1-\delta>0\)); the starting vector is adversarial and fixed before random draws. Probabilities do not depend on time, past draws, or the current iterate. The optimizer is over the **full closed simplex** of all \(m+1\) probabilities, not only leaf-exchangeable laws. The asymptotic notation is at fixed finite \(m,T\), with no asserted uniformity as either grows.

## Proof
**1. Projection representation.** Let \(v_i=A_\delta^{1/2}e_i\), so that \(\|v_i\|=1\), the leaf vectors \(v_1,\ldots,v_m\) are orthonormal, and \(\langle v_0,v_i\rangle=-\sqrt{\delta/m}\). In energy coordinates \(y=A_\delta^{1/2}x\), updating coordinate \(i\) is the orthogonal projection \(Q_i=I-v_iv_i^{\mathsf T}\). Set
\[
\Phi_{p,\delta}(X)=\sum_{i=0}^m p_i Q_iXQ_i,\qquad F_T(p,\delta)=\Phi_{p,\delta}^{T}(I).
\]
Then \(R_T(p,\delta)=\lambda_{\max}(F_T(p,\delta))\) exactly. By an orthogonal change of basis, take leaf vectors to be the usual first \(m\) basis vectors and
\[
v_0=\sqrt{1-\delta}\,e_0-\sqrt{\delta/m}\sum_{i=1}^m e_i.
\]
This realizes all Gram relations and gives a continuous matrix family on the closed probability simplex.

**2. Uniform-limit localization.** At \(\delta=0\), all coordinate projections are orthogonal coordinate deletions. Thus
\[
F_T(p,0)=\operatorname{diag}((1-p_0)^T,\ldots,(1-p_m)^T),\qquad
R_T(p,0)=\max_i(1-p_i)^T.
\]
The unique minimizer is uniform \(p_i=u\), with value \(r^T\). Since \(Q_i(\delta)-Q_i(0)=O(\sqrt\delta)\) uniformly, the same is true of \(F_T\) and \(R_T\) for fixed \(m,T\), uniformly in the probability simplex. For any minimizing vector, comparison with uniform sampling yields
\(R_T(p,0)\le r^T+O(\sqrt\delta)\). Because \(\sum_i(p_i-u)=0\), the inequality \(\max_i(1-p_i)^T-r^T\ge c_{m,T}\|p-u\mathbf1\|_\infty\) holds near uniform for a positive constant \(c_{m,T}\). Hence **every** minimizer has the form \(p_i=u+\sqrt\delta\,z_i\) with bounded \(z\) and \(\sum_i z_i=0\).

**3. The all-horizon first-order operator.** Put \(\epsilon=\sqrt\delta\). For bounded real \(z\) of zero sum, Taylor expansion of the finite matrix recurrence gives
\[
F_T(u\mathbf1+\epsilon z,\epsilon^2)=r^T I+\epsilon M_T(z)+O_{m,T,z}(\epsilon^2),
\]
with a remainder uniform for bounded \(z\). Define \(a_T=T r^{T-1}\) and \(h_T=r^T-s^T>0\). Then
\[
M_T(z)=-a_T\operatorname{diag}(z_0,\ldots,z_m)
+\frac{h_T}{\sqrt m}\sum_{i=1}^m(e_0e_i^{\mathsf T}+e_ie_0^{\mathsf T}).
\]
Here the diagonal derivative follows from \((1-p_i)^T\). To verify the off-diagonal derivative directly, write \(v_0=e_0-\epsilon m^{-1/2}\sum_i e_i+O(\epsilon^2)\). For uniform sampling, the common hub-to-average-leaf off-diagonal coefficient \(h_t\) of \(F_t\), at order \(\epsilon\), starts at \(h_0=0\) and satisfies
\[
h_{t+1}=(1-2u)h_t+u(1-u)^t.
\]
The hub projection creates the second term and other projections preserve the existing off-diagonal coefficient with combined weight \(1-2u\). This recurrence solves to \(h_T=r^T-s^T\), proving the stated formula. Changes in probabilities from uniform contribute to the off-diagonal block only at order \(\epsilon^2\).

**4. Exact minimax of the first-order operator.** On the affine hyperplane \(\sum_i z_i=0\), minimize \(\lambda_{\max}(M_T(z))\). The fixed off-diagonal part is the positive weighted adjacency matrix of a connected star. Its maximal eigenvalue is simple and has a strictly positive normalized eigenvector \(v\). For any nonzero zero-sum perturbation \(w\), the standard simple-eigenvalue second derivative is
\[
\frac{d^2}{dt^2}\lambda_{\max}(M_T(z+tw))
=2a_T^2\sum_{j\ge2}\frac{|v_j^{\mathsf T}\operatorname{diag}(w)v|^2}{\lambda_1-\lambda_j}>0.
\]
Indeed zero curvature would require \(\operatorname{diag}(w)v\) to be parallel to \(v\), forcing all entries of \(w\) equal, hence zero. The objective is strictly convex on the hyperplane and coercive because \(\lambda_{\max}(M_T(z))\ge-a_T\min_i z_i\). It consequently has one minimizer. All leaf permutations preserve the objective, so uniqueness forces \(z_1=\cdots=z_m=-z_0/m\).

Set \(z_0=k\). On the mean-leaf and hub plane, the leading matrix is
\[
\begin{pmatrix}a_Tk/m&h_T\\h_T&-a_Tk\end{pmatrix},
\]
with leaf-contrast eigenvalue \(a_Tk/m\). Because \(h_T>0\), the larger plane eigenvalue is strictly above the contrast eigenvalue. Thus the objective equals
\[
G_T(k)=-\frac{a_T(m-1)}{2m}k+
\sqrt{\left(\frac{a_T(m+1)}{2m}k\right)^2+h_T^2}.
\]
Direct strict-convex minimization gives
\[
k=\frac{(m-1)\sqrt m}{a_T(m+1)}h_T
=\frac{(m-1)m^{3/2}}{(m+1)^2}\frac{1-(1-1/m)^T}{T},
\]
and \(\min G_T=2\sqrt m\,h_T/(m+1)\).

**5. Pass to exact minimizers.** Step 2 bounds every rescaled optimizing vector \(z(\epsilon)\). Any convergent subsequence must minimize \(\lambda_{\max}(M_T(z))\), by the uniform-on-compact expansion in Step 3 and comparison with fixed trial vectors \(u\mathbf1+\epsilon z\). The unique minimizer in Step 4 forces all subsequences to the same limit. This proves both boxed asymptotic statements for **every** exact global minimizer, including any possible finite-\(\delta\) ties.

**6. Horizon separation.** The factor \([1-(1-1/m)^T]/[T/m]\) is the mean of the strictly decreasing positive sequence \(1,(1-1/m),\ldots,(1-1/m)^{T-1}\). It is one at \(T=1\) and strictly decreases thereafter. The exact one-step minimizer, available also from the inverse-positive sampling theorem, is
\[
p_0^{(1)}(\delta)=\frac{1+\sqrt{m\delta}}{m+1+2\sqrt{m\delta}},\qquad
p_i^{(1)}(\delta)=\frac{1+\sqrt{\delta/m}}{m+1+2\sqrt{m\delta}}.
\]
Its hub expansion has coefficient \(k_{m,1}\). Any \(T\)-step minimizer has strictly smaller coefficient when \(T\ge2\), so the one-step law is strictly suboptimal for the \(T\)-step criterion for sufficiently small positive \(\delta\). No claim is made about the exact finite-\(\delta\) optimal distribution for arbitrary coupling.

## Verification
The included standalone program `artifacts/verify_horizon.py` checks the energy-coordinate and original-coordinate recurrences in rational arithmetic for a nonzero coupling, derives the exact two-step operator identity from independently computed matrices, and numerically checks the leading hub coefficient for multiple leaf counts and horizons. The recorded run passed 290 assertions. These finite checks do not prove the asymptotic theorem; Steps 1–6 supply that proof.

## Relationship to prior work
Nesterov (2012), Richtárik–Takáč (2011/2016), and Qu–Richtárik (2014/2016) develop randomized coordinate descent and importance sampling, primarily through per-step or complexity-bound criteria. The open-access 2015 first-online paper by Richtárik and Takáč was examined through its actual algorithm, convergence bound and serial optimal-probability section. A previously indexed inverse-positive SPD result establishes the exact **one-step** fixed-sampling optimizer for every SPD Stieltjes matrix, hence covers the one-step formula here but not the finite-horizon claim. The presently proved object is the sharp *finite-\(T\)* worst-initial-vector expected objective after \(T\) iid draws; composing a sharp single-step bound cannot determine its exact optimum. Finite-horizon sampling can be studied through noncommuting projection-product moments; the explicit all-horizon weak-coupling coefficient and strict horizon effect were not located in the inspected material. Historical-equivalence risk remains, especially under optimal experimental design or spectral perturbation terminology.

## Limitations
The theorem concerns a weak-coupling asymptotic at fixed finite \(T,m\); it does not solve the full-coupling exact finite-horizon optimization or establish a uniform limit as \(T\) grows. It does not address dynamic/adaptive sampling, permutations without replacement, different accuracy metrics, computational work needed to infer probabilities, noise, or finite precision. The finite-horizon effect on the probabilities is order \(\sqrt\delta\), while the practical improvement may be small. The result is a sharp structural asymptotic statement, not a promised wall-clock improvement. No independent audit or exhaustive historical novelty guarantee is claimed.

## References
1. P. Richtárik and M. Takáč, *Iteration Complexity of Randomized Block-Coordinate Descent Methods for Minimizing a Composite Function*, first public arXiv posting 2011-07-14, https://arxiv.org/abs/1107.2848; Mathematical Programming 144 (2014), 1–38.
2. P. Richtárik and M. Takáč, *On optimal probabilities in stochastic coordinate descent methods*, first public arXiv posting 2013-10-13, https://arxiv.org/abs/1310.3438; Optimization Letters 10 (2016), 1233–1243, https://doi.org/10.1007/s11590-015-0916-1.
3. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling II: Expected Separable Overapproximation*, first public arXiv posting 2014-12-27, https://arxiv.org/abs/1412.8063; Optimization Methods and Software 31 (2016), 858–884, https://doi.org/10.1080/10556788.2016.1190361.
4. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, 2026, publicly indexed prior result, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995.
