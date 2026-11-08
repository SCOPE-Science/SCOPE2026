# Exact hub persistence on clique bouquets and its size-biased blade law

## Finding

Let \(G(r_1,\ldots,r_k)\) consist of \(k\geq1\) private complete graphs of orders \(r_i\geq1\), each joined to the same hub \(h\), with no edges between different private groups. Set \(L=\sum_{i=1}^k r_i\). Initially the hub holds opinion \(1\) and all other vertices hold opinion \(0\). Under the ordinary binary voter model, every vertex at rate one copies a uniformly sampled neighbor. Let \(p(r_1,\ldots,r_k)\) denote the probability that the hub never changes its opinion before consensus.

For each integer \(r\geq1\) and \(t\geq0\), form the tridiagonal \(r\)-by-\(r\) matrix \(B_r(t)\), indexed by \(z=1,\ldots,r\), whose entries are
\[
\begin{aligned}
(B_r(t))_{z,z}&=z(2r-2z+1)/r+zt,\\
(B_r(t))_{z,z-1}&=-z(r-z+1)/r\quad(z\geq2),\\
(B_r(t))_{z,z+1}&=-z(r-z)/r\quad(z\leq r-1),
\end{aligned}
\]
with every other entry zero. Define \(D_r=(r!)^2/r^r\) and \(f_r(t)=D_r/\det B_r(t)\). Then the **exact finite-network persistence law** is
\[
\boxed{p(r_1,\ldots,r_k)=\prod_{i=1}^k f_{r_i}(1/L).}
\]

Furthermore, fix a positive integer \(R\). Uniformly over all private blade sizes \(1\leq r_i\leq R\), as \(L\to\infty\),
\[
\boxed{\log p(r_1,\ldots,r_k)=-\frac{\sum_i r_i^2}{L}+O_R(L^{-1}).}
\]
In particular, for \(k\) equal-sized private cliques of fixed size \(r\),
\[
\boxed{\lim_{k\to\infty}p(\underbrace{r,\ldots,r}_{k\text{ copies}})=e^{-r}.}
\]
The ratio \(\sum_i r_i^2/\sum_i r_i\) is the size-biased mean private clique size. It determines the limiting probability that the initially isolated opinion at the hub survives **without any hub reversal**.

The standard degree-weighted voter-model conservation law gives, for comparison, the probability of eventual all-\(1\) consensus:
\[
\Pr(\text{all-}1\text{ consensus})=\frac{L}{L+\sum_i r_i^2}.
\]
This last fixation identity is classical; the new claim concerns hub persistence, including the exact factorization and its asymptotic blade law.

## Assumptions and scope

All graphs are finite, undirected, unweighted and simple. Private blades may have unequal positive sizes, and each private blade is a clique. Each private vertex is adjacent to the hub and to every other vertex of its blade; no other edges occur. Each vertex independently updates at the points of a rate-one Poisson process, copying a uniformly chosen neighbor; the embedded jump chain has the same trajectory distribution as choosing one vertex uniformly at each discrete update. An update that copies an already-held opinion is not a change. The persistence event means that the hub retains its initial opinion at every instant through the almost-surely finite global consensus time. The assumption that all private vertices initially oppose the hub is essential to the stated product. The asymptotic estimate requires a fixed uniform upper bound on all blade sizes.

## Proof

**1. Freezing the hub until its first change.** Replace the hub by a permanently fixed opinion-\(1\) vertex and leave the independent private-vertex copying clocks unchanged. Let \(Z_i(s)\) count opinion-\(0\) vertices in blade \(i\) in this frozen-hub process. In the original process, prior to its first opinion change, a hub copying update changes its state exactly when it samples one of the \(\sum_iZ_i(s)\) opposing neighbors. The hub has degree \(L\). Mark the independent hub update stream by its chosen neighbor: each directed hub-to-private-vertex copying opportunity is a Poisson process of rate \(1/L\). Conditional on all private-vertex histories, the probability that no such opinion-changing hub update occurs before the frozen-hub process reaches all \(1\) is
\[
\exp\!\left[-\frac1L\sum_i\int_0^{T_i}Z_i(s)\,ds\right],
\]
where \(T_i\) is the absorption time of blade \(i\). No-op hub copying events may occur and do not matter. The frozen-hub blades use disjoint clocks and are independent. Once all blades reach opinion \(1\), the system is at consensus and the hub can never change. Thus the desired event is exactly the no-marked-opposing-copy event, and its probability factorizes into a product of Laplace transforms of the blade exposure areas.

**2. Exact one-blade transform.** In a frozen-hub private clique of size \(r\), the number \(Z(s)\) of opinion-\(0\) vertices is a birth-death chain with rates, for \(1\leq z\leq r\),
\[
 d_z=\frac{z(r-z+1)}r\quad(z\to z-1),\qquad
 u_z=\frac{z(r-z)}r\quad(z\to z+1),
\]
with \(u_r=0\) and zero absorbing. Its absorption time \(T_0\) is finite almost surely, because this is a finite continuous-time chain with a path of positive-rate downward transitions from every nonzero state. Put
\[
 F_z(t)=\mathbb E_z\exp\!\left(-t\int_0^{T_0}Z(s)\,ds\right),\quad F_0(t)=1.
\]
First-step conditioning, equivalently the finite-state Feynman–Kac equation, yields
\[
 (d_z+u_z+zt)F_z(t)=d_zF_{z-1}(t)+u_zF_{z+1}(t).
\]
The linear system on indices \(1,\ldots,r\) is \(B_r(t)F=d_1e_1\). For \(t\ge0\), the killed-chain resolvent is invertible. Cramer's rule for this tridiagonal matrix gives
\[
 F_r(t)=\frac{\prod_{z=1}^r d_z}{\det B_r(t)}=
 \frac{(r!)^2/r^r}{\det B_r(t)}=f_r(t).
\]
Each blade begins at \(z=r_i\); inserting \(t=1/L\) into the factorization from step 1 proves the exact finite law.

