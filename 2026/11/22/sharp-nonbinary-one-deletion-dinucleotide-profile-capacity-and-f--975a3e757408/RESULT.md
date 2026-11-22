# Sharp nonbinary one-deletion dinucleotide-profile capacity and first saturation length

## Finding
Fix a labeled alphabet \(\Sigma\) with \(|\Sigma|=q\ge3\). For every linear word \(w=w_1\cdots w_n\) with \(n\ge2\), let \(P(w)\in\mathbb N^{q^2}\) be its *ordered dinucleotide profile*: the coordinate \(P_{ab}(w)\) counts adjacent occurrences of \(ab\), including multiplicities. Let
\[
B(w)=\{P(w_1\cdots w_{i-1}w_{i+1}\cdots w_n):1\le i\le n\},
\qquad b(w)=|B(w)|.
\]
Then the following capacity, saturation-length and random-word statements hold together.

**Sharp capacity.** For every \(n\ge2\) and word \(w\in\Sigma^n\),
\[
\boxed{b(w)\le M_q:=q(q-1)^2+q+2.}
\]
For every \(n\ge N_q:=q(q-1)^2+2q+2\), there is a word of length \(n\) attaining equality. No shorter word attains equality. Thus \(N_q\) is the *exact first saturation length* of the one-deletion ordered-pair profile capacity.

**Limiting saturation frequency.** For a uniformly random word \(W_n\in\Sigma^n\) and each fixed \(q\ge3\),
\[
\boxed{\lim_{n\to\infty}\Pr[b(W_n)=M_q]
=\frac{q(q-1)\bigl(q(q-1)-1\bigr)}{q^4}.}
\]
In particular, for a ternary alphabet \((M_3,N_3)=(17,20)\), with limiting frequency \(10/27\); for a four-letter alphabet \((M_4,N_4)=(42,46)\), with limiting frequency \(33/64\).

The claim concerns distinct *profiles*, not distinct deletion-descendant strings. In the previously established binary case \(q=2\), the same capacity formula gives six, but the first saturation length is nine rather than the formula \(N_q\) above; the sharp first-length theorem here explicitly assumes \(q\ge3\).

## Assumptions and scope
The alphabet symbols are distinct and labeled; all words are linear rather than cyclic. Exactly one source symbol, possibly at either endpoint, is deleted. The resulting word has length \(n-1\) and its dinucleotide profile includes all ordered length-two factors, not merely their support, and not the unordered composition of adjacent letters. The empty vector is assigned to a one-letter word. The probabilistic result assumes independent uniform symbols with fixed alphabet size as word length tends to infinity. There is no quotient by letter permutations, reversal, or word rotation.

## Proof
Let \(e_{ab}\) be the coordinate unit vector for the ordered pair \(ab\). Write \(\Delta_i=P(w\setminus w_i)-P(w)\). Deleting the first or last symbol changes the profile by \(-e_{w_1w_2}\) or \(-e_{w_{n-1}w_n}\), respectively. Deleting an internal symbol with surrounding triple \(abc\) changes it by
\[
\Delta(a,b,c)=-e_{ab}-e_{bc}+e_{ac}.
\]
Since the same original vector is added to each change, counting distinct output profiles is exactly counting distinct change vectors.

If \(a=b\) or \(b=c\), the internal change reduces to \(-e_{bb}\). These contribute at most \(q\) different *constant-type* vectors. If \(a\ne b\) and \(b\ne c\), the positive coordinate \(e_{ac}\) and the two negative coordinates \(e_{ab},e_{bc}\) uniquely determine the ordered triple \((a,b,c)\). All \(q(q-1)^2\) such *proper-triple* changes are distinct from each other and from the constant-type changes. Boundary changes add at most two more vectors. This proves \(M_q\).

For equality, all \(q(q-1)^2\) proper triples must appear internally and all \(q\) constant-type changes must appear as well. Both boundary changes must be new and distinct, requiring the first and last adjacent ordered pairs to be unequal-letter pairs and different from each other. Model the word as a directed walk on length-two states \((a,b)\), with each triple \(abc\) an edge \((a,b)\to(b,c)\). Proper triples are precisely edges between unequal-letter states. Each constant-type change \(-e_{aa}\) requires the walk to visit the equal-letter state \((a,a)\). As the walk begins and ends at unequal-letter states, every such equal state requires both an entering and an exiting edge. No edge can be incident to equal-letter states for *two different* symbols. At least \(2q\) nonproper-triple edges are therefore required, in addition to the \(q(q-1)^2\) distinct proper-triple edges. There are \(n-2\) triple edges in a length-\(n\) word. Consequently
\[
n-2\ge q(q-1)^2+2q,
\qquad n\ge N_q.
\]
This proves that no shorter source word can saturate.

For sufficiency at exactly \(N_q\), index the alphabet by \(\mathbb Z/q\mathbb Z\). Build a directed multigraph with states \((a,b)\) for all ordered pairs and include exactly one edge \((a,b)\to(b,c)\) for each proper triple \((a,b,c)\), where \(a\ne b\) and \(b\ne c\). These edges form a balanced strongly connected graph on the unequal-letter states: any state \((a,b)\) can reach \((c,d)\) in two steps when \(b\ne c\), and otherwise in three steps using an auxiliary letter distinct from \(b,d\); this is why \(q\ge3\) is used.

