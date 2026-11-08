# Sharp negative-dependence phases for cyclic vertices of uniform random mappings

## Finding
For each integer \(n\ge1\), let \(F:[n]\to[n]\) be chosen uniformly among all \(n^n\) maps, with independent uniform images of the labels. A vertex is **cyclic** if some positive iterate of \(F\) returns to it. Write \(I_i=\mathbf1_{\{i\text{ is cyclic}\}}\), and put \(K_n=\sum_{i=1}^n I_i\). The following classification is exact.

1. The exchangeable vector \((I_1,\ldots,I_n)\) is negatively associated if and only if \(n\le3\).
2. For distinct labels \(i,j\), the covariance \(\operatorname{Cov}(I_i,I_j)\) is strictly negative for \(2\le n\le5\), and strictly positive for every \(n\ge6\). In fact
   \[
   n\operatorname{Cov}(I_i,I_j)\longrightarrow 2-\frac\pi2>0.
   \]
3. At both \(n=4\) and \(n=5\), pairwise covariance is negative even though the two coordinatewise increasing observables \(I_1I_2\) and \(I_3I_4\), supported on disjoint sets, have strictly positive covariance. Explicitly,
   \[
   \operatorname{Cov}(I_1I_2,I_3I_4)=
   \begin{cases}
   23/4096,&n=4,\\
   69716/9765625,&n=5.
   \end{cases}
   \]

Thus the loss of negative association occurs precisely at four vertices, whereas the reversal of every pairwise covariance occurs precisely at six vertices. Here negative association means that \(\operatorname{Cov}(f(I_A),g(I_B))\le0\) for every pair of disjoint index sets \(A,B\) and all coordinatewise nondecreasing real functions \(f,g\) on the corresponding Boolean cubes.

## Assumptions and scope
No asymptotic approximation enters the finite claims. All assertions concern uniformly random unrestricted labeled endofunctions, loops permitted, with each of the \(n^n\) functions equally likely. The cases \(n=1\) (negative association vacuous) and \(n=2\) are included. The limiting claim keeps two distinct label positions, which by exchangeability may depend on \(n\).

## Proof
**Exact cyclic-set counting.** Fix a nonempty set \(R\subseteq[n]\) with \(|R|=k\). If \(R\) is exactly the cyclic set, the restriction of \(F\) to \(R\) is an arbitrary permutation (\(k!\) possibilities), and the other vertices form a directed forest whose components terminate at \(R\). For \(1\le k<n\), the directed matrix-tree theorem applied to the complete graph with all roots \(R\) deleted gives the number of such forests as
\[
\det(nI_{n-k}-J_{n-k})=k n^{n-k-1}.
\]
For \(k=n\), the empty forest has one possibility, consistent with the same formula. Consequently,
\[
\Pr(\{i:I_i=1\}=R)=\frac{k\,k!}{n^{k+1}},\qquad
\Pr(K_n=k)=\frac{k(n)_k}{n^{k+1}},\quad 1\le k\le n,
\]
where \((n)_k=n(n-1)\cdots(n-k+1)\). This recovers the classical cyclic-set law; no originality is claimed for this counting identity.

**Covariance reduction.** Put \(a_k=(n)_k/n^k\) for \(1\le k\le n\), set \(a_{n+1}=0\), and define \(M_n=\sum_{k=1}^n a_k\). Since \(a_k-a_{k+1}=k a_k/n=\Pr(K_n=k)\), the tail law is \(\Pr(K_n\ge k)=a_k\). Thus \(\mathbb E K_n=M_n\). The same recurrence gives \(\sum_{k=1}^n k a_k=n\) by telescoping; the factorial-moment tail identity then gives
\[
\mathbb E[K_n(K_n-1)]=2\sum_{k=1}^n(k-1)a_k=2(n-M_n).
\]
Exchangeability yields, for any \(i\ne j\),
\[
\Pr(I_i=1)=\frac{M_n}{n},\quad
\Pr(I_i=I_j=1)=\frac{2(n-M_n)}{n(n-1)},
\]
and therefore
\[
\operatorname{Cov}(I_i,I_j)=
\frac{2(n-M_n)}{n(n-1)}-\frac{M_n^2}{n^2}.
\tag{1}
\]
This is positive exactly when
\[
M_n<T_n:=\frac{2n}{\sqrt{2n-1}+1},
\tag{2}
\]
and negative when the inequality is reversed.

**All-size sign boundary.** Direct substitution gives the exact signs at sizes two through six:
\[
\begin{array}{c|ccccc}
n&2&3&4&5&6\\\hline
\operatorname{Cov}(I_1,I_2)&-1/16&-19/729&-177/16384&-30511/9765625&4391/3779136.
\end{array}
\]
For every remaining integer \(7\le n\le168\), the standard-library rational-arithmetic certificate in `verify.py` checks (1) strictly positive, evaluating \(M_n\) by the recurrence \(a_{k+1}=a_k(n-k)/n\). This is an exhaustive *finite* check over precisely the stated range, not an extrapolation.

