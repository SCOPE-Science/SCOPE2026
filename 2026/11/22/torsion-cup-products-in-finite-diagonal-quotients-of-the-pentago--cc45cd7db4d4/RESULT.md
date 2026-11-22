# Torsion cup products in finite diagonal quotients of the pentagonal moment-angle manifold

## Finding
Let \(K=C_5\) denote the abstract simplicial complex consisting of the vertices and edges of a pentagon. Write \(X=\mathcal Z_K=(D^2,S^1)^K\), with its coordinatewise \((S^1)^5\)-action. For an integer \(m\ge2\), let \(\mu_m\) multiply all five complex coordinates by the same \(m\)-th root of unity, and define \(Y_m=X/\mu_m\). The quotient is a closed, orientable, smooth seven-manifold and

\[
\pi_1(Y_m)\cong\mathbb Z/m\mathbb Z,\qquad
H^j(Y_m;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,7,\\
\mathbb Z/m\mathbb Z,&j=2,6,\\
\mathbb Z^5,&j=3,4,\\
0,&\text{otherwise}.
\end{cases}
\]

Let \(\tau\) denote an integral generator of \(H^6(Y_m;\mathbb Z)=\mathbb Z/m\mathbb Z\). There exist primitive classes \(a_1,b_1,a_2,b_2\in H^3(Y_m;\mathbb Z)\), a torsion generator \(u\in H^2(Y_m;\mathbb Z)\) and a primitive \(v\in H^4(Y_m;\mathbb Z)\), with
\[
a_i\smile b_j=\delta_{ij}\tau,\quad a_i\smile a_j=b_i\smile b_j=0,\quad
u\smile v=\tau,\quad u^2=0.
\]
The three-dimensional classes are free integral classes; their products give nonzero order-\(m\) torsion.

## Assumptions and scope
The simplicial complex is the **boundary of the ordinary five-gon**, not a five-vertex filled disk or a real moment-angle surface. Every \(\sigma\in K\) has at most two vertices. The moment-angle space is the union of products with coordinates in \(D^2\) on \(\sigma\) and \(S^1\) on its complement. The only symmetry being quotiented is simultaneous complex scalar multiplication by \(\mu_m\); **not** permutation or reflection of polygon vertices. The integer \(m\) can be composite. All cohomology groups and products use integral coefficients.

## Proof
**1. The covering manifold.** Standard moment-angle manifold theory gives that \(X\) is a smooth, closed, connected, orientable seven-manifold and is two-connected. The Hochster decomposition (or the classical five-gon connected-sum computation) gives
\[
H^j(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,& j=0,7,\\
\mathbb Z^5,&j=3,4,\\
0,&\text{otherwise}.
\end{cases}
\]
For an independent finite check: for each \(J\subseteq\{0,1,2,3,4\}\) the induced subcomplex \(K_J\) is a graph. Hochster's formula places \(\widetilde H^q(K_J;\mathbb Z)\) in cohomological degree \(q+|J|+1\). The empty subset contributes one class in degree zero, the five disconnected pairs contribute five classes in degree three, the five disconnected triples contribute five classes in degree four, and the entire pentagon contributes the top degree-seven class. No other induced graph has reduced homology. Every summand is torsion-free.

**2. The intermediate circle quotient.** The diagonal circle \(S^1\) acts freely on \(X\): outside any \(\sigma\in K\), at least three coordinates lie on \(S^1\), so a scalar fixing the point must be the identity. Put \(B=X/S^1\), and let \(e\in H^2(B;\mathbb Z)\) be the Euler class of the oriented principal-circle bundle \(S^1\to X\to B\). The space \(B\) is a closed orientable smooth six-manifold. The homotopy exact sequence, together with \(\pi_1(X)=\pi_2(X)=0\), gives \(\pi_1(B)=0\) and \(\pi_2(B)=\mathbb Z\). Hurewicz and Poincaré duality imply \(H^2(B)=H^4(B)=\mathbb Z\), \(H^5(B)=0\), \(H^6(B)=\mathbb Z\). The same homotopy sequence, or the Gysin sequence in degree two, shows that \(e\) generates \(H^2(B)\).

The Gysin sequence in degree three identifies the free subgroup \(H^3(B)\subseteq H^3(X)=\mathbb Z^5\) as the kernel of the exact sequence
\[
0\longrightarrow H^3(B)\longrightarrow\mathbb Z^5
\longrightarrow H^2(B)\xrightarrow{\smile e}H^4(B).
\]
If \(e^2\ne0\), the last map between rank-one free groups would be injective, forcing \(\operatorname{rank}H^3(B)=5\). This is impossible: the torsion-free middle cohomology of an oriented closed six-manifold has a nondegenerate integral skew-symmetric Poincaré pairing, hence even rank. Therefore \(e^2=0\), the rank of \(H^3(B)\) is four, and its skew pairing is unimodular. Also, the Gysin sequence in degree five gives that multiplication \(e:H^4(B)\to H^6(B)\) is an isomorphism: \(H^5(X)=H^6(X)=0\). Fix a generator \(b\in H^4(B)\) with \(e\smile b=[B]^*\), a preferred top-cohomology generator. Choose a symplectic basis \(\alpha_1,\beta_1,\alpha_2,\beta_2\) of \(H^3(B)\), so that \(\alpha_i\smile\beta_j=\delta_{ij}[B]^*\) and each same-type product vanishes.

**3. The finite quotient and its Gysin sequence.** Since \(\mu_m\) is a subgroup of the free diagonal circle, \(Y_m\) is the total space of an oriented principal circle bundle \(S^1/\mu_m\to Y_m\xrightarrow{\pi}B\). Under the identification \(S^1/\mu_m\cong S^1\) by \(z\mu_m\mapsto z^m\), its Euler class is \(m e\). The only potentially nonzero cup maps by \(m e\) among free groups on \(B\) are multiplication by \(m\) in degrees \(H^0(B)\to H^2(B)\) and \(H^4(B)\to H^6(B)\); the map \(H^2(B)\to H^4(B)\) is zero. The integral Gysin sequence therefore gives all the displayed cohomology groups, with \(H^3(Y_m)\) and \(H^4(Y_m)\) both free rank five. In particular, the pullbacks of \(H^3(B)\) and \(H^4(B)\) are primitive sublattices, and \(\pi^*[B]^*\) generates \(H^6(Y_m)=\mathbb Z/m\mathbb Z\). By the covering \(X\to Y_m\) and simple connectivity of \(X\), the fundamental group is \(\mu_m\cong\mathbb Z/m\mathbb Z\).

**4. Nonzero torsion cup products.** Define \(\tau=\pi^*[B]^*\), \(u=\pi^*e\), \(v=\pi^*b\), \(a_i=\pi^*\alpha_i\), and \(b_i=\pi^*\beta_i\). Functoriality of the cup product gives \(u\smile v=\tau\), \(u^2=\pi^*(e^2)=0\), and \(a_i\smile b_j=\delta_{ij}\tau\) with the other stated products zero. All required classes have the asserted orders and primitivity by the Gysin exact sequences.

## Verification
The accompanying self-contained `verify.py` enumerates all 32 vertex subsets of the pentagon and computes the reduced cohomology of each induced graph. It reproduces the exact Hochster Betti vector \((1,0,0,5,5,0,0,1)\), then checks example integers in the formal Gysin-group formulas. Its success marker is `PENTAGON_HOCHSTER_AND_GYSIN_INPUTS_OK`. The infinite family and cup products are justified by the preceding exact-sequence and Poincaré-duality proof, **not** by finitely many integer tests. No claim is made about a homeomorphism classification of the seven-manifolds \(Y_m\).

## Relationship to prior work
The topology of \(X\) follows the classical moment-angle and polygonal connected-sum literature, including Gitler–López de Medrano and Fan–Chen–Ma–Wang. Panov gives an integral cohomology framework for quotients by connected freely acting subtori; Franz extends multiplicative computations to arbitrary freely acting closed subgroups, and Limonchenko–Solomadin describe general closed-subgroup orbit spaces via toric homotopy colimits. Those general tools are broader in coverage, but the inspected texts do not explicitly calculate the five-gon **finite diagonal** quotients' integral cohomology and the specific free-to-torsion cup products proved here. Published dihedral **vertex-permutation** results study different group actions. The present proof independently derives the stated special family from the circle Gysin sequence, including the parity obstruction \(e^2=0\).

## Limitations
This result is not a classification of all polygonal moment-angle quotients, of all finite torus subgroups, or of the complete homotopy types of \(Y_m\). Existing general quotient-cohomology machinery may allow another derivation of the same computation; publication priority beyond the inspected sources is not certified. The finite verifier independently checks only the underlying Hochster ranks and sample group orders; the infinite-family conclusion relies on the full written proof.

## References
- Samuel Gitler and Santiago López de Medrano, *Intersections of Quadrics, Moment-angle Manifolds and Connected Sums*, first public 2009-01-16, https://arxiv.org/abs/0901.2580.
- Feifei Fan, Liman Chen, Jun Ma, Xiangjun Wang, *Moment-angle manifolds and connected sums of sphere products*, first public 2014-06-30, https://arxiv.org/abs/1406.7591.
- Taras Panov, *On the cohomology of quotients of moment-angle complexes*, first public 2015-06-23, https://arxiv.org/abs/1506.06875.
- Matthias Franz, *The cohomology rings of smooth toric varieties and quotients of moment-angle complexes*, first public 2019-07-10, https://arxiv.org/abs/1907.04791.
- Ivan Limonchenko and Grigory Solomadin, *On the homotopy decomposition for the quotient of a moment-angle complex and its applications*, first public 2022-02-28, https://arxiv.org/abs/2202.13899.
