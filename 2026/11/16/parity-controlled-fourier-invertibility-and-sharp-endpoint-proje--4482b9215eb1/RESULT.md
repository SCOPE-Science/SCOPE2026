# Parity-controlled Fourier invertibility and sharp endpoint projection constants for clique windmills

## Finding

Let \(r,n\ge1\) be integers. Form the clique windmill \(G_{r,n}=K_1\vee\bigl(\bigsqcup_{j=1}^n K_r\bigr)\), with one central vertex and \(n\) disjoint peripheral cliques of order \(r\). Let \(f_{r,n}\) be the indicator of all independent-set incidence vectors in the Boolean group \(H=(\mathbb F_2)^{rn+1}\). Define unnormalized convolution \(C_{r,n}g=f_{r,n}*g\), with \((f*g)(x)=\sum_{y\in H}f(y)g(x-y)\).

For central frequency \(a\in\mathbb F_2\) and peripheral frequencies \(u_j\in\mathbb F_2^r\), every unnormalized Fourier multiplier is
\[
W_{r,n}(a,u_1,\ldots,u_n)=(-1)^a+\prod_{j=1}^n\bigl(r+1-2|u_j|\bigr).
\]

**Odd peripheral clique size.** If \(r\) is odd, all multipliers are odd; \(C_{r,n}\) is invertible, its smallest multiplier magnitude is \(1\), and the only projection onto its range is the identity, of endpoint norm \(1\).

**Even peripheral clique size.** If \(r=2m\), \(m\ge1\), set \(T_m=\binom{2m+1}{m}\). Exactly \(T_m^n\) multipliers vanish, and
\[
\operatorname{rank}C_{2m,n}=2^{2mn+1}-T_m^n,\qquad
\min_{W_{2m,n}\ne0}|W_{2m,n}|=2.
\]
If \(E_{m,n}\) denotes the convolution range, then its minimum projection norm, among **every** real or complex linear projection \(\ell^p(H)\to E_{m,n}\), is the same for \(p=1\) and \(p=\infty\), and equals
\[
\boxed{\Lambda_{m,n}=1+\left(\frac{T_m}{2^m}\right)^n-\left(\frac{T_m}{2^{2m}}\right)^n.}
\]
The spectral projection attains this minimum. For all \(r,n\ge1\), \(\max_{\xi}|W_{r,n}(\xi)|=(r+1)^n+1\); thus the Moore--Penrose inverse \(\ell^2\)-norm is \(1\) when \(r\) is odd and \(1/2\) when \(r\) is even. The positive spectral condition numbers are respectively \((r+1)^n+1\) and \(((r+1)^n+1)/2\).

For fixed even \(r=2m\), the proportion of zero multipliers is \(\frac12(T_m/2^{2m})^n\to0\), although the sharp endpoint projection norm increases exponentially at base \(T_m/2^m>1\). For the friendship graph \(r=2\), the exact norm simplifies to \(1+(3/2)^n-(3/4)^n\). The parity contrast is between odd and even **peripheral clique order**, not parity of the number of cliques.

## Assumptions and scope

The vertex order is fixed: the centre first, followed by \(n\) blocks of \(r\) vertices. Frequencies and supports are elements of the same Boolean group; all Fourier transforms are unnormalized, while inverse transforms carry the factor \(2^{-(rn+1)}\). Norms on \(\ell^p(H)\) are with counting measure; the operator norm of an idempotent convolution is unchanged by scaling the base measure consistently. In the formula for the minimum projection norm, projections may be arbitrary (not necessarily translation-invariant), and the range is taken algebraically as a subspace of functions on \(H\). Only the spectral-support projection is asserted to attain the minimum, not to be unique among all minimum-norm projections.

## Proof

**1. Multipliers and spectral zero set.** An independent set either contains the centre alone or avoids the centre and chooses at most one vertex from each peripheral clique. A selected vertex in a block contributes a Walsh sign, so direct factorization gives the formula for \(W_{r,n}\). If \(r\) is odd, each factor \(r+1-2|u_j|\) is even, hence \(W_{r,n}\) is odd and never zero. A block frequency of weight \((r+1)/2\) gives a zero factor and \(W_{r,n}=\pm1\), showing sharpness of the minimum.

