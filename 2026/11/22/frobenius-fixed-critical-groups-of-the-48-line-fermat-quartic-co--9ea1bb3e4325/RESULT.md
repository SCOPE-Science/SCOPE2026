# Frobenius-fixed critical groups of the 48-line Fermat quartic configuration

## Finding
Let \(k=\mathbb F_q\) have characteristic at least five and let \(X/k\) be the smooth Fermat quartic
\[
 X:\quad x_0^4+x_1^4+x_2^4+x_3^4=0.
\]
Form the simple graph \(\Gamma\) whose vertices are its forty-eight geometric lines, with an edge for each intersecting pair of distinct lines. Geometric Frobenius induces an automorphism \(F_q\) on its integral critical group \(K(\Gamma)\). With \(C_m=\mathbb Z/m\mathbb Z\), the **complete Frobenius-fixed critical group** is
\[
K(\Gamma)^{F_q}\cong\begin{cases}
C_4^2\oplus C_{12}^{10}\oplus C_{24}^5\oplus C_{192}^6\oplus C_{960}^2\oplus C_{1920}^3\oplus C_{5760}, &q\equiv1\pmod8,\\
C_2^3\oplus C_4\oplus C_{12}^3\oplus C_{48}^3\oplus C_{96}^2\oplus C_{192}\oplus C_{960}^2\oplus C_{2880},&q\equiv3,7\pmod8,\\
C_2\oplus C_4^2\oplus C_{12}^9\oplus C_{60}\oplus C_{240}^4\oplus C_{720}, &q\equiv5\pmod8.
\end{cases}
\]
The orders in these three rows are respectively \(2^{115}3^{28}5^6\), \(2^{57}3^{13}5^3\), and \(2^{45}3^{16}5^6\). Thus all five-primary torsion is fixed for residue five, whereas just order \(5^3\) survives for residues three and seven. The full critical group (the first row) is previously established; the claim of new information is the **three nonsplit Frobenius actions** and their fixed integral group structures.

## Assumptions and scope
The graph is the simple geometric *line-intersection* graph, not the Néron–Severi lattice, the singular union-of-lines generalized Jacobian, or the Picard component group of a smoothing. The base characteristic is \(p\ge5\), and \(q=p^r\) can be any power; in particular the answer depends only on \(q\pmod8\). The graph has \(48\) vertices, \(336\) edges, is connected and \(14\)-regular. The classical description of all forty-eight lines is used, and the same incidence pattern holds for all stated characteristics.

Let \(\zeta\) be a primitive eighth root of unity over \(\bar k\), and label the lines \(\ell_{s,a,b}\) by \(s\in\{0,1,2\}\), \(a,b\in\{0,1,2,3\}\). The ordered coordinate pairings are
\[
P_0=((0,1),(2,3)),\quad P_1=((0,2),(1,3)),\quad P_2=((0,3),(1,2)).
\]
For \(P_s=((i,j),(h,l))\), the equations of \(\ell_{s,a,b}\) are \(x_i=\zeta^{2a+1}x_j\) and \(x_h=\zeta^{2b+1}x_l\). Frobenius sends each odd exponent \(e\) to \(qe\pmod8\), independently in the two positions, preserving the pairing index \(s\).

## Proof
**1. Geometric graph and Frobenius.** Two lines of one pairing family meet if one of their two exponents agrees. For families \(s<t\), writing \((a,b)\) and \((c,d)\) for their respective labels, exact elimination of their four linear equations gives the meeting criteria
\[
\begin{array}{c|l}
(s,t)&\text{congruence modulo }4\\\hline
(0,1)&a+d-c-b\equiv0\\
(0,2)&a+b+d+1-c\equiv0\\
(1,2)&a+b-c-d\equiv0.
\end{array}
\]
These follow because the relevant nonzero fourth/eighth roots of unity coincide exactly for equal exponents modulo eight. Each vertex has six neighbors in its own family and four in each other family. The supplied verifier independently confirms every one of the \(1128\) unordered adjacency decisions by testing the rank of the four defining line equations over three finite fields, as well as the resulting degree, edge count and connectedness. The relations are characteristic-independent for \(p\ge5\), not inferred solely from those three samples.

**2. Integral presentation.** Let \(L\) be the \(48\times48\) graph Laplacian. Choose any root vertex \(v_0\), put \(B=\mathbb Z^{\{v\ne v_0\}}\), and identify the degree-zero divisor lattice \(\operatorname{Div}^0(\Gamma)\) with \(B\) via the basis \(e_v-e_{v_0}\). Write \(R\) for the \(47\times47\) Laplacian obtained by deleting row and column \(v_0\). Then \(K(\Gamma)=\operatorname{coker}R\). If \(f_q\) is the Frobenius permutation of vertices, its action on the degree-zero basis is the integral matrix \(P_q\) with column \(v\) equal to the coordinates of \(e_{f_q(v)}-e_{f_q(v_0)}\). The coinvariants therefore have the exact rectangular presentation
\[
 K(\Gamma)_{F_q}=\operatorname{coker}\left[\,R\mid P_q-I\,\right].
\]
The critical group carries a canonical perfect symmetric pairing with values in \(\mathbb Q/\mathbb Z\), preserved by all graph automorphisms. Thus \(K(\Gamma)^{F_q}\) is canonically Pontryagin dual to \(K(\Gamma)_{F_q}\). In particular, the two finite abelian groups have identical invariant factors. This is a *finite integral* assertion; ordinary rational eigenspace dimensions do not suffice.

