# A single antipodal shortcut optimally reduces Kemeny transport on cycles

## Finding
Let \(C_n\) be the simple undirected unit-edge cycle on \(\mathbb Z/n\mathbb Z\), where \(n\ge4\). Add one previously absent edge between vertices separated by cyclic distance \(d\), where \(2\le d\le\lfloor n/2\rfloor\), and denote the resulting graph by \(G_{n,d}\). On each graph take the discrete-time simple random walk with transition probabilities \(P_{ij}=1/\deg(i)\) for adjacent \(i,j\), and let \(\mathcal K(G)=\sum_{\lambda\ne1}(1-\lambda)^{-1}\) be Kemeny's constant, with eigenvalues counted with multiplicity.

Write \(r=d(n-d)\). Then the exact transport change is
\[
\boxed{\mathcal K(G_{n,d})-\mathcal K(C_n)=
\frac{n^3-n+nr(n-2)-(n+4)r^2}{6(n+1)(n+r)}.}
\]
For all the stated \(n,d\) this quantity is strictly negative, and it is strictly decreasing as \(d\) increases from \(2\) to \(\lfloor n/2\rfloor\). Consequently the single-edge intervention minimizing Kemeny's constant is a chord joining vertices of maximum cyclic separation (unique up to cycle symmetry), and
\[
\min_{d}\frac{\mathcal K(G_{n,d})}{\mathcal K(C_n)}\longrightarrow\frac34
\qquad(n\to\infty).
\]
Thus the optimal added edge reduces the stationary-target mean hitting time by asymptotically one quarter; no added chord exhibits the Kemeny version of the Braess effect.

## Assumptions and scope
All edges have unit conductance; no self-loops, delays, or edge-weight retuning are introduced. The walk is discrete-time and chooses each neighboring vertex uniformly. The stationary distribution is proportional to vertex degree. Kemeny's constant is the expected first hitting time of a target sampled from that stationary distribution, taking hitting time zero when the target is the starting state. This is *not* a claim about the spectral-gap mixing time, all individual hitting times, arbitrary weighted chords, or graphs other than a cycle with exactly one new chord. The degree-two cycle walk may be periodic, but Kemeny's constant remains well defined.

## Proof
For a connected unit-resistance graph with \(m\) edges, vertex degrees \(w_i\), and effective resistances \(R_{ij}\), the standard commute-time identity and the random-target lemma give
\[
\mathcal K(G)=\frac1{2m}\sum_{i<j}w_iw_jR_{ij}.
\tag{1}
\]
Indeed, with \(\pi_i=w_i/(2m)\), random-target averaging is one half of the stationary-pair average commute time, and the commute time is \(2mR_{ij}\). For the cycle, \(R_{ij}=k(n-k)/n\) when \(k\) is either arc distance; therefore \(\mathcal K(C_n)=(n^2-1)/6\).

Rotate the cycle so the new edge is \(\{0,d\}\). Its pre-insertion effective resistance is \(R_{0d}=r/n\). Let \(v\) denote the potential for one unit of current injected at \(0\) and extracted at \(d\), normalized by \(v_d=0\). Kirchhoff's law yields
\[
v_i=\begin{cases}
(n-d)(d-i)/n,&0\le i\le d,\\
d(i-d)/n,&d\le i\le n-1.
\end{cases}
\]
Adding a unit-conductance \(0d\)-edge is a rank-one Laplacian update. The effective resistances after insertion satisfy
\[
R'_{ij}=R_{ij}-\frac{(v_i-v_j)^2}{1+r/n}.\tag{2}
\]
The new degree vector is \(w_i=2+\mathbf1_{i=0}+\mathbf1_{i=d}\), with \(\sum_iw_i=2(n+1)\). Summing the old-cycle resistances with these new degree weights gives
\[
S:=\sum_{i<j}w_iw_jR_{ij}
=\frac{n(n^2-1)}3+\frac{2(n^2-1)}3+\frac rn.\tag{3}
\]
The weighted potential mean is \(\bar v=(\sum_iw_iv_i)/(2n+2)=r/(2n)\). Two arithmetic-progression square sums along the two arcs give exactly
\[
V:=\sum_iw_i(v_i-\bar v)^2
=\left(\frac rn\right)^2\left(\frac n6+\frac{n}{3r}+\frac12\right).\tag{4}
\]
The elementary identity \(\sum_{i<j}w_iw_j(v_i-v_j)^2=(\sum_iw_i)V=2(n+1)V\), together with (1)--(4), gives
\[
\mathcal K(G_{n,d})=
\frac1{2(n+1)}\left(S-\frac{2(n+1)V}{1+r/n}\right).
\]
Subtract \((n^2-1)/6\) and simplify to obtain the boxed rational formula.

