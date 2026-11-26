# Exact dark-space dimension for Hamming-ball absorption on hypercube quantum walks

## Finding
Let \(d\ge6\), \(2\le r\le d\), and let \(Q_d\) be the binary \(d\)-cube. Every vertex at Hamming distance at most \(r\) from the origin is a strictly positive sink. For continuous-time coherent hopping on the entire cube with arbitrary positive, possibly unequal, sink strengths, the dimension of the exactly nondecaying subspace is
\[
D(d,r)=2^d-\sum_{w=0}^d\binom d{\min\{r,w,d-w\}}.
\]
In particular, for \(r\le\lfloor d/2\rfloor\), its orthogonal complement (the eventual absorbing or *bright* space) has dimension
\[
B(d,r)=2\sum_{j=0}^{r-1}\binom dj+(d-2r+1)\binom dr,
\]
and for \(r\ge\lfloor d/2\rfloor\) there are no dark states. The last prethreshold radius has a striking exact residual:
\[
D(2t,t-1)=\frac{1}{t+1}\binom{2t}{t}\quad(t\ge3),\qquad
D(2t+1,t-1)=\frac{2}{t+2}\binom{2t+2}{t+1}\quad(t\ge3).
\]
These are respectively one and two consecutive Catalan numbers. A uniform classical mixture of all \(2^d\) site states is ultimately absorbed with probability exactly \(B(d,r)/2^d\). For fixed \(r\ge2\), as \(d\to\infty\),
\[
B(d,r)=\frac{d^{r+1}}{r!}+O(d^r),
\qquad \frac{B(d,r)}{2^d}\longrightarrow0.
\]
For example \(D(8,2)=98\), \(D(8,3)=14\), and \(D(8,4)=0\), although the undirected cube is connected at every radius.

## Assumptions and scope
Identify vertices with subsets \(x\subseteq[d]\). Write \(A_d\) for the usual (unweighted, undirected) cube adjacency matrix. Fix \(J>0\), a real scalar offset \(\epsilon\), and strictly positive finite real coefficients \(\kappa_x\) for each \(x\) with \(|x|\le r\). Define the effective one-particle non-Hermitian Hamiltonian
\[
K=J A_d+\epsilon I-i\Gamma,\qquad
\Gamma=\sum_{|x|\le r}\kappa_x |x\rangle\langle x|.
\]
No measurement-induced dephasing, additional disorder, or many-body interactions are assumed. Time evolution is \(e^{-itK}\); a component is called *dark* precisely if its norm is preserved at all times. Loss probability is the missing norm of the unnormalized one-particle state. The initial completely mixed state means \(\rho_0=I/2^d\), an incoherent site mixture. The formulas apply to every specified real \(J\), \(\epsilon\), and every individual strictly positive \(\kappa_x\), not merely equal rates.

## Proof
**1. Exactly nondecaying states are common free-Hamiltonian eigenvectors annihilated by all sinks.** For \(\psi(t)=e^{-itK}\psi(0)\),
\[
\frac{d}{dt}\|\psi(t)\|^2=-2\langle\psi(t),\Gamma\psi(t)\rangle\le0.
\]
A state preserving its norm for all times must satisfy \(\Gamma\psi(t)=0\) for all times, hence lies in the largest \(A_d\)-invariant subspace of \(\ker\Gamma\). Because \(A_d\) is Hermitian, this largest invariant subspace is the orthogonal direct sum of \(\ker\Gamma\cap E_w\), where \(E_w\) are its distinct eigenspaces. Conversely every vector in this direct sum evolves unitarily without loss. Every other eigenvalue of \(K\) lies strictly below the real axis: if \(Kv=\lambda v\) and \(\operatorname{Im}\lambda=0\), taking imaginary parts gives \(\langle v,\Gamma v\rangle=0\), and positivity then gives \(\Gamma v=0\), so \(v\) belongs to the dark space. The orthogonal dark complement is invariant under \(K\) (both the Hermitian adjacency and the diagonal loss preserve the dark space and its orthogonal complement); all its eigenvalues have negative imaginary parts. Finite-dimensional matrix exponentiation therefore tends to zero on the complement, including any Jordan blocks. Hence eventual survival is exactly the initial dark-space weight.

