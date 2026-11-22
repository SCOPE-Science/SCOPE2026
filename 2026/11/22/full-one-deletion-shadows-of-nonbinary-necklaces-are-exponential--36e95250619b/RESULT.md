# Full one-deletion shadows of nonbinary necklaces are exponentially typical among proper circles

## Finding
Let \(q\ge3\), \(n\ge3\), and \(\Sigma_q=\{0,\ldots,q-1\}\). For an indexed circular word \(w\in\Sigma_q^n\), let \(\mathcal D_\circ(w)\) be the set of *rotation classes* of the \(n\) words produced by deleting exactly one indexed position of \(w\), with no reversal or letter relabeling. Let \(A_q(n)\) count the labeled, indexed words with \(|\mathcal D_\circ(w)|=n\), and let \(C_q(n)\) count the circularly proper words, those satisfying \(w_i\ne w_{i+1}\) at every cyclic position.

The sharp maximum and the quantitative all-length genericity bound are
\[
\max_{w\in\Sigma_q^n}|\mathcal D_\circ(w)|=n,\qquad C_q(n)=(q-1)^n+(-1)^n(q-1),
\]
\[
0\le C_q(n)-A_q(n)\le\binom n2(n-1)q^{\lfloor n/2\rfloor}.
\]
Consequently, for each fixed \(q\ge3\), a uniformly chosen circularly proper indexed word has its full \(n\)-element one-deletion shadow with probability
\[
\frac{A_q(n)}{C_q(n)}=1-O_q\!\left(n^3\left(\frac{\sqrt q}{q-1}\right)^n\right).
\]
Thus the limiting probability is one, with exponential convergence. The construction \(2u\), where \(u\) is the alternating binary word of length \(n-1\) beginning with \(0\), attains the maximum for every \(n\). Moreover every full-shadow word is circularly proper and aperiodic.

## Assumptions and scope
Positions are indexed before quotienting the resulting words by cyclic rotation. Two different deletion sites contribute one output when the surviving length-\(n-1\) strings are cyclic rotations. Distinct symbols are labeled: neither reversal nor alphabet permutation is factored out. The ordinary proper-coloring count \(C_q(n)\) is for the cycle on \(n\) indexed vertices. The asymptotic is for fixed \(q\ge3\), conditional on the source being circularly proper, *not* for all uniformly random words. The claim covers exactly one deletion and all \(n\ge3\).

## Proof
**1. Necessity of circular properness.** There are only \(n\) deletion sites, giving the universal upper bound \(|\mathcal D_\circ(w)|\le n\). If two cyclically adjacent source symbols are equal, deleting either gives the same surviving circular word. So the full bound requires \(w_i\ne w_{i+1}\) for every \(i\) modulo \(n\).

**2. Sharp construction at three colors.** Choose distinct symbols \(0,1,2\) and let \(u=u_1\cdots u_{n-1}\), with \(u_i=0\) for odd \(i\) and \(u_i=1\) for even \(i\). Put \(w=2u\). Deleting the unique \(2\) gives a binary output circle. Every other output retains exactly one \(2\); rooting it immediately after that marker recovers the ordinary linear word obtained by deleting the corresponding position of \(u\). For any two different sites in a linearly adjacency-distinct word, those two one-deletion strings differ: comparing them from the common start, the first discrepancy is an adjacent unequal pair of letters. Therefore all \(n-1\) marker-containing outputs are distinct, and none equals the marker-free output. Hence the maximum is \(n\).

**3. Collision alignments have no fixed points.** Suppose a circularly proper \(w\) has a collision between distinct sites \(i,j\). Pick one cyclic alignment of their surviving \(n-1\) indexed sites witnessing equality. It defines a bijection of the remaining source sites, from the order after deleting \(i\) to the order after deleting \(j\), followed by a chosen cyclic shift of the latter order. Extend this bijection to a permutation \(\pi\) of all \(n\) sites by defining \(\pi(i)=j\). The collision requires \(w_a=w_{\pi(a)}\) for every site \(a\), and hence \(w\) is constant on each cycle of \(\pi\).

We claim \(\pi\) has no fixed points whenever such a collision is compatible with properness. Since \(i\ne j\), neither \(i\) nor \(j\) is fixed. If \(\pi(p)=p\), root *both* equal surviving circles at the common retained symbol indexed \(p\). This yields identical ordinary linear deletion strings of the original length-\(n\) word rooted at \(p\). The deleted sites are distinct and the rooted original word has unequal adjacent letters, so the elementary first-discrepancy argument of Step 2 says their linear deletion strings must differ. Contradiction. Thus \(\pi\) has no one-cycles.

