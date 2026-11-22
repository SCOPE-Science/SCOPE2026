# Sharp rank-one-boundary diagonal sensitivity and dimension-linear instability of semidefinite projection

## Finding

Let \(\mathbb S^n\) denote real symmetric \(n\times n\) matrices, \(n\ge3\), and let \(\Pi(A)=A_+\) be Frobenius nearest-point projection onto the positive-semidefinite cone. Both input and output entry magnitudes are measured by \(\|A\|_{\max}=\max_{i,j}|A_{ij}|\). For a unit vector \(u\), write \(P=uu^{\mathsf T}\), \(Q=I-P\), and \(A_{\eta,u}=P-\eta Q\), \(\eta>0\).

The exact limiting diagonal differential amplification on this canonical rank-one-positive, flat-negative spectral stratum is independent of the chosen output diagonal index and equals
\[
\boxed{\mathcal B_n=\sup_{\|u\|_2=1}\lim_{\eta\downarrow0}
\sup_{\substack{H=H^{\mathsf T}\\\|H\|_{\max}\le1}}
\bigl|\bigl[D\Pi(A_{\eta,u})H\bigr]_{11}\bigr|
=\max_{0\le p\le1}\bigl(n p(1-p)+p+2\sqrt{n-1}\sqrt p(1-p)^{3/2}\bigr).}
\]
There is a unique maximizing \(p=p_n\) in \((1/4,1/2)\) for every \(n\ge3\). It is equivalently characterized by
\[
n(1-2p_n)+1=\sqrt{n-1}(4p_n-1)\sqrt{(1-p_n)/p_n}.
\]
All maximizing vectors may be taken with \(|u_1|^2=p_n\) and equal remaining squared coordinate magnitudes \((1-p_n)/(n-1)\); an explicit sign matrix realizes the limiting differential norm.

For the *unrestricted* global entrywise Lipschitz modulus
\[
\mathcal L_n=\sup_{A\ne B}\frac{\|A_+-B_+\|_{\max}}{\|A-B\|_{\max}},
\]
the following bounds and asymptotic conclusions hold:
\[
\boxed{\mathcal B_n\le\mathcal L_n\le n,\qquad
\mathcal B_n=\frac n4+\frac{\sqrt n}{2}+\frac34+O(n^{-1/2}),
\qquad \mathcal L_n=\Theta(n).}
\]
The formula for \(\mathcal B_n\) is exact **only for the stated rank-one boundary differential class**; no formula for the unrestricted \(\mathcal L_n\) is asserted. At \(n=2\) it gives the previously known \(\mathcal B_2=3/2\); the novel dimensional assertion concerns \(n\ge3\).

## Assumptions and scope

The matrices and perturbations are **real symmetric**; an off-diagonal perturbation changes both symmetric entries together. The projection minimizes Frobenius distance, *not* entrywise distance. The norm \(\|\cdot\|_{\max}\) is the largest absolute individual entry, not the induced maximum row-sum norm. The parameter \(\eta\) tends to zero only after evaluating the ordinary Fréchet derivative at the nonsingular matrix \(A_{\eta,u}\); no differentiability of \(\Pi\) at the singular limiting matrix is assumed. There are no restrictions on the signs of the perturbations.

## Proof

**1. Projection differential.** Since \(A_{\eta,u}\) has a simple eigenvalue \(1\) with projector \(P\), and its remaining eigenvalues are \(-\eta\), spectral positive-part projection satisfies \(\Pi(A_{\eta,u})=P\). Differentiating the isolated positive eigenpair (or applying the standard divided-difference spectral derivative) gives, for every symmetric \(H\),
\[
D\Pi(A_{\eta,u})H=PHP+\frac{PHQ+QHP}{1+\eta}.
\]
Thus the limiting linear operator is
\[
T_P(H)=\lim_{\eta\downarrow0}D\Pi(A_{\eta,u})H=PH+HP-PHP.
\]
This limit concerns derivatives at strictly nonsingular matrices and is justified by the explicit formula, including when the negative eigenvalue is repeated.

