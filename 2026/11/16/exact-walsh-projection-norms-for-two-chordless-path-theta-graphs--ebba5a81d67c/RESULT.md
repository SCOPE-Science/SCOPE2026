# Exact Walsh projection norms for two-chordless-path theta graphs

## Finding
For integers \(a,b\ge 2\), let \(\Theta_{a,b}\) be the simple graph consisting of two internally vertex-disjoint paths of lengths \(a\) and \(b\) between the same endpoints, together with the direct edge joining those endpoints. Write \(E=E(\Theta_{a,b})\), so \(|E|=a+b+1\), and let \(\mathcal T_{a,b}\subseteq\mathbb F_2^E\) consist of the incidence vectors of all spanning trees. Let \(P_{a,b}\) be the Fourier multiplier on functions on \(\mathbb F_2^E\) whose multiplier is the indicator of \(\mathcal T_{a,b}\). Define
\[
c_n=2^{-n}\binom n{\lfloor n/2\rfloor},\qquad \epsilon_n=\begin{cases}0&n\text{ even},\\1&n\text{ odd}.\end{cases}
\]
Then the exact sharp endpoint norms are
\[
\boxed{\|P_{a,b}\|_{\ell^1\to\ell^1}=\|P_{a,b}\|_{\ell^\infty\to\ell^\infty}
=(ab+a+b)c_ac_b+\epsilon_ac_a+\epsilon_bc_b-\epsilon_a\epsilon_bc_ac_b.}
\]
The full Fourier support of \(\mathbf1_{\mathcal T_{a,b}}\) has cardinality \(2^{a+b+1}-Z_{a,b}\), where
\[
\boxed{Z_{a,b}=\begin{cases}
0,&\text{if at least one of }a,b\text{ is odd},\\
2\left[\binom a{a/2}\binom b{b/2}+\binom a{a/2-1}\binom b{b/2-1}\right],&\text{if both are even}.
\end{cases}}
\]
Thus convolution by \(\mathbf1_{\mathcal T_{a,b}}\) on the Boolean edge group is invertible exactly when at least one path length is odd. When \(a=b=n\) tends to infinity through even or odd integers respectively, the exact norms have the distinct expansions
\[
\begin{aligned}
L_{n,n}&=\frac{2n}{\pi}+\frac3\pi+O(n^{-1})&&\text{(even }n\text{)},\\
L_{n,n}&=\frac{2n}{\pi}+\frac1\pi+2\sqrt{\frac{2}{\pi n}}+O(n^{-1})&&\text{(odd }n\text{)}.
\end{aligned}
\]

## Assumptions and scope
All edge sets are labeled, and all graphs here are finite simple graphs: \(a,b\ge2\) avoids duplicate copies of the direct edge. The two paths meet only at the two endpoints. The Boolean group \(\mathbb F_2^E\) is the set of all edge subsets with symmetric-difference addition. Its characters are \(\chi_z(x)=(-1)^{\sum_{e\in E}z_ex_e}\). Functions and Fourier multipliers are complex-valued; endpoint \(\ell^p\) norms use counting measure. The unnormalized Walsh transform is \(\widehat f(z)=\sum_x f(x)\chi_z(x)\). All equalities hold separately for every integer pair \(a,b\ge2\), with no parity or asymptotic restriction.

## Proof
**1. Tree parameterization and Fourier transform.** The graph has \(a+b\) vertices and \(a+b+1\) edges. A spanning tree therefore omits exactly two edges. Necessarily the omitted edges lie on two different paths among the three terminal-to-terminal paths: otherwise one complete cycle remains, or an internal path segment is disconnected. Conversely, removing one edge from each of two distinct paths gives a connected acyclic spanning subgraph. In particular, there are exactly \(ab+a+b\) spanning trees.

For any \(z\in\mathbb F_2^E\), write \(s_e=(-1)^{z_e}\), let \(X\) and \(Y\) be the sums of these signs on the respective paths, let \(\delta\in\{-1,1\}\) be the sign on the direct edge, and let \(\Sigma=\prod_{e\in E}s_e\). The preceding tree description yields the exact identity
\[
\widehat{\mathbf1_{\mathcal T_{a,b}}}(z)=\Sigma\bigl(XY+\delta(X+Y)\bigr).
\tag{1}
\]
Indeed, the sign product along a retained tree equals \(\Sigma\) times the signs of its two omitted edges, because signs are their own inverses.

