# Dual negative-type thresholds for projective-plane incidence and nonincidence metrics

## Finding

Let \(\Pi\) be **any finite projective plane** of order \(q\ge2\), not necessarily Desarguesian, with \(v=q^2+q+1\) points and \(v\) lines. Its *incidence graph* \(G_q^+\) joins incident points and lines; its *nonincidence graph* \(G_q^-\) joins nonincident points and lines. Both have the ordinary shortest-path metric \(d\), and both have diameter three. Define the supremal negative-type exponent
\[
\beta(G)=\sup\{p\ge0:\ \sum_{x,y}c_xc_y d(x,y)^p\le0\text{ whenever }\sum_x c_x=0\}.
\]
Here \(d(x,x)^0=0\), whereas \(d(x,y)^0=1\) for distinct points. Let \(\sigma_q\in(0,1)\) be the unique solution of
\[
\sqrt q\,(3^{\sigma_q}-1)=2^{\sigma_q}.
\]
For \(q\ge3\), let \(\gamma_q\in(0,1/q)\) be the unique solution of
\[
q(q+1)2^{\gamma_q}=q^2+(q+1)3^{\gamma_q}.
\]
Then the complete sharp classification is
\[
\boxed{\beta(G_q^+)=\sigma_q,\qquad
\beta(G_q^-)=\begin{cases}\sigma_2,&q=2,\\\gamma_q,&q\ge3.\end{cases}}
\]
For each graph, the powered distance has conditional negative type **exactly** for \(0\le p\le\beta(G)\), and strict conditional negative type for \(0\le p<\beta(G)\). At the endpoint the nullity on the zero-sum subspace is \(v-1\) for \(G_q^+\) and for \(G_2^-\), but is **one** for \(G_q^-\), \(q\ge3\). Accordingly, the minimum Hilbert dimension for representing the endpoint powered metric as squared Euclidean distance is \(v\) in the first cases and \(2v-2\) in the last case. For every fixed \(t>0\), the Gaussian-type kernel \(\exp[-t d(x,y)^p]\) is positive semidefinite for all \(t>0\) exactly when \(p\le\beta(G)\), by Schoenberg's criterion; for such \(p\) it is in fact strictly positive definite for \(t>0\) because the metric has distinct points.

The two exponents have different asymptotic scales:
\[
\sigma_q=\frac{1}{\sqrt q\log3}+O(q^{-1}),\qquad
\gamma_q=\frac{1}{q^2\log2}+O(q^{-3})\quad(q\to\infty).
\]
Thus changing edges from incidence to nonincidence changes the sharp exponent by a factor of order \(q^{3/2}\), and the controlling nullspace changes from a \((v-1)\)-dimensional incidence singular-vector sector to a single part-contrast vector at every order \(q\ge3\).

## Assumptions and scope

A projective plane of order \(q\) has \(v=q^2+q+1\) points and as many lines, each line contains \(q+1\) points, and any two distinct points lie on exactly one line. A non-Desarguesian projective plane is allowed wherever it exists. No transitivity or coordinate field is assumed. In the nonincidence graph, the degree is \(q^2\) and two distinct points have exactly \(q(q-1)\) common neighboring lines. These properties guarantee shortest-path distances 1 and 3 across the bipartition and distance 2 within each part for distinct vertices. Both graphs have \(2v\) vertices.

## Proof

