# Sharp generalized roundness of all three-column finite-field rank metrics

## Finding
For every prime power \(q\ge2\) and integer \(m\ge3\), the supremal negative-type exponent of the rank-distance metric on \(M_{m,3}(\mathbb F_q)\) is the **unique** root \(\alpha_{q,m}\in(0,1)\) of
\[
\Phi_{q,m}(a)=(t-h)-((q+1)t-qh)2^a+(qt-(q-1)h-1)3^a=0,
\qquad t=q^m,\quad h=q^2+q+1.
\]
For \(0<a<\alpha_{q,m}\) the metric has strict \(a\)-negative type; equality is allowed but is not strict at the endpoint; for \(a>\alpha_{q,m}\) it fails \(a\)-negative type.

The endpoint zero-sum kernel has dimension exactly
\[
h(t-1)(t-q),
\]
and is the span of precisely those additive characters indexed by rank-two matrices. The minimum Euclidean dimension for squared distance \(d^a\) is \(q^{3m}-1\) when \(0<a<\alpha_{q,m}\), and it decreases at the endpoint to
\[
q^{3m}-1-h(t-1)(t-q).
\]
For fixed \(q\), the exponent strictly decreases as the number \(m\) of rows increases, with asymptotic law
\[
\alpha_{q,m}\sim\frac{q^{-m}}{q\log(3/2)-\log2}\qquad(m\to\infty).
\]
This contrasts with the dimension-independent negative-type exponent in the diameter-two case: the three-column bilinear-forms graph is the first rank-metric family in which the threshold decays to zero with the row dimension.

## Assumptions and scope
Let \(\mathbb F_q\) be an arbitrary finite field, including nonprime fields. Let \(V=M_{m,3}(\mathbb F_q)\) as an additive abelian group, and let \(d(X,Y)=\operatorname{rank}_{\mathbb F_q}(X-Y)\). We use the convention \(0^a=0\) for \(a>0\). A metric has \(a\)-negative type if, for every finite family of real weights \(c_X\) summing to zero,
\[
\sum_{X,Y\in V}c_Xc_Yd(X,Y)^a\le0.
\]
The strict version replaces the inequality by strict negativity for any nonzero weight vector. The Euclidean statement concerns isometric embeddings of the snowflaked metric \(d^{a/2}\), since its squared distances are \(d^a\). Fourier transforms are unnormalized and use any nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\) and pairing \(\langle B,X\rangle=\sum_{i,j}B_{ij}X_{ij}\).

## Proof
**1. Rank-sphere Fourier multipliers.** For a character frequency \(B\in V\) of rank \(s\), let
\[
F_r(s)=\sum_{\operatorname{rank}X=r}\psi(\langle B,X\rangle),\qquad r=0,1,2,3.
\]
These integers depend only on \(s\) by left-right invertible changes of variables. For \(j=0,1,2,3\), sum the character over all matrices whose row space lies in a fixed \(j\)-dimensional subspace \(W\le\mathbb F_q^3\), then sum over \(W\). Orthogonality of additive characters yields
\[
H_j(s)=q^{mj}{3-s\brack j}_q.
\]
A matrix of rank \(r\) is counted \({3-r\brack j-r}_q\) times in this sum, so
\[
H_j(s)=\sum_{r=0}^j {3-r\brack j-r}_q F_r(s),
\quad F_0(s)=1.
\]
This is an exact, elementary derivation of the three-column rank-character table. Using \({3\brack1}_q={3\brack2}_q=h\) and \({2\brack1}_q=q+1\), triangular inversion gives, for \(s=1,2,3\),
\[
\begin{array}{c|ccc}
s &F_1(s)&F_2(s)&F_3(s)\\\hline
1 &(q+1)t-h&t^2-(q+1)^2t+qh&-t^2+q(q+1)t-(q-1)h-1\\
2 &t-h&-(q+1)t+qh&qt-(q-1)h-1\\
3 &-h&qh&-(q-1)h-1
\end{array}
\]
where \(t=q^m\).

