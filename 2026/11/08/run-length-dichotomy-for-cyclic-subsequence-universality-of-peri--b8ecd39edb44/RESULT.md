# Run-length dichotomy for cyclic subsequence universality of periodic words

## Finding
Let \(q\ge 3\), let \(c_0,\ldots,c_{q-1}\) be pairwise distinct letters, and let \(a_0,\ldots,a_{q-1}\) be positive integers. Set
\[
U=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad p=\sum_{i=0}^{q-1}a_i.
\]
For every phase \(0\le s<p\), write \(U_s=U[s:p]U[0:s]\), with zero-based half-open slices, and let \(t(s)\) be the offset of phase \(s\) from the beginning of its constant-letter run. Write \(\delta(s)=[t(s)>0]\).

For a finite word \(w\) over \(\Sigma=\{c_0,\ldots,c_{q-1}\}\), its scattered-subsequence universality index \(\iota(w)\) is the largest integer \(r\ge0\) such that every word in \(\Sigma^r\) occurs as an order-preserving subsequence of \(w\). For every integer \(k\ge1\), the **complete phase-index classification** is
\[
\iota(U_s^k)=
\begin{cases}
k,&\min_i a_i=1,\\[3pt]
k+\left\lfloor\dfrac{k-1+\delta(s)}{q-1}\right\rfloor,&\min_i a_i\ge2.
\end{cases}
\]
Consequently the circular universality index of \(U^k\), defined by \(\zeta(U^k)=\max_{0\le s<p}\iota(U_s^k)\), is
\[
\zeta(U^k)=
\begin{cases}
k,&\min_i a_i=1,\\[3pt]
k+\left\lfloor\dfrac{k}{q-1}\right\rfloor,&\min_i a_i\ge2.
\end{cases}
\]
When at least one run is a singleton, all \(p\) phases attain this maximum. When every run has length at least two, all \(p\) phases attain it if \((q-1)\nmid k\); if \((q-1)\mid k\), exactly the \(p-q\) strictly internal run phases attain it and the \(q\) run-start phases have universality index one smaller.

## Assumptions and scope
The alphabet contains exactly the \(q\) displayed letters. Their distinctness is essential: the circular run order visits every alphabet letter exactly once per period. The run lengths are arbitrary positive integers; \(k\) is an arbitrary positive integer. Cyclic rotations are by **positions**, not only by run boundaries. The statement does not concern multiplicities of subsequence embeddings or universality with respect to a larger ambient alphabet.

## Proof
**1. Greedy arches and universality.** Greedily cut a word immediately after the first position at which every symbol in \(\Sigma\) has appeared since the previous cut. Call each complete piece an *arch*; the final piece may omit some symbols. If there are \(m\) complete arches, each target word of length \(m\) embeds by choosing one specified letter from each arch. Conversely, take the last letter of each arch, followed by any symbol absent from the final piece. Each arch's last letter is its first occurrence of that letter inside that arch, so leftmost subsequence matching is forced through all \(m\) arch endpoints and cannot match the final symbol. Thus a word with \(m\) complete greedy arches has index exactly \(m\).

**2. Arch endpoint recurrence on the infinite periodic run sequence.** Extend \(U\) periodically in both directions and index its successive maximal runs by all integers; run \(R_j\) carries \(c_{j\bmod q}\), has length \(a_{j\bmod q}\), and the next run is \(R_{j+1}\). Consider the factor \(U_s^k\) beginning at offset \(t=t(s)\) of run \(R_j\). Its right endpoint lies at the same offset in run \(R_{j+kq}\).

Write \(J_r\) for the global run index whose **first letter** completes arch \(r\) when scanning the infinite word forward from this starting position. The first arch needs the remaining \(q-1\) alphabet letters after \(c_{j\bmod q}\), hence \(J_1=j+q-1\). Once an arch ends at the first letter of \(R_{J_r}\), there are two possibilities. If \(a_{J_r\bmod q}\ge2\), another copy of its letter remains in that run, and the next arch ends at the first letter of \(R_{J_r+q-1}\). If \(a_{J_r\bmod q}=1\), the next arch starts in the next run and requires all \(q\) cyclic run classes, ending at the first letter of \(R_{J_r+q}\). Therefore
\[
J_{r+1}=J_r+
\begin{cases}
q-1,&a_{J_r\bmod q}\ge2,\\
q,&a_{J_r\bmod q}=1.
\end{cases}
\tag{1}
\]
An endpoint in run \(R_{J_r}\) belongs to the half-open factor being studied exactly when \(J_r<j+kq\), or when \(J_r=j+kq\) and \(t>0\). Hence
\[
\iota(U_s^k)=\#\{r\ge1:J_r-j\le kq-1+\delta(s)\}.
\tag{2}
\]

