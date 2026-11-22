# Even-normal cone-volume rigidity and the exceptional square

## Finding

Let \(N\ge4\) be even, put \(\theta=2\pi/N\), and let \(P_N\) be the regular \(N\)-gon centered at the origin whose side support numbers in the directions \(u_j=(\cos(j\theta),\sin(j\theta))\), \(0\le j<N\), are all one. Suppose that \(Q,R\) are full-dimensional convex polygons containing the origin in their interiors, each with these \(N\) outward facet normals, and that \(Q+R=P_N\). If for some \(c>0\) their respective cone-volume atoms obey

\[
 V_Q(\{u_j\})=c V_R(\{u_j\})\qquad(0\le j<N),
\]

then the following sharp dichotomy holds.

**Rigidity:** For every even \(N\ge6\), there is \(t\in(0,1)\) with \(Q=tP_N\) and \(R=(1-t)P_N\), without translations.

**Exception and its full classification:** When \(N=4\), every admissible pair consists of centered axis-aligned rectangles with support vectors, in cyclic order, \((s,t,s,t)\) and \((1-s,1-t,1-s,1-t)\), respectively, for uniquely determined \(s,t\in(0,1)\). Their cone-volume measures are proportional with factor

\[
 c=\frac{st}{(1-s)(1-t)}.
\]

The pair is homothetic to the square if and only if \(s=t\). Thus the square is the sole even regular polygon admitting non-homothetic proportional-cone-volume Minkowski summands of this type.

The key discrete theorem, proved independently below, states that for every even \(N\ge6\), the only positive \(N\)-periodic solution of

\[
 x_{j-1}+x_{j+1}=2\cos(2\pi/N)x_j+\frac{2-2\cos(2\pi/N)}{x_j}
\]

is \(x_j\equiv1\). For \(N=4\), the entire positive solution set is \((t,t^{-1},t,t^{-1})\), \(t>0\). The odd-period result for \(N\ge5\) is established in Monahan's Theorem 6.7; the even extension, its proof mechanism, and square classification are the contributions here.

## Assumptions and scope

Each polygon is strictly convex in the polygonal sense: all \(N\) prescribed facet lengths are positive and all support numbers relative to the common origin are positive. The origin is interior. The normal directions occur exactly once, in counterclockwise order; labels and normalization are fixed by \(P_N\). All cone-volume weights use \(V_K(\{u_j\})=h_K(u_j)\ell_j(K)/2\), where \(\ell_j(K)>0\) is the corresponding edge length. The Minkowski-sum condition is an equality of sets, not merely an area constraint. For \(N=4\), the result classifies all admissible pairs; for even \(N\ge6\), it asserts global uniqueness within this class. No assertion is made for arbitrary normals or arbitrary pairs without a fixed Minkowski sum.

## Proof

### 1. Reduction from cone-volume equality to a periodic recurrence

Set \(a=2\cos\theta\), \(\kappa=2-a>0\). Denote the support coordinates of \(R\) by \(r_j\), and those of \(Q\) by \(q_j=1-r_j\); the identity follows from \(Q+R=P_N\). All \(r_j,q_j\) lie strictly between zero and one. For any polygon with these equally spaced facet normals and supports \(z_j\), the elementary intersection-of-support-lines formula for the edge length is

\[
 \ell_j(z)=\frac{z_{j-1}+z_{j+1}-a z_j}{\sin\theta}.
\]

Introduce \(L_j(r)=r_{j-1}+r_{j+1}-a r_j\), so \(L_j(q)=\kappa-L_j(r)\). Positivity of each facet length and the equality of cone-volume weights give

\[
 (1-r_j)(\kappa-L_j(r))=c r_j L_j(r).
\]

Because the denominator is positive, this is equivalent to

\[
 r_{j-1}+r_{j+1}=a r_j+\kappa\frac{1-r_j}{1-r_j+c r_j}.
 \tag{1}
\]

If \(c=1\), set \(z_j=r_j-1/2\). Equation (1) becomes \(z_{j-1}+z_{j+1}=2(a-1)z_j\). When \(N\ge6\), \(0<\theta\le\pi/3\) and

\[
 \cos(2\theta)<2\cos\theta-1<\cos\theta.
\]

Every eigenvalue of the cyclic neighbor operator is \(2\cos(k\theta)\). The intervening value \(2(a-1)\) is not in its spectrum; hence \(z_j=0\) for all \(j\), and the pair is homothetic.

For \(c\ne1\), choose \(\lambda\in(0,1)\setminus\{1/2\}\) satisfying \(c=(1-\lambda)^2/\lambda^2\), and set

\[
 x_j=\frac{\lambda^2+(1-2\lambda)r_j}{\lambda(1-\lambda)}>0.
\]

