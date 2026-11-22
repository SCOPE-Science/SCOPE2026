# Sharp sixth-cumulant tomography and hidden dissipation of a four-direction trapped swimmer

## Finding

A single stationary position ensemble of a thermally diffusing, harmonically confined four-direction run-and-tumble swimmer determines its *unobserved propulsion axes*, dimensionless turning rate, propulsion amplitude, thermal diffusivity, and the dimensionless total entropy-production rate from directional cumulants of orders **two, four and six**. The inference is globally unique, and order six is necessary when the propulsion amplitude and thermal diffusivity are both unknown. The precise attainable region of these three cumulants is given below.

Let the trap relaxation rate \(\mu>0\) be independently calibrated. Write the symmetric quarter-turn rate \(\gamma>0\), rotated-coordinate active speed \(v>0\), and isotropic translational diffusivity \(D>0\), and put
\[
\beta=\gamma/\mu,\qquad a=v/\mu,\qquad h=D/\mu.
\]
The coordinate axes \(u,v\) (orthogonal, bisecting the four physical velocity directions) are determined up to sign and exchange by the **strict minima** of the fourth directional cumulant \(\kappa_4(\theta)\). In angular coordinates measured from one such axis,
\[
\kappa_4(\theta)=-\frac{6a^4}{(2\beta+1)^2(2\beta+3)}\frac{3+\cos(4\theta)}4.
\]
Take one recovered axis and denote its positional cumulants by \(s=\kappa_2>0\), \(-k=\kappa_4<0\), and \(w=\kappa_6>0\). They obey the sharp dimensionless corridor
\[
\boxed{0<R:=\frac{w^2}{k^3}<32,\qquad
s>\sqrt{\frac{k(2\beta+3)}6},}
\]
where \(\beta\) is determined uniquely from \(R\) by
\[
\boxed{t=\frac{800+\sqrt{640000-19200R}}{6R},\quad
\beta=\frac{t-5}{2}.}
\]
The complete physical inverse is
\[
\boxed{a=\sqrt{2\beta+1}\left[\frac{k(2\beta+3)}6\right]^{1/4},
\qquad h=s-\sqrt{\frac{k(2\beta+3)}6}>0.}
\]
Every triple satisfying the displayed strict inequalities, with \(w=\sqrt{Rk^3}>0\), is realized by exactly one parameter triple \((\beta,a,h)\). In the even-orientation time-reversal convention, the known stationary entropy-production law becomes the **position-only thermodynamic reconstruction**
\[
\boxed{\frac{\dot S}{\mu}=
\frac{4\beta\sqrt{k(2\beta+3)/6}}{s-\sqrt{k(2\beta+3)/6}}.}
\]
This concerns the ideal exact ensemble distribution; it does not assert finite-sample or trajectory-level identifiability.

## Assumptions and scope

Let \(\mathbf X_t\in\mathbb R^2\) solve, in its unique stationary regime,
\[
d\mathbf X_t=(-\mu\mathbf X_t+\sqrt2v\mathbf e_{\Theta_t})dt+\sqrt{2D}\,d\mathbf B_t,
\]
with \(\mu,v,\gamma,D>0\), standard planar Brownian motion \(\mathbf B\), and \(\mathbf e_{\Theta}\) taking four unit values separated by right angles. From every heading, the chain turns clockwise at rate \(\gamma\) and counterclockwise at the same rate \(\gamma\), independently of \(\mathbf B\); there are no separate half-turns, position resets, anisotropic traps or heading biases. The absolute orientation of the four heading directions may be unknown. The propulsion speed magnitude is \(\sqrt2v\), so \(v\) is the speed component in the diagonal coordinates. When \(\mu\) is known, \(\gamma=\mu\beta\), \(v=\mu a\), and \(D=\mu h\) are recovered in physical units. Without that calibration, only their dimensionless ratios and \(\dot S/\mu\) are identifiable from a stationary snapshot.

All cumulants are population cumulants of the stationary positional marginal and are indexed by polynomial degree, not sample estimates. For a unit vector making angle \(\theta\) with a recovered diagonal axis, \(\kappa_j(\theta)\) is the order-\(j\) scalar cumulant of its projection. The physical entropy-production convention treats orientations as even under time reversal, and includes both diffusive and orientation-jump contributions. The athermal case \(D=0\) obeys the same shape inversion with a non-strict feasibility inequality, but then the displayed finite entropy-production formula is not applicable; all main claims above assume \(D>0\).

## Proof

