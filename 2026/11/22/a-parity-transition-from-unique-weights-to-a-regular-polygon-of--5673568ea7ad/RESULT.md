# A parity transition from unique weights to a regular polygon of Schur-cycle normers

## Finding

For each integer \(n\ge 3\), let \(P\) be the cyclic shift \((Px)_j=x_{j-1}\), with indices modulo \(n\), and let \(B=I+P\). For probability vectors \(u,v\in[0,1]^n\) put
\[
F(u,v)=\|D_{\sqrt u}B D_{\sqrt v}\|_{S_1}.
\]
The maximum of \(F\) is \(2/[n\sin(\pi/(2n))]\) for odd \(n\) and \(2/[n\tan(\pi/(2n))]\) for even \(n\). For odd \(n\) the unique maximizing pair is uniform. For even \(n\), put \(\theta=2\pi/n\). The maximizing pairs are exactly
\[
u_j=\frac{1+a\cos(\theta j)+b\sin(\theta j)}{n},\qquad
v_j=\frac{1+a\cos(\theta(j+1/2))+b\sin(\theta(j+1/2))}{n},
\]
where \(a,b\) are real and all displayed coordinates are nonnegative. The feasible \((a,b)\) form a regular \(2n\)-gon of inradius one. The sign of the half-step is tied to the specified shift: for the transpose mask \(I+P^\mathsf T\) the half-step is instead \(-1/2\).

## Scope

Matrices act on complex Euclidean space, \(\|\cdot\|_{S_1}\) is the nuclear norm, and zero probability coordinates are allowed. These are all norming **probability pairs**, not a classification of all norming input matrices. In fact the operator norm of Schur multiplication by the real mask \(B\) is \(\max_{u,v}F(u,v)\): for unit vectors \(x,y\), one has \(x^*(B\circ A)y=\operatorname{tr}((D_x B D_{\overline y})^*A)\). Maximizing over \(\|A\|\le1\) gives the nuclear norm, and diagonal unitaries remove the coordinate phases of \(x,y\).

## Proof

**Sharp bound and equality.** Let \(W=|B|\), write \(B=HW\) with \(H\) a unitary polar extension, and let \(Q\) project onto the support of \(W\). Both \(W\) and \(HWH^*=|B^*|\) have constant diagonal \(c=\operatorname{tr}(W)/n\), since they are circulant. Set \(X=D_{\sqrt u}HW^{1/2}\), \(Y=D_{\sqrt v}W^{1/2}\). Then \(XY^*=D_{\sqrt u}B D_{\sqrt v}\) and \(\|X\|_F^2=\|Y\|_F^2=c\). Trace-norm duality gives \(\|XY^*\|_1=\max_{U\text{ unitary}}\operatorname{Re}\operatorname{tr}(Y^*UX)\le c\), with equality if and only if some unitary \(U\) satisfies \(UX=Y\). For the converse, equality of the Gram matrices \(X^*X=Y^*Y\) makes \(Xz\mapsto Yz\) a well-defined isometry that extends to a unitary. Conjugating the Gram condition by the inverse of \(W^{1/2}\) on its support gives
\[
Q(H^*D_uH-D_v)Q=0. \tag{1}
\]
Uniform weights attain \(c\), so (1) characterizes maximizers even when weights vanish.

**Complete frequency test.** Use Fourier modes \(\phi_r(j)=n^{-1/2}e^{2\pi irj/n}\) and \(\widehat u(k)=n^{-1}\sum_j u_j e^{2\pi ikj/n}\), and analogously for \(v\). The eigenvalue of \(B\) is \(1+e^{-2\pi ir/n}\). Use the centered integer representatives \(I=[-\lfloor(n-1)/2\rfloor,\lfloor(n-1)/2\rfloor]\cap\mathbb Z\) for modes on the support of \(W\). Thus \(L=|I|\) is \(n\) for odd \(n\) and \(n-1\) for even \(n\); the mode \(n/2\) is absent in the latter case. The polar phase on \(I\) is \(h_r=e^{-\pi ir/n}\), since \(\cos(\pi r/n)>0\). Equation (1) therefore says that for all \(r,s\in I\) with \(s-r\equiv k\pmod n\),
\[
\widehat v(k)=e^{-\pi i(s-r)/n}\,\widehat u(k). \tag{2}
\]
For \(1\le k\le n-1\), the possible actual differences are \(k\) and \(k-n\); their pair counts are \(\max(0,L-k)\) and \(\max(0,L-(n-k))\). If both occur, their phase factors in (2) have opposite signs, forcing both coefficients to be zero. For odd \(n\) both always occur; for even \(n\) both occur except at \(k=1,n-1\). There is at least one pair for every \(k\), including the smallest even case \(n=4\). At \(k=1\) in even dimension, the only factor is \(e^{-\pi i/n}\); the relation at \(k=-1\) is its conjugate.

For even \(n\), normalization gives the constant term \(1/n\). The allowed first harmonic of \(u\) can be written as in the Finding, with \(\widehat u(1)=(a+ib)/(2n)\). Under the positive-exponent transform (whose inverse uses the negative exponent), evaluating this first-harmonic trigonometric polynomial at \(j+1/2\) multiplies \(\widehat u(1)\) by \(e^{-\pi i/n}\). This is exactly (2) and proves both directions of the classification. The inequalities for \((a,b)\) have normals opposite the unit vectors at angles \(\theta j\) and \(\theta(j+1/2)\): they give all \(2n\) equally spaced side normals at distance one from the origin, hence the stated polygon.

**Value.** The singular values of \(B\) are \(2|\cos(\pi r/n)|\). For odd \(n\) their half-sum is \(\sum_{r\in I}\cos(\pi r/n)=1/\sin(\pi/(2n))\) by the centered geometric sum. For even \(n\) the same sum over \(I\), with the omitted term zero, is \(\cos(\pi/(2n))/\sin(\pi/(2n))\). Dividing the singular-value sum by \(n\) gives the two maxima.

## Relation to prior work and limitations

The scalar norm of a circulant Schur multiplier and uniform optimality are classical; the contribution is the classification of every probability pair for the cyclic two-neighbor mask. Mathias's abstract describes the circulant norm and a matrix Cauchy–Schwarz equality result. The full Mathias article was not available for this comparison, so earlier cycle-specific equality analysis cannot be excluded. Levene's Schur probability characterization supplies the norm interpretation, not the cycle-specific solution of the equality equations. The proof does not classify all norming matrices or other masks.

## Verification and references

`python3 verify.py` runs bounded numerical checks with NumPy, including the specified shift orientation, uniform values, nonuniform optimizers, and even polygon boundary points. The proof above, not sampling, gives the complete classification.

1. R. Mathias, *The Hadamard operator norm of a circulant and applications*, SIAM J. Matrix Anal. Appl. 14 (1993), 1152–1167, [doi:10.1137/0614080](https://doi.org/10.1137/0614080).
2. R. H. Levene, *A half-line of Schur idempotent norms*, [arXiv:2611.08419](https://arxiv.org/abs/2611.08419), §2, Lemma 2.3.
