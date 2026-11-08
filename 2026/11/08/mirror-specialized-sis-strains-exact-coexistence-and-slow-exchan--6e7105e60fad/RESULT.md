# Mirror-specialized SIS strains: exact coexistence and slow exchange under strong migration

## Finding

Consider the mass-action, two-strain SIS patch system of Doumatè–Issa–Salako [1] on two patches with symmetric unit edge weights. All three epidemiological classes migrate at the same rate \(d>0\), total host mass is \(N=2\), both strains recover at rate one, and the strain-specific transmission vectors are mirror images:
\[
\beta_1=(b,a),\qquad\beta_2=(a,b),\qquad 0<a<b.
\]
Define the disease-free growth eigenvalue
\[
\Lambda(d)=\frac{a+b}{2}-1-d+\sqrt{d^2+\frac{(b-a)^2}{4}}.
\]
There is a strictly positive coexistence equilibrium **if and only if** \(\Lambda(d)>0\). Whenever it exists, it is the **unique strictly positive coexistence equilibrium** on the conserved mass-two simplex, and is locally exponentially attracting relative to that simplex. It has the form
\[
S=(s,s),\quad I_1=(p,q),\quad I_2=(q,p),\quad 0<q<p,\quad s+p+q=1,
\]
where \(s\) is the **smaller root** in \((0,1)\) of
\[
ab s^2-(a+b)(1+d)s+1+2d=0,
\]
and
\[
\frac{p}{q}=\frac{d}{1+d-bs},\qquad p+q=1-s.
\]
For \(a+b>2\), coexistence persists for every finite \(d>0\), but the slowest linear relaxation rate \(\lambda_{\rm slow}(d)<0\) approaches zero as migration grows:
\[
\lim_{d\to\infty}d\lambda_{\rm slow}(d)=-\frac{(b-a)^2(a+b-2)}{4(a+b)^2},\qquad
\lim_{d\to\infty}d(p-q)=\frac{(b-a)(a+b-2)}{2(a+b)^2}.
\]
Thus the endemic spatial segregation shrinks like \(d^{-1}\), while the relaxation time of strain composition grows linearly in \(d\). In the complementary case \(a+b<2\) and \(b>1\), the sharp viability cutoff is
\[
0<d<d_c,\qquad d_c=\frac{(b-1)(1-a)}{2-a-b};
\]
coexistence exists exactly below this cutoff, not at or above it. When \(b\le1\), coexistence is absent for all \(d>0\). When \(a+b=2\) and \(a<b\), coexistence exists for every finite \(d>0\).

## Assumptions and scope

All compartments are nonnegative, all flow rates are constant, mass-action transmission is used, there is no coinfection or strain mutation, and the two patches exchange population symmetrically. For \(j=1,2\) and \(\ell=1,2\), let \(k=3-j\). The equations are
\[
\begin{aligned}
\dot S_j&=d(S_k-S_j)-S_j\big(\beta_{1j}I_{1j}+\beta_{2j}I_{2j}\big)+I_{1j}+I_{2j},\\
\dot I_{\ell j}&=d(I_{\ell k}-I_{\ell j})+(\beta_{\ell j}S_j-1)I_{\ell j}.
\end{aligned}
\]
The total population \(\sum_j(S_j+I_{1j}+I_{2j})=2\) is conserved. Strictly positive coexistence means all six coordinates are positive. Local attraction and eigenvalues always refer to the five-dimensional fixed-total-mass state space; there is a trivial zero eigenvalue if the conservation law is not restricted. Neither global attraction nor a stochastic individual-based epidemic is asserted.

## Proof

**Step 1: total patch mass.** Write \(T_j=S_j+I_{1j}+I_{2j}\). Reaction terms cancel, so \(\dot T_1=d(T_2-T_1)\), \(\dot T_2=d(T_1-T_2)\). Every equilibrium on the mass-two simplex therefore has \(T_1=T_2=1\); the difference perturbation has eigenvalue \(-2d\).

