# Sharp height-four reset threshold and exact spectrum of binary maximal prefix-code decoders

## Finding

Let \(C\subset\{0,1\}^{+}\) be a finite maximal prefix code whose longest codeword has length exactly \(4\). Its literal decoder has one state for each proper prefix of a codeword (including the empty word), and whenever a letter completes a codeword the decoder returns to its root. For a synchronizing decoder, write \(s(C)\) for the minimum length of a word that maps all its states to one state.

There are exactly \(651\) such labeled codes: \(632\) have a synchronizing decoder, and \(19\) do not. The exact distribution of \(s(C)\) is:

| Shortest reset length | Number of codes |
|---:|---:|
| 1 | 2 |
| 2 | 20 |
| 3 | 44 |
| 4 | 92 |
| 5 | 96 |
| 6 | 56 |
| 7 | 50 |
| 8 | 144 |
| 9 | 118 |
| 10 | 4 |
| 11 | 2 |
| 12 | 2 |
| 17 | 2 |

Let \(s_2(k)\) denote the largest shortest reset length among synchronizing finite maximal binary prefix codes of exact maximum word length \(k\). Consequently, the sharp height-four extremum is \(s_2(4)=17\). Exactly two labeled codes attain it: \(C_0=\{000\}\cup(\{0,1\}^{4}\setminus\{0000,0001\})\) and its bitwise-complement code \(C_1\). Their literal decoders have \(14\) states. The word `00011110001111000` resets the first decoder, and its bitwise complement resets the second, each in \(17\) letters.

## Assumptions and scope

The alphabet is the **labeled binary alphabet** \(\{0,1\}\), and the codes must be **finite, maximal and prefix-free**, with exact maximum codeword length \(4\). Labeled codes are counted separately; complementing all letters exchanges two codes unless the code is invariant. We use the full proper-prefix *literal* decoder, not a minimized DFA. Unsynchronizing codes have no value of \(s(C)\) and are counted separately. This statement does not concern larger heights or alphabets.

## Proof

A finite binary maximal prefix code corresponds bijectively to a rooted, full, ordered binary tree with codewords at its leaves; its internal vertices are the proper-prefix states. Let \(T_h\) count such trees whose leaves have depth at most \(h\), also including the formal tree consisting of one empty leaf. Then \(T_0=1\) and \(T_h=1+T_{h-1}^{2}\), since a tree is either one leaf or a root with an independently chosen left and right subtree. Thus \((T_0,T_1,T_2,T_3,T_4)=(1,2,5,26,677)\), and exactly \(T_4-T_3=651\) trees have height exactly four. The one formal empty-leaf tree never enters the height-four enumeration.

For each such tree, index its internal vertices \(0,\dots,m-1\) by traversal, root \(0\). There are at most \(1+2+4+8=15\) internal vertices. Define \(\delta(q,c)\) to be the internal child indexed by the extended prefix if it exists, and \(0\) otherwise, because a missing internal child of a full prefix tree is a leaf completing a codeword. For each nonempty mask \(S\subseteq\{0,\ldots,m-1\}\), define \(\delta(S,c)=\{\delta(q,c):q\in S\}\). Starting from the full mask, breadth-first search along labels \(0\) and \(1\) visits every reachable mask and assigns its exact minimum word length. This is true by induction on word length, since every word is a path through this finite subset graph. The first singleton has shortest possible reset length; if no singleton is reachable, there is no reset word. No upper cutoff is assumed: the entire reachable subset graph is explored (at most \(2^{15}-1\) masks per code).

The standalone Python and C++ programs included with this statement independently generate all \(677\) trees and compute their decoder distances. Both produce exactly the histogram above, \(19\) nonsynchronizing height-four decoders, and exactly two extremal codes with shortest reset length \(17\). Hence the exhaustive finite enumeration, together with the coverage and shortest-path arguments, proves the classification. The extremal two-depth codes also have the independently established length \(17\) from Chadha's theorem; that theorem by itself does not cover the additional height-four tree shapes with shallow leaves.

## Verification

Run `python3 prefix_verify.py` (Python standard library only) and independently compile and run `c++ -std=c++17 -O2 prefix_verify.cpp -o prefix_verify && ./prefix_verify`. Both programs check the expected height-four histogram and the uniqueness count of the two extremizers by explicit assertions. The first enumerates nested tree tuples and precomputes subset transitions. The second parses parenthesized tree descriptions and computes subset images directly. Both exhaust all reachable subsets rather than searching only up to a guessed bound. The Python output includes the two shortest-word witnesses, which were also simulated directly in the literal decoders.

## Relationship to prior work

Chadha [1], first publicly posted on 3 November 2026, proves a general upper bound \((k-1)(4k-5)\) for synchronizing maximal-prefix-code literal decoders, and a sharp bound \(2(k-1)^2-1\) when all codeword lengths are the two consecutive values \(k-1\) and \(k\). For binary height four, the published general interval is \(17\le s_2(4)\le33\); [1] already constructs the two displayed extremal decoders with shortest reset length \(17\). The new part is the assertion that *no other height-four tree* exceeds \(17\), the complete \(651\)-code distribution, and the precise synchronizing/nonsynchronizing split. Ryzhikov and Szykuła [2] develop algorithms for synchronizing literal Huffman decoders; their results do not state this exhaustive height-four spectrum.

## Limitations

This is an exact finite exhaustive theorem, not a symbolic all-height formula. Its proof depends on reproducibly executing or checking the supplied complete enumerators; numerical logs alone would not establish completeness. The two maximizers and their reset lengths were known from [1]; no new all-height extremal construction is claimed. Other alphabets and heights beyond four are not classified. An equivalent unindexed census remains possible and warrants external examination. Independent validation has not been performed.

## References

[1] Samrath Singh Chadha, *Quadratic reset bounds for finite maximal prefix codes*, arXiv:2611.05675, first publicly submitted 3 November 2026, https://arxiv.org/abs/2611.05675.

[2] Andrew Ryzhikov and Marek Szykuła, *Finding Short Synchronizing Words for Prefix Codes*, arXiv:1806.06299, 2018, https://arxiv.org/abs/1806.06299.
