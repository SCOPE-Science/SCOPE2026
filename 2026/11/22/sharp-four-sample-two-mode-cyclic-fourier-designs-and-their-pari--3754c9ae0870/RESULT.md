# Sharp four-sample two-mode cyclic Fourier designs and their parity gap

## Finding
Let \(N\ge4\) be an integer and \(\omega_N=e^{2\pi i/N}\). For each four-element subset \(S\subset\mathbb Z/N\mathbb Z\), let \(F_S\in\mathbb C^{4\times2}\) have row \((1,\omega_N^s)\), one row for each \(s\in S\). Define \(G_S=F_S^*F_S\). These are **unweighted, distinct-site** two-mode Fourier samplers. Put
\[
\delta_N=\begin{cases}
0,&N\text{ even},\\
2\bigl(\cos(\pi/N)-\cos(2\pi/N)\bigr),&N\text{ odd}.
\end{cases}
\]
Then the exact sharp bounds, simultaneously, are
\[
\max_{|S|=4}\det G_S=16-\delta_N^2,\qquad
\max_{|S|=4}\lambda_{\min}(G_S)=4-\delta_N,
\]
\[
\min_{|S|=4}\operatorname{tr}(G_S^{-1})=\frac8{16-\delta_N^2},\qquad
\min_{|S|=4}\frac{\lambda_{\max}(G_S)}{\lambda_{\min}(G_S)}=\frac{4+\delta_N}{4-\delta_N}.
\]
Each extremal set is the same for all four criteria, and all equality sets are as follows.

* If \(N\) is even, they are **exactly** the unions of two distinct antipodal pairs, \(\{a,a+N/2,b,b+N/2\}\), with precisely \(\binom{N/2}{2}\) distinct unordered optimal sets.
* If \(N\) is odd, they are **exactly** the \(N\) distinct cyclic translates of
\[
\left\{0,1,\frac{N-1}{2},\frac{N+3}{2}\right\}\pmod N.
\]

In particular, an exactly tight four-sample two-mode design exists **if and only if** \(N\) is even. For odd \(N\), the sharp smallest-eigenvalue deficit is \(\delta_N=3\pi^2N^{-2}+O(N^{-4})\), while the determinant loss is \(\delta_N^2=9\pi^4N^{-4}+O(N^{-6})\). For independent equal-variance observation noise, the best total least-squares parameter variance is inflated over the continuous/orthogonal benchmark by the exact factor \((1-\delta_N^2/16)^{-1}\).

## Assumptions and scope
The nodes are distinct elements of a single cyclic grid of order \(N\); the two column frequencies are consecutive, \(0\) and \(1\). Every sample has unit weight, no repeats are allowed, and \(F_S\) is unnormalized. Thus \(\operatorname{tr}G_S=8\) for all admissible \(S\). The condition-number expression is the **squared** spectral condition number of \(F_S\). For a two-component complex coefficient vector observed with independent variance-\(\sigma^2\) noise, the least-squares covariance is \(\sigma^2G_S^{-1}\), provided \(F_S\) has full column rank. That rank condition holds automatically because the sampled nodes are distinct and the columns cannot be proportional on four distinct rows.

## Proof
**1. One Fourier coefficient controls all design criteria.** Put \(z_S=\sum_{s\in S}\omega_N^s\). Directly from the two columns,
\[
G_S=\begin{pmatrix}4&z_S\\\overline{z_S}&4\end{pmatrix},\quad
\operatorname{spec}(G_S)=\{4-|z_S|,4+|z_S|\},\quad
\det G_S=16-|z_S|^2.
\]
Distinct sampled roots ensure \(|z_S|<4\) and positive definiteness. Moreover \(\operatorname{tr}(G_S^{-1})=8/(16-|z_S|^2)\). Each asserted optimality criterion is therefore equivalent to minimizing \(|z_S|\), with identical equality cases.