**2. Fourier decomposition of the cube.** For each frequency subset \(S\subseteq[d]\), define its Walsh character \(\chi_S(x)=(-1)^{|S\cap x|}\). The characters of weight \(|S|=w\) span an eigenspace \(E_w\) of eigenvalue \(d-2w\), dimension \(\binom dw\). These \(d+1\) eigenvalues are pairwise distinct. Write \(F_{r,w}\) for the restriction matrix with entries \(\chi_S(x)\), rows \(|x|\le r\), columns \(|S|=w\). Because \(\ker\Gamma\) is exactly the space of functions vanishing on this ball,
\[
\dim(E_w\cap\ker\Gamma)=\binom dw-\operatorname{rank}_{\mathbb C}F_{r,w}.
\]

**3. Exact restrictions by subset incidence.** With \(\mathbf1_{T\subseteq S}\) denoting the usual subset-incidence indicator, expansion of the product \(\chi_S(x)=\prod_{i\in x}(1-2\mathbf1_{i\in S})\) gives
\[
\chi_S(x)=\sum_{T\subseteq x}(-2)^{|T|}\mathbf1_{T\subseteq S}.
\]
The transformation is triangular and invertible over characteristic zero on the entire down-closed family \(|x|\le r\). Thus \(F_{r,w}\) has the same row span as the stack of subset-inclusion matrices \(W_{j,w}\), for \(0\le j\le r\), where \((W_{j,w})_{T,S}=\mathbf1_{T\subseteq S}\).

Put \(t=\min\{r,w,d-w\}\). If \(r\ge\min\{w,d-w\}\), the block \(W_{t,w}\) has full column rank \(\binom dw\): when \(t=w\) it is an identity matrix, and when \(t=d-w\le w\), the classical maximal-rank theorem for inclusion matrices makes its square matrix nonsingular over characteristic zero [3]. Hence the stack has full column rank.

If \(r<\min\{w,d-w\}\), \(W_{r,w}\) has full row rank \(\binom dr\) by the same theorem [3]. For each \(Y\) of size \(j<r\), the identity
\[
\sum_{T\supseteq Y,\ |T|=r}\mathbf1_{T\subseteq S}
=\binom{w-j}{r-j}\mathbf1_{Y\subseteq S}
\]
expresses every row of \(W_{j,w}\) as a linear combination of rows of \(W_{r,w}\), since \(w\ge r\) and the binomial coefficient is nonzero. Thus the whole stack has rank \(\binom dr\). Both cases yield the exact sector rank
\[
\operatorname{rank}_{\mathbb C}F_{r,w}=\binom d{\min\{r,w,d-w\}}.
\]
This is precisely the known subset-incidence rank mechanism, here evaluated simultaneously across every energy sector of the non-Hermitian transport problem.

**4. Sum the sectors and find the transition.** Summing the sector ranks yields \(B(d,r)\) and subtracting from \(2^d\) gives \(D(d,r)\). For \(r\le\lfloor d/2\rfloor\), the indices \(w<r\), \(r\le w\le d-r\), and \(w>d-r\) give the displayed closed binomial sum. For \(r=\lfloor d/2\rfloor\), binomial symmetry gives \(B(d,r)=2^d\), hence no dark state for any larger radius. Substituting \(d=2t,r=t-1\) yields \(D=\binom{2t}{t}-\binom{2t}{t-1}=\binom{2t}{t}/(t+1)\). Substituting \(d=2t+1,r=t-1\) gives \(D=2(\binom{2t+1}{t}-\binom{2t+1}{t-1})=2\binom{2t+2}{t+1}/(t+2)\). Finally \(\binom dr=d^r/r!+O(d^{r-1})\) proves the fixed-radius asymptotic.

