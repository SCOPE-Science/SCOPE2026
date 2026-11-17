# Minimal absent scattered subsequences of repeated binary run blocks

## Finding

Let \(a,b,r\ge 1\) be integers and \(W_{a,b,r}=(0^a1^b)^r\). A **minimal absent scattered subsequence** (MAS) is a nonempty binary word that does not occur as an order-preserving subsequence of \(W_{a,b,r}\), but every word obtained by deleting one symbol does occur. Write \(M_r(a,b)\) for the number of distinct MAS words (not occurrences).

**Theorem.** For every \(a,b,r\ge 1\), the complete MAS language is described in the criterion below, and its exact cardinality is

\[
M_r(a,b)=\begin{cases}
F_{2r+2},&a,b\ge2,\\
3\cdot 2^{r-1},&\min(a,b)=1<\max(a,b),\\
[z^r]\dfrac{z(3-z+2z^2)}{1-2z+z^2-z^3},&a=b=1.
\end{cases}
\]

Here \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). The last case begins \(3,5,9,16,28,49,86,\ldots\), and obeys \(M_1=3,M_2=5,M_3=9\) and \(M_r=2M_{r-1}-M_{r-2}+M_{r-3}\) for \(r\ge4\). Hence increasing either run length beyond one never changes the count, even though it changes the identities and lengths of the absent words.

For an arbitrary nonempty candidate \(u=x_1^{\ell_1}\cdots x_h^{\ell_h}\) with maximal constant runs, alternating \(x_i\in\{0,1\}\), define \(c_0=a,c_1=b\) and
\[
B(u)=\sum_{i=1}^h\left\lceil\frac{\ell_i}{c_{x_i}}\right\rceil
-\#\{1\le i<h:(x_i,x_{i+1})=(0,1)\}.
\]
Then \(u\) is an MAS **if and only if** all of the following hold:

1. \(B(u)=r+1\).
2. Every run satisfies \(\ell_i\equiv1\pmod{c_{x_i}}\).
3. If \(h\ge2\), the first run is not \(0^1\) and the last run is not \(1^1\).
4. If \(h\ge3\), no internal \(1\)-run has length one when \(a=1\), and no internal \(0\)-run has length one when \(b=1\).

The criterion is an effective finite description of every missing word, including all boundary cases. Here \(0^1\) and \(1^1\) denote singleton runs, not restrictions on a single-run candidate.

## Assumptions and scope

Subsequences may skip symbols but must preserve order; they are not contiguous factors. The host word is exactly \((0^a1^b)^r\), beginning with zero and ending with one. All three parameters are positive integers; the candidate alphabet is exactly \(\{0,1\}\); counts distinguish absent words by their content, never by how many embeddings they possess. All generating functions are formal power series in \(z\).

## Proof

**1. Greedy block consumption.** Greedily match the letters of \(u\) in the host. A run of \(0\)'s of length \(\ell\) needs \(\lceil\ell/a\rceil\) zero-blocks, and a run of \(1\)'s needs \(\lceil\ell/b\rceil\) one-blocks. The transition \(0\to1\) shares the current host block, reducing the combined requirement by exactly one; a transition \(1\to0\) requires the next host block. Inducting over the runs proves that the least number of full \(0^a1^b\) blocks in which \(u\) embeds is precisely \(B(u)\). In particular \(u\) is present exactly when \(B(u)\le r\). Deleting a symbol never raises \(B\), and lowers it by at most one.

**2. Exact deletion test.** If a deleted symbol belongs to a run of length at least two, the surrounding run pattern stays unchanged and the change in \(B\) is
\[
\left\lceil\frac{\ell}{c}\right\rceil-\left\lceil\frac{\ell-1}{c}\right\rceil,
\]
which equals one precisely when \(\ell\equiv1\pmod c\). If the deleted symbol is the first singleton \(0\)-run and another run follows, the lost run and the lost \(0\to1\) discount cancel, so \(B\) does not decrease. The same cancellation occurs for a final singleton \(1\)-run. A first singleton \(1\) or final singleton \(0\) decreases \(B\) by one.

For an internal singleton \(x\), its two neighboring runs both have the opposite letter \(y\). If their lengths are \(L,R\), direct cancellation of the singleton contribution and the adjacent transition discount gives
\[
B(u)-B(u\text{ with this singleton deleted})=
\left\lceil\frac L{c_y}\right\rceil+
\left\lceil\frac R{c_y}\right\rceil-
\left\lceil\frac{L+R}{c_y}\right\rceil.
\]
When every nonsingleton run already satisfies condition 2, \(L,R\equiv1\pmod{c_y}\); the displayed quantity is one if \(c_y\ge2\), and zero if \(c_y=1\). The same conclusion holds if the neighboring lengths are themselves one: for a capacity of one the difference is zero, and for capacity at least two it is one. Thus conditions 2–4 characterize exactly the words for which **every** single-symbol deletion decreases \(B\) by one.

If \(u\) is minimally absent then \(B(u)>r\), while every deletion has value at most \(r\); because each deletion changes \(B\) by at most one, necessarily \(B(u)=r+1\) and each deletion reduces \(B\) by one. Conversely, conditions 1–4 give these properties, so \(u\) is minimally absent. This proves the language criterion with no length cutoff.

