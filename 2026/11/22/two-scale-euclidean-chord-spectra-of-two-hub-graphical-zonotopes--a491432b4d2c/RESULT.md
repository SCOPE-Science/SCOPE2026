# Two-scale Euclidean chord spectra of two-hub graphical zonotopes

## Finding
For every integer \(n\ge2\), let \(Z_n\) be the centered, unit-weight graphical zonotope of the complete bipartite graph \(K_{2,n}\), realized in its standard Euclidean coordinates:
\[
Z_n=\sum_{j=1}^{n}\left[-\frac{e_A-e_j}{2},\frac{e_A-e_j}{2}\right]
+\sum_{j=1}^{n}\left[-\frac{e_B-e_j}{2},\frac{e_B-e_j}{2}\right]\subset \mathbb R^{n+2}.
\]
Let \(D_n(z)=\sum_{\{v,w\}\subset\operatorname{Vert}(Z_n),\ v\ne w}z^{\|v-w\|_2^2}\) be the **unordered distinct-vertex squared-distance polynomial**. Its exponents are nonnegative integers. The following formula determines every coefficient using four-letter sums and a polynomial-state convolution, rather than enumerating the exponentially many vertices.

Put \(S_+=\{(1,1),(-1,-1),(1,-1)\}\), \(S_-=\{(1,1),(-1,-1),(-1,1)\}\), and \(S_0=\{(1,1),(-1,-1)\}\). For \(X,Y\in\{+,-,0\}\), define the Laurent polynomial
\[
T_{XY}(u,v,z)=\sum_{(a,b)\in S_X}\sum_{(c,d)\in S_Y}
u^{(a-c)/2}v^{(b-d)/2}z^{(a+b-c-d)^2/4}
\]
and its quadratic hub-collapsed \(n\)-fold convolution
\[
H_{XY}^{(n)}(z)=\sum_{j=-n}^{n}\sum_{k=-n}^{n}z^{j^2+k^2}[u^jv^k]T_{XY}(u,v,z)^n.
\]
With \(\kappa_+=\kappa_-=1\), \(\kappa_0=-1\), and \(N_n=2\cdot3^n-2^n\), the complete exact result is
\[
\boxed{D_n(z)=\frac12\left(\sum_{X,Y\in\{+,-,0\}}\kappa_X\kappa_Y H_{XY}^{(n)}(z)-N_n\right).}
\]
In particular, \(D_n(1)=\binom{N_n}{2}\), the smallest nonzero squared distance is \(2\), and the largest is \(2n(n+2)\), occurring once. For example,
\[
D_2(z)=32z^2+12z^4+32z^6+6z^8+8z^{10}+z^{16}.
\]

There is a geometric **two-scale law**. Let \(Q_n\) be the squared Euclidean distance of a uniformly chosen unordered pair of distinct vertices. Then
\[
\boxed{\frac{Q_n}{n^2}\ \xrightarrow{\mathrm d}\ \frac12\delta_0+\frac12\delta_{2/9}.}
\]
For a nonexceptional vertex, its associated acyclic orientation uses precisely one of the mixed columns \((1,-1)\) and \((-1,1)\); call the corresponding type its **branch**. Conditional on both vertices being nonexceptional and of the same branch,
\[
\boxed{\frac{Q_n}{n}\ \xrightarrow{\mathrm d}\ \frac43+\frac23U^2+\frac29V^2,}
\]
where \(U,V\) are independent standard normals. Conditional on opposite branches,
\[
\boxed{\frac{Q_n-(2/9)n^2}{n^{3/2}}\ \xrightarrow{\mathrm d}\ N\!\left(0,\frac{16}{81}\right).}
\]
The exceptional vertices, containing no mixed column, have vanishing sampling probability \(O((2/3)^n)\). Thus half of all random chords have squared length of order \(n\), with a shifted **non-Gaussian** limit, while half have squared length of order \(n^2\) with Gaussian fluctuations of order \(n^{3/2}\).

## Assumptions and scope
The two hubs \(A,B\) and \(n\) leaves are labeled. All generators are exactly the displayed unit Euclidean root segments; the affine span is the zero-sum hyperplane. Vertices are sampled uniformly from *distinct* zonotope vertices, not by volume measure, a random linear objective, or a random topological ordering. All Euclidean norms are ambient norms and agree with intrinsic norms on the affine span. The asymptotic statements are as the integer \(n\) tends to infinity. The formal indeterminate \(z\) records squared distances; \(u,v\) are Laurent variables and coefficient extraction is purely algebraic.

