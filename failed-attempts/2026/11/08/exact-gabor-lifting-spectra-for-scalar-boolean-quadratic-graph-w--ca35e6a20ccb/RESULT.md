# Exact Gabor lifting spectra for scalar Boolean quadratic graph windows

## Finding
Let \(m\ge 1\), let \(Q:\mathbb F_2^m\to\mathbb F_2\) be a Boolean polynomial of degree at most two, and write \(B_Q(u,v)=Q(u+v)+Q(u)+Q(v)+Q(0)\). Its rank is even, say \(2r\), with radical dimension \(k=m-2r\). Set
\[
 N=2^{m+1},\quad M=2^m,\quad D=2^{2r},\quad K=2^k,\quad G=\mathbb F_2^m\times\mathbb F_2.
\]
Let \(S_Q=\{(x,Q(x)):x\in\mathbb F_2^m\}\) and \(g=\mathbf1_{S_Q}\), with no norm rescaling. For \(a,b,z\in G\), use \((T_ag)(z)=g(z+a)\), \((M_bg)(z)=(-1)^{b\cdot z}g(z)\), and \(g_{a,b}=M_bT_ag\). Define the complex-linear operator
\[
 \mathcal L_g:\mathbb C^{N\times N}\to\mathbb C^{G\times G},\qquad (\mathcal L_g H)(a,b)=\operatorname{tr}(g_{a,b}g_{a,b}^*H),
\]
with Hilbert--Schmidt norms in the domain and ordinary Euclidean norms in the codomain.

**Theorem.** The multiset of positive singular values of \(\mathcal L_g\), with multiplicities, is
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
\sqrt N\,M&K\\
\sqrt N\,M/2&4K(D-1)\\
\sqrt N\,K\sqrt D&KD^2.
\end{array}
\]
The middle multiplicity is zero when \(r=0\). Equal numeric singular values from different rows contribute **additive** multiplicities. All other singular values vanish. Thus
\[
\operatorname{rank}\mathcal L_g=K(D^2+4D-3),\qquad \operatorname{nullity}\mathcal L_g=N^2-K(D^2+4D-3).
\]
The result depends only on the polar rank, not the affine part or Arf invariant of \(Q\).

With the *same* support \(S_Q\), a generic window \(h\) taking arbitrary nonzero complex values on that support has exactly
\[
 \operatorname{rank}\mathcal L_h=N|S_Q-S_Q|=N(N-K).
\]
Here generic means on a nonempty open dense subset of full Lebesgue measure in the space of nonzero complex support coefficients. In the nondegenerate case \(k=0\), the indicator rank is \(2^{2m}+4\cdot 2^m-3\), asymptotic to \(N^2/4\), whereas generic weighting reaches \(N(N-1)\).

## Assumptions and scope
All sums and Boolean polars are over \(\mathbb F_2\), except the Fourier and matrix operations, which are over \(\mathbb C\). The graph has cardinality \(M\). No normalization of the window, character matrix, projector, or measurement operator is implicit. A rank here is the complex-linear rank of the complete matrix analysis operator, **not** the rank of the length-\(N\) Gabor synthesis frame and **not** a claim that arbitrary signals admit phase retrieval. The theorem includes degenerate forms, including affine \(Q\) with \(r=0\). In characteristic two, every alternating bilinear form has even rank.

## Proof
**Step 1 (Weyl diagonalization and normalization).** Put \(W_{u,v}=M_vT_u\) for \((u,v)\in G^2\). The normalized matrices \(W_{u,v}/\sqrt N\) form an orthonormal Hilbert--Schmidt basis of all complex \(N\)-by-\(N\) matrices. For a window \(h\), define its ambiguity coefficient
\[
 A_h(u,v)=\langle h,W_{u,v}h\rangle
 =\sum_{z\in G}\overline{h(z)}h(z+u)(-1)^{v\cdot z}.
\]
For each basis element, conjugating by the time--frequency shift multiplies its projector pairing by a character of \(G^2\). Orthogonality of the \(N^2\) characters therefore makes \(\mathcal L_h^*\mathcal L_h\) diagonal in the Weyl basis with eigenvalues \(N|A_h(u,v)|^2\). Hence every singular value is \(\sqrt N|A_h(u,v)|\), with zeros included. This establishes the normalization independently of any injectivity assumption.

**Step 2 (quadratic normal form).** An invertible linear change of the \(m\) input coordinates expresses the polar as \(r\) hyperbolic pairs plus a \(k\)-dimensional radical. Every quadratic with that polar differs from \(Q_0(x)=\sum_{j=1}^r x_{2j-1}x_{2j}\) by an affine-linear function; its contribution to the graph is removed by the group automorphism \((x,t)\mapsto(x,t+\ell(x))\) and a translation in the last coordinate. Such transformations permute Weyl shifts up to phases, so preserve all singular values. Thus it suffices to analyze \(Q_0\).

**Step 3 (nondegenerate block).** First take \(k=0\), write \(d=2r\), and use \(D=2^d\). Direct factorization over the \(r\) independent coordinate pairs gives the bent Walsh identity
\[
 W_Q(v):=\sum_{x\in\mathbb F_2^d}(-1)^{Q_0(x)+v\cdot x}\in\{-\sqrt D,\sqrt D\}
\]
when \(r>0\) (the single empty product when \(r=0\) equals one).
For a translation \(u=(a,t)\) with \(a=0\), only \(t=0\) has overlapping graph supports: at last modulation coordinate zero there is the one coefficient \(D\); at last modulation coordinate one there are \(D\) coefficients of magnitude \(\sqrt D\). A translation \((0,1)\) has empty overlap.

