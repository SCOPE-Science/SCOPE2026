# Parity and degree-two Fourier resonances for rooted forests of \(K_{2,n}\)

## Finding
Fix an integer \(n\ge2\). Let \(K_{2,n}\) have left vertices \(u,v\), right vertices \(w_1,\ldots,w_n\), and edges \(uw_j,vw_j\). In the Boolean edge group \(G=\mathbb F_2^{2n}\), define \(f_n(x)\) to be the **number of rooted spanning forests** having edge-incidence vector \(x\). In particular, for an acyclic edge subset \(F\),
\[
f_n(1_F)=\prod_{C\in\operatorname{comp}(F)}|V(C)|,
\]
and for cyclic edge subsets this value is zero. Thus \(f_n\) is a nonnegative integer-valued *counting measure*, not the zero-one indicator of unrooted forests.

For a Walsh frequency \(\xi\in G\), classify its \(n\) right-vertex columns according to the two signs \(p_j=(-1)^{\xi_{uw_j}}\), \(q_j=(-1)^{\xi_{vw_j}}\): let \(a,b,c,d\) be the respective counts of \((p_j,q_j)=(+,+),(+,-),(-,+),(-,-)\), so that \(a+b+c+d=n\). The complete unnormalized Fourier spectrum is
\[
\boxed{\widehat f_n(\xi)=(-1)^d3^a\left[\left(1+\frac{2a}{3}-2c\right)\left(1+\frac{2a}{3}-2b\right)-\left(-\frac a3+b+c+d\right)^2\right].}\tag{1}
\]
Every quadruple of nonnegative integers summing to \(n\) occurs with multiplicity \(n!/(a!b!c!d!)\); coefficients are integers despite the rational intermediate expression.

Let \(T_ng=f_n*g\) denote unnormalized counting convolution on \(\mathbb C^G\). Then
\[
\boxed{T_n\text{ is invertible if and only if }n\text{ is even}.}\tag{2}
\]
For every odd \(n=2k+1\ge3\), the frequency with \(a=k\), \(d=k+1\), and \(b=c=0\) has zero multiplier, giving at least \(\binom n{k}\) Fourier null directions.

A more sensitive recovery statement holds uniformly: **every Fourier multiplier of Hamming weight at most two is nonzero, except when \(n=5\)**. At \(n=5\) the precisely \(20\) zero multipliers of weight two select the edges \(uw_i\) and \(vw_j\) with \(i\ne j\). There are no other zero multipliers of Hamming weight at most two.

The complete nullity is also given by a finite exact formula. Define
\[
H(a,b,c,d)=a^2-2a(b+c)+2ad+4a-3(b-c)^2-6d(b+c)-6(b+c)-3d^2+3.
\]
Then
\[
\boxed{\operatorname{nullity}(T_n)=\sum_{\substack{a,b,c,d\ge0,\ a+b+c+d=n\\H(a,b,c,d)=0}}\frac{n!}{a!b!c!d!},\quad\operatorname{rank}(T_n)=4^n-\operatorname{nullity}(T_n).}\tag{3}
\]
For example, the nullities for \(n=2,3,4,5,6,7,8,9\) are respectively \(0,3,0,30,0,245,0,1638\).

## Assumptions and scope
All \(2n\) edges are distinctly labelled. A rooted spanning forest includes every vertex and chooses exactly one root in each tree component, with isolated vertices serving as roots. Multiple root choices contributing the same edge subset are counted with multiplicity. Frequencies use Walsh characters \(\chi_\xi(x)=(-1)^{\langle\xi,x\rangle}\), Fourier coefficients are unnormalized, and convolution is taken with counting measure. Both the rank and the invertibility assertion concern the full \(4^n\)-dimensional complex signal space. The primary classification concerns discrete Fourier analysis of a counting measure, not a claim about the graph-theoretic number of unrooted forests.

## Proof
**1. A weighted forest determinant.** Let each edge \(e\) have sign weight \(s_e=(-1)^{\xi_e}\) and let \(L_s\) be the usual weighted graph Laplacian, so its off-diagonal entries are minus the corresponding edge weights and diagonal entries are their sums. The weighted matrix-forest theorem (Chebotarev–Shamis, Theorem 5) gives
\[
\widehat f_n(\xi)=\sum_{(F,R)}\prod_{e\in F}s_e=\det(I_{n+2}+L_s),
\]
where the sum ranges over all rooted spanning forests and remains valid for the signed weights. The equality also follows directly from expanding the determinant by minors of the oriented vertex-edge incidence matrix.

