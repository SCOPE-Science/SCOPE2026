# Sharp theta laws for commuting idempotent tuples in finite triangular algebras

## Finding

Fix a prime power \(q\ge 2\) and an integer \(t\ge2\). Let \(T_n(q)\) be the algebra of upper triangular \(n\times n\) matrices over \(\mathbb F_q\). Choose \(t\) matrices independently and uniformly from its idempotents. Let \(P_{q,t}(n)\) denote the probability that the chosen idempotents commute pairwise.

Put \(r=2^t\), and for an integer \(r\ge2\) set
\[
A_r(n,q)=\sum_{\substack{m_1,\ldots,m_r\ge0\\m_1+\cdots+m_r=n}}
\binom{n}{m_1,\ldots,m_r}\,q^{\sum_{i<j}m_im_j}.
\]
The exact enumeration, valid for every \(n\ge0\), is
\[
\boxed{P_{q,t}(n)=\frac{A_{2^t}(n,q)}{A_2(n,q)^t}.}
\]
This counts ordered, not necessarily distinct, idempotents. The denominator is the number of unrestricted ordered idempotent tuples.

For integers \(r\ge2\) and \(0\le s<r\), define the rank-\((r-1)\) shifted lattice and its positive theta sum by
\[
\Lambda_{r,s}=\left\{(k_1-s/r,\ldots,k_r-s/r):k_i\in\mathbb Z,\ \sum_{i=1}^rk_i=s\right\},
\qquad
\Theta_{r,s}(q)=\sum_{\delta\in\Lambda_{r,s}}q^{-\frac12\sum_i\delta_i^2}.
\]
These sums converge absolutely. Let
\[
\mu_t=\frac{2^t-t-1}{2},\qquad
\kappa_t=\frac{t-2}{4}+\frac{1}{2^{t+1}},
\]
and, for \(0\le s<2^t\),
\[
C_{q,t,s}=\frac{(2^t)^{2^{t-1}-1}}{(2\pi)^{\mu_t}}
\frac{\Theta_{2^t,s}(q)}{\Theta_{2,s\bmod2}(q)^t}.
\]
**Sharp asymptotic theorem.** As \(n\to\infty\) with \(q,t\) fixed,
\[
\boxed{P_{q,t}(n)=C_{q,t,n\bmod 2^t}\,n^{-\mu_t}q^{-\kappa_t n^2}
\left(1+O_{q,t}(n^{-1})\right).}
\]
In particular, for two idempotents,
\[
\boxed{P_{q,2}(n)=\frac{4}{\sqrt{2\pi n}}
\frac{\Theta_{4,n\bmod4}(q)}{\Theta_{2,n\bmod2}(q)^2}
\,q^{-n^2/8}\left(1+O_q(n^{-1})\right).}
\]
The positive leading constant depends only on the residue class of \(n\) modulo \(2^t\); no assertion is made that this is its *minimal* period. In particular, the asymptotic has both a quadratic exponential exponent and a nontrivial power-of-\(n\) correction.

