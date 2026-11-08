# Two shortcuts turn cycle maximal-entropy relaxation from diffusive to exponentially slow

## Finding
For each integer \(L\geq5\), let \(G_L\) be the simple graph on \(\mathbb Z/(2L)\) formed by the ordinary cycle edges together with the **two** nonoverlapping shortcut edges \(\{0,2\}\) and \(\{L,L+2\}\). Write \(A_L\) for its adjacency matrix and \(\lambda_+(L)>\lambda_-(L)\) for its two highest eigenvalues.

**Theorem.** Exactly two eigenvalues of \(A_L\) are strictly larger than \(2\). They are simple, and \(\lambda_+(L)>\lambda_-(L)>2\); every remaining adjacency eigenvalue is at most \(2\). Write \(q_\pm(L)\in(0,1)\) for their unique spectral parameters, \(\lambda_\pm=q_\pm+q_\pm^{-1}\). These parameters are precisely the unique solutions to

\[
\frac{q_\pm(1+q_\pm^2)}{1-q_\pm^2}\,
\frac{1\pm q_\pm^{L-2}}{1\mp q_\pm^L}=1.
\]

Let \(q_*\) be the unique root in \((0,1)\) of \(q^3+q^2+q-1=0\), and define \(\lambda_*=q_*+q_*^{-1}\). Then

\[
\lambda_+(L)-\lambda_-(L)\sim C_*q_*^L,\qquad
C_*=\frac{2(1+q_*^2)(1-q_*^2)^3}{q_*^4(1+4q_*^2-q_*^4)}.
\]

The maximal-entropy random walk (MERW) on \(G_L\) has the positive subleading eigenvalue ratio \(\lambda_-/\lambda_+\), and its corresponding exponential relaxation time obeys

\[
\tau_{\rm MERW}^{(2)}(L):=\frac{1}{\log(\lambda_+(L)/\lambda_-(L))}
\sim\frac{\lambda_*}{C_*}\,q_*^{-L}.
\]

Numerically, \(q_*=0.543689012692\ldots\), \(\lambda_*=2.382975767906\ldots\), \(C_*=4.947359378555\ldots\), and \(\lambda_*/C_*=0.481666195149\ldots\). This is exponential in the number of vertices \(2L\), despite the presence of only two noncycle edges.

There is a sharp comparison: on the bare cycle, positive-mode relaxation is \(\tau_{\rm MERW}^{(0)}(L)\sim2L^2/\pi^2\); with **one** shortcut \(\{0,2\}\), it converges to the finite constant \(1/\log(\lambda_*/2)\). By contrast, the ordinary degree-normalized simple random walk on \(G_L\) retains a positive-mode spectral relaxation time of order \(L^2\). Thus adding a second, distant, identical shortcut to the one-shortcut graph changes MERW positive-mode relaxation from bounded to exponentially large.

## Assumptions and scope
All graphs are finite, undirected, simple, with unit edge weights and no self-loops. Vertex indices are modulo \(2L\). The one-shortcut graph is the same cycle with only \(\{0,2\}\) adjoined, and the zero-shortcut graph is the cycle itself. For each connected graph, let \(\lambda_1\) be the Perron adjacency eigenvalue, let \(\psi>0\) be its Euclidean-unit eigenvector, and define MERW by \(P_{ij}=A_{ij}\psi_j/(\lambda_1\psi_i)\). Its stationary measure is \(\pi_i=\psi_i^2\). The transition eigenvalues are exactly adjacency eigenvalues divided by \(\lambda_1\). The relaxation time in this theorem refers specifically to the positive second eigenmode, \(1/\log(\lambda_1/\lambda_2)\), **not** an unproved total-variation mixing-time cutoff or the absolute-value spectral radius.

The symmetric two-shortcut graph contains triangles and is irreducible and aperiodic. The statements apply to every integer \(L\ge5\), with asymptotics along integers tending to infinity. No random graph ensemble is assumed.

## Proof
**1. Exact resolvent and rank-two reduction.** Let \(B\) be the adjacency matrix of the \(2L\)-cycle. For \(\lambda>2\), let \(q\in(0,1)\) be defined by \(\lambda=q+q^{-1}\). The Green function of the cycle is

\[
R_{ij}:=\bigl((\lambda I-B)^{-1}\bigr)_{ij}
=G(i-j),\quad G(k)=\frac{q^{\bar k}+q^{2L-\bar k}}{(q^{-1}-q)(1-q^{2L})},\quad \bar k\in\{0,\ldots,2L-1\}.
\]

