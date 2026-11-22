# A mod-four Walsh recovery law for two-row injective assignments

## Finding

Let \(n\ge2\). In the Boolean edge group \(G_n=\mathbb F_2^{2n}\) for the complete bipartite graph \(K_{2,n}\), let \(f_n\) indicate the incidence vectors of matchings that cover **both** vertices on the two-vertex side (equivalently, injective assignments of the two labelled tasks to \(n\) labelled resources). There are \(n(n-1)\) such assignments. Let \(T_n g=f_n*g\), with unnormalized counting convolution.

**Complete signed Fourier spectrum.** For every frequency mask, write its two rows of Walsh signs as \(x_i,y_i\in\{-1,1\}\), and define \(a=\sum_i x_i\), \(b=\sum_i y_i\), \(c=\sum_i x_i y_i\). Then its multiplier is exactly
\[
W_n(x,y)=ab-c.
\]
More explicitly, if \(u\) of the \(x_i\) are negative, \(v\) of the \(y_i\) are negative, and \(t\) coordinates have both signs negative, then
\[
W_n(u,v,t)=(n-2u)(n-2v)-n+2(u+v-2t).
\]
The multiplicity of this type is \(\binom nu\binom ut\binom{n-u}{v-t}\), with \(0\le u,v\le n\) and \(\max(0,u+v-n)\le t\le\min(u,v)\). Thus the displayed values and multiplicities form the **entire signed spectrum**, including coincident values obtained from different types.

**Exact invertibility and sharp surviving gap.**
\[
T_n\text{ is invertible}\iff n\equiv3\pmod4.
\]
For every \(n\ge2\) the largest absolute multiplier is \(n(n-1)\). The smallest *strictly positive* absolute multiplier is \(4\) if \(n\equiv1\pmod4\) and \(2\) otherwise. Hence the exact Hilbert-space spectral condition number on the recoverable range is \(n(n-1)/4\) if \(n\equiv1\pmod4\), and \(n(n-1)/2\) otherwise.

**Exact lost dimension.** Define
\[
Z_n=\sum_{u=0}^{n}\sum_{v=0}^{n}
\sum_{t=\max(0,u+v-n)}^{\min(u,v)}
\binom nu\binom ut\binom{n-u}{v-t}
\mathbf1\!\left\{(n-2u)(n-2v)=n-2(u+v-2t)\right\}.
\]
Then \(\operatorname{nullity}(T_n)=Z_n\) and \(\operatorname{rank}(T_n)=4^n-Z_n\), without an unperformed infinite enumeration. In particular, \(Z_n=0\) exactly when \(n\equiv3\pmod4\). Sample exact nullities for \(n=2,3,4,5,6,7,8,9\) are respectively \(8,0,64,400,800,0,10640,66864\).

## Assumptions and scope

The two left vertices and all \(n\) right vertices are labelled. An admissible matching contains **exactly two** edges, one adjacent to each left vertex, and uses distinct right vertices. The ambient Boolean coordinates include all \(2n\) possible edges. The Fourier transform and convolution are unnormalized: \((f*g)(z)=\sum_{w\in G_n}f(w)g(z-w)\). The character of an edge mask is the product of its corresponding signs on each incidence vector. Real singular values of \(T_n\) are the absolute Fourier multipliers. No assertion is made for partial matchings that leave a left vertex unmatched, or for square perfect-matchings with a variable number of rows.

## Proof

An admissible matching is uniquely specified by an ordered pair \((i,j)\) of distinct right endpoints. Its character value is \(x_i y_j\), so
\[
W_n=\sum_{i\ne j}x_i y_j=\left(\sum_i x_i\right)\left(\sum_j y_j\right)-\sum_i x_i y_i=ab-c.
\]
The counts of jointly negative and singly negative signs give \(a=n-2u\), \(b=n-2v\) and \(c=n-2(u+v-2t)\). To count frequency masks of fixed type, first choose the \(u\) negatives of the first row, then the \(t\) overlapping negatives of the second, and finally its remaining \(v-t\) negatives outside the first row. This yields the stated exact signed multiplicities. Character diagonalization of additive convolution now proves the rank/nullity formulas.

