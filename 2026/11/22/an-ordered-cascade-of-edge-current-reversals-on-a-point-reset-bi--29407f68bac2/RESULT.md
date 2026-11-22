# An ordered cascade of edge-current reversals on a point-reset biased Markov ring

## Finding

For every integer \(n\ge3\), a clockwise-biased nearest-neighbor Markov walk on an \(n\)-site cycle with Poisson resetting to site \(0\) has exactly \(\lfloor n/2\rfloor\) distinct positive resetting rates at which a local **hopping-only** stationary current reverses direction. No other hopping-current reversals occur. Every reversal is simple, and increasing the reset rate creates a contiguous counterclockwise-current arc from the edge entering site \(0\), one edge at a time.

More precisely, fix clockwise hopping rate \(p>q>0\), counterclockwise hopping rate \(q\), and resetting rate \(r>0\). Let \(\pi_j(r)\) denote the stationary probability at site \(j\in\{0,\ldots,n-1\}\), and set
\[
J_j(r)=p\pi_j(r)-q\pi_{j+1\pmod n}(r),\quad 0\le j<n.
\]
Then \(J_j(r)>0\) for all \(r>0\) when \(0\le j\le\lfloor(n-1)/2\rfloor\). For every \(\lceil n/2\rceil\le j\le n-1\), there is exactly one \(r_j>0\) for which \(J_j(r_j)=0\), with \(J_j>0\) below and \(J_j<0\) above that rate. The thresholds obey
\[
0<r_{n-1}<r_{n-2}<\cdots<r_{\lceil n/2\rceil}.
\]
For fixed \(q>0\) and weak positive bias \(\delta=p-q\downarrow0\),
\[
r_j=\frac{2\delta}{2j+1-n}+O(\delta^2/q),\qquad \lceil n/2\rceil\le j<n.
\]

## Assumptions and scope

The state space is \(\mathbb Z/n\mathbb Z\), with \(n\ge3\). Hopping to the clockwise neighbor occurs with rate \(p>q>0\); hopping to the counterclockwise neighbor occurs with rate \(q\). An independent rate-\(r\) Poisson clock teleports the particle from every state to site \(0\), including ineffective events when already at site \(0\). The finite irreducible continuous-time chain has a unique stationary distribution. Currents \(J_j\) count only the original nearest-neighbor hopping transitions, *not* the teleporting reset transitions. In particular these local currents need not be constant across the cycle. The theorem is not a statement about a convention-dependent conserved current obtained by assigning paths to reset jumps.

## Proof

**Stationary recurrence.** Off the reset site, the master equation is
\[
p\pi_{j-1}+q\pi_{j+1}-(p+q+r)\pi_j=0\qquad(1\le j<n).
\]
Let \(s=p+q+r\) and introduce two positive characteristic roots
\[
x=\frac{2p}{s+\sqrt{s^2-4pq}},\qquad y=\frac{p}{qx}.
\]
Since \(p>q>0\) and \(r>0\), \(0<x<1<y\), and \(x,y\) are the roots of \(qz^2-sz+p=0\). The periodic recurrence through \(j=n-1\) gives a positive stationary profile
\[
\pi_j=C\left(\frac{x^j}{1-x^n}+\frac{y^j}{y^n-1}\right),\qquad C>0,
\]
where \(C\) normalizes the sum. The recurrence holds at every nonreset site. Since the stationary master equations sum to zero, the equation at site \(0\) follows automatically. Thus this is the unique stationary distribution.

**Exact sign ratio.** Put \(h=p/q>1\), so \(y=h/x\). The positive \(x\)-root contribution to \(J_j\) is \(C x^j(p-qx)/(1-x^n)\), whereas its negative \(y\)-root contribution is \(C y^j(p-qy)/(y^n-1)\). Their absolute ratio is
\[
R_j(x,h)=\frac{h^{j+1}x^{n-2j-1}(1-x)(1-x^n)}{(h-x)(h^n-x^n)},\qquad
\operatorname{sgn}J_j=\operatorname{sgn}(1-R_j).
\]
All factors shown are positive. For fixed \(h>1\), \(x\) strictly decreases from \(1\) to \(0\) as \(r\) increases from \(0\) to infinity.

**Permanent positive half.** Write \(R_j=x^{n-2j-1}F_j\), where
\[
F_j(h,x)=\frac{h^{j+1}(1-x)(1-x^n)}{(h-x)(h^n-x^n)}.
\]
For every \(0<x<1\), \(F_j(1,x)=1\), while for all \(0\le j<n\) and \(h>1\),
\[
\partial_h\log F_j=\frac{j+1}{h}-\frac1{h-x}-\frac{nh^{n-1}}{h^n-x^n}
<\frac{j+1-n}{h}-\frac1{h-x}<0.
\]
Hence \(F_j<1\). If \(j\le\lfloor(n-1)/2\rfloor\), the exponent \(n-2j-1\ge0\), whence \(R_j<1\) and \(J_j>0\) for all positive reset rates.

