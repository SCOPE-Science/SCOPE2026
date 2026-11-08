# Support-independent Fourier zero counts at the critical moment-curve degree

## Finding
Fix an integer \(r\ge 2\) and a prime \(p\ge 2r+1\). Choose any two disjoint \(r\)-element subsets \(A,B\subset\mathbb F_p\). For \(\boldsymbol a=(a_1,\ldots,a_{2r-1})\in\mathbb F_p^{2r-1}\), put
\[
F_{A,B}(\boldsymbol a)=\sum_{x\in A}\exp\!\left(\frac{2\pi i}{p}\sum_{j=1}^{2r-1}a_jx^j\right)-\sum_{x\in B}\exp\!\left(\frac{2\pi i}{p}\sum_{j=1}^{2r-1}a_jx^j\right).
\]
The number of frequencies at which this signed Fourier sum vanishes depends only on \(r\) and \(p\), not on either support's locations. In fact,
\[
\#\{\boldsymbol a:F_{A,B}(\boldsymbol a)=0\}
=\sum_{t=1}^{r}B_{r,t}\prod_{j=1}^{t-1}(p-j),\qquad
B_{r,t}=\frac{(r!)^2}{t!}
\sum_{\substack{m_1,\ldots,m_t\ge1\\m_1+\cdots+m_t=r}}
\prod_{i=1}^{t}(m_i!)^{-2}.
\]
Here an empty product is one. The integer \(B_{r,t}\) is the number of partitions of the \(2r\) labelled support positions into \(t\) nonempty blocks, each containing equally many positive and negative positions. Thus the zero count is a polynomial in \(p\) of degree \(r-1\), with leading coefficient \(r!\). In particular, for \(r=2\) it is \(2p-1\), for \(r=3\) it is \(6p^2-9p+4\), and for \(r=4\) the coefficients \((B_{4,1},B_{4,2},B_{4,3},B_{4,4})\) are \((1,34,72,24)\).

## Assumptions and scope
The field is the prime field \(\mathbb F_p\); the sign coefficients are exactly \(+1\) on \(A\) and \(-1\) on \(B\), with \(|A|=|B|=r\) and \(A\cap B=\varnothing\). The ambient Fourier set is the degree-\((2r-1)\) moment curve \(x\mapsto(x,x^2,\ldots,x^{2r-1})\). Frequencies include zero and are counted without quotient by a scalar or affine symmetry. The restriction \(p\ge2r+1\) supplies \(2r\) pairwise distinct support nodes and a nondegenerate polynomial evaluation system. The result is not a claim for general complex coefficients, nonprime fields, lower polynomial degrees, or arbitrary frequency curves.

## Proof
**Cyclotomic reduction.** For a fixed frequency, set \(u_x=\sum_{j=1}^{2r-1}a_jx^j\in\mathbb F_p\) and let \(c_s\) be the number of positive positions with \(u_x=s\), minus the number of negative positions with that value. The vanishing condition is \(\sum_{s=0}^{p-1}c_s\zeta_p^s=0\), with \(\zeta_p=e^{2\pi i/p}\). The minimal polynomial of \(\zeta_p\) over \(\mathbb Q\) is \(1+X+\cdots+X^{p-1}\), so all \(c_s\) agree. Their sum is zero because there are equally many positive and negative positions; hence all \(c_s=0\). Conversely, vanishing of every \(c_s\) plainly makes the sum zero. Therefore a frequency is a zero exactly when the positive and negative lists of polynomial evaluations are equal as multisets.

**Evaluation hyperplane.** Order the \(2r\) distinct nodes as \(x_1,\ldots,x_{2r}\), positives first. The map from coefficients to evaluation vectors,
\[
E:\mathbb F_p^{2r-1}\longrightarrow\mathbb F_p^{2r},\quad
\boldsymbol a\longmapsto(f_{\boldsymbol a}(x_1),\ldots,f_{\boldsymbol a}(x_{2r})),\qquad f_{\boldsymbol a}(X)=\sum_{j=1}^{2r-1}a_jX^j,
\]
is injective: a nonzero polynomial of degree at most \(2r-1\) cannot vanish at \(2r\) distinct points. Lagrange interpolation identifies its image as the hyperplane
\[
H=\left\{\boldsymbol v:\sum_{i=1}^{2r}\lambda_i v_i=0\right\},\qquad
\lambda_i=\prod_{j\ne i}\frac{-x_j}{x_i-x_j}.
\]
Indeed the displayed functional is the constant term of the unique interpolating polynomial of degree at most \(2r-1\). Since it evaluates the constant polynomial one to one, \(\sum_i\lambda_i=1\).