More generally, for any finite poset \(X\), the number of ordered, pairwise commuting \(t\)-tuples of idempotents in its incidence algebra \(I(X,\mathbb F_q)\) is exactly
\[
\boxed{\sum_{c:X\to\{0,1\}^{t}}q^{e_X(c)},\quad
 e_X(c)=\#\{(x,y):x<y\text{ in }X,\ c(x)\ne c(y)\}.}
\]
This identity specializes to \(A_{2^t}(n,q)\) for the \(n\)-point chain.

## Assumptions and scope

The field has exactly \(q\) elements, where \(q\) is any prime power, including characteristic two. The integer \(t\ge2\) is fixed in the asymptotic limit, and matrices may coincide or equal zero or the identity. ``Pairwise commuting'' means every two entries of the ordered tuple commute under usual matrix multiplication. For the poset formula, \(X\) is any finite poset, with incidence-algebra multiplication given by convolution along intervals. An empty poset is allowed for the exact formula; the asymptotic is for chains of increasing positive length only. None of the limits is asserted uniformly when \(q\) or \(t\) varies with \(n\).

## Proof

**1. Simultaneous diagonalization with fixed diagonal.** Let \(R=I(X,\mathbb F_q)\) and \(E_1,\ldots,E_t\in R\) be commuting idempotents. Their diagonal entries belong to \(\{0,1\}\). For every binary vector \(a=(a_1,\ldots,a_t)\), form
\[
Q_a=\prod_{j=1}^t\bigl(a_jE_j+(1-a_j)(1-E_j)\bigr).
\]
The \(Q_a\) are pairwise orthogonal idempotents summing to \(1\). For each \(x\in X\), let \(c(x)\) be the vector of diagonal entries of the \(E_j\) at \(x\). Put \(D_a\) for the diagonal indicator of \(\{x:c(x)=a\}\), and set
\[
U=\sum_aQ_aD_a.
\]
Its diagonal is identically one, so \(U\) is an invertible element of the incidence algebra with diagonal one (a unitriangular unit). Since \(Q_aU=UD_a\), we have
\[
E_jU=U\sum_{a:a_j=1}D_a.
\]
Thus all \(E_j\) are conjugate by the *same* unitriangular matrix to their prescribed diagonal projections. This is also the content of the previously established simultaneous-conjugacy lemma in Garcés--Khrypchenko (2021, Lemma 5.4); the construction above independently supplies the needed precise normalization.

**2. Counting each diagonal fiber.** Let \(G_X\) be the unitriangular group of \(R\), of order \(q^{b_X}\), where \(b_X\) is the number of strict comparable ordered pairs \((x,y)\) of \(X\). Fix a coloring \(c:X\to\{0,1\}^{t}\). Step 1 shows that \(G_X\) acts transitively by simultaneous conjugation on commuting-idempotent tuples with this joint diagonal. A unitriangular \(U\) stabilizes all corresponding diagonal projections exactly when \(U(x,y)=0\) whenever \(x<y\) and \(c(x)\ne c(y)\). The stabilizer therefore has order \(q^{b_X-e_X(c)}\). Orbit--stabilizer gives exactly \(q^{e_X(c)}\) tuples with diagonal coloring \(c\), proving the poset formula.

For a chain, all pairs of positions are comparable. A coloring using \(r=2^t\) colors with multiplicities \(m_1,\ldots,m_r\) has
\[
e_X(c)=\sum_{i<j}m_im_j
 =\tfrac12\left(n^2-\sum_im_i^2\right).
\]
There are \(\binom{n}{m_1,\ldots,m_r}\) such colorings. This proves \(A_r(n,q)\). For one idempotent \(r=2\), so independent uniform sampling gives the stated ratio exactly.

**3. Theta asymptotics of the color sum.** Fix \(r\ge2\) and write \(n=ra+s\), where \(0\le s<r\). For a vector of nonnegative integer multiplicities, write \(m_i=n/r+\delta_i\). The vector \(\delta\) lies in \(\Lambda_{r,s}\), and
\[
\sum_{i<j}m_im_j=\frac{r-1}{2r}n^2-\frac12\sum_i\delta_i^2.
\]
Stirling's formula, uniformly for \(\max_i|\delta_i|\le L_n\), with \(L_n=\sqrt{K\log n}\) and fixed sufficiently large \(K\), gives
\[
\binom{n}{m_1,\ldots,m_r}
=\frac{r^n r^{r/2}}{(2\pi n)^{(r-1)/2}}
\left(1+O_r\left(\frac{1+\sum_i\delta_i^2}{n}
+\frac{(1+\max_i|\delta_i|)^3}{n^2}\right)\right).
\]
This is obtained by expanding \(\log\Gamma(m_i+1)\) at \(n/r\); the linear terms cancel because \(\sum_i\delta_i=0\). The Gaussian theta weight has finite moments of all orders for \(q>1\). Consequently, summing the displayed local error against the weights contributes a relative \(O_{q,r}(n^{-1})\) term.

The omitted part of the lattice does not affect this bound. Indeed every multinomial coefficient is at most \(r^n\), and \(\sum_{\delta:\|\delta\|_\infty>L_n}q^{-\sum\delta_i^2/2}\) decays faster than any prescribed negative power of \(n\) when \(K\) is chosen sufficiently large. Its ratio to the central prefactor is therefore \(o(n^{-1})\). We obtain
\[
\boxed{A_r(n,q)=\frac{r^n r^{r/2}}{(2\pi n)^{(r-1)/2}}
q^{(r-1)n^2/(2r)}\Theta_{r,n\bmod r}(q)
\left(1+O_{q,r}(n^{-1})\right).}
\]
All theta constants are positive, so relative division is valid. Substituting \(r=2^t\) in the numerator and \(r=2\) in each of the \(t\) denominator factors produces the exponent
\[
\frac{r-1}{2r}-\frac{t}{4}=-\left(\frac{t-2}{4}+\frac{1}{2r}\right)=-\kappa_t,
\]
and the power of \(n\) equal to \(-(r-t-1)/2=-\mu_t\). The quotient of central prefactors is precisely \(C_{q,t,s}\). This proves the theorem with its stated quantifiers and error.

## Verification

The standalone `verify.py` directly enumerates actual incidence-algebra elements over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\), filters idempotents by direct multiplication, and tests pairwise commutativity by direct multiplication. It checks chain algebras through size four, including triples, plus two nonchain posets. These direct checks are compared with a separate coloring sum; the latter is also cross-checked against an independent dynamic multinomial convolution. The program ends with `VERIFY_OK` on success.

