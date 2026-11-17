# Pole-reversal fixed configurations on every finite multitheta graph

## Finding

For each integer \(m\ge3\), let \(\Theta_m\) be the graph made of \(m\) internally disjoint closed arcs from a common pole \(A\) to a common pole \(B\). Parametrize each arc by \([0,1]\) from \(A\) to \(B\), and let \(\tau\) reverse all arcs, interchanging the poles. For every integer \(k\ge0\), the actual topological fixed-point space of unordered collision-free configurations has the canonical decomposition

\[
 \operatorname{UConf}_k(\Theta_m)^\tau\ \cong\
 \coprod_{\substack{0\le a\le m,\ b\ge0\\a+2b=k}}
 \binom ma\ \operatorname{UConf}_b(S_m^\circ),
\]

where \(S_m^\circ\) is the \(m\)-arm star with its \(m\) outer endpoints deleted, and a binomial coefficient preceding a space means that many disjoint copies. For \(b\ge1\), each factor is connected and homotopy equivalent to a bouquet of \(R_m(b)\) circles, where

\[
 R_m(b)=1+(m-1)\binom{b+m-2}{m-1}-\binom{b+m-1}{m-1},\qquad R_m(0)=0.
\]

Consequently, writing \(c_{m,k}\) for the number of components and \(h_{m,k}\) for the first integral Betti number,

\[
 c_{m,k}=\sum_{\substack{0\le a\le m,\ b\ge0\\a+2b=k}}\binom ma,
 \qquad
 h_{m,k}=\sum_{\substack{0\le a\le m,\ b\ge0\\a+2b=k}}\binom ma R_m(b).
\]

All higher integral homology vanishes and all integral homology is torsion-free. Both complete sequences have rational generating functions:

\[
\sum_{k\ge0}c_{m,k}x^k=\frac{(1+x)^m}{1-x^2},\qquad
\sum_{k\ge0}h_{m,k}x^k=(1+x)^m\left(\frac1{1-x^2}-\frac{1-(m-1)x^2}{(1-x^2)^m}\right).
\]

For every \(m\ge3\), first homology of the fixed-point space vanishes for \(k\le3\) and is nonzero for every \(k\ge4\). In particular,
\[
 \operatorname{UConf}_4(\Theta_m)^\tau\simeq
 \left(\bigvee^{\binom{m-1}{2}}S^1\right)
 \sqcup\ \left(\binom m2+\binom m4\right)\text{ isolated points}.
\]
The binomial term \(\binom m4\) is understood as zero for \(m<4\).

## Assumptions and scope

Graphs are geometric one-dimensional CW complexes, not discrete vertex sets. All configurations are unordered sets of exactly \(k\) distinct points, with no collision at either pole or at the interior of any arc. The involution \(\tau\) acts on the graph by \(\tau(i,t)=(i,1-t)\); its fixed-point set on the underlying graph consists of the \(m\) distinct midpoints. The space \(S_m^\circ\) has a common central vertex and \(m\) branches modeled on half-open intervals \([0,1)\). The empty configuration space \(\operatorname{UConf}_0(X)\) is a singleton. The assertion concerns geometric fixed points, not invariant homology classes or the orbit quotient. The first public foundational source used is Farley–Sabalka [1], first posted 25 October 2004 (not its 2005 journal date).

## Proof

**1. Complete orbit-sector homeomorphism.** Set \(F=|\Theta_m|^\tau\), the set of arm midpoints. Removing \(F\) splits the graph into two open-ended stars \(U_A\) and \(U_B\), exchanged by \(\tau\); both are homeomorphic to \(S_m^\circ\). If a finite configuration \(Q\) is \(\tau\)-invariant, then every particle in \(F\) forms a singleton orbit, while every other particle belongs to a two-point orbit \(\{p,\tau p\}\) with exactly one point \(p\in U_A\). Thus \(Q\) is uniquely determined by a subset \(T\subseteq F\) of cardinality \(a\) and a \(b\)-point configuration \(P\subset U_A\), subject to \(a+2b=k\): the inverse map sends \((T,P)\) to \(T\cup P\cup\tau P\). These maps are continuous in the finite-subset topology. Within the fixed configuration space the functions recording which midpoints are occupied are locally constant: a fixed midpoint cannot become occupied or vacated through a continuous invariant collision-free path, since any approaching nonfixed orbit brings two points together at that midpoint. Hence the finitely many sectors indexed by \(T\) are open and closed, and the continuous inverse maps combine to a homeomorphism of the displayed disjoint union. No quotient identification between different \(T\)'s is introduced.

**2. The half-open star is homotopically an ordinary star for configurations.** Identify each branch of \(S_m^\circ\) with \([0,\infty)\) by an increasing homeomorphism. Let \(S_m\) instead have closed unit branches. The inclusion of \(S_m\) into the infinite star and the injective branchwise map \(s\mapsto s/(1+s)\) in the other direction induce maps on every unordered configuration space. The composites are homotopic to identity maps through the strictly increasing injections \(s\mapsto(1-t)s+t s/(1+s)\), so collisions never occur. Therefore \(\operatorname{UConf}_b(S_m^\circ)\simeq\operatorname{UConf}_b(S_m)\) for all \(b\ge0\).

**3. Dimension and connectedness of the star factor.** For \(b=0\) the configuration space is a point, and for \(b=1\) it is the contractible star. For \(b\ge2\) it is path connected: the third arm can be used to bypass the center while reassigning finite, unlabeled particles to prescribed radial positions; the particles are indistinguishable and branch order can be preserved. The radial-tree case of the discrete Morse theorem [1, Section 4, especially Corollary 4.2 and Theorem 4.3] shows that the space has homotopy type of a connected one-dimensional CW complex. Hence it is a wedge of finitely many circles and its rank is \(1-\chi\).