Now let \(r=2m\). Each factor is odd. The equality \(W_{r,n}=0\) forces the product of the factors to have magnitude one. Therefore for every block \(j\), \(|u_j|\in\{m,m+1\}\). The factor equals \(1\) at weight \(m\) and \(-1\) at weight \(m+1\); for every choice of peripheral frequencies in these two layers there is exactly one central frequency making \(W=0\). Their total number is \((\binom{2m}{m}+\binom{2m}{m+1})^n=T_m^n\), using Pascal's identity. All nonzero multipliers are even, and choosing peripheral weights \(m\) with central sign \(+1\) gives multiplier \(2\). The zero count and sharp spectral gap follow. The triangle inequality gives \(|W|\le(r+1)^n+1\), attained at zero frequency. Plancherel diagonalization proves the rank, inverse norms and condition numbers.

**2. Exact local Krawtchouk absolute sum.** Define the two central Hamming layers \(B_m=\{u\in\mathbb F_2^{2m}:|u|=m\text{ or }m+1\}\), with \(|B_m|=T_m\), and let
\[
A_m(x)=\sum_{u\in B_m}(-1)^{u\cdot x},\qquad
S_m=\sum_{x\in\mathbb F_2^{2m}}|A_m(x)|.
\]
We show the finite, non-asymptotic identity
\[
\boxed{S_m=2^m T_m.}
\]
By permutation symmetry \(A_m(x)\) depends only on \(j=|x|\). With \(d=2m+1\), the coefficient-generating identity
\[
A_m(j)=[t^{m+1}](1-t)^j(1+t)^{d-j}
\]
follows by adjoining a zero coordinate to the physical vector: the last frequency coordinate may be zero or one, so the two adjacent layers combine into the weight-\(m+1\) layer of a \((2m+1)\)-cube.

