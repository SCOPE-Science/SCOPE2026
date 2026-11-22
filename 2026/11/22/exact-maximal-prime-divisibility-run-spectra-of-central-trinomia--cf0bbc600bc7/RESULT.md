# Exact maximal prime-divisibility run spectra of central trinomial coefficients

## Finding
For every prime \(p\ge5\) and integer \(L\ge1\), all maximal strings of indices at which the central trinomial coefficient \(T_n=[x^0](x^{-1}+1+x)^n\) is zero or nonzero modulo \(p\), inside the consecutive index block \(0\le n<p^L\), have the following exact length distributions. Write
\[
Z_p=\{d\in\{0,\ldots,p-1\}:T_d\equiv0\pmod p\},\qquad z=|Z_p|,\qquad a=p-z.
\]
If \(z=0\), every term is nonzero modulo \(p\); the entire block is one nonzero run of length \(p^L\), with no zero runs.

If \(z>0\), list \(Z_p=\{d_1<\dots<d_z\}\), define \(s=d_1\), \(t=p-1-d_z\), and
\[
E_h=(p-1-2z)\frac{a^h-1}{a-1}\quad(h\ge0),\qquad E_0=0.
\]
All zero runs have lengths \(p^j\) for \(0\le j<L\); **exactly \(z a^{L-j-1}\) zero runs have length \(p^j\)**, and no other zero-run length occurs. The nonzero-run length multiset, counting coincident lengths with their multiplicities added, consists of
\[
\begin{aligned}
&\text{length }d_{i+1}-d_i-1\text{ with multiplicity }a^{L-1}\quad(1\le i<z),\\
&\text{length }s\text{ with multiplicity }a^{L-1}-E_{L-1},\\
&\text{length }t\text{ with multiplicity }a^{L-1}-E_{L-1},\\
&\text{length }s+t\text{ with multiplicity }E_{L-1}.
\end{aligned}
\]
For \(L\ge2\), the largest nonzero-run length is **exactly**
\[
M_p=\max\bigl(\{s+t\}\cup\{d_{i+1}-d_i-1:1\le i<z\}\bigr)<p.
\]
Consequently, for every prime which divides at least one central trinomial coefficient, the lengths of consecutive *nondivisible* stretches have a uniform finite bound \(M_p\), while the lengths of divisible stretches range over all powers \(p^j\), without bound. The zero runs in the finite blocks are also maximal in the infinite sequence.

## Assumptions and scope
The prime \(p\) is any ordinary prime at least five, and \(L\) is any positive integer. A run means a **maximal nonempty consecutive interval inside the specified finite index block**, so a nonzero run touching an endpoint is truncated by that endpoint. \(T_n\) is the classical central trinomial coefficient, with \(T_0=T_1=1\) and recurrence
\[
nT_n=(2n-1)T_{n-1}+3(n-1)T_{n-2}\quad(n\ge2).
\]
All counts are exact integers. If two entries of the nonzero-run multiset give the same numerical length, add their multiplicities. The empty interior-gap family when \(z=1\) contributes nothing. The complementary, \(z=0\) case includes primes such as \(5\), \(11\), and \(13\).

## Proof
**1. Single-digit zeros are interior and isolated.** The generating function is
\[
F(x)=\sum_{n\ge0}T_n x^n=(1-2x-3x^2)^{-1/2}.
\]
For odd primes, the formal-power-series identity over \(\mathbb F_p\)
\[
F(x)\equiv (1-2x-3x^2)^{(p-1)/2}F(x^p)\pmod p
\]
shows, on comparing the coefficient of \(x^{p-1}\), that \(T_{p-1}\equiv(-3)^{(p-1)/2}\not\equiv0\pmod p\). Also \(T_0=T_1=1\). If \(1\le j\le p-2\) and \(T_j\equiv T_{j+1}\equiv0\pmod p\), the recurrence at index \(j+1\) yields \(3jT_{j-1}\equiv0\pmod p\). As \(3j\) is invertible, descending induction would force \(T_0\equiv0\), contradiction. Hence \(Z_p\subseteq\{2,\ldots,p-2\}\) and contains no adjacent digits. In particular \(a\ge3\), \(s,t\ge1\), and \(p-1-2z\ge1\) (because the adjacent digits \(0,1\) are allowed).

**2. Digitwise divisibility.** Write each \(0\le n<p^L\) with exactly \(L\) base-\(p\) digits \(n_i\), including leading zeros. The coefficient comparison in step 1 gives \(T_n\equiv\prod_{i=0}^{L-1}T_{n_i}\pmod p\). Thus the indicator of nondivisibility is 1 exactly on words whose digits lie in the allowed alphabet \(A_p=\{0,\ldots,p-1\}\setminus Z_p\), of size \(a\). There are exactly \(a^L\) allowed indices in the block. This digit-product identity is established in the cited prior literature and is used here, not asserted to be new.

**3. Zero-run classification.** An index is forbidden as soon as its least significant forbidden digit occurs. For \(0\le j<L\), fix the \(L-j-1\) more significant digits to any allowed word and the next digit to any of the \(z\) forbidden digits; the lower \(j\) digits are arbitrary. This creates one interval of exactly \(p^j\) consecutive forbidden indices. The digits immediately before and after this interval are allowed at the changed digit because forbidden digits are interior and isolated, and lower neighboring digits are \(p-1\) or \(0\), both allowed. Every zero run arises uniquely this way by taking its most significant forbidden digit (equivalently the largest aligned forbidden block not extendable at either side). Thus the count at length \(p^j\) is \(z a^{L-j-1}\); the runs are maximal even in the infinite sequence. Distinct constructed runs are disjoint and cannot merge.