**2. Two-by-two Schur complement.** In the vertex order \(u,v,w_1,\ldots,w_n\), the lower-right block of \(I+L_s\) is diagonal with \(j\)th entry \(1+p_j+q_j\), which equals \(3,1,1,-1\) in the four column types and is never zero. Eliminating this block yields determinant \((-1)^d3^a\) times that of
\[
\begin{pmatrix}
1+2a/3-2c & -a/3+b+c+d\\
-a/3+b+c+d & 1+2a/3-2b
\end{pmatrix}.
\]
This establishes (1), including every normalization and multiplicity. Expanding the bracket gives \(H(a,b,c,d)/3\), so \(\widehat f_n=(-1)^d3^{a-1}H\). For \(a=0\), the displayed expression remains an integer because \(H\) is divisible by \(3\). This proves (3).

**3. Parity and a matching zero.** Reducing the determinant modulo two removes every sign: \(L_s\equiv L_+\pmod2\). The Laplacian eigenvalues of \(K_{2,n}\) are \(0,n,n+2\) once each, and \(2\) with multiplicity \(n-1\); hence
\[
\widehat f_n(\xi)\equiv\det(I+L_+)=(n+1)(n+3)3^{n-1}\pmod2.
\]
When \(n\) is even, every multiplier is odd and is consequently nonzero. Conversely, when \(n=2k+1\), choose \(k\) columns of type \((+,+)\) and \(k+1\) of type \((-,-)\). Both diagonal entries of the displayed Schur complement then equal the off-diagonal entry, so its determinant is zero. The \(\binom n{k}\) corresponding frequencies are distinct. This proves (2).

**4. Exactly one degree-two resonance.** A frequency of weight one has \((a,b,c,d)=(n-1,1,0,0)\) or the interchange of \(b,c\). The corresponding value of \(H\) is \(n^2-7\), never zero for integral \(n\ge2\). A weight-two frequency has either one column of type \((-,-)\), or two distinct columns each containing one minus sign. In the first case \(H=(n-1)(n+5)\); in the second case the two minus signs lie on the same left side (\(H=n^2-4n-17\)) or opposite left sides (\(H=(n-5)(n+1)\)). The first two expressions never vanish for integral \(n\ge2\): the quadratic \(n^2-4n-17\) has nonsquare discriminant \(84\). The final expression vanishes exactly at \(n=5\). Choosing the two distinct columns and an assignment of opposite left sides gives \(n(n-1)=20\) frequencies at \(n=5\). The zeroth-frequency coefficient is the positive number \((n+1)(n+3)3^{n-1}\). Therefore the weight-at-most-two statement follows.

## Verification
The standalone script `checks/check_rooted_forest.py` independently constructs the forest counting measure from all edge subsets for each \(1\le n\le5\), detects cycles by disjoint-set union, counts one root per component, and applies a direct integer Walsh–Hadamard transform. All \(1364\) coefficients agree with (1). The size-\(1\) computation is a diagnostic boundary check; the theorem is stated for \(n\ge2\). The signed spectrum and ranks at arbitrary width are proved symbolically; exhaustive finite checks do not substitute for the all-width proof. Run: `python3 checks/check_rooted_forest.py`.

## Relationship to prior work
Chebotarev and Shamis established the weighted matrix-forest determinant for arbitrary graphs; this identity is used as an established input and is not claimed as new. Goodall surveyed finite Fourier methods for graphical objects. The previously published complete Walsh spectrum for **spanning-tree incidence vectors** of \(K_{2,n}\) concerns a different kernel: there is no root multiplicity and only trees, so that result has highly sparse Fourier support, unlike the rooted-all-forest counting measure here. The contribution proved here is the explicit four-type all-width spectrum of the rooted-forest measure, the sharp even/odd invertibility boundary, and the unique two-edge singular resonance at width five. A general determinant representation alone does not state these cancellations or their frequency classification.

## Limitations
The counting kernel is not a zero-one forest indicator. Formula (3) is a finite multinomial sum rather than a simplified closed form for every odd-width nullity. This result does not give sharp condition numbers, a full closed classification of all high-degree zeros, or a claim for arbitrary \(K_{m,n}\) with \(m>2\). Earlier unlocated specializations of weighted forest determinants might contain an equivalent evaluated case; priority comparisons are bounded.

## References
1. Pavel Chebotarev and Elena Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575, first public arXiv submission February 25, 2006. https://arxiv.org/abs/math/0602575 . Weighted rooted-forest determinant, Theorem 5.
2. Andrew Goodall, *Fourier Analysis on Finite Abelian Groups: Some Graphical Applications*, preprint available in 2006, chapter published January 18, 2007. https://iuuk.mff.cuni.cz/~andrew/dwajgApr06.pdf . Finite Fourier methods for graph problems.
3. *Complete Walsh spectrum and sharp Fourier projection norms for the spanning trees of \(K_{2,n}\)*, published mathematical research record, November 8, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-walsh-spectrum-and-sharp-fourier-projection-norms-for-t--89f45551846c/RESULT.md . Distinct unrooted spanning-tree kernel.
