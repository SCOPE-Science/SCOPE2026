# A single tail-order reversal for projective-plane coupon collection

## Finding

Let \(V\) be the thirteen points of the ternary projective plane \(\operatorname{PG}(2,3)\). Consider two independent-draw coverage mechanisms, each starting with no points discovered. In the **line mechanism** each draw selects uniformly one of the thirteen four-point projective lines. In the **full mechanism** each draw selects uniformly one of all \(\binom{13}{4}=715\) four-point subsets. Let \(T_{\mathrm L}\) and \(T_{\mathrm U}\) be the respective numbers of draws until every point has appeared, and put

\[
\Delta(t)=\Pr(T_{\mathrm L}>t)-\Pr(T_{\mathrm U}>t),\qquad t\in\mathbb Z_{\ge0}.
\]

**The complete tail-sign classification is**

\[
\boxed{\Delta(t)=0\ (0\le t\le3),\qquad
\Delta(4)=-\frac{15480}{2924207}<0,\qquad
\Delta(t)>0\ (t\ge5).}
\]

In particular, neither cover time first-order stochastically dominates the other. The line mechanism has the larger expected completion time (an earlier result), but a strictly larger probability of completing in four draws; for every later time it has a strictly larger probability of *not* having completed. There is exactly one transition between the strict signs.

## Assumptions and scope

All draws are independent across time and uniformly distributed within their specified finite block family; repeated blocks are permitted. Every projective line has four points, every point lies on four lines, and two distinct lines meet in one point. No other block-selection distributions, larger projective planes, or different stopping rules are included.

The plane is explicitly constructed over \(\mathbb F_3\): normalize each nonzero triple so its first nonzero coordinate equals one, giving thirteen projective points. For each such nonzero normalized normal vector \(a\), take the line \(\{x:a\cdot x=0\}\). This supplies all thirteen four-point lines without relying on any particular labeling.

## Proof

**1. Exact finite inclusion-exclusion.** For a block family \(\mathcal F\) of size \(m\), define \(h(U)=|\{B\in\mathcal F:B\cap U=\varnothing\}|\) for each nonempty set of points \(U\). Missing every point of \(U\) after \(t\) independent draws has probability \((h(U)/m)^t\). Hence, for every integer \(t\ge1\),

\[
\Pr(T>t)=\sum_{\varnothing\ne U\subseteq V}(-1)^{|U|+1}
\left(\frac{h(U)}m\right)^t.
\]

For the projective lines, group the complete \(2^{13}-1=8191\) nonempty-point-subset sum by \(h(U)\). The nonzero signed coefficients are

| \(h\) | 9 | 6 | 4 | 3 | 2 | 1 | 0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(\sum_{U:h(U)=h}(-1)^{|U|+1}\) | 13 | -78 | 234 | -182 | -78 | 130 | -38 |

These numbers follow from exhaustive finite enumeration of the explicitly defined thirteen projective lines, or from the independently enumerated covering-subfamily counts in `verify.py`. Both complete algorithms and the exact tables are included in that standalone source. The \(h=0\) term vanishes when \(t\ge1\).

For the full mechanism, a missed set of size \(j\) is avoided by exactly \(\binom{13-j}{4}\) blocks if \(j\le9\), and by none otherwise. The resulting nonzero coefficient table is

| \(h\) | 495 | 330 | 210 | 126 | 70 | 35 | 15 | 5 | 1 | 0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| coefficient | 13 | -78 | 286 | -715 | 1287 | -1716 | 1716 | -1287 | 715 | -220 |

Consequently the common leading terms \(13(9/13)^t-78(6/13)^t\) cancel in \(\Delta(t)\). Since \(13\mid715\), the remaining terms have the common denominator \(715^t\). Write \(\Delta(t)=H_t/715^t\), where for every integer \(t\ge1\),

\[
\begin{aligned}
H_t={}&234\,220^t-286\,210^t-182\,165^t+715\,126^t
-78\,110^t\\
&-1287\,70^t+130\,55^t+1716\,35^t
-1716\,15^t+1287\,5^t-715.
\end{aligned}
\]

**2. Exact early-time signs.** No three blocks of cardinality four can cover thirteen points, so both survival probabilities are one for \(0\le t\le3\). Substitution of \(t=4,5\) in the preceding integer expression gives