**Single crossing on each remaining edge.** For \(j\ge\lceil n/2\rceil\), the exponent \(n-2j-1<0\), and
\[
\partial_x\log R_j=\frac{n-2j-1}{x}
+\left(-\frac1{1-x}+\frac1{h-x}\right)
+nx^{n-1}\left(-\frac1{1-x^n}+\frac1{h^n-x^n}\right)<0.
\]
Each displayed group is strictly negative because \(h>1\). Thus \(R_j\) increases strictly with \(r\). Its limits are \(0\) as \(r\downarrow0\) and infinity as \(r\to\infty\); continuity gives exactly one zero of \(1-R_j\), with strict derivative. Furthermore,
\[
\frac{R_{j+1}}{R_j}=\frac{h}{x^2}>1.
\]
Consequently the outermost edge \(j=n-1\) crosses first, and the thresholds are strictly ordered as claimed.

**Weak-bias thresholds.** Let \(\delta=p-q\) and hold \(q>0\) fixed. At \((\delta,r)=(0,0)\) the stationary law is uniform; analytic dependence of a finite-state stationary distribution yields
\[
J_j(\delta,r)=\frac{\delta}{n}+\frac{n-1-2j}{2n}r
+O((|\delta|+r)^2/q).
\]
The linear coefficient of \(r\) at \(\delta=0\) also follows directly from stationary conservation \(J_j-J_{j-1}=-r\pi_j\) away from site \(0\), together with \(\sum_jJ_j=0\) when \(p=q\). For \(j\ge\lceil n/2\rceil\), the coefficient is strictly negative, so the implicit-function theorem and the proven global uniqueness give the stated expansion.

## Verification

The accompanying standalone `verify_cascade.py` reconstructs independent stationary distributions by exact rational Gaussian elimination, checks the recurrence-derived root profile and current signs over multiple finite cycles and rates, and bisects the predicted critical rates. It passed 180 rational test families and independent rate and asymptotic comparisons. The verified three thresholds for \(n=6\), \(p=3/2\), \(q=1\), for edges \(j=5,4,3\) respectively, are approximately \(0.226733124762\), \(0.484739267504\), and \(3.435620322242\). These finite checks support but do not replace the analytic argument for all \(n\ge3\).

Run with `python verify_cascade.py` using Python 3's standard library; no data files or third-party packages are required.

## Relationship to prior work

Rose, Touchette, Lesanovsky and Garrahan (2018) derive a general spectral formula for reset-chain stationary probabilities and a decomposition of link currents. Their exact periodic example is *totally* asymmetric, \(q=0\), so it cannot display the counterflow regime requiring both rates positive. Their general formula provides foundational resolvent machinery, not the simultaneous all-size uniqueness and ordering inequalities proved here. Riascos and colleagues (2019) derive network resetting formulas and investigate undirected walks; their results do not identify directional local hopping-current reversals on a biased cycle. Tucci and colleagues (2020) clarify why the resetting contribution to a **conserved** ring current depends on the chosen resetting path; this result deliberately isolates the unambiguous hopping-only component instead. Sarkar and Gupta (2022) address bias and resetting on comb networks with returns from branches to backbone nodes rather than a single reset destination on a homogeneous ring. Li and Sun (2025) give general biased-network stationary and first-passage formulas; their accessible published summary does not establish the present all-edge reversal staircase, but a full-text comparison remains a priority risk.

## Limitations

The theorem assumes homogeneous nearest-neighbor hopping, one complete-reset destination, \(p>q>0\), and finite cycle size. The strict threshold sequence need not persist for site-dependent rates, distributed reset sites, non-Poisson reset clocks, or interactions among multiple walkers. The reversal is a property of physical nearest-neighbor hopping counts, not a sign reversal of an arbitrarily routed total reset-plus-hop current. The general resolvent literature can implicitly reproduce model-specific probability expressions; publication priority for the new monotonicity theorem remains subject to independent specialist review. No independent mathematical audit or experimental validation is claimed.

## References

1. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (first public 2018-06-04), https://arxiv.org/abs/1806.01298.
2. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568 (2019), https://arxiv.org/abs/1910.13568.
3. G. Tucci, A. Gambassi, S. Gupta and É. Roldán, *Controlling particle currents with evaporation and resetting from an interval*, arXiv:2005.05173 (2020), https://arxiv.org/abs/2005.05173.
4. M. Sarkar and S. Gupta, *Biased random walk on random networks in presence of stochastic resetting: Exact results*, arXiv:2205.15232 (2022), https://arxiv.org/abs/2205.15232.
5. A. Li and X. Sun, *Biased random walks on networks with stochastic resetting*, Physical Review E 111, 054309 (2025), https://doi.org/10.1103/PhysRevE.111.054309.
