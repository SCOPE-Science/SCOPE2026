# Sharp eighth-moment identification of hidden diffusivity switching and dissipation

## Finding
Consider a one-dimensional Brownian particle in a fixed harmonic trap whose diffusivity switches symmetrically between two unknown, distinct, strictly positive values. When the trap relaxation rate is known, **the second, fourth, and eighth moments of the stationary position law determine the two diffusivities (up to exchange), the switching rate, and the stationary entropy-production rate exactly**. The eighth order is optimal among one-time stationary position moments: all moments through order six leave a continuum of positive physical parameter triples indistinguishable, even though their entropy-production rates differ.

Write the known relaxation rate as \(\gamma>0\), the unknown switching rate as \(k>0\), and the unknown diffusivities as \(0<D_-<D_+\). Let \(S_t\in\{-,+\}\) flip in either direction at rate \(k\), independently of a standard Brownian motion \(W\). The model is
\[
 dX_t=-\gamma X_t\,dt+\sqrt{2D_{S_t}}\,dW_t.
\]
For its unique stationary law, define \(m_{2j}=\mathbb E[X_*^{2j}]\) and
\[
 M=m_2,\qquad B=\frac{m_4}{3}-M^2,\qquad
 R=\frac{m_8/105-M^4-6M^2B}{B^2}.
\]
Exactly the triples \((m_2,m_4,m_8)\) for which
\[
 \boxed{M>0,\quad B>0,\quad 1<R<3,\quad (3-R)M^2>2RB}
\]
arise from these positive nondegenerate switching models. On this exact admissible domain, the unique recovery (up to the names of the two states) is
\[
 \boxed{k=\frac{3\gamma(R-1)}{3-R},\qquad
 D_\pm=\gamma\left(M\pm\sqrt{\frac{2RB}{3-R}}\right).}
\]
The steady-state entropy-production rate \(\mathcal E\), in the convention of Alston--Cocconi--Bertrand, is likewise identified:
\[
 \boxed{\mathcal E=\frac{3\gamma B(R-1)}{(3-R)M^2-2RB}.}
\]
In every model of this family, odd stationary position moments vanish and
\[
 \boxed{m_6=15\left(M^3+3MB\right).}
\]
Consequently the sixth moment supplies a model-consistency identity but cannot separate switching frequency from diffusivity contrast.

## Assumptions and scope
The process is in its stationary regime on the entire real line. The Brownian noise and the two-state chain are independent. Both environmental transition rates equal \(k\); both diffusivities are positive and unequal; the harmonic relaxation \(\gamma\) is strictly positive and independently known. There are no hidden observations of \(S_t\), no time-lag measurements, and no measurement noise: the data are exact ensemble moments of a single stationary position snapshot. All positive finite values of \(\gamma,k,D_-,D_+\) satisfying these assumptions are included. The state labels are unobservable, so recovery of the diffusivities is necessarily unordered.

## Proof
**1. A stationary Gaussian variance mixture.** The dissipative stochastic integral
\[
 X_t=\int_{-\infty}^t e^{-\gamma(t-u)}\sqrt{2D_{S_u}}\,dW_u
\]
constructs the stationary solution and is unique by exponential contraction. Conditional on the entire chain history, it is centered Gaussian with variance
\[
 V_t=2\int_0^\infty e^{-2\gamma u}D_{S_{t-u}}\,du.
\]
Let \(\lambda=2\gamma\) and define the normalized exponentially weighted fraction of high-diffusivity time by
\[
 Y_t=\lambda\int_0^\infty e^{-\lambda u}{\bf1}_{\{S_{t-u}=+\}}\,du.
\]
Then \(0<Y_t<1\) almost surely and \(V_t=(D_-+(D_+-D_-)Y_t)/\gamma\). Reversibility of the symmetric two-state chain makes the backward history have the same law as the forward stationary chain. The Markovian weighted occupation variable evolves with drift \(\dot Y=\lambda(1-Y)\) in state \(+\) and \(\dot Y=-\lambda Y\) in state \(-\), switching at rate \(k\).

