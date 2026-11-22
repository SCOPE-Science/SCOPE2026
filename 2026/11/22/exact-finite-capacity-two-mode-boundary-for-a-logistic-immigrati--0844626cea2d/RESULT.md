# Exact finite-capacity two-mode boundary for a logistic immigration population

## Finding

For every integer \(N\ge2\) and positive birth, death, and immigration rates \(\nu,\mu,\alpha\), consider the finite-capacity single-step population chain
\[
\lambda_j=(N-j)\left(\alpha+\frac{\nu j}{N-1}\right),\quad
\mu_j=\mu j,\qquad 0\le j\le N.
\]
Set \(a=\alpha/\mu\), \(b=\nu/\mu\). The unique stationary population law \(\pi\) has a strictly decreasing first step followed by a later strictly increasing step—hence a vacant-state mode and a distinct occupied-state modal component—**if and only if**
\[
0<a<\frac1N,\qquad b>B_N(a),\qquad
B_N(a)=(N-1)\min_{1\le t\le N-1}\frac{(1+a)t+1-Na}{t(N-t)}.
\]
The inequality in \(b\) is strict. At equality the stationary probabilities are nonincreasing, possibly with a flat shoulder, not a second rising modal component. Every stationary law in this model has at most two separated modal components, counting connected plateaus as one component.

The exact finite-integer threshold has a closed continuous envelope and an explicit lattice correction. With \(\delta=1-Na\in(0,1)\), define
\[
t_c=\frac{N\sqrt\delta}{\sqrt{N+1}+\sqrt\delta},\qquad
B_c=\frac{N-1}{N^2}\bigl(\sqrt{N+1}+\sqrt\delta\bigr)^2.
\]
Then
\[
\boxed{\quad B_N(a)=B_c\left(1+
\min_{1\le t\le N-1}\frac{(t-t_c)^2}{t(N-t)}\right).\quad}
\]
Only the admissible integers immediately below or above \(t_c\), with endpoint clipping, need be compared. As immigration increases from zero toward \(\mu/N\), \(B_N(\alpha/\mu)\) is a strictly decreasing, concave, piecewise-affine function. Its minimizing integer never increases.

At the natural weak-immigration scale \(\alpha=\eta\mu/N\), for any fixed \(0\le\eta<1\) (with \(\eta>0\) for the irreducible chain),
\[
\boxed{\quad
B_N(\eta/N)=1+\frac{2\sqrt{1-\eta}}{\sqrt N}
+\frac{1-\eta}{N}+O_\eta(N^{-3/2}),\quad}
\]
and the first incipient occupied-state rising step is at an index \(t+1\) with \(t=\sqrt{(1-\eta)N}+O_\eta(1)\). Thus stationary two-mode onset has a sharp positive finite-size correction to the deterministic growth threshold, with a nontrivial dependence on weak immigration.

## Assumptions and scope

The state is the count \(j\in\{0,\ldots,N\}\). The boundary rates are \(\lambda_N=0\), \(\mu_0=0\). All three rates are strictly positive, so the chain is finite, irreducible, and has a unique strictly positive invariant probability mass function. A *stationary rise* is an index \(j\ge1\) with \(\pi_j>\pi_{j-1}\). A *vacant-state mode* means \(\pi_0>\pi_1\). A *separated second modal component* means such a mode at zero coexists with at least one rise at a later index. This operational definition accommodates exact plateau parameters. It is a statement about the stationary distribution of **population counts**, not the distribution of active-period durations or quasi-stationary survival.

All equalities and inequalities in the finite theorem are exact. The large-capacity asymptotic holds for fixed \(\eta\) strictly below one; it is not asserted uniformly as \(\eta\uparrow1\).

## Proof

**1. Stationary ratios.** The detailed balance equations yield
\[
\frac{\pi_n}{\pi_{n-1}}=R_n
=\frac{N-n+1}{n}\left(a+\frac{b(n-1)}{N-1}\right),
\qquad 1\le n\le N.
\]
In particular \(R_1=Na\), so a strict vacant-state mode exists exactly when \(a<1/N\).

**2. Global mode-count bound.** Direct common-denominator subtraction gives, for \(1\le n<N\),
\[
R_{n+1}-R_n=
\frac{\frac{b}{N-1}\bigl(N+1-n(n+1)\bigr)-(N+1)a}
{n(n+1)}.
\]
The numerator strictly decreases as \(n\) increases. Therefore the ratio sequence rises and then falls, possibly with one of those phases absent; it cannot rise after falling. Consequently \(R_n-1\) can change sign at most twice, and a stationary mass sequence formed by multiplying successive ratios has at most two separated modal components. If \(R_1\ge1\), there is no strict vacant-state mode. If \(R_1<1\), a second modal component occurs exactly when \(R_n>1\) at some \(n\ge2\): the initial descent and later ascent are then separated, and the finite sequence ultimately reaches a modal component (at the upper endpoint if necessary). Equal adjacent masses can enlarge a modal component into a plateau but cannot create a new rising component.

**3. Exact threshold.** Put \(t=n-1\). For \(1\le t\le N-1\) and \(\delta=1-Na>0\), algebra gives
\[
R_{t+1}>1\quad\Longleftrightarrow\quad
b>(N-1)\frac{(1+a)t+\delta}{t(N-t)}=:b_t(a).
\]
Existence of a later rise is therefore exactly \(b>\min_t b_t(a)\), proving the first criterion, including its strict boundary.