This is checked directly by substitution into \((\lambda I-B)G=\delta_0\): away from zero, \(\lambda q^k=q^{k-1}+q^{k+1}\); the displayed denominator supplies the unit source at zero and enforces cyclic periodicity.

Set \(v_1=e_0+e_2\), \(v_2=e_L+e_{L+2}\), \(w_1=e_0-e_2\), and \(w_2=e_L-e_{L+2}\). The shortcut perturbation is

\[
A_L-B=\tfrac12(v_1v_1^T+v_2v_2^T)-\tfrac12(w_1w_1^T+w_2w_2^T).
\]

The reflection \(i\mapsto2-i\pmod{2L}\) commutes with both \(B\) and \(A_L\), fixes each \(v_j\) and negates each \(w_j\). Thus its even sector has a nonnegative rank-two perturbation; its odd sector has a nonpositive perturbation and cannot support eigenvalues larger than \(2\), since \(\max\operatorname{spec}(B)=2\).

By the elementary Birman–Schwinger identity (multiply \((\lambda I-B)u=\tfrac12\sum_j v_jv_j^Tu\) by the two row vectors \(v_j^T\)), the eigenvalues above \(2\) are those for which \(1\) is an eigenvalue of the real symmetric \(2\times2\) matrix \(\tfrac12(v_i^TRv_j)_{i,j=1,2}\). Its diagonal entries are \(G(0)+G(2)\), and its off-diagonal entries \(G(L)+G(L-2)\). The two scalar secular equations are therefore

\[
1=G(0)+G(2)\pm\bigl(G(L)+G(L-2)\bigr).
\]

Substitution and cancellation of \(1\pm q^L\) give precisely the two stated equations. For each sign, its right-hand side, viewed as a Rayleigh quadratic form of \((\lambda I-B)^{-1}\) on the nonzero vector \(v_1\pm v_2\), is strictly decreasing and continuous in \(\lambda>2\) and tends to zero at infinity. The plus branch diverges at \(\lambda\downarrow2\). For the minus branch, the limit at \(q\uparrow1\) is \((L-2)/2\), strictly greater than \(1\) exactly for \(L\ge5\). There is hence exactly one root in each branch for every stated \(L\). The plus branch dominates the minus branch because \(G(L)+G(L-2)>0\); hence its root gives the strictly greater eigenvalue. These account for every eigenvalue above \(2\) because the positive perturbation has rank two. Simplicity follows from strict scalar monotonicity and distinct roots.

**2. Exponentially small splitting.** Put \(F(q)=q(1+q^2)/(1-q^2)\). The isolated-well limit \(F(q_*)=1\) is equivalent to \(q_*^3+q_*^2+q_*-1=0\). Strict monotonicity gives its unique positive root. As \(L\to\infty\), the two branches converge locally uniformly to \(F(q)=1\), so \(q_\pm\to q_*\). Since

\[
F'(q)=\frac{1+4q^2-q^4}{(1-q^2)^2},\qquad
\frac{d}{dq}(q+q^{-1})=-\frac{1-q^2}{q^2},
\]

first-order expansion of the exact secular equations yields

