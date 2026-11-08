# Conditional spatial mixing on rational Feres billiard angle classes

## Finding
Fix an integer \(N\ge 7\), put \(\alpha=\pi/N\), and take \(0<\theta<\alpha\). For the Feres random reflection kernel specified below, initialize a unit-circle billiard at an arbitrary boundary azimuth \(s\) and outgoing angle \(\theta\). Write \((S_t,\Theta_t)\) for position and outgoing angle after \(t\) random collisions. Then:

1. The angular chain has exactly \(N\) states, is irreducible and reversible, and has stationary law
   \[\pi_\theta(v)=\frac{\sin v}{\sum_{w\in\mathcal C_\theta}\sin w}.\]
   Its period is \(1\) when \(N\) is odd and \(2\) when \(N\) is even.
2. If \(\theta/\pi\) is irrational, then for every fixed nonzero integer \(k\) and every function \(g\) on the angular class there are constants \(C_{k,g}<\infty\) and \(r_k<1\) such that
   \[\left|\mathbb E_{s,\theta}[e^{ikS_t}g(\Theta_t)]\right|\le C_{k,g}r_k^t.\]
   In particular \(S_t\) converges weakly in law to normalized Haar measure \(H\) on the boundary. For odd \(N\), the joint law converges weakly to \(H\otimes\pi_\theta\). For even \(N\), its two limiting laws, according to \(t\bmod 2\), are \(H\otimes\pi_\theta^{(0)}\) and \(H\otimes\pi_\theta^{(1)}\), respectively. Here \(\pi_\theta^{(j)}\) is the stationary law conditioned on the cyclic class occupied at time \(t\equiv j\pmod 2\).
3. If \(\theta/\pi\) is rational, every \(S_t\) belongs to a common finite translate of a finite subgroup of the circle, and therefore the boundary marginal cannot converge weakly to \(H\).

Consequently irrationality of \(\theta/\pi\) is *necessary and sufficient* for weak Haar convergence of the boundary marginal from a point initial condition on this angular class. This conditional convergence holds although the full random billiard is not globally mixing for rational \(\alpha/\pi\).

## Assumptions and scope
For \(0<\alpha<\pi/6\), define the four angle maps on \((0,\pi)\):
\[T_1(v)=v+2\alpha,\quad T_2(v)=-v+2\pi-4\alpha,\quad T_3(v)=v-2\alpha,\quad T_4(v)=-v+4\alpha.\]
A branch is used only where its probability is positive. Set \(u_\beta(v)=(1+\tan\beta\cot v)/2\), where \(\cot v=\cos v/\sin v\) is well-defined for all \(0<v<\pi\), including \(v=\pi/2\). The four probabilities, in the ordering of the maps, are the published Feres law:

\[p_1(v)=\begin{cases}1&0\le v<\alpha,\\u_\alpha(v)&\alpha\le v<\pi-3\alpha,\\2\cos(2\alpha)u_{2\alpha}(v)&\pi-3\alpha\le v<\pi-2\alpha,\\0&\pi-2\alpha\le v\le\pi\end{cases}\]
\[p_2(v)=\begin{cases}0&0\le v<\pi-3\alpha,\\u_\alpha(v)-2\cos(2\alpha)u_{2\alpha}(v)&\pi-3\alpha\le v<\pi-2\alpha,\\u_\alpha(v)&\pi-2\alpha\le v<\pi-\alpha,\\0&\pi-\alpha\le v\le\pi\end{cases}\]
\[p_3(v)=\begin{cases}0&0\le v<2\alpha,\\2\cos(2\alpha)u_{2\alpha}(-v)&2\alpha\le v<3\alpha,\\u_\alpha(-v)&3\alpha\le v<\pi-\alpha,\\1&\pi-\alpha\le v\le\pi\end{cases}\]
\[p_4(v)=\begin{cases}0&0\le v<\alpha,\\u_\alpha(-v)&\alpha\le v<2\alpha,\\u_\alpha(-v)-2\cos(2\alpha)u_{2\alpha}(-v)&2\alpha\le v<3\alpha,\\0&3\alpha\le v\le\pi.\end{cases}\]
The stochastic angle kernel is \(P(v,w)=\sum_{i:T_i(v)=w}p_i(v)\). The circular billiard composition after choosing \(w\) is \((s,v)\mapsto(s+2w\pmod{2\pi},w)\). The only asserted initial-angle interval is \(\theta\in(0,\pi/N)\); endpoints and other angle classes are outside the claim. The claim is for each fixed \(N\), not uniformly as \(N\to\infty\).