**Step 2: necessary uniform susceptible density.** At a positive equilibrium let \(s_1=S_1\), \(s_2=S_2\). The two infected vectors are positive nullvectors of the Metzler matrices
\[
M_1=\begin{pmatrix}bs_1-1-d&d\\d&as_2-1-d\end{pmatrix},\qquad
M_2=\begin{pmatrix}as_1-1-d&d\\d&bs_2-1-d\end{pmatrix}.
\]
Their determinants both vanish. Subtraction gives \((1+d)(b-a)(s_1-s_2)=0\); hence \(s_1=s_2=s\). Both infected vectors must be positive Perron nullvectors. Their common principal eigenvalue is
\[
L(s)=\frac{a+b}{2}s-1-d+\sqrt{d^2+\frac{(b-a)^2s^2}{4}}.
\]
It is strictly increasing for \(s\ge0\) because \(a,b>0\), with \(L(0)=-1\). Therefore a root with \(0<s<1\) exists exactly when \(L(1)=\Lambda(d)>0\). The determinant equation is the quadratic in the finding; its smaller root is the unique zero of the *principal* eigenvalue \(L(s)\). The other algebraic root, when admissible as a number, corresponds to a non-Perron eigenmode and cannot support a positive infected vector. This proves necessity of the viability condition and identifies \(s\) uniquely.

**Step 3: existence and uniqueness.** Fix this root and let \((P,Q)\gg0\) be the positive nullvector of \(M_1(s,s)\), with \(P>Q\) since \(b>a\). The corresponding nullvector of \(M_2(s,s)\) is \((Q,P)\). Write the actual infected equilibrium as \(I_1=c(P,Q)\), \(I_2=e(Q,P)\), \(c,e>0\). The two patch-mass identities require \(cP+eQ=cQ+eP=1-s\), forcing \(c=e\). This determines all four infected coordinates uniquely and gives the displayed \(p,q\). Conversely, the constructed state satisfies all six differential equations, hence is the unique positive coexistence equilibrium.

**Step 4: local attraction.** On the invariant equal-patch-mass manifold set \((x,y,u,v)=(I_{11},I_{12},I_{21},I_{22})\). At \((p,q,q,p)\), reflection of patch and strain splits the four-dimensional Jacobian into the matrices
\[
A_{\pm}=\begin{pmatrix}bs-1-d-bp&d\mp bp\\d\mp aq&as-1-d-aq\end{pmatrix}.
\]
The subscript \(+\) denotes reflection-even perturbations, the subscript \(-\) reflection-odd perturbations. The matrix \(M=\begin{psmallmatrix}bs-1-d&d\\d&as-1-d\end{psmallmatrix}\) has eigenvalues zero and a strictly negative number, so both blocks have negative trace \(\operatorname{tr}M-bp-aq<0\). From \(d(p-q)=(bs-1)p=-(as-1)q\), direct determinant expansion gives
\[
\det A_- =d(p-q)\left(\frac{bp}{q}-\frac{aq}{p}\right)>0,\qquad
\det A_+=\det A_-+2d(bp+aq)>0.
\]
Each real two-by-two block is Hurwitz. The remaining fixed-mass eigenvalue is \(-2d\), proving local exponential attraction on the whole conserved-mass simplex, not only on the equal-mass invariant manifold.

**Step 5: cutoff and strong-migration asymptotics.** If \(a+b\ge2\), then \(\Lambda(d)>0\) for finite \(d>0\), because \(\sqrt{d^2+(b-a)^2/4}>d\). If \(a+b<2\), positive growth requires \(b>1>a\); squaring the positive inequality \(\sqrt{d^2+(b-a)^2/4}>d+(2-a-b)/2\) yields the claimed sharp \(d_c\). If \(b\le1\), the infected linearization at the disease-free state is strictly stable for every \(d>0\).

Suppose \(a+b>2\). Dividing the quadratic equation for \(s\) by \(d\) gives \(s\to2/(a+b)\). Perron eigenvector ratios imply \(p/q\to1\), hence \(p,q\to(a+b-2)/(2(a+b))\). The exact identity \(d(p-q)=(bs-1)p\) yields the spatial-segregation limit in the finding. The odd-block determinant consequently tends to \((b-a)^2(a+b-2)/(2(a+b)^2)\), while its trace is \(-2d+O(1)\). The odd block therefore has one eigenvalue \(-2d+O(1)\) and one \(-[(b-a)^2(a+b-2)/(4(a+b)^2)]d^{-1}+o(d^{-1})\). The even block has determinant \(d(a+b-2)+O(1)\) and trace \(-2d+O(1)\), so its slow eigenvalue tends to \(-(a+b-2)/2<0\). Together with the patch-mass mode \(-2d\), this identifies the asserted slowest eigenvalue and establishes its exact leading coefficient.

## Verification

