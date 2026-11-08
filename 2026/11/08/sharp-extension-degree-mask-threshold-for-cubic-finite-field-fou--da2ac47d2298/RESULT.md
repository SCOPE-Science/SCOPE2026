# Sharp extension-degree mask threshold for cubic finite-field Fourier tomography

## Finding

Let \(F=\mathbb F_{p^m}\), with an odd prime \(p\ge5\), an integer \(m\ge1\), and \(q=p^m\). Fix a nontrivial additive character \(\psi:F\to\mathbb C\). For a nonempty set of cubic-curve curvature offsets \(\Lambda\subseteq F\), define the real linear map on Hermitian matrices \(A\in\operatorname{Herm}(q)\) by the complete profiles

\[
\rho_{\lambda,A}(x,t)=\sum_{a,b\in F}A_{ab}\,\psi\!\left(x(a-b)+t\big(a^3+\lambda a^2-b^3-\lambda b^2\big)\right),\quad(x,t)\in F^2,\quad\lambda\in\Lambda.
\]

Every output is real because \(A\) is Hermitian. Write \(\mathcal T_\Lambda A=(\rho_{\lambda,A}(x,t))_{\lambda,x,t}\). Choose any \(\lambda_0\in\Lambda\), and let

\[
H=\operatorname{span}_{\mathbb F_p}\{\lambda-\lambda_0:\lambda\in\Lambda\},\qquad h=\dim_{\mathbb F_p}H.
\]

**Exact real kernel and image dimensions** are

\[
\boxed{\dim_{\mathbb R}\ker\mathcal T_\Lambda=\frac{q-1}{2}(p^{m-h}+1),\qquad \operatorname{rank}_{\mathbb R}\mathcal T_\Lambda=q^2-\frac{q-1}{2}(p^{m-h}+1).}
\]

The traceless diagonal matrices always lie in the kernel and exhaust it **if and only if** \(H=F\). Thus the profiles determine every off-diagonal matrix entry and the trace, for every Hermitian input, exactly when the offset differences span \(F\) over its prime subfield. The smallest possible number of offsets for this property is **\(m+1\)**, attained by \(\Lambda=\{0,\beta_1,\dots,\beta_m\}\) for any \(\mathbb F_p\)-basis \((\beta_1,\dots,\beta_m)\). In particular, two offsets suffice over prime fields, but not over proper extension fields.

With exactly one offset, equip \(\operatorname{Herm}(q)\) with its Frobenius norm and \(\mathbb R^{F^2}\) with the normalized Euclidean norm \((q^{-2}\sum_{x,t}|\rho(x,t)|^2)^{1/2}\). Then the **complete real singular spectrum** of \(\mathcal T_{\{\lambda\}}\) is

| Singular value | Real multiplicity |
| --- | ---: |
| \(\sqrt q\) | \(1\) |
| \(\sqrt2\) | \((q-1)^2/2\) |
| \(1\) | \(q-1\) |
| \(0\) | \((q^2-1)/2\) |

For a rank-one matrix \(A=zz^*\), each \(\rho_{\lambda,A}\) is the squared Fourier magnitude of the complex signal \(z\) with deterministic polynomial phase \(a^3+\lambda a^2\). When \(H=F\), all signals with at least three nonzero coordinates are determined up to a common phase. Two-site unequal-modulus signals have exactly two solutions modulo common phase, two-site equal-modulus signals have one, and one-site signals have \(q\) solutions; these statements concern competing **rank-one signals** and do not assert full matrix recovery.

## Assumptions and scope

All sums are over the **full** field \(F\), and all \((x,t)\in F^2\) are measured separately for every offset. The odd-prime assumption excludes characteristic three because the cubic-difference quadratic coefficient vanishes there. The map is a linear measurement of Hermitian matrices, not a phase-retrieval assertion for every unrestricted signal at insufficient offsets. Changing the reference \(\lambda_0\) does not change \(H\). One may realize these offsets as translated cubic curves: for \(\kappa=\lambda/3\), the identity \((a+\kappa)^3=a^3+\lambda a^2+(\lambda^2/3)a+\kappa^3\) shows that the extra linear and constant terms can be absorbed by reindexing \(x\) and applying an irrelevant constant phase.

