# Sharp Gini norm and equality geometry of two-terminal graph-harmonic extension

## Finding
For every finite connected, positively conductance-weighted undirected network with two fixed boundary vertices, its Dirichlet harmonic extension has an **exact, attained** complete-pair Gini seminorm. Write \(n\ge2\) for the vertex count and let \(h\) be the unique voltage with boundary values \(0\) and \(1\). If \(I\) is the set of the remaining \(n-2\) vertices, then
\[
\|H\|_{G\to G}=1+\frac{\sum_{\{u,v\}\subset I}|h_u-h_v|}{n-1}.
\]
Thus the operator is nonexpansive precisely when the harmonic voltage is constant on all interior vertices. Every finite network satisfies the **sharp all-network bound**
\[
1\le\|H\|_{G\to G}\le\frac{\lfloor n^2/4\rfloor}{n-1}.
\]
The upper bound is attained in every size. For a unit-conductance path whose endpoints are prescribed, the exact value is \(n(n+1)/(6(n-1))\), which is greater than one precisely when \(n\ge4\) and is asymptotic to \(n/6\).

## Assumptions and scope
Let \(V\) have \(n\ge2\) vertices. The undirected network is connected, its existing edges have conductances \(c_{uv}=c_{vu}>0\), and missing edges have conductance zero. Pick distinct vertices \(a,b\). For real input \(f\in\mathbb R^V\), define \(Hf\) by \((Hf)(a)=f(a)\), \((Hf)(b)=f(b)\), and
\[
\sum_{v\in V}c_{uv}\big((Hf)(u)-(Hf)(v)\big)=0\qquad(u\in I:=V\setminus\{a,b\}).
\]
The connected Dirichlet problem is uniquely solvable. Put \(G(x)=\sum_{\{u,v\}\subset V}|x_u-x_v|\) and \(\|H\|_{G\to G}=\sup_{G(x)>0}G(Hx)/G(x)\). The empty sum is zero. All assertions concern these **unweighted all-pairs** differences, rather than conductance-weighted edge variations.

## Proof
**Reduction to the unique voltage.** Let \(h=H\mathbf 1_{\{b\}}\). The maximum principle gives \(0\le h_i\le1\), including \(h_a=0\), \(h_b=1\). By linearity and uniqueness, for every input
\[
(Hf)_i=f_a+(f_b-f_a)h_i,
\qquad G(Hf)=|f_b-f_a|G(h).
\]
For each interior vertex, the triangle inequality gives \(|f_i-f_a|+|f_i-f_b|\ge|f_b-f_a|\). Therefore
\[
G(f)\ge(n-1)|f_b-f_a|+\sum_{\{u,v\}\subset I}|f_u-f_v|\ge(n-1)|f_b-f_a|.
\]
Both inequalities are equalities for any nonconstant input with interior coordinates all equal to one common number between its two distinct boundary values. Conversely, when the boundary contrast is nonzero, equality requires precisely this condition (for at most one interior vertex, the interior-constancy condition is vacuous). Consequently \(\|H\|_{G\to G}=G(h)/(n-1)\). Since \(h_a=0\), \(h_b=1\), and all interior potentials lie in \([0,1]\), their boundary-to-interior contributions sum to \(n-2\), and the boundary pair contributes one. Hence \(G(h)=n-1+G_I(h)\), proving the exact norm and all nonconstant input equality cases.

**Nonexpansivity and a local conductance test.** Since \(G_I(h)\ge0\), the norm is one precisely when all interior voltages are a common \(\theta\in[0,1]\), with the convention that no interior vertices makes this condition vacuous. Substituting this constant into the interior harmonic equations cancels all interior-to-interior terms, leaving exactly
\[
\theta c_{ia}=(1-\theta)c_{ib}\qquad(i\in I).
\]
Conversely, if some \(\theta\in[0,1]\) satisfies all these equations, the corresponding constant-interior extension solves the Dirichlet equations and so equals \(h\). This is a complete necessary-and-sufficient network classification, including missing boundary edges and \(\theta=0,1\).

