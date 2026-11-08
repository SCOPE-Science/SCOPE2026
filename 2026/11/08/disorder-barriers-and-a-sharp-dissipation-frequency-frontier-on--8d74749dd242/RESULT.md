# Disorder barriers and a sharp dissipation–frequency frontier on a three-state Markov cycle

## Finding

Consider the continuous-time, three-state stochastic ring with positive edge activities \(g_0,g_1,g_2\) and a common signed circulation parameter \(j\), with \(|j|<m:=\min_i g_i\). Across oriented edge \(i\to i+1\) (indices modulo three), the forward rate is \(g_i+j\) and the backward rate is \(g_i-j\). Write
\[
G=g_0+g_1+g_2,\qquad H=g_0g_1+g_1g_2+g_2g_0,
\qquad \Delta^2=G^2-3H=\tfrac12\sum_{i<k}(g_i-g_k)^2.
\]
The two nonstationary generator eigenvalues are exactly
\[
\lambda_{\pm}=-G\pm\sqrt{\Delta^2-3j^2}.
\]
Consequently, a nonreal (oscillatory) relaxation pair exists exactly for \(3j^2>\Delta^2\). A genuine size-two exceptional point occurs at \(3j^2=\Delta^2>0\). The zero-circulation uniform point \(g_0=g_1=g_2,\ j=0\) instead has a semisimple double eigenvalue. For prescribed activities, some admissible circulation can create an oscillatory pair **if and only if** \(\Delta^2<3m^2\). Thus an inhomogeneous ring can be incapable of oscillating even at arbitrarily large entropy-production rate; for example \((g_0,g_1,g_2)=(1,1,3)\).

Let \(\sigma\) be stationary entropy production per unit time, in natural logarithmic units. For every fixed total symmetric rate \(G>0\) and budget \(s>0\), let \(j_s\in(0,G/3)\) be the **unique** solution of
\[
2j_s\log\frac{G+3j_s}{G-3j_s}=s.
\]
Every ring in this class with total rate \(G\) and \(\sigma\le s\) obeys the **sharp** frequency bound
\[
\boxed{\quad\max_{\lambda\in\operatorname{spec}(Q)}|\operatorname{Im}\lambda|\le\sqrt3\,j_s.\quad}
\]
For positive budget, equality holds **if and only if** \(g_0=g_1=g_2=G/3\) and \(|j|=j_s\). The frontier is therefore achieved by the uniform ring and strictly worsens under edge disorder. The result gives both a disorder feasibility threshold at fixed microscopic rates and a global, exactly attained dissipation–frequency optimum at fixed total symmetric activity.

## Assumptions and scope

The state space is the oriented triangle \(\{0,1,2\}\). The model is an irreducible continuous-time Markov chain with all six transition rates strictly positive. Its row generator \(Q\), acting on row probability vectors on the right, has off-diagonal entries \(Q_{i,i+1}=g_i+j\), \(Q_{i+1,i}=g_i-j\), and rows summing to zero. All parameters are real, \(g_i>0\) and \(-m<j<m\). The stationary distribution is exactly uniform \(\pi_i=1/3\). The frequency refers to the angular frequency of the imaginary part of a generator eigenvalue, not the coherence of a quantum channel or a finite-step Floquet exponent. The entropy-production expression is the usual stationary stochastic-thermodynamic irreversibility rate, and it can be interpreted thermodynamically when local detailed balance is present.

The budget theorem quantifies over **all** triples of positive conductances with the same sum \(G\), and all admissible signed \(j\), with \(\sigma\le s\). A nonoscillatory chain has frequency zero. At \(s=0\), the sharp frequency is zero for all reversible chains, so the positive-budget uniqueness statement does not extend to the zero-budget equality case.

## Proof

