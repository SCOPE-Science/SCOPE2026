# A sharp four-site weak-dephasing threshold with reentrant contact dependence

## Finding
For the boundary-driven tilted four-site \(XX\) chain defined below, the sign of the *initial* response of the stationary spin current to bulk dephasing has exactly one tilt threshold at each positive contact coupling. The threshold is strictly positive at every finite contact coupling, but tends to zero in both the weak-contact and strong-contact limits. This produces a reentrant contact-coupling dependence of the local benefit of dephasing. The claim concerns \(\partial_\gamma I(0^+)\), not a global classification of the current at arbitrary positive \(\gamma\).

Use units \(\hbar=1\). Define \(t=2J>0\), \(u=2|U|\ge0\), \(G=\Gamma>0\), and dimensionless parameters
\[
x=(G/t)^2>0,\qquad y=(u/t)^2\ge0.
\]
Define the polynomial
\[
\begin{aligned}
F(x,y)={}&-48x(x+4)^2\\
&+(x^4+32x^3-96x^2+1408x+8960)y\\
&+(50x^3+1008x^2+2464x+21888)y^2\\
&+(913x^2+8016x+37296)y^3\\
&+(7200x+13824)y^4+20736y^5.
\end{aligned}
\]
For every \(J,G>0\), real \(U\), and \(0<f\le1\), the stationary current \(I(\gamma)\) satisfies the **exact derivative identity**
\[
\left.\frac{dI}{d\gamma}\right|_{0^+}
=\frac{8fF(x,y)}{(x+4+16y)^2(4x+xy+16+12y+9y^2)^2}.
\]
Thus a unique \(y_c(x)>0\) solves \(F(x,y_c(x))=0\), and the derivative is negative for \(y<y_c(x)\), zero exactly at \(y_c(x)\), and positive for \(y>y_c(x)\). In terms of the positive frequency tilt \(u_c=t\sqrt{y_c((G/t)^2)}\),
\[
\lim_{G/t\to0}\frac{u_c}{G}=\sqrt{3/35},\qquad
\lim_{G/t\to\infty}\frac{u_c G}{t^2}=4\sqrt3.
\]
In particular \(u_c\) is continuous, strictly positive at every finite \(G>0\), and approaches zero at *both* ends of the contact-coupling range, so it has a positive interior maximum (uniqueness of the maximum is not claimed).

## Assumptions and scope
Let \(\sigma_j^a\) denote Pauli matrices at sites \(j=1,2,3,4\). Consider the time-independent Hamiltonian
\[
H=J\sum_{j=1}^{3}(\sigma_j^x\sigma_{j+1}^x+\sigma_j^y\sigma_{j+1}^y)
+U\sum_{j=1}^{4}(j-1)\sigma_j^z.
\]
The Markovian quantum dynamics is the standard Lindblad equation with end-site jumps
\[
L_{1,\pm}=\sqrt{G(1\pm f)/2}\,\sigma_1^\pm,\qquad
L_{4,\pm}=\sqrt{G(1\mp f)/2}\,\sigma_4^\pm,
\]
and site dephasing jumps \(L_{j,d}=\sqrt{\gamma/2}\,\sigma_j^z\) for \(j=1,2,3,4\). Here \(G,J>0\), \(0<f\le1\), \(\gamma\ge0\), and \(U\in\mathbb R\). We define the stationary spin current by
\[
I(\gamma)=2J\operatorname{Tr}\!\left[(\sigma_1^x\sigma_2^y-\sigma_1^y\sigma_2^x)\rho_\infty\right].
\]
All statements apply to these four sites and this reservoir/dephasing normalization. The current is positive in the stated orientation for positive bias. The tilt sign is immaterial by the exact \(U\mapsto-U\) symmetry.

## Proof
**1. Exact closed stationary equation.** Let \(h\) be the Hermitian one-particle matrix with \(h_{jj}=(j-1)u\) and \(h_{j,j+1}=h_{j+1,j}=t\), after choosing \(U\ge0\), without loss of generality for the current. Write \(E=\operatorname{diag}(1,0,0,1)\), \(B=\tfrac G2\operatorname{diag}(1,0,0,-1)\), and let \(\mathcal O(K)=K-\operatorname{diag}(K_{11},K_{22},K_{33},K_{44})\). The exact stationary fermionic two-point response is \(C=\tfrac12\mathbf 1+fK\), where \(K=K^\dagger\) solves
\[
-i[h,K]-\tfrac G2\{E,K\}-2\gamma\mathcal O(K)+B=0.
\tag{1}
\]
The Pauli–Jordan–Wigner identities yield \(I(\gamma)=4ft\operatorname{Im}K_{12}\). This is an exact closure for this noninteracting chain, not a tridiagonal truncation or a small-bias approximation.

**2. Existence and nondegeneracy.** Consider the homogeneous linear equation obtained from (1). Taking its Hilbert–Schmidt real inner product with \(K\) shows that the positive boundary-row damping vanishes, as must the off-diagonal dephasing contribution if \(\gamma>0\). For \(\gamma=0\), the vanishing boundary contribution already forces the first and last rows of \(K\) to vanish. The commutator equation then propagates a zero row inward along the nonzero nearest-neighbor hopping, giving \(K=0\). For \(\gamma>0\), zero off-diagonal entries and the commutator condition likewise force a constant diagonal, while boundary damping makes that constant zero. Thus the finite real linear system is invertible for all \(\gamma\ge0\), and the current is differentiable from the right at zero.

