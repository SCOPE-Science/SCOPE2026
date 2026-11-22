# Universal critical extinction at successive microbial nutrient-exchange thresholds

## Finding

In the fully locally separated, one-abiotic-resource consumer–resource model of ElGamel and Mugler [1], all strictly positive trajectories converge to a uniquely selected equilibrium, even when species are lost and the equilibrium is nonhyperbolic. Increasing the rate of nutrient exchange from a global supply pool to isolated niches removes consumer species **one at a time**, at explicit, strictly ordered exchange rates. At every such boundary, the marginal species becomes extinct at a universal inverse-time rate, with an explicit amplitude independent of its initial abundance.

**Theorem.** Fix an integer \(S\geq2\), positive parameters \(\gamma,R_0,\beta,\alpha_i,k_i\), and pairwise distinct break-even local nutrient levels
\[
0<c_1<\cdots<c_S<R_0,\qquad c_i=k_i/\alpha_i.
\]
Consider the deterministic dimensionless-time equations
\[
\begin{aligned}
\dot N_i&=(\alpha_iT_i-k_i)N_i,\\
\dot T_i&=\beta(R-T_i)-\gamma\alpha_iT_iN_i,\qquad i=1,\ldots,S,\\
\dot R&=R_0-R-\beta\sum_{i=1}^S(R-T_i),
\end{aligned}
\tag{1}
\]
with \(R(0)>0\), \(T_i(0)>0\), and \(N_i(0)>0\) for every \(i\). There is a unique \(r\in(0,R_0)\) solving
\[
r+\beta\sum_{i=1}^S(r-c_i)_+=R_0,\qquad(z)_+=\max(z,0),
\tag{2}
\]
and every such trajectory converges to the equilibrium
\[
R^*=r,\qquad T_i^*=\min\{c_i,r\},\qquad N_i^*=\frac{\beta(r-c_i)_+}{\gamma k_i}.
\tag{3}
\]
Precisely those species with \(c_i<r\) survive at positive limiting abundance. For each \(j=2,\ldots,S\), the unique exchange rate at which species \(j\) becomes marginal is
\[
\boxed{\displaystyle \beta_j=\frac{R_0-c_j}{\sum_{i<j}(c_j-c_i)}}.
\tag{4}
\]
The distinct thresholds obey \(0<\beta_S<\cdots<\beta_2\). For fixed \(j\), species \(j\) has positive limiting biomass for \(\beta<\beta_j\), is exponentially extinguished for \(\beta>\beta_j\), and at exactly \(\beta=\beta_j\) is extinguished only algebraically, with
\[
\boxed{\displaystyle\lim_{\tau\to\infty}\tau N_j(\tau)
=\frac{1}{\gamma\alpha_j^2c_j\left(\beta_j^{-1}+[1+\beta_j(j-1)]^{-1}\right)}}.
\tag{5}
\]
At the same critical rate, the local nutrient and shared nutrient have exact first-order relaxation amplitudes
\[
\lim_{\tau\to\infty}\tau(T_j(\tau)-c_j)=-\frac1{\alpha_j},\qquad
\lim_{\tau\to\infty}\tau(R(\tau)-c_j)=-\frac{\beta_j}{\alpha_j(1+j\beta_j)}.
\tag{6}
\]
The limits in (5)–(6) hold for **every** strictly positive initial state, not merely trajectories on a chosen center manifold.

## Assumptions and scope

Equation (1) is the \(\theta_i=1\) (fixed full isolation) and single-nutrient specialization of [1, equations (3)–(5)]. Time \(\tau\), uptake coefficients \(\alpha_i\), mortality rates \(k_i\), shared–local exchange \(\beta\), and conversion \(\gamma\) use its dimensionless normalization. The external resource supply \(R_0\) is constant. Species never migrate between niches; only nutrients exchange. No stochastic forcing, additional limiting nutrients, partial localization, nonlinear growth response, or time-varying localization is included.

Requiring \(c_S<R_0\) makes all \(S-1\) exchange thresholds positive. Distinct \(c_i\) excludes simultaneous multiple critical extinctions; the theorem does not assert the same inverse-time law when break-even levels coincide. The consumer abundance is measured in the original dimensionless biomass normalization \(N_i\), not the scaled variable used in the proof.

## Proof

**1. Equilibrium classification and strict threshold ordering.** Put \(x_i=\gamma N_i\) and \(t_i=\min\{c_i,r\}\). At a noninvasible equilibrium, a consumer with \(x_i>0\) must have \(T_i=c_i\), so its local nutrient equation gives \(x_i=\beta(r-c_i)/k_i>0\). For a missing consumer, \(x_i=0\), its nutrient satisfies \(T_i=r\), and nonpositive invasion growth requires \(r\le c_i\). Substitution into the shared nutrient equation gives (2). Its left side is continuous and strictly increasing from zero, so a unique \(r\in(0,R_0)\) exists. Formula (3) follows and has all missing-species invasion exponents nonpositive.