**4. Closed envelope and lattice correction.** On the real interval \((0,N)\), the sign of the derivative of \(((1+a)t+\delta)/(t(N-t))\) is the sign of
\[
(1+a)t^2+2\delta t-N\delta.
\]
This expression has exactly one positive zero. Using \(N(1+a)+\delta=N+1\), its root is
\[
t_c=\frac{\sqrt{\delta(N+1)}-\delta}{1+a}
=\frac{N\sqrt\delta}{\sqrt{N+1}+\sqrt\delta}.
\]
Substitution gives the continuous minimum \(B_c\) stated above. More sharply, the discriminant-zero identity at this double contact is
\[
(N-1)\bigl((1+a)t+\delta\bigr)
-B_c\,t(N-t)=B_c(t-t_c)^2
\]
for all real \(t\). Divide by \(t(N-t)>0\) and minimize over admissible integers to obtain the exact lattice correction. Strict decrease on \((0,t_c)\) and strict increase on \((t_c,N)\) restrict the minimization to the two nearest surrounding admissible integers (clipped at boundaries).

**5. Geometry of the immigration boundary.** For each integer \(t\),
\[
b_t(a)=(N-1)\left(\frac{t+1}{t(N-t)}-\frac a t\right).
\]
Its slope in \(a\) is \(-(N-1)/t<0\). The minimum of these finitely many lines is continuous, concave, piecewise affine, and strictly decreasing. Since the slopes increase with \(t\), the index of an active minimizing line can only move toward smaller \(t\) as \(a\) increases. At a tie, both consecutive minimizers are admitted.

**6. Finite-size asymptotic.** Fix \(\eta\in[0,1)\), set \(a=\eta/N\), \(\delta=1-\eta\), and expand
\[
B_c=\frac{N-1}{N^2}\bigl(\sqrt{N+1}+\sqrt\delta\bigr)^2
=1+2\sqrt\delta N^{-1/2}+\delta N^{-1}+O_\eta(N^{-3/2}).
\]
Also \(t_c=\sqrt{\delta N}+O_\eta(1)\). The nearest admissible integer differs from \(t_c\) by at most one and has \(t(N-t)=\Theta_\eta(N^{3/2})\); hence the exact lattice correction is \(O_\eta(N^{-3/2})\). Combining these estimates proves the displayed expansion and the onset-index statement. The \(\eta=0\) expression denotes the one-sided zero-immigration limit of the threshold, not an invariant positive-law statement at \(\alpha=0\).

## Verification

All exact identities can be verified by elementary algebra from the generator. A standalone standard-library program, `verify.py`, checks exact stationary ratios and the claimed sharp threshold for \(2\le N\le100\), multiple rational immigration fractions, and intensities just below, equal to, and above the threshold; it also checks the lattice identity and asymptotic diagnostics. This finite computation is supplementary, **not** the proof for arbitrary capacity.

An explicit illustration takes \(N=10\), \(a=1/50\), \(b=8/5\). The exact critical value is \(B_{10}(1/50)=639/400\), attained at \(t=2\). Since \(8/5>639/400\), the mass sequence decreases from occupancy zero to occupancy two, then increases to occupancy three, then declines: zero and three are distinct strict local modes. This is a local-modal statement, not a claim that the two peaks have equal stationary probability mass.

## Relationship to prior work

Brugevin and Zanette's finite-population logistic birth–death–immigration model motivates the question; their investigation concerns vacant and active-period statistics, population counts, network effects, and an approximate diffusion-potential treatment of active-time bimodality. Their work supplies the transition model, not the exact positive-immigration two-parameter stationary *count-mode* boundary, discrete lattice correction, or weak-immigration finite-size onset derived here. Their approximate leading small-immigration correction is not represented as new.

Xu's stochastic logistic mate-limitation model also has stationary bimodality, but uses a strong-Allee birth mechanism and asymptotic extinction/persistence results. The present threshold concerns the distinct logistic-contact mechanism **without** mate limitation and provides an exact finite-size classification. Classical birth–death detailed balance is an essential previously known input, not a contribution claimed here. Earlier immigration-logistic population studies include cumulant and saddlepoint approximations; the possibility of an uninspected stronger exact result in that literature remains a priority risk.

## Limitations

This is a local modality theorem for a finite stationary count distribution. It does not quantify peak masses, switching times, conditional active-period duration distributions, or spatial-network effects. It is not a theorem about deterministic bistability or Allee effects; two stationary peaks can occur even when deterministic growth has a single positive equilibrium. The count-mode threshold is not interchangeable with the source's active-duration bimodality threshold. Exact equality of stationary probabilities may create plateaus; the strict-rise definition resolves this boundary. Independent historical-priority and scientific audits have not been performed.

## References

1. L. M. Brugevin and D. H. Zanette, *Logistic dynamics of small populations with demographic stochasticity*, arXiv:2605.27100 (first public posting 2026-05-26), https://arxiv.org/abs/2605.27100 ; doi:10.1103/rt9k-tm2q.
2. C. Xu, *Strong Allee Effect in A Stochastic Logistic Model with Mate Limitation and Stochastic Immigration*, arXiv:1605.06084 (2016), https://arxiv.org/abs/1605.06084 ; doi:10.3934/dcdsb.2016049.
3. J. H. Matis and T. R. Kiffe, *On stochastic logistic population growth models with immigration and multiple births*, Theoretical Population Biology 65 (2004), 89–104, doi:10.1016/j.tpb.2003.08.003.
