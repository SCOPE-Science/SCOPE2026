# Sharp two–three–four absorber transitions in tunable circular quantum ladders

## Finding
For an \(n\)-rung circular ladder with independently tunable uniform ring and rung hopping, the minimum number of absorbing vertices needed to eliminate *every* coherent nondecaying state is exactly two, three, or four. The precise transitions are finite, explicit, frequency-difference resonances; a four-site resonance occurs at a dense set of coupling ratios when the ladder size varies.

Write \(\kappa=K/J>0\), \(c_j=\cos(2\pi j/n)\), with \(0\le j\le M=\lfloor n/2\rfloor\), and define the angular multiplicity
\[
m_j=\begin{cases}1,&j=0\text{ or }(2\mid n\text{ and }j=M),\\2,&\text{otherwise}.\end{cases}
\]
Define the finite resonance sets
\[
\mathcal R_q(n)=\left\{c_j-c_\ell:0\le j<\ell\le M,\ m_j+m_\ell\ge q\right\}\quad(q=3,4).
\]
Then the exact minimum number of absorbers for complete eventual capture of all states is
\[
\mu(n,\kappa)=\begin{cases}4,&\kappa\in\mathcal R_4(n),\\3,&\kappa\in\mathcal R_3(n)\setminus\mathcal R_4(n),\\2,&\text{otherwise}.\end{cases}
\]
The corresponding optimal absorber supports are, respectively, \(\{(0,0),(1,0),(0,1),(1,1)\}\), \(\{(0,0),(1,0),(0,1)\}\), and \(\{(0,0),(1,0)\}\), with the sites indexed by angular coordinate and layer. These supports are universal within their respective parameter class. The result holds for any strictly positive losses on the chosen sites.

Every \(\kappa>2\) requires just two absorbers. At \(n=5\), the ratio \(\kappa=\sqrt5/2\) forces four; at \(n=6\), the ratios \(\kappa=1/2,1,2\) require three, four, and two respectively. For each fixed \(n\), the set of exceptional ratios is finite, but \(\bigcup_{n\ge5}\mathcal R_4(n)\) is dense in \((0,2)\).

There is also an exact count of optimal two-site layouts at nonresonant ratios. Put \(g=\gcd(n,2)\). When \(\kappa\notin\{c_j-c_\ell:j<\ell\}\), the optimal pairs are precisely those with distinct angular coordinates separated by \(d\) satisfying \(\gcd(n/g,d)=1\). Their number is
\[
N_2(n)=2ng\,\varphi(n/g),
\]
where the layer of each absorber is unrestricted and \(\varphi\) is Euler's totient function.

## Assumptions and scope
Fix an integer \(n\ge3\) and \(J,K>0\). The Hilbert space is \(\mathbb C^n\otimes\mathbb C^2\). The coherent Hamiltonian is \(H_0=J A(C_n)\otimes I_2+K I_n\otimes X\), where \(A(C_n)\) is the simple-cycle adjacency matrix and \(X=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). At a nonempty absorbing set \(T\subseteq\mathbb Z/n\mathbb Z\times\{0,1\}\), let \(\Gamma_T=\sum_{v\in T}\gamma_v|v\rangle\langle v|\) with all \(\gamma_v>0\), and \(H=H_0-i\Gamma_T\). The eventual capture probability for a density matrix \(\rho\) is \(1-\lim_{t\to\infty}\operatorname{tr}(e^{-itH}\rho e^{itH^\dagger})\). Complete capture means this probability is one for *every* initial density matrix.

The ratio \(\kappa\) is fixed while initial states and absorber rates are arbitrary. No claim is made about finite-time capture speed, coupled dissipation, disorder, or nonlinear dynamics.

## Proof
**1. Characterization of dark modes.** For any eigenpair \(H\psi=z\psi\), taking the imaginary part of the inner product gives \(\operatorname{Im}z\,\|\psi\|^2=-\langle\psi,\Gamma_T\psi\rangle\le0\). Equality forces \(\psi|_T=0\) and \(H_0\psi=z\psi\), and the converse holds. Every such real-energy dark eigenvector is also an eigenvector of \(H^\dagger\), so their span reduces \(H\). On the orthogonal complement, every eigenvalue has strictly negative imaginary part. Jordan blocks there are harmless because exponential-polynomial terms decay; a Jordan block at a real eigenvalue is impossible for the contraction semigroup \(e^{-itH}\). Thus every initial state is captured if and only if, for *every* \(H_0\)-eigenspace, restriction to the coordinate set \(T\) is injective. This equivalence is independent of the values of the positive rates.

**2. Degenerate Fourier eigenspaces.** Write \(\theta_j=2\pi j/n\) and \(|\sigma\rangle=(|0\rangle+\sigma|1\rangle)/\sqrt2\), with \(\sigma=\pm1\). The Fourier eigenvalues of \(H_0\) are \(2Jc_j+\sigma K\). Within each parity band the distinct cosine levels have dimensions \(m_j\). Because the \(c_j\) are strictly decreasing for \(0\le j\le M\), an energy has at most one angular level from each of the two parity bands. A cross-band coincidence occurs precisely when
\[
2Jc_\ell+K=2Jc_j-K\quad\Longleftrightarrow\quad\kappa=c_j-c_\ell>0,\qquad j<\ell.
\]
Such an eigenspace has dimension \(m_j+m_\ell\), at most four. Noncrossing eigenvalues have dimension one or two. Since \(n\ge3\), at least one internal cosine level has multiplicity two, making two a universal lower bound. Hence the maximum eigenspace dimension is exactly the formula stated for \(\mu\), and at least this many absorber coordinates are necessary.