**3. Exact integral Smith computation.** The known full critical-group calculation gives
\[
 |K(\Gamma)|=2^{115}3^{28}5^6,\qquad \exp K(\Gamma)=5760.
\]
Every coinvariant is a quotient of this group. Consequently its Smith factors are supported only at primes \(2,3,5\), with valuation bounds \(7,2,1\) respectively. The standalone verifier constructs the matrix \([R\mid P_q-I]\) directly, and for each prime performs unimodular row and column reductions modulo \(2^9\), \(3^5\), or \(5^3\). At each step it chooses an entry of *minimum prime valuation*, moves it to the pivot position, makes that pivot divide its remaining row and column using invertible elementary operations, and removes the pivot row and column. As the modulus is larger than the maximum possible exponent, all valuations obtained are exact. This elementary modular algorithm calculates the local Smith factors without requiring a heuristic integer-matrix package.

The nonzero prime-primary Smith exponents and their multiplicities, omitting zero exponents, are:

| \(q\bmod8\) | prime 2 | prime 3 | prime 5 |
|---|---|---|---|
| 1 | \(2:12,3:5,6:8,7:4\) | \(1:26,2:1\) | \(1:6\) |
| 3 or 7 | \(1:3,2:4,4:3,5:2,6:4\) | \(1:11,2:1\) | \(1:3\) |
| 5 | \(1:1,2:12,4:5\) | \(1:14,2:1\) | \(1:6\) |

For each residue, sort the local prime-power factors and pad the shorter lists with unit factors at the beginning. Multiplying the corresponding prime powers gives exactly the invariant factors stated in the Finding. The calculation was separately repeated with root vertices numbered \(0,15,47\), yielding identical results. For \(q\equiv1\pmod8\), \(P_q=I\), so the calculation also reproduces the full previously published graph critical group. These independent consistency checks guard against an incorrect choice of divisor basis or Frobenius difference matrix.

## Verification
Run `python3 verify.py` using Python 3 and its standard library only; no data files or optional dependencies are needed. The verifier constructs all graph edges from symbolic congruences, independently checks the line-equation ranks over \(\mathbb F_{17}\), \(\mathbb F_{41}\), and \(\mathbb F_{73}\), proves the concrete graph is connected, builds Frobenius on degree-zero divisors, and determines all four local Smith systems with three independent reduced-Laplacian roots. Its expected final line is `FERMAT_48_LINE_FROBENIUS_FIXED_CRITICAL_GROUPS_OK`; the included `verification_output.txt` records the exact run. The finite-field rank checks verify the symbolic adjacency but are not substituted for the all-characteristic proof from the root-of-unity equations.

## Relationship to prior work
Schütt–Shioda–van Luijk establish the forty-eight-line configuration and the classical surface's Picard lattice. Shimada–Shioda describe the lines over the eighth-cyclotomic field and Galois action on the line configurations. A prior complete 48-line graph-critical-group computation establishes the *full* critical group and its order/exponent, and a separate mod-eight arithmetic Picard calculation determines rational divisor-span ranks. A further study computes the connected generalized Jacobian of the singular line union. None of these statements determines the finite **fixed subgroup of the graph critical group** for the three nonidentity Frobenius permutations: full abstract group type plus rational divisor traces do not determine the integral fixed subgroup, and the connected singular-curve Picard group is a different invariant. The published Frobenius-critical-group calculation for the Hermitian quartic in characteristic three concerns the different \(112\)-line graph. The standard perfect monodromy pairing is classical, not new. See the explicit claim-to-source comparisons in `AUDIT.json`.

## Limitations
The computation is confined to the distinguished forty-eight geometric Fermat-quartic lines in characteristics at least five. It makes no claim for the larger characteristic-three line configuration, arbitrary quartic surfaces or twists, integral Picard descent, a Néron component group, or the singular curve's connected generalized Jacobian. Exact numerical Smith decompositions are supplied with executable certificates rather than printed full matrices. Some specialized earlier computation not located in the inspected primary literature could contain an equivalent integral fixed-group table; historical priority is not independently certified. No independent mathematical audit has been carried out.

## References
1. M. Schütt, T. Shioda and R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377 (first public version December 12, 2008), https://arxiv.org/abs/0812.2377.
2. I. Shimada and T. Shioda, *On a smooth quartic surface containing 56 lines which is isomorphic as a K3 surface to the Fermat quartic*, arXiv:1604.06265 (first public version April 21, 2016), especially Section 3, https://arxiv.org/abs/1604.06265.
3. F. Shokrieh, *The monodromy pairing and discrete logarithm on the Jacobian of finite graphs*, arXiv:0907.4764 (first public version July 27, 2009), https://arxiv.org/abs/0907.4764.
4. *Critical group of the 48-line intersection graph on the complex Fermat quartic*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-critical-group-of-the-48-line-intersection-graph-on-the-complex--e6a8bff17712.
5. *The mod-eight arithmetic Picard diagram of the Fermat quartic and its line-class defect*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-mod-eight-arithmetic-picard-diagram-of-the-fermat-quartic-an--4c8353f211cf.
6. *The genus-289 Fermat quartic line divisor: integral torus and point-free arithmetic*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-genus-289-fermat-quartic-line-divisor-integral-torus-and-poi--0ec6abf1f810.
