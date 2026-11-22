# Exact three-terminal heat law and sharp rectification bound on an Ising triangle

## Finding
Consider three ferromagnetically coupled Ising spins on the triangle, each connected to its own thermal bath and updated at rate one by local heat-bath Glauber flips. Write \(t_i=\tanh(2\beta_i J)\), where \(J>0\) and \(0<\beta_i<\infty\). The signed stationary heat current \(Q_i\) **from** bath \(i\) **into** the spins satisfies an exact three-terminal nonlinear conductance law:

\[
Q_i=\frac{2J}{\Delta}\sum_{j\ne i}(4+t_k)(t_j-t_i),\quad
\Delta=32-t_1t_2t_3-2(t_1t_2+t_1t_3+t_2t_3),
\]

where \(k\) is the remaining vertex outside \(\{i,j\}\). In particular, \(Q_1+Q_2+Q_3=0\) and every effective pair conductance \(2J(4+t_k)/\Delta\) is strictly positive. Thus the hottest reservoir always supplies heat, the coldest always receives it, and a reservoir with intermediate temperature has exactly one zero-current value as its own temperature is varied between the others.

For \(0<\beta_{\mathrm h}<\beta_{\mathrm c}<\infty\), put \(x=\tanh(2\beta_{\mathrm h}J)\) and \(y=\tanh(2\beta_{\mathrm c}J)\). Compare (A) one hot spin/two cold spins with (B) two hot spins/one cold spin; measure the **total current out of the hot reservoir** in each case. Then

\[
R(x,y)=\frac{Q_{\rm hot,A}}{Q_{\rm hot,B}}
=\frac{8-xy-2x}{8-xy-2y},\qquad
1<R(x,y)<\frac43.
\]

The upper bound is sharp and unattained at finite strictly positive temperatures: it is approached only as \(x\to0\), \(y\to1\), that is, infinite hot-bath and zero cold-bath temperatures. This is a finite-state stationary rectification law, not a thermodynamic phase transition.

## Assumptions and scope
The configuration space is \(\sigma\in\{-1,+1\}^3\) with energy
\[\mathcal H(\sigma)=-J(\sigma_1\sigma_2+\sigma_2\sigma_3+\sigma_3\sigma_1),\quad J>0.\]
Each site has an independent unit-rate Poisson update clock. At site \(i\), the heat-bath update draws the spin from the Gibbs conditional law at its assigned inverse temperature \(\beta_i>0\). Equivalently, the flip rate is
\[
c_i(\sigma)=\frac12\left[1-\frac{t_i}{2}\sigma_i(\sigma_j+\sigma_k)\right],\qquad t_i=\tanh(2\beta_iJ).
\]
The heat current is defined through the energy change \(\mathcal H(\sigma^{(i)})-\mathcal H(\sigma)\) induced by a flip, weighted by \(c_i\). There is no applied magnetic field and no constraint on total magnetization. Rates and bond strengths are identical at all sites except for the bath temperatures. Temperatures are finite and positive in all strict statements; limiting temperatures are used only to state the sharp supremum.

## Proof
Set \(a=t_1,b=t_2,c=t_3\), \(C_{ij}=\mathbb E_\pi[\sigma_i\sigma_j]\), with \(\pi\) the unique stationary distribution. For \(\{i,j,k\}=\{1,2,3\}\), applying the generator to \(\sigma_i\sigma_j\) gives
\[
0=-2C_{ij}+\frac{t_i}{2}(1+C_{jk})+\frac{t_j}{2}(1+C_{ik}).\tag{1}
\]
This is a three-by-three linear system. Solving it gives, with the above \(\Delta\),
\[
C_{12}=\frac{(4+c)(ab+2a+2b)}{\Delta},\quad
C_{13}=\frac{(4+b)(ac+2a+2c)}{\Delta},\quad
C_{23}=\frac{(4+a)(bc+2b+2c)}{\Delta}.\tag{2}
\]
Because \(a,b,c\in(0,1)\), we have \(\Delta>25\), and every spin-flip rate is strictly positive. Therefore the chain is irreducible and has a unique stationary distribution; the solution of (1) must be its pair correlations. In fact global spin-flip invariance gives explicitly
\[
\pi(\sigma)=\frac18\bigl[1+C_{12}\sigma_1\sigma_2+C_{13}\sigma_1\sigma_3+C_{23}\sigma_2\sigma_3\bigr].
\]