**3. Sharp two-, three-, and four-coordinate witnesses.** On any internal angular eigenspace the real Fourier basis consists of \(\cos(\theta_j x)\) and \(\sin(\theta_j x)\). At consecutive angular sites \(x=0,1\), its evaluation matrix has determinant \(\sin(\theta_j)\ne0\). Endpoint levels have a single basis function, constant for \(j=0\) and alternating in \(x\) for \(j=M\) when \(n\) is even. When no cross-band collision of dimension at least three occurs, \(T_2=\{(0,0),(1,0)\}\) therefore detects all individual cosine levels. The only possible cross-band coincidence of dimension two joins the two endpoints at \(\kappa=2\); the two evaluation columns are \((1,1)^\mathsf T\) and \((1,-1)^\mathsf T\), which are independent. Thus \(T_2\) is sufficient exactly in the two-absorber class.

If all cross-band eigenspaces have dimension at most three, extend to \(T_3=T_2\cup\{(0,1)\}\). Every three-dimensional collision pairs one internal two-dimensional cosine/sine level with one endpoint level of *opposite rung parity*. Evaluating at the two layers of angle zero separates the cosine component from the endpoint component, while the remaining angular-one value detects the nonzero sine component. The restricted matrix is therefore nonsingular. All smaller eigenspaces remain detected. This proves the three-absorber upper bound.

For every coupling ratio, take \(T_4=\{(0,0),(1,0),(0,1),(1,1)\}\). Summing and subtracting the two layer observations at each angle separates the two rung parities. Within either parity, the two consecutive angles injectively detect any angular level of dimension at most two. Thus every eigenspace, including a four-dimensional cross-band collision, is detected. In combination with the multiplicity lower bounds, the piecewise minimum is exact.

**4. All optimal pairs off resonance.** At a coupling with no cross-band coincidence, any two coordinates in the same angular position fail to detect an internal sine mode. For distinct angular positions \(a,b\), set \(d=b-a\pmod n\). The two evaluation rows are independent on every internal cosine/sine level, independently of their chosen layers, precisely when \(\sin(2\pi j d/n)\ne0\) for all \(1\le j<n/2\). Put \(g=\gcd(n,2)\) and \(L=n/g\). The condition is equivalent to \(\gcd(L,d)=1\): a nontrivial divisor gives some \(1\le j<L\) with \(L\mid jd\), and conversely a coprime \(d\) cannot. Exactly \(g\varphi(L)\) nonzero residues \(d\pmod n\) satisfy it. Counting the ordered first site \(2n\), the two choices of layer at the second site, and dividing unordered pairs by two gives \(2ng\varphi(L)\).

**5. Density of four-coordinate resonances.** For every target \(\alpha\in(0,2)\), choose angles \(u,v\in(0,\pi)\) with \(u<v\) and \(\cos u-\cos v=\alpha\); for example take \(\cos u=\alpha/2\), \(\cos v=-\alpha/2\). For arbitrarily large \(n\), choose indices \(1\le j<\ell<n/2\) whose grid angles \(2\pi j/n\) and \(2\pi\ell/n\) approach \(u,v\). Their cosine differences lie in \(\mathcal R_4(n)\) and converge to \(\alpha\). Conversely, all differences of cosines lie in \((0,2]\), and each fixed \(n\) supplies only finitely many. This proves the density and finite-exception claims.

## Verification
The standalone `verification/check_weighted_prism.py` independently constructs the finite Hamiltonian adjacency action, forms the coordinate-observability Krylov matrix, and computes its rank modulo the prime \(1000003\) for rational couplings. It also constructs the complete real Fourier eigenspaces and checks the proposed supports at every pairwise crossing through \(n=28\). Its completed replay reported 144 finite-field witness/lower-bound tests, 1,215 two-site-pair comparisons, and 1,040 spectral resonance cases (`VERIFY_OK`). These are finite checks, not the proof of the infinite-family theorem; the latter is given above.

Run with Python 3 and NumPy available: `python verification/check_weighted_prism.py`.

## Relationship to prior work
Krovi and Brun established a spectral-degeneracy explanation for infinite quantum hitting times. Mülken and Blumen described non-Hermitian trapping for continuous-time quantum walks. Nakamura and colleagues studied coherent transport in circular ladder networks attached to semi-infinite leads, with a different scattering observable. In contrast, the present theorem classifies the *minimum number and geometry of local absorbers* needed for complete eventual capture as the rung coupling varies, including the exact two-to-three-to-four resonance diagram and its dense size-varying four-site locus. Equal-coupling prism spectral coincidences are a special case, not a replacement for the variable-coupling absorber optimization.

## Limitations
The model assumes uniform positive intra-ring and inter-ring coherent couplings, strictly positive onsite losses at every selected trap, and single-particle dynamics in a finite network. The formula does not optimize lifetimes, rates, or measurement protocols, does not establish thermodynamic behavior at fixed \(n\), and says nothing about arbitrary graph perturbations or interactions. Exact historical priority within specialized control-theoretic observability literature has not been independently certified.

## References
1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times* (first public 2006-06-10), https://arxiv.org/abs/quant-ph/0606094.
2. K. Nakamura et al., *Quantum Transport in Ladder-Type Networks: Role of nonlinearity, topology and spin* (first public 2009-09-13), https://arxiv.org/abs/0909.2401.
3. O. Mülken and A. Blumen, *Continuous-Time Quantum Walks: Models for Coherent Transport on Complex Networks* (first public 2011-01-12), https://arxiv.org/abs/1101.2572.
