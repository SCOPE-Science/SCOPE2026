# Exact five-point positive-type extension region on \(S_3\) and a strict local-to-global gap

## Finding

Let \(G=S_3=\langle s,t:s^2=t^2=(st)^3=e\rangle\), and let the five-point inverse-closed set be \(\Delta=\{e,s,t,st,ts\}\). For real \(a,b,c\), prescribe normalized Hermitian scalar Fourier data
\[
\varphi(e)=1,\quad \varphi(s)=a,\quad\varphi(t)=b,\quad\varphi(st)=\varphi(ts)=c.
\]
A *local positive-type datum* means that every fully specified Gram matrix \((\varphi(x^{-1}y))_{x,y\in\Sigma}\), with \(\Sigma^{-1}\Sigma\subseteq\Delta\), is positive semidefinite. A *global positive-type extension* is a complex-valued positive-definite function \(\Phi:G\to\mathbb C\) agreeing with those five values; it is not assumed a priori that the unspecified value is real.

**Theorem (exact local and global regions).** The datum is locally positive if and only if
\[
-\tfrac12\le c\le1,\qquad |a|\le1,\quad|b|\le1,\qquad
1+2abc-a^2-b^2-c^2\ge0.
\tag{L}
\]
It admits a global positive-type extension if and only if
\[
\boxed{ -\tfrac12\le c\le1,\qquad
\left(\max\{\,|a+b|-\tfrac23(1+2c),\,0\}\right)^2
+\tfrac13(a-b)^2\le\tfrac49(1-c)^2. }
\tag{G}
\]
Thus each fixed-\(c\) global region is the Minkowski sum of a closed ellipse with a line segment along the diagonal in the \((a,b)\)-plane.

**All completions.** Write \(d=\Phi(sts)\) for the missing transposition. A real completion exists exactly when the following two inequalities admit a common real \(d\):
\[
|a+b+d|\le 1+2c,
\qquad
(a+b-2d)^2+3(a-b)^2\le4(1-c)^2.
\tag{C}
\]
Every real \(d\) satisfying these inequalities gives a globally positive-type extension. If a complex extension exists, a real extension also exists. This is an exact constructive completion criterion, including degenerate boundary points.

**Sharp symmetric local-to-global gap.** On the slice \(a=b=h\), the local criterion is
\[
|h|\le\sqrt{\frac{1+c}{2}},
\]
while global extendibility is exactly
\[
|h|\le\frac{2+c}{3}.
\]
For every \(-\tfrac12<c<1\), these bounds differ strictly, since
\[
\frac{1+c}{2}-\left(\frac{2+c}{3}\right)^2
=\frac{(1-c)(1+2c)}{18}>0.
\]
In particular, the rational datum \(a=b=11/16\), \(c=0\) is locally positive, with the nontrivial three-point Gram determinant \(7/128>0\), but does not admit *any* positive-type extension.

## Assumptions and scope

The group is the six-element nonabelian symmetric group with the displayed Coxeter presentation. Values are normalized by \(\varphi(e)=1\), and all four other specified entries are real; the missing value may initially be complex. Positivity means positive *semidefiniteness*, including boundary and singular cases. No commutativity or class-function assumption is imposed on an extension. The theorem classifies exactly this five-point domain; it neither characterizes general partial domains nor operator-valued positive extensions.

## Proof

**1. Classify every required local Gram test.** The graph on \(G\), with an edge \(x\!\sim\!y\) whenever \(x^{-1}y\in\Delta\setminus\{e\}\), is the octahedral graph \(K_6\) with a perfect matching removed. Indeed, the one forbidden difference is the remaining transposition \(u=sts\), of order two; hence nonedges pair \(x\) with \(xu\). Every clique contains at most three vertices. There are exactly eight maximal three-vertex cliques, six with their three off-diagonal data \(a,b,c\), and two with all three off-diagonal data \(c\). This can be verified directly by the six group products, and a deterministic enumeration in `check.py` supplies a supplementary finite check. The two maximal Gram types, up to simultaneous permutation, are
\[
M_{abc}=\begin{pmatrix}1&a&b\\a&1&c\\b&c&1\end{pmatrix},
\qquad
M_{ccc}=\begin{pmatrix}1&c&c\\c&1&c\\c&c&1\end{pmatrix}.
\]
Their positive semidefiniteness is equivalent to (L): \(M_{ccc}\) has eigenvalues \(1+2c,1-c,1-c\), while \(M_{abc}\) has determinant \(1+2abc-a^2-b^2-c^2\), and its order-two principal minors are nonnegative exactly when \(|a|,|b|,|c|\le1\). The latter bound on \(c\) is already implied by the former eigenvalue bounds. All smaller cliques are principal submatrices, proving (L).

**2. A real missing value suffices.** If \(\Phi\) is positive definite, then so is its pointwise complex conjugate: their Gram matrices are related by complex conjugation and both are positive semidefinite. Their arithmetic mean is a real-valued positive-definite extension, because all specified values are real. Consequently it is enough to classify real \(d=\Phi(u)\).

