# Complete dynamical sectors and sector-resolved currents in long-jump exclusion

## Finding

For the fixed-step exclusion process of Nhung, Nguyen Ngoc and Thi, every finite marked-particle state belongs either to a frozen singleton or to a fully irreducible active class. The classes have explicit arithmetic labels and an exact finite-size current.

Let a periodic ring have \(L>N\ge2\) sites and \(N\) particles, and fix an integer jump length \(1\le I<L\). In particle order let \(g_i\ge1\) be the headway between particle \(i\) and the next one; write \(h_i=g_i-1\), so \(\sum_i h_i=L-N=:H\). Mark particle \(0\) and write its location \(z\in\mathbb Z/L\mathbb Z\). Set
\[
r_i=h_i\bmod I,\qquad q_i=(h_i-r_i)/I,\qquad
Q=\sum_{i=0}^{N-1}q_i,\qquad d=\gcd(L,I).
\]
Every \(r_i\) belongs to \(\{0,\ldots,I-1\}\).

**Classification.** If \(Q=0\), the state is frozen and its communicating class is the singleton \((z,r)\). If \(Q\ge1\), its complete communicating class consists exactly of the marked configurations with the same ordered residue vector \(r=(r_0,\ldots,r_{N-1})\) and \(z\bmod d\). Its cardinality is
\[
\frac{L}{d}\binom{Q+N-1}{N-1}.
\]
This remains true for purely one-way hopping.

**Stationary current.** Write \(w_i(k)=\exp(J_{1+r_i+Ik})\) and
\[
Z_{r,Q}=[t^Q]\prod_{i=0}^{N-1}
 \left(\sum_{k\ge0}w_i(k)t^k\right),\qquad Z_{r,-1}=0.
\]
In every active class the unique stationary law assigns probability proportional to \(\prod_i w_i(q_i)\), independently of the allowed marked-particle phase. The net stationary particle current per lattice bond is exactly
\[
\boxed{\mathcal J_{r,Q}=\frac{NI}{L}(a-b)\frac{Z_{r,Q-1}}{Z_{r,Q}}}
\quad(Q\ge1),
\]
and is zero for \(Q=0\), where \(a,b\ge0\), \(a+b>0\), are the bare right and left rates.

**Frozen and flowing states coexist** at the same \(L,N,I\), with \(a>b\), if and only if
\[
I\le L-N\le N(I-1).
\]
Equivalently, at fixed particle number and jump length, an active configuration exists when \(L-N\ge I\), while some frozen configuration exists when \(L\le NI\).

## Assumptions and scope

A jump of particle \(i\) by \(I\) sites to the right requires all \(I\) sites ahead to be unoccupied, equivalently \(h_i\ge I\). It sends \(h_i\mapsto h_i-I\) and \(h_{i-1}\mapsto h_{i-1}+I\), with indices modulo \(N\). A left jump similarly moves \(I\) units of surplus gap from \(h_{i-1}\) to \(h_i\). The rates are respectively
\[
a\exp(J_{g_i-I}-J_{g_i}),\qquad
b\exp(J_{g_{i-1}-I}-J_{g_{i-1}}).
\]
Here \(J_g\) is any finite real finite-range headway potential, in particular with the zero conventions of the cited model. The marked particle moves its coordinate \(z\) only when particle \(0\) jumps, by the signed distance \(I\). Marking a particle is a bookkeeping lift of the original unlabelled ring system; the physical current is unchanged. There is no overtaking. At least one hopping direction must have strictly positive bare rate. The infinite formal generating series is used only to extract the finite coefficient \(Z_{r,Q}\).

"Current per bond" means the stationary expected net number of signed particle crossings of any fixed oriented bond per unit time, with a length-\(I\) hop contributing one crossing at each of its \(I\) traversed bonds.

## Proof

**1. Arithmetic invariants.** A right jump transfers precisely one unit of \(q_i\) to \(q_{i-1}\), and a left jump transfers one unit in the opposite direction; the residues \(r_i\) never change. Each displacement of the marked coordinate is a multiple of \(I\), so \(z\bmod d\) is also conserved. If \(Q=0\), every surplus gap is at most \(I-1\); neither direction is possible and the state is an absorbing singleton.

**2. Irreducibility for \(Q\ge1\).** Each positive-rate direction implements unit-mass transport of the \(Q\) indistinguishable quanta on a directed \(N\)-cycle. Since the cycle is strongly connected, any weak composition \(q\) of \(Q\) can be transformed into any other by transporting individual quanta around directed paths. It remains to connect the possible marked positions. Starting with any \(q\) and selecting one existing quantum, send that quantum once around the gap cycle, using the positive-rate direction. This restores the entire vector \(q\), makes exactly one jump of every particle, and moves \(z\) by \(+I\) for right transfers (or \(-I\) for left transfers). Iterating the cycle produces every phase congruent to \(z\bmod d\), because \(I\) generates the subgroup of \(\mathbb Z/L\mathbb Z\) of size \(L/d\). One can first change the composition and then adjust the phase. These moves prove that the conserved labels are complete even with strictly unidirectional rates. The stars-and-bars count of \(Q\)-compositions gives the class size.

