# Sharp switching-rate reversal on a four-spin Ising plaquette

## Finding

A ferromagnetic Ising system on the simple four-cycle has a sharp, exactly computable temperature threshold for nonmonotonic stationary energy under randomly switching reservoirs. One reservoir is at infinite temperature; the other has fixed finite inverse temperature \(\beta>0\). Every site flips at rate \(\exp[-\beta_b\Delta H/2]\) when the active bath has inverse temperature \(\beta_b\); the common bath changes at rate \(\gamma>0\).

Put \(w=2\cosh(2\beta)>2\), \(s=2\sinh(2\beta)=\sqrt{w^2-4}\), and
\[
\begin{aligned}
 B(\gamma,w)&=(w+2)\gamma^2+(9w+6)\gamma+16w,\\
 D(\gamma,w)&=(w+2)(w+6)\gamma^3+2(w+2)(7w+18)\gamma^2\\
 &\quad+8(7w^2+14w+24)\gamma+64(w^2+4).
\end{aligned}
\]
The **exact stationary mean total energy** is
\[
\boxed{\mathcal E(\gamma,w)=-\frac{4s(\gamma+2)B(\gamma,w)}{D(\gamma,w)}.}
\]
For every \(2<w<6\), the function \(\gamma\mapsto\mathcal E(\gamma,w)\) increases strictly up to one **global maximum** \(\gamma_*(w)>0\) and decreases strictly afterwards. The maximizer is the unique positive root of
\[
\begin{aligned}
 P(\gamma,w)&=3(w^2-4)\gamma^4+4(11w^2-8w-60)\gamma^3\\
 &\quad+4(59w^2-116w-324)\gamma^2\\
 &\quad+256(2w^2-7w-10)\gamma+128(3w^2-16w-12).
\end{aligned}
\]
For \(w\ge6\), the energy is strictly decreasing for all \(\gamma>0\). Thus the threshold in the cold inverse temperature is
\[
\boxed{\beta_{\mathrm c}=\tfrac12\operatorname{arcosh}(3)
=\tfrac12\log(3+2\sqrt2).}
\]
A nonmonotone rate dependence occurs **if and only if** \(0<\beta<\beta_{\mathrm c}\). Near the threshold and in the weak-cold-bath regime, respectively,
\[
\gamma_*(w)=\frac{6-w}{2}+O((6-w)^2)\quad(w\uparrow6),
\qquad \gamma_*(w)\sim\frac{32}{3(w-2)}\quad(w\downarrow2).
\]
The second relation is also \(\gamma_*(\beta)\sim 8/(3\beta^2)\) as \(\beta\downarrow0\).

## Assumptions and scope

The graph is the four-vertex cycle \(C_4\), with four **single** nearest-neighbor bonds, not the multigraph obtained from a doubly wrapped two-by-two periodic square lattice. Spins \(\sigma_i\in\{-1,1\}\), \(i=1,2,3,4\), have Hamiltonian
\[
H(\sigma)=-\sum_{i=1}^4\sigma_i\sigma_{i+1},\qquad \sigma_5=\sigma_1.
\]
The hot reservoir has inverse temperature zero and the cold reservoir has inverse temperature \(\beta\in(0,\infty)\). The reservoir state changes from hot to cold, or conversely, at symmetric exponential rate \(\gamma\in(0,\infty)\), independently of the spins. Given bath \(b\), site \(i\) independently attempts a flip with continuous-time rate \(\exp(-\beta_b\Delta_i H/2)\); the rate prefactor is normalized to one. All expectations refer to the unique stationary law of the resulting 32-state irreducible continuous-time Markov chain. Physical rates are obtained by dividing both the bath switching rate and time by the site-flip prefactor when that prefactor is not unity. Temperature and energy are measured in units with \(J=k_B=1\).

## Proof

**Orbit reduction.** Rotation, reflection and simultaneous reversal of all four spins commute with both fixed-bath generators and with the bath-switching operator. There are exactly four spin orbits: uniform configurations (two states, energy \(-4\)), one minority spin (eight states, energy zero), two adjacent up and two adjacent down (four states, energy zero), and alternating configurations (two states, energy \(+4\)). In that orbit order, the generator acting on a **column** of orbit probabilities is
\[
M(t)=\begin{pmatrix}
-4/t&t&0&0\\ 4/t&-t-2-1/t&4&4t\\
0&2&-4&0\\0&1/t&0&-4t
\end{pmatrix},\qquad t=e^{2\beta_b}.
\]
For example, the uniform orbit has four possible outward flips, each at rate \(1/t\), whereas each alternating state has four outward flips at rate \(t\). The two zero-energy orbits have their incident flip counts shown by the remaining entries. Every column sums to zero. The eight-orbit joint generator is
\[
Q=\begin{pmatrix}M(u)-\gamma I_4&\gamma I_4\\
\gamma I_4&M(1)-\gamma I_4\end{pmatrix},\qquad u=e^{2\beta}>1.
\]
This finite Markov chain is irreducible, hence possesses one strictly positive stationary vector \(p\). Replacing one row of \(Q\) by the all-ones normalization and solving \(Qp=0\), \(\boldsymbol 1^\top p=1\), yields the displayed rational expression for \(\mathcal E=-4(p_1+p_5)+4(p_4+p_8)\), after using \(u+u^{-1}=w\) and \(u-u^{-1}=s\). The displayed matrices allow direct reproduction of this elimination.