Expanding the multiplier also gives the integer identity
\[
W_n=n(n-1)-2(n-1)(u+v)+4(uv-t).
\]
For odd \(n\), \(W_n\equiv n(n-1)\pmod4\). Thus when \(n\equiv3\pmod4\), every multiplier is congruent to \(2\pmod4\), and therefore no multiplier vanishes and every absolute multiplier is at least \(2\). If \(n=4k+3\), choose \(u=v=2k+1\) with overlap \(t=k\). These sets are feasible (the union has \(3k+2\) elements), and they give \(a=b=1\), \(c=-1\), and \(W_n=2\). This attains the lower bound.

If \(n=4k+1\) with \(k\ge1\), every Fourier multiplier is divisible by \(4\). Choose \(u=v=2k\) and \(t=k\); then \(a=b=c=1\), giving \(W_n=0\). Choose instead the feasible overlap \(t=k-1\); then \(a=b=1\), \(c=-3\), giving \(W_n=4\). Hence singularity and the sharp positive gap both hold.

If \(n\) is even, take the first-row signs balanced, so \(a=0\), and initially set all second-row signs to \(+1\); then \(c=0\) and \(W_n=0\). Flipping one second-row sign at a coordinate with first-row sign \(+1\) changes \(c\) to \(-2\) while leaving \(a=0\), so \(W_n=2\). Every multiplier is an even integer because it is a sum of the even number \(n(n-1)\) of signs. Hence this is the sharp positive gap at even \(n\).

Finally, the triangle inequality gives \(|W_n|\le n(n-1)\), with equality when all edge signs are positive. Dividing this maximum by each proven sharp positive minimum gives the claimed condition numbers. These arguments establish all asserted ranges, without relying on finite computation for general \(n\).

## Verification

`check_spectrum.py` independently enumerates all \(2^{2n}\) character masks for \(2\le n\le8\), directly sums \(n(n-1)\) ordered injective assignments per mask, and checks the signed formula, zero multiplicity, exact invertibility and sharp gaps. `check_counts.py` separately enumerates the three overlap parameters for \(2\le n\le30\), checks exact nullity and explicit extremizers, including all four residue classes. Both programs passed using the embedded code, but finite tests are corroboration only: the proof above covers every \(n\ge2\).

## Relationship to prior work

The general use of additive characters to diagonalize convolution is classical Fourier analysis; see O'Donnell (2014). The signed permanent of square \((\pm1)\)-matrices has a rich older literature. In particular Wanless (2005), Theorem 1, reproduces the classical criterion that a square sign matrix of order \(m\) has a zero permanent for some signing exactly when \(m+1\) is not a power of two. That square-matrix result neither states nor implies the complete **two-row rectangular** spectrum here: the family has only two prescribed matched rows and a varying number of columns. The two conditions even differ, e.g. at eleven columns a two-row operator here is invertible although an eleven-by-eleven sign matrix with zero permanent exists. The closed form here also supplies exact signed multiplicities, nullities and sharp surviving gaps, none of which follow from that square existence theorem. An accessible indexed order-five square-permutation Fourier census likewise concerns the distinct square object; an equivalent older two-row signed-rook calculation remains possible and has not been ruled out exhaustively.

## Limitations

The result is a complete elementary spectral classification for precisely the two-row injection family, not a general theorem about arbitrary rectangular matchings. Its scientific interest is the unexpectedly sharp mod-four injectivity boundary, all-frequency multiplicity formula and exact surviving condition numbers. No asymptotic simplification of \(Z_n\) is claimed; no independent external validation has occurred. Bibliographic and indexed prior-art searches are bounded and cannot establish absolute priority.

## References

- I. M. Wanless, *Permanents of matrices of signed ones*, Linear and Multilinear Algebra 53 (2005), 427–433, DOI: 10.1080/03081080500093990. Author-hosted full text: https://users.monash.edu.au/~iwanless/papers/wangconjLAMA.pdf.
- R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), DOI: 10.1017/CBO9781139814782. Original publication identified at Cambridge University Press: https://www.cambridge.org/core/books/analysis-of-boolean-functions/B05A66E4DCC778E02B84C16376F4D1FD.