**3. The size-biased limit.** The generator acting on the coordinate function \(z\) satisfies
\[
 (\mathcal L z)(z)=u_z-d_z=-z/r.
\]
Consequently \(\mathbb E_r Z(s)=re^{-s/r}\), and Tonelli's theorem gives the exact integrated exposure expectation
\[
 \mathbb E_r\int_0^{T_0}Z(s)\,ds=\int_0^\infty re^{-s/r}\,ds=r^2.
\]
For each fixed \(r\), the absorption time of the finite birth-death chain has a finite second moment, so the exposure area also has a finite second moment. Taylor's theorem for the Laplace transform gives \(\log f_r(t)=-r^2t+O_r(t^2)\) as \(t\downarrow0\). When every \(r_i\le R\), the constants are uniform over the finite set \(1\le r\le R\). Taking \(t=1/L\), summing over blades and using \(k\le L\) gives
\[
 \log p=-\frac{\sum_i r_i^2}{L}+O_R(k/L^2)=-\frac{\sum_i r_i^2}{L}+O_R(L^{-1}),
\]
as claimed. Equal-sized blades give the limit \(e^{-r}\).

**4. Classical fixation comparison.** The degree-weighted proportion of opinion \(1\) is a bounded martingale for the voter model on any finite undirected graph. At absorption it equals either zero or one. Initially only the hub is opinion \(1\); its degree is \(L\), while the sum of all private-vertex degrees is \(\sum_i r_i^2\). Optional stopping therefore yields the displayed fixation probability. It is not the no-flip event: the hub may change and later return to its initial opinion.

## Verification

The determinant formula gives \(f_1(t)=1/(1+t)\), \(f_2(t)=1/(1+4t+2t^2)\), and \(f_3(t)=2/(2+18t+27t^2+9t^3)\). Hence a star with \(L\) private leaves has persistence \((1+1/L)^{-L}\to e^{-1}\); pairing those \(L\) leaves into \(L/2\) private edges (for even \(L\)) changes the probability to \((1+4/L+2/L^2)^{-L/2}\to e^{-2}\). Both graphs have the same number of vertices and the same hub degree; adding edges *only among peripheral vertices* changes the persistent-hub limit.

The accompanying program `verification/check_birth_death.py` checks exact symbolic Laplace transforms, determinant identities and exposure derivatives for blade sizes through six, together with the fixed-size limits. The independently implemented program `verification/check_full_state.py` constructs the full labelled-state killed generator, solves its Dirichlet equations and compares with the analytic formula for all 40 tested blade compositions of total size at most eight with private sizes at most three. Both programs pass; their saved standard outputs and the required Python packages are included. These finite computations are cross-checks, not replacements for the argument in the Proof section.

## Relationship to prior work

Ben-Naim, Frachebourg and Krapivsky introduced zero-opinion-change persistence in the voter model, studying lattice and complete-graph temporal statistics, not the present absorption-stopped hub probability on clique bouquets. Sood, Antal and Redner established the degree-weighted conservation law and, in particular, the star's probability of eventual consensus, which is reused solely as the classical fixation comparison. Iwamasa and Masuda studied consensus-time extremizers for voter, link and invasion updates on lollipop, barbell and double-star networks, rather than no-flip paths in the present graph family. The present finite factorization and size-biased limit are not obtained from those specific published statements. The derivation uses standard finite-state Feynman–Kac and Poisson thinning; its contribution is their explicit structural evaluation for this natural family. Literature searches did not identify a theorem implying exactly these evaluated formulas, but cannot certify worldwide priority.

## Limitations

The exact formula assumes one initially different hub and otherwise unanimous opposing vertices, and the usual voter copying rule. The asymptotic estimate holds when private clique sizes are uniformly bounded; it is not asserted for clique sizes increasing without bound. The proof does not compute persistence for arbitrary mixed initial blade configurations, the absorption-time law, or the entire distribution of numbers of hub reversals. Finite numerical checks validate cases and arithmetic only. Independent scientific verification has not been performed.

## References

1. E. Ben-Naim, L. Frachebourg, and P. L. Krapivsky, *Coarsening and Persistence in the Voter Model*, arXiv:cond-mat/9511040v1 (public 1995-11-08); *Physical Review E* **53** (1996), 3078–3087, DOI: 10.1103/PhysRevE.53.3078.
2. V. Sood, T. Antal, and S. Redner, *Voter Models on Heterogeneous Networks*, arXiv:0712.4288 (public 2007-12-27); *Physical Review E* **77** (2008), 041121, DOI: 10.1103/PhysRevE.77.041121.
3. Y. Iwamasa and N. Masuda, *Networks maximizing the consensus time of voter models*, arXiv:1404.6360 (public 2014-04-25); *Physical Review E* **90** (2014), 012816, DOI: 10.1103/PhysRevE.90.012816.
