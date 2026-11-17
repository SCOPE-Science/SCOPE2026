# Triangular-partition law and sharp quadratic stabilization for scattered \(001\)

## Finding
For a binary word \(w\), let \(c_{001}(w)\) denote the number of triples of positions \(i<j<h\) spelling \(001\), and let
\[B_{001}(n,k)=\big|\{w\in\{0,1\}^n:c_{001}(w)=k\}\big|.\]
Fix any \(k\ge1\). Define the finite set \(\mathcal P_\triangle(k)\) of vectors \(\mathbf r=(r_2,r_3,\ldots)\) of nonnegative integers with finite support such that
\[\sum_{j\ge2}\binom j2 r_j=k.\]
For each vector let \(J=\max\{j:r_j>0\}\), let \(\ell=\sum_{j\ge2}r_j\), and let \(d=J+\ell\). Define the polynomial
\[P_k(z)=\sum_{\mathbf r\in\mathcal P_\triangle(k)}z^{d(\mathbf r)}.\]
The **exact all-length generating function**, with \(k\) fixed, is
\[\sum_{n\ge0}B_{001}(n,k)z^n=\frac{P_k(z)}{(1-z)^3}.\]
For **every** \(n\ge k\), the count is exactly the quadratic polynomial
\[B_{001}(n,k)=\frac12\sum_{\mathbf r\in\mathcal P_\triangle(k)}(n-d(\mathbf r)+2)(n-d(\mathbf r)+1).\]
The quadratic leading coefficient is \(|\mathcal P_\triangle(k)|/2\), the number of unrestricted partitions of \(k\) into positive triangular numbers \(1,3,6,10,\ldots\), divided by two. This threshold is optimal uniformly and individually in the following strong sense: at \(n=k-1\), the same polynomial evaluates to \(B_{001}(k-1,k)+1\).

## Assumptions and scope
All binary words are indexed linear words, and occurrences are *scattered* subsequences (not contiguous factors). The parameter \(k\) is any positive integer; lengths \(n\) are nonnegative. All sums defining \(P_k\) are finite because a nonzero part \(r_j\) requires \(\binom j2\le k\). The quadratic polynomial is evaluated in the usual algebraic sense outside its valid range; the exact rational generating function holds for every \(n\ge0\). Reversal/complementation preserve counts and transport the result from \(001\) to its symmetry class \(\{001,011,100,110\}\). No claim is made for \(k=0\) or the distinct three-run patterns \(010,101\).

## Proof
**1. Unique zero-gap decomposition and occurrence weight.** A word with \(t\) zeros is uniquely represented by
\[w=1^{a_0}0\,1^{a_1}0\cdots0\,1^{a_t},\qquad a_j\ge0.\]
Each one in the gap after precisely \(j\) zeros contributes \(\binom j2\) scattered copies of \(001\), by choosing two earlier zeros. Hence
\[c_{001}(w)=\sum_{j=2}^t\binom j2a_j.\]
If this count is \(k>0\), at least one \(a_j>0\) with \(j\ge2\). The positive-weight coordinates \((a_2,a_3,\ldots,a_t)\), extended by zero thereafter, determine one vector \(\mathbf r\in\mathcal P_\triangle(k)\), whose maximum occupied gap is \(J\). The remaining freedom is precisely the initial two one-gap multiplicities \(a_0,a_1\) and the number \(h=t-J\) of zeros following the last occupied positive-weight gap. Each is independently an arbitrary nonnegative integer. Conversely, these choices uniquely reconstruct the original word; there is no quotienting or overcounting.

**2. Exact generating function.** For a fixed \(\mathbf r\), the obligatory \(J\) zeros and \(\ell=\sum r_j\) positively weighted ones contribute word length \(d=J+\ell\). The three independent free variables \(a_0,a_1,h\) add length \(a_0+a_1+h\). Their length generating series is \((1-z)^{-3}\). Summing over the unique profiles yields the claimed identity. In particular the exact all-length coefficient is
\[B_{001}(n,k)=\sum_{\mathbf r\in\mathcal P_\triangle(k):\,d(\mathbf r)\le n}\binom{n-d(\mathbf r)+2}{2},\]
where the binomial coefficient is its ordinary combinatorial value for nonnegative arguments.

