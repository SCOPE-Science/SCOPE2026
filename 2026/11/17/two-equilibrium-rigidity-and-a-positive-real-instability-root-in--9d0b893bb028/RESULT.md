# Two-equilibrium rigidity and a positive real instability root in common-latency phage cocktails

## Finding

**Theorem.** For every finite number \(n\geq1\) of phage types, the Bardina–Cano–Cuadrado coinfection delay system with a **common positive latency** has either at most two strictly positive coexistence equilibria or, in one explicitly characterized degenerate case, an entire one-parameter family. The upper bound two is attained with strictly positive biological parameters for **every** \(n\geq2\). Whenever two such equilibria exist, the one with smaller susceptible-bacterial population has a **strictly positive real characteristic exponent**, hence is linearly unstable for the actual biologically compatible delay dynamics. No assertion is made about stability of the larger equilibrium.

More generally, at any positive coexistence equilibrium with susceptible population \(s\), the sign of the characteristic determinant at zero is exactly the sign of the derivative of the scalar equilibrium function:
\[
\boxed{\Delta_s(0)=\mu s\left(\prod_{i=1}^{n}(m_i+A_i s)\right)F'(s).}
\]
Thus \(F'(s)<0\) is a delay-equation instability certificate, \(F'(s)=0\) forces a zero characteristic root, and the real-root conclusion does not require a small-delay approximation.

## Assumptions and scope

Fix a finite integer \(n\geq1\). Let the bacterial growth and death rates \(\alpha,\mu>0\), latency \(\tau>0\), and for every phage type \(i\), adsorption coefficients \(k_i,h_i>0\), decay \(m_i>0\), burst size \(b_i>0\), and constant dose \(d_i>0\). All phage types have the same latency \(\tau\); no equality of their remaining parameters is assumed. Use the notation \(S,I,Q_i\) for susceptible bacteria, infected bacteria, and free phage concentrations. The equations are
\[
\begin{aligned}
\dot S(t)&=S(t)\left(\alpha-\sum_{i=1}^{n}k_iQ_i(t)\right),\\
\dot I(t)&=S(t)\sum_{i=1}^{n}k_iQ_i(t)-\mu I(t)
 -E S(t-\tau)\sum_{i=1}^{n}k_iQ_i(t-\tau),\\
\dot Q_i(t)&=d_i-m_iQ_i(t)-k_iQ_i(t)S(t)-h_iQ_i(t)I(t)
 +k_i b_i E Q_i(t-\tau)S(t-\tau),\\
E&=e^{-\mu\tau}\in(0,1).
\end{aligned}
\]
As in the motivating model, compatible histories obey the infected-population identity
\[
 I(t)=\sum_{i=1}^{n}k_i\int_{t-\tau}^{t}e^{-\mu(t-u)}Q_i(u)S(u)\,du.
\]
A *positive coexistence equilibrium* means constant \(S=s>0\), \(I>0\), and every \(Q_i>0\), with this identity satisfied. Define
\[
 c=\frac{\alpha(1-E)}{\mu},\quad A_i=k_i(1-b_iE)+h_i c,\quad
 a_i(s)=m_i+A_i s,
\]
\[
 D=\{s>0:a_i(s)>0\text{ for all }i\},\qquad
 F(s)=\sum_{i=1}^{n}\frac{k_i d_i}{a_i(s)}\quad(s\in D).
\]
The set \(D\) is one interval beginning at zero; it is either \((0,\infty)\) or \((0,R)\) for some \(R>0\). The characteristic determinant \(\Delta_s(\lambda)\) is taken for the full \((n+2)\)-dimensional linearized retarded system, ordered \((S,I,Q_1,\ldots,Q_n)\), and normalized as \(\det(\lambda\mathrm{Id}-J_0-e^{-\lambda\tau}J_\tau)\).

## Proof

**1. Exact reduction and complete equilibrium census.** At a positive equilibrium, the first equation forces \(\sum_i k_iQ_i=\alpha\). The infected-population identity gives \(I=cs\). Each phage equation then gives \(d_i=Q_i[m_i+(k_i+h_i c-k_i b_i E)s]=Q_i a_i(s)\), hence \(Q_i=d_i/a_i(s)\). Thus every positive equilibrium arises uniquely from a root \(F(s)=\alpha\) in \(D\); conversely, any such root generates the positive equilibrium
\[
 (S,I,Q_1,\ldots,Q_n)=\left(s,cs,\frac{d_1}{a_1(s)},\ldots,\frac{d_n}{a_n(s)}\right).
\]
On the entire interval \(D\),
\[
 F'(s)=-\sum_i\frac{k_i d_i A_i}{a_i(s)^2},\qquad
 F''(s)=2\sum_i\frac{k_i d_i A_i^2}{a_i(s)^3}.
\]
If any \(A_i\ne0\), all denominators are positive and \(F''(s)>0\) on \(D\). Hence \(F'\) is strictly increasing, and a horizontal line meets \(F\) at most twice (otherwise Rolle's theorem would give two distinct zeros of \(F'\)). If all \(A_i=0\), then \(F(s)=\sum_i k_i d_i/m_i\) for every \(s>0\). In that and only that case there is a continuum of equilibria if \(\alpha=\sum_i k_i d_i/m_i\), and none otherwise. If two roots \(s_-<s_+\) exist in the nondegenerate case, strict convexity and the mean value theorem force \(F'(s_-)<0<F'(s_+)\).

**2. Zero-frequency characteristic identity.** Write \(q_i=d_i/a_i(s)\). The characteristic matrix at real frequency zero has first two rows
\[
 (0,0,s k_1,\ldots,s k_n),\qquad
 (-\alpha(1-E),\mu,-s k_1(1-E),\ldots,-s k_n(1-E)),
\]
and for each phage row, the nonzero entries are \(k_iq_i(1-b_iE)\) in the \(S\) column, \(h_iq_i\) in the \(I\) column, and \(a_i(s)\) in its own phage column. Add \((1-E)\) times the first row to the second. Then use that second row to eliminate the \(I\) entry of every phage row. The remaining phage rows have first entry \(A_i q_i\) and phage diagonal \(a_i(s)\). Expanding along the \(I\) column and taking the Schur complement of the positive diagonal block gives
\[
 \Delta_s(0)=-\mu s\left(\prod_i a_i(s)\right)
             \sum_i\frac{k_iq_i A_i}{a_i(s)}
           =\mu s\left(\prod_i a_i(s)\right)F'(s).
\]
This is an identity for the **unmodified** retarded differential equations and their prescribed characteristic determinant, not a quasisteady approximation.

For real \(\lambda\ge0\), \(\Delta_s(\lambda)\) is real and continuous. Since \(e^{-\lambda\tau}\to0\) and the characteristic matrix is \(\lambda\mathrm{Id}+O(1)\),
\[
 \lim_{\lambda\to+\infty}\frac{\Delta_s(\lambda)}{\lambda^{n+2}}=1.
\]
Whenever \(F'(s)<0\), the identity gives \(\Delta_s(0)<0\), while \(\Delta_s(\lambda)>0\) for all sufficiently large positive real \(\lambda\). The intermediate value theorem yields a real \(\lambda_*>0\) with \(\Delta_s(\lambda_*)=0\).

The eigenmode is compatible with the infected-bacteria history constraint: for an exponential perturbation with rate \(\lambda_*>0\), the linearized infected equation implies
\[
 \delta I=\left(\sum_i k_i(q_i\delta S+s\delta Q_i)\right)
 \frac{1-e^{-(\mu+\lambda_*)\tau}}{\mu+\lambda_*},
\]
which equals the linearization of the required history integral. As the equilibrium is strictly positive, small compatible perturbations in this eigendirection preserve positivity of the histories. A positive real characteristic exponent therefore proves physical linear instability. For the lower root \(s_-\), the strict convexity result above gives \(F'(s_-)<0\) and proves the asserted instability. If \(F'(s)=0\), the determinant identity instead gives a zero characteristic exponent, without deciding nonlinear stability.

**3. Sharpness for every cocktail size.** Choose \(\alpha=\mu=1\), \(\tau=\log 2\), and for types \(1,2\), let \(k_i=m_i=1\), \(h_i=2\), with burst sizes \((b_1,b_2)=(2,6)\) and doses \((d_1,d_2)=(1,1/16)\). Then \(E=c=1/2\), \((A_1,A_2)=(1,-1)\), \(D=(0,1)\), and
\[
 F(s)=\frac{1}{1+s}+\frac{1}{16(1-s)}.
\]
The equation \(F(s)=1\) is \(16s^2-15s+1=0\), with two distinct roots
\[
 s_\pm=\frac{15\pm\sqrt{161}}{32}\in(0,1).
\]
For every \(n\ge3\), add \(n-2\) types with \(k_i=m_i=1\), \(h_i=2\), \(b_i=4\), and \(d_i=1/[64(n-2)]\). These have \(A_i=0\), and the new function is
\[
 F_n(s)=\frac{1}{1+s}+\frac{1}{16(1-s)}+\frac1{64},\quad s\in(0,1).
\]
Here \(F_n(0)=69/64>1\), \(F_n(3/5)=51/64<1\), and \(F_n(s)\to\infty\) as \(s\uparrow1\), so continuity gives two roots in \(D\), and strict convexity proves these are the only ones. Both are simple and therefore persist under small perturbations of all model parameters, allowing every appended coefficient \(A_i\) to become nonzero if desired. The case \(n=2\) also has two simple roots. This completes the proof.

## Verification

Run \(\texttt{python3 verify.py}\) with the adjacent standard-library-only script. It reconstructs the exact rational characteristic matrix and verifies the zero-frequency determinant identity in 23 finite cases, including equilibrium families with two, three, four, and six types and degenerate continua. It separately brackets positive real characteristic roots for sharp two-equilibrium witnesses with two, three, four, and six types. All checks completed successfully during preparation of this record. Such tests are finite corroboration; the preceding proof establishes the theorem for every admissible finite \(n\).

## Relationship to prior work

Bardina, Cano and Cuadrado [1] introduce precisely these delayed phage equations with possibly unequal latencies. They analyze general \(n\) but derive a full coexistence-equilibrium classification for \(n=2\) with equal latency (their Section 5.1, Proposition 5.5). Their two-type rational equilibrium function and strict-convexity calculation are acknowledged as prior mathematics, as is their **numerical** observation of coexistence instability. The result here establishes a sharp uniform equilibrium bound for all finite \(n\) and provides an analytic real-positive-eigenvalue certificate at every decreasing-branch equilibrium, independently of the size of the common latency. No argument assumes that a cocktail of many unequal types can be reduced to two effective types.

An earlier related analysis, *Critical-dose bifurcation and algebraic clearance in delayed phage cocktails*, concerns the **bacteria-free threshold** and a local branch of the form \(s=\delta/\kappa+O(\delta^2)\), with critical algebraic relaxation. In the present common-latency specialization its local coefficient is \(\kappa=F_s\bigl(0;\alpha_c\bigr)\). That local identity is acknowledged, not claimed as new here: it neither counts remote positive coexistence equilibria nor proves a positive real characteristic root on every decreasing branch.

The earlier single-phage coinfection literature [2] and the two-phage resistance/immune modelling of [3] concern different dimensionality or mechanisms. Neither supplies the stated arbitrary-cocktail characteristic determinant. Priority beyond the primary sources inspected remains subject to independent literature assessment.

## Limitations

The finite-type assumption and strictly positive parameters are essential to the stated domain. The proof requires **identical latency periods**, not merely similar latencies. It classifies strictly positive equilibria, not equilibria on biological boundary faces, trajectories, global basins, or long-term clinical outcomes. The presence of a positive real exponent proves instability of the lower coexistence state but **does not prove attraction or stability of the upper coexistence state**. A zero characteristic exponent is not a nonlinear fold theorem. The explicit sharpness parameters illustrate mathematical feasibility and are not inferred therapeutic measurements. There has been no independent mathematical validation or definitive historical-priority certification.

## References

[1] X. Bardina, M. Cano, S. Cuadrado, *Modelling and analysis of a cocktail phage therapy with coinfection*, arXiv:2611.08370v1 (first posted 2026-11-05), https://arxiv.org/html/2611.08370v1 ; especially (2.1)–(2.3) and Section 5.

[2] X. Bardina and C. Rovira, *Coinfection in a stochastic model for bacteriophage systems*, arXiv:1702.06177 (2017), https://arxiv.org/abs/1702.06177 .

[3] J. Marchi, C. N. N. Minh, L. Debarbieux, J. S. Weitz, *Multi-strain phage induced clearance of bacterial infections*, PLOS Computational Biology 21 (2025), e1012793, https://doi.org/10.1371/journal.pcbi.1012793 .
