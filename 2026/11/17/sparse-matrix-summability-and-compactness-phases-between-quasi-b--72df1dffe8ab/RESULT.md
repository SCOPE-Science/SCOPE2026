# Sparse-matrix summability and compactness phases between quasi-Banach sequence spaces

## Finding

Let \(0<p,t<1\), let \(d\ge1\) be an integer, and let \(A=(a_{ij})_{i,j\ge1}\) be a complex matrix with at most \(d\) nonzero entries in each row. Assume each column belongs to \(\ell_t\), and put

\[
c_j=\left(\sum_{i\ge1}|a_{ij}|^t\right)^{1/t},\qquad
q_t=\frac{t}{1-t},\qquad
r_{p,t}=\begin{cases}\infty,&p\le t,\\pt/(p-t),&p>t.\end{cases}
\]

Initially define \(T_Ax=(\sum_j a_{ij}x_j)_i\) on finitely supported sequences. The following assertions hold, simultaneously for all such matrices, including matrices with arbitrary complex signs.

1. **Boundedness:** \(T_A\) extends to a bounded map \(\ell_p\to\ell_t\) if and only if \((c_j)\in\ell_{r_{p,t}}\). In that case
   \[
   d^{-1/t}\|c\|_{r_{p,t}}\le\|T_A\|_{\ell_p\to\ell_t}\le\|c\|_{r_{p,t}}.
   \]
   When \(p\le t\), the exact norm is \(\|T_A\|=\sup_jc_j\), without the loss factor.
2. **Absolute summability:** For bounded \(T_A\), the following are equivalent:
   \[
   c\in\ell_{q_t};\qquad T_A\in\Pi_{(2,1)}(\ell_p,\ell_t);\qquad
   T_A\in\bigcup_{1\le s\le r<\infty}\Pi_{(r,s)}(\ell_p,\ell_t).
   \]
   If these fail, then a *single* weakly \(1\)-summable input sequence witnesses failure of every \((r,s)\)-absolute summability condition with \(1\le s\le r<\infty\).
3. **Compactness:** If \(p>t\), every bounded \(T_A\) is compact. If \(p\le t\), then
   \[
   \|T_A\|_{\mathrm{ess}}=\limsup_{j\to\infty}c_j,
   \]
   where the essential quasi-norm is distance to compact operators; in particular, compactness is equivalent to \(c_j\to0\). In every exponent regime, the compact signed difference operator
   \[
   (D_tx)_i=i^{-1/q_t}x_i-(i+1)^{-1/q_t}x_{i+1}
   \]
   fails **all** finite \((r,s)\)-absolute summability conditions.

For comparison, the finite-support \(\ell_1\)-amplification
\[
\mathcal B_t(A)=\sup\{\|T_Ax\|_t:x\in c_{00},\ \|x\|_1\le1\}
\]
satisfies \(d^{-1/t}\|c\|_{q_t}\le\mathcal B_t(A)\le\|c\|_{q_t}\) with extended-real conventions. For entrywise nonnegative matrices the lower constant improves to \(d^{-1/q_t}\), and **that improved constant is sharp** for each \(d\) (one output row summing exactly \(d\) inputs). The bounded-row-degree assumption is essential: the rank-one map \(x\mapsto(\sum_jx_j)e_1\) is compact and absolutely summing although all its column norms equal one.

## Assumptions and scope

The spaces are complex \(\ell_u(\mathbb N)\), \(0<u<1\), with \(\|x\|_u=(\sum|x_j|^u)^{1/u}\). Their continuous duals identify with \(\ell_\infty\) through coordinate pairing. A sequence \((x^{(k)})\subset\ell_p\) is weakly \(s\)-summable when \(\sum_k|f(x^{(k)})|^s<\infty\) for every continuous linear functional \(f\); \(T\in\Pi_{(r,s)}\) when every such sequence has \(\sum_k\|Tx^{(k)}\|_t^r<\infty\). The quasi-norm on operators is \(\sup_{\|x\|_p\le1}\|Tx\|_t\). All sums over empty sets are zero and \(\|c\|_\infty=\sup_jc_j\). The result is restricted to uniformly bounded row support, not bounded column support, band width, or a positivity hypothesis.

## Proof

