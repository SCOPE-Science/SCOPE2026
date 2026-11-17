# Two separated attracting windows for one alternating orbit in weighted bipartite phase networks

## Finding
Fix any finite, connected, undirected, positively weighted bipartite graph \(G=(U\sqcup V,E)\) whose weighted degree is the constant \(r>0\) at each vertex of \(U\) and the constant \(s>0\) at each vertex of \(V\). Put \(\Lambda=r+s\). For the discrete phase-network map
\[
 F_h(\theta)_i=\theta_i+h\sum_{j:\{i,j\}\in E}a_{ij}\left[\sin(\theta_i-\theta_j)+\frac15\sin(3(\theta_i-\theta_j))\right]\pmod{2\pi},\qquad h>0,
\]
there is a unique *symmetric alternating two-colour* primitive two-cycle of the form specified below for every \(h\Lambda>5/4\), and none for \(h\Lambda\le5/4\). This is uniqueness within the symmetric alternating two-colour ansatz only, not a classification of arbitrary periodic states.

Put \(t_1=\arccos(1/\sqrt3)\), \(t_3=\pi-t_1\), and \(K(t)=5t/[2\sin t(1+\cos^2t)]\). Define the four thresholds
\[
 A_0=\frac54,\quad A_1=\frac{15}{8}\sqrt{\frac32}\,t_1,\quad A_2=\frac{5\pi}{4},\quad A_3=\frac{15}{8}\sqrt{\frac32}\,t_3.
\]
They are strictly ordered \(A_0<A_1<A_2<A_3\), with numerical values \(1.25,2.193785866130905,3.926990816987241,5.020556928529579\). The two-cycle is **locally exponentially attracting on the phase-rotation quotient** in exactly the two disjoint parameter windows
\[
 \boxed{\;A_0<h\Lambda<A_1\quad\text{or}\quad A_2<h\Lambda<A_3.\;}
\]
It is a hyperbolic repeller on the quotient for \(A_1<h\Lambda<A_2\) or \(h\Lambda>A_3\). At \(h\Lambda=A_1,A_2,A_3\), all non-neutral return multipliers equal one; no nonlinear stability assertion is made there. The nontrivial period-two branch first appears at \(h\Lambda=A_0\), and that equality is not a primitive two-cycle.