**3. Exact enumeration.** If \(\ell\equiv1\pmod c\), then \(\ell=c(t-1)+1\) for a unique positive integer \(t\), and the run contributes \(t=\lceil\ell/c\rceil\) to \(B\). Its unrestricted weight series is \(q=z/(1-z)\); when the run must not be a singleton the weight series is \(p=z^2/(1-z)\). Each \(0\to1\) transition contributes the correction \(z^{-1}\). Let \(H(z)\) enumerate *all* words satisfying conditions 2–4, weighted by \(z^{B(u)}\); do not yet impose condition 1. Each singleton-run-only word contributes to the coefficient at \(z\), giving \([z]H=2\). Hence the MAS generating function is \((H(z)-2z)/z\).

If \(a,b\ge2\), no internal singleton restriction applies. For an even number \(2k\) of runs with \(k\ge1\), the two possible initial letters contribute respectively \(z^{k+1}/(1-z)^{2k}\) and \(z^{k+2}/(1-z)^{2k}\). For an odd number \(2k+1\ge3\), the two orientations contribute \(2z^{k+2}/(1-z)^{2k+1}\). Adding also the single-run contribution \(2z/(1-z)\) and summing the geometric series with ratio \(z/(1-z)^2\) yields
\[
\frac{H(z)-2z}{z}=\frac{z(3-z)}{1-3z+z^2}.
\]
The coefficients satisfy \(M_1=3,M_2=8,M_r=3M_{r-1}-M_{r-2}\), and so equal \(F_{2r+2}\).

If exactly one capacity is one, reversal followed by exchanging the letters reduces to \(a=1,b\ge2\). The initial run contributes either \(p\) (initial zero, forbidden to be a singleton) or \(q\) (initial one). Every further run contributes the *effective* weight \(q\): a following zero has unrestricted weight \(q\), while a following one has non-singleton weight \(p\) and the \(0\to1\) discount \(z^{-1}\), so \(pz^{-1}=q\). Including isolated-run words gives \(H=2q+(p+q)q/(1-q)\), whence
\[
\frac{H(z)-2z}{z}=\frac{3z}{1-2z}.
\]
This yields \(M_r=3\cdot 2^{r-1}\).

If \(a=b=1\), every internal run must be nonsingleton, as must an initial zero run and a final one run. At \(2k\ge2\) runs, the two orientations contribute \(z^{3k-1}/(1-z)^{2k}\) and \(z^{3k}/(1-z)^{2k}\). At \(2k+1\ge3\) runs they contribute \(2z^{3k+1}/(1-z)^{2k+1}\). Adding \(2z/(1-z)\) and summing with ratio \(z^3/(1-z)^2\) yields
\[
\frac{H(z)-2z}{z}=\frac{z(3-z+2z^2)}{1-2z+z^2-z^3}.
\]
These three cases exhaust the parameter range and prove the theorem.

## Verification

The accompanying standalone \(`checker.py`\) independently generates all scattered subsequences, constructs minimal absent words by explicit one-letter deletion tests, checks the full language criterion against literal candidates, and compares the counts with the three exact formulas. It passed 55 positive parameter triples with \(1\le a,b,r\le4\) and host length at most \(20\), comparing 693 actual MAS words against 683,530 literal candidate checks, plus recurrence values through \(r=10\). A separate brute-force greedy-cost comparison checked all \(1\le a,b,r\le4\) against every binary candidate of length at most 13. Finite computations corroborate, but do not prove, the infinite statement; the complete argument is the run/deletion/series proof above.

## Relationship to prior work

Kosche, Koß, Manea and Siemer studied absent scattered subsequences and gave general characterizations and illustrative periodic constructions. Manea, Ringleb, Siemer and Winkler (2025) studied efficient enumeration of all minimal and shortest absent subsequences. The present theorem is a structural specialization to two-run periodic binary hosts, providing all-parameter exact counts in three sharply different regimes and an explicit full-language test. A general-purpose enumeration algorithm is not itself the stated closed counting formula. Existing work on the largest number of **shortest** absent subsequences concerns a different counting object: the shortest-absent subset need not equal the full minimal-absent antichain.

## Limitations

Only two-letter alphabet and repeated blocks of the specific form \((0^a1^b)^r\) are classified. The result does not count embeddings, all absent subsequences (which form an infinite upward-closed set), minimal *contiguous* absent factors, or arbitrary periodic binary block patterns. Priority against every unindexed or inaccessible specialization has not been independently established, and the numerical checker cannot certify the infinite theorem.

## References

- F. Manea, M. Ringleb, J. Siemer and C. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (first public 2025-04-30), https://arxiv.org/abs/2504.21471.
- M. Kosche, T. Koß, F. Manea and J. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (2021), https://arxiv.org/abs/2108.13968.
- M. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (2024), https://arxiv.org/abs/2407.18599.
- M. Praveen et al., *On piecewise complexity of words and periodic words*, arXiv:2311.15431 (2023), https://arxiv.org/abs/2311.15431.