**1. Stationarity and spectrum.** Along each oriented edge, stationary clockwise minus anticlockwise probability flux equals \(\pi_i(g_i+j)-\pi_{i+1}(g_i-j)=2j/3\). Since this is independent of \(i\), incoming and outgoing stationary fluxes cancel at each vertex. Strict positivity makes the stationary distribution unique. The generator is
\[
Q=\begin{pmatrix}
-g_0-g_2&g_0+j&g_2-j\\
g_0-j&-g_0-g_1&g_1+j\\
g_2+j&g_1-j&-g_1-g_2
\end{pmatrix}.
\]
Direct expansion of its characteristic polynomial gives
\[
\det(zI-Q)=z\bigl[z^2+2Gz+3(H+j^2)\bigr].
\]
Solving the quadratic establishes \(\lambda_\pm=-G\pm\sqrt{G^2-3H-3j^2}\), which is the displayed expression. The identity \(G^2-3H=\tfrac12\sum_{i<k}(g_i-g_k)^2\) proves nonnegativity of \(\Delta^2\).

**2. Complete real/complex and exceptional-point classification.** The nonzero eigenvalues are distinct real exactly for \(3j^2<\Delta^2\), a conjugate pair exactly for \(3j^2>\Delta^2\), and a repeated real value \(-G\) at equality. At equality, a semisimple repeated nonstationary eigenvalue would force the restriction of \(Q\) to the sum-zero plane to equal \(-G I\), and therefore \(Q=-G(I-\boldsymbol1\boldsymbol1^\mathsf T/3)\), because the stationary eigenspace is spanned by \(\boldsymbol1\). The latter matrix has equal off-diagonal rates, forcing \(g_0=g_1=g_2\) and \(j=0\). Conversely, this uniform reversible point is symmetric and its double eigenvalue is semisimple. Every other equality point is therefore a nontrivial Jordan block of size two.

A feasible oscillatory \(j\) must satisfy simultaneously \(\Delta/\sqrt3<|j|<m\). Such a real number exists precisely when \(\Delta^2<3m^2\). If \(\Delta>0\) and this strict inequality holds, the two admissible threshold values \(j=\pm\Delta/\sqrt3\) are exceptional points. For \((g_0,g_1,g_2)=(1,1,3)\), \(\Delta^2=4\) and \(3m^2=3\); oscillation is excluded for every positive rate choice within the one-parameter circulating family. As \(|j|\uparrow1\), a backward rate tends to zero and the entropy production below diverges, showing why affinity alone does not overcome the disorder obstruction.

**3. Exact entropy production.** The net stationary current on each edge is \(2j/3\). Summing current times its log forward/backward rate ratio therefore gives
\[
\sigma(g_0,g_1,g_2,j)=\frac{2j}{3}\sum_{i=0}^2\log\frac{g_i+j}{g_i-j}\ge0.
\]
This expression is even in \(j\) and vanishes exactly when \(j=0\). Fix \(j>0\). The function \(f_j(x)=\log((x+j)/(x-j))\), defined for \(x>j\), satisfies
\[
f_j''(x)=\frac{4jx}{(x^2-j^2)^2}>0.
\]
Jensen's inequality at the fixed arithmetic mean \(G/3\) gives
\[
\sigma\ge2j\log\frac{G+3j}{G-3j}=:S_G(j),
\]
with equality if and only if \(g_0=g_1=g_2=G/3\). The same result holds for negative circulation on replacing \(j\) by \(|j|\). This use of Jensen is valid because \(G/3\ge m>|j|\).

**4. Sharp global frequency at fixed activity and entropy budget.** On \(0<j<G/3\), \(S_G(j)\) is continuous and strictly increasing, since the positive logarithm and its derivative are positive; furthermore \(S_G(j)\to0\) as \(j\downarrow0\) and \(S_G(j)\to+\infty\) as \(j\uparrow G/3\). Thus, for each \(s>0\), there is exactly one root \(j_s\) of \(S_G(j_s)=s\). For every admissible chain with \(\sigma\le s\), the preceding inequality gives \(|j|\le j_s\). Independently, the spectral formula yields
\[
\max_{\lambda\in\operatorname{spec}(Q)}|\operatorname{Im}\lambda|
=\sqrt{\max\{0,3j^2-\Delta^2\}}
\le\sqrt3\,|j|\le\sqrt3\,j_s.
\]
For the uniform triple \(g_i=G/3\), the choice \(j=\pm j_s\) is admissible, has \(\Delta=0\) and \(\sigma=s\), and achieves equality. If \(s>0\), equality in the displayed chain implies \(\Delta=0\) and \(|j|=j_s\), proving uniqueness up to circulation orientation.

## Verification