**2. Exact diagonal dual norm.** Set \(p=u_1^2\) and \(s=\sum_{j=2}^n|u_j|\). Expansion in the independent symmetric entries of \(H\) gives
\[
[T_P(H)]_{11}=(2p-p^2)H_{11}
+2u_1(1-p)\sum_{j>1}u_jH_{1j}
-p\sum_{j>1}u_j^2H_{jj}
-2p\sum_{2\le j<k\le n}u_ju_kH_{jk}.
\]
The entrywise unit ball allows each independent entry of \(H\) to take the sign of its coefficient. Consequently the exact dual norm of this scalar functional is
\[
R(u)=2p-p^2+2\sqrt p(1-p)s+p s^2.
\]
Cauchy–Schwarz yields \(s\le\sqrt{(n-1)(1-p)}\), with equality when the magnitudes of all remaining coordinates are equal. Both coefficients of \(s\) are nonnegative, so the largest value for fixed \(p\) is
\[
F_n(p)=n p(1-p)+p+2\sqrt{n-1}\sqrt p(1-p)^{3/2}.
\]
For equality, take \(u_1=\sqrt p\), \(u_j=\sqrt{(1-p)/(n-1)}\) for \(j>1\), and symmetric \(H\) with \(H_{11}=H_{1j}=H_{j1}=1\) for all \(j\), and \(H_{jk}=-1\) for \(j,k>1\). Then \(\|H\|_{\max}=1\) and \([T_P(H)]_{11}=F_n(p)\). This proves the exact boundary-class formula.