\[
q_+(L)=q_*-\frac{(1+q_*^2)q_*^{L-2}}{F'(q_*)}+o(q_*^L),\qquad
q_-(L)=q_*+\frac{(1+q_*^2)q_*^{L-2}}{F'(q_*)}+o(q_*^L).
\]

Here the correction to a power caused by shifting \(q\) is of order \(Lq_*^{2L-3}=o(q_*^L)\), because \(0<q_*<1\). The derivative of \(q+q^{-1}\) then gives the stated positive constant \(C_*\) and spectral splitting. Finally, \(\log(\lambda_+/\lambda_-)\sim(\lambda_+-\lambda_-)/\lambda_*\), which proves the relaxation-time asymptotic.

**3. Why exactly two shortcuts matter.** The bare cycle has top eigenvalues \(2\) and \(2\cos(\pi/L)\), and MERW is ordinary simple random walk. Thus \(\tau^{(0)}=1/[-\log\cos(\pi/L)]\sim2L^2/\pi^2\). For the graph with one shortcut \(\{0,2\}\), the shortcut quadratic form is \(\tfrac12(v_1v_1^T-w_1w_1^T)\). Consequently there is at most one eigenvalue above \(2\); its positive secular equation is \(1=G(0)+G(2)\), whose largest eigenvalue tends to \(\lambda_*>2\). Rank-one eigenvalue interlacing gives \(2\cos(\pi/L)\le\lambda_2\le2\). Therefore \(\lambda_2\to2\) and its relaxation time tends to \(1/\log(\lambda_*/2)\), which is finite.

**4. Degree-normalized walk remains diffusive.** On \(G_L\), degrees lie between \(2\) and \(3\) and the edge count equals \(2L+2\). The stationary measure of the ordinary simple random walk is proportional to degree; its reversible Dirichlet form is \(\mathcal E(f,f)=[2(2L+2)]^{-1}\sum_{\{u,v\}\in E}(f(u)-f(v))^2\). Compared with the cycle, the Poincaré lower bound follows from \(\mathcal E_{G_L}\ge c\mathcal E_{C_{2L}}\), uniformly equivalent stationary variances, and the cycle spectral gap of order \(L^{-2}\). For the matching upper bound, take \(f(j)=\sin(\pi j/L)\), subtract its degree-weighted mean, and use \(\sum_j(f(j+1)-f(j))^2=O(L^{-1})\), while each added chord contributes \(O(L^{-2})\) to the sum; the stationary variance is bounded below. The quotient is \(O(L^{-2})\). Hence the ordinary positive spectral gap is \(\Theta(L^{-2})\), and its corresponding relaxation time is \(\Theta(L^2)\).

## Verification
The stand-alone `verify.py` requires only Python 3. It independently builds the actual finite adjacency matrices, computes all their eigenvalues via a symmetric Jacobi rotation routine for \(5\le L\le14\), verifies both exact secular roots and that no third eigenvalue exceeds \(2\), tests the explicit resolvent eigenvectors entrywise, compares with one-chord matrices, and checks the asymptotic coefficient at several larger sizes. The extracted verifier prints `VERIFY_OK 131 assertions`. These are finite sanity checks; the exact/all-size and asymptotic statements are proved above.

## Relationship to prior work
Burda, Duda, Luck and Waclaw (arXiv:0810.4113, 2008) introduced the MERW stationary construction and established localization by defects; those foundational facts are not new here. Their later review (arXiv:1004.3667, 2010), Sections 6.1–6.3, treats repulsive rung defects and **one attractive rung**, including a localized wavefunction; it does not give the paired span-two chords on a single cycle or the two-eigenvalue formula here. Ochab (arXiv:1202.1160, 2012), Section 4, **already observed exponential MERW relaxation** numerically in ladders with two extensive intact regions separated by missing-rung gaps, contrasted with diffusive generic walks. Hence exponential MERW trapping and the tunneling analogy are not independently new claims. The present contribution is the *exact two-added-edge threshold* on an otherwise regular cycle and the proved closed-form splitting exponent/prefactor for this minimal symmetric two-shortcut family. Lin and Zhang (arXiv:1406.3680, 2014) derive general spectral expressions for MERW mean first passage times in other network families; that does not directly assert this positive relaxation gap.

## Limitations
The two shortcut locations and spans are fixed by the graph definition; no claim is made for arbitrary two-edge placements, weighted edges, general defect shapes or random networks. The computed time is the positive second-mode e-folding time, not a total-variation mixing-time constant, a universal cutoff, or a hitting time. The analytical spectral computation does not establish priority over every possibly uncatalogued two-defect eigenvalue calculation. Earlier work already establishes qualitatively exponential relaxation for other graphs; only the particular sharp minimal-edge statement and exact constant are under originality consideration.

## References
1. Z. Burda, J. Duda, J. M. Luck and B. Waclaw, *Localization of maximal entropy random walk*, first posted 2008-10-22, https://arxiv.org/abs/0810.4113 .
2. Z. Burda, J. Duda, J. M. Luck and B. Waclaw, *The various facets of random walk entropy*, first posted 2010-04-21, https://arxiv.org/abs/1004.3667 , especially Section 6.
3. J. K. Ochab, *Maximal Entropy Random Walk: solvable cases of dynamics*, first posted 2012-02-06, https://arxiv.org/abs/1202.1160 , especially Section 4.
4. Y. Lin and Z. Zhang, *Mean first-passage time for maximal-entropy random walks in complex networks*, 2014, https://arxiv.org/abs/1406.3680 .
