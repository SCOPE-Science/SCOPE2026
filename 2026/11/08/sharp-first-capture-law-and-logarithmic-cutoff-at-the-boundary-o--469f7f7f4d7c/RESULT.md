# Sharp first-capture law and logarithmic cutoff at the boundary of a five-parameter affine circle map

## Finding
Let the five-parameter map of Gaivão, Laurent and Nogueira satisfy the strict admissibility conditions stated below. Its natural invariant core is \(J=[c,b)\). If \(\tau(x)=\min\{n\geq0:f^n(x)\in J\}\), the complete Lebesgue-distribution of \(\tau\) is an explicit sum of two truncated affine-geometric terms, valid for all three cases \(\lambda\mu<1\), \(\lambda\mu=1\), and \(\lambda\mu>1\). In particular, there is a **sharp finite uniform capture time**, even though the motivating paper establishes only pointwise eventual entry.

Set
\[
s=\lambda\mu,\quad A=\frac{a}{1-\lambda},\quad d=\mu(b-a)-c,
\qquad [z]_+=\max\{z,0\}.
\]
For every integer \(n\geq0\), writing \(L_n=\operatorname{Leb}\{x\in[0,1):\tau(x)>n\}\), one has
\[
L_n=\left[A-(A-c)\lambda^{-n}\right]_++R_n,
\]
where
\[
R_n=\begin{cases}
\left[1-r-(b-r)s^{-n}\right]_+,&s\ne1,\quad r=d/(s-1),\\
\left[1-b-nd\right]_+,&s=1.
\end{cases}
\]
Here \(r<b\) for \(s<1\), and \(r>1\) for \(s>1\). In particular \(\operatorname{Leb}\{\tau=0\}=b-c\), \(\operatorname{Leb}\{\tau=n\}=L_{n-1}-L_n\) for \(n\geq1\), and \(\mathbb E\tau=\sum_{n\geq0}L_n\) under the uniform probability on \([0,1)\).

The exact maximum first-capture time is \(N=\max(N_L,N_R)\), where
\[
N_L=\left\lceil\frac{\log(A/(A-c))}{\log(1/\lambda)}\right\rceil
\]
and
\[
N_R=\begin{cases}
\left\lceil\frac{\log((1-r)/(b-r))}{\log(1/s)}\right\rceil,&s<1,\\
\left\lceil\frac{1-b}{d}\right\rceil,&s=1,\\
\left\lceil\frac{\log((r-b)/(r-1))}{\log s}\right\rceil,&s>1.
\end{cases}
\]
The values at \(c=0\) or \(b=1\) are understood literally (the corresponding logarithmic ratio equals one), giving zero time for the absent exterior branch.

A sharp singular boundary is exhibited by
\[
\lambda=\tfrac34,\quad \mu=2,\quad b=\tfrac12,\quad c=0,\quad a=\tfrac14-\varepsilon,\qquad0<\varepsilon<\tfrac18.
\]
For this full admissible one-parameter subfamily,
\[
L_n=\left[(\tfrac12+4\varepsilon)(\tfrac23)^n-4\varepsilon\right]_+,
\quad
N_\varepsilon=\left\lceil\log_{3/2}\left(1+\frac{1}{8\varepsilon}\right)\right\rceil.
\]
Consequently \(N_\varepsilon=\log(1/\varepsilon)/\log(3/2)+O(1)\) as \(\varepsilon\downarrow0\), while
\[
\mathbb E\tau=(\tfrac32+12\varepsilon)(1-(\tfrac23)^{N_\varepsilon})-4\varepsilon N_\varepsilon\longrightarrow\tfrac32.
\]
At \(\varepsilon=0\), which is outside strict admissibility but retains a well-defined map of \([0,1)\), each point still enters \(J\) in finite time, while the uniform bound disappears: \(L_n=\tfrac12(\tfrac23)^n>0\) for all finite \(n\), and \(\mathbb E\tau=\tfrac32\). This is an exact distinction between worst-case and mean time to reach the invariant core.

## Assumptions and scope
The domain is \(I=[0,1)\), using the original convention for the discontinuity. Let \(\eta=(b-a)/\lambda\), and
\[
f(x)=\begin{cases}
\lambda x+a,&0\le x<\eta,\\
\lambda\mu(x-\eta)+c,&\eta\le x<1.
\end{cases}
\]
The full strict admissible parameter domain is
\[
0<\lambda<1,\quad\mu>0,\quad0\le c<b\le1,\quad
(\lambda\mu\le1\ \text{or}\ \mu(1-b)\le1-c),
\]
\[
b(1-\lambda)<a<b-\lambda c,\qquad
(1-\lambda)(c-\mu b)<(1-\mu)a.
\]
All claims concerning the exact uniform cutoff hold on this domain. The boundary example at \(\varepsilon=0\) is explicitly outside the strict domain; it is analyzed directly from its formula. The measure is normalized Lebesgue measure on \(I\), which has total length one.

