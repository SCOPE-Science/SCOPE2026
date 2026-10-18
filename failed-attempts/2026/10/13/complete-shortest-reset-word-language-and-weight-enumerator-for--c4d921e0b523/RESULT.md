# Complete shortest-reset-word language and weight enumerator for the Wielandt automata

## Finding

For every integer \(n\ge 2\), let \(\mathcal W_n\) be the binary deterministic automaton in the next section. Its minimum reset-word length is \(L=n^2-3n+3\), as previously known. The complete set of words attaining this length is described by independent compulsory letters:

\[
\begin{aligned}
 w_{j(n-1)}&=a &&(0\le j\le n-2),\\
 w_{1+jn}&=b &&(0\le j\le n-3).
\end{aligned}
\]

Here positions are numbered \(0,\ldots,L-1\), the two compulsory-position sets are disjoint, and all other letters can be chosen arbitrarily. Consequently the total number of shortest reset words and their letter-\(a\) enumerator are respectively

\[
2^{(n-2)(n-3)}\quad\text{and}\quad
\sum_{\substack{w:\ |w|=L\\w\text{ resets }\mathcal W_n}}
z^{\#_a(w)}=z^{n-1}(1+z)^{(n-2)(n-3)}.
\]

The classification and the two enumerations—not the established minimum length—constitute the finding.

## Assumptions and scope

The state set is \(Q=\{0,1,\ldots,n-1\}\), and the labeled alphabet is \(\{a,b\}\). For each \(0\le i<n-1\), both letters map \(i\) to \(i+1\). At the final state, \(a(n-1)=1\) and \(b(n-1)=0\). A word is a **reset word** when its induced transformation sends all states to one state. Distinct strings over the labeled alphabet count distinctly even when they happen to induce the same transformation. The result holds for all integers \(n\ge2\); the exceptional small case \(n=2\) is handled directly below.

## Proof

**1. The sharp length lower bound.** Assume \(n\ge3\). In a shortest reset word, the terminal image must be state \(1\): every other state has exactly one predecessor state under either letter (state \(0\) only from \(n-1\) under \(b\); state \(j\ge2\) only from \(j-1\)), so if the entire state set mapped to another terminal state, the final letter could be removed without changing the image cardinality.

Any directed return from \(1\) to \(1\) consists of cycles of length \(n-1\) (traversing \(1,2,\ldots,n-1,1\), choosing \(a\) at \(n-1\)) and of length \(n\) (traversing \(1,2,\ldots,n-1,0,1\), choosing \(b\) at \(n-1\)). Thus every return length is a nonnegative integer combination of \(n-1\) and \(n\). Their Frobenius number is \(F=n(n-1)-n-(n-1)=n^2-3n+1\).

Suppose a shortest reset word had length \(m<L=F+2\). Prepend \(L-1-m\) arbitrary letters to this shortest word. The resulting word has length \(L-1\) and still ends at state \(1\). Starting at state \(0\), the first letter necessarily reaches \(1\); the remaining \(F\) letters would return \(1\) to itself, contrary to the Frobenius property. Thus \(L\) is a lower bound. Step 4 constructs reset words of this length, making it exact.

**2. Compulsory \(a\)-positions.** Let \(w\) reset in length \(L\). Starting at state \(n-1\), its first letter cannot be \(b\). If it were, the next letter would send \(0\) to \(1\), leaving a prohibited return of length \(L-2=F\). Therefore \(w_0=a\), immediately reaching state \(1\). The remaining length is \(L-1=(n-1)(n-2)\). If it consists of \(u\) cycles of length \(n-1\) and \(v\) of length \(n\), then

\[
u(n-1)+vn=(n-1)(n-2).
\]

Reduction modulo \(n\) gives \(u\equiv n-2\pmod n\). Since \(0\le u\le n-2\), necessarily \(u=n-2\) and \(v=0\). Every return cycle must therefore have length \(n-1\), forcing \(a\) at times \(j(n-1)\) for \(0\le j\le n-2\).

**3. Compulsory \(b\)-positions.** Starting instead at state \(n-2\), the first letter moves to \(n-1\). At time \(1\), letter \(a\) would move to \(1\), leaving an impossible return of length \(L-2=F\). Hence \(w_1=b\), reaching state \(0\) at time \(2\), and the next letter always reaches \(1\). The remaining length is \(L-3=n(n-3)\). Expressed as a sum of lengths \(n-1\) and \(n\), the coefficient of \(n-1\) must be a nonnegative multiple of \(n\); because the total length is less than \(n(n-1)\), this coefficient is zero. Hence all return cycles have length \(n\), forcing \(b\) at positions \(1+jn\), for \(0\le j\le n-3\).

**4. Sufficiency of just these positions.** Define nested target sets for times \(1\le t\le L\) as follows. Write \(t-1=j(n-1)+r\), with \(0\le r\le n-2\) and \(0\le j\le n-2\), and put

\[
S_t=\{1+r+k\pmod n:0\le k\le n-2-j\}.
\]

Then \(S_1=\{1,\ldots,n-1\}\) and \(S_L=\{1\}\). The first compulsory \(a\) maps the whole state set into \(S_1\). At each subsequent time \(t<L\) with \(r=n-2\), the compulsory \(a\) maps \(S_t\) into \(S_{t+1}\), shortening the target interval by one. At any time with \(r<n-2\), letter \(b\) maps \(S_t\) onto \(S_{t+1}\). The alternative letter \(a\) differs from \(b\) only on source state \(n-1\), substituting target \(1\) for target \(0\); it violates \(a(S_t)\subseteq S_{t+1}\) exactly when \(r=j\), which is exactly time \(t=1+jn\), one of the compulsory \(b\)-positions. Hence **every** word satisfying the compulsory-position conditions inductively maps \(Q\) into \(S_L=\{1\}\), and resets. No condition on any remaining letter is necessary.

For \(n=2\), the only shortest reset word is the single letter \(a\), and the same formulas hold.

**5. Exact enumeration.** The \(n-1\) compulsory \(a\)-positions and \(n-2\) compulsory \(b\)-positions do not intersect: if \(j(n-1)=1+kn\), then \(j+k\equiv1\pmod n\), which is inconsistent with the given ranges (or directly follows from their placement in the distinct reductions above). More transparently, at a compulsory \(b\) time \(1+kn\), the residue modulo \(n-1\) is \(1+k\in\{1,\ldots,n-2\}\), so it is not a compulsory \(a\) time. There are therefore

\[
L-(n-1)-(n-2)=(n-2)(n-3)
\]

free binary positions. Each can independently be \(a\) or \(b\), proving the count and the binomial \(a\)-letter enumerator.

## Verification

The accompanying `verify_dp.py` constructs the exact subset-image automaton and counts all reset words at the minimum length with a separate count for each number of \(a\)'s. It verifies the binomial polynomial for every \(2\le n\le12\), verifies no shorter reset word exists for these cases, and directly checks all interval-map inclusions for \(2\le n\le40\). The independent C++ program `verify_independent.cpp` directly enumerates all labeled binary words of the claimed shortest length for \(2\le n\le6\), comparing each word's actual action to its compulsory-position status. Both programs complete with `VERIFY_OK`; they support, but do not replace, the all-length proof. For example, the numbers of shortest reset words at \(n=2,3,4,5,6\) are \(1,1,4,64,4096\).

To reproduce: run `python3 verify_dp.py`; compile the other program with `g++ -O3 -std=c++17 verify_independent.cpp -o verify_independent` and execute `./verify_independent`. Python's standard library and a C++17 compiler suffice.

## Relationship to prior work

Ananichev–Gusev–Volkov determined the minimal reset-word length \(n^2-3n+3\) of these automata and exhibited a shortest word. Their original preprint and expanded paper establish the threshold, not the complete set of achieving strings or their number. Gusev–Pribavkina extend reset-threshold analysis to related two-cycle-length automata, but a lower/upper bound on reset length does not determine shortest-word multiplicities. Ryzhikov–Szykuła (2018) identify the same family as a minimized decoder of a prefix code and study the complexity of finding short synchronizing words; they do not classify all shortest strings. Algorithms for finding shortest synchronizing words likewise need not classify every shortest word. The contribution here is the full positionwise characterization of every shortest word and the consequent binomial weight distribution, which are not logically implied by the known threshold or one witness.

## Limitations

The claim pertains to the specified two-letter Wielandt automata, exact minimum length, and labeled input words; it does not count distinct state transformations or classify longer reset words. The proof is mathematical and finite-dimensional, not a computational proof for unbounded \(n\). Some older or unindexed literature may already contain an equivalent full enumeration; no claim of exhaustive worldwide bibliographic coverage or independent audit is made.

## References

- D. S. Ananichev, V. V. Gusev, M. V. Volkov, *Slowly synchronizing automata and digraphs*, 2010, arXiv:1005.0129, https://arxiv.org/abs/1005.0129 (earliest public preprint, 2010-05-02).
- D. S. Ananichev, V. V. Gusev, M. V. Volkov, *Primitive digraphs with large exponents and slowly synchronizing automata*, 2013, arXiv:1302.5793, https://arxiv.org/abs/1302.5793 (expanded treatment, especially the Wielandt-family theorem).
- V. V. Gusev, E. V. Pribavkina, *Reset thresholds of automata with two cycle lengths*, 2014, arXiv:1403.3992, https://arxiv.org/abs/1403.3992.
- A. Kisielewicz, J. Kowalski, M. Szykuła, *Computing the shortest reset words of synchronizing automata*, 2013, https://doi.org/10.1007/s00224-013-9481-5.
- A. Ryzhikov, M. Szykuła, *Finding Short Synchronizing Words for Prefix Codes*, MFCS 2018, https://doi.org/10.4230/LIPIcs.MFCS.2018.21.
