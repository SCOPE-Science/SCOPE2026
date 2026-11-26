# A Fibonacci–Tribonacci law for shortest cyclic covers of the binary no-triple-one language

## Finding

Let \(\mathcal L_k=\{w\in\{0,1\}^k:111\text{ is not a factor of }w\}\), for every integer \(k\ge3\). Let \(C_k\) be the smallest length of a **nonempty cyclic binary word** containing every member of \(\mathcal L_k\) as a cyclic contiguous length-\(k\) factor. The containing word is *unrestricted*: it is allowed to use factors outside \(\mathcal L_k\). Let \(A_k=|\mathcal L_k|\), and let \(E_k=C_k-A_k\).

Then the exact ordinary generating functions are

\[
\sum_{k\ge0}A_kz^k=\frac{1+z+z^2}{1-z-z^2-z^3},\qquad
\sum_{k\ge0}E_kz^k=\frac{z^4(1+2z)}{(1-z-z^2)(1-z-z^2-z^3)}.
\]

Here \(A_0=1,A_1=2,A_2=4\) and \(E_0=E_1=E_2=E_3=0\); the equality \(C_k=A_k+E_k\) is asserted for \(k\ge3\). The values for \(k=3,4,\ldots,10\) are

\[
(C_3,C_4,C_5,C_6,C_7,C_8,C_9,C_{10})=(7,14,28,53,102,194,367,692).
\]

There is always an optimal cyclic covering word that itself avoids `111`, even though the minimization permits words containing `111`. If \(\rho\in(0,1)\) is the unique positive root of \(1-\rho-\rho^2-\rho^3=0\), then

\[
\lim_{k\to\infty}\frac{E_k}{A_k}
=\frac{\rho(1+2\rho)}{1+\rho+\rho^2}
=0.6170242320\ldots.
\]

Thus the unavoidable optimal repetition overhead approaches a positive proportion of the distinct required words.

## Assumptions and scope

A cyclic word of length \(N\) is a sequence of \(N\) binary symbols with indices understood modulo \(N\). Its length-\(k\) cyclic factors are read with wraparound, even when \(N<k\); the proof below shows that the optimum for \(k\ge3\) is at least \(A_k\). Repeated factors are permitted. Words differing by rotation are not distinguished for purposes of coverage or minimization. No restriction on the alphabet or factor set beyond binary avoidance of the **contiguous** pattern `111` is implicit. The proof does not assume a unique optimal word.

## Proof

**1. The overlap graph and its imbalances.** Let \(m=k-1\). Form the directed graph with all words of length \(m\) avoiding `111` as vertices, and each word \(w\in\mathcal L_k\) as one arc from its length-\(m\) prefix to its length-\(m\) suffix. This graph is strongly connected: any vertex reaches \(0^m\) by appending zeroes, and \(0^m\) reaches any vertex by appending its symbols. All those paths avoid `111`.

For each vertex \(v\), the required-arc outdegree is \(1\) if \(v\) ends in `11`, and \(2\) otherwise; the required-arc indegree is \(1\) if \(v\) begins in `11`, and \(2\) otherwise. Define

