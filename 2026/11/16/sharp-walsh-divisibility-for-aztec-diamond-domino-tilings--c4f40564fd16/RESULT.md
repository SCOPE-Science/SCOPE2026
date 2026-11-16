# Sharp Walsh divisibility for Aztec-diamond domino tilings

## Finding

For each integer \(n\geq 1\), let \(G_n\) be the usual order-\(n\) Aztec-diamond domino graph, and let \(\mathcal M_n\) denote its perfect matchings. On the binary edge-coordinate group \(\mathbb F_2^{E(G_n)}\), define the unnormalized Walsh multipliers

\[
W_n(S)=\sum_{M\in\mathcal M_n}(-1)^{|M\cap S|},\qquad S\subseteq E(G_n).
\]

Then the **exact common divisor of every signed domino-tiling sum** is

\[
\boxed{\gcd_{S\subseteq E(G_n)}W_n(S)=2^n.}
\]

Moreover, there is a specified family of only \(n\) edges such that, among the \(2^n\) signings supported on those edges, an **odd number** have \(W_n(S)/2^n\) odd. This supplies sharpness for every order without requiring a Fourier-spectrum enumeration. In contrast, the all-positive multiplier is \(W_n(\varnothing)=2^{n(n+1)/2}\), the classical Aztec-diamond tiling number.

## Assumptions and scope

Use the following bipartite coordinate realization of the Aztec-diamond graph. Its white vertices are \(w_{j,k}\) with \(0\leq j<n\), \(0\leq k\leq n\), and its black vertices are \(b_{p,q}\) with \(0\leq p\leq n\), \(0\leq q<n\). Place an edge between \(w_{j,k}\) and \(b_{p,q}\) exactly when \(p\in\{j,j+1\}\) and \(k\in\{q,q+1\}\). These are the two color classes of the ordinary Aztec diamond, each of cardinality \(m=n(n+1)\).

All edges are independently allowed signs \(\pm1\) in the Walsh sum; no periodicity, symmetry, positivity of the individual edge weights, or restriction to a particular matching is assumed. Define the distinguished edges

\[
d_j=\{w_{j,j},b_{j,j}\},\quad 0\leq j<n.
\]

The odd-number sharpness assertion refers specifically to sign sets \(S\subseteq\{d_0,\ldots,d_{n-1}\}\).

## Proof

**1. Kasteleyn determinant identity.** The graph is planar and its bounded faces are quadrilaterals. Give a present edge \(w_{j,k}b_{p,q}\) a fixed sign \(-1\) precisely if \(p=j+1\) and \(q=k\), and \(+1\) otherwise. Every bounded quadrilateral has exactly one negative edge. Hence this is a real bipartite Kasteleyn signing. If \(K(S)\) is the resulting square signed bipartite matrix after multiplying the entry of every edge in \(S\) by \(-1\), the determinant expansion has the same fixed permutation/sign factor for every perfect matching, so

\[
\det K(S)=\varepsilon_n W_n(S),\qquad \varepsilon_n\in\{-1,1\}
\]

where \(\varepsilon_n\) is independent of \(S\). The familiar Kasteleyn sign rule also follows by comparing two matchings around each alternating cycle: its interior contains an even number of unmatched-to-cycle vertices, and each enclosed quadrilateral contributes a negative face sign.

**2. Universal divisibility.** Reduce \(K(S)\) modulo two. Every nonzero entry becomes one, independently of \(S\). The resulting binary matrix \(A\) is a Kronecker product \(U\otimes V\), where

\[
U_{j,p}=\mathbf1_{\{p=j\text{ or }p=j+1\}},\quad
V_{k,q}=\mathbf1_{\{k=q\text{ or }k=q+1\}}.
\]

Here \(U\) has dimensions \(n\times(n+1)\), and \(V\) has dimensions \((n+1)\times n\). Both have rank \(n\) over \(\mathbb F_2\), as witnessed by their first \(n\) columns or rows respectively. Thus

\[
\operatorname{rank}_{\mathbb F_2} A=n^2,
\qquad m-\operatorname{rank}_{\mathbb F_2} A=n.
\]

An integral square matrix of size \(m\) and binary rank \(m-n\) has determinant divisible by \(2^n\): integer elementary row/column operations lift a binary rank decomposition, leaving \(n\) even rows. The determinant identity proves \(2^n\mid W_n(S)\) for every \(S\).

**3. An odd complementary minor.** Delete from \(A\) the \(n\) rows \(w_{j,j}\) and the \(n\) columns \(b_{j,j}\), for \(0\leq j<n\), and call the retained \(n^2\times n^2\) submatrix \(A_*\). We show \(A_*\) is nonsingular over \(\mathbb F_2\).

For a column-vector array \(X=(x_{p,q})\), its image \(Y=AX\) satisfies \(Y=UXV^{\mathsf T}\). Every column of \(V\) has exactly two ones; therefore \(\sum_{k=0}^n y_{j,k}=0\) for each \(j\), modulo two. If \(x_{j,j}=0\) for each \(j\) and all output entries outside positions \(w_{j,j}\) vanish, these row-sum equations force all output entries to vanish. Since \(V^{\mathsf T}\) has full row rank, \(UXV^{\mathsf T}=0\) implies \(UX=0\). The kernel of \(U\) is spanned by the all-ones vector, so for each \(q\), the values \(x_{p,q}\) are constant as \(p\) varies. The constraints \(x_{q,q}=0\) force every such constant to be zero. Thus the retained submatrix has trivial kernel and \(\det A_*=1\) in \(\mathbb F_2\).