The solution \(r=r(\beta)\) is strictly decreasing: since \(r>c_1\), the positive-part sum is strictly positive, and a larger \(\beta\) forces a smaller \(r\). The crossing \(r=c_j\) yields (4), with positive numerator and denominator. The function \((R_0-c)/\sum_{c_i<c}(c-c_i)\) decreases strictly as \(c\) runs from \(c_2\) to \(c_S\), establishing the ordering. Since \(r>c_1\) for all finite \(\beta\), the first species always remains present.

**2. A strict global entropy dissipation identity, including boundary equilibria.** Let
\[
\phi_a(z)=z-a-a\log(z/a)\quad(a>0),\qquad \phi_0(z)=z.
\]
Set \(x_i^*=\gamma N_i^*\), and define
\[
\mathcal V=\phi_r(R)+\sum_i\phi_{t_i}(T_i)+\sum_i\phi_{x_i^*}(x_i).
\tag{7}
\]
For initially positive states all terms are well-defined. The mass balance \(R_0=r+\beta\sum_i(r-t_i)\) and the equilibrium uptake identities \(\alpha_it_ix_i^*=\beta(r-t_i)\) give by direct differentiation
\[
\dot{\mathcal V}=-\frac{(R-r)^2}{R}+\beta\sum_i F_i+
\sum_{\{i:x_i^*=0\}}(\alpha_ir-k_i)x_i,
\tag{8}
\]
where
\[
F_i=-\left(1-\frac rR\right)[(R-r)-(T_i-t_i)]
+\left(1-\frac{t_i}{T_i}\right)(R-T_i)
-\frac{(r-t_i)(T_i-t_i)}{t_i}.
\]
To check the nonstandard sign, write \(a=R/r\), \(b=T_i/t_i\), and \(d=t_i/r\in(0,1]\). Exact algebra gives
\[
\frac{F_i}{r}=3-d-
\left[d\left(\frac ba+\frac ab\right)+(1-d)\left(\frac1a+\frac ab+b\right)\right]\le0.
\tag{9}
\]
Indeed \(b/a+a/b\ge2\), while \(1/a+a/b+b\ge3\) by arithmetic–geometric mean, since the three factors have product one. Each missing species satisfies \(\alpha_ir-k_i\le0\). Thus \(\dot{\mathcal V}\le0\) everywhere in the positive domain.

For positive reference values, each entropy summand is coercive toward zero and infinity. For zero-reference consumer values, \(\phi_0(x)=x\) is coercive toward infinity and nonnegative down to the permitted boundary. Sublevels of \(\mathcal V\) consequently give compact forward-invariant sets with all resources, and all consumers with \(x_i^*>0\), bounded away from zero; missing consumers may approach zero. In the zero-dissipation set of (8), \(R=r\). Equation (9) then forces \(T_i=t_i\) for every \(i\). The local nutrient dynamics at these constant values force \(x_i=x_i^*\) for every \(i\), including marginally missing consumers (because \(\alpha_i t_i>0\)). Therefore the largest invariant zero-dissipation subset is the sole equilibrium (3). LaSalle's invariance principle yields convergence of **every** strictly positive orbit to (3), including nonhyperbolic critical cases.

**3. Simple critical eigendirection and universal extinction coefficient.** Fix \(j\in\{2,\ldots,S\}\), put \(\beta=\beta_j\), \(r=c_j\), and \(h=j-1\). Active indices are \(i<j\); all larger indices have strictly negative invasion exponents. The linearization on the face \(x_j=0\), excluding the strictly decaying larger-species coordinates, is Hurwitz. To see this directly, the quadratic term of (7), restricted to shared and local nutrient perturbations and positive-resident consumer perturbations, is positive definite. Its derivative is nonpositive by (8)–(9); equality of this quadratic dissipation forces all nutrient perturbations to vanish, and the local nutrient equations then force all resident-consumer perturbations to vanish. Hence no imaginary-axis eigenvector exists. The linearized matrix thus has strictly negative real-part eigenvalues. Reintroducing \(x_j\) gives exactly one simple zero eigenvalue, with the remaining spectrum in the open left half-plane.

