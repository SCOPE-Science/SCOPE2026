# Universal simple-pole susceptibility for grandparent bond percolation with finite-mean offspring

## Finding

Let \(T\) be a Bienaymé–Galton–Watson rooted tree with nonnegative integer offspring \(X\) of arbitrary law, subject only to \(1<m=\mathbb E X<\infty\). Add a formal parent \(\star\) above its root, connect every vertex to its parent, and connect every vertex other than the original root to its grandparent (so \(\star\) is connected to the root and all of its children). Independently retain each edge with probability \(p\). Let \(C_p\) be the vertices of \(T\) in the open cluster of \(\star\), excluding \(\star\), and write \(\chi_X(p)=\mathbb E|C_p|\). This is the *augmented-ancestor* susceptibility, not the original-root susceptibility.

Let \(\phi(z)=\mathbb E[z^X]\), \(f=f_X(p)\) be the unique solution in \((0,1)\) of
\[
f=1-p+p(1-p)\phi(f),
\]
put \(v=\phi'(f)\), \(a=(1-p)\phi(f)\), and \(\Delta=1-p^2(1-p)^2v^2\). Define
\[
U(p)=\frac1{1-mp}-\frac{a}{\Delta},\qquad
V(p)=\frac{m(1-p)}{1-mp}-\frac{(1-p)^2v}{\Delta}.
\]
For every \(0<p<p_c(X)\), where \(p_c(X)\) is the bond-percolation critical point on the grandparent graph,
\[
\boxed{\chi_X(p)=\frac{U(p)}{1-V(p)}.}
\]
Moreover, \(U(p_c)>0\), \(V(p_c)=1\), and \(0<V'(p_c)<\infty\), so
\[
\boxed{\lim_{p\uparrow p_c}(p_c-p)\chi_X(p)
=\frac{U(p_c)}{V'(p_c)}\in(0,\infty).}
\]
Thus the subcritical susceptibility exponent is exactly one, with an explicit finite, strictly positive residue, for *every* finite-mean supercritical offspring law, **even when its variance is infinite**. The threshold itself is the unique solution in \((0,m^{-2})\) identified by Ménard and Sénizergues [1].

## Assumptions and scope

The graph is the undirected, unweighted grandparent graph of a Galton–Watson tree, with a single extra parent above the root as specified. Short and long edges are all independently open with the *same* parameter \(p\). The tree may become extinct; expectations average over both the tree and the bond configuration. Only \(\mathbb E X=m\in(1,\infty)\) is assumed. No offspring variance, bounded-support, or exponential-moment hypothesis is made. The strict inequalities and derivatives in the claim are on the open interval containing \(p_c\), where \(p_c<m^{-2}<m^{-1}\). The case \(p=0\) has \(\chi_X(0)=0\); the displayed formulas extend continuously there. The exact residue applies to the augmented-ancestor observable defined above, not an unidentified root-conditioned or quenched susceptibility.

## Proof

**1. The established block exploration.** For \(0<p<m^{-1}\), let \(\widetilde C_p\) be the family reachable downwards from the root using open grandparent edges, and split it by even/odd height. It is a Galton–Watson tree with offspring pgf \(\phi(1-p+pz)\), of mean \(pm<1\). A short edge anywhere in \(\widetilde C_p\) connects its two parity classes. Let \(D_p\) be the intersection of \(\widetilde C_p\) with the cluster of \(\star\). As established by the independent-block decomposition in [1, Proposition 7], the full cluster is a union of such finite blocks indexed by a Galton–Watson process whose offspring count \(B_p\) is the number of corresponding boundary subtrees; each descendant block has the same law as \(D_p\). In particular, below the critical point,
\[
\mathbb E|C_p|=\mathbb E|D_p|\sum_{j=0}^\infty(\mathbb E B_p)^j
=\frac{\mathbb E|D_p|}{1-\mathbb E B_p}.
\]
The block decomposition is used here as a cited theorem, not asserted as a new lemma. Its validity includes finite-mean, potentially infinite-variance, offspring laws because \(pm<1\).

**2. Exact first-block size.** For \(p<m^{-1}\), the expected total number of vertices of \(\widetilde C_p\) equals \(1/(1-mp)\). All its odd-level vertices connect by long edges to \(\star\); its even-level vertices connect precisely when at least one of the \(|\widetilde C_p|\) internal short edges is open [1, Proposition 7]. If \(E_p\) counts even-level vertices and \(x=1-p\), then
\[
\mathbb E|D_p|=\frac{1}{1-mp}-\mathbb E[x^{|\widetilde C_p|}E_p].
\]
To calculate the last term, define the parity-refined total-size pgfs \(G_0(s,t),G_1(s,t)\), with \(G_0=s\phi(1-p+pG_1)\) and \(G_1=t\phi(1-p+pG_0)\). At \(s=t=x\), both pgfs are \(a=x\phi(f)\), with \(f=1-p+pa\). Differentiation of the two identities in \(s\) gives
\[
s\partial_sG_0\big|_{s=t=x}
=\frac{a}{1-(xp\phi'(f))^2}.
\]
The denominator is positive because \(xp\phi'(f)\le pm<1\). Therefore \(\mathbb E|D_p|=U(p)\) as claimed.

**3. Exact boundary offspring mean.** Equation (5) of [1, Proposition 9] states
\[
\mathbb E B_p=\frac{m(1-p)}{1-mp}-\partial_z A(1-p,1,1,p),
\]
where \(A\) records the downward-tree size and the two parity-boundary counts. Differentiating equation (4) of the same proposition in the two parity variables, at \(x=1-p,y=z=1\), gives the linear system
\[
A_y=xpvA_z,\qquad A_z=xv(pA_y+x).
\]
Hence \(A_z=x^2v/[1-(xpv)^2]\) and \(\mathbb E B_p=V(p)\). Theorem 10 of [1] shows that \(V(p_c)=1\), with \(0<p_c<m^{-2}\); Proposition 8 implies \(V(p)<1\) when \(p<p_c\). Combining these facts with the block identity proves the exact formula.

**4. Strict positivity and differentiability of the pole.** Throughout \(0<p\le m^{-2}\), the unique fixed point satisfies \(1-p\le f\le1-p^2<1\). Thus \(\phi'\) and \(\phi''\) at \(f\) are finite, regardless of whether \(\mathbb E X^2\) is finite, and the implicit-function theorem applies. Direct differentiation yields
\[
f'(p)=\frac{-1+(1-2p)\phi(f(p))}{1-p(1-p)\phi'(f(p))}<0,
\qquad v'(p)=\phi''(f(p))f'(p)\le0.
\]
For \(H(p,v)=(1-p)^2v/[1-p^2(1-p)^2v^2]\), ordinary partial differentiation at fixed \(v\) gives
\[
\partial_pH=-\frac{2(1-p)v[1-p(1-p)^3v^2]}{\Delta^2}<0,
\qquad
\partial_vH=\frac{(1-p)^2[1+p^2(1-p)^2v^2]}{\Delta^2}>0.
\]
Indeed, \(v\le m\), so \(p(1-p)^3v^2\le pm^2(1-p)^3<1\) on the stated interval. Consequently \(\mathrm dH(p,v(p))/\mathrm dp<0\). Since
\[
V'(p)=\frac{m(m-1)}{(1-mp)^2}-\frac{\mathrm d}{\mathrm dp}H(p,v(p))>0,
\]
its value at \(p_c\) is finite and strictly positive. Finally, \(U(p)=\mathbb E|D_p|\ge p>0\) because the root belongs to \(D_p\) when the edge \((\star,\text{root})\) is open. Continuity and the first-order expansion \(1-V(p)=V'(p_c)(p_c-p)+o(p_c-p)\) finish the proof.

## Verification

The supplied `CHECK.py` is a standard-library-only finite checker. It tests the exact pgf formulas and derivatives for seven finite-support offspring laws, checks the pole limit numerically and enumerates all open/closed configurations of the two-generation deterministic binary graph with exact rational probabilities. It passed 247 deterministic assertions. In the deterministic binary example, \(p_c\approx0.15865632604477647\) and the **augmented-ancestor** pole residue is approximately \(0.08260628557486904\). The finite-depth expected cluster sizes for depths zero, one, two at \(p=1/10\) are respectively \(1/10\), \(33753/100000\), and \(4357733646841/10000000000000\), strictly below the infinite expression. These finite tests do not prove any infinite statement; the preceding argument does.

The theorem includes, for example, offspring with \(\Pr(X=k)=k^{-5/2}/\zeta(5/2)\) on positive integers: its mean is finite and greater than one, but its variance is infinite. Its derivatives at \(f(p_c)<1\) remain finite.

## Relationship to prior work

Ménard and Sénizergues [1], first public on 6 November 2026, introduce the grandparent bond-percolation model, prove the independent-block exploration and characterize \(p_c\) via an offspring generating-function equation. The present result adds an explicit *augmented-ancestor mean cluster size* and establishes its sharp simple-pole divergence and residue without a second-moment assumption. It does not claim discovery of the block decomposition or of the critical probability.

Špakulová [2] develops tree-of-pieces percolation methods and computes the regular grandparent example's threshold. Hutchcroft [3] proves mean-field critical exponents for quasi-transitive nonunimodular graph percolation, potentially covering the exponent-only assertion for deterministic regular grandparent trees; neither inspected abstract establishes this arbitrary finite-mean random-offspring formula or the explicit amplitude. The exact original-root site-percolation susceptibility has a different dependence structure and does not imply this bond-percolation statement. Other branching-process susceptibility results, such as Janson [4] for random graphs with prescribed degrees, concern different models.

## Limitations

The result is annealed and pertains to a formal-parent-connected cluster in the augmented graph; no exact original-root or quenched susceptibility is claimed. It does not provide the critical cluster-size distribution, the supercritical order-parameter exponent, or a rate of convergence in the pole asymptotic. The exact amplitude is implicit through the unique fixed point and a derivative, not a closed radical for a general offspring law. Historical literature beyond the inspected materials may contain stronger statements; no independent mathematical audit has been performed.

## References

[1] L. Ménard and D. Sénizergues, *Percolation on grandparent graphs of Bienaymé trees*, arXiv:2611.09762v1, 6 November 2026, https://arxiv.org/html/2611.09762v1 (especially Propositions 7–9 and Theorem 10).

[2] I. Špakulová, *Critical percolation of virtually free groups and other tree-like graphs*, Annals of Probability 37 (2009), 2262–2296, arXiv:0801.4153, https://arxiv.org/abs/0801.4153.

[3] T. Hutchcroft, *Non-uniqueness and mean-field criticality for percolation on nonunimodular transitive graphs*, Journal of the American Mathematical Society 33 (2020), 1101–1165, arXiv:1711.02590, https://arxiv.org/abs/1711.02590.

[4] S. Janson, *Susceptibility of random graphs with given vertex degrees*, arXiv:0911.2636, https://arxiv.org/abs/0911.2636.