Direct substitution into (1) yields

\[
 x_{j-1}+x_{j+1}=a x_j+\frac{\kappa}{x_j}. \tag{2}
\]

Since \(1-2\lambda\ne0\), rigidity of positive periodic solutions of (2) forces all \(r_j\) to be equal. We now prove that rigidity for **every even \(N\ge6\)**.

### 2. Three identities for a positive periodic solution

Let \(x_j>0\) satisfy (2). Summing the recurrence, multiplying by the first Fourier character, and multiplying by \(x_j\) and then summing, respectively, give

\[
 S:=\sum_j x_j=\sum_j\frac1{x_j},\qquad
 \sum_j\frac{e^{-ij\theta}}{x_j}=0,\qquad
 B(x):=2\sum_jx_jx_{j+1}-a\sum_jx_j^2=\kappa N. \tag{3}
\]

For the middle identity, the neighbor operator has eigenvalue \(a\) on the first Fourier character, so its projection kills that character on the left of the rearranged equation. These identities use periodicity only; no parity is assumed.

Write \(E_k(j)=e^{ikj\theta}\), \(\widehat{x}(k)=N^{-1}\sum_jx_je^{-ikj\theta}\), and \(\mu_k=2\cos(k\theta)-a\). Thus \(\mu_0=\kappa\), \(\mu_1=\mu_{N-1}=0\), and \(\mu_k<0\) for \(2\le k\le N-2\). The real Fourier decomposition is

\[
 x_j=m+p_j+h_j,\qquad m=S/N,\qquad
 p_j=\widehat{x}(1)E_1(j)+\widehat{x}(N-1)E_{N-1}(j),\qquad
 h_j=\sum_{k=2}^{N-2}\widehat{x}(k)E_k(j).
\]

Parseval's identity gives \(B(x)=\kappa Nm^2+B(h)\), where \(-B(h)=N\sum_{k=2}^{N-2}(-\mu_k)|\widehat{h}(k)|^2\).

### 3. Strict weighted Fourier inequality despite a sharp even-parity linear-program bound

Give \(\mathbb C^N\) the positive-definite Hermitian inner product

\[
 \langle v,w\rangle_x=\frac1S\sum_{j=0}^{N-1}\frac{v_j\overline{w_j}}{x_j}.
\]

By (3), every character \(E_k\) has norm one and every adjacent pair \(E_k,E_{k+1}\) is orthogonal. Let \(v\) have weighted norm one. For \(2\le k\le N-2\), put \(s_k=|\langle E_k,v\rangle_x|^2\), and put \(s_1=s_{N-1}=0\). Pairwise Bessel bounds imply \(s_k+s_{k+1}\le1\) for every \(1\le k\le N-2\).

Write \(\alpha=\pi/N\) and \(\delta_j=\cot(j\alpha)-\cot((j+1)\alpha)>0\). The exact trigonometric identity

\[
 \frac{\kappa}{-\mu_k}=\frac{\tan\alpha}{2}(\delta_{k-1}+\delta_k)
\]

therefore yields

\[
 T_x(v):=\kappa\sum_{k=2}^{N-2}\frac{s_k}{-\mu_k}
 =\frac{\tan\alpha}{2}\sum_{j=1}^{N-2}\delta_j(s_j+s_{j+1})\le1. \tag{4}
\]

**The even-parity point is strictness in (4) for actual Hilbert-space coefficients, although the relaxed linear program attains one.** Equality would force every \(s_j+s_{j+1}=1\). Since \(s_1=0\), this implies \(s_2=s_4=1\). For even \(N\ge6\), both characters \(E_2\) and \(E_4\) are present and distinct. Equality \(|\langle E_k,v\rangle_x|=1\) for two unit vectors forces \(v\) to be a scalar multiple of each, impossible: distinct Fourier characters are never proportional on the full positive-weight grid. Thus \(T_x(v)<1\) for every such \(v\).

If \(h\ne0\), apply weighted Cauchy–Schwarz to \(\langle h,h/\|h\|_x\rangle_x\), using the strict bound (4). It follows that

\[
 \frac1S\sum_j\frac{h_j^2}{x_j}
 <\frac1\kappa\sum_{k=2}^{N-2}(-\mu_k)|\widehat h(k)|^2,
 \quad\text{or}\quad
 -B(h)>\frac{\kappa N}{S}\sum_j\frac{h_j^2}{x_j}. \tag{5}
\]

When \(h=0\), equality holds in (5) with both sides zero. This strictness argument does not claim any uniform gap independent of \(x\); only pointwise strictness is needed.

### 4. The upper bound and equality case