## Proof
**1. Complete acyclic-orientation model.** Assign signs \((a_j,b_j)\in\{\pm1\}^2\) to the two edges incident with leaf \(j\), with positive sign indicating orientation from hub to leaf. The signed vertex is
\[
W(a,b)=\frac12\left(\sum_j a_j,\ \sum_j b_j,\ -a_1-b_1,\ldots,-a_n-b_n\right).
\]
Vertices of a graphical zonotope correspond bijectively to acyclic orientations. In \(K_{2,n}\), a directed cycle occurs precisely when some leaf has mixed type \((1,-1)\) and another has \((-1,1)\): these two leaves form a directed four-cycle, and every possible simple cycle of \(K_{2,n}\) is a four-cycle. Consequently its vertex sign words form \(S_+^n\cup S_-^n\), with intersection \(S_0^n\). Distinct acyclic orientations yield distinct exposed vertices. Thus there are exactly \(N_n=2\cdot3^n-2^n\) vertices.

**2. A complete two-point enumerator.** For two words \((a_j,b_j)\) and \((c_j,d_j)\), let \(h_1=\sum_j(a_j-c_j)/2\), \(h_2=\sum_j(b_j-d_j)/2\), and \(\ell_j=(a_j+b_j-c_j-d_j)^2/4\). Direct coordinate subtraction gives the exact identity
\[
\|W(a,b)-W(c,d)\|^2=h_1^2+h_2^2+\sum_{j=1}^n\ell_j.
\]
For independently chosen words restricted to \(S_X^n\) and \(S_Y^n\), the product \(T_{XY}^n\) records the two hub differences and the sum of leaf squared differences. Therefore \(H_{XY}^{(n)}\) is their exact ordered-pair distance polynomial. The indicator of the union is the sum of the two branch indicators minus their intersection indicator. Applying this identity independently to both points gives \(\sum_{X,Y}\kappa_X\kappa_Y H_{XY}^{(n)}\). This counts all ordered pairs, including \(N_n\) diagonal pairs of distance zero. Subtracting the diagonal and dividing by two establishes the boxed exact formula, for every \(n\ge2\). The finite-state convolution has \(O(n^3)\) possible hub-difference/leaf-square states and runs in \(O(n^4)\) integer arithmetic operations for fixed nine kernels.

**3. Boundary values.** Changing just one sign across a valid adjacent orientation changes the vertex by one root vector of squared norm \(2\), and all distinct vertex differences have squared norm an even positive integer: their integral coordinates sum to zero, so the sum of coordinate squares is even. Thus the minimum is \(2\). For every vertex, the two hub coordinates have absolute value at most \(n/2\), while each leaf coordinate has absolute value at most \(1\), giving \(\|W\|^2\le n^2/2+n\). Equality requires both hubs to attain absolute value \(n/2\) and every leaf to have modulus one, leaving only the two antipodal sign words consisting entirely of \((1,1)\) and entirely of \((-1,-1)\). Their mutual squared distance is \(2n(n+2)\). Hence they are the unique diametral unordered pair. These extremal values also follow from the established multipartite-zonotope circumsphere theorem; they are consistency checks, not novelty claims.

**4. Probabilities of the two branches.** Put \(L_n=3^n-2^n\), the number of orientations in either branch but outside the intersection. The fraction of exceptional vertices is \(2^n/N_n=O((2/3)^n)\); sampling without replacement differs from independent vertex sampling by probability \(1/N_n\). Among two nonexceptional vertices, the probability of matching branches tends to \(1/2\), and the probability of opposite branches tends to \(1/2\). Conditioning a three-letter product word on containing at least one mixed column changes its law by total variation at most \((2/3)^n\). Thus it suffices to analyze two independent uniform words of the appropriate three-letter alphabets.

**5. Same-branch non-Gaussian law.** In branch \(+\), one leaf's sign pair \((a,b)\) has mean \((1/3,-1/3)\) and covariance
\[
\Sigma=\begin{pmatrix}8/9&4/9\\4/9&8/9\end{pmatrix}.
\]
For two independent words from this branch, their per-leaf differences have zero mean and covariance \(2\Sigma\). By the bivariate central limit theorem, the scaled hub-difference vector converges to a centered Gaussian whose two orthogonal covariance eigenvalues are \(8/3\) and \(8/9\). The hub contribution to \(Q_n/n\) therefore converges to \((2/3)U^2+(2/9)V^2\). The per-leaf squared difference has mean
\[
\frac14\mathbb E[(a+b-c-d)^2]=\frac43,
\]
and the ordinary law of large numbers makes its average converge in probability to \(4/3\). Slutsky's theorem gives the same-branch law. The other branch has identical covariance by hub exchange.

