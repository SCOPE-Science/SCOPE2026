# A minimal finite-switching Gibbs obstruction on the four-spin Ising cycle

## Finding

A ferromagnetic Ising ring can have an equilibrium-looking stationary spin marginal for every switching rate when it has three spins, but it **cannot** have a single-temperature Gibbs spin marginal at any *finite* positive switching rate when it has four spins. This contrast is exact for the global hot/cold temperature-switching dynamics below.

For the four-cycle let \(A,B,C,F\) denote the stationary **orbit masses**, summed over the bath state, of respectively (i) the two aligned configurations with energy \(-4\), (ii) the eight configurations with one exceptional spin and energy \(0\), (iii) the four adjacent-pair configurations with energy \(0\), and (iv) the two alternating configurations with energy \(+4\). Thus \(A+B+C+F=1\). For every cold inverse temperature \(\beta>0\) and symmetric bath switching rate \(\gamma>0\),
\[
 C=\frac B2,\qquad \boxed{\Delta=16AF-B^2>0.}
\]
Equivalently, the two adjacent-energy-gap estimators
\[
 \beta_{\rm low}=\frac14\log\frac{4A}{B},\qquad
 \beta_{\rm high}=\frac14\log\frac{B}{4F}
\]
obey \(\beta_{\rm low}>\beta_{\rm high}\) at every finite \(\gamma>0\). A canonical spin law would require their equality. With \(w=2\cosh(2\beta)>2\), the gap closes at a sharp rate,
\[
 \boxed{\beta_{\rm low}-\beta_{\rm high}
 =\frac{w-2}{2\gamma}+O(\gamma^{-2})\quad(\gamma\to\infty).}
\]
The four-cycle is minimal among simple nearest-neighbor cycles: on the triangle, symmetry forces a two-energy-level spin law, which is Gibbs at some positive effective inverse temperature for every finite switching rate.

## Assumptions and scope

Let \(n=3\) or \(n=4\) and take the simple undirected cycle \(C_n\), with one edge per adjacent vertex pair, coupling \(J=1\) and no external field. For a spin configuration \(\sigma\in\{-1,+1\}^n\), define \(H(\sigma)=-\sum_{i=1}^n\sigma_i\sigma_{i+1}\), indices modulo \(n\). A global bath variable takes values hot and cold and switches between them independently at exponential rate \(\gamma>0\). The hot bath has inverse temperature \(0\), and the cold bath has fixed inverse temperature \(\beta>0\). A spin flip with energy increment \(\Delta H\) has continuous-time rate \(\exp(-\beta_b\Delta H/2)\) in bath \(b\), with unit rate prefactor per spin. All probabilities are under the unique joint stationary law; only the bath-marginalized spin distribution is assessed for Gibbs form. An effective inverse temperature is required to be a *single* real number for all configurations; a fit to one scalar observable does not suffice.

## Proof

**1. Exact four-spin orbit dynamics.** Spin inversion and dihedral symmetries preserve the generator. In the orbit order \((A,B,C,F)\), the column generator of the spin process with \(t=e^{2\beta_b}\) is
\[
 M(t)=\begin{pmatrix}
 -4/t&t&0&0\\
 4/t&-t-2-1/t&4&4t\\
 0&2&-4&0\\
 0&1/t&0&-4t
 \end{pmatrix}.
\]
For instance, an aligned configuration has four energy-increasing flips at rate \(1/t\), and an alternating configuration has four energy-decreasing flips at rate \(t\). The other entries follow by counting spin flips of increments \(\pm4\) or \(0\). For the joint orbit probability column \(p\), the full generator is
\[
 Q=\begin{pmatrix}M(u)-\gamma I_4&\gamma I_4\\
 \gamma I_4&M(1)-\gamma I_4\end{pmatrix},\qquad u=e^{2\beta}>1.
\]
It is irreducible. The unique stationary \(p\) solves \(Qp=0\), \(\boldsymbol1^\top p=1\). Summing the two bath equations for the third orbit yields \(2B-4C=0\), so \(C=B/2\).

**2. Exact rational elimination and factorization.** Write \(w=u+u^{-1}=2\cosh(2\beta)\). Define strictly positive polynomials
\[
\begin{aligned}
D(\gamma,w)={}&(w+2)(w+6)\gamma^3+2(w+2)(7w+18)\gamma^2\\
 &+8(7w^2+14w+24)\gamma+64(w^2+4),\\
H(\gamma,w)={}&8\gamma^4(w+2)+\gamma^3(7w^2+108w+140)\\
 &+\gamma^2(78w^2+424w+504)\\
 &+\gamma(256w^2+512w+1024)+256(w^2+4).
\end{aligned}
\]
Solving the displayed normalized eight-dimensional linear system by rational elimination gives
\[
 B=\frac{4\gamma^3(w+2)+2\gamma^2(w^2+16w+28)
 +2\gamma(6w^2+28w+80)+16(w^2+12)}{D(\gamma,w)},
\]
and, with \(\mathcal E=\mathbb E[H]=-4A+4F\),
\[
 \mathcal E=-\frac{4(u-u^{-1})(\gamma+2)
 [ (w+2)\gamma^2+(9w+6)\gamma+16w]}{D(\gamma,w)}.
\]
Because \(A+F=1-3B/2\), one can reconstruct
\(A=[1-3B/2-\mathcal E/4]/2\) and
\(F=[1-3B/2+\mathcal E/4]/2\). Substitution and exact polynomial cancellation yield the factorization
\[
 \boxed{16AF-B^2=\frac{4(\gamma+2)(w^2-4)H(\gamma,w)}{D(\gamma,w)^2}.}
\]
Every factor on the right is strictly positive for \(\gamma>0\), \(w>2\). This is an algebraic identity, not a numerical inequality inferred from a finite scan. The complete symbolic reconstruction and a separate full-state generator comparison appear in `verify.py`.

