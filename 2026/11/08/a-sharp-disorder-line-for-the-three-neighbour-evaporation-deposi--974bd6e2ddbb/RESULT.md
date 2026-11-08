# A sharp disorder line for the three-neighbour evaporation–deposition automaton

## Finding

For the periodic three-neighbour evaporation–deposition probabilistic cellular automaton (NED), let the deposition parameter be \(p\in(0,1)\) and the complementary second deposition parameter be \(q\in(0,1)\). Define
\[
a=1-p,\qquad b=\frac{a^2}{q},\qquad P(z,q)=1-(1+p)z+p^2z^2+p(a-b)z^3.
\]
Define the quadratic in \(q\)
\[
R_p(q)=(1-p)^2(3p-4)q^2-2(p-2)(7p^2-10p+1)q+27p(1-p)^2.
\]
There is exactly one positive zero \(q_c(p)\), which obeys \(0<q_c(p)<1-p\). The infinite-volume stationary connected occupation correlation \(C_r=\mathbb E[\eta_0\eta_r]-\mathbb E[\eta_0]^2\), at integer separation \(r\geq1\), has the following *complete long-distance classification*.

* If \(0<q<q_c(p)\), the two subleading spatial modes form a nonreal conjugate pair. There exist \(A\neq0\), \(0<\vartheta<\pi\) and \(0<\kappa<1\) such that \(C_r=2\operatorname{Re}(A\kappa^re^{-ir\vartheta})\) exactly for every \(r\geq1\). The correlation changes sign infinitely often and its oscillation wavelength need not be commensurate with the lattice.
* If \(q=q_c(p)\), there is a nonzero positive constant \(K\) and \(0<\kappa<1\) such that \(C_r\sim K r\kappa^r\). The polynomial prefactor is the signature of the double subleading pole.
* If \(q_c(p)<q<1\), there are \(K>0\), \(0<\kappa<1\) such that \(C_r\sim K\kappa^r\). In this region the asymptotic correlations are strictly positive and nonoscillatory.

At the boundary, if \(z_c>1\) denotes the double root of \(P(\cdot,q_c)\), the oscillation angle for \(q\uparrow q_c\) satisfies
\[
\vartheta(q)\sim \frac{1}{z_c}\sqrt{-\frac{2P_q(z_c,q_c)}{P_{zz}(z_c,q_c)}}\sqrt{q_c-q}.
\]
Here \(P_q>0\) and \(P_{zz}<0\) at this double root, so the oscillation wavelength diverges as \((q_c-q)^{-1/2}\). These statements describe a spatial *disorder line*, not a singularity of the bulk free energy.

The three-neighbour model is the first neighbourhood size in the NED family admitting nonreal stationary spatial modes: at neighbourhood size two the spatial transfer polynomial is quadratic with strictly positive discriminant for every admissible parameter pair.

## Assumptions and scope

The model uses a periodic ring of length \(n\geq3\), binary variables \(\eta_i\), and independent synchronous updates conditioned on the current configuration. A site becomes occupied with probability \(p\) if its current triple beginning at that site is \(000\), and with probability \(1-q\) if the triple is \(001\); in all remaining cases the next occupation is zero. Parameters satisfy \(0<p,q<1\). The infinite-volume correlation is obtained by taking the periodic stationary law to its unique translation-invariant thermodynamic limit *before* sending \(r\to\infty\). No assertion about dynamical time correlations, finite-rate phase transitions or additional stationary phases is made.

