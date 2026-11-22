# Sharp seed-energy rigidity and frame-index dichotomy for contractive weighted shifts

## Finding

For every positive contractive unilateral weighted shift \(We_n=w_ne_{n+1}\), \(0<w_n\le1\), the total squared norm of the initial vectors of any orbit frame with lower bound \(A>0\) is at least
\[
\boxed{A\left(1+\sum_{n=0}^{\infty}(1-w_n^2)\right).}
\]
The bound is sharp, even when infinite, and equality for finite total seed energy forces the *entire orbit frame* to be \(A\)-tight and its initial-vector frame operator to equal \(A(I-WW^*)\). In particular, the least cardinality of an equality-attaining family is the rank of \(I-WW^*\).

Moreover, the least possible number of generators of **any** orbit frame has the exact dichotomy
\[
\boxed{\gamma(W)=1\quad\Longleftrightarrow\quad\prod_{n=0}^{\infty}w_n>0,
\qquad\gamma(W)=\infty\quad\Longleftrightarrow\quad\prod_{n=0}^{\infty}w_n=0.}
\]
The second assertion includes the critical case \(\|W\|=1\). When the product is positive, the sharp seed-energy infimum is attainable by a *finite* generator family if and only if only finitely many weights are strictly below one. Otherwise finite generator families approach the infimum but never attain it, with explicit formulas below.

## Assumptions and scope

Work on the complex Hilbert space \(\ell^2(\mathbb N_0)\) with standard orthonormal basis \((e_n)\). Fix arbitrary real weights \(0<w_n\le1\) and a real number \(A>0\). Let \(J\) be finite or countable, and let \((g_j)_{j\in J}\subset\ell^2\). Its orbit family consists of \(\{W^kg_j:k\in\mathbb N_0,\ j\in J\}\), including multiplicities. It is a frame with lower bound \(A\) if there exists a finite \(B\ge A\) such that
\[
A\|f\|^2\le\sum_{j\in J}\sum_{k=0}^{\infty}|\langle f,W^kg_j\rangle|^2\le B\|f\|^2
\quad(f\in\ell^2).
\]
Define initial seed energy \(E=\sum_j\|g_j\|^2\in[0,\infty]\), deficit \(x_n=1-w_n^2\), \(D=\sum_nx_n\), and \(\beta_n=\prod_{j=0}^{n-1}w_j\), with \(\beta_0=1\). The positive infinite product \(\prod_nw_n\) may vanish. The frame index \(\gamma(W)\) is the smallest finite number of initial vectors that yields an orbit frame, or \(\infty\) when no finite number suffices.

When \(D<\infty\), put \(P_m=\prod_{j=m}^{\infty}w_j>0\). For each \(N\ge0\), define a finite generator family consisting of
\[
\sqrt A\,e_0,\qquad \sqrt{Ax_j}\,e_{j+1}\quad(0\le j<N),\qquad
\sqrt{A\big(P_{N+1}^{-2}-w_N^2\big)}\,e_{N+1},
\]
omitting any zero generators. The family has lower bound exactly \(A\) and upper bound at most \(A/P_{N+1}^2\); its energy is
\[
E_N=A\left(\sum_{j=0}^{N}x_j+P_{N+1}^{-2}\right),
\quad E_N-A(1+D)=A\left(P_{N+1}^{-2}-1-\sum_{j>N}x_j\right)\longrightarrow0
\]
in the sense that the displayed nonnegative difference converges to zero (not necessarily monotonically as a function of \(N\)). Thus the finite-generator infimum is \(A(1+D)\).

## Proof