To derive the needed recurrence, put \(P_j(t)=(1-t)^j(1+t)^{d-j}\) and \(F_j=[t^{m+1}]P_j(t)\). Direct differentiation gives \((d-j)P_{j+1}(t)+jP_{j-1}(t)=dP_j(t)-2tP_j'(t)\); comparison of the coefficient of \(t^{m+1}\) yields
\[
(d-j)F_{j+1}=-F_j-jF_{j-1}\quad (1\le j<d),
\]
with \(F_0=T_m\) and \(F_1=-T_m/d\). Iterating in pairs gives \(F_{2h-1}=F_{2h}\) for \(1\le h\le m\) and, including \(h=0\) for \(F_0\),
\[
F_{2h}=(-1)^h T_m\frac{(2h-1)!!(2m+1-2h)!!}{(2m+1)!!}.
\]
Here \((-1)!!=1\). In particular, the signs alternate in pairs and no local coefficient vanishes. Combining the weights of positions \(2h-1\) and \(2h\) yields
\[
\begin{aligned}
S_m/T_m
&=1+\sum_{h=1}^m\left(\binom{2m}{2h-1}+\binom{2m}{2h}\right)
\frac{(2h-1)!!(2m+1-2h)!!}{(2m+1)!!}\\
&=\sum_{h=0}^m\binom{m}{h}=2^m.
\end{aligned}
\]
The penultimate equality uses Pascal's identity and the factorial formulas for odd double factorials. This proves the local absolute-sum identity.

**3. Spectral projection kernel and global optimality.** Write \(Z\subseteq\widehat H\) for the set of zero multipliers when \(r=2m\). For a block frequency \(u\in B_m\), define \(\varepsilon(u)=(-1)^{|u|-m}\), the sign of its corresponding nonzero factor. The central frequency in \(Z\) is the unique \(a\) with \((-1)^a=-\prod_j\varepsilon(u_j)\). Put
\[
B_m^{\mathrm{sign}}(x)=\sum_{u\in B_m}\varepsilon(u)(-1)^{u\cdot x}
=(-1)^m A_m(x+\mathbf1).
\]
In particular, the absolute sums of \(A_m\) and \(B_m^{\mathrm{sign}}\) both equal \(S_m\). Fourier inversion of \(1_Z\), at a physical coordinate \((z,x_1,\ldots,x_n)\) with central bit \(z\), gives the normalized kernel \(K_Z\) with
\[
K_Z(0,x_1,\ldots,x_n)=2^{-(2mn+1)}\prod_j A_m(x_j),
\]
\[
K_Z(1,x_1,\ldots,x_n)=-2^{-(2mn+1)}\prod_j B_m^{\mathrm{sign}}(x_j).
\]
At the all-zero physical vector \(K_Z(0,0,\ldots,0)=T_m^n/2^{2mn+1}<1\). The Fourier projection onto \(E_{m,n}\) has convolution kernel \(K_E=\delta_0-K_Z\). Its absolute row sum, and hence its exact \(\ell^1\) and \(\ell^\infty\) operator norms, is
\[
\begin{aligned}
\|K_E\|_1
&=1-\frac{T_m^n}{2^{2mn+1}}+\frac{S_m^n-T_m^n}{2^{2mn+1}}+\frac{S_m^n}{2^{2mn+1}}\\
&=1+\frac{S_m^n-T_m^n}{2^{2mn}}
=1+\left(\frac{T_m}{2^m}\right)^n-\left(\frac{T_m}{2^{2m}}\right)^n.
\end{aligned}
\]
For any linear projection \(Q\) onto the translation-invariant subspace \(E_{m,n}\), average all conjugates by the translation isometries of \(H\). The averaged operator is again a projection onto \(E_{m,n}\) with norm no larger than \(\|Q\|\), and it commutes with all translations. Fourier diagonalization makes it the unique translation-invariant projection onto \(E_{m,n}\), namely the projection calculated above. This proves unrestricted endpoint optimality for both \(p=1\) and \(p=\infty\), over either scalar field.

## Verification

The standalone file `verification_checker.py` uses exact integers and rational arithmetic. It independently constructs graph-independent-set indicators and transforms them by a Boolean fast Walsh transform; it checks the explicit character formula, all spectral zeros, minimum/maximum magnitudes, inverse-transform spectral-projection endpoint norm, and selected direct character sums. It also tests the central two-layer Krawtchouk absolute-sum identity through peripheral clique order \(30\) using a separate coefficient formula. On a completed run the checker prints `WINDMILL_FOURIER_PROJECTION_EXACT_PASS`, with a total of \(29{,}268\) exact coefficients checked across parameter pairs satisfying \(1+rn\le13\) and \(1\le r\le6,1\le n\le4\). These finite checks supplement, but do not replace, the all-parameter proof above.

## Relationship to prior work

The standard windmill and friendship graph constructions predate this result. Alikhani, Brown and Jahari study the **domination polynomial** of friendship graphs, and Jahari and Alikhani study domination polynomials of flower graphs obtained from cycles sharing a vertex. Neither graph domination count gives character-dependent independent-set coefficients, spectral nullity, or an endpoint projection constant. Zippin discusses the general translation-averaging approach to finite-group projections, which is therefore acknowledged as a known principle; the original calculation here is the signed spectral zero set and its exact Krawtchouk absolute sum for clique windmills. The graph invariant studied here is Fourier multiplier rank and Banach-space projection norm, not adjacency spectrum, independence-complex homology, or Hodge projection in graph edge spaces.

## Limitations

The theorem applies to the uniform clique windmill with one central vertex and identical peripheral clique sizes. It does not classify heterogeneous clique bouquets, higher-dimensional hub cliques, every nonzero Fourier-multiplier multiplicity, intermediate \(\ell^p\) projection norms, or uniqueness of optimal non-translation-invariant projections. A prior, more general signed-partition-function identity could imply part of this theorem; bounded literature comparisons cannot rule out every unpublished or inaccessible source. No independent mathematical audit has been performed.

## References

1. S. Alikhani, J. I. Brown and S. Jahari, *On the Domination Polynomials of Friendship Graphs*, arXiv:1401.2092 (first version 2014-01-08). https://arxiv.org/html/1401.2092v2
2. S. Jahari and S. Alikhani, *Domination Polynomial of Generalized Friendship and Generalized Book Graphs*, arXiv:1501.05856 (first version 2015-01-23). https://arxiv.org/abs/1501.05856
3. M. Zippin, *A variant of Rudin's inequality for translation invariant projections on group algebras and its generalization to finite dimensional Banach spaces*, Archiv der Mathematik 82 (2004), 61--67, doi:10.1007/s00013-003-0582-x.
4. J. Gilbert and Z. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Annales de l'Institut Fourier 60 (2010), 1317--1346, doi:10.5802/aif.2556 (context on finite-group Fourier operator norms; a different operator norm problem).
