# Euclidean distortion, Jordan--von Neumann, and Ptolemy constants coincide on the \(q=2\) Lorentz plane
## Finding
For the real two-dimensional Lorentz sequence space \(X=d^{(2)}(w,2)\) with weights \(w_1\ge w_2>0\), put \(a=w_2/w_1\). Then \(d_{\mathrm{BM}}(X,\ell_2^2)^2=C_{\mathrm{NJ}}(X)=C_{\mathrm{Pt}}(X)=2/(1+a)=2w_1/(w_1+w_2)\).

Thus the affine Euclidean distortion, the parallelogram-law defect, and the four-point Ptolemy defect have one common exact value on this full one-parameter family.

## Assumptions and scope
The scalar field is real. The two-dimensional Lorentz norm is
\[
\|(x,y)\|_{w,2}=\left(w_1(x_1^*)^2+w_2(x_2^*)^2\right)^{1/2},
\]
where \((x_1^*,x_2^*)\) is the decreasing rearrangement of \((|x|,|y|)\). Multiplying a norm by a positive scalar changes none of the three quantities in the claim, so it suffices to normalize \(w_1=1\) and write \(a=w_2/w_1\in(0,1]\).

For this normalization define
\[
N_a(x,y)^2=\max\{x^2+a y^2,\;a x^2+y^2\}.
\]
The Banach--Mazur distance is
\[
d_{\mathrm{BM}}(X,\ell_2^2)
=\inf_T \|T\|\,\|T^{-1}\|,
\]
over linear isomorphisms from \(X\) onto \(\ell_2^2\). The constants \(C_{\mathrm{NJ}}\) and \(C_{\mathrm{Pt}}\) are the standard Jordan--von Neumann and Ptolemy constants.

## Proof
First,
\[
\frac{1+a}{2}\,(x^2+y^2)
\le N_a(x,y)^2
\le x^2+y^2.
\]
Indeed, the upper bound follows because \(a\le1\), while the lower bound follows because the maximum of the two quadratic forms is at least their average. If \(K=\{z:N_a(z)\le1\}\), this gives
\[
B_2\subseteq K\subseteq \sqrt{\frac2{1+a}}\,B_2.
\]
Hence
\[
d_{\mathrm{BM}}(X,\ell_2^2)
\le \sqrt{\frac2{1+a}}.
\]

For the reverse Banach--Mazur bound, let
\[
E_A=\{z:z^T A z\le1\},\qquad
A=\begin{pmatrix}p&r\\r&q\end{pmatrix}>0,
\]
and suppose
\[
E_A\subseteq K\subseteq \lambda E_A.
\]
Write
\[
Q_1=\begin{pmatrix}1&0\\0&a\end{pmatrix},\qquad
Q_2=\begin{pmatrix}a&0\\0&1\end{pmatrix}.
\]
Since \(K=E_{Q_1}\cap E_{Q_2}\), the inclusion \(E_A\subseteq K\) implies
\[
A-Q_1\succeq0,\qquad A-Q_2\succeq0.
\]
In particular \(p\ge1\) and \(q\ge1\). Both points
\[
u_+=\frac{(1,1)}{\sqrt{1+a}},\qquad
u_-=\frac{(1,-1)}{\sqrt{1+a}}
\]
belong to \(K\). Since \(K\subseteq\lambda E_A\),
\[
\lambda^2\ge
\frac{p+q+2r}{1+a},
\qquad
\lambda^2\ge
\frac{p+q-2r}{1+a}.
\]
Therefore
\[
\lambda^2\ge
\frac{p+q+2|r|}{1+a}
\ge \frac2{1+a}.
\]
Taking the infimum over all ellipses proves
\[
d_{\mathrm{BM}}(X,\ell_2^2)^2=\frac2{1+a}.
\]

Next consider the Jordan--von Neumann constant. The same norm comparison and the Euclidean parallelogram identity give, for arbitrary \(x,y\),
\[
N_a(x+y)^2+N_a(x-y)^2
\le \|x+y\|_2^2+\|x-y\|_2^2
=2\left(\|x\|_2^2+\|y\|_2^2\right)
\le \frac4{1+a}\left(N_a(x)^2+N_a(y)^2\right).
\]
Thus
\[
C_{\mathrm{NJ}}(X)\le\frac2{1+a}.
\]
With
\[
x=\frac{(1,1)}{\sqrt{1+a}},
\qquad
y=\frac{(1,-1)}{\sqrt{1+a}},
\]
one has \(N_a(x)=N_a(y)=1\), while \(N_a(x+y)^2=N_a(x-y)^2=4/(1+a)\). Hence equality holds:
\[
C_{\mathrm{NJ}}(X)=\frac2{1+a}.
\]

