# Coefficientwise Roman-defense dominance of the Desargues graph

## Finding
Write \(P=\operatorname{GP}(10,2)\) for the twenty-vertex dodecahedral graph and \(D=\operatorname{GP}(10,3)\) for the twenty-vertex Desargues graph. For any finite simple graph \(G\), let
\[
R_G(z)=\sum_f z^{\sum_{v\in V(G)}f(v)},
\]
where the sum ranges over **all** Roman dominating functions \(f:V(G)\to\{0,1,2\}\): each zero-labelled vertex has a neighbor labelled two. Then
\[
\boxed{R_D(z)-R_P(z)=4z^{12}(1+z)^6Q(z)}
\]
with
\[
\begin{aligned}
Q(z)={}&80+760z+3025z^2+6748z^3+9712z^4+9873z^5\\
&+7427z^6+4233z^7+1825z^8+580z^9+125z^{10}+15z^{11}.
\end{aligned}
\]
All coefficients of \(Q\) are positive. Consequently, for each integer weight \(w\) from \(12\) to \(29\), strictly more Roman dominating functions of weight \(w\) exist on \(D\) than on \(P\); outside this range their counts coincide. The two graphs have the same minimum Roman weight \(12\) (known previously) but respectively \(340\) and \(20\) minimum functions. The total numbers of Roman dominating functions are \(754{,}088{,}530\) and \(742{,}721{,}362\), respectively.

In particular, assign independent labels to all twenty vertices with probabilities proportional to \(1:z:z^2\), where \(z>0\). The Roman domination success probability is \(R_G(z)/(1+z+z^2)^{20}\), and is strictly greater for \(D\) than for \(P\) at **every** positive parameter value. At \(z=1\) the absolute difference is exactly \(11{,}367{,}168/3^{20}\). This is a full-weight comparison, not simply a comparison of optimum weights or numbers.

## Assumptions and scope
The generalized Petersen graph \(\operatorname{GP}(10,k)\), with \(k\in\{2,3\}\), has vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/10\mathbb Z\) and undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\) for every \(i\). These two graphs are simple, connected, cubic, and have \(20\) vertices and \(30\) edges each. Their Roman-label probability comparison assumes the **same** parameter \(z\) and the independent per-vertex label distribution specified above. All counting concerns named vertex labelings, without dividing by automorphisms. Zero labels must be adjacent to at least one *open-neighborhood* label two; no perfect/unique-defense condition is imposed.

## Proof
**Exact support decomposition.** Fix any graph \(G\) with \(n\) vertices and let \(B=f^{-1}(2)\). Define the closed neighborhood \(N[B]=B\cup\bigcup_{v\in B}N(v)\). Every vertex outside \(N[B]\) must carry label one, whereas every vertex inside \(N[B]\setminus B\) may carry label zero or one freely. Each choice determines a distinct Roman function, and all Roman functions arise uniquely in this way. Thus, for every finite graph,
\[
R_G(z)=\sum_{B\subseteq V(G)}z^{2|B|+n-|N[B]|}(1+z)^{|N[B]|-|B|}.
\tag{1}
\]
The formula includes the empty support, for which only the all-ones function occurs. There is no assumption that any chosen support is a dominating set.

**Exact finite census.** Apply (1) independently to \(P\) and \(D\). Each has precisely \(2^{20}=1{,}048{,}576\) two-label supports \(B\), represented by all unsigned twenty-bit words. Let \(h_G(t,r)\) count supports with \(|B|=t\) and \(|V(G)\setminus N[B]|=r\). Formula (1) becomes
\[
R_G(z)=\sum_{t=0}^{20}\sum_{r=0}^{20}h_G(t,r)z^{2t+r}(1+z)^{20-t-r}.
\tag{2}
\]
All \(21\times21\) histogram entries and all \(41\) coefficients for each graph appear as exact integers in `data/roman_census.json`. The file is a finite table certificate, not an extrapolation from sampling: the two standalone implementations construct their own graph adjacency relations, exhaust the entire support universe, recompute every entry, and check both polynomial arrays. One verifier constructs generalized Petersen edges directly; the other uses distinct twenty-vertex adjacency triples with explicit isomorphism permutations. The second additionally tests its support-decomposition formula against an independent direct \(3^{10}\)-label exhaustive search on the ten-vertex Petersen graph. Both implementations terminate successfully and report matching counts.