**Exact derivative and signs.** Direct polynomial differentiation of the rational expression and cancellation gives
\[
\frac{\partial\mathcal E}{\partial\gamma}
=-\frac{4(w-2)\sqrt{w^2-4}}{D(\gamma,w)^2}\,P(\gamma,w).
\]
Every coefficient of \(D\) is positive on \(w>2\), \(\gamma\ge0\). From highest to lowest powers of \(\gamma\), the coefficient-sign change locations of \(P\) for \(w>2\) occur successively at
\[
2,\quad\frac{30}{11},\quad\frac{58+4\sqrt{1405}}{59},
\quad\frac{7+\sqrt{129}}{4},\quad6.
\]
These five numbers are strictly increasing. Consequently, for every \(2<w<6\), the descending list of nonzero coefficients of \(P\) has exactly one sign change, its leading coefficient is positive, and its constant coefficient is negative. Descartes' rule of signs, combined with the intermediate value theorem, proves that \(P\) has precisely one positive real root, necessarily simple. Hence \(P<0\) before this root and \(P>0\) after it; the derivative formula proves the claimed increase and decrease. If \(w\ge6\), all nonconstant coefficients of \(P\) are strictly positive and the constant coefficient is nonnegative, so the derivative is strictly negative for every \(\gamma>0\). This includes the equality threshold \(w=6\), where the root lies only at the excluded endpoint \(\gamma=0\).

**Threshold and boundary laws.** Because \(w=2\cosh(2\beta)\) increases strictly from \(2\), the equation \(w=6\) gives \(\beta_{\mathrm c}=\tfrac12\operatorname{arcosh}(3)\). At \((\gamma,w)=(0,6)\), the polynomial has derivatives \(P_\gamma=5120\) and \(P_w=2560\), so the implicit-function theorem gives \(\gamma_*=(6-w)/2+O((6-w)^2)\). At \(w=2+\varepsilon\), rescale \(\gamma=z/\varepsilon\) in \(P\); its highest two powers give \(12z^4-128z^3\), with unique positive nonzero balance \(z=32/3\). The exactly-one-root result and coefficient bounds justify convergence to that balance. Since \(w-2=4\beta^2+O(\beta^4)\), the weak-cold-bath law follows.

## Verification

The companion `verify.py` uses only the Python standard library. It computes exact rational stationary energies both from the eight-state symmetry-reduced generator and independently from the complete 32-state spin-plus-bath generator. It also checks the rational derivative identity at multiple parameter values and the threshold signs. Run `python verify.py`; its expected report is `PASS: 34 exact rational assertions; quotient/full generators and derivative`. Separately, symbolic polynomial differentiation of the rational energy and coefficient factorization establish the displayed exact derivative; no finite test is used as proof of the all-parameter theorem.

The zero-switching and rapid-switching limits provide additional analytic consistency tests:
\[
\lim_{\gamma\downarrow0}\mathcal E=-\frac{2sw}{w^2+4},\qquad
\lim_{\gamma\to\infty}\mathcal E=-\frac{4s}{w+6}.
\]
The former equals the mean of the hot- and cold-equilibrium Ising energies; the latter equals equilibrium at effective inverse temperature \(\beta/2\), as expected from the averaging of site-flip rates for this cycle.

## Relationship to prior work

Dutta, Sarkar and Basu introduce stochastic two-temperature Ising dynamics with the exponential detailed-balance flip rate and demonstrate nonmonotone magnetization and energy in larger two-dimensional lattices, with limiting-rate analyses and finite-size simulations [1]. Their preprint was first public on 30 August 2025. The present result uses the same exponential-rate mechanism but an extreme hot bath and one elementary four-cycle; it proves a complete exact switching-rate classification, a sharp inverse-temperature criterion, and optimizer boundary laws. Neither the rate mechanism nor qualitative nonmonotonicity is claimed to be new.

Schmittmann and Schmüser analyze an Ising chain with **spatially alternating, permanently assigned** sublattice bath temperatures [2]. That generator differs from the single globally switching bath here. Tamayo, Alexander and Gupta study competing two-temperature update dynamics and critical universality in larger Ising systems [3], rather than the telegraph switching of a single global bath. Those results do not state the four-cycle stationary energy or the threshold polynomial above.

## Limitations

This is an exact finite-system theorem for the single four-edge cycle, not a thermodynamic-limit phase transition or a theorem for a periodic two-dimensional lattice. The rates are exponential detailed-balance flips, not the logistic Glauber rate; the two update conventions must not be interchanged. The hot reservoir is exactly at infinite temperature, the other has arbitrary fixed finite positive inverse temperature, and switching rates are symmetric. A unique energy maximum does not assert a maximum of magnetization, heat current, or entropy production. The novelty assessment is limited by unindexed or inaccessible earlier formulas for related finite telegraph-driven spin chains.

## References

[1] D. Dutta, R. Sarkar, and U. Basu, *Stochastic Two-temperature Nonequilibrium Ising model*, arXiv:2509.00494 (first submitted 30 August 2025), *New Journal of Physics* 28 (2026), 034602, DOI: 10.1088/1367-2630/ae4776. https://arxiv.org/html/2509.00494v2

[2] B. Schmittmann and F. Schmüser, *Stationary correlations for a far-from-equilibrium spin chain*, *Physical Review E* 66 (2002), 046130, DOI: 10.1103/PhysRevE.66.046130. https://pubmed.ncbi.nlm.nih.gov/12443282/

[3] P. Tamayo, F. J. Alexander and R. Gupta, *Two-temperature nonequilibrium Ising models: Critical behavior and universality*, *Physical Review E* 50 (1994), 3474, DOI: 10.1103/PhysRevE.50.3474. https://journals.aps.org/pre/abstract/10.1103/PhysRevE.50.3474
