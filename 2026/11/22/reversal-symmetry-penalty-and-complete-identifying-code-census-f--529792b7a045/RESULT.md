# Reversal-symmetry penalty and complete identifying-code census for Fibonacci cubes through dimension seven

## Finding

Let \(\Gamma_n\) be the Fibonacci cube: its vertices are the indexed binary words of length \(n\) avoiding `11`, and two distinct vertices are adjacent exactly when their Hamming distance is one. An *identifying code* is a set of detector vertices whose intersections with all closed radius-one neighborhoods are nonempty and pairwise distinct. Let \(I_n\) be its smallest cardinality, \(A_n\) the number of labeled minimum codes, \(I_n^{\mathrm{rev}}\) the smallest cardinality of an identifying code invariant under word reversal, and \(A_n^{\mathrm{rev}}\) the number of reversal-invariant codes of that latter smallest cardinality.

For \(2\le n\le7\), the exact census is:

| \(n\) | Vertices | \(I_n\) | \(A_n\) | \(I_n^{\mathrm{rev}}\) | \(A_n^{\mathrm{rev}}\) | Reversal-fixed among \(A_n\) | Orbits among \(A_n\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 2 | 1 | 2 | 1 | 1 | 1 |
| 3 | 5 | 3 | 6 | 3 | 2 | 2 | 4 |
| 4 | 8 | 4 | 14 | 4 | 2 | 2 | 8 |
| 5 | 13 | 5 | 2 | 6 | 8 | 0 | 1 |
| 6 | 21 | 8 | 18 | 8 | 2 | 2 | 10 |
| 7 | 34 | 12 | 13 | 12 | 5 | 5 | 9 |

For \(n=1\) no identifying code exists because the two vertices have identical closed neighborhoods.

Consequently, **dimension five is the first dimension admitting identifying codes for which mandatory reversal symmetry costs an additional detector**, while the minimum-size reversal penalty vanishes again at dimensions six and seven:

\[
I_5=5<I_5^{\mathrm{rev}}=6,\qquad I_6=I_6^{\mathrm{rev}}=8,\qquad I_7=I_7^{\mathrm{rev}}=12.
\]

At dimension seven there are exactly thirteen labeled minimum twelve-detector codes, five of them reversal-fixed. They form nine reversal classes. Every one of the thirteen twelve-word codebooks is listed in `OPTIMA_N7.tsv`.

## Assumptions and scope

The graph is simple and undirected; a detector observes its own vertex and all adjacent vertices. All binary words are indexed, not quotient words. Reversal acts simultaneously on every word, and no other group action is quotiented out in the labeled counts. The claims concern precisely the seven dimensions \(1\le n\le7\), with the nonexistence case at one, and make no assertion about dimensions above seven.

## Proof

For any graph vertex \(v\), write \(B(v)=\{u:d(u,v)\le1\}\). For a selected detector set \(S\), the signature at \(v\) is \(S\cap B(v)\). The requirement that each \(S\cap B(v)\) be nonempty, together with the equivalence below for distinct \(u,v\),

\[
S\cap B(u)\ne S\cap B(v)\iff S\cap\bigl(B(u)\mathbin{\triangle}B(v)\bigr)\ne\varnothing
\]

show that a detector set identifies every vertex exactly when it *hits* every member of the finite family

\[
\mathcal H_n=\{B(v):v\in V(\Gamma_n)\}\ \cup\
\{B(u)\mathbin{\triangle}B(v):u<v\}.
\]

The arbitrary total order in the second set is simply the natural binary-integer order on vertex words. This reduction is an equivalence, not merely a relaxation. For \(n=1\), the symmetric difference of the two closed neighborhoods is empty, proving impossibility.

For \(2\le n\le6\), `fib_identifying_verify.cpp` enumerates all \(2^{F_{n+2}}\) detector subsets, checks the signatures exactly using integer bitmasks, and counts every minimum-size feasible set. It also tests each set for invariance under coordinate reversal and counts the smallest invariant sets. The completely separate enumeration in `fib_identifying_alternate.cpp` reproduces each result. Since every subset is tested, the stated minima and complete counts in these dimensions follow.

For \(n=7\), there are \(34\) vertices and exactly \(595\) distinct nonempty hitting requirements after removing duplicate sets. The exact recursive search chooses any unmet requirement \(R\in\mathcal H_7\), branches on every potential new detector in \(R\), and explores the resulting partial code. This is exhaustive because each valid completion must select at least one detector from \(R\). The search prunes if the detector budget has been exceeded. Its second pruning rule greedily selects a family of pairwise disjoint as-yet-unmet requirements: every completion must add at least one *different* detector for each of them, so a branch with too few remaining detector positions is impossible. Both rules are logically sound for finite hitting-set search.

With a budget of eleven, the recursion finds no valid code. With a budget of twelve, it collects, by exact bitmask identity, all thirteen distinct solutions; their unambiguous encodings are reproduced in `OPTIMA_N7.tsv` and independently checked by `fib_identifying_alternate.cpp`. Thus \(I_7=12\) and \(A_7=13\). The main verifier's actual recursive visit counts are \(1{,}345{,}072\) and \(14{,}117{,}207\), respectively; these counts aid reproduction but are not substituted for the mathematical exhaustiveness argument.

For the invariant minimum at dimension seven, partition its \(34\) vertices into the \(21\) orbits of reversal. A reversal-invariant detector set must be a union of these orbits. Independent exhaustive enumeration of the \(2^{21}\) possible orbit selections shows that the minimum size is twelve, attained by five sets; all five occur among the thirteen unrestricted optimizers. At dimension five, the two unrestricted optimizers are exchanged by reversal, and none is invariant. There are exactly eight invariant identifying codes of minimum size six, proving the sharp one-detector penalty.

Finally, reversal preserves Hamming distance and the no-`11` condition, so it induces an involution on every minimum-code family. By elementary orbit counting, the number of reversal classes is half the sum of the total minimum-code count and its reversal-fixed count. The last column follows.

## Verification

The self-contained C++17 sources `fib_identifying_verify.cpp` and `fib_identifying_alternate.cpp` use integer arithmetic, exact bitmasks, and no optimization library. They can be compiled and run with:

```sh
g++ -std=c++17 -O3 fib_identifying_verify.cpp -o verify
./verify
g++ -std=c++17 -O3 fib_identifying_alternate.cpp -o alternate
./alternate OPTIMA_N7.tsv
```

Expected terminal success markers are `VERIFY_OK` and `ALTERNATE_OK`. The secondary checker independently enumerates all labeled detector subsets in dimensions two through six, enumerates all reversal-invariant subsets at dimension seven, and checks every recorded twelve-detector optimum. No numerical tolerance, floating-point optimization, finite sampling, or unverified external solver is needed for the claimed finite proof.

## Relationship to prior work

Identifying codes model unique closed-neighborhood detector signatures, as formalized by Chen, Lu and Miao for paths and cycles [1]. The Fibonacci cubes and their network motivation are standard. Castro, Klavžar, Mollard and Rho [2] prove that for dimensions at least two the automorphism group of a Fibonacci cube is generated by word reversal, and compute domination and 2-packing invariants on the same graph family. Those invariants are not identifying-code minima or counts: domination requires only nonempty signatures, whereas identifying codes additionally require all signatures to differ; 2-packing maximizes separated vertices instead of minimizing globally distinguishing detectors. Ren [3] studies domination bounds, not identification. Ashrafi and collaborators [4] prove absence of perfect efficient-dominating codes for larger Fibonacci cubes; perfect domination and identifying codes are different conditions, and their theorem does not imply the new census.

These sources provide direct motivation and terminology, while the new content is the complete stated identifying-code census and dimension-five reversal penalty. Searches under identifying, separating, reversal-invariant, vertex-fingerprint, and Fibonacci-network terminology found no matching exact table. Such search results are not a proof of historical priority.

## Limitations

The exhaustive upper bounds apply only for \(n\le7\). The counting does not determine an asymptotic identifying-code rate, a general recurrence, or higher-radius identification. The thirteen dimension-seven optimizers are verified by exact enumeration, but the result has not undergone independent external mathematical audit. An earlier unindexed enumeration or equivalent invariant remains a possible historical-priority risk. The verification programs are finite exhaustive algorithms, not formal proofs in a proof assistant.

## References

1. C. Chen, C. Lu, Z. Miao, *Identifying codes and locating-dominating sets on paths and cycles*, arXiv:0908.2750v1 (first public posting August 19, 2009). https://arxiv.org/abs/0908.2750
2. A. Castro, S. Klavžar, M. Mollard, Y. Rho, *On the domination number and the 2-packing number of Fibonacci cubes and Lucas cubes*, Computers & Mathematics with Applications 61 (2011), 2655–2660. https://www-fourier.ujf-grenoble.fr/~mollard/accepte/FibonacciLucas5.pdf
3. S. Ren, *The Larger Bound on the Domination Number of Fibonacci Cubes and Lucas Cubes*, Journal of Applied Mathematics (2014), article 954738. https://doi.org/10.1155/2014/954738
4. A. R. Ashrafi, J. Azarija, A. Babai, K. Fathalikhani, S. Klavžar, *The (non-)existence of perfect codes in Fibonacci cubes*, Information Processing Letters 116 (2016). https://users.fmf.uni-lj.si/klavzar/preprints/Fibonacci-PC-final.pdf
