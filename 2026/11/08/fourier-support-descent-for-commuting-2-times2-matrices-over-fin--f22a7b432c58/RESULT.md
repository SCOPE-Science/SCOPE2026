# Fourier support descent for commuting \(2\times2\) matrices over finite chain rings

## Finding

Let \(R\) be any finite commutative chain ring, with maximal ideal \((\pi)\), residue-field size \(q\ge2\), nilpotency length \(k\ge1\), and \(|R|=q^k\). Let
\[
\mathcal C_R=\{(X,Y)\in M_2(R)^2:XY=YX\}.
\]
Choose a generating additive character \(\psi:R\to\mathbb C^\times\) and write its unnormalized additive Fourier transform as
\[
F_R(A,B)=\sum_{(X,Y)\in\mathcal C_R}\psi(\operatorname{tr}(AX+BY)).
\]
For \(A,B\in M_2(R)\), define the two-row, three-column frequency matrix
\[
W(A,B)=\begin{pmatrix}A_{11}&A_{21}&A_{12}\\ B_{11}&B_{21}&B_{12}\end{pmatrix}.
\]
**The Fourier-support descent theorem** is
\[
F_R(A,B)\ne0\quad\Longleftrightarrow\quad
\operatorname{tr}A=\operatorname{tr}B=0\ \text{and every }2\times2\text{ minor of }W(A,B)\text{ belongs to }(\pi^{k-1}).
\]
For \(k=1\), the last condition is vacuous. Equivalently, after removing the two scalar coordinates, the Fourier support is precisely the full inverse image of the rank-one determinantal congruence variety one ring-length lower. All Fourier coefficients are rational integers and depend only on \(q,k\) and the Smith exponents of \(W\).

In particular, the complex rank of unnormalized convolution by \(\mathbf1_{\mathcal C_R}\) on the additive group \(M_2(R)^2\) is exactly
\[
\boxed{\operatorname{rank}T_{\mathcal C_R}=(q^2+q+1)q^{4k}-(q+1)q^{3k+1}.}
\]
Its nullity is \(q^{8k}-\operatorname{rank}T_{\mathcal C_R}\). The formula applies unchanged to equal-characteristic and mixed-characteristic chain rings, including residue characteristic two. For fixed \(q\), the surviving Fourier fraction is asymptotic to \((q^2+q+1)q^{-4k}\).

## Assumptions and scope

The ring is finite, commutative, local and a principal ideal chain ring; the nonzero ideals are \((\pi^j)\), with \(0\le j<k\), and \(\pi^k=0\). For an element \(u\in R\), write \(\nu(u)\) for the largest \(j\le k\) with \(u\in(\pi^j)\), so \(\nu(0)=k\). A generating character is one whose kernel contains no nonzero ideal. Such a character exists: choose a nontrivial character on the minimal nonzero ideal and extend it to the finite additive group. Its induced character on \(R/(\pi^m)\), defined by multiplication by \(\pi^{k-m}\), is also generating.

When the two traces vanish, let \(0\le s\le t\le k\) be the Smith exponents of \(W=W(A,B)\): invertible row and column operations over \(R\) reduce it to \(\begin{psmallmatrix}\pi^s&0&0\\0&\pi^t&0\end{psmallmatrix}\), with \(\pi^k=0\). Then \(F_R(A,B)=q^{2k}H_{s,t}\), where the complete multiplier is as follows. For \(t<k\),
\[
H_{s,t}=\begin{cases}
0,&s+t\le k-2,\\
-q^{3k-2},&s+t=k-1,\\
q^{2k+s+t}-(q+1)q^{3k-2},&s+t\ge k.
\end{cases}
\]
For \(0\le s<k\),
\[
H_{s,k}=q^{3k}+(q^3-1)\sum_{h=k-s}^{k-1}q^{4k-h-3}-q^{3k+s-2},
\]
with an empty sum interpreted as zero, and
\[
H_{k,k}=q^{3k}+(q^3-1)\sum_{h=0}^{k-1}q^{4k-h-3}=|\mathcal D_k|,
\]
where \(\mathcal D_m=\{(u,v)\in(R/(\pi^m))^3\times(R/(\pi^m))^3:u\wedge v=0\}\) and \(|\mathcal D_0|=1\). When either trace is nonzero, \(F_R(A,B)=0\).

## Proof