**1. The Stein identity and the universal lower bound.** Let \(S\) be the bounded positive frame operator of the orbit family. By summing the orbit series and shifting its time index,
\[
S=Q+WSW^*,\qquad Q=\sum_{j\in J}\langle\,\cdot,g_j\rangle g_j\ge0,
\qquad AI\le S\le BI.
\]
The series defining \(Q\) converges strongly because the time-zero vectors are a Bessel family. Write \(s_n=\langle Se_n,e_n\rangle\) and \(q_n=\langle Qe_n,e_n\rangle\). Since \(W^*e_0=0\) and \(W^*e_{n+1}=w_ne_n\),
\[
q_0=s_0,\qquad q_{n+1}=s_{n+1}-w_n^2s_n\ge0.
\]
For every integer \(M\ge0\), telescoping gives
\[
\sum_{n=0}^{M}q_n=s_M+\sum_{n=0}^{M-1}x_ns_n
\ge A\left(1+\sum_{n=0}^{M-1}x_n\right).
\]
Because \(\sum_nq_n=\operatorname{Tr}Q=\sum_j\|g_j\|^2=E\) (Tonelli, allowing infinity), taking the supremum over \(M\) yields \(E\ge A(1+D)\). In particular, if \(D=\infty\), every orbit frame uses infinite seed energy and cannot have finitely many generators.

**2. Sharpness, equality, and rigidity.** The adjoint \(W^*\) is strongly stable: for any finitely supported \(f\), \(W^{*k}f=0\) for all sufficiently large \(k\), and \(\|W^{*k}\|\le1\), so density gives the claim for every \(f\). Take \(Q_0=A(I-WW^*)\), which is diagonal with coefficients \(A,Ax_0,Ax_1,\ldots\). The corresponding canonical initial vectors \(\sqrt A\,e_0\) and \(\sqrt{Ax_n}\,e_{n+1}\) yield
\[
\sum_{k=0}^{M-1}W^kQ_0W^{*k}=A(I-W^MW^{*M})\xrightarrow[M\to\infty]{\mathrm{s.o.t.}} AI.
\]
They therefore form an \(A\)-tight orbit frame and have energy \(A(1+D)\), including when \(D=\infty\).