**3. Existence and uniqueness of the maximizing mass.** On \(0<p<1\),
\[
F_n'(p)=n(1-2p)+1+\sqrt{n-1}(1-4p)\sqrt{(1-p)/p}.
\]
It is positive for \(p\le1/4\). On \((1/4,1/2]\), its derivative is strictly negative because
\[
F_n''(p)=-2n+\frac{\sqrt{n-1}\,(8p^2-4p-1)}{2p^{3/2}\sqrt{1-p}}<0.
\]
Also \(F_n'(1/2)=1-\sqrt{n-1}<0\) for \(n\ge3\). Hence there is exactly one critical point in \((1/4,1/2)\). To exclude later maxima, put \(c=(n+1)/(2n)\le3/4\). On \(1/2<p<c\), the elementary identity
\[
(4p-1)^2(1-p)-p=-(2p-1)(8p^2-8p+1)\ge0
\]
shows \((4p-1)\sqrt{(1-p)/p}\ge1\). Thus \(F_n'(p)\le n(1-2p)<0\). For \(p\ge c\), both \(n(1-2p)+1\le0\) and \(1-4p<0\), so again \(F_n'<0\). The unique maximizer has the stated equation. At \(n=2\), the same sign argument gives \(p_2=1/2\), consistent with the previously established two-dimensional coefficient.

**4. Real finite-pair instability and global bounds.** At every fixed \(\eta>0\), the nonsingular spectral projector is differentiable. For its maximizing sign perturbation \(H\),
\[
\lim_{h\to0}\frac{|[\Pi(A_{\eta,u}+hH)-\Pi(A_{\eta,u})]_{11}|}{|h|}
=|[D\Pi(A_{\eta,u})H]_{11}|.
\]
Letting \(\eta\downarrow0\) gives \(F_n(p)\); hence the supremum over *actual distinct finite matrix pairs* defining \(\mathcal L_n\) is at least \(\mathcal B_n\). Conversely, Hilbert-space nearest-point projection is nonexpansive in Frobenius norm:
\[
\|A_+-B_+\|_{\max}\le\|A_+-B_+\|_F\le\|A-B\|_F\le n\|A-B\|_{\max}.
\]
Thus \(\mathcal B_n\le\mathcal L_n\le n\).

**5. Asymptotics.** The maximizer satisfies \(p_n\to1/2\): otherwise the leading term \(np(1-p)\) would lose a positive multiple of \(n\), while the remaining terms are \(O(\sqrt n)\). The critical-point equation then yields \(p_n=1/2-1/(2\sqrt n)+O(n^{-1})\). Uniform Taylor expansion at \(p=1/2+z/\sqrt n\), with bounded \(z\), gives
\[
F_n(p)=\frac n4+\frac{\sqrt n}{2}+\frac12-z^2-z+O(n^{-1/2}).
\]
Putting \(z=-1/2+O(n^{-1/2})\) yields \(\mathcal B_n=n/4+\sqrt n/2+3/4+O(n^{-1/2})\). The lower and upper bounds then imply \(\mathcal L_n=\Theta(n)\).

## Verification

Run `python3 verify.py` using Python 3's standard library. It checks the differentiated formula, the analytic row-profile identity, the maximizing root across many dimensions, finite-difference derivatives computed by a Jacobi symmetric eigensolver for nonsingular test matrices, and large-dimensional asymptotic samples. The present checker reports **2,843 supplementary checks passed**. These computations are finite tests and do not establish the all-dimensional result; the preceding analytic proof is the certificate for arbitrary dimensions and all perturbations.

## Relationship to prior work

Malick–Sendov provides a general Fréchet/generalized Jacobian of the positive-semidefinite cone projector, including the cross-eigenspace divided difference used in step 1. Ding–Sun–Sun–Toh treats local Lipschitz continuity and generalized differentials of much broader spectral operators. Goulart–Nakatsukasa–Rontsis provides Frobenius-error bounds for approximate semidefinite projection. These results supply derivative and projection background, not the optimized maximum-entry diagonal boundary profile or its dimensional asymptotic. The previously published exact two-by-two entrywise result gives \(3/2\) and only a dimension-independent block-embedding lower bound for larger matrices. Its two-dimensional conclusion is not claimed new here. The new result establishes exact rank-one boundary amplification for every larger dimension and shows that the unrestricted entrywise global coefficient must in fact grow linearly with dimension. Prior source coverage has been assessed by statements and implications, not by keyword absence alone.

## Limitations

The unrestricted global Lipschitz constant \(\mathcal L_n\) is **not** computed exactly; only its sharp dimensional order and a precise lower bound from a natural boundary class are proved. The limiting differential optimization does not assert a finite-pair maximizer, nor does it cover complex Hermitian matrices, non-Frobenius projections, correlation-matrix diagonal constraints, or nonsymmetric inputs. Relevant published derivative formulas make the new calculation possible, and an earlier unlocated exact coordinatewise optimization remains a historical-priority risk.

## References

1. C. Ding, D. Sun, J. Sun, K.-C. Toh, *Spectral operators of matrices: semismoothness and characterizations of the generalized Jacobian*, initial public arXiv version 2018-10-22, https://arxiv.org/abs/1810.09856. Open full-text author's version: https://www.polyu.edu.hk/ama/profile/dfsun/files/SPECTRAL%20OPERATORS%20OF%20MATRICES_II_2020.pdf.
2. P. J. Goulart, Y. Nakatsukasa, N. Rontsis, *Accuracy of approximate projection to the semidefinite cone*, initial arXiv version 2019-08-05, https://arxiv.org/abs/1908.01606.
3. J. Malick, H. S. Sendov, *Clarke generalized Jacobian of the projection onto the cone of positive semidefinite matrices*, Set-Valued Analysis **14** (2006), 273–293, https://www.stats.uwo.ca/faculty/hssendov/Publications/CGJPCPSDM.pdf.
4. *Sharp diagonal and off-diagonal amplification in two-by-two semidefinite projection*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-diagonal-and-off-diagonal-amplification-in-two-by-two-semi--e19c93a79149.
