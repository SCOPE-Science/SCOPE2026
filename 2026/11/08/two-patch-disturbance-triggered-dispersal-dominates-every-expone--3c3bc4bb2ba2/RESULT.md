# Two-patch disturbance-triggered dispersal dominates every exponential deadline, but not every fixed deadline

## Finding

For a closed two-patch metapopulation starting with exactly one occupied, suitable patch and one suitable, empty patch, compare pure disturbance-triggered (*pulsed*) dispersal with pure continuous dispersal at the same nominal per-donor-to-available-target colonization intensity. For every positive demographic extinction rate, patch destruction rate, and patch restoration rate, and every nonzero admissible pulse success probability, pulsed dispersal gives **strictly greater exponentially discounted expected persistence** at every nonnegative discount rate. In particular, it gives strictly greater mean global extinction time.

Nevertheless, this is **not** a survival stochastic-dominance theorem: at an explicitly certified rational parameter point, continuous dispersal gives greater survival at the fixed deadline \(t=2\), even though pulsed dispersal has the larger mean and the larger exponential-deadline survival probability for every exponential rate. This distinction between deadline types is the substantive finding.

## Assumptions and scope

There are exactly two distinguishable habitat patches, each in state \(0\) (unsuitable, unoccupied), \(1\) (suitable, empty), or \(2\) (suitable, occupied). Habitat restoration \(0\to1\) occurs at rate \(\ell>0\); habitat destruction \(1\to0\) and \(2\to0\) occurs at rate \(b>0\); demographic extinction \(2\to1\) occurs at rate \(e>0\). All elementary clocks are independent conditional on the state, except for the coupled effects of a destruction-triggered pulse. There is no external immigration, and the first state with no occupied patch is absorbing for the global-extinction experiment. The initial state is \((2,1)\). Let \(\tau_{\mathrm P}\) and \(\tau_{\mathrm C}\) denote the corresponding times to global extinction.

In the pulsed model, there is no continuous colonization. When an occupied patch is destroyed, it colonizes the *other* patch with probability \(q\in(0,1]\) if that other patch is in state \(1\), leaving the donor in state \(0\). In the continuous model, there is no destruction-triggered colonization; an occupied patch colonizes an available empty patch at rate \(c=bq\). Hence both models have the same **nominal colonization intensity per occupied donor and available empty target**; the total number of realized colonizations need not agree because availability histories differ. For a population of two patches this corresponds to the standard parameters \(c_1=2bq\) for continuous dispersal or \(c_2=2q\) for pulses, with \(c_1=bc_2\). The admissibility restriction \(q\le1\) is essential.

For \(z\ge0\), define the discounted survival functional
\[
U_m(z)=\mathbb E\left[\int_0^{\tau_m}e^{-zt}\,dt\right]
=\int_0^\infty e^{-zt}\Pr(\tau_m>t)\,dt,
\quad m\in\{\mathrm P,\mathrm C\}.
\]
At \(z=0\), it is the mean extinction time. For \(z>0\), \(zU_m(z)\) is the survival probability against an independent exponential deadline of rate \(z\).

**Theorem.** For all \(\ell,e,b>0\), \(0<q\le1\), and \(z\ge0\),
\[
\boxed{U_{\mathrm P}(z)>U_{\mathrm C}(z).}
\]
However, when \((\ell,e,b,q)=(1/10,3,1,1)\),
\[
\boxed{\Pr(\tau_{\mathrm P}>2)<\Pr(\tau_{\mathrm C}>2).}
\]
No ordering at every deterministic time is asserted.

## Proof

**Exact generators.** By patch-exchange symmetry, identify the transient configurations with \(A=(2,0)\), \(B=(2,1)\), and \(C=(2,2)\), understood up to swapping the two patches. The pulsed model started at \(B\) never reaches \(C\). In the state order \((A,B)\), its transient subgenerator is
\[
Q_{\mathrm P}=\begin{pmatrix}
-(e+b+\ell)&\ell\\
b(1+q)&-(e+2b)
\end{pmatrix}.
\]
The \(B\to A\) rate \(b(1+q)\) accounts for loss of the unoccupied habitat at rate \(b\) and successful donor-destruction pulse at rate \(bq\). The donor's unsuccessful destruction and demographic extinction lead to absorption.