**4. Sharpness and odd number of witnesses.** Fix the Kasteleyn matrix \(K(\varnothing)\), and independently flip only \(d_0,\ldots,d_{n-1}\), according to Boolean variables \(z_j\in\{0,1\}\). The polynomial \(D(z)=\det K(\{d_j:z_j=1\})\) is multilinear. Its full-degree coefficient is, up to sign,

\[
(-2)^n\det K(\varnothing)_*,
\]

where the minor removes those \(n\) rows and columns. This minor is odd by step 3. Since \(2^n\) divides every value \(D(z)\), the Boolean function \(D(z)/2^n\) is integer valued. Its top Boolean finite difference is odd; equivalently

\[
\sum_{z\in\{0,1\}^n}\frac{D(z)}{2^n}\equiv1\pmod2.
\]

Consequently an odd number of these controlled signings attain exact two-adic valuation \(n\) (zeros contribute zero). By the fixed-sign determinant identity the same holds for \(W_n\).

**5. Removing odd common factors.** The Walsh inversion formula on the full group \(\mathbb F_2^{E(G_n)}\), evaluated at the incidence vector of any matching, gives

\[
2^{|E(G_n)|}=\sum_{S\subseteq E(G_n)}W_n(S)(-1)^{|M\cap S|}.
\]

Therefore the gcd of the integer multipliers divides a power of two. Steps 2 and 4 determine its two-adic exponent exactly as \(n\), completing the proof.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently constructs the bipartite graph and verifies the binary full-rank complementary minor through order twelve. Exact recursive perfect-matching enumeration computes all \(2^n\) controlled signings for orders one through five, with tiling totals \(2,8,64,1024,32768\) and corresponding gcds \(2,4,8,16,32\). A distinct integer Bareiss determinant implementation matches the signed matching sums in absolute value for every controlled signing through order four. The counts of sharp controlled signings for orders one through five are \(1,3,3,5,5\), all odd. These checks support, but do not replace, the infinite proof.

Run: `python3 verify.py`.

## Relationship to prior work

Elkies–Kuperberg–Larsen–Propp establish the unsigned Aztec-diamond count and orientation/refinement generating functions. Brualdi–Kirkland evaluate the corresponding sign-nonsingular determinant, at the all-positive dimer weights. Barkley–Liu establish a channel-space lower bound on the two-adic order of **unsigned** perfect-matching counts, and explicitly find \(2^n\) as a divisor for the Aztec diamond; this is the closest earlier statement. Chhita–Duits analyze Aztec-diamond Kasteleyn matrices and arbitrary positive edge weights for correlations.

The general integer-matrix nullity lemma in Barkley–Liu (Lemma 2.9), together with their Aztec-diamond channel calculation, **already implies the universal lower bound** \(2^n\mid W_n(S)\) once any signed Kasteleyn matrix is considered: all such matrices have the same binary reduction. The new claim is **exact sharpness** of that previously available bound simultaneously across the Fourier family: some signing has valuation exactly \(n\) for every order. The complementary-minor construction proves a stronger odd-parity count of sharp signings inside a specified \(n\)-edge subfamily, and Walsh inversion converts dyadic sharpness to the exact common integer divisor. Neither this sharpness nor that witness parity is furnished by the cited unsigned divisibility calculation. No novelty is claimed for the general determinant divisibility lemma, the binary channel count, or the Kasteleyn construction.

## Limitations

The result does not give a complete Walsh spectrum, determine all zero frequencies, classify every sharp signing, or evaluate inverse/projection operator norms. The proof concerns the ordinary Aztec-diamond graph and cannot be applied unchanged to arbitrary weighted regions. The relevant historical comparison is bounded; an earlier exact simultaneous-signed gcd formula could exist outside the inspected sources. This is an internal proof with reproducible finite corroboration, not independent validation.

## References

1. N. Elkies, G. Kuperberg, M. Larsen, J. Propp, *Alternating Sign Matrices and Domino Tilings*, dated June 1991 in the available arXiv text, https://arxiv.org/abs/math/9201305.
2. R. A. Brualdi, S. Kirkland, *Aztec Diamonds and Digraphs, and Hankel Determinants of Schröder Numbers*, manuscript dated 2003-06-02, https://people.math.wisc.edu/~rbrualdi/aztec2.pdf.
3. G. T. Barkley, R. I. Liu, *Channels, Billiards, and Perfect Matching 2-Divisibility*, arXiv first posted 2019-11-19, Theorem 3.5 and Example 6.10, https://arxiv.org/abs/1911.08102.
4. S. Chhita, M. Duits, *On the Domino Shuffle and Matrix Refactorizations*, 2023, Section 2, https://doi.org/10.1007/s00220-023-04676-y.
