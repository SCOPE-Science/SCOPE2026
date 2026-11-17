# An effective-resistance distance law reconstructs every finite metric bouquet

## Finding

An **unlabelled, two-point electrical-resistance distribution** uniquely determines all the edge lengths of a finite bouquet of metric circles. No labels, individual resistance measurements, generic-position assumption, or a priori knowledge of the number of loops is required. Moreover, a finite jet of its Laplace transform at large positive argument suffices.

**Theorem.** Let \(m\ge1\) be a finite integer, and let \(\boldsymbol\ell=(\ell_1,\ldots,\ell_m)\) have arbitrary positive real entries. Identify one point of each circle of circumference \(\ell_i\) to a single common junction, obtaining a compact metric graph \(G_{\boldsymbol\ell}\). Give its edges unit resistance per unit arclength. Independently choose \(X,Y\) from its normalized arclength measure and set \(R=r_G(X,Y)\), where \(r_G\) is effective electrical resistance. Then the probability law of \(R\) determines \(m\) and the multiset of lengths \(\{\ell_i\}_{i=1}^m\), including multiplicities. Thus it determines the bouquet up to isometry. Specifically, the first \(m+2\) coefficients of the large-argument asymptotic expansion of \(\mathbb E[e^{-sR}]\) suffice; \(m\) itself is obtained from the first two.

Write \(L=\sum_i\ell_i\), \(\varphi(t)=\int_0^1e^{-tu(1-u)}du\), and \(\mathcal L(s)=\mathbb E[e^{-sR}]\). The exact distributional identity is

\[
L^2\mathcal L(s)=\sum_{i=1}^{m}\ell_i^2\varphi(s\ell_i)+\sum_{i\ne j}\ell_i\ell_j\varphi(s\ell_i)\varphi(s\ell_j),\qquad s\ge0.
\]

The asymptotic expansion is understood term-by-term: for each fixed integer \(N\ge1\), its truncation after \(N\) terms has a remainder \(O(s^{-N-1})\) as \(s\to\infty\), with constants depending on the fixed finite graph.

## Assumptions and scope

Each loop has strictly positive finite metric length and a uniform, linear resistance density (the electrical resistance of an arc equals its length). Every point, not just the vertices, is sampled according to arclength; pairs are independent. Multiple loops may have equal lengths. The observable is the **exact population probability distribution** of a single pairwise resistance; the observer does not see which loops contain the points. The topology is assumed to be a finite bouquet, although \(m\) is unknown. Isometry treats permutations of loops as immaterial.

The metric graph is viewed as a continuous electrical network. The self-resistance of a point is zero and has zero probability in the sampling model. Effective resistance here is distinct from shortest-path (geodesic) distance: on a single loop the former combines the two arcs in parallel.

## Proof

**1. Series–parallel reduction and exact Laplace identity.** Parameterize loop \(i\) by the fractional arclength \(u\in[0,1)\) from the junction. The effective resistance from the junction to that point is

\[
q_i(u)=\frac{(\ell_i u)(\ell_i(1-u))}{\ell_i}=\ell_i u(1-u).
\]

For two points on the same loop, with circle-separation arclength \(d\), the two complementary arcs are parallel, so their resistance is \(d(\ell_i-d)/\ell_i\). All other loops are attached only to the junction and carry no current between these terminals. If two points lie on *different* loops, their resistances to the junction are in series and add, since each loop is otherwise linked to the remainder only at this junction. Conditional on belonging to a given loop, the fractional coordinate is uniform. The difference modulo one of two independent uniform fractional coordinates is uniform, hence the conditional same-loop resistance is distributed as \(\ell_i U(1-U)\). For different loops it is distributed as \(\ell_i U(1-U)+\ell_jV(1-V)\), with independent uniform \(U,V\). The ordered loop-index sampling weights are \(\ell_i\ell_j/L^2\). Therefore the displayed exact identity follows, including the ordered cross terms. This also proves normalization \(\mathcal L(0)=1\).

**2. Universal Laplace coefficients.** For \(Z=U(1-U)\), change variables on both inverse branches of the quadratic map to obtain its density

