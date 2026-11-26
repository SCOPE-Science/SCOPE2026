# Sharp seed-energy rigidity and frame-index dichotomy for contractive weighted shifts

## Finding

Let \(W e_n=w_n e_{n+1}\) on \(\ell^2(\mathbb N_0)\), with \(0<w_n\le 1\). If the forward orbits of a finite or countable seed family \((g_j)_j\) form a frame with lower bound \(A>0\), then the total seed energy satisfies
\[
E:=\sum_j\|g_j\|^2\ \ge\ A\left(1+\sum_{n=0}^\infty(1-w_n^2)\right).
\]
This bound is attained by the canonical defect seeds, with the equality interpreted in the extended-real sense when both sides are infinite. Equality with finite energy forces the orbit frame to be \(A\)-tight and the time-zero frame operator to be \(A(I-WW^*)\). The least cardinality of a minimizing seed family is the rank of \(I-WW^*\), interpreted as countably infinite in the infinite-rank case.

The minimum number of seeds for an orbit frame, regardless of energy, is one if \(\prod_{n=0}^\infty w_n>0\) and countably infinite if \(\prod_{n=0}^\infty w_n=0\). The latter conclusion holds even when \(\|W\|=1\). In the positive-product case, finite seed families attain the sharp energy if and only if only finitely many weights are less than one. Otherwise explicit finite families have energies decreasing to the infimum without attaining it.

## Assumptions and scope

The Hilbert space is complex with its standard orthonormal basis. All forward time indices \(k\in\mathbb N_0\) and all seeds are counted with multiplicities. A frame has bounds \(A,B\), for \(0<A\le B<\infty\), if
\[
A\|f\|^2\le\sum_j\sum_{k=0}^\infty |\langle f,W^k g_j\rangle|^2\le B\|f\|^2
\qquad(f\in\ell^2).
\]
Write \(x_n=1-w_n^2\), \(D=\sum_n x_n\), and \(\beta_n=\prod_{j=0}^{n-1}w_j\) with \(\beta_0=1\). Since \(-\log(1-x)\ge x\) on \([0,1)\) and \(-\log(1-x)\le 2x\) for \(0\le x\le 1/2\), \(D<\infty\) is equivalent to a positive weight product. When \(D<\infty\), let \(P_m=\prod_{j=m}^\infty w_j\). For each \(N\ge 0\) a finite family is given by
\[
\sqrt A\,e_0,\qquad \sqrt{Ax_j}\,e_{j+1}\quad(0\le j<N),\qquad
\sqrt{A(P_{N+1}^{-2}-w_N^2)}\,e_{N+1},
\]
omitting zeros. Its optimal lower bound is \(A\), its upper bound is at most \(A/P_{N+1}^2\), and its energy is
\[
E_N=A\left(\sum_{j=0}^N x_j+P_{N+1}^{-2}\right).
\]
The excess \(E_N-A(1+D)=A(P_{N+1}^{-2}-1-\sum_{j>N}x_j)\) is nonnegative and nonincreasing in \(N\), and tends to zero.

## Proof

**Energy bound.** Let \(S\) be the bounded orbit frame operator and let \(Q\) be the time-zero frame operator (the seed vectors are Bessel but need not be a frame on the whole space). The strongly converging positive operator sums give \(S=Q+WSW^*\) and \(AI\le S\le BI\). Put \(s_n=\langle Se_n,e_n\rangle\), \(q_n=\langle Qe_n,e_n\rangle\). Then \(q_0=s_0\), and \(q_{n+1}=s_{n+1}-w_n^2s_n\ge 0\). It follows that
\[
\sum_{n=0}^M q_n=s_M+\sum_{n=0}^{M-1}x_ns_n\ge A\left(1+\sum_{n=0}^{M-1}x_n\right).
\]
By summing squares of the basis coefficients of the seeds, \(\sum_n q_n=\sum_j\|g_j\|^2\), allowing infinity. Taking \(M\to\infty\) proves the bound.