Write \(N=2m+1\) (odd) or \(N=2m\) (even), and set
\[A_j=\theta+2j\alpha,\qquad B_j=-\theta+2j\alpha.\]
For odd \(N\), the class is \(\mathcal C_\theta=\{A_0,\ldots,A_m\}\cup\{B_1,\ldots,B_m\}\); for even \(N\), it is \(\{A_0,\ldots,A_{m-1}\}\cup\{B_1,\ldots,B_m\}\). Both sets have exactly \(N\) distinct members in \((0,\pi)\).

## Proof
**Angular graph and stationary law.** Direct substitution of the displayed branch maps and their positive probability intervals gives precisely these undirected transition edges (every edge permits both directions and there are no self-loops). In both parities there are the neighbor edges \(A_j\!\leftrightarrow\!A_{j+1}\) whenever both indices appear, and \(B_j\!\leftrightarrow\!B_{j+1}\) whenever both appear. Additional edges are \(A_1\!\leftrightarrow\!B_1\) and \(A_{m-1}\!\leftrightarrow\!B_m\) for odd \(N=2m+1\), or \(A_1\!\leftrightarrow\!B_1\) and \(A_{m-1}\!\leftrightarrow\!B_{m-1}\) for even \(N=2m\). The explicit intervals show all these probabilities are strictly positive for \(0<\theta<\alpha\). Thus the graph is one cycle of length \(N-2\) with two pendant vertices, and is connected. Since all transition edges can be traversed in both directions, the period is \(\gcd(2,N-2)\), giving the stated parity.

The elementary identity \(u_\beta(v)=\sin(v+\beta)/(2\cos\beta\sin v)\) simplifies the edge weights. Substitution on each of the listed edge types (including the two reflection edges, where the terms involving \(\cos(2\alpha)\) cancel appropriately) proves
\[\sin(v)P(v,w)=\sin(w)P(w,v)\qquad(v,w\in\mathcal C_\theta).\]
For instance, along a nonexceptional forward edge \(w=v+2\alpha\), both sides equal \(\sin(v+\alpha)/(2\cos\alpha)\). At the lower endpoint edge \(A_0\leftrightarrow A_1\), both sides are \(\sin\theta\); at a terminal degree-one edge, both sides equal the sine of the pendant-state angle. On the reflection edge \(A_1\leftrightarrow B_1\), both sides equal \(\sin(\alpha-\theta)/(2\cos\alpha)\). On the upper reflection edge, both sides equal \(\sin\theta/(2\cos\alpha)\) if \(N\) is odd, and \(\sin(\alpha-\theta)/(2\cos\alpha)\) if \(N\) is even. These identities follow by simplifying the displayed branch formulas with \(\sin(v+\beta)/(2\cos\beta\sin v)\), and cover every edge type. This proves detailed balance, positivity, uniqueness and the stated stationary distribution. A finite irreducible Markov chain converges to its stationary law in the aperiodic case and to the corresponding cyclic conditional stationary laws along each residue class when its period is two.