\[
S_m=\{v:v\text{ ends in `11' but does not begin in `11'}\},\quad
T_m=\{v:v\text{ begins in `11' but does not end in `11'}\}.
\]

The required arcs have an outgoing deficit of one at every \(v\in S_m\), an incoming deficit of one at every \(t\in T_m\), and zero net deficit elsewhere.

**2. An unrestricted lower bound.** Every cyclic covering word, including one containing forbidden factors, induces a closed walk in the **full** binary order-\(m\) de Bruijn graph. Remove one occurrence of each required arc. The remaining nonnegative integral arc multiset is a flow whose nonzero imbalances consist of one outgoing unit at each \(v\in S_m\) and one incoming unit at each \(t\in T_m\). Decompose this integral flow into directed paths from sources in \(S_m\) to targets in \(T_m\), together with directed cycles.

For \(v\in S_m\), denote by \(r(v)\) the index (starting at zero) of its **first** occurrence of `11`. Because \(v\) does not begin with `11` but ends with `11`, \(1\le r(v)\le m-2\). Any path of length \(\ell<r(v)\) starting at \(v\) has a terminal vertex whose first two symbols are the symbols of \(v\) at positions \(\ell,\ell+1\); they cannot be `11` by the definition of \(r(v)\). Thus such a path cannot reach any vertex of \(T_m\), even if it uses forbidden arcs. Every surplus-carrying path starting at \(v\) costs at least \(r(v)\) arcs, so every cover has length at least

\[
A_k+\sum_{v\in S_m}r(v).
\]

**3. A bijection and an attaining augmentation.** Split every \(v\in S_m\) uniquely at its first `11` as \(v=p\,11\,s\), where \(|p|=r(v)\). The prefix \(p\) is nonempty, ends in zero and avoids `11`. The suffix \(s\) is empty or starts in zero and ends in `11`; the entire \(v\) avoids `111`.

Associate to \(v\) the vertex \(t(v)=11\,s\,p^{\mathrm{rev}}\). It is in \(T_m\): the reverse of \(p\) begins in zero, contains no `11`, and provides a non-`11` suffix. Conversely, take \(t\in T_m\) and cut immediately **after its last occurrence of** `11`. The remaining nonempty suffix is \(p^{\mathrm{rev}}\); reversing it gives a nonempty `11`-avoiding \(p\) ending in zero. The prefix preceding that suffix is \(11s\), with \(s\) empty or beginning in zero and ending in `11`. This uniquely reconstructs \(v=p11s\in S_m\). Hence \(t:S_m\to T_m\) is a bijection.

Starting at \(v=p11s\), append the \(r(v)\) letters of \(p^{\mathrm{rev}}\). The successive order-\(m\) windows trace a path to \(t(v)\) of exactly \(r(v)\) arcs. All its length-\(k\) labels avoid `111`: the only new junction is after the final `11` in \(v\), where \(p^{\mathrm{rev}}\) begins with zero, and the appended block has no `11`.

Duplicate these arcs for every \(v\in S_m\). The extra paths balance every vertex because their starting and ending vertices are paired bijectively; the original strongly connected graph remains connected. Euler's directed-circuit criterion now supplies a cyclic word using precisely

\[
A_k+\sum_{v\in S_m}r(v)
\]

arcs. It covers every required word and itself avoids `111`. This attains the unrestricted lower bound. Thus \(E_k=\sum_{v\in S_{k-1}}r(v)\).

**4. Counting and the generating function.** Let \(F_0=0,F_1=1\) be the Fibonacci numbers. For \(r\ge1\), there are \(F_{r+1}\) binary words \(p\) of length \(r\) that avoid `11` and end in zero, whence

\[
P(z)=\sum_{r\ge1}rF_{r+1}z^r
=\frac{z(1+2z)}{(1-z-z^2)^2}.
\]

Let \(B_t\) count possible suffixes \(s\) of length \(t\) in the decomposition above. The empty suffix is allowed; for \(t\ge3\), a nonempty suffix is \(s=0u11\), where \(u\) is empty or ends with zero, and \(u\) avoids `111`. The counts for \(t=1,2\) are zero. The number of legal binary length-\(j\) words is \(A_j\) with

\[
A(z)=\sum_{j\ge0}A_jz^j=\frac{1+z+z^2}{1-z-z^2-z^3}.
\]

Consequently,

\[
B(z)=\sum_{t\ge0}B_tz^t=1+z^3+z^4A(z)
=\frac{1-z-z^2}{1-z-z^2-z^3}.
\]

Since each source has length \(m=r+2+t\), the generating function for the excess indexed by \(k=m+1\) is

\[
\sum_{k\ge0}E_kz^k=z^3P(z)B(z)
=\frac{z^4(1+2z)}{(1-z-z^2)(1-z-z^2-z^3)}.
\]

Finally, the positive simple pole \(z=\rho\) of \(A(z)\) and \(E(z)\) is strictly nearer the origin than the positive pole of \(1/(1-z-z^2)\). Standard rational-function coefficient asymptotics give the displayed ratio, using \(1-\rho-\rho^2=\rho^3\). This completes the proof.

## Verification

The accompanying `verify.py` uses exact integer arithmetic. It separately generates all binary words avoiding `111`, constructs the explicit source-to-target augmentation, verifies the induced Eulerian cycle and complete factor coverage for every \(3\le k\le16\), and evaluates the independent rational generating-function recurrence. Where the optional `networkx` library is present, it also solves minimum-cost flow on **both** the constrained and full binary overlap graphs for every \(3\le k\le10\), independently confirming the unrestricted optimum. Run with `python3 verify.py`; the recorded execution printed `VERIFY_OK constructed_exact_cycles_k=3..16 independent_constrained_and_unrestricted_mincost_k=3..10`. The all-\(k\) proof is the combinatorial argument above, not these finite checks.

## Relationship to prior work

De Bruijn's overlap-graph construction and its Euler-tour formulation are classical; Compeau, Pevzner and Tesler give an accessible exposition. Burstein and Kitaev investigate unavoidable sets of word patterns and universal cycles of patterns, a different enumeration objective. Kapun and Tsarev study sound cycles in paired de Bruijn graphs, which are a different graph model. The general directed postman/eulerization principle is prior knowledge. The new statement is the *explicit all-length optimal cyclic-cover law for the particular `111`-avoiding binary language*, the particular first-occurrence/reversed-prefix bijection realizing the lower bound even in an unrestricted host, and its Fibonacci–Tribonacci generating function and limiting overhead. No novelty is claimed for Euler's criterion or generic min-cost eulerization.

## Limitations

The formula does not classify the number of optimal cyclic words, and it does not treat avoidance of longer runs or arbitrary forbidden-factor sets. The literature comparison cannot exclude equivalent results under a different terminology or an unindexed theorem; independent review has not been performed. The verification scripts are finite independent checks and are not infinite certificates.

## References

- Alexander Burstein and Sergey Kitaev, *On unavoidable sets of word patterns*, arXiv:math/0311399, first posted 2003-11-23; sections 2 and 3.
- Phillip E. C. Compeau, Pavel A. Pevzner, and Glenn Tesler, *How to apply de Bruijn graphs to genome assembly*, Nature Biotechnology 29 (2011), 987–991, DOI 10.1038/nbt.2023, published online 2011-11-08; Box 1 and Euler-tour discussion.
- Evgeny Kapun and Fedor Tsarev, *On NP-Hardness of the Paired de Bruijn Sound Cycle Problem*, arXiv:1307.7806, first posted 2013-07-30; definitions and introduction.
- Jack Edmonds and Ellis L. Johnson, *Matching, Euler tours and the Chinese postman*, Mathematical Programming 5 (1973), 88–124, DOI 10.1007/BF01580113 (general optimization background).
