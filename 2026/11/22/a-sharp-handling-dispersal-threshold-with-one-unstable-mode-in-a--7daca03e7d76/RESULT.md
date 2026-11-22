# A sharp handling-dispersal threshold with one unstable mode in a behavioral predator–prey model

## Finding
Consider the isotropic reaction–cross-diffusion equations derived from active/refuge prey and searching/handling predator states in Bisi, Bondesan, Groppi and Soresina (2026). There is a strictly positive ecological parameter family in which **varying only the diffusivity of handling predators produces a sharp, complete spatial-instability transition**, with exactly one unstable Neumann harmonic and no instability of any higher harmonic. At an explicit parameter in the unstable regime, the two *effective diagonal diffusion coefficients coincide*, so testing only self-diffusivity contrasts would miss the instability.

More precisely, let \(w>0\) denote the handling-predator diffusivity. On the one-dimensional reflecting habitat \(0<z<2\pi\), set
\[
\begin{aligned}
 \partial_t x &= \partial_{zz}\Phi_1(x,y)+F(x,y),\\
 \partial_t y &= \partial_{zz}\Phi_2(x,y;w)+G(x,y),
\end{aligned}
\]
where
\[
\begin{aligned}
 F(x,y)&=x-\frac{49x^2(1+y^2)}{100(1+y)^2}-\frac{453xy}{200(1+x+y)},\\
 G(x,y)&=-\frac{3y}{100}+\frac{9xy}{100(1+x+y)},\\
 \Phi_1(x,y)&=\frac{199x+xy}{100(1+y)},\\
 \Phi_2(x,y;w)&=\frac{y(1+y)}{100(1+x+y)}+\frac{wxy}{1+x+y}.
\end{aligned}
\]
With homogeneous Neumann conditions on both population densities, the positive constant state \((x,y)=(1,1)\) exists for all \(w>0\). Define
\[
\boxed{w_* = \frac{15421}{10900}.}
\]
Its complete **linear mode** classification is:

1. For \(0<w<w_*\), every Neumann mode is strictly spectrally stable.
2. At \(w=w_*\), only the first nonconstant Neumann harmonic has a simple zero eigenvalue; its other eigenvalue and all remaining spatial-mode eigenvalues have strictly negative real part.
3. For \(w>w_*\), **exactly the first nonconstant harmonic** \(\cos(z/2)\) has one positive real eigenvalue. All other harmonics, including the spatially homogeneous mode, are strictly stable.

At \(w=893/200\), the linearized diffusion matrix has equal diagonal entries of \(1\), yet the first harmonic is unstable. Replacing the off-diagonal diffusion entries by zero while retaining both diagonal entries equal to \(1\) restores strict stability of every spatial mode.

## Assumptions and scope
The four behavioral-state movement coefficients are, respectively, \(d_P=199/100\), \(d_R=1/100\), \(d_S=1/100\) and \(d_H=w>0\). The hidden/active transition and search/handling closure parameters are \(\beta=\delta=1\). The active and hidden prey have the same intrinsic birth rate \(\alpha_P=\alpha_R=1\), both separately experience competition coefficient \(49/100\), and the predation, predator birth and predator death constants are \(453/200\), \(9/100\), and \(3/100\), respectively. All are positive.

For the isotropic fast-reaction limit, the state fractions are \(x/(1+y)\), \(xy/(1+y)\), \(y(1+y)/(1+x+y)\) and \(xy/(1+x+y)\). Their weighted movement fluxes give the displayed \(\Phi_1,\Phi_2\); the separate competition terms and the Beddington–DeAngelis encounter denominator give \(F,G\). Thus the equations are a strict positive-parameter specialization of the model in the cited 2026 preprint, with the added choice of a bounded reflecting interval. The theorem is **linear** about this specified coexistence state. No nonlinear spatially patterned equilibrium or long-time dynamics are asserted.

## Proof
Direct substitution gives \(F(1,1)=G(1,1)=0\). Exact differentiation of the reaction terms at this state yields
\[
J=\begin{pmatrix}\frac1{150}&-\frac{151}{300}\\[2pt]\frac1{50}&-\frac1{100}\end{pmatrix},\qquad
\operatorname{tr}J=-\frac1{300},\quad\det J=\frac1{100}.
\]
Differentiating the nonlinear flux potentials yields the matrix of effective local diffusivities
\[
D(w)=\begin{pmatrix}
1&-\frac{99}{200}\\[2pt]
\frac{2w}{9}-\frac1{450}&\frac{2w}{9}+\frac7{900}
\end{pmatrix}.
\]
Its trace and determinant are
\[
\operatorname{tr}D(w)=\frac{200w+907}{900}>0,\qquad
\det D(w)=\frac{29900w+601}{90000}>0.
\]
Consequently the linearization is normally elliptic at the equilibrium for every \(w>0\).

