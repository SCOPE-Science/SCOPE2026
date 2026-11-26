# Exact fastest mixing and twist-parity comparison on Möbius ladders

## Finding
For every integer \(m\ge4\), let \(M_{2m}\) have vertices \(\mathbb Z/(2m)\) and undirected edges between \(x\) and \(x\pm1\), and between \(x\) and \(x+m\). Consider **every** real symmetric, entrywise nonnegative, row-stochastic matrix \(P\) supported on the loops and edges of this graph. Let \(\mu(P)=\max\{|\lambda|:\lambda\text{ is an eigenvalue of }P\text{ on }\mathbf1^\perp\}\), the second-largest eigenvalue modulus.

Set \(\theta=\pi/m\), \(E=2-2\cos(2\theta)\), \(U=2-2\cos\theta\), and
\[
V=\begin{cases}4,&m\text{ odd},\\2+2\cos\theta,&m\text{ even},\end{cases}
\qquad D=V+2E-U.
\]
The exact global optimum is
\[
\boxed{\mu_*(M_{2m})=\frac{V-U}{D}.}
\]
It is attained by the circulant transition matrix assigning \(a_*=2/D\) to each of the two cycle neighbors, \(b_*=(E-U)/D\) to the antipodal neighbor, and \(h_*=(V+E-4)/D\) to holding. All these masses are strictly positive. This is the **unique rotation-invariant** optimum. Unrestricted optimizer uniqueness is **not** claimed.

Let \(\mu_*(\mathrm{Pr}_m)\) denote the analogous global SLEM optimum on the Cartesian prism \(\mathrm{Pr}_m=C_m\square K_2\), with \(2m\) vertices. Then
\[
\boxed{\mu_*(M_{2m})=\mu_*(\mathrm{Pr}_m)\quad(m\text{ odd}),\qquad
\mu_*(M_{2m})<\mu_*(\mathrm{Pr}_m)\quad(m\text{ even}).}
\]
For odd \(m\), the two optimal rotation-invariant walks have the **same cycle-edge probability**, and the Möbius optimum interchanges the prism's antipodal-rung probability with its holding probability. For even \(m\), writing \(c=\cos(\pi/m)\), the exact advantage is
\[
\boxed{\mu_*(\mathrm{Pr}_m)-\mu_*(M_{2m})
=\frac{2E(1-c)}{(2+E)(2c+E)}>0,\qquad
\lim_{\substack{m\to\infty\\2\mid m}}m^4\bigl(\mu_*(\mathrm{Pr}_m)-\mu_*(M_{2m})\bigr)=\pi^4.}
\]
Further,
\[
\frac{h_*}{b_*}=\begin{cases}2(1+\cos\theta)/(1+2\cos\theta),&m\text{ odd},\\1,&m\text{ even},\end{cases}
\]
and
\[
\lim_{m\to\infty}m^2b_*=\frac{3\pi^2}{4},\qquad
\lim_{\substack{m\to\infty\\m\text{ odd}}}m^2h_*=\pi^2,\qquad
\lim_{\substack{m\to\infty\\m\text{ even}}}m^2h_*=\frac{3\pi^2}{4},\qquad
\lim_{m\to\infty}m^2(1-\mu_*)=2\pi^2.
\]
The optimal spectral gap is asymptotically four times the optimal spectral gap on the plain cycle \(C_{2m}\), even though each antipodal transition probability vanishes quadratically.

## Assumptions and scope
All probability matrices are symmetric, not necessarily cyclically or dihedrally invariant. Each vertex has two distinct cycle neighbors and one distinct antipodal neighbor because \(m\ge4\). Every permitted edge probability is independently variable, and loops (holding) are allowed. The stationary distribution is uniform. Spectral mixing refers to the SLEM objective; no assertion is made about exact total-variation mixing times or about nonreversible chains.

