# Unique eigenratio-optimal conductances on wheel networks

## Finding

**Theorem (globally optimal wheel Laplacian eigenratio).** Fix an integer \(m\ge 3\) and a budget \(B>0\). Let \(W_m=K_1\vee C_m\) have a hub and cyclic rim vertices \(v_0,\ldots,v_{m-1}\). Give every hub--rim edge an independently chosen conductance \(a_j\ge0\) and every rim edge \(v_jv_{j+1}\) an independently chosen conductance \(b_j\ge0\), with indices modulo \(m\) and
\[
\sum_{j=0}^{m-1}(a_j+b_j)=B.
\]
For the weighted combinatorial Laplacian \(L\), require \(\lambda_2(L)>0\) and minimize the scale-invariant spectral eigenratio
\[
\mathcal R(L)=\frac{\lambda_{m+1}(L)}{\lambda_2(L)}.
\]
Define
\[
s_m=4\sin^2\!\left(\frac{\pi}{m}\right),\qquad
S_m=4\sin^2\!\left(\frac{\pi\lfloor m/2\rfloor}{m}\right).
\]
**There is exactly one optimizer even without an assumption of rotational symmetry:** every hub--rim edge has conductance
\[
\boxed{a_j=a_*:=\frac{B S_m}{m(S_m+m)}}
\]
and every rim edge has conductance
\[
\boxed{b_j=b_*:=\frac{B}{S_m+m}}.
\]
Its rim-to-spoke rate ratio and exact globally minimal eigenratio are
\[
\boxed{\frac{b_*}{a_*}=\frac{m}{S_m},\qquad
\mathcal R_* =\frac{m+1}{1+m s_m/S_m}}.
\]
At this optimum the top two competing spectral branches coincide:
\[
\lambda_{m+1}(L_*)=(m+1)a_*=a_*+S_m b_*,\qquad
\lambda_2(L_*)=a_*+s_m b_*.
\]

**Quantitative separation from fastest continuous-time diffusion.** For every \(m\ge7\), the budget-optimal *algebraic-connectivity* design (the different problem of maximizing \(\lambda_2\)) is the unit-budget-scaled star with \(a_j=B/m\), \(b_j=0\), and \(\lambda_2^{\mathrm{gap}}=B/m\). This comparison rule is established prior work, not a new assertion of priority here. By contrast the eigenratio optimizer retains every rim edge and allocates the rim fraction
\[
F_m=\frac{\sum_j b_j}{B}=\frac{m}{m+S_m}
\]
of its entire conductance budget to the rim. Precisely,
\[
\frac{\lambda_2(L_*)}{\lambda_2^{\mathrm{gap}}}
=\frac{S_m+m s_m}{S_m+m}.
\]
Consequently, as \(m\to\infty\),
\[
\frac{b_*}{a_*}=\frac m4+O(m^{-1}),\qquad
F_m=1-\frac4m+O(m^{-2}),\qquad
\frac{\lambda_2(L_*)}{\lambda_2^{\mathrm{gap}}}=\frac4m+O(m^{-2}),
\]
and
\[
\mathcal R_*=m+1-\pi^2+o(1),\qquad
\mathcal R_{\mathrm{gap}}=m+1.
\]
Thus a constant-order improvement in eigenratio is obtained only by sacrificing a factor of order \(m\) in the absolute spectral gap. The precise measure of improvement and slowdown are both part of the theorem; an eigenratio is not itself an absolute mixing-speed guarantee.

## Assumptions and scope

Each edge conductance is nonnegative and can be independently adjusted. Vertex masses are uniform, and the Laplacian is the **combinatorial, unnormalized** weighted Laplacian, not a normalized random-walk Laplacian. Its energy is
\[
 x^\mathsf TLx=
 \sum_{j=0}^{m-1}a_j(x_h-x_j)^2+
 \sum_{j=0}^{m-1}b_j(x_j-x_{j+1})^2.
\]
All eigenvalues are counted with multiplicity and ordered as
\(0=\lambda_1(L)\le\lambda_2(L)\le\cdots\le\lambda_{m+1}(L)\).
A candidate with \(\lambda_2(L)=0\) is disconnected and has no finite feasible eigenratio; such candidates cannot be optimal. Conductance-price coefficients are one in both edge classes; changing prices is outside the claim. The budget \(B>0\) fixes a unique scale although the eigenratio itself is invariant under positive rescaling of all conductances. At \(m=3\) the wheel is a complete graph on four vertices; the same theorem and uniqueness statement apply.

