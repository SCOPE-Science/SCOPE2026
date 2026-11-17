# Fixed symbolic entropy with tunable exact physical relaxation in a five-branch interval family

## Finding

A four-parameter open family of piecewise-affine, uniformly expanding five-branch interval maps retains one fixed topological entropy, but its absolutely continuous invariant density and its finite-time relaxation from Lebesgue initial data vary with branch geometry. All maps in this family have
\[
h_{\mathrm{top}}=\log\left(\frac{3+\sqrt{17}}2\right),
\]
while their nontrivial *step-density* transfer eigenvalue is exactly \(-q\), and every \(q\in(0,1/2)\) is realizable. The pushforward of normalized Lebesgue measure has an exact alternating transient, with total variation distance \(Cq^{n-1}\) at every integer \(n\ge1\), for an explicit nonnegative coefficient \(C\) that may vanish at special geometries. The metric entropy of the physical measure is strictly smaller than the common topological entropy except on a uniquely characterized one-dimensional constant-slope locus. The central distinction is quantitative: identical symbolic orbit growth does not constrain the physical mixing rate or the statistical entropy.

## Assumptions and scope

Choose \(0=c_0<c_1<c_2<c_3<c_4<c_5=1\) and positive branch lengths \(\ell_j=c_{j+1}-c_j\), \(j=0,\ldots,4\). Assume \(c_4>1/2\) and \(\ell_3<c_3\). On the open branch \(J_j=(c_j,c_{j+1})\) define
\[
F(x)=\frac{H_j(c_{j+1}-x)}{\ell_j},\qquad
H_j=\begin{cases}c_4,&j\in\{0,2,4\},\\c_3,&j\in\{1,3\}.\end{cases}
\]
The map's values at cuts can be assigned arbitrarily; all measure claims ignore their countable backward orbit. These assumptions make every branch slope magnitude strictly greater than one. Even-indexed branches cover \((0,c_4)\); odd-indexed branches cover \((0,c_3)\). The fifth branch feeds into the first four in one iterate, and receives no images of positive Lebesgue measure. Define
\[
E=\frac{\ell_0+\ell_2}{c_4},\quad d=\frac{\ell_3}{c_3},\quad q=Ed,
\quad A_*=(c_3+E\ell_3)^{-1},\quad D_*=EA_*.
\]
Then \(0<q<1/2\).

Let \(m\) be normalized Lebesgue measure on \((0,1)\). Write \(\rho_n\) for the density of \(F_*^n m\). Put
\[
A_1=\frac{\ell_0+\ell_2+\ell_4}{c_4}+\frac{\ell_1+\ell_3}{c_3},\qquad
D_1=\frac{\ell_0+\ell_2+\ell_4}{c_4}.
\]
The unique absolutely continuous invariant probability \(\mu\) has density \(\rho_*=A_*\) on \(J_0\cup J_1\cup J_2\), density \(D_*\) on \(J_3\), and zero on \(J_4\). For every integer \(n\ge1\),
\[
\begin{split}
\rho_n|_{J_0\cup J_1\cup J_2}&=A_*+(A_1-A_*)(-q)^{n-1},\\
\rho_n|_{J_3}&=D_*+(D_1-D_*)(-q)^{n-1},\\
\rho_n|_{J_4}&=0,\\
\|F_*^nm-\mu\|_{\mathrm{TV}}&=c_3|A_1-A_*|q^{n-1}.
\end{split}
\]
Here total variation is one half of the \(L^1\) distance of the densities.

More generally, any initial *piecewise-constant density* supported on the first four cells evolves under a two-dimensional matrix with eigenvalues \(1,-q\). No spectral assertion for arbitrary bounded-variation or smooth initial densities is made.

## Proof