For homogeneous Neumann conditions on \((0,2\pi)\), the spatial eigenfunctions are \(\cos(nz/2)\), with squared wavenumbers \(q_n=n^2/4\), for integers \(n\geq0\). On the corresponding harmonic the linearized matrix is \(J-q_nD(w)\), whose trace is
\[
\operatorname{tr}(J-qD(w))=-\frac{200qw+907q+3}{900}<0\quad(q\geq0).
\]
Its determinant is the explicit quadratic
\[
P_w(q)=\det(J-qD(w))=
\frac{(29900w+601)q^2+(105-10200w)q+900}{90000}.
\]
At \(n=0\), \(P_w(0)=1/100>0\). At \(n=1\),
\[
P_w(1/4)=\frac{15421-10900w}{1440000},
\]
which changes sign exactly at the stated \(w_*\). For all other spatial modes \(n\ge2\), one has \(q_n\ge1\). At the left endpoint,
\[
P_w(1)=\frac{9850w+803}{45000}>0.
\]
Furthermore, for every \(q\ge1\),
\[
90000\,P'_w(q)=2(29900w+601)q+105-10200w
\ge49600w+1307>0.
\]
Thus \(P_w(q_n)>0\) for **every** \(n\ge2\), with no truncation of the infinite mode set. For a real two-by-two matrix, strictly negative trace and positive determinant give two eigenvalues with negative real part; negative determinant gives opposite-sign real eigenvalues; zero determinant and negative trace give one simple zero and one negative eigenvalue. These three cases prove the full classification.

Finally, setting \(w=893/200\) makes
\[
D=\begin{pmatrix}1&-\frac{99}{200}\\[2pt]\frac{99}{100}&1\end{pmatrix},
\quad \det D=\frac{29801}{20000}>0,
\quad P_w(1/4)=-\frac{4433}{192000}<0.
\]
If the cross terms are removed, \(D\) becomes the identity matrix, while the reaction matrix \(J\) stays fixed. Then
\[
\operatorname{tr}(J-qI)=-\frac1{300}-2q<0,
\qquad \det(J-qI)=q^2+\frac q{300}+\frac1{100}>0
\]
for every \(q\ge0\). Hence the first-harmonic instability is caused by the off-diagonal flux couplings, not by unequal effective diagonal diffusivities.

## Verification
The included `verify.py` uses standard-library rational arithmetic and two-variable first-order dual numbers. It recomputes the nonlinear equilibrium, all four entries of both linearization matrices, the complete determinant polynomial, the critical threshold, the monotonicity certificate controlling every higher spatial mode, and the equal-diagonal comparison. It has no floating-point dependency and requires only Python 3. Run `python3 verify.py`; the script raises an assertion on any failed identity and prints `PASS` when all checks succeed. The finite sample comparisons in the code are supplemental; the derivative inequality above, not sampled modes, proves the infinite statement.

## Relationship to prior work
Bisi, Bondesan, Groppi and Soresina (arXiv:2611.14132v1, 10 November 2026) derive the prey-refuge/search-handling cross-diffusion model and its separate-state competition term; their concluding discussion explicitly identifies stability and spatial-pattern onset for the resulting macroscopic model as open for analysis. The displayed model here is their isotropic limiting system with strictly positive rational parameters; the exact full mobility phase transition is an additional mathematical conclusion.

Cross-diffusion-driven Turing instability as a general mechanism is **not new**. Desvillettes and Soresina (2019) derive a related four-state non-triangular cross-diffusion predator–prey system and study Turing phenomena versus standard diffusion, but the 2026 model distinguishes its separately competing active and hidden prey demographics from those earlier reactions. Conforto, Desvillettes and Soresina (2018) study a three-state predator model with unstructured prey. Brocchieri and Soresina (2026) give structural Turing criteria for generalized competitive SKT-type models; their two-species competitive reaction Jacobian does not immediately imply the present predator–prey parametric formula. Miao (2018) studies a distinct three-species generalist-predator system. Thus the contribution claimed here is **this exact sharp, one-mode threshold in the newly specified behavioral predator–prey reaction system**, including the equal-effective-diagonal instability; no generic discovery of cross-diffusion instabilities is claimed. Full-text access to the 2019 non-triangular study was unavailable, so an unrecognized exact specialization remains a priority risk.

## Limitations
The theorem concerns the linearization at one rational, constant coexistence state on a particular reflecting interval. It does not establish nonlinear patterned equilibria, nonlinear stability, the eventual fate of perturbations, applicability to all habitat sizes, or validity of the formal kinetic limit. The numerical constants are an exact constructed witness, not ecological measurements. A different interval length changes the list of admissible Laplacian wavenumbers and thus may change the threshold and modal multiplicity. The older 2019 model-specific full text was not accessible; general theoretical overlap is acknowledged, so independent literature/priority review remains appropriate.

## References
1. M. Bisi, A. Bondesan, M. Groppi, C. Soresina, *Mesoscopic derivation of predator–prey dynamics via diffusive fast-reaction asymptotics: cross-diffusion and fear effects*, arXiv:2611.14132v1, first public 10 November 2026. https://arxiv.org/html/2611.14132v1
2. L. Desvillettes, C. Soresina, *Non-triangular cross-diffusion systems with predator–prey reaction terms*, Ricerche di Matematica 68 (2019), 295–314. DOI:10.1007/s11587-018-0403-y
3. F. Conforto, L. Desvillettes, C. Soresina, *About reaction-diffusion systems involving the Holling-type II and Beddington–DeAngelis functional responses for predator-prey models*, Nonlinear Differential Equations and Applications 25 (2018), 24. arXiv:1712.10159. https://arxiv.org/abs/1712.10159
4. E. Brocchieri, C. Soresina, *Cross-diffusion and fast-reaction in pattern formation: a structural analysis*, arXiv:2603.22177v1, 23 March 2026. https://arxiv.org/html/2603.22177v1
5. B. Miao, *Persistence and Turing instability in a cross-diffusive predator–prey system with generalist predator*, Advances in Difference Equations (2018), 260. https://doi.org/10.1186/s13662-018-1676-x
