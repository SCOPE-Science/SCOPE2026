# Exact transport error of complete periodic-point censuses in generalized tent repellers

## Finding
For every real \(H\ge 2\) and every integer \(n\ge1\), let
\[
f_H(x)=H\min\{x,1-x\},\qquad
K_H=\{x\in[0,1]:f_H^j(x)\in[0,1]\text{ for every }j\ge0\}.
\]
Let \(\mu_H\) be the equal-weight Bernoulli measure on the two inverse branches of \(f_H|_{K_H}\), and let \(\nu_{H,n}\) be the uniform measure on all distinct real points fixed by \(f_H^n\). There are exactly \(2^n\) such points. For the Euclidean cost on \([0,1]\), their exact first Wasserstein distance is
\[
\boxed{W_1(\nu_{H,n},\mu_H)=
\frac{H-1}{(2H-1)H^n}\left(1+\frac{1}{2(H^{2n}-1)}\right).}
\]
The same census has exact Kolmogorov distance
\[
\boxed{\sup_{x\in\mathbb R}|\nu_{H,n}(( -\infty,x])-\mu_H(( -\infty,x])|=2^{-n}.}
\]
In particular, the leading transport coefficient \((H-1)/(2H-1)\) is strictly positive, and the **first correction** is of order \(H^{-3n}\), with no \(H^{-2n}\) term:
\[
W_1=\frac{H-1}{2H-1}H^{-n}
+\frac{H-1}{2(2H-1)}H^{-3n}+O_H(H^{-5n}).
\]
At \(H=3\) this is the classical middle-thirds Cantor measure and the count of *all* points fixed by the \(n\)-th iterate, **not** points from a single primitive periodic orbit.

## Assumptions and scope
The map is considered on the real line. If \(x<0\), then \(f_H(x)=Hx<x\) and the orbit cannot return; if \(x>1\), then \(f_H(x)<0\) and the next orbit is negative. Thus every real periodic point is in \([0,1]\), and necessarily in \(K_H\). Only points whose entire forward orbit remains in \([0,1]\) are included in \(K_H\). The map need not preserve all of \([0,1]\) when \(H>2\). Write \(r=H^{-1}\) and define the contracting inverse branches
\[
S_0(t)=rt,\qquad S_1(t)=1-rt.
\]
Their invariant compact set is precisely \(K_H\). They have disjoint open image intervals for \(H\ge2\), although the closed intervals touch at \(H=2\). The unique self-similar probability measure satisfies \(\mu_H=\tfrac12(S_0)_*\mu_H+\tfrac12(S_1)_*\mu_H\); it has no atoms and has mean \(1/2\). This is the maximal-entropy probability for the full binary repeller. For each binary word \(w=(w_1,\dots,w_n)\), write \(S_w=S_{w_1}\circ\cdots\circ S_{w_n}\) and let \(p_w\in S_w(K_H)\) be its unique fixed point. All these points are distinct and \(f_H^n(p_w)=p_w\). A point of lower prime period dividing \(n\) appears exactly once in \(\nu_{H,n}\). There is no restriction that its least period equal \(n\).

## Proof
**1. Optimal transport reduces to a one-point conditional cost.** Each cylinder \(S_w(K_H)\) has \(\mu_H\)-mass exactly \(2^{-n}\), contains exactly one point \(p_w\), and lies in an interval whose interior does not intersect any other same-length cylinder interval. As all these intervals are ordered along the line, the monotone optimal coupling transports exactly the mass within each cylinder to its own point \(p_w\). This remains valid when \(H=2\) because boundary points carry zero \(\mu_H\)-mass. Thus, if \(X\sim\mu_H\), and \(Y_n\) is independent and uniformly distributed over the \(p_w\), then using \(S_w(p_w)=p_w\) and the absolute contraction ratio \(r^n\),
\[
W_1(\mu_H,\nu_{H,n})
=2^{-n}\sum_{|w|=n}\int|S_w(x)-p_w|\,d\mu_H(x)
=r^n\,\mathbb E|X-Y_n|.
\tag{1}
\]
The same partition shows the CDF discrepancy is at most \(2^{-n}\), since before or after the unique atom inside a cylinder the discrepancy is bounded by that cylinder's total mass. The all-zero word gives \(p_w=0\), so at \(x=0\) the discrepancy is exactly \(2^{-n}\) because \(\mu_H\) is atomless.