Normalize a zero eigenvector by \(\delta x_j=1\). From the resident consumer and nutrient equations, \(\delta T_i=0\) and \(\delta x_i=(\beta/k_i)\delta R\) for \(i<j\). From the absent larger species' nutrient equations, \(\delta T_i=\delta R\) for \(i>j\). The marginal local nutrient equation and shared-resource balance give
\[
\delta R=-\frac{\alpha_jr}{1+\beta h},\qquad
\delta T_j=-\alpha_jr\left(\frac1\beta+\frac1{1+\beta h}\right).
\tag{10}
\]
For \(y=x_j\) the local center reduction (or stable-fiber slaving of any approaching positive orbit) is therefore
\[
\dot y=\alpha_j(T_j-r)y=-C_jy^2+O(y^3),\qquad
C_j=\alpha_j^2r\left(\frac1\beta+\frac1{1+\beta h}\right)>0.
\tag{11}
\]
In particular, the positive center branch is asymptotically attracting. As every strictly positive orbit has already been shown to converge to the equilibrium, its stable directions decay exponentially relative to its critical variable; the invariant face \(y=0\) is the stable manifold. Therefore all orbits with \(y(0)>0\) obey \(\dot y=-C_jy^2+o(y^2)\), so \(\tau y(\tau)\to1/C_j\). Since \(y=\gamma N_j\), this proves (5). Substituting (10) into the same asymptotic relation gives (6). There is no claim of a universal finite-time transient before the asymptotic regime.

## Verification

The standalone `check.py` verifies (9) symbolically, checks the coefficient identity in (10)–(11), constructs the exact rational stationary states, and integrates the equations for five exchange rates. With \(S=3\), \(\alpha_i=1\), \((k_1,k_2,k_3)=(1,2,3)\), \(R_0=5\), and \(\gamma=2\), the thresholds are \(\beta_3=2/3\) and \(\beta_2=3\). Formula (5) gives exactly \(\lim\tau N_3=7/81\) at \(\beta=2/3\), and \(\lim\tau N_2=3/7\) at \(\beta=3\). In both cases \(\lim\tau(T_j-c_j)=-1\). All executable tests passed. The exact proof, not these finite integrations, supplies the infinite-time and arbitrary-parameter conclusions.

Run from the directory containing the files with `python check.py`; the checker requires Python, NumPy, SciPy, and SymPy. Reproducibility of the proof uses only the displayed equations and elementary AM–GM, LaSalle invariance, and local center-manifold theory.

## Relationship to prior work

ElGamel and Mugler [1] introduce the shared/global nutrient model, including its fully separated limit, present two-species steady-state coexistence conditions in supplemental equations (S15)–(S24), and numerically examine survivor fractions. Equations (2)–(4) generalize that equilibrium bookkeeping, but **their existence alone is not the contribution**. The key additional results here are one global convergence statement valid on *all* extinct and critically neutral boundary faces and the **universal, normalized critical amplitudes** (5)–(6) for every positive initial condition and every species-entry threshold.

Classical chemostat stability results [2,3] and spatial chemostat diffusion studies [4,5] concern related but not identical kinetic structures; they motivate careful comparison rather than establishing this exact threshold-and-amplitude theorem. Spatial microbial coexistence studies [6] consider more complex geometric or interaction mechanisms. Claims about general critical slowing in ecological systems are not made; the computed coefficient and full global classification concern (1) alone.

## Limitations

The model assumes one abiotic resource, linear uptake, constant supply and mortality, equal exchange rates, and full fixed isolation of each niche. Repeated break-even levels are excluded. The algebraic extinction law is asymptotic and applies in deterministic dimensionless time; it is not a stochastic extinction-time prediction or an empirical population forecast. The critical theorem does not treat partial isolation, adaptive niche formation, nonlinear uptake, or multisubstrate chemostats. An equivalent theorem in older, unindexed compartmental literature cannot be categorically ruled out; related complete 2019 and 2023 articles were not accessible for full-text comparison.

## References

[1] M. ElGamel and A. Mugler, *Spatial structure promotes coexistence, resilience, and synergy in microbial communities*, arXiv:2611.00222v1, posted 2026-10-30. https://arxiv.org/html/2611.00222v1

[2] F. Mazenc and M. Malisoff, *Stability and stabilization for models of chemostats with multiple limiting substrates*, Journal of Biological Dynamics **6** (2012), 612–627. https://doi.org/10.1080/17513758.2012.663795

[3] N. Abdellatif, R. Fekih-Salem, and T. Sari, *Competition for a single resource and coexistence of several species in the chemostat*, Mathematical Biosciences and Engineering (2016). https://doi.org/10.3934/mbe.2016012

[4] I. Haidar, A. Rapaport, and F. Gérard, *Effects of spatial structure and diffusion on the performances of the chemostat*, Mathematical Biosciences and Engineering **8** (2011), 953–971. https://doi.org/10.3934/mbe.2011.8.953

[5] F. Yu, W. Song, and Y. Wang, *Effect of diffusion on a consumer-resource system with source-sink patches*, Discrete and Continuous Dynamical Systems B. https://doi.org/10.3934/dcdsb.2022152

[6] A. Lobanov, S. Dyckman, H. Kurkjian, and B. Momeni, *Spatial structure favors microbial coexistence except when slower mediator diffusion weakens interactions*, eLife **12** (2023), e82504. https://elifesciences.org/articles/82504
