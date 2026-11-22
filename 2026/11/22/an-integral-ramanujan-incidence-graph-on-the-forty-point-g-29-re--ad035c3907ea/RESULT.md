# An integral Ramanujan incidence graph on the forty-point \(G_{29}\) reflection configuration

## Finding
Let \(Z_{29}\) be the forty reflection-normal points in \(\mathbb P^3_{\mathbb C}\) associated with the exceptional complex reflection group \(G_{29}\), regarded as the specified subconfiguration of the sixty-point Klein configuration. Let \(\mathcal L\) be its thirty distinguished Klein lines in projective three-space. Join two distinct points of \(Z_{29}\) when they lie on a common line in \(\mathcal L\). This geometrically defined graph is connected, nine-regular, and has 180 edges and adjacency spectrum

\[
\operatorname{Spec}(A)=\{9^{(1)},5^{(5)},1^{(15)},(-1)^{(4)},(-3)^{(15)}\}.
\]

It is consequently a nine-regular Ramanujan graph, and the point-line incidence matrix \(B\in\{0,1\}^{40\times30}\) has rank \(25\) over \(\mathbb Q\), with left and right nullities \(15\) and \(5\).

## Assumptions and scope
All geometry is over \(\mathbb C\). Coordinates are \([x_0:x_1:x_2:x_3]\). Put \(\mu_4=\{1,-1,i,-i\}\). The point set is exactly the union of (i) the twenty-four points with support \(\{a,b\}\), \(0\le a<b\le3\), whose two nonzero coordinates are \((1,\zeta)\), \(\zeta\in\mu_4\), and (ii) the sixteen points \([1:b:c:d]\), \(b,c,d\in\mu_4\) with \(bcd=1\). This reproduces the \(Z_{29}\) selection given in Section 3.1 of arXiv:2611.13108.

There are six coordinate lines \(x_a=x_b=0\). For each of the three partitions \(\{a,b\}\sqcup\{c,d\}=\{0,1,2,3\}\) with \(a<b,c<d\), take the eight lines \(x_a=\varepsilon x_b,\ x_c=\eta x_d\), with either \(\varepsilon,\eta\in\{1,-1\}\) or \(\varepsilon,\eta\in\{i,-i\}\). The resulting \(6+3\cdot8=30\) lines are the Klein lines listed in Section 3.2 of that source. Incidence means satisfaction of the two defining homogeneous linear equations, and the graph is simple.

## Proof
Define \(B_{P,L}=1\) precisely when the point \(P\) satisfies both equations for the line \(L\), and \(0\) otherwise. Direct evaluation of the stated finite coordinate sets gives: each point lies on exactly three Klein lines; each line contains exactly four points of \(Z_{29}\); and any distinct two points share at most one of these lines. Thus
\[
BB^{\mathsf T}=3I_{40}+A,
\]
where \(A\) is a symmetric zero-diagonal, zero-one matrix. Every row of \(A\) has sum \(3(4-1)=9\), so the graph has \(40\cdot9/2=180\) edges.

To certify the full spectrum without a floating-point eigensolver, construct \(A\) by the coordinate rules and verify the exact integer polynomial identity
\[
(A-9I)(A-5I)(A-I)(A+I)(A+3I)=0.
\]
The exact integer traces \((\operatorname{tr}(A^k))_{k=0}^4\) are
\[
(40,0,360,960,10920).
\]
Because \(A\) is real symmetric, its eigenvalues belong to the five distinct real roots of the displayed annihilating polynomial. Solving the five Vandermonde trace equations \(\sum_j m_j\lambda_j^k=\operatorname{tr}(A^k)\), for \(0\le k\le4\), gives uniquely multiplicities \((1,5,15,4,15)\) at eigenvalues \((9,5,1,-1,-3)\). The multiplicity-one eigenvalue \(9\) proves connectedness. All other eigenvalues have absolute value at most \(5<2\sqrt{8}\), proving the Ramanujan property. Since \(BB^{\mathsf T}=A+3I\), its nullity is fifteen and hence \(\operatorname{rank}_{\mathbb Q}B=40-15=25\); the right nullity is \(30-25=5\).

## Verification
Run `python3 g29_incidence_check.py` with a standard Python 3 installation; no additional modules are needed. The script reconstructs all forty points over the Gaussian integers, all thirty lines, the complete incidence matrix, and verifies the claimed incidence counts, matrix annihilator, trace vector and forced eigenvalue multiplicities by exact integer arithmetic. The finite exhaustive computation is a proof because the coordinate lists completely specify the finite objects; it is not a sample of an unbounded family.

## Relationship to prior work
Hanumanthu–Huizenga–Kettinger–Merta–Szemberg–Szpond (2026), Sections 3.1–3.2, gives the exact forty-point subgroup selection and thirty-line geometry, including three lines through each point and four selected points on every line. Pokora–Szemberg–Szpond (2020/2022), Section 2, develops the parent sixty-point/thirty-line Klein configuration and its applications to unexpected surfaces and geproci properties. Neither work, in the material checked, states the point-collinearity spectral factorization, the associated incidence-matrix rank, or the Ramanujan property. The rank and spectrum sharpen the source's cardinality information with exact information on rational linear dependencies and spectral expansion.

## Limitations
This theorem concerns the specified finite point-line system, not the full sixty-point collinearity graph or other possible reflection subconfigurations. It does not classify all graphs with the displayed spectrum or claim uniqueness. No mathematical consequences for Waldschmidt constants or symbolic-power containments are proved here. Published priority beyond the inspected sources is subject to unindexed literature.

## References
1. K. Hanumanthu, J. Huizenga, J. Kettinger, Ł. Merta, T. Szemberg, J. Szpond, *Waldschmidt constants and invariant geometry for exceptional rank-four complex reflection groups* (2026), arXiv:2611.13108v1, https://arxiv.org/abs/2611.13108.
2. P. Pokora, T. Szemberg, J. Szpond, *Unexpected properties of the Klein configuration of 60 points in \(\mathbb P^3\)*, arXiv:2010.08863v2, https://arxiv.org/abs/2010.08863.
