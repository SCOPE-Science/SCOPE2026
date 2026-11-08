# Optimal Kuhn packets in the \(A_4\) root lattice: exactly 120 directed-path frames

## Finding
Let \(H=\{x\in\mathbb R^5:\sum_{i=1}^5x_i=0\}\) carry the induced Euclidean metric, and set \(A_4=H\cap\mathbb Z^5\). For an unordered four-element linearly independent set \(F=\{b_1,b_2,b_3,b_4\}\subset A_4\), write \(\kappa_F\) for the maximum of the minimum-enclosing-ball radii of its 24 permutation simplices:
\[
\Delta_\sigma(F)=\operatorname{conv}\left\{0,b_{\sigma(1)},b_{\sigma(1)}+b_{\sigma(2)},b_{\sigma(1)}+b_{\sigma(2)}+b_{\sigma(3)},\sum_{j=1}^4b_j\right\}.
\]
Here the containing balls may have different centers, but all simplices use the same frame. Then
\[
\boxed{\kappa(B^4,A_4)=\inf_F\kappa_F=\sqrt{6/5}=\mu(B^4,A_4).}
\]
Moreover, precisely \(5!=120\) unordered frames attain the infimum. They are
\[
\boxed{F_\pi=\{e_{\pi(1)}-e_{\pi(2)},e_{\pi(2)}-e_{\pi(3)},e_{\pi(3)}-e_{\pi(4)},e_{\pi(4)}-e_{\pi(5)}\}\quad (\pi\in S_5).}
\]
The graph encoded by each frame is one directed Hamiltonian path on five labeled vertices. These optimal frames are all full lattice bases.

## Assumptions and scope
We use the ordinary Euclidean norm inherited by the four-dimensional zero-sum hyperplane \(H\). The allowed frames are **any** four independent lattice vectors, including frames whose integer span could a priori be a proper sublattice. Two frames differing only by an ordering of the same four vectors are the same frame. Coordinate-label permutations are counted as distinct labeled frames. The invariant is the original common-independent-frame Kuhn-packet radius of Xue [1], not the more permissive periodic-triangulation invariant. The lattice covering radius \(\mu\) uses translates by the actual lattice \(A_4\).

## Proof
**1. Classical covering radius.** The Voronoi cell about zero is
\[
V=\{x\in H: |x_i-x_j|\le1\text{ for all }i,j\}.
\]
Necessity follows by comparing zero with each root \(e_i-e_j\), whose squared norm is \(2\). Conversely, let \(x\in V\) and \(z\in A_4\). If \(m=\sum_{z_i>0}z_i=-\sum_{z_i<0}z_i\), then
\[
\langle x,z\rangle\le m(\max_i x_i-\min_i x_i)\le m\le\tfrac12\sum_i z_i^2.
\]
The last inequality uses \(z_i^2\ge|z_i|\) for integers. Hence zero is at least as close as every lattice point. A vertex of \(V\) must have all its coordinates at one of two levels exactly one unit apart: otherwise its active equality graph is disconnected and leaves a nonzero tangent perturbation in \(H\). With \(k\in\{1,2,3,4\}\) coordinates at the higher level, its coordinates are \((5-k)/5\) (\(k\) times) and \(-k/5\) (\(5-k\) times). Its squared norm equals \(k(5-k)/5\), maximized at \(k=2,3\). Consequently \(\mu(B^4,A_4)^2=6/5\).

**2. A fitting ball for every path-frame simplex.** Fix a permutation \(\pi\in S_5\) and its directed path frame \(F_\pi\). Given an arbitrary ordering of the four edges, let \(u_0=0,u_1,\ldots,u_4\) be the successive partial sums. Every coordinate of each \(u_j\) lies in \(\{-1,0,1\}\). More strongly, in one coordinate the successive values cannot include both \(-1\) and \(1\): one incoming and one outgoing directed edge are added once each, and whichever is added first determines the unique nonzero sign before both are present. This also holds at the path endpoints, where only one edge is incident.

Put \(a_i=-\min_{0\le j\le4}(u_j)_i\). Thus \(a\in\{0,1\}^5\), and each \(u_j+a\) is a binary vector. Every \(u_j\) has coordinate sum zero, so the binary vectors have one common Hamming weight \(k=\sum_i a_i\). The two path endpoints force \(1\le k\le4\). With the center \(c=(k/5)\mathbf1-a\in H\),
\[
\|u_j-c\|^2=\|u_j+a-(k/5)\mathbf1\|^2=\frac{k(5-k)}5\le\frac65
\quad\text{for every }j=0,\ldots,4.
\]
Therefore **all** 24 permutation simplices of each \(F_\pi\) fit in Euclidean balls of radius \(\sqrt{6/5}\). Xue's established inequality \(\mu\le\kappa\) [1, Proposition 2.4] supplies the converse, yielding equality.