**2. The even-grid case and all its equality sets.** Two disjoint antipodal pairs sum to zero, so the best possible value is \(|z_S|=0\). Conversely, suppose four distinct unit complex numbers \(u_1,u_2,u_3,u_4\) sum to zero. In the monic polynomial \(P(t)=\prod_j(t-u_j)\), the coefficient of \(t^3\) is zero. Since all roots have modulus one, the coefficient of \(t\) equals \(-\prod_j u_j\) times the conjugate of their sum, and hence is zero too. Therefore \(P(t)=t^4+c t^2+d\) is even. Its roots occur in opposite pairs. On an \(N\)-th-root grid this is possible exactly when \(N\) is even, and every zero-sum four-set is the union of two distinct antipodal pairs. There are \(N/2\) antipodal pairs and exactly \(\binom{N/2}{2}\) ways to choose two.

**3. Two unequal chord-sums on every odd grid.** Now let \(N\) be odd and write \(m=(N-1)/2\). Any chord connecting distinct \(N\)-th roots has a unique shorter cyclic distance \(d\in\{1,\dots,m\}\); the modulus of the sum of its two endpoints is
\[
h_d=2\cos(\pi d/N),\qquad h_1>h_2>\cdots>h_m>0.
\]
Order an arbitrary four-set cyclically as \(A,B,C,D\). Among its two pairings into opposite sides, namely \((A,B)|(C,D)\) and \((A,D)|(B,C)\), at least one pairs chords of **different** lengths. For otherwise \(|A-B|=|C-D|\) and \(|A-D|=|B-C|\) in Euclidean chord length; both pairs of opposite sides of the quadrilateral \(ABCD\) would be equal, so it would be a parallelogram. An inscribed parallelogram is a rectangle, hence contains opposite points of the circle, which an odd-order grid cannot have.

For the resulting unequal distances \(d_1,d_2\), the reverse triangle inequality gives
\[
|z_S|\ge |h_{d_1}-h_{d_2}|\ge h_1-h_2=2\bigl(\cos(\pi/N)-\cos(2\pi/N)\bigr).
\]
The last inequality holds **strictly** unless \(\{d_1,d_2\}=\{1,2\}\). Indeed, consecutive positive length drops satisfy
\[
h_j-h_{j+1}=4\sin\left(\frac{(2j+1)\pi}{2N}\right)\sin\left(\frac{\pi}{2N}\right),
\quad 1\le j<m,
\]
and these drops increase strictly with \(j\), since their first arguments lie in \((0,\pi/2)\). Every difference between distinct members of the decreasing sequence is therefore at least its first drop, with equality only for the first two members.

**4. Attainment and uniqueness for odd orders.** Consider the pair \(\{a,a+1\}\), of chord distance one, and the pair \(\{b,b+2\}\), of chord distance two. Their sums are respectively
\[
2\cos(\pi/N)e^{\pi i(2a+1)/N},\qquad
2\cos(2\pi/N)e^{\pi i(2b+2)/N}.
\]
Their sum attains the reverse-triangle lower bound exactly if these two vectors point in opposite directions, which is equivalent to
\[
2b+2-(2a+1)\equiv N\pmod{2N},\qquad
b\equiv a+(N-1)/2\pmod N.
\]
This produces precisely the translated four-point sets in the statement; their four entries are distinct for every odd \(N\ge5\). Conversely, equality in the lower bound of Step 3 forces the chosen pairing to have chord distances one and two and its pair sums to be opposite, so it forces exactly this construction. No nontrivial translation can fix any such four-set: the order of a translation stabilizer divides both the odd integer \(N\) and the set size four. Thus there are exactly \(N\) equality sets.

**5. Determinant, spectrum, and the parity asymptotics.** Substitution of \(\min|z_S|=\delta_N\) into Step 1 proves all four sharp formulas. Taylor expansion of cosine gives \(\delta_N=3\pi^2/N^2+O(N^{-4})\) along odd orders; squaring yields \(\delta_N^2=9\pi^4/N^4+O(N^{-6})\). With the fixed noise covariance described above, relative total-variance inflation is \([8/(16-\delta_N^2)]/(8/16)=(1-\delta_N^2/16)^{-1}\). This completes all cases and quantifiers.