In the state order \((A,B,C)\), the continuous model has
\[
Q_{\mathrm C}=\begin{pmatrix}
-(e+b+\ell)&\ell&0\\
b&-(e+2b+bq)&bq\\
2b&2e&-2(e+b)
\end{pmatrix}.
\]
For example, a demographic loss from \(C\) returns to \(B\), where recolonization can occur again; therefore the \(B\leftrightarrow C\) loop must not be discarded. These are subgenerators: row deficits are rates of absorption.

**Resolvent identity.** Let
\[
\begin{aligned}
a(z)&=z+e+b+\ell,\\
D_{\mathrm P}(z)&=\det(zI-Q_{\mathrm P}),\\
D_{\mathrm C}(z)&=\det(zI-Q_{\mathrm C}),\\
P(z)&=z^2+(\ell+bq+3b+2e)z\\
&\quad+\ell bq+\ell b+\ell e+2b^2q+2b^2+3be+e^2.
\end{aligned}
\]
The backward equation for discounted survival gives \(U_m(z)=[(zI-Q_m)^{-1}\boldsymbol1]_B\). Inverting the displayed two- and three-state matrices, followed by expansion and cancellation, yields the exact identity
\[
\boxed{
U_{\mathrm P}(z)-U_{\mathrm C}(z)
=\frac{bq\,a(z)P(z)}{D_{\mathrm P}(z)D_{\mathrm C}(z)}.
}
\]
For direct replication, the determinants are equivalently
\[
\begin{aligned}
D_{\mathrm P}(z)&=a(z)(z+e+2b)-\ell b(1+q),\\
D_{\mathrm C}(z)&=a(z)\big[(z+e+2b+bq)(z+2e+2b)-2ebq\big]\\
&\qquad-\ell b(z+2e+2b+2bq).
\end{aligned}
\]
The polynomial \(P(z)\) is strictly positive for \(z\ge0\) and the stated parameters. Both subgenerators correspond to transient finite-state continuous-time chains, since \(e,b>0\) and there is a positive probability of losing all occupied patches within finitely many transitions; thus each \(zI-Q_m\) is a nonsingular \(M\)-matrix and its determinant is positive for \(z\ge0\). Alternatively, expanding either determinant in powers of \(z\) gives positive coefficients after using \(1-q\ge0\). Since also \(bq\,a(z)>0\), the desired strict inequality follows.

**A fixed-deadline reversal, certified without floating point.** Set \(\ell=1/10\), \(e=3\), \(b=q=1\). At \(z=0\), exact inverse matrices give
\[
\mathbb E[\tau_{\mathrm P}]=\frac{61}{203},\qquad
\mathbb E[\tau_{\mathrm C}]=\frac{469}{1712},\qquad
\mathbb E[\tau_{\mathrm P}]-\mathbb E[\tau_{\mathrm C}]=\frac{9225}{347536}>0.
\]
To certify the *opposite* strict survival inequality at \(t=2\), uniformize each three-state transient generator at common rate \(8\), using the three-state pulsed matrix with unreachable state \(C\). The two substochastic transition matrices are
\[
P_{\mathrm P}=\begin{pmatrix}39/80&1/80&0\\1/4&3/8&0\\1/4&3/4&0\end{pmatrix},\qquad
P_{\mathrm C}=\begin{pmatrix}39/80&1/80&0\\1/8&1/4&1/8\\1/4&3/4&0\end{pmatrix}.
\]
With \(h_m(n)=\boldsymbol e_B^{\mathsf T}P_m^n\boldsymbol1\in[0,1]\), define the finite **rational** sum
\[
W_{80}=\sum_{n=0}^{80}\frac{16^n}{n!}\,[h_{\mathrm P}(n)-h_{\mathrm C}(n)].
\]
Exact fraction arithmetic yields \(-98<W_{80}<-97\), in particular \(W_{80}<-90\). The omitted absolute tail is bounded by
\[
\sum_{n=81}^\infty\frac{16^n}{n!}
\le\frac{16^{81}}{81!}\left(1-\frac{16}{82}\right)^{-1}<\frac1{1000}.
\]
Consequently
\[
\Pr(\tau_{\mathrm P}>2)-\Pr(\tau_{\mathrm C}>2)
=e^{-16}(W_{80}+R)<0,\qquad |R|<1/1000.
\]
This is a strict, finite rational certificate, not a numerical guess. Approximate survival probabilities are \(0.00066110526\) and \(0.00067212258\), respectively. At sufficiently small positive times the pulsed strategy instead has the larger survival probability: the initial absorption rates are \(e+b(1-q)=3\) for pulses and \(e+b=4\) for continuous dispersal. Continuity therefore guarantees at least one fixed-time reversal.