The mathematical object is an exact spectral-condition-number design problem: the objective is the condition number of \(L\) on the orthogonal complement of the constants. It is motivated by linear synchronization with a tunable global stable step, whereas \(\lambda_2\) alone controls the slowest continuous-time decay rate. The result compares these two design criteria, not discrete-time stochastic-chain SLEM with nonnegative holding probabilities.

## Proof

**1. Three universal Rayleigh comparisons.** Set
\[
 \bar a=\frac1m\sum_j a_j,\qquad
 \bar b=\frac1m\sum_j b_j,
 \qquad m(\bar a+\bar b)=B.
\]
Connectedness implies \(\bar a>0\), since otherwise the hub is isolated. Let \(u\) have hub entry \(-m\) and every rim entry \(1\). Then \(u\) is orthogonal to the constants, and direct evaluation gives its Rayleigh quotient \((m+1)\bar a\). The Rayleigh--Ritz and Courant--Fischer principles therefore give **both**
\[
\lambda_2(L)\le(m+1)\bar a\le\lambda_{m+1}(L). \tag{1}
\]
Write \(\theta=2\pi/m\). Let \(c^{(k)},s^{(k)}\) be vectors with hub entry zero and rim entries \(\cos(kj\theta)\), \(\sin(kj\theta)\), respectively. For \(k=1\), both vectors are real, orthogonal to the constants, and have norm squared \(m/2\). Their squared components add to one, and on each rim edge the squared differences add to \(4\sin^2(k\pi/m)\). Averaging their two Rayleigh quotients yields exactly
\[
\bar a+s_m\bar b.
\]
Each quotient is at least \(\lambda_2(L)\), so
\[
\lambda_2(L)\le\bar a+s_m\bar b.\tag{2}
\]
For the **highest** rim frequency \(k=\lfloor m/2\rfloor\), the same average equals \(\bar a+S_m\bar b\), and each quotient is at most \(\lambda_{m+1}(L)\). When \(m\) is even, the sine vector is identically zero and the cosine vector is alternating \(\pm1\); its norm squared is \(m\), and its single Rayleigh quotient is still \(\bar a+S_m\bar b\). Consequently for every parity,
\[
\lambda_{m+1}(L)\ge\bar a+S_m\bar b.\tag{3}
\]
Combining (1)--(3) gives a **global** lower bound valid for every independent edge allocation,
\[
\mathcal R(L)\ge
\frac{\max\{(m+1)\bar a,\bar a+S_m\bar b\}}
{\min\{(m+1)\bar a,\bar a+s_m\bar b\}}.\tag{4}
\]

**2. Exact one-variable minimization.** Because \(\bar a>0\), write \(r=\bar b/\bar a\ge0\). The right-hand side of (4) is
\[
G_m(r)=\frac{\max\{m+1,1+S_mr\}}
{\min\{m+1,1+s_mr\}}.\tag{5}
\]
The thresholds satisfy \(0<m/S_m\le m/s_m\), since \(0<s_m\le S_m\). For \(0\le r\le m/S_m\), the numerator is \(m+1\) and the denominator \(1+s_mr\); this branch is **strictly decreasing**. For \(m/S_m\le r\le m/s_m\), the function is \((1+S_mr)/(1+s_mr)\). If \(S_m>s_m\), this branch is **strictly increasing**, since its derivative is \((S_m-s_m)/(1+s_mr)^2>0\). If \(S_m=s_m\), which occurs only at \(m=3\), this middle interval is a singleton. On \(r\ge m/s_m\), the denominator is the constant \(m+1\) and the numerator \(1+S_mr\), so this branch is strictly increasing. Therefore **for every integer \(m\ge3\)**, the unique minimum of the lower bound is
\[
 r_* =\frac{m}{S_m},\qquad
 G_m(r_*)=\frac{m+1}{1+ms_m/S_m}.\tag{6}
\]
The sum budget fixes the unique mean weights
\[
\bar a=a_*=\frac{B S_m}{m(S_m+m)},\qquad
\bar b=b_*=\frac{B}{S_m+m}.\tag{7}
\]
These means are positive, so connected symmetric candidates exist.

**3. Attainment, without requiring a symmetry assumption.** For the explicit equal-within-class weights in (7), the standard wheel Fourier decomposition gives the **complete** spectrum
\[
\operatorname{spec}(L_*)=
\left\{0,(m+1)a_*,\ a_*+4b_*\sin^2\!\left(\frac{\pi k}{m}\right):1\le k\le m-1\right\}.\tag{8}
\]
Here \(\lambda_2=a_*+s_mb_*\), because \(s_m\le S_m\) and \(s_m\le m+S_m\), and the largest eigenvalue is \((m+1)a_* =a_*+S_mb_*\) by \(S_mb_*=ma_*\). Thus (4) and (6) are equalities and the advertised minimum is **attained**.