## Proof
**1. Symmetry reduction without restricting the problem.** For any feasible \(P\), average the \(2m\) matrices \(R^jPR^{-j}\) over powers of the graph rotation \(R:x\mapsto x+1\). The average remains feasible and circulant. Since \(P\mapsto\|P-(2m)^{-1}\mathbf1\mathbf1^{\mathsf T}\|_2\) is convex and unchanged under rotations, averaging does not increase SLEM. Thus a global optimum exists with cycle-edge probability \(a\ge0\), antipodal probability \(b\ge0\), and holding probability \(h=1-2a-b\ge0\). This does *not* imply uniqueness among unrestricted optimizers.

**2. Fourier reduction.** At frequency \(j\in\{0,\ldots,2m-1\}\), Fourier diagonalization gives
\[
\lambda_j=1-a\bigl(2-2\cos(\pi j/m)\bigr)-2b\,[j\text{ odd}].
\]
The constant mode is \(\lambda_0=1\). For even nonzero \(j\), the factor \(\delta_j=2-2\cos(\pi j/m)\) ranges from \(E\) to \(F\), where \(F=4\) for even \(m\), and \(F=2+2\cos(\pi/m)\) for odd \(m\). For odd \(j\), it ranges from \(U\) to \(V\) as defined above. It follows that the SLEM is the maximum of the absolute values of the four endpoint multipliers \(1-aE\), \(1-aF\), \(1-aU-2b\), and \(1-aV-2b\).

**3. Sharp three-mode lower certificate.** For any feasible \((a,b)\), set \(\rho\) to be its SLEM. Three of the Fourier constraints are
\[
\rho\ge u:=1-Ea,\qquad \rho\ge v:=1-Ua-2b,\qquad
\rho\ge w:=-1+Va+2b.
\]
Put \(\alpha=(V-U)/E>0\). Exactly, \(\alpha u+v+w=\alpha\) for every \(a,b\). Since the three weights \(\alpha,1,1\) are positive,
\[
\rho\ge\frac{\alpha u+v+w}{\alpha+2}=
\frac{V-U}{V+2E-U}=:\rho_*.
\]
Equality forces \(u=v=w=\rho_*\); solving these three affine equalities gives the unique invariant candidate \(a=2/D\) and \(b=(E-U)/D\).

**4. Feasibility and all omitted frequencies.** The explicit \(a,b\) are positive since \(E>U>0\). The holding mass is \(h=(V+E-4)/D\): if \(m\) is odd, \(V=4\) and \(h=E/D>0\); if \(m\) is even, \(V+E-4=E-U>0\), so \(h=b>0\). For every odd frequency, monotonicity in \(\delta_j\in[U,V]\) places \(\lambda_j\) between \(+\rho_*\) and \(-\rho_*\). For every nonzero even frequency, \(\lambda_j\le1-aE=\rho_*\); the required lower bound \(1-aF\ge-\rho_*\) is equivalent to \(F\le V+E-U\). If \(m\) is odd, the right-minus-left difference is \(E>0\). If \(m\) is even, it equals \(4\cos\theta(1-\cos\theta)>0\). Hence all Fourier constraints hold and the sharp bound is attained. Equality in the positive three-mode combination proves unique \((a,b)\) among rotation-invariant kernels. Symmetry reduction proves unrestricted global optimality.

**5. Rigorous prism comparison.** Write \(\Delta=2-2\cos(2\pi\lfloor m/2\rfloor/m)\). On \(C_m\square K_2\), Fourier modes along the cycle and symmetric/antisymmetric layer modes give \(1-a\delta_j\) and \(1-a\delta_j-2b\). Their three constraints at \((\delta_j,\text{layer})=(E,0),(0,1),(\Delta,1)\), with the same positive-weight certificate as above, give the globally optimal \(a_{\mathrm{Pr}}=2/(\Delta+2E)\), \(b_{\mathrm{Pr}}=E/(\Delta+2E)\), and \(\mu_*(\mathrm{Pr}_m)=\Delta/(\Delta+2E)\). The remaining frequency and holding constraints hold because \(\Delta+E\ge4\) for all \(m\ge4\). The global reduction again follows by graph symmetry averaging. When \(m\) is odd, \(\Delta=4-U=V-U\), so the two optimal values and cycle probabilities coincide and \((b_*,h_*)=(h_{\mathrm{Pr}},b_{\mathrm{Pr}})\). When \(m\) is even, \(\Delta=4\) while \(V-U=4\cos\theta\); direct subtraction yields the strictly positive difference displayed above.

