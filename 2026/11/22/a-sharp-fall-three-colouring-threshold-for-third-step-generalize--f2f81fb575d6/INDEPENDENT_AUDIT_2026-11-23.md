# Independent mathematical audit

## correctness

PASS

For n≥7 the listed edges give distinct degree-three neighbours. Properness and the two-neighbour-colour equalities are exactly the five local conditions, and involve only a seven-column window. A state contains the first six columns and a valid transition appends the seventh while dropping the first. A cyclic length-n word returns to its starting state after n such transitions; with equal initial six columns, concatenating walks therefore checks the crossing windows too. All eleven explicit words and the common six-column state for n=10,…,18 were verified directly against adjacency. The sums 10+(10,…,18) and 11+18 cover 20,…,29, and repeating 10 covers all larger sizes. For n=7 and 8 an independent exhaustive enumeration without orbit quotienting checked respectively 126 and 258 proper named outer words, 2016 and 6630 spoke/outer-neighbour-compatible extensions, and 252 and 192 with inner-edge properness; none was fully fall-valid. A separate adjacency backtrack with u_0=0,u_1=1 (permitted by palette symmetry) checked 84 and 939 proper full assignments respectively and found zero with exactly two colours in every neighbourhood. Even n is cubic bipartite by assigning opposite spoke parity and using the odd step 3, so the cited at-most-four theorem applies. In fact at n=8 a direct four-colour witness is outer 01010101 and inner 23232323; every vertex sees its same-ring alternate colour and its spoke colour. Two proper colours give only one neighbour colour, so the stated exact even-order values follow.

## originality

PASS

For exactly three available colours a proper two-homogeneous colouring and a fall three-colouring are the same constraint. The relevant cubic-bipartite theorem supplies four colours in general and three only under additional conditions, and the inspected same-family equitable-colouring results concern a different palette and neighbour-count condition. The full two-exception threshold with a construction for every larger order, including odd n, is not covered by the inspected comparisons.

## value

PASS

The result resolves an exact three-colour existence question in a standard infinite family. It distinguishes the two genuine small exceptions from every larger order by exact exclusion and a constructive uniform local splicing method. In the even subfamily it answers the three-versus-four question that the general cubic-bipartite bound leaves unresolved, rather than just improving a numerical search range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
