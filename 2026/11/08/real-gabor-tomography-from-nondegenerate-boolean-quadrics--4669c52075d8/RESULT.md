# Real Gabor tomography from nondegenerate Boolean quadrics

## Finding
For every integer \(m\ge2\), let \(V=\mathbb F_2^{2m}\), \(N=|V|=2^{2m}\), and \(t=2^m\). Let \(Q:V\to\mathbb F_2\) be a quadratic form with \(Q(0)=0\), whose polar form is nondegenerate. Its quadratic Gauss sign is \(\varepsilon\in\{+1,-1\}\). For the unweighted indicator \(g=\mathbf1_{\{Q=0\}}\), consider the \(N^2\) real Walsh time-frequency shifts and their rank-one intensity projectors.

The complete complex-linear intensity-lifting singular-value multiset is
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
\sqrt N\,k&1\\
\sqrt N\,\lambda&2(N-1)\\
\sqrt N\,t/2&(N-1)(N/2-1)\\
0&N(N-1)/2
\end{array},\qquad
k=\frac{N+\varepsilon t}{2},\quad
\lambda=\frac{N+2\varepsilon t}{4}.
\]
Levels of equal magnitude have their multiplicities added. In particular,
\[
\operatorname{rank}\mathcal L=\frac{N(N+1)}2,
\qquad \kappa^+(\mathcal L)=t+\varepsilon.
\]
Thus these highly structured binary-support windows attain the **largest matrix-recovery rank possible for real-valued measurement vectors**. The full orbit reconstructs every real symmetric matrix, hence every real signal up to a global sign. The negative-Gauss-sign quadratic forms have the strictly better positive-spectrum condition number \(2^m-1\), versus \(2^m+1\) for positive sign.

## Assumptions and scope
All vector additions, dot products, and bilinear forms are over \(\mathbb F_2\). The quadratic polar form is \(B(x,y)=Q(x+y)+Q(x)+Q(y)\); it is nonsingular and alternating. Put
\[
\varepsilon=2^{-m}\sum_{x\in V}(-1)^{Q(x)},\quad
S=\{x:Q(x)=0\},\quad g(x)=\mathbf1_S(x).
\]
The shift/modulation operators act on \(\mathbb C^V\) by
\[
(T_af)(x)=f(x+a),\qquad (M_bf)(x)=(-1)^{b\cdot x}f(x).
\]
For each \((s,u)\in V^2\) put \(v_{s,u}=M_uT_sg\) and \(P_{s,u}=v_{s,u}v_{s,u}^{\mathsf T}\). Define the complex-linear map
\[
\mathcal L(H)_{s,u}=\operatorname{tr}(HP_{s,u}),\quad H\in\mathbb C^{N\times N},
\]
with unnormalized Hilbert--Schmidt norm on matrices and Euclidean norm on the output. Because the measurement vectors are real, this agrees with the usual Hermitian-projector formulation. The real restriction is \(\mathcal L:\operatorname{Sym}_N(\mathbb R)\to\mathbb R^{N^2}\). No normalization of \(g\) by its norm has been made. Such normalization multiplies every nonzero singular value by \(1/k\) without altering rank or condition number.

## Proof
**1. The quadratic Walsh transform.** Nonsingularity and the derivative formula \(Q(x+a)=Q(x)+Q(a)+B(x,a)\) give
\[
\left(\sum_x(-1)^{Q(x)}\right)^2
=\sum_{a}(-1)^{Q(a)}\sum_x(-1)^{B(x,a)}=N.
\]
Therefore the Gauss sum is \(\varepsilon t\) for a sign \(\varepsilon\). For each frequency \(b\) there is a unique \(z_b\in V\) with \(b\cdot x=B(z_b,x)\) for all \(x\), and the change of variables \(x\mapsto x+z_b\) gives
\[
\sum_x(-1)^{Q(x)+b\cdot x}=\varepsilon t(-1)^{Q(z_b)}.
\]
In particular, \(g=(1+(-1)^Q)/2\) and \(|S|=k=(N+\varepsilon t)/2\).

**2. Every ambiguity coefficient.** Write \(L(a)\) for the dual frequency of \(B(a,\cdot)\), so \(z_{L(a)}=a\). Define
\[
A(a,b)=\sum_x g(x)g(x+a)(-1)^{b\cdot x}.
\]
Expand the product of the two indicators and apply the transform in step 1:
\[
A(a,b)=\frac N4\bigl(\mathbf1_{b=0}+(-1)^{Q(a)}\mathbf1_{b=L(a)}\bigr)
+\frac{\varepsilon t}{4}(-1)^{Q(z_b)}\bigl(1+(-1)^{a\cdot b}\bigr).
\tag{1}
\]
Indeed, \(z_{b+L(a)}=z_b+a\), so the quadratic derivative identity reduces the two Gauss terms to the last factor in (1). For \(a=0\), this says \(A(0,0)=k\), while every \(b\ne0\) gives \(|A(0,b)|=t/2\). For \(a\ne0\), both \(b=0\) and \(b=L(a)\) satisfy \(a\cdot b=0\), are distinct, and give \(|A(a,b)|=\lambda\), where
\[
\lambda=\frac N4+\frac{\varepsilon t}{2}=\frac{t(t+2\varepsilon)}4>0
\qquad(m\ge2).
\]
Among the other frequencies with \(a\cdot b=0\), all \(N/2-2\) have \(|A(a,b)|=t/2\); all \(N/2\) frequencies with \(a\cdot b=1\) have \(A(a,b)=0\). There are no additional zeros.