Set \(a=1-p\), \(b=a^2/q\), and
\[
T=\begin{pmatrix}p&1&0\\pa&0&1\\pb&0&1\end{pmatrix},\quad
U(z)=p\left(z+az^2+\frac{bz^3}{1-z}\right),\quad
P(z)=(1-z)(1-U(z)).
\]
Let \(z_0\in(0,1)\) be the unique solution \(U(z_0)=1\), and let \(\rho=\big[z_0U'(z_0)\big]^{-1}\). The other roots of \(P\), counted with multiplicity, have modulus strictly greater than \(z_0\) (with the root at infinity omitted when the cubic coefficient vanishes). When these roots are simple, write them \(z_1,z_2\) and set \(A_j=-(1-z_j)/(z_jP'(z_j))\). Then an exact form, stronger than the three asymptotic cases above, is
\[
C_r=\rho\sum_{j=1}^2 A_j\left(\frac{z_0}{z_j}\right)^r,\qquad r\geq1.
\]
At the removable quadratic parameter \(q=1-p\), only the finite non-Perron root appears.

## Proof

**1. Exact finite-ring representation.** By the stationary-weight formula of Ayyer and Podder (Theorem 3.3 of the cited source), a configuration containing at least one occupied site is weighted by \(p\) per occupied site and, for each intervening zero gap of length \(g\), by the factor \(w_g\) with \(w_0=1\), \(w_1=a\), and \(w_g=b\) for \(g\geq2\). The all-zero configuration has weight one. Three transfer states (zero, one, or at least two zeros since the last occupied site) therefore give the matrix \(T\) above, and the finite-ring partition function is exactly \(Z_n=\operatorname{tr}(T^n)\). This is valid for every \(n\geq3\); no infinite-ring assumption enters this step. The matrix is nonnegative, irreducible and aperiodic because \(p,b>0\) and both a self-loop at the occupied state and the long-zero state exist. Consequently it has a simple positive Perron eigenvalue and the periodic stationary local measures have a unique translation-invariant thermodynamic limit.