**Orbit transversality.** Let \(Y\subset\mathbb F_p^{2r}\) consist of vectors whose first and last \(r\) coordinates have the same multiset of values. The diagonal translation \(\boldsymbol v\mapsto\boldsymbol v+c(1,\ldots,1)\) preserves \(Y\), acts freely on it, and changes the defining linear functional of \(H\) by precisely \(c\). Every translation orbit in \(Y\) therefore meets \(H\) once. Thus \(|Y\cap H|=|Y|/p\), independently of all node locations. By injectivity of \(E\), \(|Y\cap H|\) is exactly the required Fourier zero count.

**Balanced-partition enumeration.** For \(\boldsymbol v\in Y\), its fibers under the map from labelled positions to the distinct coordinate values form a partition into \(t\) balanced blocks. A balanced partition of size pattern \((m_1,\ldots,m_t)\) is obtained by independently splitting the positive and negative positions into blocks of these sizes, then pairing the blocks. After dividing by \(t!\) to forget the block ordering, the number is exactly \(B_{r,t}\). Assigning \(t\) different field values to these blocks has \(p(p-1)\cdots(p-t+1)\) choices. Hence \(|Y|=\sum_t B_{r,t}(p)_t\), and dividing by \(p\) proves the formula. The singleton-pair partition has \(B_{r,r}=r!\), giving the leading coefficient.

## Verification
Run `python3 CHECK.py` with the standard Python 3 library. The script directly enumerates all frequency vectors for six instances up to \(p=11\); it also counts balanced vectors intersecting the Lagrange hyperplane independently in four instances, including two different eight-node configurations at \(p=11\). It confirms the coefficients \((1,34,72,24)\) at \(r=4\). As a boundary test, lowering degree from five to four at \(r=3,p=11\) gives, respectively, \(141\), \(51\), and \(231\) zeros for the signed supports \((A,B)=(\{0,1,2\},\{3,4,5\})\), \((\{0,1,2\},\{3,4,6\})\), and \((\{0,1,3\},\{2,4,5\})\). Thus location independence cannot simply be asserted one degree lower. The proof covers all admissible \(r,p\), not merely the checked examples.

## Relationship to prior work
Biswas, Carneiro, Flock, Oliveira e Silva, Stovall and Tautges analyze endpoint extension estimates for finite-field moment curves by converting equality of power sums into multiset coincidences of varying tuples [1]. Their subsequent paper gives a probabilistic extremal principle for the same extension problem [2]. These establish the setting and related multiset combinatorics, but the claim here concerns the *zero set of a fixed signed support* as the polynomial phase varies, and requires the support-independent evaluation-hyperplane orbit argument. Li's finite-parabola work gives uncertainty bounds and rigidity for general complex coefficients in degree two [3]; the present theorem is a separate exact signed-coefficient statement at degree \(2r-1\). The balanced partition counting ingredient and cyclotomic minimal-polynomial fact are standard; novelty is claimed only for their combined support-independent Fourier zero law and the indicated lower-degree boundary.

## Limitations
This is a fixed-sign theorem over prime fields and not an uncertainty bound for all complex coefficients. The result does not prove degree \(2r-1\) is the minimal threshold for every \(r\); the explicit degree-four failure establishes a boundary at \(r=3\) only. Existing multiset-counting results may imply parts of the enumeration by a different route; an older unindexed equivalent conditional zero-count formula cannot be excluded. A full comparison with some highly relevant 2026 manuscripts was impeded by lack of full-text access; those sources should be checked before claiming publication priority.

## References
[1] C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall, J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377 (first public 2025-08-11).

[2] C. Biswas et al., *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882 (first public 2026-09-24).

[3] D. Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030 (first public 2026-09-11).
