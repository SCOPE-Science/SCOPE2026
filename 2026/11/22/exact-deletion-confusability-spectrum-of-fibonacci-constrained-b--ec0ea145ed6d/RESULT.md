# Exact deletion-confusability spectrum of Fibonacci-constrained binary words

## Finding

Let \(\mathcal F_n\) be the set of indexed binary words of length \(n\ge1\) that avoid the contiguous factor `11`. For \(x\in\mathcal F_n\), let \(\Delta(x)\) be the **set** of distinct length-\(n-1\) words obtained by deleting exactly one coordinate, including either endpoint and either symbol. Let \(G_n\) be the simple graph with vertex set \(\mathcal F_n\) and an edge \(\{x,y\}\) for distinct vertices precisely when \(\Delta(x)\cap\Delta(y)\ne\varnothing\). Write \(e_n=|E(G_n)|\), and define \(e_0=0\) for generating-function bookkeeping.

**Theorem.** The exact all-length ordinary generating function of confusable unordered pairs is
\[
\sum_{n\ge0}e_nz^n
 = \frac{z(1-z+z^3)}{(1-z)(1-z-z^2)^3}
 = \frac{z}{(1-z-z^2)^2}+\frac{z^2}{(1-z)(1-z-z^2)^3}.
\]
The first summand counts precisely the confusable pairs that differ in exactly one coordinate (the ordinary Fibonacci-cube edges); the second counts precisely those pairs that are confusable by deletion but **not** adjacent in the Fibonacci cube. In particular the first ten edge counts are
\[
(e_1,\ldots,e_{10})=(1,3,9,23,55,124,268,560,1139,2266).
\]
If \(\phi=(1+\sqrt5)/2\), then
\[
e_n\sim \frac{\phi^3}{10\sqrt5}\,n^2\phi^n,\qquad
\frac{2e_n}{|\mathcal F_n|}\sim\frac\phi5 n^2.
\]
These are statements about graph edges and mean degree, not exact maximum code sizes.

## Assumptions and scope

Only source words must avoid `11`; their deletion outputs are not constrained. Sources are **linear indexed** binary words, without quotient by rotations, reversal, complementation, or leading-zero removal. Two sources are adjacent whenever their deletion-shadow intersection is nonempty, even if several distinct deletion pairs yield the same output. The alphabet is literally \(\{0,1\}\), and the theorem holds for every integer \(n\ge1\).

The source graph is the ordinary one-deletion confusability graph *induced* on the length-\(n\) binary Fibonacci language. It is not the Hamming graph (the usual Fibonacci cube), not the two-read reconstruction graph (which requires two common outputs), and not a channel that deletes only zero symbols.

## Proof

**1. A finite-state characterization.** We count *ordered* input pairs \((x,y)\) of equal length that have a common one-deletion output. Read the pairs \((x_i,y_i)\) synchronously. Use six nondeterministic bookkeeping states: \(P\), for an equal prefix before either deletion; \(Q\), for after both deletions; \(X_0,X_1\), when a position of \(x\) was deleted first and the indicated last-read bit from \(y\) awaits its match in \(x\); and the symmetric states \(Y_0,Y_1\) when a position of \(y\) was deleted first.

At a read pair \((a,b)\), state \(P\) may continue as \(P\) if \(a=b\), may delete both current coordinates and enter \(Q\), may delete only the current \(x\)-coordinate and enter \(X_b\), or may delete only the current \(y\)-coordinate and enter \(Y_a\). State \(Q\) continues as \(Q\) if and only if \(a=b\). From \(X_c\) a transition is legal precisely when \(a=c\); it either deletes the current \(y\)-coordinate and enters \(Q\), or consumes that bit for the next alignment and enters \(X_b\). The \(Y_c\) transitions are symmetric: require \(b=c\), then enter \(Q\) or \(Y_a\). Initially only \(P\) is active; accept only if \(Q\) is active after the last pair. Every accepting path chooses exactly one deleted coordinate in each word and matches all surviving symbols. Conversely any two choices of deletions yielding identical survivors specify an accepting path, so this is an exact *existential*, not multiplicity-weighted, characterization.