**1. Independent diagonal coordinates and thermal convolution.** A quarter-turn switches exactly one of the two diagonal orientation signs. Equal clockwise and counterclockwise jump rates therefore make these signs independent stationary telegraph processes, each flipping at rate \(\gamma\). The diagonal positions \(U,V\) are independent, identically distributed filters of their respective telegraph processes plus independent Brownian OU noise. In a diagonal coordinate, the stationary active part is \(aZ_\beta\), where \(Z_\beta\) has the known symmetric Beta density
\[
f_\beta(z)=\frac{\Gamma(\beta+1/2)}{\sqrt\pi\Gamma(\beta)}(1-z^2)^{\beta-1}{\bf1}_{|z|<1}.
\]
The Brownian contribution is an independent \(G\sim N(0,h)\), so \(U\overset d=aZ_\beta+G\). This stationary law follows either from the zero-flux telegraph transport equations or from the exact known trapped-swimmer propagator. Strict \(\mu,\gamma>0\) and the stable linear filter ensure the invariant law exists uniquely.

**2. Exact cumulants and angular anisotropy.** The beta integral gives, for integer \(j\ge0\),
\[
\mathbb E[Z_\beta^{2j}]=\frac{(1/2)_j}{(\beta+1/2)_j},\qquad
\mathbb E[Z_\beta^{2j+1}]=0.
\]
Because independent Gaussian noise contributes only to the second cumulant, these identities imply
\[
\kappa_2(U)=h+\frac{a^2}{2\beta+1},\quad
\kappa_4(U)=-\frac{6a^4}{(2\beta+1)^2(2\beta+3)},\quad
\kappa_6(U)=\frac{240a^6}{(2\beta+1)^3(2\beta+3)(2\beta+5)}.
\]
For \(Z_\theta=U\cos\theta+V\sin\theta\), independence and multilinearity of cumulants give \(\kappa_4(Z_\theta)=\kappa_4(U)(\cos^4\theta+\sin^4\theta)\). Using \(\cos^4\theta+\sin^4\theta=(3+\cos4\theta)/4\) and \(\kappa_4(U)<0\), the unique minimizing **unoriented** axes are the diagonal lines (modulo sign and exchange). Covariance alone is isotropic and cannot identify these axes; degree four is sufficient and the first possible even anisotropic order.

**3. Global inverse and exact feasibility.** Set \(k=-\kappa_4(U)>0\), \(w=\kappa_6(U)>0\). Cancelling the positive unknown amplitude yields
\[
R=\frac{w^2}{k^3}=\frac{800(2\beta+3)}{3(2\beta+5)^2}.
\]
Its derivative is \(-1600(2\beta+1)/[3(2\beta+5)^3]<0\); its endpoint limits as \(\beta\downarrow0\), \(\beta\uparrow\infty\) are \(32\) and \(0\). Hence it is a strict bijection from \((0,\infty)\) onto \((0,32)\). With \(t=2\beta+5>5\), the ratio equation is \(3Rt^2-800t+1600=0\). Of the two algebraic roots, only the displayed larger root is greater than five. This establishes a unique \(\beta\).

The fourth cumulant then yields \(a^4=k(2\beta+1)^2(2\beta+3)/6\); its unique positive root gives the displayed \(a\). The active variance is precisely
\[
\frac{a^2}{2\beta+1}=\sqrt{\frac{k(2\beta+3)}6},
\]
so the second cumulant recovers \(h=s-\sqrt{k(2\beta+3)/6}\), which is positive exactly under the stated inequality. Conversely, these reconstructed parameters are strictly positive for every triple in the claimed region and substitution reproduces all three cumulants. This proves both necessary and sufficient feasibility, global injectivity, and the exact parameter boundary exclusions.

**4. Sixth order is necessary when thermal intensity and speed are unknown.** Fix any interior physical \((\beta_0,a_0,h_0)\), and hold its second and fourth cumulants fixed. For every \(\beta\) in a sufficiently small open interval about \(\beta_0\), set
\[
a(\beta)^4=\frac{k(2\beta+1)^2(2\beta+3)}6,\qquad
h(\beta)=s-\sqrt{\frac{k(2\beta+3)}6}.
\]
Continuity preserves \(a(\beta)>0\) and \(h(\beta)>0\) in that interval, giving continuously many genuinely different positive physical parameter triples with identical second- and fourth-degree cumulants (indeed, identical entire moments up to degree four, by reflection symmetry and isotropic covariance). The ratio in step 3 varies strictly with \(\beta\), so the sixth cumulant distinguishes all of them. Thus order six is minimal within one-time stationary polynomial position statistics for reconstructing all parameters. The orientation itself is already identifiable at degree four.

**5. Thermodynamic reconstruction.** Under the specified even-orientation entropy convention, steady entropy balance with symmetric orientation transitions gives
\[
\dot S=\frac1D\mathbb E[(\sqrt2v\mathbf e_\Theta)\cdot(-\mu\mathbf X+\sqrt2v\mathbf e_\Theta)].
\]
The stationary joint generator yields \(\mathbb E[(\sqrt2v\mathbf e_\Theta)\cdot\mathbf X]=2v^2/(\mu+2\gamma)\), since each diagonal telegraph component relaxes at rate \(2\gamma\). Also \(\mathbb E[|\sqrt2v\mathbf e_\Theta|^2]=2v^2\). Therefore
\[
\dot S=\frac{4\gamma v^2}{D(\mu+2\gamma)},\qquad
\frac{\dot S}{\mu}=\frac{4\beta a^2}{h(1+2\beta)}.
\]
Inserting the recovered active variance and \(h\) proves the boxed position-only formula. The entropy-production expression itself is established previous physics; the new statement is recovery of its value from a finite collection of **position-only** cumulants without observing orientation transitions.