**4. Independent derivation of the exact rank.** Subdivide each arm of the closed star into \(L\) edges, with \(L>b+1\). The standard discretized cubical configuration complex is homotopy equivalent to the continuous one for this sufficient subdivision [1, Section 2]. A cubical cell occupying \(j\) mutually vertex-disjoint edges and \(b-j\) vertices outside their endpoints has dimension \(j\). If \(M_j\) denotes the number of \(j\)-edge matchings of the subdivided star (which has \(V=1+mL\) vertices), its Euler characteristic is

\[
 \chi_b=\sum_{j=0}^b(-1)^j M_j\binom{V-2j}{b-j}.
\]

For a path on \(L\) vertices let \(F_L(t)=\sum_{j\ge0}\binom{L-j}{j}t^j\) be its matching polynomial, with \(F_0(t)=1\). Resolving whether the center of the star is matched gives its matching polynomial

\[
 M(t)=F_L(t)^m+mtF_{L-1}(t)F_L(t)^{m-1}.
\]

Substitute \(t=-z/(1+z)^2\), multiply by \((1+z)^{1+mL}\), and use the elementary path identity

\[
F_L\!\left(-\frac{z}{(1+z)^2}\right)=\frac{1-z^{L+1}}{(1-z)(1+z)^L}.
\]

The exact generating function for the cubical Euler characteristics is then

\[
\sum_b \chi_bz^b=\frac{(1+z)(1-z^{L+1})^m-mz(1-z^L)(1-z^{L+1})^{m-1}}{(1-z)^m}.
\]

For every \(b<L\), terms involving \(z^L\) vanish when taking the \(z^b\) coefficient. Hence \(\chi_b=[z^b](1-(m-1)z)/(1-z)^m\), that is
\[
 \chi_b=\binom{b+m-1}{m-1}-(m-1)\binom{b+m-2}{m-1}.
\]
Connectedness and the one-dimensional Morse bound give the claimed \(R_m(b)=1-\chi_b\). This agrees with the classical radial-tree rank in [1, Corollary 4.2], which is prior work, not a new ordinary-star result.

**5. Integral topology and phase transition.** Each sector is a connected wedge of circles, or a point. Counting the \(\binom ma\) possible midpoint subsets yields the Betti sums; summing in \(k\) gives the displayed rational generating functions. No higher or torsion homology can occur. Since \(R_m(0)=R_m(1)=0\) and \(R_m(2)=\binom{m-1}{2}>0\), there are no loops for \(k\le3\). For even \(k\ge4\) choose \(a=0\) and \(b=k/2\), and for odd \(k\ge5\) choose \(a=1\) and \(b=(k-1)/2\); in both cases \(b\ge2\), so some sector has a nonzero first Betti number. The explicit \(k=4\) decomposition follows by listing \((a,b)=(0,2),(2,1),(4,0)\).

## Verification

Run `python3 verification/pole_theta_check.py` using the Python standard library. The independent program enumerates all cubical star cells by disjoint edge and vertex selections, compares their alternating face counts with the closed Euler-rank formula for twenty cases (three to six arms, zero to four particles), and checks involution-invariant vertex subsets in twenty-one finite theta subdivisions against their predicted midpoint/paired-orbit sectors. The saved deterministic output is `verification/pole_theta_output.txt`, ending in `THETA_POLE_FIXED_SECTOR_CHECKS_PASS`. This is a finite check of the arithmetic, orbit indexing, and sign convention, not an exhaustive proof for continuous configurations or all particle counts. The universal argument is above.

## Relationship to prior work

Farley and Sabalka [1] establish the graph-configuration Morse bound and the ordinary radial-tree braid rank; these are used and explicitly not claimed as new. A published calculation of two-particle theta configurations and their complete arm/pole action [2] covers the two-particle special case. A previously published all-positive-separation equivariant deformation of two particles on equilateral banana graphs [3] also covers that two-particle instance and is not superseded here. The new claim is specifically the topological **fixed-space decomposition for every particle count** under pole reversal, with its integral homology and rational full-particle generating functions. Previously published work on four-particle theta *homology representations* [4] computes an action on ambient homology rather than its geometric fixed configurations, and does not imply this classification. The decomposition uses an elementary orbit principle, but the complete identified fixed spaces and the sharp emergence of loops at four particles are not present in the inspected sources. A generic configuration-orbit result or unindexed equivalent theorem remains a priority risk.

## Limitations

The involution must reverse the two poles and preserve each arm individually. This result does not classify combined pole reversal with nontrivial arm permutations, other automorphism subgroups, particle-labeled configurations, or the topology of the quotient configuration space. Its homotopy equivalences for individual star factors are not claimed as canonical or equivariant under residual arm permutations. The stated homeomorphism of fixed-space sectors is exact. Independent mathematical audit and definitive literature priority assessment have not been performed.

## References

[1] D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539, first public 25 October 2004; Algebraic & Geometric Topology 5 (2005), 1075–1109, especially Section 4, Corollary 4.2 and Theorem 4.3. https://arxiv.org/abs/math/0410539

[2] *The integral arm-permutation and pole-swap module of two-point theta configurations*, published result (8 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-integral-arm-permutation-and-pole-swap-module-of-two-point-t--21b7a73a2f7e

[3] *Equivariant diametral retraction for two hard-core particles on equilateral banana graphs*, published result (1 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-equivariant-diametral-retraction-for-two-hard-core-particles-on--05feb980a5f4

[4] *Pole-interchange parity and Schur modules in four-particle generalized-theta homology*, published result (18 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-pole-interchange-parity-and-schur-modules-in-four-particle-gener--e1f090c48cdc