**4. Rigidity of every globally optimal allocation.** Suppose arbitrary feasible edge weights attain (6). Then their mean ratio must be \(r_*\) by strict one-variable minimization; moreover, as their ratio meets the lower bound (4), equality holds in (2):
\(\lambda_2(L)=\bar a+s_m\bar b\). Both real first-frequency Fourier vectors \(c^{(1)}\), \(s^{(1)}\) have Rayleigh quotients at least \(\lambda_2(L)\), whose average equals it. Hence **both individually achieve equality** and are eigenvectors at \(\lambda_2(L)\).

Take their complex combination \(z=c^{(1)}+\mathrm i s^{(1)}\), with \(z_h=0\) and \(z_j=e^{\mathrm i j\theta}\). At rim vertex \(j\), the eigenvector relation divided by \(z_j\ne0\) reads
\[
a_j+b_{j-1}(1-e^{-\mathrm i\theta})+b_j(1-e^{\mathrm i\theta})=\lambda_2(L).\tag{9}
\]
Taking imaginary parts yields \((b_{j-1}-b_j)\sin\theta=0\). As \(m\ge3\), \(\sin(2\pi/m)\ne0\); consequently \(b_j\) is constant across all rim edges. Taking real parts of (9) then forces every \(a_j\) to be constant as well. Their exact budget and required mean ratio force the weights in (7). This establishes **global uniqueness** among all feasible nonsymmetric and boundary allocations; a mere group averaging argument would not have sufficed.

**5. Comparison with connectivity design and sharp asymptotics.** If \(m\ge7\), then \(s_m<1\), and (2) gives
\[
\lambda_2(L)\le\bar a+s_m\bar b
=\frac Bm-(1-s_m)\bar b\le\frac Bm.
\]
The star with uniform \(a_j=B/m\) and zero rim weights attains the cap; equality forces all rim weights zero and, by the same first-Fourier eigenvector argument, all spoke weights equal. This independently reproduces only the **known** spectral-gap optimizer for the comparison. Its top eigenvalue is \((m+1)B/m\), hence eigenratio \(m+1\). Formula (8) gives the eigenratio-optimal spectral gap
\(\lambda_2(L_*)=B(S_m+m s_m)/[m(S_m+m)]\), yielding the stated exact ratio.

Finally \(s_m=4\pi^2/m^2+O(m^{-4})\), and \(S_m=4+O(m^{-2})\) (exactly four for even \(m\)). Elementary expansion proves all displayed large-wheel laws. In particular
\[
\frac{m s_m}{S_m}=\frac{\pi^2}{m}+O(m^{-3}),
\qquad
\frac{m+1}{1+m s_m/S_m}=m+1-\pi^2+o(1).
\]
This completes the proof.

## Verification

The standalone script `verify_wheel_eigenratio.py` constructs full symmetric Laplacians from **independent** spoke and rim edge weights, verifies the explicit spectrum and exact optimum for a range of sizes, tests many nonsymmetric and off-optimum allocations, and symbolically compares characteristic polynomials to the Fourier product for four sizes. Its deterministic execution using NumPy and SymPy reports:

```text
VERIFY_OK 3910 spectral, minimax, nonsymmetric, exact polynomial comparisons
```

Run `python verify_wheel_eigenratio.py`. These finite tests corroborate matrix construction, normalization, integer and boundary cases, and reproducibility; they do **not** prove the all-graph, all-budget theorem. The analytical Rayleigh comparisons (1)--(4), strict scalar minimization (5)--(7), Fourier attainment (8), and eigenvector-rigidity calculation (9) constitute the proof for all \(m\) and all real \(B>0\).

For direct rational checks, \(m=6\) has \(s_6=1\), \(S_6=4\), \(b_*/a_*=3/2\), and \(\mathcal R_*=14/5\). At \(m=3\), the wheel is \(K_4\) and the unique optimum assigns all six edges rate \(B/6\), with \(\mathcal R_*=1\). The code also checks direct asymmetric competitors, but no finite set of competitors could establish uniqueness by itself.

## Relationship to prior work

The earlier *Quadratic spoke-price frontier for fastest mixing on wheels* [1] solves **maximization of \(\lambda_2\)** on the same general wheel conductance class, with a linear price budget and unrestricted edge rates, and derives the Fourier spectrum and a first-frequency eigenvector-rigidity argument. **Those tools and the rim-deletion threshold are established prior work.** Our claim is instead the exact minimum of \(\lambda_{m+1}/\lambda_2\), the unique joint saturation of the first and last Fourier bounds, and the asymptotic severe allocation/spectral-gap separation from \(\lambda_2\)-optimization. The former theorem neither states nor implies that global eigenratio optimizer by its optimality assertion, since a wheel can optimize \(\lambda_2\) while having a provably worse eigenratio.

