# Universal logarithmic correction at a multi-resident invasion threshold of a quadratic population map

## Finding

Fix an integer \(r\ge2\) and a common coefficient \(a>0\). Consider the homogeneous quadratic population map on the strictly positive cone of \(\mathbb R^{r+1}\)
\[
H_i(x)=\theta_i x_i\left(\sum_{j=1}^{r+1}x_j-\frac{x_i}{2}\right),\qquad
\theta_i=a\ (1\le i\le r),\qquad
\theta_{r+1}=a\left(1-\frac1{2r}\right).
\]
For an arbitrary strictly positive starting state, let \(x^{(n)}=H^{\circ n}(x^{(0)})\), let \(p_i^{(n)}=x_i^{(n)}/\sum_jx_j^{(n)}\), and put \(z_n=p_{r+1}^{(n)}\). **There is a finite real constant \(C\), dependent on the starting composition, for which**
\[
\boxed{\frac1{z_n}=\frac{2r+1}{2(2r-1)}\,n-\frac12\log n+C+o(1)\qquad(n\to\infty).}
\]
The \(r\) resident types satisfy
\[
\frac{p_i^{(n)}}{1-z_n}=\frac1r+O(\rho^n),\qquad 1\le i\le r,
\]
for some \(0<\rho<1\) depending on the initial resident composition. In particular,
\[
\lim_{n\to\infty}n z_n=\frac{2(2r-1)}{2r+1}.
\]
The \(-\frac12\log n\) coefficient is **independent of the number of resident types**, even though the leading inverse-time coefficient depends on \(r\). The threshold is a neutral-invasion boundary: the rare type has multiplier exactly one in the normalized dynamics at the balanced resident state.

## Assumptions and scope

The iteration counter \(n\) is a nonnegative integer; asymptotic statements use \(n\to\infty\) through positive integers and natural logarithms. There are at least two resident types. Every initial population coordinate is strictly positive, and the initial total population may be arbitrary. The common scale \(a>0\) cancels in the composition dynamics, so the theorem holds for every such \(a\) without an initial-mass restriction. The constant \(C\) is not asserted uniform in initial conditions, and the geometric factor \(\rho\) may approach one for extremely imbalanced resident starts. A zero initial rare coordinate is excluded, because it remains identically zero.

## Proof

**1. Exact normalized equations.** Put \(h=1-1/(2r)\). Homogeneity and cancellation of the common coefficient give the closed simplex recurrence
\[
p'_i=\frac{p_i(1-p_i/2)}{g}\quad (i\le r),\qquad
z'=\frac{h z(1-z/2)}{g},\qquad
g=\sum_{i=1}^r p_i(1-p_i/2)+hz(1-z/2).
\]
All coordinates stay positive. Let \(S=1-z\), \(u_i=p_i/S\) for \(i\le r\), and \(q=\sum_{i=1}^r u_i^2\). Then \(\sum_i u_i=1\) and
\[
u_i'=\frac{u_i(1-Su_i/2)}{1-Sq/2}.
\]
Define the resident variance \(E=q-1/r=\sum_{i=1}^r(u_i-1/r)^2\), and set
\[
a_0=\frac{2r+1}{4r},\qquad c_r=\frac{a_0}{h}=\frac{2r+1}{2(2r-1)}.
\]
Direct expansion of the normalizer gives the **exact** identities
\[
g=h+\frac{z}{2r}-a_0z^2-\frac{(1-z)^2E}{2},
\qquad
z'-z=\frac{-a_0z^2(1-z)+\frac12z(1-z)^2E}{g}.
\]

