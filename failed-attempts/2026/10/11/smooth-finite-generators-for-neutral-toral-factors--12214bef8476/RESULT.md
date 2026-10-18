# Smooth finite generators for neutral toral factors
## Finding
For every integer \(q\ge 1\), consider the Haar-preserving endomorphism
\[
T_q:\mathbb T^{q+1}\longrightarrow\mathbb T^{q+1},\qquad
T_q(x_1,\ldots,x_q,y)=(x_1,\ldots,x_q,2y\bmod 1).
\]
Its defining integer matrix is \(A_q=\operatorname{diag}(I_q,2)\), so \(|\det A_q|=2\) and \(A_q\) is not expanding because \(1\) is an eigenvalue. Nevertheless, \(T_q\) has an explicit smooth finite one-sided generator with at most \(2^{q+1}\) atoms.

Represent every circle coordinate by its unique element of \([0,1)\). Define
\[
\beta(y)=\mathbf 1_{[1/2,1)}(y),\qquad
\gamma_j(x_j,y)=\mathbf 1_{\{y<x_j\}},\quad 1\le j\le q,
\]
and partition \(\mathbb T^{q+1}\) by the label
\[
L(x_1,\ldots,x_q,y)=\bigl(\beta(y),\gamma_1(x_1,y),\ldots,\gamma_q(x_q,y)\bigr).
\]
The resulting partition is a one-sided generator modulo Haar-null sets.

This gives a neutral-eigenvalue boundary to the smooth-generator obstruction in arXiv:2610.01642v1. That preprint states in its abstract that every nonexpanding toral endomorphism lacks a smooth finite generator, while its precise Theorem 1 assumes an eigenvalue of modulus strictly smaller than \(1\). The family above shows that the strict contraction hypothesis cannot be replaced by mere nonexpansion.

## Assumptions and scope
The torus is \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\) with Haar probability measure. A finite partition is a one-sided generator when the names \(L(T_q^n z)\), \(n\ge0\), separate points on a full-measure subset. A partition is smooth in the sense used in the motivating source when atom boundaries are piecewise smooth differentiable submanifolds.

No ergodicity of \(T_q\) is asserted: the coordinates \(x_1,\ldots,x_q\) are invariant. The only ergodicity used below is that of the doubling map on the final circle coordinate.

## Proof
Let \(D(y)=2y\bmod1\). Write
\[
L(T_q^n(x_1,\ldots,x_q,y))=(b_n,c_{1,n},\ldots,c_{q,n}).
\]
Then
\[
b_n=\mathbf 1_{[1/2,1)}(D^n y),\qquad
c_{j,n}=\mathbf 1_{\{D^n y<x_j\}}.
\]

First, the sequence \((b_n)_{n\ge0}\) reconstructs \(y\) exactly. Indeed, if \(r_n=D^n y\in[0,1)\), then \(r_{n+1}=2r_n-b_n\). Iterating this identity gives
\[
y=\sum_{n=0}^{N-1} b_n2^{-n-1}+2^{-N}r_N.
\]
Since \(0\le r_N<1\), letting \(N\to\infty\) yields
\[
y=\sum_{n=0}^\infty b_n2^{-n-1}.
\]
Thus the full orbit \((D^n y)_{n\ge0}\) is also known from the name.

The doubling map is ergodic for Lebesgue measure. Applying the ergodic theorem to a countable basis of intervals with rational endpoints shows that, for Lebesgue-almost every \(y\), the orbit \(\{D^n y:n\ge0\}\) is dense in \([0,1)\). Fix such a \(y\). For every \(j\), the comparison bits determine the subset of orbit values below \(x_j\), and density gives
\[
x_j=\sup\Bigl(\{0\}\cup\{D^n y:c_{j,n}=1\}\Bigr).
\]
Therefore the one-sided name determines \((x_1,\ldots,x_q,y)\) on the full-measure set \(\mathbb T^q\times Y_\mathrm{dense}\). Hence the partition is a generator modulo Haar-null sets.

It remains to verify smoothness. In the fundamental cube \([0,1)^{q+1}\), every atom is a finite Boolean combination of the half-spaces cut by \(y=1/2\) and \(y=x_j\). After passing to the torus, possible discontinuities of the chosen representatives add only the coordinate seams \(y=0\) and \(x_j=0\). Thus every atom boundary is contained in a finite union of affine codimension-one subtori or their smooth pieces, with lower-dimensional intersections. The partition is therefore smooth in the stated sense.

## Verification
The reconstruction argument is exact and does not rely on finite enumeration or numerical extrapolation. The identity
\[
y=\sum_{n=0}^{N-1} b_n2^{-n-1}+2^{-N}D^N y
\]
checks the binary-coordinate recovery, including dyadic points under the chosen half-open convention. Dense-orbit recovery of each invariant coordinate uses only the supremum formula above. The exceptional set is confined to the null set of doubling orbits that are not dense; no claim is made that every point is separated.

The construction was also stress-tested on finite orbit prefixes as a diagnostic only; those finite tests are not used as proof.

## Relationship to prior work
Leuridan's arXiv:2610.01642v1 defines one-sided generators by separation on a full-measure set and smooth partitions by piecewise smooth boundaries. Its abstract asserts nonexistence of smooth finite generators for every nonexpanding toral endomorphism, including nonhyperbolic ones. In the body, however, the precise negative theorem assumes an eigenvalue of modulus strictly smaller than \(1\). The same paper also explains that an earlier construction produces smooth Rokhlin partitions even when the matrix is not expanding, but does not claim those partitions are generators in the neutral case.

Mihailescu's earlier result excludes generating Rokhlin partitions for hyperbolic nonexpanding toral endomorphisms. It does not cover \(A_q=\operatorname{diag}(I_q,2)\), which is nonhyperbolic because of the eigenvalue \(1\), and the partition constructed here need not be a Rokhlin partition.

The present finding therefore identifies the neutral spectral boundary explicitly: a contracting eigenvalue can obstruct smooth finite generators under the hypotheses of Leuridan's theorem, whereas neutral identity factors can coexist with a smooth finite generator because the expanding coordinate can act as a dense comparison probe.

## Limitations
The claim is only for the explicit family \(\operatorname{diag}(I_q,2)\); it does not classify all nonhyperbolic nonexpanding integer matrices. It does not assert that the displayed generator is independent, Rokhlin, minimal in alphabet size, or topologically generating at every point. An equivalent comparison coding may exist in older general generator literature not located in the checked searches; that residual possibility affects originality, not the proof or the counterexample to the broad nonexpanding assertion.

## References
1. Christophe Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators*, arXiv:2610.01642v1, first public 2026-10-01.
2. Eugen Mihailescu, *On some coding and mixing properties for a class of chaotic systems*, Monatshefte für Mathematik 167 (2012), 241–255, DOI:10.1007/s00605-011-0347-8.
