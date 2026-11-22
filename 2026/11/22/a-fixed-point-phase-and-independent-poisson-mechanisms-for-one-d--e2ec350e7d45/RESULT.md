# A fixed-point phase and independent Poisson mechanisms for one-deletion diversity of random involutions

## Finding

For an involution \(\pi\in S_n\), let \(D_1(\pi)\) be the set of distinct standardized permutations produced by deleting exactly one entry, and define its one-deletion *deficit* \(L_n(\pi)=n-|D_1(\pi)|\). Let \(f=f_n\) satisfy \(0\le f\le n\), \(n-f\) even, and \(f/\sqrt n\to\alpha\in[0,\infty)\). Draw \(\pi\) uniformly among involutions with precisely \(f\) fixed points.

Four explicitly defined rare local motif counts \((A_n,B_n,C_n^+,C_n^-)\) converge jointly to independent Poisson random variables with respective means \((\alpha^2,1,1/2,1/2)\). The remaining motif count \(E_n\) tends to zero in probability, and the *exact identity* is

\[
L_n=A_n+B_n+2(C_n^++C_n^-+E_n).
\]

Consequently

\[
L_n\xrightarrow{d}X_\alpha+2Y,\qquad
X_\alpha\sim\operatorname{Pois}(1+\alpha^2),\quad
Y\sim\operatorname{Pois}(1),\quad X_\alpha\perp Y.
\]

In particular, \(\Pr(|D_1(\pi)|=n)\to e^{-(2+\alpha^2)}\). The exact finite-size expectation is

\[
\mathbb E L_n=\frac{f(f-1)}n+\frac{n-f}{n}
 +\frac{2(n-f)(n-2)}{n(n-1)}\qquad(n\ge2).
\]

For an **unrestricted** uniform involution (with its fixed-point count random), \(L_n\Rightarrow\operatorname{Pois}(2)+2\operatorname{Pois}(1)\), with the two variables independent. Thus the limiting chance of the maximum possible \(n\) distinct standardized deletion outputs is \(e^{-3}\).

## Assumptions and scope

Positions and values are labeled by \(\{1,\ldots,n\}\); an involution satisfies \(\pi(\pi(i))=i\). Each deletion is standardized by replacing its surviving values by their ranks. The observed set contains *distinct* outputs, not multiplicities. Let \(m=n-f\) denote the number of nonfixed positions.

For every adjacent index pair \((i,i+1)\), define \(A_n\) as the number with \(\pi(i)=i\) and \(\pi(i+1)=i+1\), and \(B_n\) as the number with \(\pi(i)=i+1\), \(\pi(i+1)=i\). For each \(1\le i<j-1\le n-2\) (equivalently \(1\le i\le n-3\), \(i+2\le j\le n-1\)), count one \(C_n^+\) motif when \(\pi(i)=j,\ \pi(i+1)=j+1\), or one \(C_n^-\) motif when \(\pi(i)=j+1,\ \pi(i+1)=j\). In each case involutivity specifies the reverse partners. Let \(E_n\) count \(1\le i\le n-2\) such that \(\pi(i)=i+2\), \(\pi(i+1)=i+1\), \(\pi(i+2)=i\). The symbols \(C_n^\pm\) indicate the two pairings, not a sign on their counts.

The conditional limit assumes fixed \(\alpha\) and parity-compatible integers \(f_n\). It does not assert convergence for \(f_n\) larger than order \(\sqrt n\), or a Poisson law at every finite length.

## Proof

**1. Deletion collisions and the motif identity.** For any permutation, deletions at consecutive positions yield the same standardized word if and only if those two adjacent values are consecutive integers. Across all deletion positions, equality classes are exactly the maximal runs linked by these *bonds*. Consequently \(|D_1(\pi)|=n-b(\pi)\), where \(b\) is the number of adjacent-position consecutive-value bonds (see Homberger, Theorem 6). This is an identity for each permutation, not a probabilistic approximation.

For an involution, inspect the positions \(i,i+1\) of one bond. If both are fixed, it is an \(A\) bond. If they are each other's partner, it is a \(B\) bond. Otherwise, if both are nonfixed and their distinct partners are adjacent, the four vertices form two disjoint adjacent intervals with either parallel or crossed pairings, one \(C^+\) or \(C^-\) motif. That motif contributes two bonds because the partner interval also has consecutive images. The only remaining possibility is exactly one fixed vertex: it must be the midpoint of two positions paired to one another, forming an \(E\) motif that likewise contributes two bonds. These cases partition every bond, proving the displayed identity.

**2. Exact finite means.** A uniformly chosen fixed-site subset of size \(f\), with a uniformly chosen matching of its \(m\) other sites, gives

\[
\begin{aligned}
\mathbb E A_n&=f(f-1)/n,\\
\mathbb E B_n&=m/n,\\
\mathbb E C_n^+&=\mathbb E C_n^-=m(m-2)/(2n(n-1)),\\
\mathbb E E_n&=fm/(n(n-1)).
\end{aligned}
\]

To derive these, prescribe respectively two fixed vertices, one specific matched pair, two specified matched pairs, or one fixed midpoint plus an outer matched pair; count their eligible embeddings, and use the uniform fixed-subset/matching law. Summing the resulting expectations with multiplicities \(1,1,2,2,2\) simplifies to the stated expectation. Terms with impossible motifs are zero, also at the small boundaries \(m=0,2\).

**3. Joint factorial moments.** For a prescribed collection of \(s\) distinct fixed vertices and \(r\) disjoint specified transposition edges on other vertices, the exact probability of occurrence is