**Sharp envelope and all maximal potentials.** Put \(m=n-2\). For \(m\ge2\), sort the interior voltages as \(0\le v_1\le\cdots\le v_m\le1\). An exact adjacent-gap identity is
\[
G_I(h)=\sum_{k=1}^{m-1}k(m-k)(v_{k+1}-v_k)
\le\big\lfloor m^2/4\big\rfloor(v_m-v_1)
\le\big\lfloor m^2/4\big\rfloor.
\]
Equality holds exactly when \(v_1=0\), \(v_m=1\), and every strictly positive gap \(v_{k+1}-v_k\) occurs at an index maximizing \(k(m-k)\). For even \(m\), this means half of the interior voltages are zero and half one; for odd \(m\), there are \((m-1)/2\) zeros and \((m-1)/2\) ones, with one remaining voltage arbitrary in \([0,1]\). When \(m\le1\), the upper and lower bounds both equal one, without these gap restrictions. The identity \(n-1+\lfloor(n-2)^2/4\rfloor=\lfloor n^2/4\rfloor\) gives the claimed global sharp bound. It is achieved by a graph containing the boundary edge and attaching \(\lfloor m/2\rfloor\) interior leaves only to \(a\) and all other interior leaves only to \(b\); the interior voltages are then zero or one. For the odd case, an additional interior vertex joined to both boundaries realizes any desired intermediate voltage by choosing its two positive conductances.

**Path formula.** On the unit-conductance path of \(n\) vertices, with the two endpoints as the prescribed boundary, the voltage is \(h_j=j/(n-1)\) for \(0\le j<n\). Therefore
\[
G(h)=\frac{1}{n-1}\sum_{0\le i<j<n}(j-i)=\frac{n(n+1)}6,
\qquad\|H\|_{G\to G}=\frac{n(n+1)}{6(n-1)}.
\]
This equals one at \(n=2,3\), exceeds one for every \(n\ge4\) (at \(n=4\) it is \(10/9\)), and grows like \(n/6\). This completes the proof.

## Verification
A standalone exact-rational Python checker, `check_harmonic_gini.py`, independently solves the finite Dirichlet linear systems and evaluates every nonconstant binary cut for all \(771\) connected simple graphs of size two through five. It also verifies \(390\) randomly generated connected positive integer-conductance networks, explicit extremal networks through size \(29\), unit paths through size \(49\), and the sorted-gap equality condition on the tested networks. These finite calculations corroborate the proof; the proof does not extrapolate from the tests. Run with `python3 check_harmonic_gini.py` from the extracted files.

## Relationship to prior work
Classical electrical-potential and hitting-probability correspondences give the harmonic voltage \(h\), but do not by themselves identify its operator norm in complete-pair Gini variation. Lin and Xi (2009) study local Lipschitz regularity of graph-harmonic functions, and give examples of failure of global Lipschitz regularity; that seminorm and setting differ from the finite all-pairs one here. Palacios, Gómez and Del Río (2014) analyze graph-walk hitting times by electrical voltages, rather than sharp Gini sensitivity of the two-terminal extension. The present theorem is consistent with the known universal comparison between oscillation and Gini seminorms: the oscillation norm of this extension equals one, but the comparison alone does not specify the exact voltage-dependent Gini norm or its equality/network criteria.

## Limitations
The theorem assumes a **two-point Dirichlet boundary**, a connected finite undirected positive-conductance graph, real vertex signals and complete-pair **unweighted** Gini variation. It does not give the sharp corresponding result for three or more boundary vertices, for conductance-weighted edge variation, or for nonlinear \(p\)-harmonic interpolation. The literature comparison is not a historical uniqueness certificate; equivalent formulations outside the inspected material may exist.

## References
1. Yong Lin and Lifeng Xi, *Lipschitz property of harmonic function on graphs*, Journal of Mathematical Analysis and Applications 366 (2010), 673–678, first available online 30 December 2009. DOI: 10.1016/j.jmaa.2009.12.037. https://archive.ymsc.tsinghua.edu.cn/pacm_download/671/12551-yonglin9.pdf
2. José Luis Palacios, Eduardo Gómez and Miguel Del Río, *Hitting Times of Walks on Graphs through Voltages*, Journal of Probability (2014), Article 852481, first published 20 May 2014. DOI: 10.1155/2014/852481. https://onlinelibrary.wiley.com/doi/10.1155/2014/852481
