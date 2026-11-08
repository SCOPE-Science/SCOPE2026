# False-twin rigidity of polarization under a new social tie

## Finding

Let \(G\) be any finite simple undirected graph on \(n\ge2\) agents. Give each agent an innate opinion \(s_i\in[0,1]\). In the unit-weight Friedkin–Johnsen equilibrium, write
\[
 z_G=(I+L_G)^{-1}s,\qquad
 P_G(s)=\sum_{i=1}^n(z_{G,i}-\bar z_G)^2.
\]
Here \(L_G\) is the combinatorial graph Laplacian and \(\bar z_G=n^{-1}\sum_i z_{G,i}\). For a missing edge \(uv\), the following are equivalent:

1. \(P_{G+uv}(s)\le P_G(s)\) for **every** \(s\in[0,1]^n\).
2. \(u\) and \(v\) have exactly the same open neighborhood in \(G\), i.e. they are **false twins**: \(N_G(u)=N_G(v)\).

If these neighborhoods differ, there are admissible innate-opinion vectors yielding a **strict increase** and others yielding a **strict decrease** in polarization after adding the same edge. Consequently, every possible missing-edge addition is polarization-nonincreasing for every innate-opinion vector **if and only if** \(G\) is complete multipartite, including complete graphs. Among connected graphs, the smallest graph admitting an increase from adding one missing edge has four vertices; no connected graph of order at most three admits one.

An exact four-agent witness uses existing edges \(\{01,03,12\}\), adds edge \(02\), and takes \(s=(0,0,1/2,1)^\mathsf T\). It satisfies
\[
 P_G(s)=\frac{83}{784},\qquad P_{G+02}(s)=\frac{349}{3200},\qquad
 P_{G+02}(s)-P_G(s)=\frac{501}{156800}>0.
\]

## Assumptions and scope

All graphs are finite, simple, unweighted and undirected; connectivity is **not** assumed for the main equivalence. Only a **previously missing** edge is added with unit weight. Innate opinions are fixed during the intervention, all agents have one unit of self-weight, and expressed opinions are evaluated at the unique equilibrium \((I+L_G)^{-1}s\). The polarization is the sum of squared centered opinions rather than its average; multiplying by \(1/n\) preserves every comparison. This theorem concerns an isolated edge insertion, not simultaneous link rewiring, endogenous opinion changes, nonlinear influence, heterogeneous self-weights, or empirical behavior.

## Proof

**Exact difference formula.** Write \(L=L_G\), \(A=(I+L)^{-1}\), \(b=e_u-e_v\), \(v=Ab\), \(w=A^2b\), and \(\alpha=(1+b^\mathsf TAb)^{-1}>0\). By the Sherman–Morrison identity,
\[
 (I+L+bb^\mathsf T)^{-1}=A-\alpha vv^\mathsf T.
\]
As \(A\mathbf1=\mathbf1\) and \(v^\mathsf T\mathbf1=0\), the opinion mean is invariant and the vector changed by the edge has zero mean. Expanding the two squared norms therefore yields, for every \(s\in\mathbb R^n\),
\[
 \Delta_G(s;uv):=P_{G+uv}(s)-P_G(s)
 =\alpha^2\lVert v\rVert^2(v^\mathsf Ts)^2-2\alpha(v^\mathsf Ts)(w^\mathsf Ts).\tag{1}
\]
In particular, \(\Delta_G(s+c\mathbf1;uv)=\Delta_G(s;uv)\) and \(\Delta_G(cs;uv)=c^2\Delta_G(s;uv)\).

**The negative-semidefinite case.** Suppose \(N_G(u)=N_G(v)\). As \(uv\) is not an edge, both degrees equal some \(d\ge0\). Direct inspection of the Laplacian gives \(Lb=db\), hence \(v=(d+1)^{-1}b\) and \(w=(d+1)^{-1}v\). Substituting \(b^\mathsf TAb=2/(d+1)\) into (1) gives
\[
 \Delta_G(s;uv)=-\frac{2(d+2)}{(d+3)^2}(v^\mathsf Ts)^2\le0.
\]
Thus twins imply universal nonincrease, with equality precisely when the two initially expressed opinions agree (equivalently, their innate opinions agree).

**The indefinite case.** Conversely, suppose the missing-edge endpoints are not false twins. For any vertex \(k\notin\{u,v\}\), \((Lb)_k=\mathbf1_{kv\in E(G)}-\mathbf1_{ku\in E(G)}\); thus \(b\) is an eigenvector of \(L\) **if and only if** \(N_G(u)=N_G(v)\). Moreover, \(v\) and \(w\) are linearly dependent exactly when \(b\) is an eigenvector of \(L\): indeed \(w=\lambda v\) implies \(v=\lambda b\) after applying \(A^{-1}\), and the converse is immediate. Hence \(v,w\) are linearly independent.