The standalone standard-library script `verify.py` checks the original six-compartment flow, fixed-total-mass balance, a rational exact equilibrium, the two symmetry blocks and their determinant identities, a sharp extinction cutoff, and strong-migration numerical limits. For example, \(a=1/2\), \(b=3\), \(d=3/2\) gives exactly \(s=1/2\), \(p=3/10\), \(q=1/5\). The reflection-odd determinant is \(5/8\), while the even determinant is \(29/8\). These finite checks independently support the algebra but do not replace the all-parameter proof above.

## Relationship to prior work

Doumatè, Issa, and Salako [1, Sections 2.2–2.3.6] establish general invasion-number criteria and existence of coexistence at sufficiently small uniform migration, show numerical coexistence at larger migration, and explicitly leave uniqueness and stability of coexistence as a further question. The present result answers *local* stability and uniqueness in an exactly defined mirrored two-patch family and computes its finite-migration viability frontier and strong-migration exchange eigenvalue. It does not answer the source's general global-stability question. Earlier diffusion SIS work [2,3] establishes coexistence criteria for related models, but does not provide the stated mirror-family closed form or the linear \(d\)-scale composition relaxation. The two-species competition-patch classification [4] concerns a separately normalized Lotka–Volterra family with globally constant competition coefficients and does not directly imply the patch-specific SIS identity or its exchange-gap constant. A later mass-action two-strain diffusion analysis [5] requires a spatially constant ratio of strain transmission rates for its full equal-diffusion dynamics theorem; the present strict mirror rates have ratios \(b/a\) and \(a/b\) on the two patches, so do not meet that hypothesis. A subsequent paper of overlapping authors [6] proves coexistence uniqueness in a *different* continuous-space system with varying total population. That paper and the earlier reaction–diffusion study [7] require full-text comparison before any definitive publication-priority claim; their abstracts/metadata do not establish this specific two-patch formula or relaxation coefficient.

## Limitations

The uniqueness theorem applies only to positive **equilibria**, not to arbitrary trajectories. The exponential attraction proved here is local on the conserved-mass manifold, not global. The two patches have equal edge rates and mirrored transmission; unequal dispersal, unequal recovery, coinfection, or higher patch counts are not covered. The \(d^{-1}\) eigenvalue law assumes \(a+b>2\); the critical average \(a+b=2\) has a different asymptotic regime not analyzed here. Earlier or unindexed equivalent results cannot be excluded by search alone. Complete text of several nearby continuous-space analyses [5–7] was unavailable; exact claim-level exclusion against their full theorem sets remains a residual risk.

## References

[1] J. T. Doumatè, T. B. Issa, R. B. Salako, *Competition-exclusion and coexistence in a two-strain SIS epidemic model in patchy environments*, arXiv:2308.10348, first public version 2023-08-20, https://arxiv.org/abs/2308.10348 ; *Discrete and Continuous Dynamical Systems B* 29 (2024), 3058–3096, https://doi.org/10.3934/dcdsb.2023213 .

[2] N. Tuncer, M. Martcheva, *Analytical and numerical approaches to coexistence of strains in a two-strain SIS model with diffusion*, *Journal of Biological Dynamics* 6 (2012), 406–439, https://doi.org/10.1080/17513758.2011.614697 .

[3] Y. Wu, N. Tuncer, M. Martcheva, *Coexistence and competitive exclusion in an SIS model with standard incidence and diffusion*, *Discrete and Continuous Dynamical Systems B* 22 (2017), 1167–1187, https://doi.org/10.3934/dcdsb.2017057 .

[4] S. Chen, J. Shi, Z. Shuai, Y. Wu, *Global dynamics of a Lotka-Volterra competition patch model*, arXiv:2101.02265, https://arxiv.org/abs/2101.02265 .

[5] J. Adetola, K. G. Castellano, R. B. Salako, *Dynamics of classical solutions of a multi-strain diffusive epidemic model with mass-action transmission mechanism*, *Journal of Mathematical Biology* 90 (2025), article 1, first online 2024-11-29, https://doi.org/10.1007/s00285-024-02167-9 .

[6] J. Kotounou, T. J. Doumatè, L. Leadi, R. B. Salako, *Global dynamics of a spatially heterogeneous diffusive two-strain epidemic model with varying total population*, *Journal of Mathematical Biology* 93 (2026), article 18, https://doi.org/10.1007/s00285-026-02435-w .

[7] Y. Lou, R. B. Salako, *Mathematical analysis on the coexistence of strains in some reaction-diffusion systems*, *Journal of Differential Equations* 370 (2023), 424–469, https://doi.org/10.1016/j.jde.2023.06.018 .
