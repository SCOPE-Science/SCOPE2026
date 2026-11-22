# Exact incident-edge covariance and conditional degree variance in horizontal Voronoi visibility graphs

## Finding
Fix finitely many planar sampling sites, in general position, and assign them independent identically distributed heights having an arbitrary continuous cumulative distribution function. For every three distinct indices \(i,j,k\), consider the **horizontal Voronoi visibility** events \(E_{ij}\) and \(E_{ik}\). Define the crossed-cell sets \(A=C(i,j)\) and \(B=C(i,k)\), excluding the respective two endpoints. Put
\[
m=|A|,\quad n=|B|,\quad s=|A\cap B|,\quad h=m+n-s,
\qquad p_r=\frac{2}{(r+1)(r+2)}.
\]
The exact **joint visibility probability conditional on the sites** is
\[
q_{ijk}=\Pr(E_{ij}\cap E_{ik}\mid\text{sites})=
\begin{cases}
\dfrac{2}{(h+2)(h+3)}\left(\dfrac{1}{h+1}+\dfrac{1}{m+1}+\dfrac{1}{n+1}\right),&j\notin B,\ k\notin A,\\[7pt]
\dfrac{2}{(m+1)(h+1)(h+2)},&j\in B,\ k\notin A,\\[7pt]
\dfrac{2}{(n+1)(h+1)(h+2)},&j\notin B,\ k\in A,\\[7pt]
0,&j\in B,\ k\in A.
\end{cases}
\]
In particular, \(\operatorname{Cov}(\mathbf1_{E_{ij}},\mathbf1_{E_{ik}}\mid\text{sites})=q_{ijk}-p_m p_n\). With \(K_i\) the degree of site \(i\) in the horizontal Voronoi visibility graph and \(m_{ij}=|C(i,j)|\),
\[
\boxed{\operatorname{Var}(K_i\mid\text{sites})=
\sum_{j\ne i}p_{m_{ij}}(1-p_{m_{ij}})
+2\sum_{\substack{j<k\\j,k\ne i}}(q_{ijk}-p_{m_{ij}}p_{m_{ik}}).}
\]
These formulas are finite, exact, distribution-free, and computed solely from the crossed-cell incidence sets. The covariance can have either sign even for four distinct planar sites in general position.

## Assumptions and scope
Let \(N\ge3\) and fix distinct points \(P=(p_0,\ldots,p_{N-1})\) in \(\mathbb R^2\) with no three collinear and no four cocircular. The ordinary closed Euclidean Voronoi cell of index \(a\) is \(V_a=\{x:\|x-p_a\|\le\|x-p_b\|\text{ for every }b\}\). For distinct \(i,j\), the set \(C(i,j)\) contains exactly those \(a\ne i,j\) for which the segment \([p_i,p_j]\) meets \(V_a\) in an interval of **positive length**. The horizontal edge \(E_{ij}\) occurs precisely when \(Z_a<\min(Z_i,Z_j)\) for every \(a\in C(i,j)\). Heights \(Z_a\) are iid with one common continuous (atomless) distribution; sites are held fixed. No Poisson-site model, correlated heights, natural-visibility interpolation, or thermodynamic limit is assumed.

## Proof
A continuous common CDF transforms the iid heights into iid uniform random variables \(U_a\) on \((0,1)\); all inequalities are preserved almost surely, including when the CDF has flat intervals. For one edge with \(m\) blockers, both endpoint ranks must be the two largest among \(m+2\) independent continuous ranks, giving \(p_m=2/[(m+1)(m+2)]\), in agreement with the published pair law.

For two edges sharing the endpoint \(i\), write \(u=U_i\), \(v=U_j\), \(w=U_k\). First suppose neither target endpoint blocks the other edge: \(j\notin B\), \(k\notin A\). The \(s\) common blockers must all fall below \(\min(u,v,w)\), while the remaining \(m-s\) and \(n-s\) blockers must respectively fall below \(\min(u,v)\) and \(\min(u,w)\). Independence gives
\[
q_{ijk}=\int_{[0,1]^3}\min(u,v,w)^s
\min(u,v)^{m-s}\min(u,w)^{n-s}\,du\,dv\,dw.
\]
For fixed \(u\), partition the \((v,w)\)-square into the four regions \(v,w\ge u\), \(v<u\le w\), \(w<u\le v\), and \(v,w<u\). Integrating over \(v,w\) in that order produces
\[
u^h(1-u)^2
+u^{h+1}(1-u)\left(\frac1{m+1}+\frac1{n+1}\right)
+\frac{u^{h+2}}{h+2}\left(\frac1{m+1}+\frac1{n+1}\right).
\]
Integrating \(u\) from zero to one and using
\[
\int_0^1 u^h(1-u)^2\,du=\frac2{(h+1)(h+2)(h+3)},
\quad \int_0^1 u^{h+1}(1-u)\,du=\frac1{(h+2)(h+3)}
\]
gives the first branch of the stated formula.