**2. Uniform separation from the rare vertex.** Since \(q\le1\), the aggregate resident contribution obeys
\[
S(1-Sq/2)\ge \frac{1-z^2}{2}.
\]
It follows that
\[
z'\le Q(z):=\frac{hz(1-z/2)}{(1-z^2)/2+hz(1-z/2)}.
\]
The ratio \(z(2-z)/(1-z^2)\) is strictly increasing for \(0<z<1\), so \(Q\) is increasing, and \(Q(1/2)=h/(1+h)<1/2\). Hence \(0<z\le1/2\) implies \(z'<1/2\). For \(z\ge1/2\), the resident per-unit-mass factor satisfies \(1-Sq/2\ge(1+z)/2\ge h(1-z/2)\), so \(z'\le z\). Consequently
\[
0<z_n\le M:=\max\{z_0,1/2\}<1,
\]
for every \(n\). In particular \(S_n\ge s:=1-M>0\), and \(g_n\ge s/2\).

**3. Exponential equalization of residents.** Write \(m_n=\min_{i\le r}u_i^{(n)}\), \(M_n=\max_{i\le r}u_i^{(n)}\), and \(\Delta_n=M_n-m_n\). The scalar function \(v\mapsto v(1-Sv/2)\) is strictly increasing on \([0,1]\), preserving order. As \(m_n\le q_n\le M_n\), its normalized update gives \(m_{n+1}\ge m_n\) and \(M_{n+1}\le M_n\). Moreover,
\[
\frac{\Delta_{n+1}}{\Delta_n}
=\frac{1-S_n(M_n+m_n)/2}{1-S_nq_n/2}
=1-\frac{S_n(M_n+m_n-q_n)}{2(1-S_nq_n/2)}
\le1-\frac{s m_0}{2}=:\rho<1
\]
when \(\Delta_n>0\); the equal case stays equal. Thus \(\Delta_n\le\Delta_0\rho^n\), all resident shares approach \(1/r\) exponentially, and \(0\le E_n\le r\Delta_0^2\rho^{2n}\). This estimate requires no assumption about the behavior of \(z_n\).

**4. Rare-type extinction and a polynomial lower bound.** The drift identity implies
\[
z_{n+1}-z_n\le-Kz_n^2+C_1E_n
\]
for constants \(K,C_1>0\) fixed by \(r\), \(z_0\), and the initial resident profile, because \(1-z_n\ge s\) and \(g_n\le1\); for the positive term use \(g_n\ge s/2\). The sum of positive increments of \(z_n\) is finite since \(\sum_nE_n<\infty\). A bounded real sequence with summable positive increments converges: subtract the accumulated positive variation to obtain a nonincreasing sequence. If its limit were positive, the displayed drift would eventually be bounded strictly below zero, a contradiction. Therefore \(z_n\to0\).

Also, from the same exact drift and \(g_n\ge s/2\),
\[
z_{n+1}\ge z_n-C_2z_n^2
\]
for some \(C_2>0\). For all sufficiently large \(n\), \(C_2z_n\le1/2\), hence \(1/z_{n+1}-1/z_n\le2C_2\). This proves \(1/z_n=O(n)\), an essential bound ensuring the exponentially decaying resident asymmetry cannot affect the logarithmic asymptotic coefficient.

**5. Exact inverse recurrence and the logarithmic second term.** Put \(w_n=1/z_n\). Without dropping any error terms, the exact drift yields
\[
w_{n+1}-w_n
=c_r\frac{1-z_n}{1-z_n/2}-\varepsilon_n,
\qquad
\varepsilon_n=\frac{(1-z_n)^2E_n}{2h z_n(1-z_n/2)}\ge0.
\]
Because \(E_n=O(\rho^{2n})\) and \(1/z_n=O(n)\), the series \(\sum_n\varepsilon_n\) converges absolutely. Since \(z_n\to0\), the inverse increments tend to \(c_r\), whence \(w_n/n\to c_r\) by the Cesàro mean theorem. Thus \(z_n=O(1/n)\), and expansion of the exact fraction gives
\[
w_{n+1}-w_n=c_r-\frac{c_r}{2}z_n+O(z_n^2)-\varepsilon_n
=c_r+O(1/n).
\]
It follows that \(w_n=c_r n+O(\log n)\), so
\[
z_n=\frac1{c_r n}+O\left(\frac{\log n}{n^2}\right).
\]
In particular \(\sum_n|z_n-1/(c_r n)|<\infty\) and \(\sum_nz_n^2<\infty\). Subtract \(c_r\) from the exact inverse increment and sum: the only divergent correction is
\[
-\frac{c_r}{2}\sum_{j=1}^{n-1}z_j
=-\frac12\log n+\text{a convergent remainder}.
\]
The remaining errors \(O(z_j^2)\), \(\varepsilon_j\), and the harmonic-minus-log difference have convergent sums. Hence the sequence \(w_n-c_r n+\frac12\log n\) converges to a finite real number \(C\), establishing the claim. The parabolic rare-direction multiplier at \((1/r,\ldots,1/r,0)\) equals \(h/(1-1/(2r))=1\), explaining the critical normalization.