\[
f_Z(z)=\frac{2}{\sqrt{1-4z}}\,\mathbf1_{0<z<1/4}.
\]

Near zero its absolutely convergent power series is

\[
\frac{2}{\sqrt{1-4z}}=2\sum_{j=0}^{\infty}{2j\choose j}z^j\quad(0\le z<1/4).
\]

For every fixed \(N\), split the Laplace integral at any fixed \(0<\varepsilon<1/4\). On the first interval use the Taylor series through degree \(N-1\) with a uniform remainder \(O(z^N)\); on the second interval exponential decay dominates the integrable square-root endpoint singularity. Termwise integration of the Taylor polynomial using \(\int_0^\infty e^{-tz}z^j\,dz=j!t^{-j-1}\) gives

\[
\varphi(t)=\sum_{k=1}^N\frac{c_k}{t^k}+O(t^{-N-1}),\qquad
c_k=\frac{2(2k-2)!}{(k-1)!}>0.
\]

Each fixed loop length is positive, so this expansion can be substituted into the finite sum and products in the exact identity. Thus every coefficient \(A_k\) of \(\mathcal L(s)\) exists uniquely and can be recovered recursively from the law by successive limits:

\[
A_1=\lim_{s\to\infty}s\mathcal L(s),\qquad
A_k=\lim_{s\to\infty}s^k\left(\mathcal L(s)-\sum_{j=1}^{k-1}A_js^{-j}\right).
\]

**3. Recovering total length and number of loops.** Set \(H_0=m\) and \(H_j=\sum_i\ell_i^{-j}\) for positive integers \(j\). Note \(c_1=2\) and \(c_2=4\). Coefficient extraction gives

\[
A_1=\frac{2}{L},\qquad A_2=\frac{4m^2}{L^2}.
\]

Hence \(L=2/A_1\) and, since \(m\ge1\), \(m=(L/2)\sqrt{A_2}\). In particular there is no possibility of a sign ambiguity in recovering the number of loops.

**4. Triangular recurrence recovering reciprocal length moments.** For every \(k\ge3\), expanding products of the two series yields

\[
\begin{aligned}
L^2A_k
&=c_kH_{k-2}+\sum_{p=1}^{k-1}c_pc_{k-p}
\left(H_{p-1}H_{k-p-1}-H_{k-2}\right)\\
&=D_kH_{k-2}+\sum_{p=2}^{k-2}c_pc_{k-p}H_{p-1}H_{k-p-1},
\end{aligned}
\]

with the **known** positive scalar

\[
D_k=c_k+2c_1c_{k-1}(m-1)-\sum_{p=2}^{k-2}c_pc_{k-p}.
\]

An empty sum is zero. The crucial point is that \(D_k>0\) for all \(m\ge1\), \(k\ge3\), *without any genericity condition*. For an elementary proof define \(a_j=(2j)!/j!\) for integers \(j\ge0\). Then \(c_p=2a_{p-1}\) and, for every \(0\le j\le n\),

\[
\frac{a_j a_{n-j}}{a_n}=\frac{{n\choose j}}{{2n\choose2j}}\le1.
\]

The last inequality follows by injecting subsets of \(j\) among \(n\) pairs into subsets of \(2j\) among \(2n\) elements: retain both elements of each selected pair. For \(k\ge4\), taking \(n=k-2\) shows

\[
\sum_{p=2}^{k-2}c_pc_{k-p}
=4\sum_{p=2}^{k-2}a_{p-1}a_{k-p-1}
\le4(k-3)a_{k-2}.
\]

Since \(c_k=2a_{k-1}=2(4k-6)a_{k-2}\) and \(2c_1c_{k-1}(m-1)\ge0\), it follows that

\[
D_k\ge 4k\,a_{k-2}>0 \quad(k\ge4).
\]

For \(k=3\), direct evaluation yields \(D_3=16m+8>0\). Hence the recurrence solves uniquely for \(H_{k-2}\) once the lower \(H_j\)'s are known. Specifically, \(A_3,\ldots,A_{m+2}\) recursively determine \(H_1,\ldots,H_m\). For example, \(H_1=L^2 A_3/(16m+8)\).