Determinize by carrying the **subset** of the six active states, and store the previous read bit of each word to reject `11` on either track. There are exactly 17 reachable deterministic states, including the starting state; the supplied `artifacts/verify_transfer.py` reconstructs every state and transition from these rules.

Two deterministic states are counting-equivalent if they have the same acceptance value and, for every equivalence class, the same **number** of permitted labeled pair transitions into that class. Iterative refinement from accepting/nonaccepting yields twelve stable classes. Three classes cannot reach an accepting state and contribute zero to every accepted completion. Prune them and label the remaining nine productive classes \(A,B,C,D,E,F,G,H,I\) in breadth-first order, with \(A\) initial. In the table, \(T^m\) means exactly \(m\) outgoing pair-symbol transitions to state \(T\), and an absent entry means zero transitions. Every state except \(A\) is accepting.

| State | Weighted outgoing productive transitions |
|---|---|
| \(A\) | \(B,2C,D\) |
| \(B\) | \(B,2C,D\) |
| \(C\) | \(C,E\) |
| \(D\) | \(B\) |
| \(E\) | \(E,F,G\) |
| \(F\) | \(H,I\) |
| \(G\) | \(H\) |
| \(H\) | \(G,H\) |
| \(I\) | \(E,F\) |

Let \(M\) be this integer transition matrix, \(b=(0,1,1,1,1,1,1,1,1)^{\mathsf T}\), and let \(u(z)=(I-zM)^{-1}b\) be the unique formal-power-series solution of \((I-zM)u=b\). Then the count of accepted ordered pairs of length \(n\) is \([z^n]u_A(z)\). The integer polynomial certificate `artifacts/transfer_certificate.json` contains the *complete numerator vector* \(p(z)\) and common denominator
\[
 d(z)=(1-z)(1-z-z^2)^3
\]
with a coefficientwise identity \((I-zM)p(z)=d(z)b\). In particular its initial-state component is
\[
 p_A(z)=4z-7z^2-z^3+9z^4+z^5-3z^6-z^7.
\]
Since \(d(0)=1\), the polynomial identity determines the formal series uniquely and proves \(u_A(z)=p_A(z)/d(z)\) at *all* lengths. The standard-library verification program derives the nine productive quotient states independently from the original six-state rule and checks all nine coefficientwise integer identities. Thus the transfer evaluation does not rely on a guessed recurrence or a finite experimental extrapolation.

**2. From ordered to unordered pairs.** All words \(x\in\mathcal F_n\) have \(\Delta(x)\ne\varnothing\) for \(n\ge1\), hence all diagonal ordered pairs are accepted. Non-diagonal accepted pairs occur in both orientations. The total number of vertices has generating function
\[
 F(z)=\sum_{n\ge0}|\mathcal F_n|z^n=\frac{1+z}{1-z-z^2},
\]
where \(|\mathcal F_0|=1\), whereas the state machine rejects the empty pair. Thus
\[
 \sum_{n\ge0}e_nz^n=\frac12\left(u_A(z)-F(z)+1\right)
 =\frac{z(1-z+z^3)}{(1-z)(1-z-z^2)^3}.
\]
This counts each graph edge exactly once regardless of how many deletions witness the edge.

**3. The Hamming-only comparison.** Each pair at Hamming distance one in the induced Fibonacci cube has a unique endpoint having a `1` in its one differing position. Flipping that `1` to `0` is always admissible. These edges are therefore counted by the total number of ones across the words in \(\mathcal F_n\). The weight-refined language generating function is
\[
 F(z,t)=\frac{1+tz}{1-z-tz^2},
\]
so differentiating formally at \(t=1\) gives
\[
 H(z)=\left.\frac{\partial F(z,t)}{\partial t}\right|_{t=1}
 =\frac{z}{(1-z-z^2)^2}.
\]
Every such Hamming edge is deletion-confusable by deleting the differing coordinate in both sources. Subtracting \(H(z)\) from the preceding exact edge enumerator gives precisely \(z^2/((1-z)(1-z-z^2)^3)\), whose coefficients are positive for every length at least two. This establishes the claimed partition of edges.

