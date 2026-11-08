# Complete Smith-type Fourier spectrum of an inner-rank-one matrix Cayley graph

## Finding

For every prime \(p\) and integer \(k\ge3\), the Cayley graph on the additive matrix group \(M_2(\mathbb Z/p^k\mathbb Z)\), with adjacent matrices differing by a nonzero matrix of inner rank one, has the exact integral Fourier spectrum, including multiplicities, stated below. In particular **every adjacency eigenvalue is nonzero** and
\[
\min_{\lambda\in\operatorname{Spec}(T)}|\lambda|=p+1,
\qquad \|T^{-1}\|_{\ell^2\to\ell^2}=\frac1{p+1}.
\]
The least-absolute-eigenvalue eigenspace consists precisely of Fourier characters whose frequency matrix is invertible modulo \(p\). This gives an exact depth-independent inverse norm for the unnormalized adjacency convolution, despite an exponentially increasing graph size and valency. The formulas below actually remain valid at the auxiliary depth \(k=2\); the claimed literature gap concerns arbitrary depth at least three.

## Assumptions and scope

Fix any prime \(p\), any integer \(k\ge3\), and let \(R=\mathbb Z/p^k\mathbb Z\). A matrix has **inner rank at most one** if it factors as \(uv^{\mathsf T}\) with \(u,v\in R^2\); it has **inner rank one** if additionally it is nonzero. Let \(S\) be the set of all such nonzero matrices and define
\[
(Tf)(A)=\sum_{X\in S} f(A-X),\quad A\in M_2(R).
\]
The operator is self-adjoint because \(S=-S\). Let \(B\in M_2(R)\) and let its Smith exponents be \(0\le a\le b\le k\), meaning \(B\) is equivalent under invertible left/right operations to \(\operatorname{diag}(p^a,p^b)\), interpreting \(p^k\) as zero in \(R\). The corresponding additive Fourier character is \(\chi_B(A)=\exp(2\pi i\operatorname{tr}(B^{\mathsf T}A)/p^k)\).

Set \(U_n=p^{3n-3}(p-1)(p+1)^2\) for \(n\ge1\), and \(D_a=\sum_{n=1}^a U_n\), with \(D_0=0\). Then \(T\chi_B=\lambda_{a,b}\chi_B\), where
\[
\lambda_{a,b}=\begin{cases}
D_k,&a=b=k,\\
D_a-(p+1)p^{3a},&a=b<k,\\
D_a+(p^2-p-1)p^{3a}+(p-1)\displaystyle\sum_{n=a+2}^{k}p^{2n+a-1},&a<b=k,\\
D_a+(p^2-p-1)p^{3a}+(p-1)\displaystyle\sum_{n=a+2}^{b}p^{2n+a-1}-p^{2b+a+1},&a<b<k.
\end{cases}
\]
Empty sums are zero. The number \(m_{a,b}\) of Fourier characters of Smith type \((a,b)\) is
\[
m_{a,b}=\begin{cases}
1,&a=b=k,\\
p^{4(k-a-1)+1}(p-1)^2(p+1),&a=b<k,\\
U_{k-a},&a<b=k,\\
p^{4k-3a-b-4}(p-1)^2(p+1)^2,&a<b<k.
\end{cases}
\]
These formulas give the full spectral multiset: when distinct Smith types happen to give equal numerical eigenvalues, add their multiplicities. In particular \(\sum_{0\le a\le b\le k}m_{a,b}=p^{4k}\). The degree is \(D_k\).

## Proof

**1. Disjoint valuation decomposition.** A nonzero inner-rank-one matrix \(X\in M_2(R)\) has a unique common-entry valuation \(j\in\{0,\ldots,k-1\}\) and the form \(X=p^jY\), where \(Y\) is a matrix over \(\mathbb Z/p^{k-j}\mathbb Z\) with a unit entry and inner rank one. Such \(Y\) factors as \(uv^{\mathsf T}\) with both vectors primitive (at least one unit coordinate). The factorization is unique up to \((u,v)\mapsto(cu,c^{-1}v)\) for a unit \(c\); consequently the number of such \(Y\) at modulus \(p^n\) is
\[
U_n=\frac{(p^{2n}-p^{2n-2})^2}{p^{n-1}(p-1)}=p^{3n-3}(p-1)(p+1)^2.
\]
The disjoint levels have respective sizes \(U_n\), for \(1\le n\le k\).