## Verification
The standalone Python 3 standard-library checker `check.py` constructs every four-subset for all orders \(4\le N\le36\), independently computes the magnitude of its four-root phasor sum and the two-column Gram quantities, checks the exact sharp formula within conservative floating-point tolerance, and matches the **complete set** of optimizers to the claimed antipodal or translated families. It also checks the displayed eigenvalue, determinant and inverse-trace identities numerically. Run `python3 check.py` from the directory containing the file. The finite checks corroborate the analytic all-orders proof; no finite enumeration is presented as an infinite proof.

## Relationship to prior work
Dozzi, Oomen, and González (arXiv:2605.13120, Sections 3–4) study D-optimal nonuniform Fourier sampling for system identification. Their design optimizes continuous probability densities and uses a greedy discretization for multisine frequency-response estimation, rather than solving this four-distinct-site cyclic two-frequency design or classifying all deterministic equality sets.

Barber (arXiv:2104.15057, Section 2, Proposition 3 and its proof) treats the smallest nonzero four-root sum **with repetition allowed**, and exhibits a twice-used root in the extremal configuration for odd orders. The current exclusion of repeated sites changes the sharp value and yields the distinct-site extremizer classification; neither that broader-repetition scalar minimum nor its displayed construction implies the claimed constrained minimum. The geometric pairing technique is closely related, and is acknowledged rather than claimed as new.

Munemasa and Núñez Ponasso (arXiv:2607.00825) fix root order five while varying the number of summands, allowing repetitions. Their arithmetic classification is a separate root-sum optimization problem. Published published-finding corpus findings *Exact four-frequency determinant optimum on every cyclic grid* (four-by-four square matrices), *Certified four-point cyclic Wiener minimizers through modulus 128* (the sum of magnitudes over **all** nontrivial frequencies), and *Sharp Riesz conditioning for consecutive triples on finite cycles* (a square three-frequency model) address different statements: none supplies this all-order two-column four-distinct-site optimum or its full orbit count. The comparison was by object and implication, not just title.

## Limitations
The exact classification is restricted to four distinct, equally weighted sample sites and two consecutive frequencies. It is not an optimization over arbitrary Fourier bands, nonuniform weights, repeated samples, or larger observation budgets. The D-, E-, A-, and condition-number equivalence here depends on the two-by-two equal-diagonal Gram structure and need not persist for more modes. The supplied computations are finite corroboration only. Older equivalent results in circular optimal design or restricted roots-of-unity sums may exist; no worldwide priority or independent verification is claimed.

## References
1. E. Dozzi, T. Oomen, and R. A. González, *D-Optimized Sampling Design for System Identification*, arXiv:2605.13120, first posted 2026-05-13, https://arxiv.org/abs/2605.13120.
2. B. Barber, *Small sums of five roots of unity*, arXiv:2104.15057 (2021), Section 2; *Bulletin of the London Mathematical Society* 55 (2023), 1890–1906, https://arxiv.org/abs/2104.15057.
3. A. Munemasa and G. Núñez Ponasso, *The Minimal Absolute Value of Sums of Fifth Roots of Unity*, arXiv:2607.00825, first posted 2026-07-01, https://arxiv.org/abs/2607.00825.
4. *Exact four-frequency determinant optimum on every cyclic grid*, published-finding corpus mathematical record (2026-10-11), public RESULT.md.
5. *Certified four-point cyclic Wiener minimizers through modulus 128*, published-finding corpus mathematical record (2026-11-02), public RESULT.md.
6. *Sharp Riesz conditioning for consecutive triples on finite cycles*, published-finding corpus mathematical record (2026-10-11), public RESULT.md.