**5. Physical absorption and independence of loss rates.** The dark projection has rank \(D(d,r)\), is entirely supported outside the sink ball, and is independent of all positive \(\kappa_x\). For \(I/2^d\), the limit of the surviving trace is \(D(d,r)/2^d\), so ultimate capture is \(B(d,r)/2^d\). For an equally weighted mixture on *only* the outside sites, if \(r<d\), survival is \(D(d,r)/(2^d-\sum_{j=0}^r\binom dj)\). These are incoherent initial states; individual localized states need not have equal absorption probabilities.

## Verification
The companion standalone Python 3 program `verify.py` requires only the standard library. It exactly compares all 280 Walsh-restriction sector ranks over \(\mathbb F_{1000003}\) for dimensions two through eight with the proposed characteristic-zero ranks; compares 25 separately built direct cube-Hamiltonian Krylov ranks for dimensions two through six; and checks the integer Catalan/threshold identities up through dimension 38. Its output is `EXACT_WALSH_SECTORS 280`, `EXACT_KRYLOV_CASES 25`, `VERIFY_OK checks=759`. The small-characteristic computations are independent finite checks, not proof of the characteristic-zero infinite-family theorem, which follows analytically above. Radius-zero and radius-one cases in the program are regression controls; the assessed new claim is only for radius at least two.

## Relationship to prior work
The physical framework of continuous-time quantum transport with irreversible trapping appears in Mülken and Blumen [1], and the algebraic relation between transport efficiency, the sink-visible subspace and dark eigenstates is developed by Le et al. [2] and Razzoli, Paris and Bordone [4]. The maximal-rank theorem for subset-incidence matrices is Gottlieb's [3], and is not claimed as new. The contribution here is the simultaneous sector-by-sector rank evaluation for *all* Hamming-ball sinks on the hypercube, its radius-dependent closed absorption formula for arbitrary positive sink strengths, the sharp complete-absorption threshold and the Catalan residual dimensions. The directly related radius-zero/one hypercube sink cases are established baselines, not part of the asserted new contribution. The result does not claim that the component lemmas are new or that absence of a search hit proves priority.

## Limitations
The result requires an ideal finite cube with homogeneous real hopping, a scalar on-site offset, and strictly positive loss at **every** site inside one Hamming ball. Zero or negative rates, site-dependent real potentials, non-cube or weighted edges, several separated balls, dephasing, many particles and conditional normalized dynamics are not included. The observed dark dimension is an invariant of the model, not an experimental guarantee of a measurable long-time signal in the presence of other noise. Historical priority remains subject to specialized multi-sink quantum-walk literature and any unindexed applications of the known inclusion-matrix theorem; an independent audit has not been performed.

## References
[1] O. Mülken and A. Blumen, *Continuous-Time Quantum Walks: Models for Coherent Transport on Complex Networks*, arXiv:1101.2572, first public version 12 January 2011. https://arxiv.org/abs/1101.2572

[2] T. P. Le, L. Donati, S. Severini and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (2017). https://arxiv.org/abs/1707.07482

[3] D. H. Gottlieb, *A Certain Class of Incidence Matrices*, Proceedings of the AMS 17 (1966), 1233–1237. https://doi.org/10.1090/S0002-9939-1966-0204305-9 ; openly available manuscript https://www.math.purdue.edu/~gottlieb/Bibliography/Incidence.pdf

[4] L. Razzoli, M. G. A. Paris and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, Entropy 23 (2021), 85. https://pmc.ncbi.nlm.nih.gov/articles/PMC7826824/

[5] S. Avni and A. Samorodnitsky, *Eigenvalues and Eigenfunctions of a Hamming Ball*, arXiv:2411.14597 (2024). https://arxiv.org/abs/2411.14597