**2. The rank-two frequency is the unique obstruction.** The eigenvalue of the powered distance matrix at a nontrivial frequency of rank \(s\) is
\[
D_s(a)=F_1(s)+2^aF_2(s)+3^aF_3(s).
\]
The table gives the identities
\[
D_2(a)-D_1(a)=t\left[q(2^a-1)+(t-q^2)(3^a-2^a)\right]>0,
\]
\[
D_2(a)-D_3(a)=t\left[1+q3^a-(q+1)2^a\right]>0
\]
for all \(a>0\), because \(t=q^m>q^2\). For the second inequality, let \(g(a)=1+2\cdot3^a-3\cdot2^a\). Then \(g(0)=0\) and \(g'(a)>0\) for \(a\ge0\), since \(2\log3>3\log2\) and \((3/2)^a\) is increasing. Thus \(1+q3^a-(q+1)2^a=g(a)+(q-2)(3^a-2^a)>0\).

Therefore every nontrivial Fourier eigenvalue is negative exactly when \(D_2(a)<0\), and they are all nonpositive exactly when \(D_2(a)\le0\). The function \(D_2(a)\) is precisely \(\Phi_{q,m}(a)\).

**3. Uniqueness and location of the critical root.** Write
\[
D_2(a)=(t-h)-b2^a+c3^a,\quad
b=(q+1)t-qh,\quad c=qt-(q-1)h-1.
\]
Both \(b,c\) are positive when \(t\ge q^3\), and
\[
\frac cb>\frac{q}{q+1}\ge\frac23>\frac{\log2}{\log3}.
\]
Indeed, \(c-\frac{q}{q+1}b=\frac{q^2}{q+1}>0\). Thus \(D_2'(a)=-b(\log2)2^a+c(\log3)3^a>0\) for all \(a\ge0\). Direct evaluation gives
\[
D_2(0)=-1,\qquad
D_2(1)=(q-1)(t-q^2+1)>0.
\]
There is one and only one root \(\alpha_{q,m}\) in \((0,1)\). The strict and non-strict negative-type assertions follow from Fourier diagonalization of the translation-invariant real symmetric distance kernel.

**4. Endpoint nullity and optimal Euclidean embedding dimension.** Exactly the rank-two Fourier characters have eigenvalue zero at \(a=\alpha_{q,m}\). The number of rank-two \(m\)-by-\(3\) matrices is
\[
{3\brack2}_q(q^m-1)(q^m-q)=h(t-1)(t-q).
\]
They are all nonconstant characters. The centered Gram matrix \(-\frac12 JD_aJ\), where \(J\) projects onto the real zero-sum subspace, has rank \(q^{3m}-1\) when \(0<a<\alpha_{q,m}\), and rank \(q^{3m}-1-h(t-1)(t-q)\) at equality. A Euclidean squared-distance realization has exactly that minimum dimension; in particular no finite-dimensional embedding of \(d^{a/2}\) exists when \(a>\alpha_{q,m}\).

**5. Dependence on dimension.** The identity
\[
D_2(a)=q^m\underbrace{\left[1+q3^a-(q+1)2^a\right]}_{>0\text{ for }a>0}
+\left[-h+qh2^a-(1+(q-1)h)3^a\right]
\]
shows that \(D_2(a)\) increases strictly with \(m\), at every fixed positive \(a\). Therefore its unique zero decreases strictly with \(m\). Expanding around \(a=0\) gives the asserted asymptotic, since \(q\log(3/2)-\log2>0\) for every \(q\ge2\).

## Verification
The standalone script `rank3_checker.py` recomputes the Fourier rank-sphere character sums, using the native prime fields and the nonprime field \(\mathbb F_4\). It executes a complete binary Walsh transform at \((q,m)=(2,3)\); direct exact character sums at \((2,4)\), \((3,3)\), and \((4,3)\) for representatives of each rank; and numerical sign/order checks of the exact algebraic formulas for fifteen choices of \((q,m)\). All tests passed. Example thresholds are \(\alpha_{2,3}\approx0.3486242003\), \(\alpha_{2,4}\approx0.2263420585\), and \(\alpha_{3,3}\approx0.0781273306\). Reproduce with `python rank3_checker.py`. The algebraic proof covers all prime powers and every \(m\ge3\); finite computations are not used to extrapolate that claim.

## Relationship to prior work
Delsarte's 1978 bilinear-forms association scheme already provides the full rank-sphere character table through generalized Krawtchouk polynomials. Gadouleau and Yan's rank-metric MacWilliams results (first publicly posted in January 2007 and in a fuller June 2007 version) give equivalent Fourier/rank enumerator machinery. Murugan's 2011 study explains how supremal negative type can be obtained by investigating the first zero of a finite vertex-transitive distance matrix. The present result does not claim those tools as new. Its specific conclusion is a sharp, dimension-dependent root law for **all diameter-three bilinear-forms graphs**, proved by showing rank-two characters dominate both other nontrivial Fourier strata; it also gives the exact endpoint embedding dimension. The inspected literature does not directly state this classification. General association-scheme machinery makes it conceivable that an equivalent specialization exists elsewhere; no unconditional priority claim is made.

## Limitations
The threshold is specified by a unique, explicitly specified scalar equation rather than an elementary closed form. The classification is restricted to matrices with exactly three columns and at least three rows; no conclusion is asserted for four or more columns or arbitrary modifications of the rank distance. The originality comparison is bounded, not an exhaustive historical proof. Mathematical validation has not been independently performed.

## References
1. P. Delsarte, *Bilinear forms over a finite field, with applications to coding theory*, Journal of Combinatorial Theory, Series A **25** (1978), 226–241, DOI: 10.1016/0097-3165(78)90015-8. Character algebra and Appendix, Theorem A2.
2. M. Gadouleau and Z. Yan, *MacWilliams Identity for the Rank Metric*, arXiv:cs/0701097v1 (posted 2007-01-16), https://arxiv.org/abs/cs/0701097.
3. M. Gadouleau and Z. Yan, *MacWilliams Identity for Codes with the Rank Metric*, arXiv:0706.1751v1 (posted 2007-06-12), https://arxiv.org/abs/0706.1751. See Section III-C and Corollary 1.
4. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1 (posted 2011-12-23), https://arxiv.org/abs/1112.5657. See Theorem 3.1.