For rigidity, assume \(D<\infty\) and \(E=A(1+D)<\infty\). Since \(w_n>0\) and \(\sum_n(1-w_n^2)<\infty\), \(\beta_n\downarrow\beta_\infty>0\). The diagonal Stein recurrence can be solved as
\[
s_n=\beta_n^2s_0+\sum_{k=1}^n\left(\frac{\beta_n}{\beta_k}\right)^2q_k.
\]
As \(\sum_kq_k=E<\infty\) and the coefficients are bounded by one, dominated convergence shows that \(s_n\) has a limit \(L\ge A\). Passing to the limit in the telescoping formula, using \(\sum_nx_n<\infty\) and \(s_n\le B\), yields
\[
E=L+\sum_{n=0}^{\infty}x_ns_n.
\]
Equality with \(A(1+D)\) forces \(L=A\) and \(s_n=A\) whenever \(x_n>0\). If \(x_n=0\), the recurrence gives \(s_{n+1}\ge s_n\). On each maximal block of such indices, its endpoints are pinned to \(A\) by either a positive-deficit index, the lower bound \(s_0\ge A\), or the limit \(L=A\). Hence \(s_n=A\) for **every** \(n\). Since \(S-AI\ge0\) has zero diagonal in an orthonormal basis, its entries all vanish by the positive-form Cauchy–Schwarz inequality. Therefore \(S=AI\) and \(Q=A(I-WW^*)\). Conversely this identity clearly achieves equality. The minimum number of seed vectors in an equality family is \(\operatorname{rank}Q=1+\#\{n:w_n<1\}\), interpreting an infinite cardinal as countably infinite; this rank is achieved by the canonical diagonal factorization.

**3. Exact frame index.** If \(D=\infty\), step 1 excludes every finite seed family; step 2 still gives a countable Parseval frame, hence \(\gamma(W)=\infty\). If \(D<\infty\), then \(\inf_n\beta_n=\beta_\infty>0\); the single orbit \(\{W^ne_0=\beta_ne_n:n\ge0\}\) is a Riesz basis, so \(\gamma(W)=1\). Since \(0<w_n\le1\), \(D<\infty\) is equivalent to positivity of \(\prod_nw_n\). This proves the dichotomy even when \(\sup_nw_n=1\).

**4. Finite-generator approximation.** The finite family displayed in the scope section is a sum of coordinate-supported seed vectors. Its frame operator is diagonal. For \(k\le N\), its \(k\)-th diagonal entry is exactly \(A\) by telescoping the first \(k\) defect contributions. At \(k=N+1\), the entry equals \(A(w_N^2+P_{N+1}^{-2}-w_N^2)=A/P_{N+1}^2\). At each \(k>N+1\), multiplication by the subsequent squared weights gives \(A/P_k^2\), between \(A\) and \(A/P_{N+1}^2\). Consequently it is an orbit frame with the claimed bounds and energy. The nonnegative energy excess tends to zero since \(P_{N+1}\to1\) and \(\sum_{j>N}x_j\to0\). If infinitely many \(x_n\) are positive, equality cannot occur for any finite generator family by the infinite rank of \(Q_0\); if finitely many are positive, the canonical equality family is finite. This completes the classification.

**5. Two exact boundary examples.** For \(w_n^2=(n+1)/(n+2)\), \(\beta_m^2=1/(m+1)\to0\), \(D=\sum_{n\ge0}(n+2)^{-1}=\infty\), and \(\sup_n w_n=1\). Thus \(\gamma(W)=\infty\), despite \(\|W\|=1\). For \(w_n^2=1-(n+2)^{-2}\), \(\prod_nw_n^2=1/2\), \(D=\zeta(2)-1\), and the finite-seed energy infimum is \(A\zeta(2)\), unattained by every finite family because each \(x_n>0\).

## Verification

The self-contained program `checker.py` verifies finite rational instances of the Stein recurrence, the finite booster coefficients, the exact energy excess and the sample infinite-family telescoping identities, with **217235 assertions**. Run `python checker.py` using Python 3 and its standard library; expected output: `SHIFT_ORBIT_ENERGY_EXACT_OK 217235`. The infinite-frame, sharp-infimum, equality and cardinality statements follow from the analytic proof above, not from the finite diagnostic.

## Relationship to prior work

Gwizdek, Kużel and Majdak [1], especially Section 3.7.5, identify the canonical defect generators and give a one-generator Riesz basis when the full weight product is positive; they prove infinite frame index under the stronger strict-contraction assumption \(\sup_nw_n<1\). Sections 3.3–3.5 establish general defect-space and Stein-equation principles. The present statement uses those principles but isolates the arbitrary norm-one zero-product boundary and proves a global **minimal total seed energy**, its equality rigidity, and explicit finite-family energy approximants. These sharp budget and nonattainment assertions are not stated in [1].

Aguilera, Cabrelli, Negreira and Paternostro [2] give the general abstract frame-index/Parseval-index framework. Their general characterization concerns minimum generator cardinality and does not itself provide the explicit lower energy bound, all-case weighted-shift dichotomy, or the finite-generator energy-limit formula here. A 2026 dynamical sampling survey [3] provides context for orbit frames and Parseval constructions. Some general parts (canonical Parseval factorization and Stein equation) are deliberately cited rather than asserted to be new.

## Limitations

The result concerns **positive contractive one-sided shifts** and the energy of the initial seed vectors; it does not classify noncontractive shifts, general operators, or physical acquisition cost. The lower bound scales with the specified frame lower bound \(A\). The theorem uses infinite forward orbits and may require countably many seeds to attain equality. Its originality is checked against the listed accessible sources and literature searches but unindexed frame-optimization literature could contain an equivalent formulation; independent mathematical audit has not been performed.

## References

1. S. Gwizdek, S. Kużel and W. Majdak, *Dynamical frames through Sz.-Nagy–Foiaș dilations*, arXiv:2611.20029v1 (15 November 2026), especially Sections 3.3–3.7.5. https://arxiv.org/abs/2611.20029
2. A. Aguilera, C. Cabrelli, F. Negreira and V. Paternostro, *Optimal Dynamical Frames*, arXiv:2506.00567, especially the Parseval frame-index and general index characterizations. https://arxiv.org/abs/2506.00567
3. A. Aldroubi, C. Cabrelli, I. Krishtal and U. Molter, *Dynamical Sampling: A Survey*, *La Matematica* 5 (2026), article 37. https://doi.org/10.1007/s44007-026-00215-y