Kempton, Herrmann and di Bernardo [2] treat both Laplacian eigenratio minimization and algebraic-connectivity maximization through distributed weight adjustment, using per-node upper weighted-degree caps. **For the scale-invariant eigenratio, such positive upper caps allow every nonnegative conductance ray after sufficiently small rescaling**, so their general optimization problem covers the admissible *weight shapes* considered here. Their accessible preprint and supplemental material do not, however, state the exact wheel-specific eigenratio, the strict global uniqueness of the edge allocation after budget normalization, or the gap-versus-ratio asymptotic. The novelty here is the closed structural classification and quantitative consequence, **not** the generic eigenratio problem or a claim that differing homogeneous budget caps by themselves create a new feasible geometry. This is the focal pre-2016 literature source, with an earliest verified public preprint date of 2015-05-27, not its later journal date.

Boyd, Diaconis, Parrilo and Xiao [3, Section 5.4.3] calculate a **wheel** Fourier decomposition and an exact, graph-specific **discrete-time fastest-mixing symmetric stochastic chain**. They minimize SLEM under entrywise nonnegative stochasticity, not a scale-free Laplacian eigenratio under a total conductance budget. In particular their wheel solution's relative rim/spoke probability ratio for a six-vertex rim is \(2\), whereas our optimal rim/spoke conductance ratio for the same rim size is \(3/2\); thus the two formulas do not describe the same optimizer. Both exploit the already known Fourier wheel spectrum.

Shafi, Arcak and El Ghaoui [4] study semidefinite Laplacian spectral weight design under eigenvalue constraints, but do not assert this closed all-rim-size eigenratio-optimal allocation. Ghosh, Boyd and Saberi [5] give the wheel Laplacian spectrum and an exact symmetric reduction for **total effective-resistance** minimization, which is a different objective. Göring, Helmberg and Reiss [6] optimize the **spectral width** \(\lambda_{m+1}-\lambda_2\), rather than the ratio. Their accessible 2011 preprint specifies the difference objective explicitly and contains no wheel-specific ratio formula. Thus our novelty assertion is limited to the specific exact ratio classification and separation, not to graph Fourier methods, generic eigenvalue optimization, or synchronization motivation.

## Limitations

The theorem applies to unnormalized **undirected** Laplacians on wheels with equal vertex masses, nonnegative adjustable independent edge conductances, equal unit prices and one strictly positive **total** budget. It does not establish the optimal ratio under per-vertex degree caps, discrete-time stochastic nonnegativity, arbitrary edge prices, nonuniform vertex masses, edge failures or a constraint on the absolute algebraic connectivity. In fact the asymptotic comparison shows why a smaller eigenratio does not automatically mean faster continuous-time convergence. The solution uses established wheel Fourier representation and standard eigenvalue bounds; the new content is the exact optimizer of their **ratio** and its unrestricted uniqueness. Unindexed or inaccessible equivalent literature may exist, and no independent audit is asserted.

## References

[1] *Quadratic spoke-price frontier for fastest mixing on wheels*, publicly accessible result with full proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-quadratic-spoke-price-frontier-for-fastest-mixing-on-wheels--24216ca23b99/RESULT.md. Compared by mathematical objective and implication, not by title alone.

[2] L. Kempton, G. Herrmann and M. di Bernardo, *Self-organization of weighted networks for optimal synchronizability*, arXiv:1505.07279, first posted 2015-05-27, https://arxiv.org/pdf/1505.07279. Later journal publication is not used as the public-source date.

[3] S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optim. 20 (2009), 792–819, esp. §5.4.3, https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.

[4] S. Y. Shafi, M. Arcak and L. El Ghaoui, *Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints*, Allerton Conference (2010), https://people.eecs.berkeley.edu/~elghaoui/Pubs/SAE_Allerton_2010.pdf.

[5] A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Rev. 50 (2008), 37–66, https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.

[6] F. Göring, C. Helmberg and S. Reiss, *On Minimizing the Spectral Width of Graph Laplacians and Associated Graph Realizations*, SIAM J. Optim. 23 (2013), 834–856, https://doi.org/10.1137/110859658; freely accessible 2011 preprint: https://www.tu-chemnitz.de/mathematik/preprint/2011/PREPRINT_04.pdf.