For \(a\ne0\), let \(L_a(x)=B_Q(x,a)\), a nonzero linear functional. The graph-overlap condition is \(L_a(x)=t+Q_0(a)\); the overlap therefore is an affine hyperplane of size \(D/2\). If the last modulation coordinate is zero, its Walsh transform is supported on the two characters \(v=0\) and \(v=L_a\), each of modulus \(D/2\). Summing both values of \(t\) gives \(4\) such coefficients per nonzero \(a\). If the last modulation coordinate is one, each relevant coefficient is half the sum or difference of \(W_Q(v)\) and \(W_Q(v+L_a)\). Since these two Walsh values each have magnitude \(\sqrt D\), exactly one choice of \(t\) yields an absolute value \(\sqrt D\), and the other yields zero, for every \(v\). Thus \(D\) coefficients of that magnitude occur per nonzero \(a\). Altogether the nondegenerate block has exactly one coefficient of magnitude \(D\), \(4(D-1)\) of magnitude \(D/2\), and \(D^2\) of magnitude \(\sqrt D\). For \(r=0\), there are two coefficients of magnitude one and no others, consistent with coinciding first and last categories.

**Step 4 (radical factor and rank).** When \(k>0\), reorder coordinates so that \(g=\mathbf1_{S_{Q_0}}\otimes\mathbf1_{\mathbb F_2^k}\). The radical block contributes ambiguity factor \(K\) for each of its \(K\) translation shifts with zero radical modulation and contributes zero for every nonzero radical modulation. Each positive coefficient of the nondegenerate block therefore is multiplied by \(K\) and repeated \(K\) times. Replacing \(D\) by \(M=KD\) where appropriate gives exactly the three stated singular-value rows and the rank formula. The original quadratic normal-form change returns the claim for every \(Q\).

**Step 5 (generic reweighting).** A graph translation \((a,t)\) belongs to \(S_Q-S_Q\) iff the Boolean difference \(Q(x+a)+Q(x)\) equals \(t\) for at least one \(x\). If \(a\) lies in the polar radical (\(K\) possibilities), this difference is constant, giving one \(t\). Otherwise the difference is a nonconstant affine functional, giving both values of \(t\). Hence
\[
 |S_Q-S_Q|=K+2(M-K)=N-K.
\]
For every supported translation and every modulation, \(A_h(a,b)\) is a real polynomial in the real and imaginary parts of the independent complex support weights and is not identically zero: for \(a=0\), isolate a single support point; for \(a\ne0\), isolate a pair \(z,z+a\) and vary their relative complex phase (the two conjugate cross terms cannot vanish identically). The joint nonzero locus of these finitely many nonzero polynomials is open, dense, full measure, and intersects the region of nonzero support weights. All coefficients with unsupported translations vanish identically, so the Weyl diagonalization of Step 1 gives the generic rank \(N(N-K)\). This completes the theorem.

## Verification
The standalone file `check_quad_graph.py` uses integer-only Boolean Walsh--Hadamard transforms, checks every ambiguity coefficient for all \(1\le m\le6\), every permitted polar rank and two affine perturbations, and compares with the theorem's exact multiplicities. It independently constructs every Gabor projector and exactly diagonalizes its full Gram matrix for \((m,r)=(2,1),(3,1),(4,2)\). The output includes `BINARY_QUADRATIC_GRAPH_AMBIGUITY_CHECKS_OK` and `EXACT_PROJECTOR_GRAM_CHECKS_OK`. At \((m,r)=(4,2)\), the projector Gram eigenvalues are \(0\) with multiplicity \(707\), \(512\) with multiplicity \(256\), \(2048\) with multiplicity \(60\), and \(8192\) with multiplicity \(1\). These finite tests corroborate but do not substitute for the all-dimension proof.

## Relationship to prior work
Krahmer--Pfander--Rashkov develop uncertainty and Gabor theory on finite abelian groups, but their results concern support bounds, not the full quadratic-graph lifting spectrum. Bojarovska--Flinth establish general Weyl ambiguity criteria and frame bounds for full Gabor intensity lifting; the diagonalization in Step 1 is credited to that setting and is not claimed to be new. The present calculation supplies the previously unspecified complete **rank-stratified** ambiguity counts for graph indicators of *scalar binary quadratic forms*, including all degenerate polars, together with the exact generic-versus-flat rank contrast on the identical support. Other quadratic-graph Fourier studies and nonbinary quadratic-shell Gabor studies concern different transforms or support families; this is a bounded literature comparison, not proof of historical priority.

## Limitations
This result concerns complex-linear matrix recovery, not recovery restricted to positive semidefinite or rank-one matrices. No stability or noise-reconstruction theorem is supplied. All singular values use an unnormalized window; normalizing by \(\|g\|_2\) divides the singular values by \(M\). The supplied literature comparison cannot exclude an unlocated stronger historical theorem that already implies these particular multiplicities. Independent mathematical evaluation has not been performed.

## References
1. F. Krahmer, G. Pfander and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1 (November 16, 2006), https://arxiv.org/abs/math/0611493.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (March 19, 2015), https://arxiv.org/abs/1503.05800; especially Section 2.2, Theorem 2.3.
3. G. E. Pfander, *Gabor frames in finite dimensions*, author-distributed chapter, https://www.mathematik.uni-marburg.de/~pfander/pubs/FiniteGaborFramesChapter.pdf.