**1. Exact spectrum of the conditionally centered distance.** Let \(B\) be the point-line incidence matrix of a symmetric \(2\text{-}(v,k,\lambda)\) design, with \(1<k<v-1\); the two projective-plane examples have \((k,\lambda)=(q+1,1)\) and \((k,\lambda)=(q^2,q^2-q)\), respectively. Its incidence graph has the asserted diameter-three distance pattern. For \(p\ge0\), put \(a=2^p\), \(c=3^p\). The powered-distance matrix is
\[
D_p=\begin{pmatrix}a(J-I)&B+c(J-B)\\B^\top+c(J-B^\top)&a(J-I)\end{pmatrix}.
\]
The incidence identity \(BB^\top=(k-\lambda)I+\lambda J\) implies that the restriction of \(B\) between the two zero-mean parts has singular values \(\sqrt{k-\lambda}\), all with multiplicity \(v-1\). Decomposing the total zero-sum space into \(\{(x,y):\sum x=\sum y=0\}\) and the span of \((\mathbf1,-\mathbf1)\), the restricted quadratic form of \(D_p\) has eigenvalues
\[
-2^p\pm(3^p-1)\sqrt{k-\lambda}\quad\text{(each multiplicity }v-1\text{)},
\]
and
\[
F_{v,k}(p)=(v-1)2^p-k-(v-k)3^p\quad\text{(multiplicity one)}.
\]
Therefore conditional negative type is **equivalent to both**
\[
(3^p-1)\sqrt{k-\lambda}\le2^p,\qquad F_{v,k}(p)\le0.
\]
No other spectral sectors occur. Since \((3^p-1)/2^p\) is strictly increasing from zero to infinity on \([0,\infty)\), the first inequality has a single upper endpoint.

**2. Incidence graphs.** Here \(k=q+1\), \(k-\lambda=q\), and
\[
F_+(p)=q(q+1)2^p-(q+1)-q^2 3^p.
\]
At zero this equals \(-1\). The derivative is negative for every \(p\ge0\), because \(q\log3>(q+1)\log2\) for \(q\ge2\) (at \(q=2\) this is \(\log(9/8)>0\), and the left-side advantage increases with \(q\)), and the extra \((3/2)^p\) factor only strengthens the inequality. Thus \(F_+(p)<0\) for all \(p\ge0\), and only the singular-vector sector can obstruct negative type. Its unique zero is \(\sigma_q\), giving the first claimed exponent and endpoint nullity \(v-1\).

**3. Nonincidence graph when \(q=2\).** The complementary design has \((v,k,\lambda)=(7,4,2)\), so its singular-sector threshold is still \(\sigma_2\), while
\[
F_-(p)=6\cdot2^p-4-3\cdot3^p.
\]
The elementary strict inequality \(3^{3/4}>9/4>1+2^{1/4}\) proves \(\sigma_2<3/4\). At the singular threshold, \(3^{\sigma_2}=1+2^{\sigma_2}/\sqrt2\); hence
\[
F_-(\sigma_2)=(6-3/\sqrt2)2^{\sigma_2}-7
<4(7/4)-7=0,
\]
using \(2^{3/4}<7/4\). Thus conditional negative type holds at \(\sigma_2\). The interval property of negative type yields it for every smaller exponent, and the singular-sector eigenvalue rules it out for all larger ones. Again the endpoint nullity is \(v-1\).

**4. Nonincidence graph when \(q\ge3\).** The complementary design has \((k,\lambda)=(q^2,q^2-q)\), and
\[
F_-(p)=q(q+1)2^p-q^2-(q+1)3^p.
\]
Now \(F_-(0)=-1\), while
\[
F_-(1/q)=(q+1)\{q(2^{1/q}-1)-(3^{1/q}-1)\}-1>0.
\]
Indeed, \(q(2^{1/q}-1)>\log2>693/1000\) and \(3^{1/q}-1\le3^{1/3}-1<443/1000\); the bounds give \(F_-(1/q)> (q+1)/4-1\ge0\), with strictness throughout. The logarithmic bound follows, for example, from the first three positive terms of \(\log2=2\sum_{j\ge0}[(2j+1)3^{2j+1}]^{-1}\), and \((1443/1000)^3>3\). Moreover,
\[
F_-'(p)=(q+1)2^p\bigl(q\log2-\log3\,(3/2)^p\bigr)>0
\]
for \(0\le p\le1/q\), since \(q\log2\ge3\log2>2\) and \(\log3\,(3/2)^{1/3}<1.3\). Hence \(F_-\) has precisely one root \(\gamma_q\in(0,1/q)\).