**1. Quotient the scalar directions, without dividing by two.** Every matrix has a unique additive decomposition
\[
X=xI+\begin{pmatrix}u_1&u_2\\u_3&0\end{pmatrix},\qquad x,u_1,u_2,u_3\in R.
\]
For the corresponding decomposition of \(Y\) with vector \(v\), the commutator vanishes if and only if \(u\wedge v=0\) in \(\bigwedge^2R^3\): its three independent entries are the three signed minors \(u_iv_j-u_jv_i\). Summing over scalar parameters \(x,y\) forces \(\operatorname{tr}A=\operatorname{tr}B=0\) and contributes \(q^{2k}\). The remaining character pairing is exactly the dot product of the two rows of \(W\) with \(u,v\), respectively. Therefore, conditional on the trace equalities, \(F_R(A,B)=q^{2k}H(W)\), where \(H\) is the unnormalized Fourier transform of \(\mathbf1_{\mathcal D_k}\).

**2. Reduce frequency matrices to Smith form.** The cone \(\mathcal D_k\) is preserved by invertible linear transformations of the two row indices and the three column indices. Consequently its Fourier transform is constant on the corresponding dual orbits, classified by Smith exponents \(s,t\). It is enough to evaluate \(H\) at \(a=\pi^s e_1\), \(b=\pi^t e_2\), with the convention \(\pi^k=0\).

**3. Exact primitive-vector character sum.** Set \(m=k-h\). Every nonzero \(u\in R^3\) of depth \(h\) can be written uniquely as \(u=\pi^h u_0\), with \(u_0\in(R/(\pi^m))^3\) primitive (at least one unit coordinate). The equation \(u\wedge v=0\) is equivalent to \(v\equiv c u_0\pmod{\pi^m}\) for some \(c\in R/(\pi^m)\). For such \(u\) there are exactly \(q^{m+3h}=q^{k+2h}\) admissible \(v\).

For a vector \(c\in(R/(\pi^m))^3\), let \(\nu_m(c)\) be the minimum truncated valuation of its coordinates. The annihilator of the hyperplane \(c\cdot z=0\) under a generating character is exactly the one-dimensional module \((R/(\pi^m))c\). The hyperplane has cardinality \(q^{2m+\nu_m(c)}\): this follows after an invertible change of coordinates sending \(c\) to \(\pi^{\nu_m(c)}e_1\). Subtracting the vectors divisible by \(\pi\) gives the exact sum over primitive vectors:
\[
S_m(a,c)=q^{2m+\nu_m(c)}\mathbf1_{\{a\in(R/(\pi^m))c\}}
-q^{2m-2+\nu_{m-1}(c)}\mathbf1_{\{a\bmod\pi^{m-1}\in(R/(\pi^{m-1}))(c\bmod\pi^{m-1})\}}.
\]
The second term is interpreted over the trivial ring when \(m=1\). Summing the admissible \(v\), then the primitive \(u_0\), yields
\[
H(a,b)=q^{3k}\mathbf1_{\{b=0\}}+\sum_{h=0}^{k-1}q^{k+2h}\mathbf1_{\{b\in(\pi^h)R^3\}}S_{k-h}(a,b/\pi^h).
\]
The quotient \(b/\pi^h\) here denotes its unique class modulo \(\pi^{k-h}\), not a choice of an inverse in \(R\).

**4. Evaluate the two Smith valuations.** If \(t<k\), only \(h\le t\) contribute. For the diagonal frequency vectors, the first indicator in \(S_{k-h}\) holds exactly when \(h\ge k-s\), and the second exactly when \(h\ge k-s-1\). Thus
\[
H_{s,t}=\sum_{h=0}^{t}q^{3k+t-h}\mathbf1_{\{h\ge k-s\}}
-\sum_{h=0}^{t}q^{3k+t-h-2}\mathbf1_{\{h\ge k-s-1\}}.
\]
Summing these two geometric progressions gives the displayed three branches for \(t<k\). If \(t=k\), use \(c=0\) in \(S_m\); this gives the separate two formulas above. For \(s=0<t=k\), \(H_{0,k}=q^{3k}-q^{3k-2}>0\). For \(1\le s<k\), the term with \(h=k-s\) exceeds the negative boundary term by \((q^3-q-1)q^{3k+s-3}>0\), and the remaining summands are nonnegative. Hence all \(H_{s,k}\) are positive. For \(t<k\), \(H_{s,t}=0\) occurs only when \(s+t\le k-2\): the boundary branch is strictly negative, and the last branch is strictly positive since \(q^2-q-1>0\) for every integer \(q\ge2\).