\[
\Delta(4)=-\frac{15480}{2924207},\qquad
\Delta(5)=\frac{2178216}{418161601}.
\]

For completeness, direct substitution gives the following further exact values (each positive):

| \(t\) | \(\Delta(t)\) |
|---:|---:|
| 6 | \(10152590256/1494927723575\) |
| 7 | \(4640087167632/1068873322356125\) |
| 8 | \(125140871786616/58788032729586875\) |
| 9 | \(495968412295551384/546434764221510003125\) |

The independent covering-subfamily and covered-state calculations in `verify.py` also check the underlying distributions.

**3. Every remaining time.** For \(t\ge10\), discard the four *positive* nonleading terms of \(H_t\), and divide the remaining expression by \(234\,220^t\). The ratio of the six negative terms to that positive leading term is

\[
\begin{aligned}
B_t={}&\frac{286}{234}\left(\frac{21}{22}\right)^t
+\frac{182}{234}\left(\frac34\right)^t
+\frac{78}{234}\left(\frac12\right)^t\\
&+\frac{1287}{234}\left(\frac7{22}\right)^t
+\frac{1716}{234}\left(\frac3{44}\right)^t
+\frac{715}{234}\left(\frac1{220}\right)^t.
\end{aligned}
\]

Every base lies strictly between zero and one. Exact rational arithmetic yields \(B_{10}=70560095920809667968751/86923383681024000000000<41/50<1\); therefore \(B_t\le B_{10}<1\) for all integers \(t\ge10\). It follows that \(H_t\ge234\,220^t(1-B_t)>0\) for all such times. This proves the entire infinite tail-sign classification, not just a finite numerical range.

## Verification

Run `python verify.py` using Python's standard library. Its assertions exhaust all \(8191\) nonempty point sets, confirm the complete projective incidence relation, enumerate all \(8191\) nonempty subfamilies of thirteen lines, and independently compare the inclusion-exclusion results against covered-set dynamic programming at times four and five for both models. They confirm both exact crossing fractions, the positive signs at times five through nine, and the exact rational inequality for the analytic bound covering *all* times ten and later.

The program additionally reconstructs the already-known mean values

\[
\mathbb E[T_{\mathrm L}]=\frac{43633}{4620},\qquad
\mathbb E[T_{\mathrm U}]=\frac{1746879067753}{185252315340},
\]

only as independent consistency tests, not as new findings. Complete finite enumeration establishes the finite coefficient tables; the positive exponential bound is the step that turns those tables into a theorem over every integer time.

## Relationship to prior work

Barak-Pelleg and Berend [1, Theorem 2.1 and Section 3] introduced the projective-plane mechanism and proved the strict **expectation** inequality at plane orders two, three and four; in particular the preceding exact means are theirs. They enumerate covering sets and invoke classical inclusion-exclusion but do not state the present thirteen-point tail-sign classification or its one-transition proof. Grünbaum and Yaakobi [2] analyze group-coverage structures and monotonicity, and Berend and Sher [3] compare expected times for other group-selection distributions. The general inclusion-exclusion principle and all previously reported means are fully credited.

The new statement is limited to the complete *distributional sign comparison* on the natural next projective plane. It neither restates the already-established seven-point comparison as new nor follows merely from an inequality between expectations: the line mechanism has both an increased chance of very early coverage and a heavier tail at all times five and later.

## Limitations

The theorem does not classify arbitrary fair mechanisms or projective planes of order four and above. It does not provide a coupling between the two processes, a universal increasing-convex ordering, or an optimality theorem for all distributions on four-subsets. The certificate is a complete finite computation only for the thirteen-point coefficients; infinite-time validity follows from the stated analytic inequality. The comparison with relevant published results is a best-knowledge priority assessment, not an independent publication-priority determination.

## References

[1] D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1 (first submitted June 26, 2026), especially Theorem 2.1 and Section 3. https://arxiv.org/pdf/2606.28216v1

[2] E. Grünbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305v1 (2025). https://arxiv.org/html/2510.25305v1

[3] D. Berend and T. Sher, *On a Conjecture on Uniform Group Drawings in the Coupon Collector Problem*, arXiv:2509.17201v2 (2026 revision of 2025 preprint). https://arxiv.org/html/2509.17201v2