**2. Its exact beta law.** Let \(f_+(y),f_-(y)\) be stationary joint interior densities. Vanishing total probability flux at the two inaccessible endpoints yields \((1-y)f_+(y)=yf_-(y)\). Writing \(f=f_++f_-\), the first stationary transport equation becomes
\[
 \frac{d}{dy}\bigl[y(1-y)f(y)\bigr]=q(1-2y)f(y),
 \qquad q=\frac{k}{2\gamma}>0.
\]
Its unique normalized integrable solution is
\[
 f(y)=\frac{y^{q-1}(1-y)^{q-1}}{\mathrm B(q,q)},\qquad 0<y<1.
\]
Thus \(Y\sim\operatorname{Beta}(q,q)\). This density has mean \(1/2\), variance \(1/[4(2q+1)]\), vanishing third central moment, and standardized fourth central moment
\[
 \frac{\mathbb E[(Y-1/2)^4]}{\operatorname{Var}(Y)^2}
 =\frac{3(2q+1)}{2q+3}.
\]
The same identities follow from the stationary Markov generator; no Gaussian-mixture formula from another publication is assumed.

**3. The moment map.** Set \(v_\pm=D_\pm/\gamma\) and \(\delta=(v_+-v_-)/2\). Since \(V=M+2\delta(Y-1/2)\), the preceding beta identities imply
\[
 M=\frac{v_++v_-}{2},\qquad
 B=\operatorname{Var}(V)=\frac{\delta^2}{2q+1},\qquad
 \frac{\mathbb E[(V-M)^4]}{B^2}=\frac{3(2q+1)}{2q+3}.
\]
Conditional Gaussianity gives \(\mathbb E[X_*^{2n}]=(2n-1)!!\,\mathbb E[V^n]\) and zero odd moments. The beta symmetry then gives
\[
 m_2=M,\quad m_4=3(M^2+B),\quad
 m_6=15(M^3+3MB),\quad
 m_8=105(M^4+6M^2B+RB^2).
\]
In particular \(R=3(2q+1)/(2q+3)\).

**4. Sharp inversion and feasibility.** For \(q>0\), the last ratio increases strictly from \(1\) to \(3\), and inversion yields \(q=3(R-1)/[2(3-R)]\). Moreover
\[
 \delta^2=B(2q+1)=\frac{2RB}{3-R}.
\]
Thus \(v_\pm=M\pm\delta\), with the strictly positive lower diffusivity condition exactly \((3-R)M^2>2RB\). This proves necessity of every stated inequality and uniqueness. Conversely, any data satisfying those strict inequalities recover \(q>0\), \(\delta>0\), \(M>\delta\), and therefore a valid pair of positive diffusivities and positive switching rate. Substitution into the four moment identities returns exactly the prescribed observations. This proves sufficiency, including all boundary exclusions.

**5. Minimal observational order and explicit ambiguity.** The displayed expression for \(m_6\) shows that measurements up to order six determine only \(M\) and \(B\). Holding any feasible \(M,B\) fixed, every \(q\) in the nonempty interval
\[
 0<q<\frac12\left(\frac{M^2}{B}-1\right)
\]
produces a distinct admissible model with the same entire set of stationary moments of degree at most six by setting \(k=2\gamma q\) and \(D_\pm=\gamma(M\pm\sqrt{B(2q+1)})\). To make the ambiguity completely explicit, choose \(\gamma=1\) and either
\[
 (k,D_-,D_+)=(3,2,4),\qquad
 (k,D_-,D_+)=(8,3/2,9/2).
\]
Both models have \((m_2,m_4,m_6)=(3,111/4,1755/4)\), but the respective eighth moments are \(79485/8\) and \(1749195/176\). Their entropy-production rates differ as well, as shown next. The odd moments vanish in both models; hence degree eight is the first distinguishing stationary moment order.