**2. Exact primitive-level Fourier transform.** Let \(\mu_n(B)\) denote the character sum over unit-entry rank-one \(2\)-by-\(2\) matrices modulo \(p^n\), with \(B\) reduced modulo \(p^n\). Summing over primitive \(v\) for each primitive \(u\) gives
\[
\mu_n(B)=\frac{p^{2n}N_n(B)-p^{2n-2}N_{n-1}(B)}{p^{n-1}(p-1)},
\]
where \(N_j(B)\) counts primitive \(u\in(\mathbb Z/p^n\mathbb Z)^2\) satisfying \(B^{\mathsf T}u\equiv0\pmod{p^j}\), and \(N_0(B)=p^{2n}-p^{2n-2}\). The formula follows by subtracting the vectors divisible by \(p\) from the complete finite-character orthogonality sum. Reduce \(B\) by Smith operations. For Smith exponents \(a\le b\) truncated at \(n\), the resulting elementary kernel count yields exactly the following nonzero cases:
\[
\begin{array}{c|c}
\text{Smith condition modulo }p^n&\mu_n(B)\\\hline
 a=b=n&U_n\\
 b=n,\ a=n-1&p^{3n-3}(p^2-p-1)\\
 b=n,\ a\le n-2&(p-1)p^{2n+a-1}\\
 a=b=n-1&-(p+1)p^{3n-3}\\
 b=n-1,\ a\le n-2&-p^{2n+a-1}
\end{array}
\]
All remaining cases give zero. The first two rows include boundary \(n=1\) with the empty inequalities interpreted literally. For example, when \(b=n\) and \(a<n\), the primitive solutions to \(B^{\mathsf T}u=0\) modulo \(p^n\) have first coordinate divisible by \(p^{n-a}\) and second coordinate a unit, hence number \((p-1)p^{n+a-1}\). Counting modulo \(p^{n-1}\) analogously proves the corresponding two rows. When both Smith entries are nonzero modulo \(p^{n-1}\), no primitive vector belongs to that kernel. These observations establish every row without invoking any unproved Gauss-sum identity.

**3. Sum the layers.** The character of the level \(p^{k-n}Y\) equals the conductor-\(p^n\) character of \(Y\). Therefore \(\lambda_{a,b}=\sum_{n=1}^k\mu_n(B\bmod p^n)\). The rows with \(n\le a\) sum to \(D_a\); the next possible term, at \(n=a+1\), is either the negative diagonal or the positive unequal-Smith term; the intermediate terms \(a+2\le n\le b\) are positive; and when \(b<k\), the final term at \(n=b+1\) is negative. No later terms survive. This is precisely the displayed four-case eigenvalue formula.

**4. Smith-type multiplicities.** The zero matrix gives one character. Type \(a=b<k\) is \(p^a\) times an invertible matrix modulo \(p^{k-a}\), giving \(p^{4(k-a-1)}|\operatorname{GL}_2(\mathbb F_p)|\). Type \(a<b=k\) is \(p^a\) times a unit-entry rank-one matrix modulo \(p^{k-a}\), giving \(U_{k-a}\). For \(a<b<k\), let \(s=b-a\) and \(n=k-a\). The desired matrices, after dividing by \(p^a\), have a unit entry and determinant valuation exactly \(s\). There are \(U_s p^{4(n-s)}\) matrices with determinant divisible by \(p^s\), of which \(U_{s+1}p^{4(n-s-1)}\) also have determinant divisible by \(p^{s+1}\). Their difference is the stated multiplicity. This exhausts all matrices and verifies the total \(p^{4k}\).

