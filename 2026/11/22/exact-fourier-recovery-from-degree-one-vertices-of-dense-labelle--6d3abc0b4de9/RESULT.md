# Exact Fourier recovery from degree-one vertices of dense labelled graphs

## Finding
For every integer \(n\ge1\), let \(\mathcal G_n\) be the \(2^{\binom n2}\) simple graphs on vertex set \([n]\). Define the *degree-one profile* \(L(G)=\{v:\deg_G(v)=1\}\), and let \(p_n(S)=2^{-\binom n2}\#\{G\in\mathcal G_n:L(G)=S\}\) for \(S\subseteq[n]\). On the Boolean group \(\mathbb F_2^n\), form the probability convolution \(T_nf=p_n*f\), using XOR as the group law. Its Walsh eigenvalue at a character indexed by \(A\subseteq[n]\) depends only on \(k=|A|\) and is
\[
\rho_{n,k}=2^{-\binom n2}\sum_{j=0}^{k}\binom kj(-2)^j2^{\binom{n-j}{2}} H_j(n-j),\qquad
H_j(m)=\sum_{r=0}^{\lfloor j/2\rfloor}\frac{j!}{2^r r!(j-2r)!}m^{j-2r}.
\]
Here \(0^0=1\). For every \(n\ge1\):

1. \(T_n\) is singular precisely at \(n=2,3\), with rank \(2\) at each of those orders. At \(n=1\) it is the identity, and for every \(n\ge4\) it is strictly positive definite and invertible on real and complex \(\ell^2(\mathbb F_2^n)\).
2. At \(n=4\) the smallest Walsh eigenvalue occurs exactly at weights \(2,3\); at \(n=5\) it occurs exactly at weight \(4\); at every \(n\ge6\) it occurs uniquely at weight \(n\). In particular \(\rho_{n,k}\) is strictly decreasing as a function of \(k\) for every \(n\ge6\).
3. The exact, globally sharp probability-normalized Euclidean convolution condition bound is
\[
\sup_{n\ge4}\kappa_2(T_n)=8,
\]
with equality only at \(n=4\). Moreover \(\kappa_2(T_n)\to1\) and, as \(n\to\infty\),
\[
\kappa_2(T_n)=1+\frac{2n(n-1)}{2^{n-1}}+O\!\left(\frac{n^4}{4^n}\right).
\]

The eigenvalue at weight \(k\) has multiplicity \(\binom nk\). In particular, the least eigenvalue has multiplicity ten at \(n=4\), five at \(n=5\), and one at every \(n\ge6\). Consequently the formula gives the entire spectrum, the rank, and the sharp \(\ell^2\) inverse norm (where invertible).

## Assumptions and scope
Graphs are undirected, loopless and simple, with uniformly chosen independent equiprobable edges; the probability measure is not conditioned on connectedness or minimum degree. A vertex belongs to the recorded set only when its degree is **exactly one**, not zero and not merely odd. Walsh characters have the convention \(\chi_A(S)=(-1)^{|A\cap S|}\); convolution is by the probability distribution \(p_n\), not an unnormalized count distribution. The full group has \(2^n\) elements. All assertions hold for integer \(n\ge1\), and the strict-minimum description assumes \(n\ge4\). The \(\ell^2\) condition number uses the ratio of the largest to least singular values.

## Proof
**1. Exact joint forced-degree enumeration.** Fix \(J\subseteq[n]\) of size \(j\). To force every vertex in \(J\) to have degree exactly one, the edges internal to \(J\) must form a matching of size \(r\), in \(j!/(2^r r!(j-2r)!)\) ways. The \(j-2r\) unmatched vertices of \(J\) each choose exactly one neighbor outside \(J\), giving \((n-j)^{j-2r}\) choices. Every other edge incident to \(J\) is absent, while all \(\binom{n-j}{2}\) outside edges are arbitrary. Thus the number of graphs in which all vertices of \(J\) have degree one is exactly \(2^{\binom{n-j}{2}}H_j(n-j)\). Expanding
\[
(-1)^{|A\cap L(G)|}=\prod_{v\in A}(1-2\mathbf1_{\{\deg_G(v)=1\}})
\]
and taking expectations proves the displayed Walsh formula, without any independence assumption among vertex degrees.

**2. Small orders, exact.** Let \(\lambda_{n,k}=2^{\binom n2}\rho_{n,k}\). Applying the preceding exact formula yields these complete weight-ordered multiplier vectors:

| \(n\) | \((\lambda_{n,0},\ldots,\lambda_{n,n})\) |
|---|---|
| 1 | \((1,1)\) |
| 2 | \((2,0,2)\) |
| 3 | \((8,0,0,8)\) |
| 4 | \((64,16,8,8,32)\) |
| 5 | \((1024,512,320,224,160,224)\) |
| 6 | \((32768,22528,16640,12800,10080,8096,7136)\) |
| 7 | \((2097152,1703936,1417216,1198080,1025280,886144,772352,680576)\) |
| 8 | \((268435456,239075328,214564864,193757184,175868928,160337408,146741632,134757504,124144384)\) |

In particular the only zeros in these orders are weight \(1\) at \(n=2\), and weights \(1,2\) at \(n=3\). Their multiplicities are \(2\) and \(3+3=6\), respectively. The table establishes strict weight decrease for \(n=6,7,8\) and the claimed exceptional minimizers.

**3. Positivity at every larger order.** Let \(X_v=\mathbf1_{\{\deg_G(v)=1\}}\). Since \(\deg_G(v)\sim\operatorname{Bin}(n-1,1/2)\),
\[
\Pr(X_v=1)=\frac{n-1}{2^{n-1}},\qquad \Pr(\exists v:X_v=1)\le\frac{n(n-1)}{2^{n-1}}.
\]
For every character \(A\), the sign \((-1)^{\sum_{v\in A}X_v}\) differs from \(1\) only if some vertex has degree one. Hence
\[
\rho_{n,|A|}\ge1-\frac{2n(n-1)}{2^{n-1}}>0 \quad(n\ge8).
\]
The final inequality holds at \(n=8\) and persists since the ratio of consecutive values of \(n(n-1)2^{-(n-1)}\) is \((n+1)/(2(n-1))<1\) for \(n>3\). This, together with the exact small-order table, proves the full invertibility and positivity classification.

**4. Strict spectral ordering from order nine onward.** Fix \(A\subseteq[n]\) of size \(k<n\) and \(v\notin A\). Then
\[
\rho_{n,k}-\rho_{n,k+1}=2\Pr(X_v=1)\,\mathbb E\!\left[(-1)^{\sum_{u\in A}X_u}\mid X_v=1\right].
\]
Given \(X_v=1\), its unique neighbor is uniform among the other \(n-1\) vertices. For each fixed \(u\ne v\), the conditional probability that \(u\) also has degree one is
\[
q_n=\frac{1+(n-2)^2}{(n-1)2^{n-2}}.
\]
Indeed, with probability \(1/(n-1)\) the neighbor of \(v\) is \(u\), and then \(u\) must have no other neighbor; otherwise \(u\) must have one neighbor among the \(n-2\) remaining candidates. The conditional sign expectation is at least \(1-2kq_n\), hence at least
\[
1-\frac{2(1+(n-2)^2)}{2^{n-2}}>0\quad(n\ge9).
\]
At \(n=9\) the fraction subtracted is \(100/128<1\), and \((1+(n-2)^2)/2^{n-2}\) strictly decreases thereafter because \(2(1+(n-2)^2)-(1+(n-1)^2)=(n-2)(n-4)>0\) for \(n>4\). Consequently the frequencies decrease strictly with their weight for all \(n\ge9\). Together with the table for \(n=6,7,8\), this proves the all-order extremal-weight statement.

**5. Sharp uniform conditioning and asymptotics.** The maximum eigenvalue is \(\rho_{n,0}=1\), and all eigenvalues are positive for \(n\ge4\). From the table, \(\kappa_2(T_4)=8\), while
\[
\kappa_2(T_5)=\frac{32}{5},\quad
\kappa_2(T_6)=\frac{1024}{223},\quad
\kappa_2(T_7)=\frac{16384}{5317},\quad
\kappa_2(T_8)=\frac{1048576}{484939},
\]
each strictly less than eight. For all \(n\ge9\), Step 3 shows \(\kappa_2(T_n)\le (1-2n(n-1)/2^{n-1})^{-1}\le16/7<8\). This proves sharpness and uniqueness of the uniform maximum.

To refine the limit, let \(N=\sum_{v=1}^n X_v\). Since \(\rho_{n,n}=\mathbb E[(-1)^N]\), we have \(1-\rho_{n,n}=2\Pr(N\text{ odd})\). The pointwise inequality \(|\mathbf1_{\{N\text{ odd}\}}-N|\le2\binom N2\) shows
\[
\left|1-\rho_{n,n}-2\mathbb EN\right|\le4\mathbb E\binom N2.
\]
Here \(\mathbb EN=n(n-1)/2^{n-1}\), and the exact two-vertex count in Step 1 gives
\[
\mathbb E\binom N2=\binom n2\frac{(n-2)^2+1}{2^{2n-3}}=O(n^4/4^n).
\]
Because \(\rho_{n,n}\to1\), expanding \(1/\rho_{n,n}\) proves the stated first-order condition-number asymptotic with the stated error.

## Verification
The standalone standard-library script `verify.py` computes the joint forced-degree count formula independently of enumerating all graphs. It additionally walks **every** simple graph through order seven by a Gray-code edge enumeration, updates the degree-one profile, performs a full Walsh–Hadamard transform of the profile histogram, and compares all \(2^n\) character values to the formula. It checks every listed weight multiplier through order eight and the finite inequalities used in the proof. The script passes 591 exact assertions. The finite tests are reproducibility checks, not a replacement for the all-order arguments in Steps 3–5.

## Relationship to prior work
Lin and Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model*, arXiv:0912.4812v1 (first public 2009-12-24), develop distributional approximations and size-biased couplings for joint degree counts, including exact degree indicators. Ghosh, Goldstein and Raič, *Concentration of measure for the number of isolated vertices in the Erdős–Rényi random graph by size bias couplings*, arXiv:1106.0048v1 (2011-05-31), give concentration results for the degree-zero count and review fixed-degree count literature. The random graph model and fixed-degree indicators are established, and the single- and two-vertex probabilities here follow from elementary independent-edge counting. Neither inspected result states the complete finite Boolean-character spectrum of the degree-one **set**, its strict minimizer classification, or the globally sharp \(\ell^2\) condition constant eight. Those are the claims assessed here; no new random-graph model or degree-count central limit theorem is claimed.

## Limitations
Historical priority is not certified: an unindexed paper or table of signed degree-one set moments might imply all or part of the result. A semantic literature and published-result search did not locate one. The statement concerns only uniformly sampled **simple** labelled graphs at edge probability one half; it does not give a positivity classification for arbitrary edge probabilities, restricted graph families, or endpoint \(\ell^1\)/\(\ell^\infty\) inverse norms. The independent audit has not been performed.

## References
1. K. Lin and G. Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model*, arXiv:0912.4812v1, 24 December 2009. https://arxiv.org/html/0912.4812v1
2. S. Ghosh, L. Goldstein and M. Raič, *Concentration of measure for the number of isolated vertices in the Erdős–Rényi random graph by size bias couplings*, arXiv:1106.0048v1, 31 May 2011. https://arxiv.org/abs/1106.0048