The standalone `checks/verify.py` uses SymPy to verify the characteristic polynomial as an exact identity in four symbolic parameters; checks that the nontrivial exceptional point \((1,1,2,1/\sqrt3)\) has a defective double root, while the uniform unbiased point has a semisimple double root; tests hundreds of rational-rate configurations against the stationary spectrum and entropy inequalities; and confirms bisection solutions of the positive entropy-budget equation. Run `python checks/verify.py` from the extracted result directory. An executed copy gave 2,274 passing assertions. These finite checks are auxiliary: the universal assertions follow from the four analytical proof steps above.

## Relationship to prior work

The three-site, doubly stochastic, *discrete-time* dephased photonic walk of Huang et al. (2026, arXiv:2606.15935, publicly submitted 2026-06-14) and Longhi (2025, DOI 10.1002/qute.202500539) motivate the importance of real-to-complex relaxation transitions and non-Hermitian exceptional points. Neither their Floquet channel nor its eigenvalues are identified with this continuous-time generator; indeed the 2026 paper explicitly distinguishes the physical Lindbladian limit from its stroboscopic mechanism. Thus no equality of physical models is claimed.

Kolchinsky, Ohga and Ito (2024, DOI 10.1103/PhysRevResearch.6.013082) prove general inequalities relating entropy production and imaginary generator eigenvalues, but they do not give the exact fixed-total-symmetric-rate three-state optimum or this strict disorder impossibility criterion. Their bound \(|\operatorname{Im}\lambda|\le\sqrt{\kappa\sigma/4}\) involves the maximum edge mixing rate \(\kappa\), whereas the stated frontier is expressed solely in terms of \(G\) and \(\sigma\), with equality characterized. The broader 2026 cycle-affinity/winding theorem of Kolchinsky, Ohga and Ito (arXiv:2605.15884) gives spectral localization for cycles with specified affinity and maximum escape rate, not the precise fixed-\(G\) and entropy-budget optimization here. Xu and Meng (2026, arXiv:2608.22934) strengthen those bounds using geometric means of forward/backward rates and prove uniform cycles saturate their comparison bound; their Theorem 1 does not itself state or imply the exact disorder criterion in terms of \(\Delta\) and \(m\), nor the inverse-entropy frontier under the present constraints. In particular, their positive geometric-mean frequency upper bound cannot exclude oscillations for \((1,1,3)\), whereas the exact spectrum does. General thermodynamic constraints and equality phenomena are therefore credited as prior art.

## Limitations

The calculation concerns only three states with uniform stationary measure and common circulation; it is not a result for arbitrary larger Markov networks, partial quantum dephasing, or all nonuniform three-state stationary laws. It assumes strictly positive reverse rates. Its zero-rate boundary limits are approached but excluded. Although the spectral and optimization claims have full mathematical proofs, the exact publication priority of this parameter-constrained three-state specialization is not established by finite searching: an unindexed earlier treatment or a stronger theorem could cover it. The reproducibility checker does not constitute independent validation.

## References

1. X. Huang, L. Xiao, B. Huo, X. Wang, S. Longhi and P. Xue, *Experimental Observation of Dynamical Phase Transitions in a Dephased Photonic Quantum Walk* (2026), arXiv:2606.15935, https://arxiv.org/abs/2606.15935 (first publicly submitted 2026-06-14).
2. S. Longhi, *Dynamical Phase Transitions in Open Quantum Walks*, *Advanced Quantum Technologies* (2025), https://doi.org/10.1002/qute.202500539.
3. A. Kolchinsky, N. Ohga and S. Ito, *Thermodynamic bound on spectral perturbations, with applications to oscillations and relaxation dynamics*, *Physical Review Research* **6**, 013082 (2024), https://doi.org/10.1103/PhysRevResearch.6.013082.
4. A. Kolchinsky, N. Ohga and S. Ito, *Cycle affinity and winding localize eigenvalues of Markov generators* (2026), arXiv:2605.15884, https://arxiv.org/abs/2605.15884.
5. R. Xu and C. Meng, *Coarse-grained kinetic scale tightens thermodynamic spectral bounds of Markov cycles* (2026), arXiv:2608.22934, https://arxiv.org/abs/2608.22934.