Finally, the norm comparison and Euclidean Ptolemy inequality imply
\[
C_{\mathrm{Pt}}(X)\le\frac2{1+a}.
\]
Indeed, each numerator norm is at most its Euclidean norm, while each product in the denominator is at least \((1+a)/2\) times its Euclidean counterpart. For the reverse inequality take
\[
x=(1/2,1/2),\qquad y=(1/2,-1/2),\qquad z=(1,0).
\]
Then
\[
N_a(x-y)=N_a(z)=1,
\]
and
\[
N_a(x-z)=N_a(y)=N_a(z-y)=N_a(x)=\frac{\sqrt{1+a}}2.
\]
The Ptolemy ratio is exactly
\[
\frac1{(1+a)/2}=\frac2{1+a}.
\]
Thus
\[
C_{\mathrm{Pt}}(X)=\frac2{1+a},
\]
and all three quantities in the claim are equal.

## Verification
The proof covers every \(a\in(0,1]\), not a finite sample. The Banach--Mazur lower bound ranges over an arbitrary centered ellipse through an arbitrary positive-definite matrix \(A\). The implication \(E_A\subseteq E_Q\Rightarrow A-Q\succeq0\) follows by maximizing \(z^TQz\) on \(E_A\), equivalently from \(A^{-1/2}QA^{-1/2}\preceq I\). No numerical experiment is used as an infinite proof.

At \(a=1\) the norm is Euclidean and every displayed value equals \(1\), as required.

## Relationship to prior work
Kato and Maligranda (2001) study two-dimensional Lorentz sequence spaces \(d^{(2)}(w,q)\) and compute James and Jordan--von Neumann constants. Kato, Maligranda, and Takahashi (2001) give the exact Jordan--von Neumann value for the standard subfamily \(\ell_{p,2}\) and establish general inequalities relating Jordan--von Neumann constants to Banach--Mazur distance.

Zuo (2012) treats the same normalized \(q=2\) Lorentz plane and proves
\[
C_{\mathrm{Pt}}=\frac2{1+a}.
\]
The inspected full text contains no Banach--Mazur computation. The present claim identifies the exact Banach--Mazur distance for the whole weight family and shows that its square simultaneously equals the two geometric constants above.

A 2006 paper of Defant and Michels discusses Banach--Mazur distances of tensor products of symmetric sequence spaces and gives Lorentz sequence spaces as examples. Its abstract concerns asymptotically optimal tensor-product estimates rather than the present two-dimensional exact identity; the full text was not available in the bounded comparison, so it remains a residual coverage risk rather than evidence of noncoverage.

## Limitations
The result is specific to the real two-dimensional Lorentz family with exponent \(q=2\). It does not claim an analogous identity for \(q\ne2\), higher-dimensional Lorentz sections, or complex scalars.

The principal originality risk is notation-sensitive prior work on finite-dimensional symmetric sequence spaces. Exact-phrase, formula, invariant, and implication searches did not locate the displayed Banach--Mazur formula or the three-way identity, but absence from search is not a proof of novelty.

## References
1. M. Kato and L. Maligranda, “On James and Jordan--von Neumann Constants of Lorentz Sequence Spaces,” Journal of Mathematical Analysis and Applications 258 (2001), 457--465. DOI: 10.1006/jmaa.2000.7367.
2. M. Kato, L. Maligranda, and Y. Takahashi, “On James and Jordan--von Neumann constants and the normal structure coefficient of Banach spaces,” Studia Mathematica 144 (2001), 275--295. DOI: 10.4064/sm144-3-5.
3. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, 107 (2012). DOI: 10.1186/1029-242X-2012-107.
4. A. Defant and C. Michels, “Norms of tensor product identities,” Note di Matematica 25 (2006), 129--166. DOI: 10.1285/i15900932v25n1p129.
