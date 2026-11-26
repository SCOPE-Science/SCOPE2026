# Exact ternary length-two multispectrum enumeration and reconstruction code size

## Finding

Let \(\Sigma=\{0,1,2\}\). For every integer \(n\ge1\) and word \(w=w_1\cdots w_n\in\Sigma^n\), define its *linear ordered-pair multispectrum* by the integer matrix
\[
B(w)_{ij}=\#\{t:1\le t<n,\ (w_t,w_{t+1})=(i,j)\},\qquad i,j\in\Sigma.
\]
Write \(a_n=\#\{B(w):w\in\Sigma^n\}\). Then, as an identity of formal power series,
\[
\boxed{\sum_{n\ge1}a_n z^{n-1}=\frac{P(z)}{(1-z)^7(1+z)^2(1+z+z^2)}}
\]
with
\[
P(z)=1+5z-8z^2+8z^3+13z^4-4z^5-10z^6-8z^7+11z^8+2z^9-5z^{10}+2z^{11}.
\]
The first values \(a_1,\ldots,a_{15}\) are
\[
1,9,24,65,156,342,683,1272,2226,3708,5919,9120,13625,19827,28188.
\]
For \(n\ge2\), the sequence is a degree-six quasipolynomial with *exact* period six. In particular,
\[
a_n=\frac{7}{8640}n^6+O(n^5).
\]
A code \(\mathcal C\subseteq\Sigma^n\) is uniquely decodable from its complete, unordered multiset of length-two **contiguous** substrings exactly when distinct codewords have distinct \(B\)-matrices. The maximum possible size of such a code is **exactly** \(a_n\) for every \(n\): select one word from each nonempty fiber of \(B\).

## Assumptions and scope

The alphabet has three **labeled** symbols. Pair counts are directed: \(01\) and \(10\) are different reads. The word is *linear*, not cyclic: no pair crosses from position \(n\) to position \(1\). Repeated reads retain multiplicities. The read multiset contains all \(n-1\) consecutive pairs, without observation error, and no start/end marker. When \(n=1\), all three words yield the single empty matrix, giving \(a_1=1\). Every assertion holds for all positive integers \(n\).

## Proof

Put \(m=n-1\). A nonnegative integer matrix \(B=(b_{ij})\) with \(\sum b_{ij}=m\) occurs as \(B(w)\) precisely when the directed multigraph having \(b_{ij}\) arcs from \(i\) to \(j\) has an Euler trail. For \(m>0\), this requires that the vertices incident to arcs form a weakly connected graph and that the vector of outdegree minus indegree is either identically zero or has one \(+1\), one \(-1\), and all remaining entries zero; these conditions are also sufficient by the Euler-trail criterion. Loops affect neither the degree imbalances nor connectivity between distinct vertices.

Enumerate matrices by the number of incident vertices. For \(m=0\), there is just the zero matrix. With one incident vertex, there must be a positive multiplicity of its loop; the generating function is \(3z/(1-z)\). With exactly two incident vertices, their directed cross-arcs must have counts \((a,b)\) satisfying \(a+b>0\) and \(|a-b|\le1\). Their total generating function is \((2z+z^2)/(1-z^2)\). Each vertex admits any loop count, independently; summing over the three unordered vertex pairs gives
\[
G_2(z)=\frac{3(2z+z^2)}{(1-z^2)(1-z)^2}.
\]

For all three incident vertices, orient the triangle of unordered pairs as \(0\to1\), \(1\to2\), \(2\to0\). On the \(r\)-th oriented pair, let \(f_r\) be the forward-arc multiplicity minus the backward-arc multiplicity. For any prescribed integer \(f\), the ordered pairs of nonnegative forward/backward multiplicities with difference \(f\) have generating function \(z^{|f|}/(1-z^2)\): a minimal contribution of \(|f|\) arcs and any number of paired extra arcs. The three pairs are independent once their differences are fixed.

A closed Euler trail requires \(f_1=f_2=f_3=t\) for some \(t\in\mathbb Z\). Summing all such three-pair arc matrices before imposing connectivity gives
\[
\frac{1+z^3}{(1-z^3)(1-z^2)^3},
\]
because \(\sum_{t\in\mathbb Z}z^{3|t|}=(1+z^3)/(1-z^3)\). The **disconnected** choices are exactly \(t=0\) with no nonzero cross-pair or with precisely one nonzero cross-pair. Their generating function is \(1+3z^2/(1-z^2)\). Thus the connected balanced three-vertex cross-arc generating function is
\[
H_0(z)=\frac{1+z^3}{(1-z^3)(1-z^2)^3}-1-\frac{3z^2}{1-z^2}.
\]

For a prescribed *distinct* initial vertex and terminal vertex, an alphabet relabeling lets us take these as \(0\) and \(1\). The degree requirements then give \((f_1,f_2,f_3)=(t+1,t,t)\) for some integer \(t\). Since
\[
\sum_{t\in\mathbb Z}z^{|t+1|+2|t|}=\frac{z+z^2}{1-z^3},
\]
the unrestricted generating function for such cross-arc matrices is \((z+z^2)/((1-z^3)(1-z^2)^3)\). The only disconnected cases have \(t=0\), with cross-arcs confined to the ordered pair from the initial to the terminal vertex; their generating function is \(z/(1-z^2)\). Therefore the connected open-trail contribution for **one** ordered endpoint pair is
\[
H_1(z)=\frac{z+z^2}{(1-z^3)(1-z^2)^3}-\frac{z}{1-z^2}.
\]
There are six ordered pairs of distinct endpoints, each determined uniquely by the imbalance vector, so no such matrices are counted twice. In the balanced class the endpoint is not marked, likewise preventing overcounting.

After requiring connected cross-arcs, every one of the three vertices is incident to a cross-arc; the loop counts can now be chosen independently at all three vertices, contributing \((1-z)^{-3}\). Assembling the disjoint classes, the desired generating function is
\[
G(z)=1+\frac{3z}{1-z}
+\frac{3(2z+z^2)}{(1-z^2)(1-z)^2}
+\frac{H_0(z)+6H_1(z)}{(1-z)^3}.
\]
Expanding and combining these rational terms gives exactly the displayed quotient with numerator \(P(z)\). This establishes the identity for **every** \(n\), without relying on finite enumeration.

The denominator factors have poles only at \(1\), \(-1\), and the primitive third roots of unity. The pole at \(1\) has order seven, and the poles at \(-1\) and at the primitive third roots are nonremovable, so for all \(n\ge2\) the coefficient is a degree-six quasipolynomial of least period \(\mathrm{lcm}(2,3)=6\). The rational function has a degree-zero polynomial part affecting only \(n=1\). Finally,
\[
\lim_{z\to1}(1-z)^7G(z)=\frac{7}{12},
\]
and the transfer of coefficients of \((1-z)^{-7}\) yields \(a_n\sim (7/12)n^6/6!=7n^6/8640\). The maximum-code-size statement follows by choosing exactly one representative from each observation fiber.

## Verification

The self-contained program `verify.py` computes coefficients directly from the displayed rational generating function by integer polynomial recurrence. Independently, it enumerates all ternary words through length eleven, and enumerates every nonnegative \(3\times3\) matrix with total arc multiplicity up to twelve, testing degree imbalances and weak connectivity without invoking the generating-function decomposition. Its two independent exhaustive comparisons agree with the coefficients. To reproduce: `python3 verify.py`. Computations corroborate the proof; they do not substitute for the unbounded Euler-trail argument.

## Relationship to prior work

The linear length-two read multispectrum is the classical order-one *Markov type* and a special case of the substring-profile channel. Jacquet, Knessl, and Szpankowski give a generating-function analysis for **balanced/cyclic** frequency matrices and asymptotic counts; their connectedness conventions and cyclic scope do not supply this exact linear three-symbol series. Drmota and Szpankowski, *Analytic Information Theory*, Chapter 11, §11.2.2, explicitly distinguish noncyclic types and give identity (11.40) and **asymptotic** Corollary 11.2.8; those results imply the leading constant in the present theorem but not the exact finite-length coefficients or the six-period correction. The earlier finite-profile results of Chang et al. prove exact enumeration in the range \(\ell\le n<2\ell\), which for read length two includes only \(n=2,3\). Gabrys and Milenkovic study reconstruction codes for read lengths on a logarithmic scale, rather than this exact fixed-read-length ternary maximum. Earlier exact circular ternary multispectrum enumeration also concerns closed balanced trails, not the distinct-endpoint matrices counted here.

## Limitations

The result concerns only three labeled symbols, contiguous directed reads of length exactly two, complete multiplicity observations and a noiseless linear source. It gives the **cardinality** of an optimum distinguishing code through a choice of fiber representatives; it does not assert an efficient encoder, a unique optimal code, an optimum under errors, or formulas for arbitrary alphabet size or longer reads. The leading-order asymptotic is already implied by earlier Markov-type theory; the substantive contribution is the exact all-length generating function and its finite-length reconstruction capacity. Literature comparisons do not rule out an unindexed equivalent closed formula.

## References

- P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, Discrete Mathematics & Theoretical Computer Science (AofA 2010), DOI 10.46298/dmtcs.2768; see especially the balanced ternary generating function.
- W. Szpankowski and M. Drmota, *Analytic Information Theory: From Compression to Learning*, Chapter 11, §§11.2.1–11.2.2 (2022 online manuscript), https://www.cs.purdue.edu/homes/spa/temp/ait22.pdf.
- Z. Chang, J. Chrisnata, M. F. Ezerman, and H. M. Kiah, *Rates of DNA Sequence Profiles for Practical Values of Read Lengths*, arXiv:1607.02279 (first public 2016-07-08).
- R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (first public 2018-04-12).
- M. Marcovich and E. Yaakobi, *Reconstruction of Strings from their Substrings Spectrum*, arXiv:1912.11108 (first public 2019-12-23).