\[
\frac{(f)_{\underline s}}{(n)_{\underline s}}
\frac{(m)_{\underline{2r}}}{(n-s)_{\underline{2r}}}
\frac{(m-2r-1)!!}{(m-1)!!},
\]

where falling factorials and double factorials are interpreted by their counting meaning, and impossible prescriptions have probability zero. For fixed \(s,r\) and \(f/\sqrt n\to\alpha\), this is asymptotic to \(\alpha^s n^{-s/2-r}\) when \(\alpha>0\); the uniform upper bound of the same order with \(\alpha\) replaced by a finite constant also covers \(\alpha=0\).

Fix four nonnegative integers \((a,b,c,d)\), and expand \(\mathbb E[(A_n)_{\underline a}(B_n)_{\underline b}(C_n^+)_{\underline c}(C_n^-)_{\underline d}]\). For mutually vertex-disjoint motifs the number of choices is

\[
(1+o(1))\frac{n^{a+b+2c+2d}}{2^{c+d}},
\]

with labels *ordered within each factorial moment*. Such a selection prescribes \(2a\) fixed sites and \(b+2c+2d\) matching edges; its probability tends after multiplication to \((\alpha^2)^a(1)^b(1/2)^{c+d}\).

All overlapping selections contribute \(o(1)\): two compatible overlapping \(A\) motifs require a three-or-more-site consecutive fixed run and its total expected number is \(O(n(f/n)^3)=O(n^{-1/2})\); incompatible fixed/matched requirements contribute zero. Distinct \(B\) motifs sharing a vertex are incompatible. Distinct \(C\) motifs sharing a vertex can coexist only as overlapping length-two windows in a run of at least three parallel partner edges. Each connected run of \(q\ge3\) specified partner edges has only \(O(n^2)\) placements and probability \(O(n^{-q})\), hence vanishes; any longer connected cluster vanishes more strongly. All other overlaps of these motifs force incompatible partners. With a fixed number of selected motifs, there are only finitely many cluster types, so the same bounds apply to mixed overlaps. Therefore every joint factorial moment tends to that of independent Poisson variables of parameters \((\alpha^2,1,1/2,1/2)\), proving their joint distributional convergence. Also \(\mathbb E E_n=fm/[n(n-1)]=O(n^{-1/2})\), so Markov's inequality gives \(E_n\to0\) in probability. The decomposition and continuous mapping theorem prove the compound-Poisson law and zero-deficit probability.

**4. Unrestricted involutions.** Let \(F_n\) be the fixed-point count of an unrestricted uniform involution, and \(w_n(f)=\binom nf(m-1)!!\) for compatible \(f\). The exact ratio

\[
\frac{w_n(f+2)}{w_n(f)}=\frac{n-f}{(f+1)(f+2)}
\]

is greater than one below the scale \(\sqrt n\) and less than one above it. For every fixed \(\varepsilon>0\), successive ratios are uniformly bounded away from one outside \([(1-\varepsilon)\sqrt n,(1+\varepsilon)\sqrt n]\), up to an \(o(\sqrt n)\) boundary band, making both tails geometrically negligible compared with the total mass. Thus \(F_n/\sqrt n\to1\) in probability. The factorial-moment estimates above are uniform on compact ranges of \(f/\sqrt n\). Conditional mixing therefore yields the asserted unrestricted limit with \(\alpha=1\).

## Verification

The included `verify.py` generates every involution on \(n\le11\) labels, constructs the *actual* set of standardized one-deletion outputs, counts all five motif types independently, and tests the per-word identity. It then groups all involutions by fixed-point number and compares the empirical exact rational mean with the derived closed formula. The result is `VERIFY_OK` on 48,927 generated involutions across all sizes one through eleven (the full per-length totals are in `verification_output.txt`). These finite calculations are checks of boundary and combinatorial definitions; the all-length and distributional statements follow from the proof, not from enumeration.

## Relationship to prior work

Homberger (2012, Theorem 6) supplies the general bond/deletion identity, which is explicitly treated as prior work. Baril (2016, Lemma 2) enumerates an increasing-succession marginal in fixed-point-free involutions. Biane, Hampikian, Kirgizov and Nurligareev (first public preprint 2024; published 2024/2025), Sections 2.2–2.4, derive marginal Poisson-\(1/2\) limits for each two-edge endhered pattern in a uniform perfect matching. These are not new marginal claims here. Their joint symmetry/equidistribution does not imply joint *independence*. The contributions assessed here are a four-component joint independence theorem, its fixed-point \(\sqrt n\) phase, and the induced *compound-Poisson deletion-deficit law*, including the unrestricted-involution consequence. Relevant prior indexed results on involution descents and random chord counts use different observables, not the exact deletion deficit.

## Limitations

Independent mathematical validation has not been performed. The proof does not provide quantitative total-variation error rates. Rare-event estimates assume the indicated fixed-point scaling. Although relevant full texts and indexed claims were compared, an unindexed equivalent joint-limit formulation remains a residual originality risk. This result concerns one deletion from permutations with involution source restriction, not two deletions, general permutations, or arbitrary fixed-point densities.

## References

1. C. Homberger, *Counting Fixed-Length Permutation Patterns* (2012), Theorem 6, first posted November 29, 2012, https://arxiv.org/abs/1211.7117.
2. J.-L. Baril, *Avoiding patterns in irreducible permutations*, Discrete Mathematics & Theoretical Computer Science 17 (2016), Lemma 2, https://dmtcs.episciences.org/articles/2158.
3. C. Biane, G. Hampikian, S. Kirgizov and K. Nurligareev, *Endhered Patterns in Matchings and RNA*, Journal of Computational Biology 32 (2025), first published online December 23, 2024, Sections 2.2–2.4, https://doi.org/10.1089/cmb.2024.0658.