To prove the global sign and optimization, let
\[
A_n(r)=n^3-n+nr(n-2)-(n+4)r^2.
\]
The admissible range obeys \(r\ge2(n-2)\). At its left endpoint,
\[
A_n(2n-4)=-n^3-8n^2+55n-64<0\qquad(n\ge4),
\]
because it is already negative at \(n=4\) and strictly decreases thereafter. Moreover \(A_n'(r)=n(n-2)-2(n+4)r<0\) in the admissible range. Hence the boxed change is strictly negative. For strict decrease, differentiate the *whole quotient*: its derivative is
\[
\frac{\partial}{\partial r}\left(\mathcal K(G_{n,d})-\mathcal K(C_n)\right)
=-\frac{(n+4)r^2+2n(n+4)r+2n^2-n}{6(n+1)(n+r)^2}<0.\tag{5}
\]
Since \(d(n-d)\) strictly increases for integer \(2\le d\le\lfloor n/2\rfloor\), the longest chord is the strict minimizer among the distinct chord-distance classes.

For even \(n\), substituting \(r=n^2/4\) into the difference gives
\[
\mathcal K(G_{n,n/2})-\mathcal K(C_n)
=-\frac{(n-2)^2(n+2)^2}{24(n+1)(n+4)}.
\]
For odd \(n\) take \(r=(n^2-1)/4\). Both parity cases have difference \(-n^2/24+O(n)\) while the bare cycle constant is \(n^2/6+O(1)\). This proves the ratio limit \(3/4\).

## Verification
The standalone `code/verify.py` computes each chorded graph's exact Kemeny constant by rational Gaussian inversion of a grounded graph Laplacian and the weighted resistance sum (1). This is independent of the rank-one derivation above. It checked all 100 chord-distance cases for \(4\le n\le22\) with exact equality; it also tested the formula's sign and monotone ordering for all chord lengths through \(n=300\). The checks are finite corroboration of the analytic proof, not a substitute for it. Run `python3 code/verify.py` from the package directory; it requires no third-party packages.

## Relationship to prior work
Kirkland and Zeng introduced the Kemeny--Braess edge question and evaluated edge additions to *trees*, including path-to-lollipop families. Their general forest-counting identity also supplies a starting formula for arbitrary connected graphs, but their worked cycle occurs as an endpoint of the lollipop family, not as a cycle with an added chord. Pitman and Tang give general Kemeny forest formulas. Later work on Braess cliques and on random-graph thresholds treats different graph families. The present claim is the specific all-chord, exact-sign, optimizer, and sharp quarter-reduction law for a single-chord cycle. No claim of novelty is made for the general resistance or Kemeny identities.

## Limitations
Unknown, unindexed finite-network calculations may precede this explicit specialization, so bibliographic priority is provisional. A graph may have individual hitting times that increase despite the decrease of Kemeny's stationary-weighted average. The formula is not stated for continuous-time chains with fixed per-edge jump rates, for which normalization changes.

## References
- S. Kirkland and Z. Zeng, *Kemeny's Constant and an Analogue of Braess' Paradox for Trees*, Electronic Journal of Linear Algebra 31 (2016), 444--464, https://doi.org/10.13001/1081-3810.3222 . Full author-provided article text inspected.
- J. Pitman and W. Tang, *Tree formulas, mean first passage times and Kemeny's constant of a Markov chain*, arXiv:1603.09017 (first posted 2016-03-30), https://arxiv.org/abs/1603.09017 .
- J. Breen, E. deBlieck and K. N. Vander Meulen, *Kemeny's constant and Braess cliques in graphs*, arXiv:2608.04150, https://arxiv.org/abs/2608.04150 .
- M. Bodirsky, L. Ciardo and M. Kang, *The Kemeny--Braess Paradox in Random Graphs*, arXiv:2610.24143, https://arxiv.org/abs/2610.24143 .
