# Spanning-tree asymptotics for \(q\)-ary 2-Abelian palindromes

## Finding

For a labeled alphabet \(\Sigma_q=\{0,\ldots,q-1\}\) with any fixed integer \(q\ge2\), a word is a *2-Abelian palindrome* when it has the same contiguous-factor multiplicities of lengths one and two as its reversal. Write \(A_q(n)\) for the number of indexed length-\(n\) such words. Let \(d=\binom{q-1}{2}\). Then, as \(n\to\infty\) with \(q\) fixed,

\[
\boxed{\frac{A_q(n)}{q^n}\sim
\frac{q^{d-1+(q-2)/2}}{(2\sqrt\pi)^d(n-1)^{d/2}}.}
\]

The numerator contains \(\sqrt{q^{q-2}}\), the square root of the number of spanning trees of the complete labeled graph. In particular, the decay exponents for alphabets of sizes two, three and four are respectively \(0,1/2,3/2\). The boundary is exact: \(A_2(n)=2^{n-1}\) for \(n\ge2\). For three letters there is also an exact formula,

\[
A_3(n)=3\sum_{j=0}^{\lfloor(n-1)/2\rfloor}\binom{n-1}{2j}\binom{2j}{j}\qquad(n\ge1).
\]

The all-alphabet asymptotic with the explicit constant is the principal claim. The ternary identity is an auxiliary illustration of the method and is not asserted to be historically new on its own.

## Assumptions and scope

Words are indexed, ordinary finite words with no cyclic wrapping; adjacent-pair counts refer to the \(n-1\) ordinary consecutive pairs. All letters are labeled, and \(q\) is fixed before letting \(n\) grow. A reversal changes the count of directed pair \(ab\) to that of \(ba\), and leaves each single-letter count unchanged. Consequently the defining condition is exactly

\[
N_{ab}(w)=N_{ba}(w)\quad\text{for all distinct letters }a,b.
\]

The probabilistic denominator \(q^n\) is the total number of length-\(n\) words. No statement about higher \(k\)-Abelian equivalences, nonuniform letter laws or growing alphabets is implied.

## Proof

**1. Closed walks and cycle currents.** The difference between the number of transitions leaving a symbol and entering it is the indicator that the first letter equals that symbol minus the indicator that the last does. Thus symmetric directed pair counts imply equal first and last symbols. An indexed word is accordingly a rooted closed walk of length \(L=n-1\) in the complete \(q\)-vertex graph with one loop at each vertex. Fix the star tree with edges \(\{0,i\}\) for \(i>0\), and orient each other edge \(\{i,j\}\), \(1\le i<j\le q-1\), from \(i\) to \(j\). There are \(d=\binom{q-1}{2}\) such cotree edges. A closed walk has zero net current on every edge if and only if it has zero current on the cotree edges: after subtracting the latter, its divergence-free current is supported on a tree and must vanish.

**2. Exact Fourier representation.** For \(\theta\in[-\pi,\pi]^d\), define the Hermitian matrix \(H(\theta)\) with diagonal entries \(1\), star-edge entries \(1\), and cotree entries \(H_{ij}=e^{\mathrm i\theta_{ij}}\), \(H_{ji}=e^{-\mathrm i\theta_{ij}}\). Fourier orthogonality counts exactly the rooted closed walks with vanishing cotree currents:

\[
A_q(n)=\frac1{(2\pi)^d}\int_{[-\pi,\pi]^d}\operatorname{tr}(H(\theta)^L)\,d\theta.
\]

For \(d=0\), the integral means evaluation of the constant integrand. It gives the exact binary formula immediately.

**3. Unique spectral maximum.** Since each matrix entry has absolute value one, all eigenvalues have modulus at most \(q\). A diagonal entry is positive, so the Gershgorin lower bound is \(2-q\), ruling out an eigenvalue of modulus \(q\) on the negative side. Equality in the upper bound requires the edge phases to be gauge-equivalent to unity. Since every star-edge phase is already zero, this forces all \(\theta_{ij}=0\pmod{2\pi}\). Thus the top eigenvalue \(\lambda(\theta)\) is simple near the origin, equals \(q\) only there, and other spectral contributions are exponentially smaller away from a neighborhood of the origin.

**4. Quadratic form and determinant.** Let \(E\) be the full set of \(\binom q2\) unoriented non-loop edges. Let \(D\) be the vertex-edge incidence matrix on \(E\), and \(P\) the orthogonal projection of \(\mathbb R^E\) onto \(\ker D\). Embed the \(d\) cotree coordinates in \(\mathbb R^E\) by setting star coordinates to zero, and call this embedding \(J\). Expanding the normalized Rayleigh quotient around its uniform eigenvector and minimizing the second-order energy over vertex phases gives

\[
\lambda(\theta)=q-\frac1q\theta^{\mathsf T}G\theta+O_q(\|\theta\|^4),
\qquad G=J^{\mathsf T}PJ.
\]

The absence of odd-order terms follows because \(H(-\theta)=\overline{H(\theta)}\), so the simple eigenvalue is an even analytic function. To calculate \(G\), form a fundamental-cycle matrix \(F\) with one column for each cotree edge \(ij\); that column has coefficient \(+1\) on edges \(0i\) and \(ij\), coefficient \(-1\) on \(0j\), and zero elsewhere. Its columns span \(\ker D\), and the cotree block of \(F\) is the identity. Hence