**4. Asymptotics.** The smallest-modulus pole of the edge generating function is at \(z=\phi^{-1}\), of order three. Its leading singular coefficient is \(\phi^3/(5\sqrt5)\); coefficient extraction from \((1-\phi z)^{-3}\) gives \(e_n\sim \phi^3 n^2\phi^n/(10\sqrt5)\). The Fibonacci word count is \(|\mathcal F_n|=F_{n+2}^{\mathrm{Fib}}\sim\phi^{n+2}/\sqrt5\), giving the stated mean-degree asymptotic.

## Verification

All certificate and experiment paths below are embedded alongside this document. Run `python3 artifacts/verify_transfer.py` to reconstruct the entire synchronous pair automaton, enforce the forbidden `11` constraint, calculate its 17 reachable states and stable twelve-class quotient, prune the three dead classes, reconstruct the nine-state integer matrix, and verify \((I-zM)p=d b\) coefficient-by-coefficient. Expected output: `TRANSFER_CERTIFICATE_OK states=17 quotient=12 productive=9`.

Separately run `python3 artifacts/verify_bruteforce.py`: this program enumerates every admissible word, builds the actual distinct one-deletion shadow of each, unions *unordered* confusable pairs in a set, and compares its count against coefficients of the stated rational generating function for every length from one through fifteen. It also independently checks that the number of Hamming-only edges equals the ones-count in the input language. Expected last line: `BRUTE_FORCE_OK 15`. This exhaustive finite test is corroboration only; the all-length proof is the finite-state construction and exact polynomial identity.

## Relationship to prior work

Kulkarni and Kiyavash's 2012 foundational treatment derives constrained-source deletion-code upper bounds, including a run-length-limited example with additional endpoint conventions. Section V-A does not enumerate the edges of the full one-deletion confusability graph of arbitrary linear words avoiding `11`. Cullina, Kulkarni and Kiyavash's 2012 paper describes the unrestricted deletion graph, constant-weight constructions and colorings, rather than this exact constrained edge enumerator. The 2015 Gravier–Mollard–Špacapan–Zemljič work studies **hypercube** (Hamming-adjacency) subgraphs of Fibonacci cubes, which account only for the first summand, not the additional deletion-only edges.

A closely relevant published finite record, *First fractional deletion-packing gaps for Fibonacci-constrained binary words* (2026-11-02), studies the same input language and deletion channel, but proves exact integer and fractional **packing optima only for lengths one through seven**, with no all-length edge formula in its inspected `RESULT.md`. Those finite codebook results neither contain nor imply the rational edge enumerator above. No claim is made that the edge count alone determines a maximum deletion-correcting code size.

## Limitations

Originality is assessed against the accessible indexed records and inspected source text, not established as an exhaustive historical priority claim; unindexed computations and unavailable related papers remain risks. The all-length theorem is limited to binary linear words forbidding consecutive ones and exactly one *arbitrary-symbol* deletion from each word. It does not address circular Fibonacci/Lucas constraints, multiple deletions, full code capacity, graph degree distribution, or a different physical read model. The certificate proves a finite polynomial identity and automaton interpretation; independent mathematical audit has not been performed.

## References

1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, first publicly posted 2012-11-13, https://arxiv.org/abs/1211.3128 ; relevant HTML full text, Sections V and V-A.
2. D. Cullina, A. A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, first posted 2012-11-16, https://arxiv.org/html/1211.4056v1 ; especially Sections II-B, III, IV.
3. S. Gravier, M. Mollard, S. Špacapan and S. Zemljič, *On Disjoint Hypercubes in Fibonacci Cubes*, first posted 2015-04-03, https://arxiv.org/abs/1504.00829 ; Fibonacci-cube Hamming graph, not deletion conflicts.
4. *First fractional deletion-packing gaps for Fibonacci-constrained binary words*, published research record 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-first-fractional-deletion-packing-gaps-for-fibonacci-constrained--25a61255a325 ; inspected `RESULT.md` and the stated length scope.