**4. Count adjacent admissible high prefixes.** Let \(E_h\) count the pairs \((u,u+1)\) of admissible \(h\)-digit words, interpreted as integers in \([0,p^h)\), for which both are admissible. When incrementing \(u\), suppose it has exactly \(r\) trailing digits \(p-1\), with \(0\le r<h\). The first digit that changes must be an adjacent admissible pair \((d,d+1)\) with \(0\le d<p-1\); there are \(b=p-1-2z\) such choices, since each forbidden interior digit eliminates exactly two distinct adjacent pairs. The higher \(h-r-1\) digits each have \(a\) choices; the carried digits \(0,p-1\) are admissible. Summing over \(r\) gives
\[
E_h=b\sum_{r=0}^{h-1}a^{h-r-1}=b\frac{a^h-1}{a-1}.
\]
This also proves \(0\le E_h\le a^h-1\), so the multiplicities below are nonnegative.

**5. Nonzero-run classification.** Partition the index block into \(p^{L-1}\) consecutive subblocks of length \(p\), according to the high \(L-1\) digits. A subblock is identically zero if its high prefix is forbidden; otherwise its nonzero positions are exactly the allowed single digits. Each of the \(a^{L-1}\) admissible subblocks has interior nonzero runs of lengths \(d_{i+1}-d_i-1\), a left-edge run of length \(s=d_1\), and a right-edge run of length \(t=p-1-d_z\). Between two consecutive admissible high prefixes the right and left edge runs merge to one run of length \(s+t\), removing one of each edge run. Step 4 shows that this happens exactly \(E_{L-1}\) times. A forbidden subblock cannot be crossed, and an admissible subblock contains a forbidden digit, so no other merges occur. This gives the stated exhaustive multiset.

**6. Sharp global maximum.** For \(L\ge2\), \(E_{L-1}>0\) by step 1, so the joined run of length \(s+t\) occurs. Every interior gap occurs in each admissible subblock. The remaining edge runs have lengths at most \(s+t\). Therefore the maximum is exactly \(M_p\). Each candidate length is below \(p\), because \(s+t=p-1-(d_z-d_1)\le p-1\) and each interior gap is smaller than \(p\). Since arbitrarily large finite blocks each contain the relevant interior runs and their endpoints are not forbidden, the same maximum applies to runs in the infinite index sequence.

## Verification
A stand-alone exact-integer checker, `verify_run_spectra.py`, reconstructs the coefficients from the recurrence, enumerates all runs and compares both length-frequency maps with the theorem for every prime \(5\le p\le101\) and every depth \(L\ge1\) satisfying \(p^L\le15000\). It passed 125,867 index instances; these finite checks corroborate but do not substitute for the all-primes, all-levels proof above. Example for \(p=7\): \(Z_p=\{3\}\), \(a=6\), and the zero-run multiplicity at length \(7^j\) is \(6^{L-j-1}\). The only nonzero run lengths in \(L\ge2\) blocks are \(3\) and \(6\), with multiplicities \(2(6^{L-1}-E_{L-1})\) and \(E_{L-1}\), respectively, where \(E_h=4(6^h-1)/5\).

## Relationship to prior work
Noe (2006), Theorem 8.5, establishes the prime-divisibility digit criterion for generalized central trinomial coefficients. Rampersad and Shallit (2022) study automatic congruence questions for combinatorial sequences. Kohen (2024, version 1 published 6 November 2024), Proposition 7, supplies a digit-product characterization, alongside a symmetry theorem and density results for related Motzkin sequences. These known results settle pointwise divisibility and some limiting densities, but the inspected statements do not specify maximal consecutive zero/nonzero run lengths and their exact multiplicities at every prime and every full digit-block depth. The new portion is the joint exact run-length census and the sharp bounded/nonbounded run dichotomy; it is derived using the credited digit law.

## Limitations
The classification concerns divisibility by \(p\) only, not valuations \(\nu_p(T_n)\) above one or congruences modulo \(p^2\). Its counts are for full digit blocks \([0,p^L)\); it does not furnish an equally compact formula for arbitrary cutoffs. The nonzero endpoint runs are truncated by the finite block, whereas the zero runs are global. The presentation uses a finite digit set \(Z_p\), computable by the defining recurrence; no closed classification of which primes have \(Z_p=\varnothing\) is asserted. The literature comparison is not an exhaustive priority proof; earlier implicit or equivalent word-combinatorial formulations remain a risk. No independent mathematical audit has been performed.

## References
- N. Kohen, *Density and Symmetry in the Generalized Motzkin Numbers mod p*, arXiv:2411.03681v1 (6 November 2024), https://arxiv.org/abs/2411.03681 . See Proposition 7 and Section 3.
- T. D. Noe, *On the Divisibility of Generalized Central Trinomial Coefficients*, Journal of Integer Sequences 9 (2006), Article 06.2.7, https://cs.uwaterloo.ca/journals/JIS/VOL9/Noe/noe35.html . See Theorem 8.5 and congruence (13).
- N. Rampersad and J. Shallit, *Congruence Properties of Combinatorial Sequences via Walnut and the Rowland-Yassawi-Zeilberger Automaton*, Electronic Journal of Combinatorics 29(3) (2022), P3.36, https://doi.org/10.37236/10799 .