**4. Counting rare exceptional words.** Every fixed-point-free permutation of \(n\) objects has at most \(\lfloor n/2\rfloor\) cycles. For any specified distinct deletion sites \(i,j\) and any one of the \(n-1\) possible output rotations, the collision constraints therefore admit at most \(q^{\lfloor n/2\rfloor}\) labeled assignments to source sites: choose one symbol independently on each permutation cycle. (Imposing circular properness can only reduce the number.) There are \(\binom n2\) pairs of deletion sites and \(n-1\) candidate alignments. A union bound gives
\[
0\le C_q(n)-A_q(n)\le\binom n2(n-1)q^{\lfloor n/2\rfloor}.
\]
The standard chromatic polynomial of a cycle yields \(C_q(n)=(q-1)^n+(-1)^n(q-1)\); equivalently, it is the trace of the \(q\)-by-\(q\) matrix with zeros on its diagonal and ones off-diagonal, whose eigenvalues are \(q-1\) once and \(-1\) with multiplicity \(q-1\).

Finally \(\sqrt q/(q-1)<1\) for each integer \(q\ge3\). Divide the bound by \(C_q(n)\), which is asymptotic to \((q-1)^n\), to obtain the exponential error estimate. If \(w\) has a nontrivial cyclic period, deleting corresponding periodic sites yields rotation-equivalent descendants, so full-shadow sources are aperiodic. \(\square\)

## Verification
The standalone standard-C++17 file `verification/verify.cpp` enumerates all \(q=3\) sources of lengths \(3\) through \(12\), and all \(q=4\) sources of lengths \(3\) through \(7\), constructs and lexicographically normalizes every literal one-deletion output, and compares the maximum, properness and proper-coloring count. For the ternary alphabet the exact numbers of full-shadow indexed words at lengths \(3,4,\ldots,12\) are \(6,12,30,54,126,192,504,930,1914,3876\). For the quaternary alphabet at lengths \(3\) through \(7\), they are \(24,72,240,696,2184\). The checker also verifies the marker construction through length \(256\) and finite collision-permutation consequences through length \(30\). Compile with `c++ -std=c++17 -O2 verification/verify.cpp -o verify` and run `./verify`. Exact console output is in `verification/output.txt`. Exhaustive finite checks corroborate, but do not replace, the proof for arbitrary lengths.

## Relationship to prior work
Luchinin, Puzynina and Rao study source reconstruction of **binary** cyclic words from sets of much shorter scattered subwords; their full paper does not determine the one-deletion shadow cardinality over nonbinary alphabets or its typicality. Burudgunte, Valiant and Wang analyze recovery from repeated *stochastic* circular deletion traces, particularly sparse binary sources, not the support size of a single exactly-one-deletion channel. Gabrić and Sawada give algorithms for generating necklaces and Lyndon words, not their single-deletion degrees. The existing exact binary-necklace outdegree theorem gives strict parity-dependent maxima smaller than \(n\) for all \(n\ge4\). The existing formula for short deletions of repeated permutation words concerns periodic sources; those do not have \(n\) distinct single-deletion descendants. None of these inspected statements implies the all-\(q\ge3\) exponential full-shadow law, although this comparison does not establish global priority.

## Limitations
The exponential estimate is conditional on proper circular colorings, and the union-bound prefactor is not asserted optimal. There is no exact all-length formula here for \(A_q(n)\), nor a uniform-in-\(q\) error bound. The theorem addresses one deletion, distinct resulting circular *words*, and no multiplicity distribution or multi-deletion reconstruction guarantee. Equivalent results in older unindexed work on circular deletion graphs or necklace posets remain a priority risk. Independent review has not been performed.

## References
1. Sergey Luchinin, Svetlana Puzynina, Michaël Rao, *Recovery of cyclic words by their subwords*, first arXiv version 2024-12-04, https://arxiv.org/abs/2412.03289, especially Sections 1–4.
2. Arnav Burudgunte, Paul Valiant, Hongao Wang, *New Bounds for Circular Trace Reconstruction*, first arXiv version 2025-12-02, https://arxiv.org/abs/2512.02412, especially Sections 1–2 and 4–5.
3. Daniel Gabrić, Joe Sawada, *Necklaces and Lyndon words in colexicographic order*, first arXiv version 2026-07-06, https://arxiv.org/abs/2607.05324, especially Sections 1–4.
4. *Sharp one-deletion outdegree of binary necklaces*, public result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-one-deletion-outdegree-of-binary-necklaces--2341722fce11.
5. *Short-deletion necklaces of permutation powers: exact orbit counts and the first phase-wrap collision*, public result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-short-deletion-necklaces-of-permutation-powers-exact-orbit-count--16ccfbf22eda.