**6. Asymptotics and cycle comparison.** Taylor expansion at \(\theta=\pi/m\to0\) yields \(E=4\theta^2+O(\theta^4)\), \(U=\theta^2+O(\theta^4)\), and \(V=4-\theta^2+O(\theta^4)\) for even \(m\), while \(V=4\) for odd \(m\). Substituting proves the mass and gap limits above, and the exact even-parity difference gives the \(\pi^4\) coefficient. For an ordinary even cycle \(C_{2m}\), the sharp SLEM is \((4-U)/(4+U)\), so the optimal cycle gap is \(2U/(4+U)\sim\pi^2/(2m^2)\), compared with \(2\pi^2/m^2\) here.

## Verification
Run `python verify_mobius.py` with the versions of NumPy and SciPy specified in `requirements.txt`. The reproducibility script independently solves all-frequency linear programs, compares their optima against the closed formula, constructs full stochastic matrices and compares dense real eigensystems with Fourier modes, checks all relevant spectral inequalities, reproduces both parity identities and the prism comparison, and checks finite approximations to the stated asymptotic limits. The recorded run completed `VERIFY_OK 20439 assertions`. The proof of the statements for all \(m\ge4\) is analytical, not an inference from those finite tests.

## Relationship to prior work
Boyd, Diaconis and Xiao introduced the fastest-mixing Markov-chain semidefinite formulation. Boyd, Diaconis, Parrilo and Xiao proved automorphism averaging and supplied exact cycle and wheel examples and general block-reduction tools. Their published analysis provides the method used here but does not explicitly give the Möbius-ladder optimum or the twist-parity law. A previously recorded exact prism optimum (finding ID `54a019de-aeec-4942-bf4e-79ce2da310d3`) is acknowledged; the prism formulas are also proved afresh above for comparison, and the Möbius graphs are not the Cartesian prisms. Research on weighted Möbius-ladder Ising couplings supplies a Fourier spectral description but concerns Ising-energy optimization, not stochastic SLEM minimization. A separate Möbius-ladder spanning-tree optimality formula concerns determinant design rather than fastest mixing.

## Limitations
Only symmetric stochastic chains with possible holding are considered. The rotation-invariant optimizer is unique, but unrestricted optimizer uniqueness and optimal exact finite-time mixing are not established. The fourfold gain is a comparison of *optimal spectral gaps*, not a uniform statement about all finite-time mixing metrics. The searched literature did not identify a dominating Möbius-ladder FMMC formula, but unindexed equivalent formulations remain possible; this absence is not a proof of novelty.

## References
1. S. Boyd, P. Diaconis and L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/fmmc.html
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” arXiv:0709.0955, first publicly posted 2007-09-06; *SIAM Journal on Optimization* 20 (2009), 792–819. https://arxiv.org/abs/0709.0955
3. “Efficient computation using spatial-photonic Ising machines with low-rank and circulant matrix constraints,” *Communications Physics* (2025), DOI:10.1038/s42005-025-01987-5, Möbius-ladder Fourier spectrum section. https://www.nature.com/articles/s42005-025-01987-5
4. “Exact fastest mixing on prism graphs with vanishing optimal rung weights,” comparative mathematical result, opaque finding ID `54a019de-aeec-4942-bf4e-79ce2da310d3`.