More explicitly, for \(h\Lambda>A_0\), let \(t\in(0,\pi)\) be the unique solution of \(h\Lambda=K(t)\). The two phase configurations have respective colour differences \(\pi+t\) and \(\pi-t\), with their common phase chosen so that the arithmetic mean of all vertex phases is zero. The exact two-step multiplier spectrum is
\[
 \mu_j=\bigl(1-hq'(t)\lambda_j\bigr)^2,\qquad q(t)=\frac45\sin t\,(1+\cos^2t),\quad q'(t)=\frac45\cos t\,(3\cos^2t-1),
\]
where \(0=\lambda_1<\lambda_2\le\cdots\le\lambda_N=\Lambda\) are the eigenvalues of the weighted graph Laplacian. The multiplier \(\mu_1=1\) is common-phase rotation, not a transverse direction.

## Assumptions and scope
All vertices and edges are finite in number, all edge weights are strictly positive, and the underlying graph is connected. Each bipartition class has one constant weighted degree, but \(r\) and \(s\) need not be equal. A one-edge graph, stars, unweighted complete bipartite graphs, even regular cycles, and positive-weighted biregular examples are allowed. Vertices carry phases in \(\mathbb R/2\pi\mathbb Z\); updates are simultaneous, without a stochastic component. The claim concerns the explicitly described period-two branch only. “Attracting” means local exponential attraction after quotienting by uniform phase rotation, not global basin attraction.

## Proof
**1. Top eigenvalue and invariant colour plane.** Let \(L=D-A\) be the weighted Laplacian, with \(A\) the symmetric weighted adjacency matrix. Bipartite sign conjugation gives the irreducible nonnegative signless Laplacian \(D+A\), whose positive eigenvector takes values \(r\) on \(U\) and \(s\) on \(V\), with eigenvalue \(r+s=\Lambda\). Perron–Frobenius shows \(\Lambda\) is the simple largest Laplacian eigenvalue. Connectivity gives simple zero eigenvalue and strictly positive remaining eigenvalues.

Every colour-constant configuration remains colour-constant, since the incident weighted sums are \(r\) and \(s\). Denote the two colour phases by \(P,Q\), their difference by \(\delta=P-Q\), and the interaction by \(g(x)=\sin x+\frac15\sin3x\). Then \(\delta'=\delta+h\Lambda g(\delta)\). Since \(g(\pi+t)=-q(t)\), \(g(\pi-t)=q(t)\), the pair \(\delta_\pm=\pi\pm t\) is a genuine lifted two-cycle exactly when \(h\Lambda q(t)=2t\), equivalently \(h\Lambda=K(t)\). The weighted-degree identity \(|U|r=|V|s\) ensures the common arithmetic mean phase is unchanged; hence both colour configurations return exactly after two iterations, with no hidden common-phase drift. For \(0<t<\pi\) they are distinct modulo \(2\pi\).

**2. Global uniqueness of this branch.** The function \(q(t)=\frac45\sin t(1+\cos^2t)\) is positive on \((0,\pi)\), and \(K(t)=2t/q(t)\). Its derivative has the sign of \(q(t)-tq'(t)\). Write \(t_1=\arccos(1/\sqrt3)\) and \(t_3=\pi-t_1\). We show this difference is positive throughout \((0,\pi)\).

For \(0<t<t_1\), we have \(q''(t)=-\frac45\sin t(9\cos^2t-1)<0\), and \(q(0)=0\), whence \(q(t)-tq'(t)=-\int_0^t u q''(u)\,du>0\). On \((t_1,\pi/2)\) and \((t_3,\pi)\), \(q'<0\), so the inequality is immediate. On \((\pi/2,t_3)\), the derivative is positive, \(q(t)\ge q(\pi/2)=4/5\), and \(q'(t)\le8/45\), because the maximum of \(y(1-3y^2)\) on \([0,1/\sqrt3]\) occurs at \(y=1/3\). Also \(t<t_3<3\pi/4\). Therefore \(tq'(t)/q(t)\le\pi/6<1\). At the boundary values the inequality follows by continuity. Thus \(K\) increases strictly from \(K(0+)=5/4\) to infinity as \(t\to\pi-\). The branch exists uniquely for each \(h\Lambda>5/4\), within the specified ansatz.

**3. Full transverse multipliers and reentrance.** Every edge difference at either orbit point is \(\pm(\pi+t)\) or \(\pm(\pi-t)\), and the odd interaction has an even derivative with common value \(g'(\pi\pm t)=-q'(t)\). Thus the one-step Jacobian is the same at both points, \(J=I-hq'(t)L\), and the return derivative is \(J^2\). For \(q'(t)>0\), strict increase of \(K\) gives \(0<h\Lambda q'(t)=2tq'(t)/q(t)<2\). Every positive Laplacian eigenvalue satisfies \(0<\lambda_j\le\Lambda\), so \(-1<1-hq'(t)\lambda_j<1\), and all transverse return multipliers are strictly inside the unit circle. If \(q'(t)<0\), then \(1-hq'(t)\lambda_j>1\) for every nonzero mode, hence the two-cycle is a hyperbolic repeller. If \(q'(t)=0\), all return multipliers are one.

Finally, \(q'(t)=\frac45\cos t(3\cos^2t-1)\) is positive precisely on \((0,t_1)\cup(\pi/2,t_3)\), negative on \((t_1,\pi/2)\cup(t_3,\pi)\), and vanishes at the three separating points. Strict monotonicity of \(K\) translates those intervals into the four exact coupling thresholds. Direct evaluation yields \(K(t_1)=A_1\), \(K(\pi/2)=A_2\), and \(K(t_3)=A_3\). All claims follow. \(\square\)

## Verification
The standalone `verify_reentrant.py` uses Python 3 and NumPy. Running `python verify_reentrant.py` returned `VERIFY_OK graphs 4 amplitudes_per_graph 8 checked 32`. It checks the lifted orbit equation and every one-step eigenvalue against the explicit Laplacian formula on a single edge, \(K_{2,3}\), a weighted \(K_{2,2}\), and the six-cycle, at eight amplitudes spanning all four open regimes; it additionally samples 5,000 amplitudes for the scalar monotonicity inequality. The analytical proof above establishes the theorem for all admissible finite graphs and real couplings; finite tests alone do not.

## Relationship to prior work
Buescu, D'Aniello and Oliveira (2026) define the broad smooth-odd-interaction discrete Huygens network and prove its gradient/Lyapunov and Morse–Smale results in small-step regimes. Those results do not give the separated stability windows beyond the low-step regime for a first-plus-third-harmonic law. Buescu and Oliveira (2026) study pure-sine twisted states of rings. Related published results on weighted bipartite *pure-sine* phase networks prove local flip onset, and on biregular pure-sine networks a single attracting two-cycle window; they do not imply the return of attraction after an intervening repelling regime. A separate published higher-harmonic result proves a local \(\kappa=-1/27\) flip trichotomy for \(\sin t+\kappa\sin3t\), but explicitly stops short of global continuation of that period-two branch. The present theorem determines the complete continuation and four sharp stability thresholds for \(\kappa=1/5\) and every connected positively weighted biregular graph. It does not claim the graph spectral method or elementary flip theory as new.

## Limitations
This is a branchwise classification, not a classification of all two-cycles or all attractors. Local exponential stability does not imply global attraction. The three internal boundaries have neutral linear multipliers and their nonlinear critical dynamics is not decided. The fixed harmonic coefficient \(1/5\) makes the interaction factor explicitly; no claim is made about every possible third-harmonic coefficient or robustness bounds. Older specialized multiharmonic map calculations may contain equivalent results that were not recovered; independent mathematical validation and historical-priority certification have not been performed.

## References
1. J. Buescu, E. D'Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, submitted 2026-10-07, https://arxiv.org/abs/2610.10993.
2. J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1, submitted 2026-10-14, https://arxiv.org/abs/2610.19953.
3. *A harmonic-sign trichotomy and fourth-root flip at bipartite Huygens equilibria*, publicly accessible research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-harmonic-sign-trichotomy-and-fourth-root-flip-at-bipartite-huy--88b2989c3a50.
4. *Universal stable window and optimal decay of alternating cycles in biregular Huygens networks*, publicly accessible research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-stable-window-and-optimal-decay-of-alternating-cycles--bd570f026995.
5. *Sharp two-cycle threshold and critical decay on weighted bipartite phase networks*, publicly accessible research record, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-cycle-threshold-and-critical-decay-on-weighted-biparti--690fe2013b5e.