**3. Maximal core and sharp polynomial onset.** The sole profile with \(J=2\) is \(r_2=k\), yielding \(d=k+2\) and coefficient one in \(P_k\). For any other profile \(J\ge3\), at least one part has weight \(\binom J2\). Since every other part weighs at least one,
\[\ell\le k-\binom J2+1,\qquad d=J+\ell\le k+J+1-\binom J2\le k+1.\]
Therefore \(\deg P_k=k+2\) with leading coefficient one. For \(n\ge k\), every profile of degree \(d\le n\) contributes the quadratic binomial polynomial as above, and any possible profile with \(d=n+1\) or \(d=n+2\) contributes zero to that polynomial. Thus the sum of *all* profile polynomials equals the exact coefficient whenever \(n\ge k\). At \(n=k-1\), all profiles of degree \(d\le k+1\) still contribute exactly their combinatorial coefficient (possibly zero). The unique degree-\(k+2\) profile contributes zero to the actual count but contributes \(\frac12(-1)(-2)=1\) to its polynomial. The preboundary discrepancy is therefore exactly one, establishing sharpness.

**4. Degree and leading coefficient.** The finite set \(\mathcal P_\triangle(k)\) is nonempty because \(r_2=k\) is allowed. Every one of its terms contributes quadratic leading coefficient \(1/2\). Thus the total polynomial has exact degree two and leading coefficient \(|\mathcal P_\triangle(k)|/2\). The defining vectors are exactly partitions of \(k\) into positive triangular numbers \(\binom j2\), with unlimited multiplicity. This completes the proof.

## Verification
The standalone Python 3 program `verify_scattered001.py` runs three independent numerical checks. It compares the triangular-profile enumeration against direct binary-word enumeration for \(0\le n\le13\) and \(1\le k\le20\); compares it against an independent streaming dynamic program for \(0\le n\le48\) and \(1\le k\le15\); and verifies the sharp polynomial onset and one-unit discrepancy for \(1\le k\le40\). It reports `PASS direct=280; independent_dp=735; eventual_quadratic=240; sharp_preboundary=40`. These are finite tests supporting, not replacing, the symbolic proof above. Run using `python3 verify_scattered001.py` with no third-party dependencies.

## Relationship to prior work
Bruda (2026) proves that fixed-positive-frequency binary-subsequence counts are eventually polynomials, with degree at most the pattern length minus the number of runs plus one. His Theorem 1.4 implies an eventual quadratic for \(001\), but does not supply this all-\(k\) triangular-partition numerator, leading coefficient, or *sharp* onset \(n=k\). Menon and Singh (2023) computed explicit expressions for low frequencies, \(k\le4\); these are covered specializations, not independent new discoveries here. Tian (2025) gives general counting and construction algorithms, but no matching specialization was identified in the inspected exposition. The separate pattern \(010\) has a different scattered-count statistic and eventual degree one; its established fixed-frequency formula does not imply this quadratic result. Searches cannot certify historical uniqueness, and an unindexed independent derivation remains possible.

## Limitations
The theorem concerns one symmetry class of length-three scattered binary patterns and positive occurrence count. It does not cover zero frequency, all binary patterns, or the other length-three classes. The originality comparison is a best-knowledge literature assessment rather than exhaustive historical priority certification. No independent scientific review has been performed.

## References
- Glenn Bruda, *Enumerating binary words restricted by subsequence frequency*, first posted June 30, 2026, arXiv:2607.02578v1, https://arxiv.org/abs/2607.02578 . Theorem 1.4 and its proof.
- Krishna Menon and Anurag Singh, *Subsequence frequency in binary words*, first posted June 13, 2023, arXiv:2306.07870v1, https://arxiv.org/abs/2306.07870 . Section 3.
- Roger Tian, *Counting occurrences of a pattern in a binary word*, first posted July 3, 2025, arXiv:2507.03205v1, https://arxiv.org/abs/2507.03205 . Sections 4–5.