## Verification

The standalone dependency-free `CHECK.py` independently checks the exact projective and inverse-drift identities in rational arithmetic for multiple positive compositions, then tests the predicted logarithmic correction numerically for resident multiplicities two, three, and five. It also checks the monotone resident spread bound and the neutral invasion multiplier. Execute `python3 CHECK.py` from a directory containing the file. These finite checks corroborate, but do not establish, the all-initial-data and infinite-iteration assertions; their proof is the analytic argument above.

## Relationship to prior work

Shoyimardonov and Rozikov introduced this exact homogeneous quadratic operator and investigated its fixed points and invariant regions. Their 2024 preprint and 2025 journal article discuss two-dimensional nonhyperbolic boundary cases but do not state this multi-resident original-iteration asymptotic or its logarithmic coefficient. Previously available all-dimensional projective convergence and radial-separatrix results establish the limit direction, not its critical rate or second term. A separately published critical-algebraic exclusion theorem treats the **different multiplicity orientation** of one superior resident and several subordinate types, determining the leading \(1/n\) coefficients but not the present multiple-resident \(-\frac12\log n\) correction. These statements are not deduced by exchanging the numbers of superior and subordinate types: the weight ratios and the dimension of the attracting resident face change.

Classical one-dimensional parabolic iteration theory motivates a reciprocal-linear clock plus a logarithmic correction, but its existence alone does not determine the coefficient of this coupled, initially asymmetric, higher-dimensional system. The exact inverse recurrence and summable resident-equalization perturbation supply that coefficient. Literature searches and comparisons are not a proof of publication priority.

## Limitations

The result addresses normalized population proportions, not the absolute population magnitude, which depends on the initial mass through the quadratic homogeneity. Its logarithmic coefficient is proved for exactly one critical rare coordinate and \(r\ge2\) equally weighted resident coordinates. Unequal resident rates, several simultaneous rare ties, explicit general formulas for the initial-condition-dependent finite constant \(C\), and uniform rates as initial coordinates approach zero are not claimed. Equivalent treatments in broader nonlinear replicator or parabolic-dynamics literature might exist despite the inspected sources; independent scholarly verification remains outstanding.

## References

1. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, arXiv:2409.13450v1, first posted 2024-09-20, https://arxiv.org/abs/2409.13450.
2. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, *Russian Journal of Nonlinear Dynamics* **21** (2025), 399–418, DOI:10.20537/nd250803, https://nd.ics.org.ru/nd250803/.
3. *An exact global separatrix and water-filling convergence for a positive quadratic map* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-global-separatrix-and-water-filling-convergence-for-a-p--9175d180eec2.
4. *Universal critical algebraic exclusion in a many-type quadratic population map* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-critical-algebraic-exclusion-in-a-many-type-quadratic--de72cc31a16e.
5. *A computable global extinction–escape separatrix for a homogeneous quadratic population map* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-computable-global-extinction-escape-separatrix-for-a-homogeneo--00331e65c7d9.