A flip at site \(i\) changes the energy by \(2J\sigma_i(\sigma_j+\sigma_k)\). Consequently,
\[
Q_i=\mathbb E_\pi[2J\sigma_i(\sigma_j+\sigma_k)c_i(\sigma)]
=J\bigl(C_{ij}+C_{ik}-t_i(1+C_{jk})\bigr).\tag{3}
\]
Substituting (2) into (3), collecting terms and cancelling, gives
\[
Q_1=\frac{2J}{\Delta}\bigl[(b-a)(4+c)+(c-a)(4+b)\bigr],
\]
with the other two currents obtained cyclically. This is the claimed conductance law. Pairwise antisymmetry establishes total-current conservation. Its coefficients are positive, hence heat flows on each effective bond from smaller to larger inverse-temperature parameter. More explicitly, steady-state reservoir entropy production is
\[
\dot S_{\rm res}=-\sum_i\beta_iQ_i
=\frac{2J}{\Delta}\sum_{i<j}(4+t_k)(\beta_i-\beta_j)(t_i-t_j)\ge0,
\]
with equality exactly at equal bath temperatures.

Fix two bath parameters \(t_j=p<t_k=q\). The current at the third bath vanishes exactly when
\[
t_i=\frac{p(4+q)+q(4+p)}{8+p+q}.\tag{4}
\]
The right side lies strictly between \(p\) and \(q\), because its differences from them are \((q-p)(4+p)/(8+p+q)\) and \((q-p)(4+q)/(8+p+q)\). Since \(t_i\) increases strictly with \(\beta_i\), the zero-current temperature is unique.

For the two-bath comparison \(0<x<y<1\), the preceding current formula simplifies to
\[
Q_{\rm hot,A}=\frac{4J(y-x)}{8-xy-2y},\qquad
Q_{\rm hot,B}=\frac{4J(y-x)}{8-xy-2x}.
\]
Each is the total current contributed by the hot reservoir, whether it serves one spin or two. Their ratio is the stated \(R\). Now
\[
R=1+\frac{2(y-x)}{8-xy-2y},\qquad
\frac{\partial R}{\partial x}
=-\frac{2(8-2y-y^2)}{(8-xy-2y)^2}<0.
\]
Thus \(R(x,y)<R(0,y)=8/(8-2y)<4/3\). Letting \(x\to0\) and \(y\to1\) gives equality in the limiting supremum, proving sharpness and strict unattainability for finite positive temperatures.

## Verification
Run `python3 verify.py` with Python 3 and SymPy. It independently constructs the complete eight-state Markov generator, solves for its normalized stationary distribution by exact rational linear algebra, obtains all three stationary pair correlations and heat currents directly, and compares each with the claimed closed formulas for 125 rational bath triples. It also checks three two-temperature rectification identities and positivity of every computed stationary weight. The script prints `EXACT_8_STATE_CHECKS_PASSED 125` and `RECTIFICATION_IDENTITIES_PASSED` on success. These finite checks supplement the symbolic proof; they are not used to infer the all-temperature statements.

## Relationship to prior work
Schmüser and Schmittmann (2002) analyze nonequilibrium two-temperature kinetic Ising chains with alternating bath assignments using perturbation theory. Schmittmann and Schmüser (2002) obtain exact correlations for even-site alternating-temperature rings. Lecomte, Rácz and van Wijland (2004) study a thermodynamic-limit infinite-range Ising model, including a general number of baths in the appendices. Borchers, Pleimling and Zia (2014) analyze conserved-spin Kawasaki exchange dynamics in a two-temperature ring. These works establish related nonequilibrium spin and heat-flow methods but not the finite three-spin triangle with three independent unit-rate heat-bath Glauber reservoirs and its exact network law or sharp bath-exchange ratio. The triangle is non-bipartite and its three-bath generator is not a specialization of the even-ring alternating-bath model.

## Limitations
The theorem is restricted to exactly three spins, equal positive nearest-neighbor bonds, zero external field, positive finite temperatures, and unit-clock heat-bath flip dynamics. It says nothing about longer rings, altered flip rules, unequal couplings, thermal-current fluctuations, or phase transitions. It does not establish scientific priority over unpublished or unindexed finite-cluster calculations. The ratio compares specific one-versus-two reservoir placements, not arbitrary two-terminal architectures. All formulas are steady-state, not finite-time.

## References
- F. Schmüser and B. Schmittmann, *Non-equilibrium stationary state of a two-temperature spin chain*, arXiv:cond-mat/0206345 (first public posting 2002-06-18), https://arxiv.org/abs/cond-mat/0206345 .
- B. Schmittmann and F. Schmüser, *Stationary correlations for a far-from-equilibrium spin chain*, arXiv:cond-mat/0212616 (2002-12-27), https://arxiv.org/abs/cond-mat/0212616 .
- V. Lecomte, Z. Rácz and F. van Wijland, *Energy flux distribution in a two-temperature Ising model*, arXiv:cond-mat/0412547 (2004-12-20), https://arxiv.org/abs/cond-mat/0412547 .
- N. Borchers, M. Pleimling and R. K. P. Zia, *Nonequilibrium statistical mechanics of a two-temperature Ising ring with conserved dynamics*, arXiv:1411.6180 (2014-11-22), https://arxiv.org/abs/1411.6180 .
