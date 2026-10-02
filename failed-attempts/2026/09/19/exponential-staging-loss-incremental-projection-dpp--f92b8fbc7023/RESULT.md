# Exponential staging loss for incremental projection-DPP column selection

## Statement

Grigori and Xue (2026) introduce conditional determinantal point processes for incremental column subset selection and, in particular, multi-stage adaptive randomized pivoting (MSARP). If the stage sizes are \(k_1,\ldots,k_t\), their analysis gives the expected squared-Frobenius oblique-interpolation bound
\[
\mathbb E\|A-\widehat A_{\rm obl}\|_F^2
\le \prod_{i=1}^t(1+k_i)\,\|A-AVV^\top\|_F^2.
\]
For one new column per stage this becomes \(2^d\) at final rank \(d\). The source proves that one *single* conditional step has a tight factor, but it does not establish that the factors can compound simultaneously along one MSARP trajectory. Its experiments find MSARP comparable to one-shot ARP.

The product loss is not only an artifact of the stagewise proof. It is asymptotically sharp even for the smaller, practically relevant **orthogonal column-subset projection error**, and it can be exponentially worse than one-shot ARP on the same exact dominant singular subspace.

### Theorem — asymptotically sharp \(2^d\) staging penalty

Fix an integer \(d\ge2\). There is a family of invertible matrices \(A_\varepsilon\in\mathbb R^{(d+1)\times(d+1)}\), \(0<\varepsilon<1\), with distinct leading singular values and an exact, uniquely ordered (up to signs) dominant right singular basis \(V_\varepsilon=[v_1,\ldots,v_d]\), such that the following holds as \(\varepsilon\downarrow0\).

Let \(S_{\rm MS}\) be the \(d\)-column subset produced by MSARP with stage sizes
\[
k_1=\cdots=k_d=1,
\]
using the cumulative exact bases \([v_1,\ldots,v_s]\) at stage \(s\). Let \(S_{\rm one}\) be an independent one-shot ARP/projection-DPP sample from the final basis \(V_\varepsilon\). For
\[
P_S=A_\varepsilon(:,S)A_\varepsilon(:,S)^\dagger,
\]
we have
\[
\boxed{
\frac{\mathbb E\|(I-P_{S_{\rm MS}})A_\varepsilon\|_F^2}
{\|A_\varepsilon-(A_\varepsilon)_d\|_F^2}
\longrightarrow 2^d,
}
\]
whereas
\[
\boxed{
\frac{\mathbb E\|(I-P_{S_{\rm one}})A_\varepsilon\|_F^2}
{\|A_\varepsilon-(A_\varepsilon)_d\|_F^2}
\longrightarrow d+1.
}
\]
Consequently
\[
\boxed{
\frac{\mathbb E\|(I-P_{S_{\rm MS}})A_\varepsilon\|_F^2}
{\mathbb E\|(I-P_{S_{\rm one}})A_\varepsilon\|_F^2}
\longrightarrow \frac{2^d}{d+1}.
}
\]
In particular, for every \(\eta>0\) and fixed \(d\), a finite full-rank matrix in the family makes the MSARP normalized orthogonal error exceed \(2^d-\eta\). Thus the \(2^d\) worst-case factor cannot in general be replaced by a subexponential function of \(d\), even if the analysis is changed from the source's oblique interpolant to the optimal orthogonal projection onto the selected columns.

## Construction

Put \(n=d+1\). For \(s=1,\ldots,d\), let \(G_s\) be the identity except for the \((s,s+1)\) coordinate plane, where
\[
G_s|_{s,s+1}=
\begin{pmatrix}
c_s&-r_s\\
r_s&c_s
\end{pmatrix},
\qquad r_s=\sqrt{1-c_s^2}.
\]
Choose
\[
c_1=2^{-1/2},
\qquad
c_s=\varepsilon^{2^{s-2}}\quad(s\ge2),
\]
and define
\[
O_\varepsilon=G_1G_2\cdots G_d=[V_\varepsilon,z_\varepsilon].
\]
Fix distinct numbers
\[
\tau_1>\tau_2>\cdots>\tau_d>1
\]
independent of \(\varepsilon\), set
\[
\sigma_\varepsilon=c_d^2,
\qquad
D_\varepsilon=\operatorname{diag}(\tau_1,\ldots,\tau_d,\sigma_\varepsilon),
\]
and take
\[
A_\varepsilon=D_\varepsilon O_\varepsilon^\top.
\]
Then the singular values of \(A_\varepsilon\) are exactly \(\tau_1,\ldots,\tau_d,\sigma_\varepsilon\), and its ordered dominant right singular vectors are precisely the columns of \(V_\varepsilon\), up to their irrelevant signs. Moreover
\[
\|A_\varepsilon-(A_\varepsilon)_d\|_F^2=\sigma_\varepsilon^2=c_d^4.
\]