**1. A random-phase lemma.** If \(z_1,\ldots,z_m\in\mathbb C\), \(m\le d\), and \(\zeta_j\) are independent uniform points of the complex unit circle, then
\[
\mathbb E\left|\sum_{j=1}^m\zeta_jz_j\right|^t\ge
\max_{1\le j\le m}|z_j|^t\ge\frac1d\sum_{j=1}^m|z_j|^t.
\]
Indeed, conditioning on the other phases, the average of \(|b+a\zeta|^t\) over \(|\zeta|=1\) is at least \(|a|^t\): its distribution equals that of \(|a+b\zeta|^t\), and the mean-value inequality for the subharmonic function \(|z|^t\) at the center \(a\) applies. Now remove the conditioning and maximize over \(j\). For finite-support nonnegative amplitudes \((u_j)\), sum over rows and use Tonelli to obtain
\[
\mathbb E\left\|T_A(\zeta_ju_j)_j\right\|_t^t
\ge\frac1d\sum_jc_j^tu_j^t.\tag{1}
\]
The opposite bound for arbitrary finitely supported complex \(x\) is the \(t\)-triangle inequality:
\[
\|T_Ax\|_t^t\le\sum_jc_j^t|x_j|^t.\tag{2}
\]
Here each row contains at most \(d\) nonzero terms, but the columns may have infinitely many nonzero terms; all manipulations are valid by positivity of the summed powers.

**2. The scalar diagonal optimization.** For \(v_j\ge0\) and finite-support \(u\ge0\), define \(F_{p,t}(v)=\sup_{\|u\|_p\le1}(\sum_j(v_ju_j)^t)^{1/t}\). Hölder gives
\[
F_{p,t}(v)=\begin{cases}\sup_jv_j,&p\le t,\\(\sum_jv_j^{pt/(p-t)})^{(p-t)/(pt)},&p>t.\end{cases}\tag{3}
\]
For the second case, equality on each finite set follows by choosing \(u_j\) proportional to \(v_j^{t/(p-t)}\); the first case follows from \(\|u\|_t\le\|u\|_p\) and testing coordinate vectors. The corresponding optimization with \(\|u\|_1\le1\) always gives \(\|v\|_{q_t}\), since \(1>t\).

Apply (1) and (2) to the optimizations. A supremum over input phases in (1) is at least the expectation, so the operator quasi-norm on \(c_{00}\) lies between \(d^{-1/t}F_{p,t}(c)\) and \(F_{p,t}(c)\), as claimed. If this supremum is finite, (2) gives uniform boundedness on \(c_{00}\) and the operator extends uniquely by completeness of \(\ell_p\) and \(\ell_t\). If it is infinite, no bounded extension exists. When \(p\le t\), the upper bound is \(\sup c_j\), attained as a supremum by the unit vectors \(e_j\). The same argument with input \(\ell_1\) yields the asserted \(\mathcal B_t(A)\) bounds.

For nonnegative entries and nonnegative inputs, the elementary concavity inequality
\[
\left(\sum_{j=1}^m b_j\right)^t\ge m^{t-1}\sum_{j=1}^mb_j^t\ge d^{t-1}\sum_{j=1}^mb_j^t
\]
replaces (1). Hence \(\mathcal B_t(A)\ge d^{-(1-t)/t}\|c\|_{q_t}=d^{-1/q_t}\|c\|_{q_t}\). For a single row containing \(d\) ones, \(\mathcal B_t=1\) and \(\|c\|_{q_t}=d^{1/q_t}\), proving sharpness. No optimality is asserted for the signed-complex \(d^{-1/t}\) bound.

**3. Summability dichotomy.** If \(c\notin\ell_{q_t}\), the lower \(\mathcal B_t\) bound shows that for each positive integer \(k\), there is finitely supported \(y^{(k)}\) with \(\|y^{(k)}\|_1\le1\) and \(\|T_A y^{(k)}\|_t\ge2^k\). Let \(x^{(k)}=2^{-k}y^{(k)}\). Then \(\sum_k\|x^{(k)}\|_1\le1\), so the dual identification with \(\ell_\infty\) makes the sequence weakly \(1\)-summable, and therefore weakly \(s\)-summable for every \(s\ge1\). Yet \(\|T_Ax^{(k)}\|_t\ge1\) for every \(k\). The same sequence defeats all admissible \((r,s)\).

If \(c\in\ell_{q_t}\), (2) and Hölder give \(\|T_Ax\|_t\le\|c\|_{q_t}\|x\|_1\) on finite-support vectors. Thus \(T_A\) factors as the natural inclusion \(\ell_p\hookrightarrow\ell_1\), followed by a bounded map \(\ell_1\to\ell_t\). A weakly \(1\)-summable sequence in \(\ell_p\) is weakly \(1\)-summable after inclusion in \(\ell_1\). By the classical Orlicz theorem for \(\ell_1\), its \(\ell_1\)-norms are square summable. The factorization makes the output \(\ell_t\)-quasi-norms square summable. Thus \(T_A\in\Pi_{(2,1)}\), giving all equivalences. This proves the common-witness statement independently of the qualitative diagonal examples in the literature.

**4. Compactness.** Suppose \(p>t\) and \(T_A\) is bounded. From Step 2, \(c\in\ell_{r_{p,t}}\) with finite \(r_{p,t}\). The finite-rank operators \(T_AP_N\), where \(P_N\) truncates to the first \(N\) input coordinates, satisfy
\[
\|T_A-T_AP_N\|\le\|(c_j)_{j>N}\|_{r_{p,t}}\longrightarrow0.
\]
Hence \(T_A\) is compact.