Using (3), \(\sum p_j=0\), \(\sum p_j/x_j=0\), and \(m=S/N\), expand

\[
 \sum_j\frac{h_j^2}{x_j}=S+m^2S+\sum_j\frac{p_j^2}{x_j}-2mN.
\]

Combine this with (5) and \(B(x)=\kappa Nm^2+B(h)\):

\[
 B(x)\le\kappa N-\frac{\kappa N}{S}\sum_j\frac{p_j^2}{x_j}\le\kappa N,
\]

with equality in the first inequality only when \(h=0\). But (3) asserts \(B(x)=\kappa N\), so \(h=0\) and \(p=0\). Hence \(x\) is constant. Substituting into (2) forces \(x_j=1\). This proves the positive-periodic rigidity for each even \(N\ge6\), and by Section 1, the polygonal homothety statement.

### 5. Complete square exception

When \(N=4\), \(a=0\) and \(\kappa=2\). The positive recurrence is \(x_{j-1}+x_{j+1}=2/x_j\). The two even equations yield \(x_0=x_2\); the two odd equations yield \(x_1=x_3\), and either gives \(x_0x_1=1\). Thus all positive solutions are exactly \((t,t^{-1},t,t^{-1})\), \(t>0\).

For the geometric statement, every four-normal polygon is an axis-aligned rectangle (possibly translated). The opposite facets have identical lengths. Comparing proportional cone-volume weights at the two opposite normals gives \(q_0/(1-q_0)=q_2/(1-q_2)\), hence \(q_0=q_2\); likewise \(q_1=q_3\). Therefore every admissible \(Q\) and \(R\) is centered. Writing \(q=(s,t,s,t)\) gives \(r=(1-s,1-t,1-s,1-t)\), with \(0<s,t<1\). Each atom of \(V_Q\) equals \(st\) and each atom of \(V_R\) equals \((1-s)(1-t)\), verifying the claimed proportionality. The pair is homothetic precisely when \(s=t\).

## Verification

The accompanying standalone `check_recurrence.py` executes 2,488 finite checks: exact-rational four-period examples and proportional square atoms, trigonometric identity tests for even periods through 100, and direct numerical eigenvalue evaluations of weighted Fourier Bessel operators with strictly positive reciprocal weights whose first Fourier moment vanishes. The numerical operator norms are strictly below one in all sampled even periods at least six. A symbolic substitution into the geometric recurrence additionally reduces exactly to zero. These checks are independent sanity tests of the identities, not substitutes for the universal analytic proof above. Run with `python check_recurrence.py` (requires NumPy).

## Relationship to prior work

Cory Monahan, *A topological approach to the discrete dual Minkowski problem* (arXiv:2611.13375v1, first posted 2026-11-09), Section 6, establishes recurrence (2) as a reduction and proves the Fourier rigidity theorem for **odd** periods \(N\ge5\). In particular, its Lemma 6.8 uses parity to prove a strict bound for a relaxed linear program; that bound is exactly one for even periods. The present result uses the fact that the putative even-period equality pattern cannot occur as Bessel coefficients of a single vector, and so establishes rigidity for all even \(N\ge6\). The square is a sharp genuine exception. The source's odd-period result and general topological framework are credited and not newly claimed.

Baumbach, Chen, and Henk's *On the solution sets of the cone-volume map* (arXiv:2610.21533) studies fibers and generic multiplicities without the fixed regular Minkowski-sum condition used here. Baumbach's *On the discrete logarithmic Minkowski problem in the plane* (arXiv:2601.13159) concerns the convex hull of cone-volume images. These comparisons establish a distinct hypothesis and conclusion, not independent certification of historical priority.

## Limitations

The theorem requires exact equally spaced normals, positive facet lengths, a centered regular Minkowski sum, and componentwise proportional cone-volume weights. It is not a theorem of global injectivity of the cone-volume map, and makes no claim of general uniqueness for prescribed cone-volume vectors. Independent historical-priority checking and an independent mathematical audit remain outstanding. Relevant comparison preprints without accessible full text were evaluated only by their available abstracts and are a residual priority risk.

## References

1. Cory Monahan, *A topological approach to the discrete dual Minkowski problem*, arXiv:2611.13375v1 (2026-11-09), especially Section 6, Lemmas 6.2–6.9 and Theorem 6.7. https://arxiv.org/html/2611.13375v1
2. Tom Baumbach, Zhang Chen, and Martin Henk, *On the solution sets of the cone-volume map*, arXiv:2610.21533 (2026-10-15). https://arxiv.org/abs/2610.21533
3. Tom Baumbach, *On the discrete logarithmic Minkowski problem in the plane*, arXiv:2601.13159 (2026-01-19). https://arxiv.org/abs/2601.13159