**5. Finite moment inversion and rigidity.** Put \(z_i=1/\ell_i>0\). The recovered \(H_j=\sum_i z_i^j\) are the first \(m\) power sums of the unknown \(m\) roots. Let \(e_0=1\) and recursively define

\[
e_j=\frac1j\sum_{p=1}^j(-1)^{p-1}e_{j-p}H_p\quad(1\le j\le m).
\]

Newton's identities show that these are the elementary symmetric polynomials in \(z_1,\ldots,z_m\). Therefore the monic polynomial

\[
P(z)=z^m-e_1z^{m-1}+e_2z^{m-2}-\cdots+(-1)^m e_m
=\prod_{i=1}^m(z-z_i)
\]

is determined exactly. Its multiset of positive roots, including repetitions, is thus determined. Taking reciprocals recovers all the loop lengths. Two different bouquets cannot have the same pairwise effective-resistance distribution; conversely a loop-length multiset determines the bouquet and its law. This completes the proof.

## Verification

The standalone standard-library Python program `checker.py` independently computes exact rational formal Laplace coefficients, recursively recovers the polynomial by Newton identities, and checks it against directly multiplied root polynomials. It executed successfully for 301 explicit or pseudorandom configurations, from one to eight loops, including repeated lengths. Numerical quadrature of the exact Laplace formula was compared against independent double-mesh integrations over endpoint pairs (12 cases), and simulation means were compared with the independently derived moment identity

\[
\mathbb E[R]=\frac{2L\sum_i\ell_i^2-\sum_i\ell_i^3}{6L^2}.
\]

An auxiliary finite arithmetic check tests the coefficient inequality over a range of indices; the inequality for all integers is proved analytically above, not inferred from these checks. The execution reported `RESISTANCE_BOUQUET_INVERSE_CHECKS_OK 301 coefficients, 12 quadrature comparisons`. Run with `python checker.py` using Python 3 and no third-party packages. These checks corroborate, but do not replace, the exact proof.

## Relationship to prior work

Baker and Faber [1] establish the electrical-network framework for metrized graphs, including series/parallel resistance formulas. This paper is the earliest dated foundational source used here; **the formulas themselves are not claimed as new**. Baptista, Kennedy and Mugnolo [2] study **shortest-path** mean distance and flower-graph optimization rather than the distribution of effective resistance or inverse recovery from one unlabelled two-point law. Faught, Kempton and Knudson [3] investigate finite-vertex resistance and Kirchhoff/Kemeny invariants for a different cyclicly glued family also called *flower graphs*; their graph construction and observable are distinct. Weihrauch [4] characterizes a graph from a fully **labelled resistance metric**, which does not directly recover a graph from one aggregate scalar distribution on a continuous space. The contribution here is the explicit Laplace-coefficient reconstruction for finite single-junction metric bouquets, including exact treatment of all multiplicities.

## Limitations

The theorem assumes the combinatorial class of finite single-vertex bouquets; it does not claim that arbitrary metric graphs are characterized by two-point resistance distributions. The source measure is normalized arclength, and the resistance density is uniform. There is no proved quantitative stability estimate from noisy observations or finite random samples: recursively extracting large-argument asymptotic coefficients may be ill-conditioned. Historical priority is provisional and remains subject to specialist scrutiny of inverse resistance-metric and network tomography literature. Independent mathematical and historical validation has not been performed.

## References

[1] M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, first public 2004-07-25; https://arxiv.org/abs/math/0407428 .

[2] L. N. Baptista, J. B. Kennedy and D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952, first public 2023-12-08; https://arxiv.org/abs/2312.04952 .

[3] N. Faught, M. Kempton and A. Knudson, *Resistance distance, Kirchhoff index, and Kemeny's constant in flower graphs*, arXiv:2007.03103, first public 2020-07-06; https://arxiv.org/abs/2007.03103 .

[4] T. Weihrauch, *A Characterization of Effective Resistance Metrics*, arXiv:1710.01587, first public 2017-10-04; https://arxiv.org/abs/1710.01587 .