**5. Invertibility and sharp minimum.** If \(a=b<k\), geometric summation gives
\[
\lambda_{a,a}=-\frac{(p+1)(p^{3a+2}+p+1)}{p^2+p+1}<0.
\]
If \(a<b<k\), geometric summation gives
\[
\lambda_{a,b}=-\frac{p^{3a+3}+(p+1)^3+(p^2+p+1)p^{2b+a+2}}{(p+1)(p^2+p+1)}<0.
\]
The first magnitude is minimized at \(a=0\), where it equals \(p+1\), and strictly grows with \(a\). The second magnitude is minimized at \((a,b)=(0,1)\), where it equals \(p^3-p^2+p+1>p+1\). For \(b=k\), all terms in the formula are strictly positive, since \(p^2-p-1\ge1\); for \(k\ge2\), their sum exceeds \(p+1\). The trivial eigenvalue \(D_k\) does likewise. Thus the unique least-magnitude Smith type is \((0,0)\), i.e., the invertible frequency matrices, giving precisely the claimed inverse norm and multiplicity.

## Verification

The standalone `check_spectrum.py` enumerates the adjacency generating sets and obtains independent full Fourier spectra by four-dimensional discrete Fourier transforms at \((p,k)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1)\). For every case, the computed eigenvalue histogram equals the integer Smith-type formula and the observed valency agrees with \(D_k\). It also checks the total multiplicity, nonsingularity, and least absolute eigenvalue for \(p\in\{2,3,5,7\}\) and \(2\le k\le8\). Run `python check_spectrum.py` with Python and NumPy. These finite checks complement, and do not replace, the all-depth argument above.

## Relationship to prior work

Finite-field bilinear-forms schemes have long had character tables in terms of generalized Krawtchouk polynomials (Delsarte). Guo and Li give Smith forms and orbit cardinalities for Galois-ring matrix actions, which help with the multiplicity side but do not in their abstract assert this full character spectrum. Nica's unimodular-graph spectra treat primitive-vector dot-product graphs, not this matrix-additive Cayley graph. Huang and collaborators introduced the corresponding inner-rank-one bilinear-forms graphs over residue-class rings and obtained graph parameters; those results do not state the present all-depth spectral formulas in the accessible material. Watanabe gives a full first eigenmatrix for Smith-type translation schemes over Galois rings of **length two**; thus the auxiliary \(k=2\) case here is potentially implied by that general theorem and is not claimed as a new separate result. The new scope is the explicit complete spectrum and sharp inverse norm uniformly at every length \(k\ge3\), including its elementary factorization derivation.

## Limitations

The graph has fixed matrix size two; higher matrix sizes and non-principal finite rings are not covered. The historical priority check is bounded: a potentially relevant 2017 paper by Huang–Su–Tang–Wang and Guo–Li's 2015 general matrix-orbit paper were only available in abstract/preview form, not full manuscript; a broader earlier result may imply some formulas. Watanabe's 2026 length-two result provides a strong overlap at \(k=2\) but does not cover the stated \(k\ge3\) family. Independent mathematical validation has not been performed.

## References

- B. Nica, *Unimodular graphs and Eisenstein sums*, arXiv:1505.05034 (first posted 2015-05-19), https://arxiv.org/abs/1505.05034.
- L.-P. Huang, *Generalized bilinear forms graphs and MDR codes*, arXiv:1705.07083, https://arxiv.org/abs/1705.07083.
- L.-P. Huang, H. Su, G. Tang, J.-B. Wang, *Bilinear forms graphs over residue class rings*, Linear Algebra and its Applications **523** (2017), 13–32, https://doi.org/10.1016/j.laa.2017.01.032.
- J. Guo and F. Li, *Several Anzahl theorems of matrices over Galois rings and their applications*, Linear Algebra and its Applications **465** (2015), 296–311, https://doi.org/10.1016/j.laa.2014.09.036.
- Y. Watanabe, *Bivariate affine \(q\)-Krawtchouk polynomials and association schemes over Galois rings*, arXiv:2607.21913 (2026), https://arxiv.org/abs/2607.21913.
- P. Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory, Series A **25** (1978), 226–241.