**Transfer reduction and exact relaxation.** For a step-density vector \(f=(f_j)_{j=0}^4\), the Perron–Frobenius operator acts by the explicit finite transfer matrix
\[
(Wf)_i=\sum_{j=0}^4 \frac{\ell_j}{H_j}
{\bf1}_{\{i<4\text{ if }j\text{ even};\ i<3\text{ if }j\text{ odd}\}}f_j.
\]
Every image of a whole branch is a union of partition cells. After one iterate the vector has form \((A,A,A,D,0)\). A further iterate gives \((A',A',A',D',0)\), where
\[
\begin{pmatrix}A'\\ D'\end{pmatrix}
=\underbrace{\begin{pmatrix}1-q&d\\E&0\end{pmatrix}}_{T}
\begin{pmatrix}A\\D\end{pmatrix}.
\]
The identity \((\ell_0+\ell_2)/c_4+\ell_1/c_3=1-Ed\) follows by \(c_4=c_3+\ell_3\). The two eigenvalues of \(T\) are \(1\) and \(-q\); its positive eigenvector normalized by \(c_3A+\ell_3D=1\) is \((A_*,D_*)\). Applying \(W\) to the initial density \(f_j=1\) yields \(A_1,D_1\) as stated. The eigen-decomposition therefore proves the exact formula for \(\rho_n\). Conservation of total mass gives \(c_3(A_1-A_*)+\ell_3(D_1-D_*)=0\); hence the half-\(L^1\) difference is exactly \(c_3|A_1-A_*|q^{n-1}\).

**Uniqueness and topological entropy.** The four active cells form a primitive, uniformly expanding finite Markov system: their adjacency matrix is
\[
M=\begin{pmatrix}
1&1&1&1\\1&1&1&0\\1&1&1&1\\1&1&1&0
\end{pmatrix},\quad
\det(tI-M)=t^2(t^2-3t-2).
\]
The positive invariant step density is equivalent to Lebesgue measure on the recurrent core. Expansion and primitivity make this measure ergodic: at a density point of any invariant measurable set, shrinking Markov cylinders map affinely onto complete partition cells, forcing full measure there, and the primitive transitions propagate that conclusion to every core cell. An invariant absolutely continuous probability gives no mass to \(J_4\), as \(F^{-1}(J_4)\) has zero Lebesgue measure; ergodicity of the equivalent core measure then forces equality with \(\mu\). Markov-cylinder counts grow at the Perron root \(\lambda=(3+\sqrt{17})/2\), giving \(h_{\mathrm{top}}=\log\lambda\). The omitted transient fifth branch does not change exponential path growth.

**Every relaxation modulus.** To realize prescribed \(q_0\in(0,1/2)\), take \(c_4=4/5\), \(r=2q_0\), \(c_3=c_4/(1+r)\), and
\[
\ell_0=\ell_2=\left(\frac14+\frac{q_0}{2}\right)c_3,\quad
\ell_1=\left(\frac12-q_0\right)c_3,\quad
\ell_3=2q_0c_3,\quad \ell_4=1-c_4.
\]
These lengths are positive, have \(\ell_3<c_3\), and satisfy \(E=1/2\), \(d=2q_0\), thus \(q=q_0\). The decay factor is therefore not determined by topological entropy. When \(A_1=A_*\), the uniform initial ensemble happens to be stationary after one step even though the \(-q\) transfer eigenmode persists.

**Entropy-gap identity and equality locus.** For active states \(j,i\in\{0,1,2,3\}\), the physical stationary itinerary process has transition probabilities
\[
P_{ji}=\frac{\ell_i}{H_j}M_{ji},\quad
\pi_j=\begin{cases}\ell_jA_*,&j<3,\\\ell_3D_*,&j=3.\end{cases}
\]
The constancy of the invariant density on each cell and the affine branches prove this Markov property. Its metric entropy is
\[
h_\mu=-\sum_{j,i}\pi_jP_{ji}\log P_{ji}
=\int\log|F'(x)|\,d\mu(x).
\]
Let \(s=(\lambda-2)/2\) and \(v=(1,s,1,s)\), so \(Mv=\lambda v\). The maximal-entropy (Parry) Markov transition is \(Q_{ji}=M_{ji}v_i/(\lambda v_j)\). Stationarity cancels the \(\log v_i-\log v_j\) coboundary, yielding the exact nonnegative relative-entropy identity
\[
\log\lambda-h_\mu=\sum_j\pi_jD_{\mathrm{KL}}(P_{j\cdot}\Vert Q_{j\cdot}).
\]
All \(\pi_j\) are strictly positive, so equality requires \(P=Q\). Reading the even rows gives the necessary and sufficient conditions
\[
\ell_0=\ell_2=\frac{c_4}{\lambda},\qquad
\ell_1=\ell_3=\frac{s c_4}{\lambda},\qquad 1/2<c_4<1.
\]
Then the odd rows also equal \(Q\), and all four active slopes are \(\lambda\). Thus the maximal-entropy geometric locus is exactly the indicated one-parameter family. The general maximum-entropy principle and constant-slope criteria are established earlier mathematics; the result here is their explicit specialization combined with the independent exact relaxation law.