**2. The thermodynamic renewal kernel.** The gap-length generating series is \(U(z)=p\sum_{g\geq0}w_gz^{g+1}\). Since \(U\) increases continuously from zero to infinity on \((0,1)\), there is precisely one \(z_0\in(0,1)\) with \(U(z_0)=1\). The limiting Palm interarrival probabilities are \(f_\ell=pw_{\ell-1}z_0^\ell\) for all \(\ell\geq1\). They sum to one and have finite mean \(\mu=z_0U'(z_0)\), giving occupation density \(\rho=1/\mu\). If \(u_r\) is the probability of an occupied site at separation \(r\) conditional on occupation at the origin, the renewal equation has generating series
\[
\sum_{r\geq0}u_rs^r=\frac{1}{1-U(z_0s)}=\frac{1-z_0s}{P(z_0s)}.
\]
Thus \(C_r=\rho(u_r-\rho)\). Partial fractions yield the exact displayed root formula. Specifically the coefficient of the Perron pole \(z_0\) is \(- (1-z_0)/(z_0P'(z_0))=\rho\); all other poles determine the connected part. Perron–Frobenius guarantees \(\lvert z_j\rvert>z_0\). The finite-ring Perron limit or, equivalently, the normalized renewal bridge gives the stated thermodynamic interpretation.

**3. A unique sharp spectral boundary.** Direct calculation gives
\[
\operatorname{disc}_zP=-\frac{p(1-p)^2}{q^2}R_p(q).
\]
The leading coefficient of \(R_p\) is strictly negative, its constant coefficient is strictly positive, and \(R_p(1-p)=p^3(p-1)(3p+1)<0\). Hence \(R_p\) has exactly one positive zero and that zero lies strictly between zero and \(1-p\). For \(q<q_c\) the cubic has one real root \(z_0\) and a nonreal conjugate pair. Its nonzero residue amplitude and nonzero phase imply infinitely many changes of sign. For \(q_c<q<1-p\), all three roots are positive, with \(z_0<1<z_1<z_2\). For \(q>1-p\), exactly two roots are positive and the third is negative; Vieta's relation \(z_0+z_1+z_2=-p/(a-b)<0\) shows the magnitude of the negative root is larger than that of the non-Perron positive root. The relevant positive root \(z_1>1\) therefore controls the tail throughout \(q>q_c\). Its amplitude \(-(1-z_1)/(z_1P'(z_1))\) is positive. At \(q=1-p\) the cubic term vanishes and the same statement follows from the two real positive roots of the remaining quadratic.

**4. Double pole and boundary exponent.** At \(q=q_c\), the two non-Perron positive roots coalesce to \(z_c>1\); the polynomial factors as \(P(z)=c(z-z_0)(z-z_c)^2\) with \(c<0\). The coefficient of \((1-z/z_c)^{-2}\) in \((1-z)/P(z)\) is
\[
B=\frac{2(1-z_c)}{z_c^2P_{zz}(z_c,q_c)}>0.
\]
Consequently \(C_r\sim\rho B r(z_0/z_c)^r\). Since \(P_q(z_c,q_c)=p(1-p)^2z_c^3/q_c^2>0\) while \(P_{zz}(z_c,q_c)<0\), the Taylor expansion at the double root gives \(z_\pm(q)=z_c\pm i\sqrt{-2P_q/P_{zz}}\sqrt{q_c-q}+O(q_c-q)\). Taking arguments gives the asserted square-root law.

**5. Minimality.** For neighbourhood size two, the same gap construction gives \(P_2(z)=1-(1+p)z+p(1-(1-p)/q)z^2\). Its discriminant \((1-p)^2+4p(1-p)/q\) is strictly positive. Thus its only non-Perron mode is real and may at most alternate in sign; continuously varying nonzero spatial angles first arise at neighbourhood size three. This does not claim that size-two covariances are always positive.

## Verification

The companion `verify_disorder_line.py` reconstructs the characteristic polynomial and its discriminant in exact symbolic arithmetic. It independently enumerates the source stationary weights on periodic rings, compares those partition functions and two-point occupation sums to the transfer-matrix traces, checks both sides of the sharp boundary across parameter samples, and verifies the explicit example \(p=1/2,q=1/5\) with roots \(2/3,2i,-2i\). Run `python verify_disorder_line.py` with Python, NumPy and SymPy. This yields 310 passing checks in the recorded environment. Finite-size checks do not establish the thermodynamic limit; the transfer-matrix and renewal arguments above provide that proof.

## Relationship to prior work

Ayyer and Podder, arXiv:2602.23837v1 (first public release 2026-02-27), prove the finite-ring stationary distribution, normalizer and density and treat the size-two free energy explicitly. Their finite-ring weights are essential starting evidence, not a new result here. The searched full HTML text contains no stated two-point correlation formula, discriminant boundary, or oscillation-angle asymptotic; these are the present deductions. Older transfer-spectrum work establishes that complex spatial eigenvalues can produce damped oscillations in other lattice systems, but does not supply the NED parameter boundary. The complete explicit stationary law means this is a **derived spatial-ordering classification**, not an independently solved stationary distribution.

## Limitations

The theorem concerns stationary *spatial* two-point occupation covariances, not temporal relaxation or a nonanalytic thermodynamic transition. Both parameters are strictly between zero and one; endpoint regimes are excluded. General transfer-matrix theory establishes the broad mechanism, so originality is specifically the sharp NED curve, its coefficient, the coalescing-pole boundary law and neighbourhood minimality. An unindexed model-specific derivation could supersede that contribution. The numerical checker is corroborative, not an independent proof or an external scientific audit.

## References

1. A. Ayyer and M. Podder, *An exactly solvable evaporation-deposition PCA with long-distance interactions*, arXiv:2602.23837v1 (2026-02-27), https://arxiv.org/abs/2602.23837 . Source Theorem 3.3 and Sections 2–6.
2. M. Robert, *Decay of the direct correlation function in linear lattice systems*, Physical Review A **29**, 2854 (1984), https://doi.org/10.1103/PhysRevA.29.2854 . Different one-dimensional lattice-gas observable and model; contextual background.
3. H. Nishimura, M. C. Ogilvie and K. Pangeni, *Complex spectrum of finite-density lattice QCD with static quarks at strong coupling*, arXiv:1512.09131 (2015), https://arxiv.org/abs/1512.09131 . Different model illustrating complex spatial modes.
