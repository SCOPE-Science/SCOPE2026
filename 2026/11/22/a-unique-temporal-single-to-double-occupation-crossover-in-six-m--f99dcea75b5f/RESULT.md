# A unique temporal single-to-double occupation crossover in six-mer random sequential covering

## Finding

In one-dimensional random sequential covering of the initially empty integer lattice by length-\(k\) intervals (\(k\)-mers), each potential start has an independent unit-rate Poisson process of deposition attempts. An attempt is accepted exactly when it covers at least one site not previously covered. Let \(\pi_j^{(k)}(t)\) denote the probability that the origin is covered by exactly \(j\) accepted intervals at time \(t\).

**Theorem (first single-to-double crossover, through length six).** For each \(k\in\{2,3,4,5\}\) and every \(t>0\), \(\pi_1^{(k)}(t)>\pi_2^{(k)}(t)\). For \(k=6\), there exists exactly one \(t_*\in(0,\infty)\) such that
\[
\pi_1^{(6)}(t)>\pi_2^{(6)}(t)\quad(0<t<t_*),\qquad
\pi_1^{(6)}(t_*)=\pi_2^{(6)}(t_*),\qquad
\pi_1^{(6)}(t)<\pi_2^{(6)}(t)\quad(t>t_*).
\]
Writing \(q_*=1-e^{-t_*}\), this unique root is bracketed exactly by \(577764/10^6<q_*<577765/10^6\), with
\[
q_*=0.57776462798272308286\ldots,\qquad t_*=0.86219236683740609699\ldots.
\]

The complete exact terminal one-site multiplicity law for six-mers is
\[
\bigl(\pi_1^{(6)}(\infty),\pi_2^{(6)}(\infty),\pi_3^{(6)}(\infty),
\pi_4^{(6)}(\infty),\pi_5^{(6)}(\infty),\pi_6^{(6)}(\infty)\bigr)
=\left(\frac{38729}{90090},\frac{8026379}{18162144},\frac{10270963}{90810720},\frac{3667}{258720},\frac{559}{635040},\frac{19}{873180}\right).
\]
In particular, the previously unlisted sixfold occupation probability is \(\pi_6^{(6)}(\infty)=19/873180\). More strongly, with \(z=e^{-t}\) and \(q=1-z\), its full finite-time expression is
\[
\pi_6^{(6)}(t)=\frac{q^6}{3492720}\Bigl(76+456z+1596z^2+4256z^3+9576z^4+19152z^5
+20405z^6+25740z^7+28545z^8+26950z^9+18480z^{10}\Bigr).
\]

## Assumptions and scope

The substrate is the full lattice \(\mathbb Z\) and is empty at time zero. For every integer start \(s\), the attempted interval is \(I_s=\{s,s+1,\ldots,s+k-1\}\). Its attempts form an independent rate-one homogeneous Poisson process. A successful attempt deposits the entire interval even where it overlaps earlier accepted intervals, and all attempts that fail to add coverage are rejected. The theorem concerns a fixed site in the infinite-volume law, all finite \(t\ge0\), and the limit \(t\to\infty\). It does not concern the non-overlapping random sequential *adsorption* rule, finite-interval boundary conventions, or physical deposition times with correlated clocks.

## Proof

**1. First arrivals and local reduction.** Write \(T_s\) for the first attempted deposition time at start \(s\). The \(T_s\) are independent \(\mathrm{Exp}(1)\) variables. Only the first attempt at a start can be accepted: after it, its entire interval is already covered, whether its first attempt was accepted or rejected. At any finite list of first attempts, the union of attempted supports equals the union of accepted supports. This follows by induction: rejected first attempts add no uncovered site, so add nothing to the union. Therefore an interval \(I_s\), when first attempted, is accepted precisely if it is not contained in the union of intervals whose first attempts occurred earlier.

Only starts \(s\in A_k=\{-k+1,\ldots,0\}\) can cover the origin. The accepted status of any such start depends only on earlier intervals intersecting \(I_s\); the union of all their possible start indices is
\[
H_k=\{-2(k-1),-2(k-1)+1,\ldots,k-1\},\qquad |H_k|=3k-2.
\]
Intervals starting outside \(H_k\) are disjoint from each target interval, so cannot affect these acceptance decisions. The formula uses local *first attempts*, not the eventual acceptance of remote intervals.

**2. All-time exact subset recurrence.** For every \(S\subseteq H_k\), let \(c_k(S,j)\) be the number of permutations of the elements of \(S\) whose sequential first-attempt process accepts exactly \(j\) intervals covering zero. Define \(U(B)=\bigcup_{s\in B}I_s\) and
\[
a_k(s,B)=\mathbf1\{s\in A_k\}\,\mathbf1\{I_s\not\subseteq U(B)\}.
\]
With \(c_k(\varnothing,0)=1\) and all other empty-set counts zero, chronological-last-step removal yields the exact integer recurrence
\[
c_k(S,j)=\sum_{s\in S}c_k\bigl(S\setminus\{s\},j-a_k(s,S\setminus\{s\})\bigr),
\]
where a count with a negative index is zero. The number of first arrivals by time \(t\) in \(H_k\) is a product of independent Bernoulli variables with parameter \(q=1-e^{-t}\), and their order conditional on a chosen subset \(S\) is uniform. Hence, for every \(k\ge2\),
\[
\pi_j^{(k)}(t)=\sum_{S\subseteq H_k}\frac{c_k(S,j)}{|S|!}\,q^{|S|}(1-q)^{3k-2-|S|}.
\]
This is a constructive finite sum, not a formal infinite-volume extrapolation. At saturation only \(S=H_k\) remains, giving \(\pi_j^{(k)}(\infty)=c_k(H_k,j)/(3k-2)!\). The same recurrence yields the displayed six-mer vector and the finite-time sixfold polynomial; each coefficient is rational and independently reproducible by the attached checker.