**3. Necessity and rigidity of the frames.** Suppose some independent frame \(F=\{b_1,b_2,b_3,b_4\}\) satisfies \(\kappa_F\le\sqrt{6/5}\). For every subset \(I\subset\{1,2,3,4\}\), select a packet ordering having \(I\) first. The points \(0\) and \(b_I=\sum_{i\in I}b_i\) then lie in a common ball of radius at most \(\sqrt{6/5}\), hence \(\|b_I\|^2\le24/5\). Every vector of \(A_4\) has even integral squared norm, since \(z_i^2\equiv z_i\pmod2\) and the coordinate sum vanishes. Thus
\[
\boxed{\|b_I\|^2\le4\quad\text{for every subset }I.}
\]
In particular, every nonzero frame vector has either one \(+1\) and one \(-1\), or two of each, and all other coordinates zero. If two frame vectors both had \(+1\) in a fixed coordinate, their two-element subset sum would have a coordinate \(+2\); a zero-sum integer vector with a coordinate of magnitude at least two has squared norm at least six. The same applies to two \(-1\)'s. Therefore each of the five coordinate rows among the four frame vectors has at most one \(+1\) and at most one \(-1\).

If two or more frame vectors had squared norm four, the total number of nonzero matrix entries would be at least \(4+4+2+2=12\), contradicting the row bound of ten. If exactly one had squared norm four, the total would be exactly ten: every row would have one \(+1\) and one \(-1\), forcing \(\sum_{i=1}^4b_i=0\) and contradicting independence. Hence **all four frame vectors are roots** \(e_a-e_b\).

Interpret these vectors as four oriented edges on five labeled vertices. The row restriction gives indegree and outdegree at most one. Independence of the four incidence vectors forces their underlying graph to be connected (a disconnected graph has incidence rank at most three). Four edges on five vertices then form a tree, and the degree restrictions force a single directed Hamiltonian path. Its edge set is precisely \(F_\pi\) for a unique coordinate permutation \(\pi\). Conversely each such directed path is a unimodular root basis. There are exactly \(5!=120\) distinct unordered frames, completing the classification.

## Verification
The standalone file `verify_a4.py` uses only Python's standard library and exact integer arithmetic. It enumerates all 50 nonzero short vectors of squared norm two or four, screens every one of the \(\binom{50}{4}=230300\) unordered four-vector candidates using all nonempty subset sums, checks independence by exact four-by-four determinants, and obtains exactly the 120 oriented-path frames (all determinants of absolute value one). It independently constructs and checks an explicit ball for each of the \(120\times24=2880\) ordered packet simplices using integer identities equivalent to the squared-radius formula. These finite tests corroborate the analytic proof and are not substitutes for it.

To reproduce: `python3 verify_a4.py`. Expected marker: `A4_PACKET_EXACT_OK`.

## Relationship to prior work
The invariant, the 24-simplex packet definition, existence of an optimal frame, and the lower bound \(\mu\le\kappa\) are due to Xue [1]; none is claimed as new. That article proves coincidence with classical covering minima in dimensions at most two and on standard coordinate examples, while allowing the original common-frame radius to differ from the classical one for higher-dimensional lattices. Its ellipsoid equality for a *relaxed* periodic-triangulation invariant does not imply equality for the original common-frame invariant. The standard \(A_4\) lattice and its root data are recorded in [2]. The present result is the exact original-packet value on this four-dimensional root lattice **together with an exhaustive structural description of every optimal frame**.

## Limitations
This result is specific to the standard Euclidean \(A_4\) lattice and its uniformly scaled orthogonal images; no claim is made for all four-dimensional lattices, for arbitrary affine distortions with a fixed Euclidean ball, or for other root systems. The binary containing balls supplied in step 2 need not be the individual simplices' unique minimum enclosing balls. Historical priority is subject to older lattice-triangulation equivalences that may not use the new invariant's terminology. Independent mathematical validation has not been performed.

## References
[1] F. Xue, *On \(\kappa\)-covering minima*, arXiv:2610.39034v1, first publicly posted 28 October 2026, in particular definition (1.1) and Propositions 2.2, 2.4. https://arxiv.org/abs/2610.39034

[2] G. Nebe and N. J. A. Sloane, *Catalogue of Lattices: The Lattice A4*, published catalogue entry (2014). https://www.math.rwth-aachen.de/homes/Gabriele.Nebe/LATTICES/A4.html