To close the infinite range, for \(k\ge1\),
\[
a_k\le\exp\!\left(-\frac{k(k-1)}{2n}\right)
\le\exp\!\left(-\frac{(k-1)^2}{2n}\right).
\]
A comparison of the decreasing Gaussian sum to its integral, together with \(\pi<22/7\), gives
\[
M_n\le1+\sqrt{\frac{\pi n}{2}}<1+\sqrt{\frac{11n}{7}}.
\]
For \(n\ge169\), use the elementary rational bounds \(\sqrt2>707/500\) and \(\sqrt{11/7}<63/50\) to obtain
\[
\sqrt{2n}-\sqrt{11n/7}>
\sqrt n\,\frac{77}{500}\ge\frac{1001}{500}>2.
\]
Hence \(M_n<\sqrt{2n}-1<T_n\), the last inequality following from \(T_n>2n/(\sqrt{2n}+1)>\sqrt{2n}-1\). This proves the sign classification for every \(n\).

Finally, for \(k=O(\sqrt n)\), \(a_k=\exp(-k^2/(2n)+o(1))\) uniformly on fixed rescaled compact intervals. The same Gaussian upper bound controls the tail of the Riemann sums. Therefore \(M_n/\sqrt n\to\int_0^\infty e^{-t^2/2}\,dt=\sqrt{\pi/2}\). Multiplying (1) by \(n\) gives the asserted limit.

**Negative-association boundary.** When \(n=2\), the unique pair has covariance \(-1/16\). At \(n=3\), every increasing real-valued function on two Boolean coordinates is, up to a constant, a nonnegative linear combination of indicators of its proper increasing level sets: the two coordinates, their AND, and their OR. Indeed, subtract its minimum and write the function as the integral of its upper-level-set indicators. Every increasing function of the disjoint singleton coordinate is a nonnegative multiple of that indicator plus a constant. Therefore it suffices to check the following covariances of the four nontrivial two-coordinate upper sets with the remaining coordinate (the two coordinates have equal covariance):
\[
-19/729,\qquad -8/729,\qquad-30/729,
\]
all strictly negative. By exchangeability, this exhausts nontrivial choices of disjoint supports, proving negative association through size three. At \(n=4\), (1) gives pairwise covariance \(-177/16384\), but
\[
\Pr(I_1I_2=1)=19/64,\qquad
\Pr(I_1I_2I_3I_4=1)=3/32,
\]
so \(3/32-(19/64)^2=23/4096>0\). Likewise at \(n=5\), these probabilities are \(778/3125\) and \(216/3125\), giving \(69716/9765625>0\). For every \(n\ge6\), positive pairwise covariance itself violates negative association. The three regimes are exhaustive.

## Verification
`verify.py` is a standalone Python 3 standard-library checker. It performs exact rational sign tests for \(2\le n\le168\), directly enumerates all mappings for \(2\le n\le6\) and checks their one-, two-, and four-vertex cyclicity probabilities where defined, exhausts all monotone Boolean functions of two variables for the \(n=3\) negative-association test, and verifies the finite rational comparisons used in the analytic bound. Its observed result is: `PASS 191 exact assertions; all 2<=n<=168 certified and n>=169 by analytic bound`.

The independent direct map enumeration is finite only; the proof for all larger sizes consists of the exact recurrence, the finite rational certificate, and the analytic Gaussian bound, not the enumeration. The code can be run with `python3 verify.py` from a directory containing that file.

## Relationship to prior work
The exact cyclic-set and cyclic-count laws are classical, including Pitman's 2001 formulas (27)–(29) for general \(p\)-mappings and the 2006 Hansen–Jaworski model's cyclic-point theorem. Those laws provide the mass function used above, but they do not explicitly state the sharp three-phase negative-dependence classification or establish its all-size inequality. The claim here is *only* the qualitative sharp dependence classification, not a novel random-mapping distribution or an improved asymptotic law for cyclic counts. General formulas encode the events involved, so implicit earlier coverage is a genuine priority risk.

## Limitations
The classification uses independent uniform images and need not extend to nonuniform \(p\)-mappings or maps with prescribed indegrees. The full cyclic-set law was known. The sign theorem is a derived structural refinement, and historical priority cannot be guaranteed from the inspected sources alone. The interval \(7\le n\le168\) is discharged by an exact reproducible finite certificate rather than a short symbolic inequality. No external independent scientific audit has been performed.

## References
- J. Pitman, *Random mappings, forests, and subsets associated with Abel–Cayley–Hurwitz multinomial expansions*, Séminaire Lotharingien de Combinatoire 46 (2001), Article B46h, especially (27)–(29). https://www.mat.univie.ac.at/~slc/s/s46pitman.pdf. Public technical-report record dated 2001-06-01: https://statistics.berkeley.edu/tech-reports/593.
- J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529, first submitted 2006-03-22, especially Sections 1, 3 and conclusion. https://arxiv.org/abs/math/0603529.
- M. Drmota, *Correlations on the strata of a random mapping*, Random Structures & Algorithms 6 (1995), 357–365. https://doi.org/10.1002/rsa.3240060223. This concerns aggregate stratum counts and was accessible only as bibliographic information and abstract for the present comparison.