**3. Stationarity and uniqueness.** For a fixed class set
\[
\pi(z,q)=\frac{\prod_iw_i(q_i)}{(L/d)\,Z_{r,Q}},
\]
where \(z\) ranges over the permitted congruence class. For a right transfer out of coordinate \(i\), the unnormalised stationary flux equals
\[
a\,{\bf1}_{q_i\ge1}\,
w_i(q_i-1)\prod_{j\ne i}w_j(q_j).
\]
The same expression is the flux *into* the configuration by a right transfer from coordinate \(i+1\) to coordinate \(i\): the predecessor has \(q_i-1\) and \(q_{i+1}+1\), and its rate cancels the latter site's added weight. Summation over \(i\) therefore balances all right-going in- and out-fluxes. The same cyclic argument balances the left-going fluxes separately, including transitions that shift \(z\); for each destination phase the predecessor phase is unique and is in the same residue class. Hence \(\pi\) is stationary for arbitrary \(a,b\). Finite irreducibility from step 2 implies uniqueness.

**4. Exact current.** Under \(\pi\), the expected sum of all right jump rates is
\[
a\,\mathbb E_\pi\!\left[
\sum_i{\bf1}_{q_i\ge1}\frac{w_i(q_i-1)}{w_i(q_i)}\right]
=aN\frac{Z_{r,Q-1}}{Z_{r,Q}}.
\]
Indeed, in each summand replace the summation index \(q_i\) by \(q_i-1\): the remaining product has total degree \(Q-1\). Likewise the expected total left jump rate is \(bN Z_{r,Q-1}/Z_{r,Q}\). Each jump traverses \(I\) oriented bonds. Stationarity and local conservation force the average net flow to be the same at every bond, even though a single communicating class need not be invariant under spatial translation. Dividing the total signed bond crossings by \(L\) proves the displayed current formula. All \(w_i(k)>0\) and \(Z_{r,Q-1}>0\) for \(Q\ge1\), so its sign is exactly that of \(a-b\).

**5. Coexistence criterion.** A frozen surplus-gap vector has all \(0\le h_i\le I-1\); such vectors exist with sum \(H\) exactly when \(H\le N(I-1)\). An active vector exists precisely when \(H\ge I\), because then at least one \(h_i\) can contain an entire jump length. Both descriptions can hold at the same \(N,L,I\) exactly on the stated interval. For instance, at \(N=3,L=6,I=2\), the surplus gaps \((1,1,1)\) are frozen while \((2,1,0)\) are active. If \(J_g\equiv0\) and \((a,b)=(1,0)\), the active class has \(Q=1\), \(Z_{r,1}=3\), \(Z_{r,0}=1\), and current \(1/3\), while the frozen class has current zero. This realizes opposite dynamical outcomes at the same density \(1/2\).

## Verification

Run `python verify.py` with Python 3 (standard library only). The checker constructs the complete marked-state finite generator, computes its strongly connected components without assumptions about irreducibility, and compares each to the proposed arithmetic class. It independently tests global stationary balance using exact rational weights and rates, and checks both sides of the current identity with exact fractions. The tested range is \(2\le N\le4\), \(N+1\le L\le10\), \(1\le I\le3\) with \(I<L\), in each of three drive regimes: right-only, left-only, and asymmetric bidirectional. This covers 186 finite generators, 28,413 marked states, and 3,444 communicating-class balance/current checks. The finite tests do not replace the all-size proof.

## Relationship to prior work

Nhung, Nguyen Ngoc and Thi, arXiv:2604.01796v1 (2 April 2026), supply the long-jump headway dynamics, their Gibbs stationary measure (Theorem II.1), and the canonical/thermodynamic current framework (Section III). Those statements establish one stationary mixture, not the complete list of closed communicating classes or an exact *individual-class* current. Here the modular gap residues and the marked phase are dynamical invariants, and the conditional canonical partition functions separate active phases from frozen ones. In particular, a global Gibbs average over closed classes does not imply identical currents from different initial classes.

The mass-transport and zero-range literature, including arXiv:1011.3110, supplies related methods for multiple-chipping models; the present statement concerns the exact finite-ring tagged exclusion lift, its full arithmetic classification, and a source-specific stationary transport formula. No claim is made that unit-mass zero-range irreducibility or canonical coefficient extraction by themselves are new.

## Limitations

The result is for finite periodic rings with fixed jump length and positive Arrhenius factors, not open reservoirs, overtaking particles, or mixed jump lengths. Its classes use a marked particle; when the mark is forgotten, cyclic relabelling can identify several marked classes. The invariant Gibbs measure from the primary paper may be a mixture across classes; therefore its thermodynamic current does not automatically describe an arbitrary deterministic initial configuration. This classification does not establish convergence rates or thermodynamic limits for each sequence of residue classes. Related multiple-chipping literature may contain implicit equivalent invariants not exposed in the accessible abstract.

## References

1. L. T. Nhung, N. P. Nguyen Ngoc and H. A. Thi, *Invariant measures of exclusion processes with a look-ahead rule*, arXiv:2604.01796v1, publicly posted 2 April 2026. https://arxiv.org/html/2604.01796v1.
2. *Mass-Transport Models with Multiple-Chipping Processes*, arXiv:1011.3110, 2010. https://arxiv.org/abs/1011.3110. Only the abstract was available during the comparison.