## Proof
**Exterior branch separation.** The original parameter inequalities give \(c<\eta<b\), \(f(J)\subseteq J\), \(f(c)<b\), \(f(b^-)>c\), and strict left/right motion toward \(J\) from the respective complementary intervals (the corresponding facts are also shown in the source's Lemma 4.1). In particular, an orbit starting in \([0,c)\) remains on the left affine branch until its first entry into \(J\); a point starting in \([b,1)\) remains on the right branch until first entry. Neither branch can skip past \(J\) because \(f(c)<b\) and \(f(b^-) >c\).

**Left survivor interval.** The left affine extension has fixed point \(A=a/(1-\lambda)>b\) and \(n\)-th iterate \(A+\lambda^n(x-A)\). For \(x<c\), iterates increase and their first crossing of \(c\) is the first entrance into \(J\). Thus \(\tau(x)>n\) holds exactly when \(x<A-(A-c)\lambda^{-n}\). Intersecting with \([0,c)\) gives interval length \([A-(A-c)\lambda^{-n}]_+\).

**Right survivor interval.** Write the right affine extension as \(g(x)=sx-d\) with \(d=\mu(b-a)-c\). It strictly decreases on \([b,1)\) before entry and satisfies \(g(b)>c\). If \(s\ne1\), with fixed point \(r=d/(s-1)\), its \(n\)-th iterate is \(g^n(x)=r+s^n(x-r)\). The criterion \(g^n(x)\ge b\) is exactly \(x\ge r+(b-r)s^{-n}\). Since the orbit moves monotonically down until entry, this is equivalent to \(\tau(x)>n\); intersecting with \([b,1)\) has length \([1-r-(b-r)s^{-n}]_+\). For \(s=1\), \(g^n(x)=x-nd\), giving \([1-b-nd]_+\). The strict inequalities yield \(r<b\) for \(s<1\), \(d>0\) for \(s=1\), and \(r>1\) for \(s>1\).

**Exact uniform cutoff.** Each exterior interval's \(n\)-step survivor length is positive precisely for integers below the corresponding displayed \(N_L\) or \(N_R\). If a survivor interval has positive length at \(n=N_i-1\), it contains admissible starting points; at \(n=N_i\) its survivor set is empty. Therefore the supremum of the integer first-entry times is attained and is exactly \(N=\max(N_L,N_R)\), including the boundary cases of zero-length exterior intervals. The distribution and expectation follow from differences and the tail-sum identity; there are no other exterior states.

**Singular family.** Substituting the stated parameters gives \(s=3/2\), \(d=1/2+2\varepsilon\), \(r=1+4\varepsilon\), with no left exterior interval. This produces the exact geometric-minus-constant tail and cutoff shown above. Summing its positive terms for \(n=0,\dots,N_\varepsilon-1\) gives the expectation. As \(\varepsilon\downarrow0\), the cutoff grows logarithmically but \(\varepsilon N_\varepsilon\to0\) and \((2/3)^{N_\varepsilon}\to0\), so the expectation approaches \(3/2\). Directly at \(\varepsilon=0\), the right extension fixes the excluded endpoint \(x=1\), while every \(x<1\) drifts into \(J\); its tail is the stated untruncated geometric law.

## Verification
A standalone exact-rational script, `capture_checker.py`, tests five rational admissible parameter quintuples covering \(s<1\), \(s=1\), and \(s>1\), compares predicted tails against discrete-grid trajectories, and symbolically checks the singular family at six rational parameters and the endpoint. It completed with the message `PIECEWISE_AFFINE_CAPTURE_RATIONAL_CHECKS_OK 431`. These finite checks support, but do not replace, the proof for the continuum of real parameters.

## Relationship to prior work
Gaivão, Laurent and Nogueira introduced this five-parameter map and its natural invariant interval; their Lemma 4.1 establishes eventual entry for each initial point. Their main theorems compute the rotation number and describe the reduced dynamics. The present claim concerns the **full parameter-uniform first-entry distribution and sharp maximum delay**, together with a singular parameter boundary; it neither reproves nor strengthens the published rotation-number formulas. Laurent and Nogueira's earlier three-parameter work treats the dynamics of the normalized interval map, not this exterior-entry law.

## Limitations
The claim uses Lebesgue-distributed initial points on \([0,1)\), not a stationary invariant measure. The source's initial-value convention at the branch discontinuity is retained. The sharp cutoff is not asserted outside the strict admissible parameter domain. The endpoint result is restricted to the explicitly displayed one-parameter family. No statement about topological mixing, entropy, or Lyapunov exponents follows from the capture law. The novelty assessment compares accessible primary sources and relevant research records; unindexed equivalent work is a residual priority risk. Independent mathematical audit has not been performed.

## References
1. J. P. Gaivão, M. Laurent, A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, arXiv:2212.10944v1 (first public 2022-12-21), Sections 2–4, in particular Lemma 4.1. https://arxiv.org/html/2212.10944v1
2. J. P. Gaivão, M. Laurent, A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, *Aequationes Mathematicae*, published online 2024-04-22, doi:10.1007/s00010-024-01064-2. https://link.springer.com/article/10.1007/s00010-024-01064-2
3. M. Laurent, A. Nogueira, *Dynamics of 2-interval piecewise affine maps and Hecke-Mahler series*, arXiv:1907.08655v1 (2019-07-19). https://arxiv.org/html/1907.08655v1