**6. Thermodynamic implication.** Equation (45) in Alston, Cocconi and Bertrand (2022), specialized to symmetric diffusivity switching with common relaxation \(\gamma\), gives the independently established physical entropy-production formula
\[
 \mathcal E=\frac{\gamma k(D_+-D_-)^2}{4D_-D_+(\gamma+k)}.
\]
Substituting \(k=2\gamma q\), \(D_+-D_-=2\gamma\delta\), and \(D_-D_+=\gamma^2(M^2-\delta^2)\) yields \(\mathcal E=2\gamma qB/[M^2-(2q+1)B]\), and then the stated expression in \(M,B,R\). For the explicit ambiguous models, the entropy-production rates are \(3/32\) and \(8/27\), respectively. Thus even the dissipation is not identifiable from position moments of order six or lower, whereas the eighth moment identifies it exactly.

## Verification
Run `python3 verify_stationary_moments.py` from the same directory. The included standard-library-only script evaluates the beta moment hierarchy by the two-state transport generator, independently solves the coupled stationary diffusion moment hierarchy directly, compares them against the Gaussian beta-mixture moments, reconstructs parameters and entropy production for five exact rational test models, and verifies both ambiguity witnesses. It returned `PASS 114 exact rational assertions`. These finite checks independently exercise the derived identities; the global statement, continuum of ambiguities, uniqueness, and exact feasibility region are established by the analytical argument above, not by enumeration.

## Relationship to prior work
Alston, Cocconi and Bertrand (arXiv:2202.02630, Section 4.2.3, equation (45)) analyze precisely the symmetric switching-diffusivity harmonic model and give its forward entropy-production rate. They do not establish moment-order identifiability, the sharp inverse feasible domain, or an exact recovery of entropy production from stationary position-only moments. Zhang and Wang (2017) investigate stationary distributions of more general two-state Markov-switching Ornstein--Uhlenbeck systems; their Remark 3.1 notes parameter estimation as an application without giving this moment-optimal inversion. Frydel (arXiv:2407.12213) uses Gaussian-mixture representations for a physically different model with switching trap stiffness and fixed diffusivity, not the present constant-stiffness, switching-diffusivity map. Known beta moment formulas and Gaussian-mixture identities are used as standard tools, and the source forward entropy-production law is not claimed as new. The contribution is the exact inverse classification and its minimality and dissipation consequences.

## Limitations
Only symmetric two-state switching with independent Gaussian driving noise and known trap relaxation is considered. The labels of the two diffusivity states cannot be recovered. When the diffusivities coincide, the stationary law is Gaussian and the hidden switching rate is not identifiable. If the trap rate is unknown, simultaneous time rescaling leaves snapshot moments unchanged, so absolute rates cannot be recovered without temporal information. The result assumes exact ensemble moments; in particular, estimating an eighth moment from finite data can be unstable, and no finite-sample error bound is proved. The physical entropy-production normalization follows the stated published convention. The result does not characterize asymmetric switching, state-dependent trap stiffness, or other Markov-modulated diffusion families. Publication priority still requires independent literature review.

## References
1. H. Alston, L. Cocconi and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630 (first public version, 5 February 2022), Section 4.2.3, equation (45); J. Phys. A: Math. Theor. 55 (2022), 274004. https://arxiv.org/abs/2202.02630
2. Z. Zhang and W. Wang, *The stationary distribution of Ornstein--Uhlenbeck process with a two-state Markov switching*, Communications in Statistics -- Simulation and Computation 46 (2017), 4783--4794, especially Section 3 and Remark 3.1. https://doi.org/10.1080/03610918.2015.1132321
3. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213 (first public version, 16 July 2024), Sections II--III. https://arxiv.org/abs/2407.12213
4. Y. Lanoiselée, A. Stanislavsky, D. Calebiro and A. Weron, *Temperature and friction fluctuations inside a harmonic potential*, arXiv:2207.14068 (2022), for a related but different random-diffusivity model. https://arxiv.org/abs/2207.14068