## Proof

**Fourier fibers.** Fix \(\lambda\). Define \(\phi_\lambda(a)=a^3+\lambda a^2\). The two-dimensional finite Fourier orthogonality identity, with the unnormalized synthesis above, gives

\[
\frac1{q^2}\sum_{x,t\in F}|\rho_{\lambda,A}(x,t)|^2
=\sum_{d,e\in F}\left|\sum_{\substack{a-b=d\\\phi_\lambda(a)-\phi_\lambda(b)=e}}A_{ab}\right|^2.
\]

Consequently, \(\mathcal T_\Lambda A=0\) if and only if every displayed fiber sum is zero for all offsets \(\lambda\). For \(d=0\), all pairs \((a,a)\) lie in the single fiber \((0,0)\); the only diagonal statistic is \(\operatorname{tr}A\). Therefore the diagonal contribution to the real kernel is exactly \(q-1\).

**The quadratic reflection for each nonzero difference.** Fix \(d\in F^\times\). Every ordered pair with \(a-b=d\) has a unique sum \(s=a+b\) and is given by \(a=(s+d)/2\), \(b=(s-d)/2\). Set \(f_d(s)=A_{(s+d)/2,(s-d)/2}\). Direct expansion gives

\[
\phi_\lambda(a)-\phi_\lambda(b)=d\left(\frac{3s^2+d^2}{4}+\lambda s\right).
\]

As \(p\ne2,3\), the fiber over a fixed value of this quadratic contains exactly the pair \(s\) and \(R_\lambda(s)=-s-4\lambda/3\), except at its unique fixed point. The fiber equations are therefore **equivalent** to

\[
f_d(s)=-f_d(R_\lambda(s))\quad \text{for all }s\in F,\quad\lambda\in\Lambda.
\]

At the fixed point, the equality requires \(f_d(s)=0\); no equations are lost.

**Composition and quotient.** Two reflections compose to translation:

\[
R_\lambda R_\mu(s)=s+\frac43(\mu-\lambda).
\]

Thus a solution \(f_d\) is invariant under translations from \(H\), because \(4/3\ne0\) is in \(\mathbb F_p\), and it is odd under the reflection induced by \(R_{\lambda_0}\). Conversely, these two conditions imply all the original reflection equations. On the additive quotient \(F/H\) of odd cardinality \(N=p^{m-h}\), any affine reflection \(\bar s\mapsto-\bar s-\bar c\) has exactly one fixed coset (since doubling is bijective) and \((N-1)/2\) disjoint two-cycles. An odd function on this quotient vanishes on the fixed coset and is otherwise freely prescribed on one member of each two-cycle. Hence for each nonzero \(d\), the solution space has complex dimension \((N-1)/2\).

Hermitian conjugation exchanges the spaces for \(d\) and \(-d\): \(f_{-d}(s)=\overline{f_d(s)}\). Since \(q\) is odd, there are \((q-1)/2\) unordered sign pairs \(\{d,-d\}\); each contributes \(N-1\) **real** kernel dimensions. Adding the traceless diagonal gives

\[
(q-1)+\frac{q-1}{2}(N-1)=\frac{q-1}{2}(N+1).
\]

The full Hermitian domain has real dimension \(q^2\), proving the rank formula. The odd-function space vanishes exactly when \(N=1\), proving the stated if-and-only-if and the sharp \(m+1\) offset threshold: at most \(k-1\) differences can span from \(k\) offsets, and a basis realizes equality.