**3. Compute every irreducible Fourier positivity condition.** A real function \(\Phi\) on a finite group is positive definite if and only if its Fourier matrices in all unitary irreducible representations are positive semidefinite. For \(S_3\), these representations are the trivial character, the sign character, and the standard real two-dimensional representation. Put
\[
S=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
T=\begin{pmatrix}-\tfrac12&\tfrac{\sqrt3}{2}\\\tfrac{\sqrt3}{2}&\tfrac12\end{pmatrix},\qquad
U=-S-T.
\]
The reflection generators have matrices \(S,T\), the remaining reflection has \(U\), and the two three-cycles sum to \(-I_2\). The unnormalized Fourier transforms, with any consistent inversion convention (all matrices here are symmetric), are therefore
\[
\widehat\Phi(\mathbf1)=1+2c+a+b+d,
\qquad
\widehat\Phi(\operatorname{sgn})=1+2c-a-b-d,
\]
\[
\widehat\Phi(\operatorname{Std})=(1-c)I_2+(a-d)S+(b-d)T.
\]
The scalar transforms are nonnegative precisely when \(|a+b+d|\le 1+2c\). Since \(S^2=T^2=I_2\) and \(ST+TS=-I_2\), the last matrix has eigenvalues
\[
(1-c)\pm\sqrt{(a-d)^2+(b-d)^2-(a-d)(b-d)}.
\]
Its positive semidefiniteness is exactly the second condition in (C), together with \(c\le1\). The scalar conditions imply \(c\ge-1/2\), so the pair in (C) is both necessary and sufficient, including the endpoints. The finite-group Fourier criterion follows, for instance, from decomposing the left-regular representation into its three irreducible blocks; equivalently, it diagonalizes the full six-by-six kernel \((\Phi(x^{-1}y))_{x,y\in G}\).

**4. Eliminate the missing coordinate sharply.** Let
\[
p=\tfrac23(1-c)\ge0,\qquad q=\tfrac13(1+2c)\ge0,\qquad p+q=1.
\]
Rearranging (C), global completion holds precisely when there is a \(z\in[-2q,2q]\) with
\[
(a+b-z)^2+\tfrac13(a-b)^2\le p^2.
\]
Indeed, set \(z=\tfrac23(a+b+d)\); then the first condition in (C) gives \(|z|\le2q\), and \(a+b-2d=3(a+b-z)\), producing the second inequality after division by nine. Conversely, given \(z\), set \(d=\frac32z-(a+b)\). The minimum of \((a+b-z)^2\) over this interval is \((\max\{|a+b|-2q,0\})^2\). This yields precisely (G) and the capsule description.

**5. Prove and attain the gap.** For \(a=b=h\), \(\det M_{abc}=(1-c)(1+c-2h^2)\), and the exact local range is \(|h|\le\sqrt{(1+c)/2}\), including \(c=1\) by the two-by-two principal minors. In (G), \(a-b=0\), and the allowed symmetric interval is \(|2h|\le2q+p\), equivalently \(|h|\le q+p/2=(2+c)/3\). Direct subtraction gives the displayed strictly positive difference for every \(-1/2<c<1\). For \(h=11/16,c=0\), the local determinant is \(7/128\) and the global bound is \(2/3<11/16\), proving the rational witness. Moreover the missing-coordinate inequalities require simultaneously \(d\le-3/8\) and \(d\ge-5/16\); their exact gap is \(1/16\).

This completes the proof of all claims, with no numerical hypotheses.

## Verification

The accompanying `check.py` uses the six-element product law to enumerate all eight maximal specified cliques and checks their two Gram types. It verifies the rational witness and the exact disjoint missing-coordinate intervals in rational arithmetic, tests full six-by-six positive kernels built from 450 explicit sampled representation states, compares the elimination formula with missing-coordinate interval intersection at 650 additional sampled points, and verifies four rational strict-gap identities. It prints one `PASS` line on success and raises an assertion error otherwise. Execute `python check.py` with Python 3 and NumPy. Finite sampling independently stress-tests formulae but is not substituted for the proof in the preceding section.

## Relationship to prior work

Kakariadis, Leimbach, Todorov and van Suijlekom (2026) develop a general operator-system formulation of positive-type extensions over discrete groups, including a worked five-point domain in \(\mathbb Z^2\). The example and general quotient-map criteria are not the displayed explicit scalar \(S_3\) completion classification. Bakonyi and Timotin (2008) prove that chordal Cayley-domain patterns admit universal positive-definite extensions; the present five-point \(S_3\) graph is not chordal and therefore falls outside that sufficient theorem. Grone, Johnson, Sá and Wolkowicz (1984) prove a general chordal-pattern criterion for unstructured PSD matrix completion, including the existence of noncompletable data when chordality fails; it does not by itself give the normalized group-invariant three-variable completion region or the sharp symmetric obstruction across every \(c\). The present result calculates that region rather than merely invoking a general nonchordality obstruction.

## Limitations

The method applies to real-valued prescribed data on the exact five-element domain; it does not classify arbitrary complex prescribed values or operator-valued data. It proves only the specific group \(S_3\), not all dihedral groups. The Fourier irreducible decomposition is classical; the potentially new content is the explicit normalized projection, exact simultaneous scalar/standard-block completion conditions, and strict local-to-global threshold for every interior \(c\). An earlier equivalent finite-group positive-type extension or semidefinite completion calculation may exist outside the inspected literature. No independent mathematical audit has been performed.

## References

1. E. T. A. Kakariadis, M. Leimbach, I. G. Todorov and W. D. van Suijlekom, *Operator systems and positive extensions over discrete groups*, arXiv:2603.29958, first public 31 March 2026. https://arxiv.org/abs/2603.29958
2. M. Bakonyi and D. Timotin, *Extensions of positive definite functions on amenable groups*, arXiv:0808.1273 (2008), later Canad. Math. Bull. 54 (2011). https://arxiv.org/abs/0808.1273
3. R. Grone, C. R. Johnson, E. M. Sá and H. Wolkowicz, *Positive definite completions of partial Hermitian matrices*, Linear Algebra and its Applications 58 (1984), 109–124. https://doi.org/10.1016/0024-3795(84)90207-6