**5. Identify the one-level determinantal descent and count Fourier support.** The ideal of all \(2\times2\) minors of a Smith matrix \(\operatorname{diag}(\pi^s,\pi^t)\) is \((\pi^{\min(s+t,k)})\). Hence \(H(W)\ne0\) precisely when all its minors vanish modulo \(\pi^{k-1}\). Of the \(q^{6k}\) possible frequency matrices \(W\), exactly \(q^6|\mathcal D_{k-1}|\) satisfy that condition. To count \(\mathcal D_m\), partition the first vector by depth \(h\), noting that there are \((q^3-1)q^{3(m-h-1)}\) vectors of depth \(h\), each allowing \(q^{m+2h}\) choices for the second vector. Thus, for \(m\ge1\),
\[
|\mathcal D_m|=q^{3m}+(q^3-1)\sum_{h=0}^{m-1}q^{4m-h-3}.
\]
The same counting formula at \(m=0\) is interpreted as \(|\mathcal D_0|=1\). Substituting \(m=k-1\) and summing the geometric series gives
\[
q^6|\mathcal D_{k-1}|=(q^2+q+1)q^{4k}-(q+1)q^{3k+1}.
\]
Fourier characters diagonalize convolution on finite abelian groups, so the number of nonzero multipliers is the convolution rank. This completes the proof.

## Verification

The standalone program `verify_commuting_chain.py` enumerates the rank-one congruence cone and computes its finite additive Fourier transform for cyclic rings \(\mathbb Z/2\mathbb Z\), \(\mathbb Z/3\mathbb Z\), \(\mathbb Z/4\mathbb Z\), \(\mathbb Z/9\mathbb Z\), and \(\mathbb Z/8\mathbb Z\). It checks every predicted vanishing/nonvanishing frequency, as well as the exact rank. For each possible Smith stratum, it separately evaluates a canonical Fourier coefficient using integer cyclotomic-polynomial reduction and compares it with the proved formula. It further checks **all** 4,096 Fourier coefficients over the noncyclic chain ring \(\mathbb F_2[t]/(t^2)\) by exact integer Walsh–Hadamard arithmetic and verifies their Smith-stratum values. The transform-wide cyclic tests use floating-point FFTs with a stated tolerance; the exact canonical checks and the symbolic proof do not rely on this numerical approximation.

A reproducible command in a Python environment with NumPy is `python3 verify_commuting_chain.py`. The general statement for all \(q,k\) is established by the proof above, not by these finite tests. Example quotient Fourier ranks are 64 for \(q=2,k=1\), 1,408 for \(q=2,k=2\), 25,600 for \(q=2,k=3\), and 76,545 for \(q=3,k=2\); these are also convolution ranks on the corresponding eight-coordinate groups.

## Relationship to prior work

Košir and Sethuraman [1] investigate precisely the higher-order \(2\times3\) determinantal congruence variety over truncated polynomial rings, including its geometric components and dimensions, motivated by centralizers of commuting matrices. The present statement addresses a different invariant: all *additive Fourier zeros and exact multipliers* of the commuting-pair indicator over **every** finite commutative chain ring, including mixed characteristic. Geometry and dimension alone do not determine this Fourier transform, and the one-level descent is not asserted in [1].

Britnell and Wildon [2] study which finite-field similarity classes admit commuting representatives and their centralizer types. Those results do not supply the unnormalized additive Fourier transform of all commuting pairs over nonfields. Browning, Sawin and Wang [3], §3–4, explicitly define matrix exponential sums on commuting pairs over prime fields and derive bounds needed for integral-point counting. Their displayed estimates do not give the exact chain-ring zero criterion or convolution rank above. Existing one-variable or determinant-zero convolution formulas concern different incidence relations, not the two-row determinantal congruence here. No stronger covering statement was identified in the checked literature, but historical matrix-association or local exponential-sum theory may contain a reformulation.

## Limitations

No classification of the *multiplicities of every nonzero* Fourier value beyond the Smith-stratum formula is asserted. Noncommutative, non-chain and infinite rings are not covered. The result does not address the exact Fourier spectra for commuting matrices of size greater than two. The publication-priority assessment is bounded by the examined sources; an older equivalent theorem in general rank-metric or association-scheme language remains possible. Numerical checks cannot certify the infinite family. Independent mathematical validation has not been performed.

## References

1. Tomaž Košir and B. A. Sethuraman, *Determinantal Varieties Over Truncated Polynomial Rings*, arXiv:math/0212051v1 (first public 2002-12-03), https://arxiv.org/abs/math/0212051. In particular Introduction, Lemma 2.1 and §5.
2. John R. Britnell and Mark Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first public 2010-01-06), https://arxiv.org/abs/1001.0811.
3. Tim Browning, Will Sawin and Victor Y. Wang, *Pairs of commuting integer matrices*, arXiv:2409.01920 (first public 2024-09-03), https://arxiv.org/abs/2409.01920. In particular §3, formula (3.1), and §4.