For each symbol \(a\), add an edge \((a-1,a)\to(a,a)\), followed by \((a,a)\to(a,a+1)\), interpreting symbols modulo \(q\). Then change only the second edge at \(a=0\), replacing \((0,0)\to(0,1)\) by \((0,0)\to(0,2)\). The full graph is weakly connected, all vertices except \((0,1)\) and \((0,2)\) are balanced, \((0,1)\) has outdegree exceeding indegree by one, and \((0,2)\) has indegree exceeding outdegree by one. The directed Euler-trail theorem therefore supplies a trail starting at \((0,1)\) and ending at \((0,2)\). The associated overlapping word has exactly \(q(q-1)^2+2q\) internal triple edges and length \(N_q\). It contains every proper triple and both transitions through each equal state, and its unequal initial and final adjacent pairs are distinct. Hence it realizes all \(M_q\) change vectors. The standalone construction gives, for \(q=3\), the explicit 20-symbol witness `01011200201210212202`.

To attain equality at every greater length, append any letter different from the current last letter while keeping the final ordered pair different from the fixed first pair. Such a choice always exists because \(q\ge3\). All previously occurring internal triple types remain present. Thus the original \(q(q-1)^2+q\) interior change types and both distinct boundary types remain present indefinitely.

For the limiting frequency, let \(E_n\) be the event that the initial and final ordered pairs are both unequal-letter pairs and are distinct. For \(n\ge4\) these pairs consist of disjoint independent uniform symbols, so
\[
\Pr(E_n)=\frac{q(q-1)(q(q-1)-1)}{q^4}.
\]
The event \(b(W_n)=M_q\) requires \(E_n\). Conditional on \(E_n\), consider \(k=\lfloor(n-4)/3\rfloor\) disjoint internal triples from positions \(3\) through \(n-2\), independent of the four endpoint symbols. There are \(K=q(q-1)^2+q\) specified triples sufficient for saturation: all proper triples and, for each \(a\), the triple \(aaa\). Each has probability \(q^{-3}\) in an independent three-letter block. A union bound yields
\[
0\le \Pr(E_n)-\Pr[b(W_n)=M_q]
\le K(1-q^{-3})^{\lfloor(n-4)/3\rfloor}.
\]
The upper bound tends to zero exponentially, establishing the limit.

## Verification
The standalone Python program `verify_profile_euler.py` constructs the claimed directed Euler trail and checks its initial and final vertices, every overlapping triple, direct literal deletion profiles, and the exact capacity for each \(3\le q\le8\). It also enumerates ternary words of lengths two through nine directly. The separate C++ program `verify_profile_literal.cpp` constructs deletion descendants and ordered-pair histograms independently, confirms explicit ternary and quaternary witnesses, and exhaustively checks all words of lengths two through ten over a binary alphabet, two through eleven over a ternary alphabet, and two through seven over a four-letter alphabet. Run commands and resulting outputs are included in `VERIFICATION.md` and the two output files.

These computations independently check finite cases and the concrete construction, but the unrestricted alphabet/length theorem and limiting frequency depend on the mathematical arguments above, not on extrapolating computations.

## Relationship to prior work
The previously published *Complete one-deletion dinucleotide-profile ball distribution for binary words* proves six possible profiles for \(q=2\), the first saturation length nine, and a complete binary distribution. Its local-change identity agrees with the one used here, but its domain excludes all \(q\ge3\), and it does not imply the nonbinary capacity, the new exact saturation threshold, or the nonbinary limiting frequencies. The nonbinary equality characterization specifically uses the strongly connected unequal-pair digraph and a deliberately imbalanced Euler trail; this construction fails in the same form for binary words.

Kiah, Puleo and Milenkovic establish the ordered substring-profile channel framework and general coding methods, not this source-local one-deletion output-capacity theorem. A separate study of ternary length-two *composition* profiles globally counts unordered factor-composition observations across all words; it is a different statistic and lacks the single-deletion neighborhood restriction. The existing exact binary ordered two-multispectrum result counts profiles globally across length-\(n\) words, not different profiles generated from a fixed source by one deletion. En Gad's 2026 work motivates substring-count changes under edit operations and improved deletion codes, but the accessible abstract does not establish the present sharp local finite-alphabet capacity or first-attainment law; the relevant full text could not be inspected, so that comparison is a stated priority risk rather than a whole-document noncoverage assertion.

## Limitations
The result treats ordered adjacent-pair multiplicity profiles, one exact source-symbol deletion, linear words, \(q\ge3\), and a fixed alphabet for asymptotics. It does not give the full size-distribution generating function over nonbinary words, handle longer observed substrings or multiple errors, or construct an optimal error-correcting code. The accessible literature checks, including a full binary comparison, do not establish unique historical priority; the full En Gad manuscript was inaccessible during the comparison, and unindexed equivalents under Markov-type terminology remain possible. Independent scientific review has not been performed.

## References
1. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, first public version 2026-09-16, arXiv:2609.19493v1, https://arxiv.org/abs/2609.19493.
2. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, first public version 2015-02-02, arXiv:1502.00517v1, https://arxiv.org/abs/1502.00517.
3. *The complete one-deletion dinucleotide-profile ball distribution for binary words*, previously published research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-complete-one-deletion-dinucleotide-profile-ball-distribution--294c530e44d7/RESULT.md.
4. *Ternary length-two composition profiles and their finite-alphabet growth law*, previously published research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-ternary-length-two-composition-profiles-and-their-finite-alphabe--08e655a29220/RESULT.md.
5. *Exact binary two-multispectrum code size and singleton classification*, previously published research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71/RESULT.md.