Next suppose \(j\in B\) and \(k\notin A\). The edge \(E_{ik}\) requires \(v<\min(u,w)\). All \(m\) members of \(A\), including the \(s\) shared members, must then lie below \(v\); the other \(n-s-1\) members of \(B\) lie below \(\min(u,w)\). Integrate first over \(v\), then \(u,w\):
\[
q_{ijk}=\int_0^1\!\int_0^1\left(\int_0^{\min(u,w)}v^m\,dv\right)
\min(u,w)^{n-s-1}\,du\,dw
=\frac{1}{m+1}\int_0^1\!\int_0^1\min(u,w)^h\,du\,dw
=\frac{2}{(m+1)(h+1)(h+2)}.
\]
Here \(n-s-1\ge0\) follows from \(j\in B\setminus A\). Interchanging \(j,k\) proves the third branch. When both target endpoints belong to the other edge's blocker set, the simultaneous inequalities require \(U_j<U_k<U_j\), so their joint probability vanishes.

Finally, expand the square of \(K_i=\sum_{j\ne i}\mathbf1_{E_{ij}}\). Its diagonal terms yield \(p_{m_{ij}}(1-p_{m_{ij}})\), and each unordered pair yields twice its covariance. No independence of incident edges is assumed.

The sign reversal is geometrically realizable. In both following examples the root and targets have labels \(i=0,j=1,k=2\) and coordinates are in label order. For
\[
P_+=((-7,-9),(-8,4),(7,-4),(-4,-1)),
\]
exact Voronoi interval intersections give \(A=B=\{3\}\). Thus \(m=n=s=1\), \(q_{012}=1/4\), \(p_m=p_n=1/3\), and covariance \(5/36>0\). For
\[
P_-=((-8,-4),(2,1),(0,9),(0,-5)),
\]
those intersections give \(A=\{3\}\), \(B=\{1\}\). Thus \(m=n=1,s=0,j\in B\), \(q_{012}=1/12\), and covariance \(-1/36<0\). All triples in each configuration are noncollinear, and the four points are not cocircular, as also checked exactly.

## Verification
The independent-rank reasoning above proves the infinite class of finite configurations, with no extrapolation from tests. Run the attached standard-library Python program using `python checker.py`. Its exact `Fraction` computations enumerate every abstract admissible pair of blocker sets on up to seven named vertices and all rank permutations of the relevant sites; they agree with the four-branch joint law. Supplementary checks sample 16 generic finite site sets of each size from four through eight, verify Voronoi crossing symmetry and joint rank counts, and compare degree means and variances against exact enumeration for 12 sets of each size three through seven. Two integer-coordinate witnesses are checked using exact rational Voronoi line intervals, exact determinant general-position tests, and exact covariance fractions. Floating-point geometry in the random tests is supplementary; the displayed witnesses use rational arithmetic and the proof uses none.

## Relationship to prior work
Muñoz and Nuño, *Visibility graphs of irregularly sampled two-dimensional fields via Voronoi tessellations* (arXiv:2611.16336v1, posted 12 November 2026), defined HVG-V and proved the one-edge probability and conditional mean degree in Proposition 5, equations (7)–(9). The present result keeps precisely that graph and probabilistic model but supplies the full joint law for two incident edges, accounting for overlap and whether one target is a blocker of the other, and hence a conditional degree-variance formula; a pair marginal or mean alone does not determine this covariance. Luque et al. (2009) treat 1D horizontal visibility graphs of time series, while Lacasa and Iacovacci (2017) treat directions through regular lattices. Their settings can have special-case degree laws, but do not imply the four-branch arbitrary-site Voronoi incidence formula.

## Limitations
All assertions are conditional on a **fixed** site geometry and iid continuous heights. Averaging over random positions additionally requires the distribution of Voronoi crossed-cell patterns; no unconditional Poisson variance or asymptotic degree-variance scaling is proved. The fourth algebraic branch may be empty for some particular geometric site configurations; it remains a valid description of the mutually obstructing rank event. Finite computations verify instances but are not substituted for the analytic integration proof. Historical priority remains subject to discovery of obscure earlier overlapping-event formulas, and no independent mathematical audit has occurred.

## References
1. Francisco J. Muñoz and Juan Carlos Nuño, *Visibility graphs of irregularly sampled two-dimensional fields via Voronoi tessellations*, arXiv:2611.16336v1 (first publicly posted 2026-11-12), https://arxiv.org/abs/2611.16336, especially Definition 1, Proposition 5 and Section 6.
2. B. Luque, L. Lacasa, F. Ballesteros and J. Luque, *Horizontal visibility graphs: Exact results for random time series*, Physical Review E **80** (2009), 046103, https://doi.org/10.1103/PhysRevE.80.046103.
3. Lucas Lacasa and Jacopo Iacovacci, *Visibility graphs of random scalar fields and spatial data*, Physical Review E **96** (2017), 012318, https://arxiv.org/abs/1702.07813, https://doi.org/10.1103/PhysRevE.96.012318.