**One-offset singular spectrum.** For fixed \(d\ne0\), the quadratic has one singleton fiber and \((q-1)/2\) disjoint two-element fibers. Each fiber sum is a row of Euclidean squared length respectively \(1\) or \(2\); distinct rows have disjoint supports. The Fourier transform is an isometry under the normalized output norm. Across each Hermitian sign pair \(\{d,-d\}\), complex row eigenvectors account for two real dimensions apiece, with singular values \(1\) and \(\sqrt2\). Multiplying by \((q-1)/2\) sign pairs gives multiplicities \(q-1\) and \((q-1)^2/2\). On the diagonal, the trace functional has singular value \(\sqrt q\) and nullity \(q-1\). The residual kernel dimension is \((q^2-1)/2\). This proves the entire spectrum with the precise stated norm conventions.

**Rank-one consequences.** Once all off-diagonal products \(z_a\overline{z_b}\) are known, a nonzero product identifies exactly the corresponding pair of support points. For three or more support points, any three distinct nonzero coordinates \(i,j,k\) give \(|z_i|^2=(z_i\overline{z_j})(z_k\overline{z_i})/(z_k\overline{z_j})\), yielding all moduli and phases up to a unit scalar. For two support points the product and trace determine the two squared moduli as unordered roots of \(u(q_0-u)=|z_i\overline{z_j}|^2\), with \(q_0=\operatorname{tr}(zz^*)\); unequal roots can be swapped and equal roots cannot. A single-site signal produces constant intensity independent of its location. These cases exhaust the rank-one fibers.

## Verification

The accompanying `CHECK.py` uses integer arithmetic for the field incidence matrices, including \(\mathbb F_{25}=\mathbb F_5[\alpha]/(\alpha^2-3)\), and independently constructs the quadratic fibers from the original cubic polynomials, rather than from the derived reflection formula. It compares exact matrix ranks to the claimed dimensions for fields of sizes \(5,7,11,13,25\), verifies the reflection for all tested parameters and positions, and constructs a nonzero two-offset kernel witness over \(\mathbb F_{25}\) which becomes observable under a third offset. Direct complex Fourier sums on prime fields \(5\) and \(7\) verify real-valuedness and the normalization of Parseval's identity. Run with `python3 CHECK.py` (Python standard library only). Finite tests are not a proof of the all-field theorem; the preceding argument is.

## Relationship to prior work

Biswas, Carneiro, Flock, Madrid, Oliveira e Silva, Stovall, and Tautges prove sharp scalar Fourier extension inequalities for complete moment curves over finite fields; this concerns a different functional and does not give the Hermitian matrix kernel, additive offset span criterion, or minimal deterministic cubic offset count. The earlier scalar finite-field extension work by González-Riquelme and Oliveira e Silva concerns sharp extension inequalities, principally for quadratic surfaces. Huang and Li study coded Fourier-intensity recovery with random masks and a PhaseLift algorithm, rather than an exact deterministic all-Hermitian span criterion for polynomial offsets. The standard full-translation quadratic/parabolic moment curve has different two-point difference geometry and cannot imply the cubic reflection obstruction from its own injective difference map.

## Limitations

The mask threshold is *optimal within the family* \(a^3+\lambda a^2\) with complete \((x,t)\) measurements, and for **recovery of arbitrary Hermitian matrices modulo traceless diagonals**. It is not a lower bound for arbitrary deterministic masks or general rank-one phase retrieval. No noise-stability optimum is asserted. Full diagonal recovery is impossible in these phase-only measurement families. Characteristic three and characteristic two are excluded. Unindexed equivalent constructions in phase-coded diffraction or algebraic finite-field tomography remain a possible originality limitation.

## References

1. C. Biswas, E. Carneiro, T. C. Flock, J. Madrid, D. Oliveira e Silva, B. Stovall, J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882 (first submitted 2026-09-24). https://arxiv.org/abs/2609.29882
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (2024). https://arxiv.org/abs/2405.16647
3. G. Huang and S. Li, *PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate*, arXiv:2608.02450 (2026-08-03). https://arxiv.org/abs/2608.02450