**3. Gibbs incompatibility.** A Gibbs distribution at inverse temperature \(\theta\) has equal probabilities for all twelve zero-energy configurations and orbit masses proportional to \((2e^{4\theta},8,4,2e^{-4\theta})\). Such masses satisfy \(C=B/2\) and the necessary identity \(16AF=B^2\). The strict sign above forbids Gibbs form. Moreover,
\[
\beta_{\rm low}-\beta_{\rm high}=\frac14\log\frac{16AF}{B^2}>0.
\]
The numerator and denominator are positive by irreducibility, so both estimators are defined.

**4. Sharp rapid-switching limit.** From the preceding exact polynomials,
\[
 B=\frac4{w+6}+O(\gamma^{-1}),\quad
 \Delta=\frac{32(w^2-4)}{(w+2)(w+6)^2}\frac1\gamma
 +O(\gamma^{-2}).
\]
Consequently \(16AF/B^2=1+2(w-2)/\gamma+O(\gamma^{-2})\), establishing the displayed effective-temperature mismatch. The limiting marginal is Gibbs at inverse temperature \(\beta/2\), but it is never exactly so at finite positive \(\gamma\). The limits refer to fixed \(\beta>0\).

**5. Minimality.** On the triangle \(C_3\), all configurations have energy either \(-3\) (two aligned configurations) or \(+1\) (six configurations with one exceptional spin). Spin inversion and dihedral symmetry make the stationary probability uniform within each of these two energy levels; therefore their strictly positive per-state probability ratio defines one Gibbs inverse temperature \(\theta\). More specifically, write total aligned and exceptional masses as \(A_3,F_3\). In either bath the outgoing aligned-to-exceptional total rate is \(3e^{-2\beta_b}\), while the exceptional-to-aligned total rate is \(e^{2\beta_b}\). Summed stationary flux balance, using \(0\le\beta_b\le\beta\) and positivity of the conditional stationary masses, gives \(3A_3>F_3\), so \(\theta=(1/4)\log(3A_3/F_3)>0\). Thus the four-cycle is the first simple cycle with a persistent Gibbs obstruction.

## Verification

Execute `python verify.py` with SymPy. It reconstructs the normalized eight-state stationary probabilities symbolically, checks the orbit relation, the exact rational \(B\) and \(\mathcal E\), the positive defect factorization, and both rapid-switching limits. It independently builds the full 32-state spin-plus-bath generator directly from bit configurations and tests three exact rational choices of \(u=e^{2\beta}\) and \(\gamma\). All symbolic and exact rational checks pass. The polynomial positivity and triangle symmetry arguments are analytic proofs; finite matrix examples are corroboration only.

## Relationship to prior work

Dutta, Sarkar and Basu [1] introduce the global dichotomous-temperature Ising protocol, characterize large two-dimensional systems numerically, and identify effective-temperature behavior at rapid switching. The starting model and limiting Gibbs interpretation are theirs. A published exact four-cycle treatment [2] uses the same hot/cold exponential-rate protocol and supplies an exact stationary mean-energy law and a sharp threshold for **energy nonmonotonicity**. It includes the orbit generator used here. Neither [1] nor [2], in their inspected main results, supplies the all-finite-rate strict Gibbs obstruction, its positive closed-form level-curvature witness, the mismatch coefficient, or the minimal triangle-versus-four-cycle distinction. The energy formula here is not claimed as new. Earlier spatially alternating two-temperature Glauber chains [3] have a permanently assigned local bath, not a globally switching bath; their stationary correlation statements do not imply this result. Research on simulated tempering [4] explicitly engineers temperature-swap acceptance to preserve a chosen joint Gibbs family, unlike the independent constant-rate bath flips here.

## Limitations

The result holds for the *simple four-edge cycle*, not the doubled-edge periodic two-by-two square lattice. It requires exponential detailed-balance flip rates, exactly one infinite-temperature bath, the other at positive finite inverse temperature, and symmetric memoryless global bath switching. It does not classify arbitrary pairs of finite temperatures, other spin-update rules, larger graphs, or thermodynamic limits. The word *non-Gibbs* here means **not expressible as \(Z^{-1}e^{-\theta H}\) at any single scalar temperature for this finite Hamiltonian**, not the infinite-volume non-quasilocal Gibbs/non-Gibbs distinction. Although the physical setup and exact matrix are in prior literature, the specific positive inequality and minimality classification have not received independent publication-priority verification; unindexed equivalent results remain possible.

## References

[1] D. Dutta, R. Sarkar, U. Basu, *Stochastic Two-temperature Nonequilibrium Ising model*, arXiv:2509.00494, first public 30 August 2025; *New Journal of Physics* 28 (2026), 034602. https://arxiv.org/abs/2509.00494 ; https://doi.org/10.1088/1367-2630/ae4776

[2] *Sharp switching-rate reversal on a four-spin Ising plaquette*, publicly indexed 8 November 2026, especially its exact orbit generator and energy formula. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-switching-rate-reversal-on-a-four-spin-ising-plaquette--b8870460e67a

[3] B. Schmittmann and F. Schmüser, *Stationary correlations for a far-from-equilibrium spin chain*, *Physical Review E* 66 (2002), 046130. https://doi.org/10.1103/PhysRevE.66.046130

[4] F. Faizi, P. J. Buigues, G. Deligiannidis, and E. Rosta, *Simulated tempering with irreversible Gibbs sampling techniques*, *Journal of Chemical Physics* 153 (2020), 214111. https://doi.org/10.1063/5.0025775