**3. Exact sign certificate and uniqueness.** Put \(x=q/(1-q)=e^t-1>0\) and, for each \(k\), define
\[
B_k(x)=(1+x)^{3k-2}\bigl[\pi_1^{(k)}(t)-\pi_2^{(k)}(t)\bigr].
\]
By the subset formula, \(B_k(x)\) is a rational polynomial with zero constant term and coefficient of \(x^m\) equal to
\[
\frac1{m!}\sum_{\substack{S\subseteq H_k\\|S|=m}}\bigl(c_k(S,1)-c_k(S,2)\bigr).
\]
The exact arithmetic for \(k=2,3,4,5\) gives strictly positive coefficients at every degree from one through the polynomial's degree \(3k-2\); consequently \(B_k(x)>0\) for every \(x>0\). For \(k=6\), the certified polynomial, expressed in descending powers of \(x\), is
\[
\begin{aligned}
90810720\,B_6(x)={}&-1093063x^{16}-17489008x^{15}-131167560x^{14}-612115280x^{13}\\
&-1989374660x^{12}-4774499184x^{11}-8498073584x^{10}-10052042000x^9\\
&-3565311750x^8+13788094320x^7+33629732136x^6+40774013280x^5\\
&+30648618000x^4+14529715200x^3+4086482400x^2+544864320x.
\end{aligned}
\]
Its nonzero coefficients have exactly one sign change in descending order. Descartes' rule of signs therefore bounds the number of positive real roots by one, counted with multiplicity. The polynomial is positive for sufficiently small positive \(x\) and negative for sufficiently large \(x\), so continuity proves that exactly one positive root exists. The exact rational bracket for \(q_*\) follows by substituting the rational endpoints into this integer polynomial after the map \(x=q/(1-q)\). The displayed decimals are numerical evaluations of this unique, rigorously characterized root.

## Verification

Run \(\texttt{python3 verify.py}\) from the directory containing the extracted standalone artifact. It uses Python 3 standard-library arbitrary-precision integers and rational arithmetic. It computes the finite subset recursion independently in chronological-forward and chronological-backward forms, checks their terminal outputs for every \(k\in\{2,3,4,5,6\}\), and directly enumerates all ordered first attempts for \(k=2,3\). It reproduces all six rational terminal probabilities, all 16 exact polynomial coefficients of \(B_6\), their one sign change, the coefficient-positivity certificates for \(k\le5\), the rational crossover bracket, and all-time normalization and known first-moment identities at four exact time parameters. The script passes 222 exact identity/group assertions.

The integer recurrence and Descartes argument constitute the finite combinatorial proof; numerical root-finding is only illustrative. No finite computation is used as a substitute for an unverified infinite-volume limit, because Step 1 proves exact localization for the fixed-site event.

## Relationship to prior work

Krapivsky (2022, arXiv:2209.03992) defined the one-dimensional random sequential covering model and derived mean-coverage identities and dimer statistics. Viot and Krapivsky (first posted 2024, arXiv:2410.12373) solved the complete temporal one-site multiplicity law through \(k=5\), established general finite-hierarchy solvability in principle, and provided approximate simulations for \(k=6\); those simulations already show that double coverage eventually dominates single coverage. That qualitative terminal ordering, the general model, and general finite-hierarchy solvability are **not** claimed as new. A separate published trimer-correlation calculation already uses local first-arrival clocks and subset enumeration; the localization technique itself is not claimed as a new invention.

The additional result here is the **first exact finite-time unique reversal theorem at \(k=6\)**, certified by a full polynomial sign analysis, together with its complete exact six-mer terminal distribution and the evaluated previously unavailable sixfold temporal probability. The distinction is a statement-and-implication comparison: earlier complete temporal formulas stop at five; numerical values at six do not imply uniqueness of a crossing over the entire time axis. General finite solvability makes this an accessible specialization but does not itself supply the displayed sign certificate or evaluated six-mer invariants. Independent priority confirmation against all unindexed work remains outstanding.

## Limitations

This is a mathematical result for homogeneous one-dimensional infinite-lattice covering with independent attempt clocks and the acceptance rule specified above. The claimed *first* crossover is first in the natural ordered family \(2\le k\le6\); no theorem about \(k\ge7\) is asserted. The time-dependent distribution at six is given algorithmically by the exact subset sum, with the sixfold component explicitly factored; the full expanded expressions for the other five components are not displayed. The computational cost grows exponentially with \(k\), so this does not solve the continuous-polymer limit. The prior general closure framework can in principle generate these exact values, and the originality claim is limited to the evaluated classification and sign certificate, not to generic rationality or all-parameter solvability.

## References

1. P. L. Krapivsky, *Random Sequential Covering*, arXiv:2209.03992, first posted 2022-09-08, https://arxiv.org/abs/2209.03992.
2. P. Viot and P. L. Krapivsky, *Random sequential covering of a one-dimensional lattice by k-mers*, arXiv:2410.12373, first posted 2024-10-16, https://arxiv.org/abs/2410.12373.