**Fourier contraction.** For each integer \(k\), define the finite twisted matrix
\[K_k(v,w)=P(v,w)e^{2ikw}.\]
For any angular observable \(g\), the Markov property gives the exact identity
\[\mathbb E_{s,\theta}[e^{ikS_t}g(\Theta_t)]=e^{iks}\bigl(K_k^t g\bigr)(\theta).\]
Since \(|K_k(v,w)|\le P(v,w)\), \(\rho(K_k)\le1\). Suppose \(k\ne0\) and \(\rho(K_k)=1\). Choose an eigenvalue \(\lambda\) of modulus one and a corresponding nonzero eigenvector \(f\). The maximum-modulus principle for a finite irreducible stochastic matrix implies \(|f(v)|\) is the same positive constant for all states. Equality in the triangle inequality then enforces, on each positive edge \(v\to w\),
\[e^{2ikw}f(w)=\lambda f(v).\]
At \(A_1\), the two positive two-edge return paths \(A_1\to A_0\to A_1\) and \(A_1\to B_1\to A_1\) have total boundary displacements \(4\theta+4\alpha\) and \(8\alpha\), respectively. Applying the edge relation twice to each forces
\[e^{ik(4\theta+4\alpha)}=\lambda^2=e^{8ik\alpha},\qquad e^{4ik(\theta-\alpha)}=1.\]
If \(\theta/\pi\) is irrational and \(\alpha/\pi=1/N\), this is impossible. Thus \(\rho(K_k)<1\) for every nonzero integer \(k\). Finite matrix powers are bounded by \(C_kr_k^t\) for some \(\rho(K_k)<r_k<1\), proving the joint Fourier bounds for each fixed \(k\). Fourier approximation in the boundary coordinate and finiteness of the angle class yield weak convergence to Haar times the applicable angular limit.

**Rational-angle obstruction.** If \(\theta/\pi\) is rational, all elements of \(\mathcal C_\theta\) are rational multiples of \(\pi\). Therefore all increments \(2\Theta_t\) belong to one finite subgroup of \(\mathbb R/(2\pi\mathbb Z)\). Starting at \(s\), every \(S_t\) remains in its finite translate. A weak limit supported there cannot equal atomless Haar measure.

## Verification
The supplementary program `angles_check.py` evaluates the displayed branches and graph on integer values \(7\le N\le16\), at \(\theta=(\sqrt2/3)\alpha\), checks that probabilities sum to one, verifies detailed balance, graph topology and angular period, and computes four Fourier-mode spectral radii. This is finite evidence complementing—not replacing—the algebraic proof for every \(N\ge7\) and every \(\theta\in(0,\alpha)\).

## Relationship to prior work
Vales and Pinto-de-Carvalho (2020), arXiv:2005.01892v1, define the random circular billiard and prove almost-sure denseness of boundary trajectories for rational \(\alpha/\pi\) and irrational \(\theta/\pi\) (their Theorem 6.3). Denseness is a pathwise support property and does not imply fixed-time weak equidistribution from a point initial state. Vales (2022), arXiv:2212.00872v1, proves that the *full* random billiard is mixing only if \(\alpha/\pi\) is irrational, and exhibits the periodic and aperiodic angular graphs at \(N=8\) and \(N=7\). That global statement does not exclude the conditional boundary-marginal convergence proved here for each fixed rational angular class. The exact \(N\)-state parity classification, all nontrivial twisted-mode contraction, and phase-resolved joint limits are the additional assertions.

## Limitations
No total-variation convergence is claimed: from a point start, each fixed-time spatial law has finite support and hence remains singular with respect to Haar. No uniform rate over all boundary Fourier modes, in \(N\), or in irrational \(\theta\) is asserted. The global rational-parameter billiard remains nonmixing. Independent validation of the mathematical contribution and literature priority has not been performed.

## References
- T. Vales and S. Pinto-de-Carvalho, *A Random Billiard Map in the Circle*, arXiv:2005.01892v1 (first public 2020-05-05), especially Sections 5–6 and Theorem 6.3, https://arxiv.org/abs/2005.01892 .
- T. Vales, *Random circular billiards on surfaces of constant curvature: Pseudo integrability and mixing*, arXiv:2212.00872v1 (2022-12-01), especially Sections 3, 5 and 6, https://arxiv.org/abs/2212.00872 .
- R. Feres, *Random Walks Derived from Billiards*, in *Dynamics, Ergodic Theory and Geometry*, Cambridge University Press (print 2007), for the original reflection kernel and Markov framework.