Now assume \(p\le t\). Step 2 gives the exact tail quasi-norm \(\|T_A(I-P_N)\|=\sup_{j>N}c_j\), hence \(\|T_A\|_{\mathrm{ess}}\le L:=\limsup c_j\). Because each row has only finitely many nonzeros, \((T_Ae_j)_i\to0\) for every output coordinate \(i\). Fix any compact \(K:\ell_p\to\ell_t\). Choose a subsequence \(j_k\to\infty\) along which \(c_{j_k}\to L\) and, after taking a further subsequence, \(Ke_{j_k}\to z\) in \(\ell_t\). Set \(u_k=T_Ae_{j_k}\). For \(0<t<1\), the inequality
\[
\left|\,|a-b|^t-|a|^t\,\right|\le|b|^t
\]
and dominated convergence (coordinatewise \(u_k\to0\)) imply
\[
\|u_k-z\|_t^t-\|u_k\|_t^t\longrightarrow\|z\|_t^t.
\]
Replacing \(z\) by \(Ke_{j_k}\) introduces an error of at most \(\|Ke_{j_k}-z\|_t^t\to0\). Therefore \(\|T_A-K\|^t\ge L^t+\|z\|_t^t\ge L^t\). Take the infimum over compact \(K\). The exact essential quasi-norm and compactness criterion follow.

Finally, for \(w_j=j^{-1/q_t}\), the signed nearest-neighbor difference \((D_tx)_i=w_ix_i-w_{i+1}x_{i+1}\) has row degree two and column norms \(c_1=w_1\), \(c_j=2^{1/t}w_j\) for \(j\ge2\). These belong to \(\ell_{r_{p,t}}\) for every \(p,t\in(0,1)\) (the finite-exponent case has \(r_{p,t}>q_t\)) and tend to zero, but fail \(\ell_{q_t}\) because \(\sum_jw_j^{q_t}=\sum_j1/j\) diverges. Its asserted boundedness, compactness, and simultaneous nonsummability now follow. Without bounded row degree, the rank-one map in the statement is bounded by \(\|x\|_1\le\|x\|_p\), is finite rank, and has every \(c_j=1\), verifying the necessity of the structural hypothesis.

## Verification

A standalone Python script, `verify_sparse.py`, checks 4,403 supplementary assertions for finite matrices and exponent pairs on both sides of the source/target threshold. It checks operator upper estimates, phase-randomized lower estimates (statistical diagnostics, not certificates), the exactly sharp positive merger constant, and the rank-one boundary example. To reproduce, run `python3 verify_sparse.py` using the Python 3 standard library. The proof of the infinite-dimensional theorem is wholly analytical and does not depend on random tests or computational extrapolation.

## Relationship to prior work

Araújo's 2026 Proposition 2.5 identifies the summability threshold for **diagonal** maps from \(\ell_p\) to itself and proves the compact-diagonal criterion. The present result classifies arbitrary complex matrices with uniformly bounded row degree, extends the object to every source/target pair \((p,t)\) strictly below one, and identifies a codomain-dependent summability threshold alongside a source/target compactness transition. Its key additional step is a random-phase inequality controlling cancellations. Tomaz's 2017 result concerns lineability of non-summing operators and does not state this sparse-matrix classification; Maddox's 1987 theorem concerns the identity on \(\ell_p\). A separate existing result on weighted composition operators covers a special one-entry-per-row geometry for different operator invariants, not the signed many-entry summability dichotomy. These ingredients and special cases are not claimed as new.

## Limitations

There is no assertion for target exponents \(t\ge1\), unbounded row-support degree, or arbitrary quasi-Banach sequence spaces. The signed-complex overlap constant in the estimates is a valid universal bound, not claimed optimal. The full classification is analytically proved. An equivalent older general theorem for sparse quasi-Banach matrices could imply the result; the available literature search does not prove absolute publication priority. The generic case with unbounded row degree can behave differently, as the explicit rank-one example shows.

## References

- D. Araújo, *Maximal Spaceability of the set of non-absolutely summing operators in quasi-Banach spaces*, arXiv:2610.33999v1, submitted 2026-10-25, especially Lemma 2.4 and Proposition 2.5. https://arxiv.org/abs/2610.33999
- D. Tomaz, *Linear structure in certain subsets of quasi-Banach sequence spaces*, arXiv:1711.06049, first submitted 2017-11-16. https://arxiv.org/abs/1711.06049
- I. J. Maddox, *A non-absolutely summing operator*, J. Austral. Math. Soc. Ser. A 43 (1987), 70–73, doi:10.1017/S1446788700028974.
- Orlicz's theorem on weakly \(1\)-summable sequences in \(\ell_1\), as quoted in Araújo (2026), Theorem 1.2.