**6. Opposite-branch Gaussian law.** For a plus-branch word and a minus-branch word, the mean per-leaf hub-sign difference is \(\mu=(2/3,-2/3)\), while its covariance remains \(2\Sigma\). Write the two hub-difference coordinate sums as \(n\mu+\sqrt n Z_n\), where \(Z_n\Rightarrow N(0,2\Sigma)\). Then
\[
\frac14\|n\mu+\sqrt n Z_n\|^2=\frac{2n^2}{9}+\frac{n^{3/2}}{2}\mu\cdot Z_n+O_{\mathsf P}(n).
\]
The leaf contribution is \(O_{\mathsf P}(n)\), and \(\operatorname{Var}((\mu\cdot Z_n)/2)\to16/81\), since \(\mu^{\mathsf T}(2\Sigma)\mu/4=16/81\). This proves the stated opposite-branch CLT. In particular the opposite-branch normalized squared distance tends in probability to \(2/9\), while the same-branch normalized squared distance tends to zero. Combining the asymptotic half/half branch weights proves the two-atom unconditional limit.

## Verification
The standalone Python 3 standard-library program `artifacts/check.py` independently enumerates sign orientations by checking the forbidden directed four-cycle, constructs every distinct vertex in doubled integer coordinates, and computes all unordered Euclidean distances for \(2\le n\le6\). It separately computes the nine inclusion-exclusion polynomial convolutions and confirms every coefficient, covering 1,085,463 unordered pairs. It further checks the polynomial-state coefficients, nonzero minimum, unique diametral pair, total pairs, and the exact aggregate sum of squared chords through \(n=12\). Successful output:

`BICLIQUE_TWO_POINT_PASS brute_force_n=2..6 checked_pairs= 1085463 transfer_n=2..12`

The independent normal and chi-square scaling arguments above prove the limits; finite enumerations and sampling diagnostics do not establish them. For reference, the exact aggregate identity checked by the program is
\[
\sum_{j\ge0}j[z^j]D_n(z)=N_n\left(\frac{3^n n(n+20)}9-3n2^{n-1}\right).
\]
It follows independently from the prior uniform-vertex radial-moment computation and the zero mean induced by central symmetry.

## Relationship to prior work
Padrol, Pilaud and Poullot describe graphical zonotopes and their deformation cones, including the acyclic-orientation vertex model. Chapoton and Pilaud identify complete bipartite graphical zonotopes as fundamental shuffle summands and analyze their face structure and vertex counts. Carballosa, Khera and Reyes encode and enumerate acyclic orientations of complete multipartite graphs. These supply the objects and orientation combinatorics, but their inspected statements do not give squared two-point Euclidean spectra.

Published exact Euclidean radius shells and uniform-vertex covariance for this *same* \(K_{2,n}\) zonotope are especially relevant. The radius spectrum is a one-vertex statistic; covariance fixes the expected squared pair distance but not its full distribution or the conditional non-Gaussian/Gaussian two-scale behavior. The complete-multipartite circumsphere theorem already establishes the largest squared distance and its unique antipodal pair. These known implications are explicitly separated from the new complete polynomial and limits.

## Limitations
The theorem concerns uniform sampling of vertices of the unweighted canonical \(K_{2,n}\) realization only. It does not extend automatically to \(K_{p,n}\) with \(p\ge3\), arbitrary edge weights, intrinsic-volume sampling, or Gaussian normal-cone sampling. The exact polynomial is a coefficient-extraction/convolution formula rather than a constant-size rational generating function. Priority is provisional: an unindexed result for lonesum sign matrices, permutation-arrangement chambers, or general multivariate orientation statistics could imply the stated two-point polynomial.

## References
1. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first public 2021-11-24, https://arxiv.org/abs/2111.12422 .
2. F. Chapoton, V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first public 2022-01-18, https://arxiv.org/abs/2201.06896 .
3. W. Carballosa, J. Khera, F. Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, arXiv:2303.09021, first public 2023-03-16, https://arxiv.org/abs/2303.09021 .
4. *Exact radial shells and a Gaussian vertex-radius law for biclique graphical zonotopes*, published research record (2026), identifier `fb52cfc91ae5`.
5. *Exact vertex covariance and a six-leaf eigenaxis transition for two-hub graphical zonotopes*, published research record (2026), identifier `cf349f53c764`.
6. *Complete multipartite graphical zonotopes have cubic-moment circumspheres*, published research record (2026), identifier `2fc427ff213b`.