**3. Exact elimination and derivative.** Parameterize a Hermitian \(K\) by its four real diagonals and six complex upper-triangle entries. Equation (1) gives sixteen real equations, with coefficient matrix \(A(\gamma)\). At zero dephasing solve \(A(0)k_0=b\); then differentiate to obtain \(k'_0=-A(0)^{-1}A'(0)k_0\). Exact rational elimination yields
\[
I(0)=\frac{16fGt^4(G^2+4t^2+9u^2)}{
(G^2+4t^2+16u^2)
(4G^2t^2+G^2u^2+16t^4+12t^2u^2+9u^4)
},
\]
and the displayed derivative formula. The full sixteen-equation construction and exact symbolic equalities, together with a separate direct sixteen-dimensional full-spin Lindblad calculation, are reproducible in `VERIFY.py` (requirements in `requirements.txt`). The exact linear identities, not finite samples, establish the polynomial formula.

**4. A single sharp threshold.** For \(x>0\), the constant coefficient of \(F(x,y)\) as a polynomial in \(y\) is \(-48x(x+4)^2<0\). Its linear coefficient can be written
\[
x^4+32x(x^2-3x+44)+8960>0,
\]
since \(x^2-3x+44>0\) for all real \(x\). Every higher coefficient in \(y\) is also positive for \(x>0\). Therefore \(F(x,y)\) is strictly increasing on \(y\ge0\), starts negative and tends to positive infinity. There is exactly one positive root, and the asserted sign classification follows because the derivative denominator is positive.

**5. Contact endpoints.** At small \(x\), the equation \(F(x,y_c)=0\) forces \(y_c\to0\) and balancing its first nonzero terms gives \(8960y_c\sim768x\), hence \(y_c/x\to3/35\). At large \(x\), the equation similarly forces \(y_c\to0\). Dividing by \(x^3\), the only surviving leading terms at the root are \(-48+xy_c\), so \(xy_c\to48\). Both stated dimensional endpoint laws follow. The continuous positive threshold must attain an interior maximum because it vanishes at both endpoints.

## Verification
Reproducibility: install the versions in `requirements.txt` and execute `python VERIFY.py` in the directory containing this document. The script constructs all sixteen equations directly from (1), obtains the exact zero-dephasing current and derivative by symbolic inversion, checks both rational identities exactly, and independently constructs and solves the full \(16\times16\) spin-system Lindbladian for several dephasing values. Its passed finite tests verify normalization and guard against implementation errors; they are not substituted for the polynomial sign proof.

At \(G=t=1\), numerical roots give \(u_c\approx0.3032369902\). For \(G/t\approx4.8238\), numerical evaluation gives \(u_c/t\approx0.72607\); the theorem does **not** certify that this numerical point is the unique maximizer.

## Relationship to prior work
Jacob, Bettmann, Lacerda, Zawadzki, Clark, Goold and Mendoza-Arenas, arXiv:2407.21715 (first posted 2024-07-31), give the model, exact length-two and length-three currents, a general correlation-matrix formulation and a tridiagonal approximation for longer chains. Their full-text Section 5.1 identifies the short-chain optimal dephasing rates; Section 5.2 explicitly notes that the truncation fails for very small dephasing. The current result concerns the first nontrivial four-site case in which longer-range coherence matters, identifying the exact zero-dephasing onset boundary and its nonmonotone dependence on reservoir coupling. Their general linear system permits an implicit calculation but does not itself state this closed polynomial onset theorem or endpoint asymptotics.

Žnidarič and Horvat, arXiv:1207.5952 (first posted 2012-07-25), derive a general correlation-matrix transport formulation and analyze disordered-chain thermodynamic conductivity and periodic-disorder resonance. Those statements do not imply the specific finite, linearly tilted four-site sign classification. A prior fixed-dephasing clean-chain current bound \(I(U,\gamma)\le I(0,\gamma)\) compares tilts at the same dephasing rate; it does not compare dephasing rates at fixed nonzero tilt, and thus does not imply the new boundary. No theorem of general novelty is inferred from a search failure.

## Limitations
The result concerns an **infinitesimal right derivative** of stationary current at \(\gamma=0\), not the number or location of maxima of current for finite dephasing, nor detectability with noisy measurements. It is specific to a four-site chain with equal boundary couplings, a linear onsite potential and identical local pure dephasing. The polynomial was symbolically checked; an unindexed source offering a stronger exact finite-chain classification could affect publication originality. No independent scientific audit has been performed.

## References
- S. L. Jacob et al., *Dephasing-assisted transport in a tight-binding chain with a linear potential*, arXiv:2407.21715 (2024), https://arxiv.org/abs/2407.21715 and https://doi.org/10.3389/fphy.2024.1474018.
- M. Žnidarič and M. Horvat, *Transport in a disordered tight-binding chain with dephasing*, arXiv:1207.5952 (2012), https://arxiv.org/abs/1207.5952 and https://doi.org/10.1140/epjb/e2012-30730-9.