## Verification

A dependency-free `CHECK.py` implements the five-by-five transfer matrix with exact rational arithmetic. It checks the invariant density and exact signed transient for eleven successive times for the equal-partition example and ninety additional rational cut choices (1,001 exact total variation comparisons). Additional checks test the physical entropy versus the Parry-chain KL identity, three maximal-entropy geometries, and four prescribed relaxation factors. The successful output is:

`VERIFY_OK exact_transfer_cases=91 exact_tv=1001 entropy_KL_cases=90 parry_equality=3 tunable_rates=4`

These finite checks corroborate the algebra, not the infinitely quantified theorem. The proof above supplies the infinite-time statements and all-parameter quantifiers.

At the original equal-cut example \(\ell_j=1/5\), one obtains
\[
E=\tfrac12,\quad q=\tfrac16,\quad A_*=\tfrac{10}{7},\quad D_*=\tfrac57,
\quad\|F_*^nm-\mu\|_{\mathrm{TV}}=\frac1{140}\,6^{-(n-1)}.
\]
The physical entropy there is \((4/7)\log4+(3/7)\log3\), strictly below \(\log((3+\sqrt{17})/2)\).

## Relationship to prior work

Oliveira (2026), Section 9.4, introduces the five decreasing affine branches at equal cuts and computes their adjacency matrix and topological entropy; Sections 5.2 and 9.5 discuss entropy preservation under controlled changes. This finding does **not** claim those graph-entropy facts as new. It derives a full variable-cut family with exact physical invariant density, signed Lebesgue-ensemble relaxation and arbitrarily tunable transfer modulus at fixed entropy. Parry's maximal-entropy Markov measure, Lasota–Yorke's invariant-measure theory, and earlier maximal-ACIM slope criteria (Byers–Góra–Boyarsky) supply general conceptual background; their general entropy-maximization principle is not claimed as a new theorem here. The explicit 1990 slope-classification text was not fully accessible, creating residual priority risk for the specialized equality-locus subresult. The exact all-geometry physical relaxation statement is the main distinct result.

## Limitations

The map is discontinuous at cuts; equality of maps on cut values is irrelevant to almost-everywhere claims. The exact transient is proved for Lebesgue initial measure and the indicated finite-dimensional step-density subspace, **not** for arbitrary absolutely continuous measures, full transfer-operator spectral gaps, correlation decay or mixing rates in all function spaces. The leading amplitude can vanish for isolated geometries. Equality of metric and topological entropy uses only the unique absolutely continuous invariant probability; no classification of singular invariant measures is attempted. General historical priority and independent validation remain unestablished.

## References

- Henrique M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1 (first posted 2026-11-02), especially Sections 5.2 and 9.4; https://arxiv.org/html/2611.03287v1.
- W. Parry, *Intrinsic Markov chains*, Transactions of the American Mathematical Society 112 (1964), 55–66.
- W. Byers, P. Góra, A. Boyarsky, *Maximal absolutely continuous invariant measures for piecewise linear Markov transformations*, Ergodic Theory and Dynamical Systems 10 (1990), 645–656; https://doi.org/10.1017/S0143385700005824.
- A. Lasota and J. A. Yorke, *On the existence of invariant measures for piecewise monotonic transformations*, Transactions of the American Mathematical Society 186 (1973/74), 481–488.