**Algebraic comparison.** Subtract the two exact weight-coefficient vectors in `data/roman_census.json`. The difference at weights \(0,\ldots,11\) and \(30,\ldots,40\) is zero; at weights \(12,\ldots,29\), in increasing order, the differences are
\[
(320,4960,35140,151592,447900,966980,1589280,2045040,2101124,1746720,1183980,655580,295060,106432,29920,6220,860,60).
\]
Multiplying \(4z^{12}(1+z)^6Q(z)\) yields this entire degree-\(40\) difference vector, which both independently run verifiers check exactly, coefficient by coefficient. Every displayed coefficient of \(Q\) is strictly positive, so the difference is positive at every \(z>0\), and the coefficientwise and probability conclusions follow without asymptotic assumptions.

## Verification
From the package root, compile and execute `checks/verify_gp_roman.cpp` with a standard C++17 compiler and run `python3 checks/verify_poly_independent.py` using Python 3.8 or later; commands and expected checks are in `VERIFICATION.md`. No third-party packages or downloaded files are required. The second program verifies the exact packaged histogram and polynomial tables in addition to its independently constructed census. Each program traverses the complete finite search range and checks the factorization. An execution failure, timeout, or partial run is not a verification of these claims.

## Relationship to prior work
Wang, Xu, Yang, and Ji's 2011 preprint established \(\gamma_R(\operatorname{GP}(n,2))=\lceil8n/7\rceil\), hence the minimum value \(12\) for \(P\). Zhang, Shao, and Xu's 2014 paper proved the Roman domination number of \(\operatorname{GP}(n,3)\) and likewise gives \(12\) for \(D\). The previously published *Frozen and mobile minimum Roman functions of the Desargues graph* established the \(340\) optimum functions and their reconfiguration structure. These results do not determine all \(41\) coefficients for either graph or their strict coefficientwise comparison. The new claim here is specifically the **complete coefficientwise difference and its all-parameter Roman-defense reliability dominance**; the scalar minimum and the Desargues minimum-function count are credited, not asserted to be new. Other domination and perfect Roman variants use different predicates.

## Limitations
This is a finite, exhaustive theorem only for these two specified twenty-vertex graphs. No injection between their Roman functions, no analogue for all generalized Petersen graphs, and no inequality for arbitrary independent three-label probabilities is claimed. The exact factorization is certified by exhaustive arithmetic and independent graph-coordinate calculations, rather than derived from a uniform structural bijection. Unindexed enumerations or tables could overlap the full polynomial and therefore remain a priority risk. Independent external scientific validation has not been performed.

## References
1. H. Wang, X. Xu, Y. Yang, C. Ji, *Roman domination number of Generalized Petersen Graphs P(n,2)*, arXiv:1103.2419v1, first posted 2011-03-12, https://arxiv.org/abs/1103.2419 (Theorem 2.12).
2. Z. Zhang, Z. Shao, X. Xu, *On the Roman domination numbers of generalized Petersen graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **89** (2014), 311–320, https://combinatorialpress.com/article/jcmcc/Volume%20089/vol-089-paper%2023.pdf (Theorem 3).
3. *Frozen and mobile minimum Roman functions of the Desargues graph*, published mathematical research record, 2026-10-18, identifier `20a24343886d` (exact count and reconfiguration of minimum Roman functions).
4. E. J. Cockayne, P. A. Dreyer, S. M. Hedetniemi, S. T. Hedetniemi, *Roman domination in graphs*, Discrete Mathematics **278** (2004), 11–22 (foundational definition).