Illustrative exact values over \(\mathbb F_2\): the number of idempotents for chain sizes \(n=1,2,3,4,5,6\) is \(2,6,26,162,1442,18306\); the corresponding numbers of commuting ordered pairs are \(4,28,340,7108,254404,15531268\). Small finite checks are *not* used in lieu of the infinite proof in Step 3. A companion numerical experiment with the leading theta constant found ratios of exact to leading asymptotic near \(0.77\), \(0.87\), and \(0.91\) at representative chain sizes \(20,41,62\) for \(q=2\), consistent with the proved slow relative \(O(n^{-1})\) convergence; those numerical ratios are not part of the theorem.

## Relationship to prior work

Garcés and Khrypchenko (2021, Lemma 5.4) prove simultaneous conjugacy of commuting idempotents in incidence algebras. This structural result is **prior**, and the proof above credits it explicitly. Hou's 2019 study and Wright's 2020 online article describe and enumerate individual triangular idempotents; the one-idempotent denominator is not presented as new in isolation. Fornaroli, Khrypchenko, and Santulo (2022) study maps preserving commutativity in incidence algebras, not the probability that a uniform tuple of idempotents commutes.

The new mathematical assertion is the **sharp fixed-field, fixed-tuple-size rarity law with residue-dependent theta leading constants** (and the joint-fiber enumeration as a transparent route to it), not simultaneous diagonalizability itself. The exact color sum is equivalent, after extracting a global power of \(q\), to the antiferromagnetic Potts partition function of a complete graph with \(2^t\) colors. The Potts-model interpretation is not by itself a novelty claim; existing statistical-mechanics formulations are a residual priority risk.

## Limitations

The asymptotic is for fixed \(q\) and fixed \(t\) only. It counts all ordered tuples, including repeated matrices and scalar idempotents. It is not a claim about arbitrary full matrix algebras, noncommuting idempotents with idempotent product, or isomorphism classes. A general incidence algebra has an exact coloring formula but need not share the chain's theta asymptotic. The precise leading constant is periodic *at most* with the displayed modulus; minimal period has not been established. Independent external review and complete publication-priority verification have not been performed. Two closely relevant triangular-idempotent papers were located only through abstracts rather than inspectable full texts; this is a residual source-comparison limitation.

## References

1. X. Hou, "Idempotents in triangular matrix rings," *Linear and Multilinear Algebra* **69** (2021), 296–304; first public online March 22, 2019. DOI: https://doi.org/10.1080/03081087.2019.1596223.
2. J. J. Garcés and M. Khrypchenko, "Potent preservers of incidence algebras," arXiv:2110.10676 (first posted October 20, 2021), especially Lemma 5.4 and Section 5.2. https://arxiv.org/abs/2110.10676.
3. É. Z. Fornaroli, M. Khrypchenko, and E. A. Santulo Jr, "Commutativity preservers of incidence algebras," arXiv:2207.10713 (first posted July 21, 2022), especially Sections 1–3. https://arxiv.org/abs/2207.10713.
4. S. E. Wright, "Triangular idempotent matrices over a general ring," *Linear and Multilinear Algebra* **70** (2022), 1717–1731; first public online June 1, 2020. DOI: https://doi.org/10.1080/03081087.2020.1773377.
5. F. Bencs, E. Davies, V. Patel, and G. Regts, "On zero-free regions for the anti-ferromagnetic Potts model on bounded-degree graphs," *Annales de l'Institut Henri Poincaré D* **8** (2021), 459–489. https://arxiv.org/abs/1812.07532. This source supplies the standard Potts partition-function terminology, not the present sharp complete-graph asymptotic.