## Verification

Run `python verify.py` with Python 3 and SymPy from the package directory. It solves the independent two-state telegraph-plus-Gaussian stationary generator recurrence through moment order eight (rather than inserting the Beta density), computes the cumulants, verifies the inverse polynomial and ratio derivative, tests the angular identity, and checks 45 exact rational parameter cases at three nonnegative noise intensities. It additionally checks the nonidentifiability witness, an exact positive-noise sample and the active-power identity. The recorded run returned `PASS: 197 exact symbolic/rational checks`. General uniqueness, feasibility and minimality are proved algebraically above; no finite test is substituted for those universal arguments.

For \(\beta=a=1\), \(h=1/5\), one finds \((s,k,w)=(8/15,2/15,16/63)\), \(R=4000/147\), and reconstructs precisely \((\beta,a,h)=(1,1,1/5)\). Its normalized entropy-production rate is \(\dot S/\mu=20/3\).

## Relationship to prior work

Smith, Le Doussal, Majumdar and Schehr [1] establish the exact product-Beta stationary law of the right-angle turning model and the independent Gaussian convolution when translational diffusion is present. Their full positional distribution, angular anisotropy and expression for stationary entropy production are **prior inputs**, not discoveries here. The additional result is the sharp inverse *three-cumulant* feasible-data region, unknown-axis recovery, rigorous necessity of sixth order in the presence of unknown Gaussian broadening, and position-only determination of the established dissipation rate.

Frydel [2] derives and exploits general moment recurrences for run-and-tumble oscillators, including Gaussian thermal convolution; the supplied recurrence and forward moment technique are established methods, not claimed new. A published inverse theorem for a three-state finite-tumble oscillator [3] also requires a sixth moment to resolve a distinct two-rate ambiguity, but its internal chain has a zero-speed rest state and its analysis assumes calibrated propulsion/trap scales with no thermal diffusion. A published eighth-moment inversion theorem [4] concerns stochastic *diffusivity* switching and a Gaussian-variance mixture, not fixed-amplitude four-direction propulsion. Another four-state swimmer result [5] identifies a fourth-order signed chirality witness under **unequal** clockwise/counterclockwise turning rates, whereas this theorem assumes their equality and recovers scalar rate, speed, thermal diffusivity and dissipation. None of these inspected statements supplies the claimed exact three-parameter feasible region or the isotropically thermalized, axis-blind position-only inverse for the equal-turn model. Forward-law implications remain an acknowledged publication-priority risk: the algebraic cumulants follow from the known Beta density, but global inverse feasibility and minimality need additional proofs.

## Limitations

The theorem is for stationary ideal-population cumulants, isotropic thermal Brownian forcing, precisely symmetric right-angle turning, and a harmonic trap with known relaxation \(\mu\). No guarantee of robustness against sampling noise, uncertainty in \(\mu\), unmodeled drift, anisotropic heating, finite exposures or hidden variations in propulsion speed is claimed. In the singular regimes \(\beta\downarrow0\) and \(\beta\uparrow\infty\) the inverse becomes poorly conditioned; the strict feasible corridor excludes those endpoints. The recovered orientation has unavoidable sign and quarter-turn equivalences. The entropy-production rate uses the stated even-orientation convention and is not interchangeable with differently defined hidden-path entropy or inference of microscopic parity. The physical normalization assumes a positive thermal diffusivity; as \(D\downarrow0\), the formula diverges and no finite entropy-production value is asserted. Independent scientific validation and broader publication-priority review remain outstanding.

## References

1. N. R. Smith, P. Le Doussal, S. N. Majumdar, G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445, first public release 2022-07-21, https://arxiv.org/abs/2207.10445 .
2. D. Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, arXiv:2309.12537, first public release 2023-09-21, https://arxiv.org/html/2309.12537v1 .
3. *A twofold stationary-moment fold and three-moment identifiability in a finite-tumble harmonic particle*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-twofold-stationary-moment-fold-and-three-moment-identifiabilit--be13e0084c9a .
4. *Sharp eighth-moment identification of hidden diffusivity switching and dissipation*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-eighth-moment-identification-of-hidden-diffusivity-switchi--56d3d976847e .
5. *A fourth-order chirality fingerprint and exact factorization boundary for harmonically trapped four-state swimmers*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-fourth-order-chirality-fingerprint-and-exact-factorization-bou--f3729281ca46 .