**2. From the Walsh transform to the sharp norm.** The multiplier \(P_{a,b}\) is convolution by
\[
K(z)=2^{-(a+b+1)}\widehat{\mathbf1_{\mathcal T_{a,b}}}(z).
\]
The \(\ell^1\) and \(\ell^\infty\) operator norms of a convolution on a finite group both equal the \(\ell^1\) norm of its kernel. The upper bound is Young's inequality; point-mass input establishes equality for \(\ell^1\), and an input with phases aligned to the coefficients of the kernel establishes equality for \(\ell^\infty\). Thus the common sharp norm is the expectation of \(|XY+\delta(X+Y)|\), where the \(a+b+1\) edge signs are independent uniform Rademacher variables. Averaging over \(\delta\) gives
\[
L_{a,b}=\mathbb E\,\max\bigl\{|XY|,|X+Y|\bigr\},
\tag{2}
\]
using \((|u+v|+|u-v|)/2=\max\{|u|,|v|\}\) for real \(u,v\).

**3. Exact expectation.** For integers \(x,y\), the difference between the maximum in (2) and \(|xy|\) is precisely
\[
|y|\mathbf1_{\{x=0\}}+|x|\mathbf1_{\{y=0\}}
+\mathbf1_{\{xy>0,\;\min(|x|,|y|)=1\}}.
\tag{3}
\]
To see this, if one variable vanishes the assertion is immediate. If both are nonzero with opposite signs, \(|x+y|\le|xy|\); if they have the same sign then the positive difference is \(\max\{0,|x|+|y|-|xy|\}\), which is one exactly when at least one integer magnitude is one and zero otherwise. This checks all integer boundary cases.

Let \(S_n\) denote a sum of \(n\) independent Rademacher variables, and put \(u_n=\mathbb E|S_n|\), \(z_n=\Pr(S_n=0)\), and \(p_n=\Pr(S_n=1)\). Symmetry and the binomial distribution give
\[
z_n=(1-\epsilon_n)c_n,\quad p_n=\epsilon_nc_n,\quad u_n=(n+\epsilon_n)c_n.
\tag{4}
\]
The last identity follows either by telescoping the binomial coefficients or inductively from \(\mathbb E|S_{n+1}|-\mathbb E|S_n|=\Pr(S_n=0)\), with \(u_0=0\). Independence and symmetry show that the expectation of the last indicator in (3) is
\[
p_a(1-z_b)+p_b(1-z_a)-2p_ap_b.
\]
Here the intersection was counted twice and consists of the two same-sign configurations where both magnitudes are one. Therefore
\[
L_{a,b}=u_au_b+z_au_b+z_bu_a+p_a(1-z_b)+p_b(1-z_a)-2p_ap_b.
\]
Substituting (4), and reducing by the four parity possibilities, gives the boxed formula. In particular, for both even the answer is \((ab+a+b)c_ac_b\); for \(a\) even and \(b\) odd it is \((ab+a+b)c_ac_b+c_b\); for both odd it is \((ab+a+b-1)c_ac_b+c_a+c_b\). This completes the exact norm proof.

**4. Exact Fourier zeros.** Equation (1) vanishes precisely when
\[
(X+\delta)(Y+\delta)=1.
\]
Since both factors are integers, they are both \(1\) or both \(-1\). Hence for \(\delta=1\) the solutions are \((X,Y)=(0,0),(-2,-2)\), and for \(\delta=-1\) they are \((X,Y)=(0,0),(2,2)\). If either path length is odd, none can occur. For both even, the number of sign assignments producing \(X=0\) is \(\binom a{a/2}\), and those producing \(X=\pm2\) are counted by \(\binom a{a/2-1}\), with the analogous formulas for \(Y\). Summing over both direct-edge signs proves the stated \(Z_{a,b}\). The eigenvalues of convolution by the tree indicator are its Walsh transform, so it is invertible if and only if \(Z_{a,b}=0\).