**Sharpness and equality.** The adjoint \(W^*\) is strongly stable: its powers annihilate every finitely supported vector eventually and are contractions. For \(Q_0=A(I-WW^*)\), the diagonal seed vectors \(\sqrt A e_0\) and \(\sqrt{Ax_n}e_{n+1}\) give
\[
\sum_{k=0}^{M-1}W^kQ_0W^{*k}=A(I-W^MW^{*M})\ \longrightarrow\ AI
\]
in the strong operator topology. These seeds, omitting zeros, attain the energy bound. If equality holds for finite energy, then \(D<\infty\) and \(\beta_n\to\beta_\infty>0\). From the recurrence,
\[
s_n=\beta_n^2s_0+\sum_{k=1}^n(\beta_n/\beta_k)^2 q_k.
\]
The coefficients in the sum are bounded by one and converge for each fixed \(k\), while \(\sum_k q_k<\infty\), so \(s_n\) has a limit \(\ell\ge A\). Taking limits in the partial trace yields \(E=\ell+\sum_n x_ns_n\). Equality forces \(\ell=A\) and \(s_n=A\) whenever \(x_n>0\). For any \(n\) with \(x_n=0\), the sequence \(s_n,s_{n+1},\ldots\) is nondecreasing up to the next positive-deficit index, where its value is \(A\); if there is no such index, it is nondecreasing with limit \(A\). In either case \(s_n=A\). The positive operator \(S-AI\) with vanishing diagonal has all entries zero by Cauchy–Schwarz for its positive form. This proves \(S=AI\) and \(Q=Q_0\). A sum of fewer than \(\operatorname{rank}Q_0\) rank-one operators cannot factor \(Q_0\); the canonical seeds use exactly \(1+\#\{n:w_n<1\}\). If \(D=\infty\), the bound excludes every finite family, and the canonical family and the defect rank are both countably infinite.

**Frame index.** When the weight product is positive, \(\{W^n e_0\}_n=\{\beta_ne_n\}_n\) is a Riesz basis because \(\beta_\infty\le\beta_n\le 1\). When the product vanishes, \(D=\infty\) and the energy bound rules out all finite seed families; the canonical countable family still works. This gives the stated dichotomy including zero-product shifts of norm one.

**Finite approximants.** For the finite family displayed above, the orbit operator is diagonal with entries \(A\) for \(0\le k\le N\): the recurrence is \(s_0=A\), \(s_{k+1}=w_k^2s_k+Ax_k=A\) up to \(k=N-1\). The booster gives \(s_{N+1}=A/P_{N+1}^2\). Each subsequent entry is \(s_k=A/P_k^2\) by multiplication by the intervening squared weights. Since \(P_{N+1}\le P_k\le 1\) for \(k\ge N+1\), the bounds follow, and adding the seed norms gives the energy formula. Set \(R_N=P_{N+1}^{-2}\); then \(R_{N+1}=w_{N+1}^2 R_N\) and
\[
E_N-E_{N+1}=A x_{N+1}(R_N-1)\ge 0.
\]
Because \(P_{N+1}\to 1\) and \(\sum_{j>N}x_j\to 0\), the excess tends to zero. A finite family achieves equality only if \(Q_0\) is finite rank, equivalently there are only finitely many positive \(x_n\); that condition is also sufficient by the canonical construction.

**Boundary examples.** For \(w_n^2=(n+1)/(n+2)\), \(\beta_m^2=1/(m+1)\to 0\), \(D=\sum_{n\ge 0}(n+2)^{-1}=\infty\), and \(\|W\|=1\), so no finite seed family works. For \(w_n^2=1-(n+2)^{-2}\), the squared product telescopes to \(1/2\), \(D=\zeta(2)-1\), and the finite-seed infimum is \(A\zeta(2)\) but is not attained by any finite family.

## Verification

The proof uses exact identities and does not depend on numerical diagnostics. The accompanying standard-library `checker.py` checks finite rational examples of the Stein recurrence, booster coefficients, energy excess and boundary-product telescoping. Its expected output is `SHIFT_ORBIT_ENERGY_EXACT_OK 217235`. These finite checks do not certify the infinite theorem; in particular, monotonicity of the approximating energies follows from the exact difference identity in the proof.

## Relationship to prior work

Gwizdek, Kużel and Majdak [1, §§3.3–3.5 and §3.7.5] give defect and Stein machinery, the canonical weighted-shift defect seeds, the positive-product one-generator Riesz basis, and the infinite-index conclusion when \(\sup_n w_n<1\). Aguilera, Cabrelli, Negreira and Paternostro [2, Theorems 1.3 and 4.2] identify the Parseval index with the defect rank and characterize the unrestricted index through similar contractions. In particular, once finite-energy equality is shown to imply tightness, the equality cardinality agrees with that known Parseval index. The contribution here is the sharp total seed budget for an arbitrary orbit frame of the shift, finite-energy equality rigidity and finite-family approximation, and the use of the budget to exclude finite frame generators for every zero-product shift, including the norm-one boundary. The survey [3] gives further dynamical-sampling context.

## Limitations

The scope is positive contractive unilateral shifts and the squared norms of their initial seeds, not general operators or physical acquisition cost. There is no historical priority guarantee beyond the comparisons given here.

## References

1. S. Gwizdek, S. Kużel and W. Majdak, *Dynamical frames through Sz.-Nagy–Foiaș dilations*, https://arxiv.org/abs/2611.20029.
2. A. Aguilera, C. Cabrelli, F. Negreira and V. Paternostro, *Optimal Dynamical Frames*, https://arxiv.org/abs/2506.00567.
3. A. Aldroubi, C. Cabrelli, I. Krishtal and U. Molter, *Dynamical Sampling: A Survey*, *La Matematica* 5 (2026), article 37, https://doi.org/10.1007/s44007-026-00215-y.