\[
P=F(F^{\mathsf T}F)^{-1}F^{\mathsf T},\qquad
G=(F^{\mathsf T}F)^{-1}.
\]

Let \(C\) be the incidence matrix of the complete graph on vertices \(1,\ldots,q-1\). Then \(F^{\mathsf T}F=I_d+C^{\mathsf T}C\) and, by Sylvester's determinant identity and the complete-graph Laplacian identity,

\[
\det(F^{\mathsf T}F)
=\det(I_{q-1}+CC^{\mathsf T})
=\det(qI_{q-1}-\mathbf1\mathbf1^{\mathsf T})
=q^{q-2}.
\]

Thus \(G\) is positive definite with \(\det G=q^{-(q-2)}\). The determinant is also Cayley's complete-graph spanning-tree count, here proved directly by eigenvalues.

**5. Gaussian asymptotic.** Near the origin,

\[
(\lambda(\theta)/q)^L
=\exp\!\left(-\frac L{q^2}\theta^{\mathsf T}G\theta+O_q(L\|\theta\|^4)\right).
\]

The compact spectral gap from Step 3 and positive definiteness of \(G\) justify multivariate Laplace asymptotics. The Gaussian integral contributes

\[
\frac{A_q(n)}{q^L}\sim
\frac1{(2\pi)^d}\left(\frac{\pi q^2}{L}\right)^{d/2}(\det G)^{-1/2}
=\frac{q^{d+(q-2)/2}}{(2\sqrt\pi)^dL^{d/2}}.
\]

Dividing by \(q\) and substituting \(L=n-1\) proves the stated probability formula. For \(q=2\) the graph has no cycles and the same formula holds exactly, with the convention that an empty product is one.

**6. Ternary exact specialization.** For three letters, encode each consecutive pair by the increment \(0,+1,-1\) around the three-symbol cyclic ordering. A word is uniquely determined by its first symbol and its \(L\) increments. Its directed pair counts are symmetric precisely when the signed sum of those increments is zero (the closed-walk congruence follows automatically). Choosing \(j\) positive, \(j\) negative and \(L-2j\) zero increments yields the displayed central-trinomial sum.

## Verification

`verify_exhaustive.py` checks the equivalence between the original pair-multiplicity condition and the cotree-current criterion for every word through lengths nine (two symbols), ten (three), nine (four), and seven (five), and independently checks the ternary binomial identity. `verify_transfer.py` uses a second dynamic-programming method over signed cotree currents, testing additional values up to length twenty-two for three letters and twenty for four letters. The exact determinant identity has also been checked symbolically for alphabet sizes three through seven. These finite checks verify instances and algebraic implementation details; the infinite-range statement follows from the analytic proof.

## Relationship to prior work

Huova and Karhumäki introduced the relevant \(k\)-Abelian framework and studied repetition avoidance. Karhumäki, Saarela and Zamboni established broader \(k\)-Abelian equivalence and complexity theory. Karhumäki and Puzynina, and later Cassaigne, Karhumäki and Puzynina, studied \(k\)-Abelian palindromic rich and poor infinite words and counts of *distinct palindromic factors within hosts*, rather than the ambient alphabet-wide fixed-length count here. Saarela's Section 6 explicitly counts *equivalence classes* containing (\(k,S\))-palindromes, not the number of individual \(q\)-ary \(2\)-Abelian palindromic words of prescribed length or their spanning-tree asymptotic. The ternary reductions in the accessible presentation are compatible with the exact ternary illustration and may subsume that illustration. The main asymptotic does not follow from these cited statements without additional local spectral analysis.

## Limitations

Historical priority is qualified. The full 2014 conference paper on \(k\)-Abelian palindromic rich and poor words was not obtained, although its public abstract and a related complete presentation were inspected; an equivalent older result in another terminology cannot be ruled out. A subsequent 2018 study is relevant to conceptual background but its inspected abstract concerns infinite-word richness and poverty, not the all-alphabet census. The proof treats a fixed finite uniform alphabet and \(k=2\) only. Its agreement with finite enumerations is a check, not a proof of a limit. No independent mathematical audit has yet occurred.

## References

1. M. Huova and J. Karhumäki, *Observations and Problems on k-abelian Avoidability*, arXiv:1104.4273, first public 2011-04-21, https://arxiv.org/abs/1104.4273.
2. J. Karhumäki, A. Saarela and L. Q. Zamboni, *On a Generalization of Abelian Equivalence and Complexity of Infinite Words*, arXiv:1301.5104, first public 2013-01-22, https://arxiv.org/abs/1301.5104.
3. J. Karhumäki and S. Puzynina, *On k-Abelian Palindromic Rich and Poor Words*, DLT 2014, DOI 10.1007/978-3-319-09698-8_17, https://doi.org/10.1007/978-3-319-09698-8_17.
4. A. Saarela, *Equivalence Relations Defined by Numbers of Occurrences of Factors*, *Fundamenta Informaticae*, Section 6, https://amsaar.gitlab.io/articles/sa16fi.pdf.
5. J. Cassaigne, J. Karhumäki and S. Puzynina, *On k-Abelian Palindromes*, publicly accessible conference presentation, https://www.cirm-math.fr/ProgWeebly/Renc1429/Puzynina.pdf; later journal treatment, DOI 10.1016/j.ic.2018.04.001.