**5. Parity-dependent asymptotics.** For even \(n\), \(c_n=\sqrt{2/(\pi n)}\,[1-1/(4n)+O(n^{-2})]\), so the exact expression \(L_{n,n}=(n^2+2n)c_n^2\) yields the stated even expansion. For odd \(n\), \(c_n=\binom{n+1}{(n+1)/2}/2^{n+1}\), and the exact expression \(L_{n,n}=(n^2+2n-1)c_n^2+2c_n\) yields the stated odd expansion by the same central-binomial expansion. No numerical limit inference is used.

## Verification
The standalone standard-library script `check_theta.py` constructs each graph independently, enumerates all size-\((a+b-1)\) connected edge sets using a union-find test, forms their indicator vector, and applies an independent integer Walsh–Hadamard transform. It checks the complete coefficient identity (1), exact tree count, boxed norm, and nonzero Fourier support. Its default tests cover every ordered pair \(2\le a,b\le6\) with \(a+b\le11\), a total of 24 graph instances, with up to \(2^{12}\) Fourier coefficients each. The successful marker is `THETA_ALL_WALSH_CERTIFICATES_PASS 24`. These checks corroborate the proof, which establishes the unrestricted parameters.

## Relationship to prior work
Goodall's survey of Fourier analysis on finite abelian groups gives the relevant Walsh formalism and applications of Fourier spectra to graph invariants, including the number of spanning trees **of a Cayley graph** (not the Walsh spectrum of spanning-tree incidence vectors of a prescribed graph). Dall and Pfeifle establish a general weighted matrix-tree identity for regular matroids. That identity can evaluate the **signed tree-count polynomial at a fixed weighting**, but it does not evaluate the absolute average of that polynomial over all edge signings and therefore does not supply the displayed binomial expression or the exact zero multiplicity.

The three-path theta graph has also been studied for algebraic gnarledness (a degree-one chain-extension invariant), and cactus graphs have been studied for projection norms in transportation spaces. These are different operators on different spaces; neither formula implies the Fourier multiplier norm on the Boolean edge group. Likewise, a Walsh projection calculation for the spanning-tree incidence vectors of \(K_{2,n}\) concerns a different graph family and does not contain a direct-edge theta graph as a parameter specialization. The present contribution is a uniform sharp Fourier endpoint invariant for a noncactus bicyclic family, together with its exact Fourier-nullity law and parity asymptotics. No exhaustive historical-priority claim is made.

## Limitations
The graph is restricted to two internally disjoint paths and a single direct terminal edge. The theorem does not cover arbitrary three-path theta graphs with all path lengths greater than one, arbitrary series-parallel graphs, or arbitrary graphic matroids. The leading asymptotic statements shown are for equal path lengths, although the exact formula covers unequal path lengths. The full coefficient identity is elementary and follows from the known weighted spanning-tree polynomial; the novelty claim concerns its absolute Walsh norm and kernel-zero classification. An unindexed earlier signed-tree Walsh norm or equivalent table remains a bibliographic risk. The work has not been independently mathematically validated.

## References
1. Andrew Goodall, *Fourier analysis on finite Abelian groups: some graphical applications*, in *Combinatorics, Complexity, and Chance*, 2007, DOI: 10.1093/acprof:oso/9780198571278.003.0007 (published 2007-01-18; author-supplied full text at https://www.researchgate.net/publication/266250848_Fourier_Analysis_on_Finite_Abelian_Groups_Some_Graphical_Applications).
2. Aaron Dall and Julian Pfeifle, *A Polyhedral Proof of the Matrix Tree Theorem*, arXiv:1404.3876 (first posted 2014-04-15), especially Theorem 15 on weighted regular matroids, https://arxiv.org/html/1404.3876v2.
3. *Exact algebraic gnarledness of three-path theta graphs*, public research record `cceb12dd2a0d` (2026), for a distinct chain-complex invariant.
4. *Sharp coordinate-projection norms for edge bases of cactus transportation spaces*, public research record `b98930fbc1cd` (2026), for a distinct Lipschitz-free-space projection.