## Verification

Run `python CHECK.py` with SymPy available. The checker verifies the exact general resolvent identity and determinant expansions symbolically; independently constructs the five-state labelled-patch generator and compares exact resolvents to the lumped matrices; verifies the rational parameter means; and certifies the \(t=2\) survival reversal using the \(81\)-term rational uniformization sum plus an explicit tail bound. The general inequality follows from the analytical positive-factor identity, not from the finite checks. Exact rational comparisons certify the deterministic-deadline counterexample.

## Relationship to prior work

Reigada, Schreiber, Altermatt and Holyoak (published online January 8, 2015) introduce the three-state ephemeral-patch habitat and contrasting pulsed versus continuous dispersal mechanisms with matched nominal colonization rates. Their main paper develops mean-field/branching approximations and numerical comparisons for larger finite landscapes. It supplies the model and motivation, **not** the present two-patch all-discount factorization or the fixed-deadline non-ordering certificate. The exact comparison must not be conflated with their large-landscape establishment findings.

Hill and Caswell (2001) analyze finite-landscape chain-binomial occupancy and extinction-time questions, but their discrete-time habitat-loss model is not this disturbance-triggered colonization comparison. Kang and Lanchier (2010) analyze stochastic two-patch Allee-effect population densities, rather than three-state habitat renewal with destruction pulses. These are related comparisons, not statements that imply the present theorem.

## Limitations

Only two identical patches, a closed one-species occupancy process, Markov rates, an initially singly occupied landscape, and the specified matching of nominal colonization intensity are covered. The result is **not** a comparison of realized propagule counts, a claim that pulsed dispersal is universally superior for larger networks, or a field-calibrated intervention. Positive restoration, destruction and demographic rates are assumed for the theorem; the displayed deterministic-time counterexample has positive restoration. Laplace-transform ordering by itself does not establish pointwise survival ordering; the exact certificate explicitly prevents that inference. Historical priority is provisional, particularly regarding supplementary analyses and less accessible finite-landscape literature; no independent audit has been performed.

## References

1. Reigada, C., Schreiber, S. J., Altermatt, F., and Holyoak, M. (2015), *Metapopulation Dynamics on Ephemeral Patches*, *The American Naturalist* 185:183–195, published online January 8, 2015. https://doi.org/10.1086/679502 . Author-accessible paper: https://www.altermattlab.ch/wp-content/uploads/2018/06/Reigada.et_.al_AmNat_2015.pdf .
2. Hill, M. F. and Caswell, H. (2001), *The effects of habitat destruction in finite landscapes: A chain-binomial metapopulation model*, *Oikos* 93:321–331. https://doi.org/10.1034/j.1600-0706.2001.930215.x .
3. Kang, Y. and Lanchier, N. (2010), *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, preprint publicly posted February 27, 2010. https://arxiv.org/abs/1003.0121 .