## The nested projection-DPP chain

Let \(O_s=G_1\cdots G_s\) on the first \(s+1\) coordinates and let
\[
z^{(s)}=O_se_{s+1},
\qquad
a_j^{(s)}=(z_j^{(s)})^2,
\quad 1\le j\le s+1.
\]
The first \(s\) columns of the final \(O_\varepsilon\) are already fixed after \(G_s\), so the cumulative stage-\(s\) projector is supported on the first \(s+1\) coordinates and equals
\[
K_s=V_sV_s^\top=I_{s+1}-z^{(s)}(z^{(s)})^\top
\]
there. Hence a rank-\(s\) projection-DPP sample contains exactly \(s\) of those \(s+1\) indices. If it omits \(j\), the determinant lemma gives
\[
\det K_s(-j,-j)=1-\|z^{(s)}_{-j}\|_2^2=(z_j^{(s)})^2=a_j^{(s)}.
\]
Since the \(a_j^{(s)}\) sum to one, they are exactly the omission probabilities.

The null-vector weights obey the simple recursion
\[
a_j^{(s)}=(1-c_s^2)a_j^{(s-1)}\quad(j\le s),
\qquad
a_{s+1}^{(s)}=c_s^2.
\]
At stage \(s-1\), MSARP has selected all but one index \(J_{s-1}\) among \(\{1,\ldots,s\}\). Conditioning the next projection DPP on the retained set leaves only two possible omissions: the old omission \(J_{s-1}\), or the new index \(s+1\). Writing
\[
A=a_{J_{s-1}}^{(s-1)},
\qquad
u=(1-c_s^2)A,
\qquad
v=c_s^2,
\]
the two conditional probabilities are \(u/(u+v)\) and \(v/(u+v)\). Therefore
\[
\mathbb E\!\left[\frac1{a_{J_s}^{(s)}}\,\middle|\,J_{s-1}\right]
=
\frac{u}{u+v}\frac1u+
\frac{v}{u+v}\frac1v
=
\frac2{u+v}.
\]

At the first stage,
\[
a_1^{(1)}=a_2^{(1)}=\frac12,
\qquad
\mathbb E\frac1{a_{J_1}^{(1)}}=2.
\]
The hierarchical choice of \(c_s\) satisfies
\[
\frac{c_s^2}{\min_j a_j^{(s-1)}}\longrightarrow0
\qquad(\varepsilon\downarrow0)
\]
for every fixed \(s\ge2\). For \(s=2\), the old weights are both \(1/2\), so the ratio is \(2\varepsilon^2\to0\). For \(s\ge3\), the newest old weight is of order \(c_{s-1}^2\), while
\[
\frac{c_s^2}{c_{s-1}^2}
=\varepsilon^{2^{s-2}}\longrightarrow0,
\]
and all earlier weights are larger up to factors tending to one. Consequently, uniformly over every possible old omission,
\[
\frac2{(1-c_s^2)A+c_s^2}
=\frac{2}{A}(1+o(1)).
\]
Induction gives
\[
\boxed{
\mathbb E\frac1{a_{J_d}^{(d)}}\longrightarrow2^d.
}
\]
This already shows that the source's one-column-per-stage oblique bound is asymptotically sharp for one consistent nested basis, rather than merely stagewise tight for separately chosen examples.

## From interpolation growth to actual orthogonal CSS error

The stronger point is that the same factor survives optimal projection onto the selected columns.

At final rank \(d=n-1\), every selected subset omits one column, say \(j\). Since \(A_\varepsilon\) is invertible, the orthogonal projection residual vanishes on all selected columns and is the distance of the omitted column from their span. If
\[
G=A_\varepsilon^\top A_\varepsilon,
\]
the Schur-complement identity gives
\[
\|(I-P_{-j})A_\varepsilon\|_F^2
=\frac1{(G^{-1})_{jj}}.
\]
Now
\[
G^{-1}
=V_\varepsilon\operatorname{diag}(\tau_1^{-2},\ldots,\tau_d^{-2})V_\varepsilon^\top
+\sigma_\varepsilon^{-2}z_\varepsilon z_\varepsilon^\top.
\]
Writing
\[
a_j=(z_{\varepsilon,j})^2,
\qquad
b_j=\sum_{i=1}^d\frac{(V_\varepsilon)_{ji}^2}{\tau_i^2},
\]
we obtain the exact normalized error
\[
\boxed{
\frac{\|(I-P_{-j})A_\varepsilon\|_F^2}{\sigma_\varepsilon^2}
=
\frac1{a_j+\sigma_\varepsilon^2b_j}.
}
\]
The \(b_j\) are uniformly bounded. For small \(\varepsilon\), the smallest final null weight is \(c_d^2\), while
\[
\sigma_\varepsilon^2=c_d^4,
\qquad
\frac{\sigma_\varepsilon^2}{\min_j a_j}=c_d^2\to0.
\]
Hence the normalized orthogonal error is uniformly
\[
\frac1{a_j}(1+o(1)).
\]
Averaging over the MSARP omission distribution therefore yields the first limit \(2^d\).