**3. Lift diagonalization and all multiplicities.** The real Walsh Weyl matrices \(W_{a,b}=M_bT_a\) satisfy \(W_{a,b}^{\mathsf T}=(-1)^{a\cdot b}W_{a,b}\), are pairwise orthogonal in Hilbert--Schmidt norm, and have squared norm \(N\). Consequently, the \(N(N+1)/2\) matrices with \(a\cdot b=0\) form an orthogonal basis for real symmetric matrices, and the \(N(N-1)/2\) matrices with \(a\cdot b=1\) form one for real skew-symmetric matrices. Weyl conjugation satisfies
\[
W_{s,u}^{-1}W_{a,b}W_{s,u}=(-1)^{b\cdot s+a\cdot u}W_{a,b}.
\]
Hence, for symmetric \(W_{a,b}\),
\[
\mathcal L(W_{a,b})_{s,u}=(-1)^{b\cdot s+a\cdot u}A(a,b).
\]
The displayed output characters are mutually orthogonal over the \(N^2\) choices of \((s,u)\), each with Euclidean norm \(N\). Dividing the input Weyl matrix by \(\sqrt N\) therefore gives singular value \(\sqrt N\,|A(a,b)|\). Skew matrices contribute zero. The counts from step 2 are: one coefficient of magnitude \(k\); \(2(N-1)\) of magnitude \(\lambda\); \((N-1)(N/2-1)\) of magnitude \(t/2\); and \(N(N-1)/2\) zero coefficients. These total \(N^2\). Thus the kernel is exactly the complex span of skew Weyl matrices, and the real symmetric restriction is injective.

**4. Sharp conditioning and real-signal consequence.** Since \(k>\lambda\ge t/2>0\) for \(t\ge4\), the sharp positive-spectrum condition number is \(k/(t/2)=t+\varepsilon\). The equality \(\lambda=t/2\) arises only for \(t=4\), \(\varepsilon=-1\). If real vectors \(f,h\) have identical squared measurements, then \(ff^{\mathsf T}-hh^{\mathsf T}\) is a real symmetric matrix in the kernel, hence zero. Accordingly \(h=\pm f\) (including the zero case). Both Gauss signs occur, for example for
\[
Q_+(x)=\sum_{j=0}^{m-1}x_{2j}x_{2j+1},\qquad
Q_-(x)=Q_+(x)+x_0+x_1.
\]
Their Gauss signs are respectively \(+1\) and \(-1\), as follows by factoring the two-bit quadratic sums.

## Verification
The standalone standard-library checker `artifacts/quad_bent_gabor_check.py` independently enumerates the indicator windows for both Gauss signs in dimensions \(n=4,6,8\). For each translation it obtains all ambiguity coefficients by a direct integer fast Walsh transform and compares **every coefficient including its sign** against equation (1). It verifies all singular-level multiplicities and exact rank counts. For both signs in dimension four it also constructs the entire real intensity-measurement matrix on the \(136\)-dimensional symmetric subspace and computes its full rank by exact modular elimination over \(\mathbb F_{101}\). All six cases passed; the program ends with `QUADRATIC_BENT_REAL_GABOR_EXACT_CHECKS_OK`. These are checks of concrete finite instances, not substitutes for the unrestricted proof.

## Relationship to prior work
The finite-group Weyl/STFT framework and uncertainty inequalities of Krahmer, Pfander and Rashkov (2006) and the projective-intensity analysis of Bojarovska and Flinth (2015) supply the underlying harmonic-analysis methodology. The latter's full complex-operator injectivity condition requires nonzero ambiguity at **all** Weyl indices and therefore cannot apply to any nontrivial real window on a binary group, where skew indices necessarily vanish. Its difference-set example is conditioned by the smallest prime factor and does not imply the stated binary quadratic result. Leopardi (2015) documents the Hadamard difference-set parameters and strongly regular Cayley graphs associated with binary bent supports, but not their real Gabor projector-span spectrum.

Nearby published work on first-Walsh-band restriction to binary quadrics concerns an \((n+1)\)-dimensional character subspace rather than the entire \(N(N+1)/2\)-dimensional real symmetric matrix space. Published work on Gabor tomography of hyperbolic quadratic shells over **odd** finite fields treats a distinct characteristic, level set and operator kernel. Neither gives this full characteristic-two ambiguity-magnitude classification, maximal real tomography, or Gauss-sign conditioning law. These distinctions compare the mathematical statements, not merely terminology.

## Limitations
Only even binary dimension at least four, nondegenerate quadratic forms with \(Q(0)=0\), and the specified real indicator window are covered. The complex lifting has the unavoidable skew-symmetric kernel: no arbitrary-complex-matrix or complex-signal uniqueness is claimed. The condition number concerns linear lifting on the real symmetric matrix space, not optimal nonlinear recovery under a specified noise model. No optimality across *all* real windows or all binary difference sets is asserted. The statement uses exact unnormalized operator norms. Historical-priority review is bounded; independent mathematical audit has not been performed.

## References
1. F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1 (first public 2006-11-16), https://arxiv.org/abs/math/0611493.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (first public 2015-03-19), https://arxiv.org/abs/1503.05800; especially Theorems 2.2--2.3 and Proposition 2.2.
3. P. Leopardi, *Twin bent functions, strongly regular Cayley graphs, and Hurwitz--Radon theory*, arXiv:1504.02827v1 (first public 2015-04-11), https://arxiv.org/abs/1504.02827.