**2. Exact barycenter of the periodic-point census.** Write \(S_w(t)=D_w+\varepsilon_w r^n t\) with \(\varepsilon_w=(-1)^{\#\{j:w_j=1\}}\). For a uniformly random length-\(n\) word, the first-letter averaging identity \(\tfrac12(S_0(t)+S_1(t))=\tfrac12\) gives \(\mathbb E D_w=1/2\) for all \(n\ge1\). Put \(b_n=\mathbb E(\varepsilon_wD_w)\). Directly \(b_1=-1/2\). Conditioning on the first letter and using \(\mathbb E\varepsilon_{w_2\cdots w_n}=0\) for \(n>1\) gives \(b_n=rb_{n-1}\). Hence \(b_n=-r^{n-1}/2\). Since
\[
p_w=\frac{D_w}{1-\varepsilon_w r^n}
=\frac{D_w(1+\varepsilon_w r^n)}{1-r^{2n}},
\]
the census mean is exactly
\[
m_n:=\mathbb E Y_n=
\frac{1-r^{2n-1}}{2(1-r^{2n})}.
\tag{2}
\]

**3. Exact absolute-deviation mean.** Define \(\Phi(t)=\int|x-t|\,d\mu_H(x)\) for \(t\in K_H\). By conditioning on the first inverse branch, and using \(\mathbb E X=1/2\),
\[
\Phi(t)=\frac{1}{2H}\Phi(f_H(t))
+\frac{H-1}{4H}+\frac12\left|t-\frac12\right|.
\tag{3}
\]
Indeed the same-branch integral scales by \(1/H\), while the cross-branch integral has constant sign. The map \(f_H\) permutes the \(2^n\) points fixed by its \(n\)-th iterate; consequently \(Y_n\) and \(f_H(Y_n)\) have the same distribution. Moreover \(f_H(t)=H(\tfrac12-|t-\tfrac12|)\), whence
\[
\mathbb E\left|Y_n-\frac12\right|=\frac12-\frac{m_n}{H}.
\]
Averaging (3) over \(Y_n\) now yields
\[
\mathbb E\Phi(Y_n)
=\frac12-\frac{m_n}{2H-1}
=\frac{H-1}{2H-1}\frac{2-r^{2n}}{2(1-r^{2n})}.
\tag{4}
\]
Substitute (4) into (1) and simplify \((2-r^{2n})/[2(1-r^{2n})]=1+[2(H^{2n}-1)]^{-1}\). This proves the transport identity with every boundary case included. Expanding its positive denominator establishes the stated asymptotic and the nonvanishing leading coefficient.

## Verification
The included standalone `checker.py` uses exact rational arithmetic for all five slopes \(H\in\{2,3,4,5/2,7/3\}\), each period \(1\le n\le8\): 40 slope-period cases covering 2,550 distinct fixed points. It recomputes the inverse-branch fixed points and the exact recursion for \(\Phi\), then checks (2) and the transport formula exactly. Twelve independent cylinder-midpoint transport approximations for depths \(11\) at three slopes and four periods agree with the claimed formula inside a rigorous \(H^{-11}/2\) error envelope. Run `python3 checker.py` from the extracted package; the code uses only Python's standard library. These finite checks corroborate, but do not replace, the all-real-parameter and all-positive-integer proof above.

For orientation, \(W_1=7/36\) at \(H=2,n=1\), and \(W_1=17/120\) at \(H=3,n=1\).

## Relationship to prior work
Ayers–Dmitrishin–Radunskaya–A. Stokolos–C. Stokolos [1] study periodic points of precisely this generalized tent map and, in Section 6, compare single-orbit periodic-point histograms with samples from the Cantor set at \(H=3\). They explicitly leave the analytic distribution of points **from one orbit** unresolved. The theorem here instead gives the exact metric discrepancy for the **complete fixed-point census**; it neither answers their individual-orbit sampling question nor claims novelty for the inverse-branch coding. Chen–Dong [2] give classical tent-map periodic-point formulas and examine barycenters of individual cycles. Chen–Shi–Xu [3] provide formulas for skew-tent periodic-point coordinates, not an identified exact Wasserstein law. Graf–Luschgy [4] study optimal quantization of the Cantor law, not the error of these dynamically prescribed codebooks. Known Wasserstein convergence and self-similar measure principles supply context, but do not by themselves yield the finite-\(n\) correction above.

## Limitations
The distance is Euclidean \(W_1\), not higher-order Wasserstein distance. The empirical law uses every point fixed by \(f_H^n\) with equal weight, including lower-period orbits; it is not the empirical law of an individual orbit or the law of only primitive period-\(n\) points. The result does not address nonuniform branch weights, asymmetric slopes, or finite-precision numerical orbit detection. A closely related skew-tent paper [3] was available only as a substantial publisher preview, not an inspected complete paper; an unindexed equivalent transport identity cannot be excluded. No independent mathematical audit has been conducted.

## References
[1] K. Ayers, D. Dmitrishin, A. Radunskaya, A. Stokolos, C. Stokolos, *Search for Invariant Sets of the Generalized Tent Map*, arXiv:2111.08904v1, first posted 2021-11-17, especially Section 6. https://arxiv.org/abs/2111.08904

[2] K.-C. Chen and X. Dong, *On the barycenter of the tent map*, Proceedings of the American Mathematical Society **138** (2010), 4009–4023, DOI:10.1090/S0002-9939-2010-10397-0. Lawful author-hosted preprint: https://www.math.nthu.edu.tw/~kchen/papers/ChenDongTentCenter.pdf

[3] K. Chen, Y.-G. Shi, B. Xu, *Periodic Points of Skew Tent Maps*, Journal of Dynamical and Control Systems **29** (2023), 443–454, DOI:10.1007/s10883-022-09594-1; publisher preview inspected, full text not obtained.

[4] S. Graf and H. Luschgy, *The Quantization of the Cantor Distribution*, Mathematische Nachrichten **183** (1997), 113–133, DOI:10.1002/mana.19971830108.

[5] K. Scheicher, V. F. Sirvent, P. Surer, *Dynamical properties of the tent map*, Journal of the London Mathematical Society **93** (2016), 319–340, DOI:10.1112/jlms/jdv071; metadata and abstract inspected.