For one-shot ARP, the final projection kernel is
\[
V_\varepsilon V_\varepsilon^\top=I-z_\varepsilon z_\varepsilon^\top,
\]
so the probability of omitting \(j\) is exactly \(a_j\). Thus
\[
\frac{\mathbb E\|(I-P_{S_{\rm one}})A_\varepsilon\|_F^2}{\sigma_\varepsilon^2}
=
\sum_{j=1}^{d+1}
\frac{a_j}{a_j+\sigma_\varepsilon^2b_j}
\longrightarrow d+1.
\]
This proves the theorem.

## Interpretation

The result isolates a genuine price of irrevocability. A one-shot projection DPP samples globally from the final \(d\)-dimensional subspace. In the constructed family, MSARP repeatedly commits to a pivot before a much smaller new coordinate scale is revealed. Each new scale creates, asymptotically, another factor of two in the inverse-volume amplification, and the losses multiply.

The construction also removes a possible ambiguity from repeated leading singular values: the \(\tau_i\) are distinct, so the ordered singular vectors fed to the stages are determined up to signs. The bad behavior is therefore not an artifact of choosing a pathological basis inside a degenerate top singular subspace.

The classical \(d+1\) worst-case factor for one-shot volume sampling/ARP is not new. The new conclusion is the exponential separation created by preserving earlier samples under the new conditional-DPP/MSARP mechanism, together with sharpness for the actual orthogonal CSS residual.

## Reproducibility

`artifacts/verify_staging.py` implements the Givens family, the exact two-choice conditional omission recursion, and the orthogonal-residual formula with distinct leading singular values using `mpmath` 1.3.0 at 80 decimal digits. `artifacts/verification_output.txt` records representative values for \(d=2,\ldots,6\) and \(\varepsilon=0.1,0.03\). For example, at \(d=6\), \(\varepsilon=0.03\), the staged normalized orthogonal error is
\[
63.91367757364856,
\]
approaching \(2^6=64\), while one-shot ARP is \(7.0\) to the displayed precision.

## Scope and limitations

The theorem is a worst-case asymptotic construction for each fixed \(d\); it does not assert that typical data sets or the matrices in the motivating experiments exhibit exponential degradation. The family is increasingly close to rank \(d\), with a small tail singular value \(\sigma_\varepsilon\), so its condition number grows as \(\varepsilon\downarrow0\). This is natural for a relative low-rank approximation lower bound but is still an important limitation.

The result concerns the maximally incremental regime \(k_1=\cdots=k_d=1\). It does not prove that the general product \(\prod_i(1+k_i)\) is simultaneously sharp for arbitrary block sizes. It also addresses final-rank squared Frobenius error, not intermediate-rank monotonicity, spectral-norm error, numerical stability of the conditional sampler, or average-case behavior.

The proof is exact arithmetic. Very small \(\varepsilon\) creates widely separated scales, so direct floating-point simulation of the full matrices can become ill-conditioned; the reproducibility artifact evaluates the exact low-dimensional probability and Schur-complement formulas at high precision instead.

## References

1. L. Grigori, Z. Xue, *Incremental Column Subset Selection via Conditional Determinantal Point Processes*, arXiv:2609.20556, 2026. https://arxiv.org/abs/2609.20556
2. A. Cortinovis, D. Kressner, *Adaptive Randomized Pivoting for Column Subset Selection, DEIM, and Low-Rank Approximation*, SIAM Journal on Matrix Analysis and Applications 47(1) (2026), 25–47. https://doi.org/10.1137/24M1719189
3. E. N. Epperly, *Adaptive randomized pivoting and volume sampling*, arXiv:2510.02513, 2025. https://arxiv.org/abs/2510.02513
4. A. Deshpande, L. Rademacher, *Efficient Volume Sampling for Row/Column Subset Selection*, FOCS 2010. https://doi.org/10.1109/FOCS.2010.38
5. A. Deshpande, L. Rademacher, S. Vempala, G. Wang, *Matrix approximation and projective clustering via volume sampling*, Theory of Computing 2 (2006), 225–247.