**3. No singleton runs.** If all lengths exceed one, (1) gives \(J_r=j+r(q-1)\). Formula (2) becomes
\[
\left\lfloor\frac{kq-1+\delta(s)}{q-1}\right\rfloor
=k+\left\lfloor\frac{k-1+\delta(s)}{q-1}\right\rfloor.
\]
There are \(q\) run-start phases (offset zero) and \(p-q\) other phases. The two floor values differ precisely when \((q-1)\mid k\). Because every run has length at least two, an internal phase always exists and attains the larger value.

**4. At least one singleton run.** Define the nonnegative integer \(E_r=rq-(J_r-j)\). From \(J_1=j+q-1\), we have \(E_1=1\). Each transition at a nonsingleton endpoint increases \(E_r\) by one; a transition at a singleton endpoint leaves it unchanged. Before the first singleton endpoint, the run labels of successive endpoints move strictly backward through the \(q\) distinct run classes, so a singleton is reached among the first \(q\) endpoints. Thereafter the endpoint stays in that same run class and \(E_r\) is constant. In particular \(1\le E_r\le q\) for all \(r\). Moreover \(E_r=q\) can happen only if the starting run \(R_j\) itself is singleton, which forces \(t=0\).

For every \(k\ge1\), \(J_k=j+kq-E_k<j+kq\), so the \(k\)-th arch finishes inside the factor. But \(J_{k+1}=j+(k+1)q-E_{k+1}\ge j+kq\). Equality can occur only when \(t=0\), in which case that endpoint is exactly at the excluded right boundary. Hence the \((k+1)\)-st arch never finishes inside the factor. It follows that \(\iota(U_s^k)=k\) for every phase.

Taking maxima in the two cases proves the circular-index formula and the complete maximizing-phase census.

## Verification
A standalone standard-library Python program `verify.py` separately scans the factors to count greedy arches, compares all phase values with the formulas, checks the precise maximizing-phase multiplicities, and separately reconstructs full scattered-subsequence spectra for small cases without relying on arch counting. Executing `python3 verify.py` passed **9,671 parameter/repetition cases**, **105,476 phase-index comparisons**, and **678 direct full-spectrum cross-checks**. These finite tests corroborate, rather than replace, the all-parameter proof above.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea and Nowotka (2020) introduced scattered-factor universality and circular universality; their Lemma 20 bounds the circular index by one above the ordinary index and their Theorem 22 relates a specific circular gain to powers. Their general results neither specify this family's singleton dichotomy nor classify every cyclic starting phase. Fleischmann, Germann and Nowotka (2021) proved eventual periodicity for universality growth of powers (their Theorem 21) and supplied general recurrence-based algorithms (Propositions 22–23). The explicit no-transient period \(q-1\), sharp singleton obstruction, and all-phase count here are more specialized structural data. Schnoebelen and Veron (2023) described arch-jumping functions and an algorithm for circular universality (their Lemma 4.1); an algorithm evaluating phases does not itself state the above length-independent formulas or the exact optimizing-phase census. General shortest-absent-subsequence theory in Kosche, Koß, Manea and Siemer (2021) provides additional context for the arch method. These comparisons do not establish absolute novelty beyond inspected and searched material.

## Limitations
The theorem requires one cyclic run for each alphabet symbol. When a symbol occurs in multiple runs per period, the run-index recurrence (1) no longer follows from merely counting runs. The result concerns which lengths of subsequences are universally present, not the number or identities of missing subsequences. Independent verification and exhaustive bibliographic priority confirmation are not supplied. The reported checks are finite; the infinite statement follows only from the proof.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words* (2020), https://arxiv.org/abs/2003.04629, especially §4, Lemma 20 and Theorem 22.
2. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality — The Power of the Remainder* (2021), https://arxiv.org/abs/2104.09063, especially §3 and Theorem 21/Propositions 22–23.
3. P. Schnoebelen, J. Veron, *On arch factorization and subword universality for words and compressed words* (2023), https://arxiv.org/abs/2304.11932, especially §§3–4, Lemma 4.1.
4. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words* (2021), https://arxiv.org/abs/2108.13968, especially §§2–3.