The singular threshold \(\sigma_q\) is strictly larger than \(1/q\): for \(q\ge3\),
\[
\sqrt q(3^{1/q}-1)\le\frac{\log3\,3^{1/3}}{\sqrt q}
\le\frac{\log3\,3^{1/3}}{\sqrt3}<1<2^{1/q}.
\]
Therefore the constant contrast eigenvalue crosses zero strictly before the singular-sector eigenvalue. Both inequalities hold for \(0\le p\le\gamma_q\), and the constant contrast rules out all larger exponents (or use the negative-type interval property). Its zero is simple and all other zero-sum eigenvalues remain strictly negative, so the endpoint nullity is one.

**5. Embedding rank and asymptotics.** For a conditionally negative squared-distance matrix \(D_p\), the centered Gram matrix \(-\tfrac12 HD_pH\), with \(H=I-J/(2v)\), has rank \((2v-1)\) minus the zero-sum nullity. This yields the claimed minimal Hilbert embedding dimensions. The equation \(3^{\sigma_q}-1=q^{-1/2}2^{\sigma_q}\) gives the first expansion by Taylor expansion at zero. Taylor expansion of \(F_-(\gamma_q)=0\), with its derivative at zero \((q+1)(q\log2-\log3)\), and the bound \(\gamma_q<1/q\), first gives \(\gamma_q=O(q^{-2})\): indeed \(F_-(2/(q^2\log2))>0\) for all sufficiently large \(q\), while \(F_-(0)=-1\). Substituting this stronger bound into the Taylor expansion gives \(\gamma_q=(q^2\log2)^{-1}+O(q^{-3})\). These estimates are uniform along any sequence of orders for which projective planes exist.

## Verification

The accompanying `checker.py` independently constructs \(\operatorname{PG}(2,q)\) for the prime orders \(q=2,3,5,7\), verifies incidence identities exactly, diagonalizes the full centered matrices for both graph types, and checks their spectra against the proved formula. It passes 40 finite numerical spectral comparisons with thresholds and sign checks. These finite computations do **not** prove the arbitrary-plane or asymptotic assertions, which follow from the displayed identities and inequalities. Reproduction: `python checker.py` with NumPy installed.

## Relationship to prior work

Sánchez (2011, arXiv:1108.0451) established general finite-metric methods for supremal negative type and evaluated complete bipartite graph metrics, which have only two positive distance levels. The present incidence and nonincidence graphs have three positive distance levels and a nontrivial incidence singular spectrum, and the projective/complementary sharp thresholds and endpoint multiplicity transition do not follow as stated from the complete-bipartite formula. Haemers–Kharaghani–Meulenberg (open preprint, *Divisible Design Graphs*) developed algebraic spectra for design-derived graphs but did not in its inspected spectral and construction sections classify the powered path-metric kernels. De Winter–Lazebnik–Verstraëte (2008) investigated the geometry and cycles of projective-plane incidence graphs rather than powered metric negative type. Earlier general distance-matrix methods can in principle imply algorithmic recoverability of these exponents; an explicit equivalent specialization elsewhere cannot be ruled out.

## Limitations

Novelty has been checked against relevant indexed records and accessible primary literature, but an unlocated exact formula or association-scheme specialization may exist. The theorem requires a genuine projective plane of order \(q\); it makes no existence assertion for hypothetical orders. Numerical validation covers four prime orders, while the proof covers every existing plane, including non-Desarguesian examples. Independent mathematical validation has not been performed.

## References

- Sánchez, I. D., *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first posted 2011-08-02. https://arxiv.org/html/1108.0451v1
- De Winter, S., Lazebnik, F., and Verstraëte, J., *An Extremal Characterization of Projective Planes*, Electronic Journal of Combinatorics 15 (2008), R143, published 2008-11-30, DOI:10.37236/867. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v15i1r143
- Haemers, W. H., Kharaghani, H., and Meulenberg, M. A., *Divisible Design Graphs*, open preprint. https://www.cs.uleth.ca/~hadi/research/ddg-v4.pdf