Choose
\[
 s_+=v-\frac{v^\mathsf Tw}{\lVert w\rVert^2}w.
\]
Then \(w^\mathsf Ts_+=0\) and strict Cauchy–Schwarz gives \(v^\mathsf Ts_+=\lVert v\rVert^2-(v^\mathsf Tw)^2/\lVert w\rVert^2>0\). Formula (1) gives \(\Delta_G(s_+;uv)>0\). In contrast, choose \(s_-=b\). Let \(r=b^\mathsf TAb>0\) and \(c=\lVert Ab\rVert^2>0\). Formula (1) gives \(\Delta_G(b;uv)=\alpha rc(\alpha r-2)<0\), because \(0<\alpha r<1\). Both nonconstant vectors can be shifted by a constant and scaled by a positive factor into \([0,1]^n\); the strict signs persist by the identities following (1). This proves the equivalence and both strict possibilities.

**Characterization of networks and the sharp order.** If every missing edge joins false twins, the relation \(u\sim v\) defined by equality or nonadjacency is transitive: whenever \(uv\) and \(vw\) are both missing edges, their false-twin property gives \(N(u)=N(v)=N(w)\), which forbids \(uw\) as an edge as well. Its equivalence classes are independent sets, with all possible edges between distinct classes. Thus \(G\) is complete multipartite. Conversely, all nonadjacent vertices of a complete multipartite graph share a neighborhood, so every insertion is safe.

Every connected graph with two vertices is complete, and every connected graph with three vertices is either the path \(P_3=K_{1,2}\) or \(K_3\), both complete multipartite. The four-vertex path \(2-1-0-3\), which is not complete multipartite, provides the displayed strict positive witness. Direct inversion of the two \(4\times4\) integer matrices gives the three rational values in the Finding section. Thus the connected threshold is exactly four. \(\square\)

## Verification

Run `python3 verify.py` after installing the listed dependency in `requirements.txt`. It checks the Sherman–Morrison polarization-difference matrix identity using exact rational arithmetic, tests the false-twin negative identity and constructive positive/negative witnesses for all 3,227 nonedges occurring across all 772 labeled connected graphs of order at most five, and reproduces the exact four-vertex witness. This finite checking supplements the arbitrary-order proof and is not used to assert a result for all graph sizes. The graph classification and positive/negative existence have independent symbolic arguments above.

## Relationship to prior work

Friedkin and Johnsen (1990) developed the foundational influence-with-innate-opinions model. Parsegov et al. (arXiv:1505.04920, first posted 2015-05-19) developed and analyzed multidimensional variants. Musco, Musco and Tsourakakis (2018) define centered polarization and optimize polarization **plus** disagreement. Chitra and Musco (2019) study degree-preserving edge-weight reallocations and polarization changes. Bhalla, Lechowicz and Musco (2021, arXiv:2111.14020v1, Sections 3.1–3.3 and Appendix A) prove that adding an edge decreases polarization **plus** disagreement and specifically note that Loewner order on Laplacians does not pass through the squared inverse needed to compare polarization alone. The present result instead gives a complete topology-only, all-innate-opinions characterization for **polarization alone**, including the complete multipartite equivalence and sharp connected size cutoff. It does not claim that polarization increases under every innate-opinion assignment.

## Limitations

The equivalence is exact only for the specified scalar, homogeneous, unit-edge Friedkin–Johnsen equilibrium and a single previously absent undirected link. It is a structural possibility theorem, not an estimate of how often random opinion assignments cause increases or an empirical statement about social networks. Historical priority beyond the inspected sources is uncertain, and the original 1990 full text was not accessible in the inspected sources. Independent scholarly review has not been performed.

## References

- N. E. Friedkin and E. C. Johnsen (1990), *Social influence and opinions*, *The Journal of Mathematical Sociology* 15, 193–206. https://doi.org/10.1080/0022250X.1990.9990069
- S. E. Parsegov, A. V. Proskurnikov, R. Tempo and N. E. Friedkin (2015), *Novel Multidimensional Models of Opinion Dynamics in Social Networks*, first arXiv posting 2015-05-19. https://arxiv.org/abs/1505.04920
- C. Musco, C. Musco and C. E. Tsourakakis (2018), *Minimizing Polarization and Disagreement in Social Networks*, WWW. https://groups.csail.mit.edu/tds/papers/Musco/WWW18.pdf
- U. Chitra and C. Musco (2019), *Understanding Filter Bubbles and Polarization in Social Networks*, arXiv:1906.08772. https://arxiv.org/abs/1906.08772
- N. Bhalla, A. Lechowicz and C. Musco (2021), *Local Edge Dynamics and Opinion Polarization*, arXiv:2111.14020v1. https://arxiv.org/abs/2111.14020
