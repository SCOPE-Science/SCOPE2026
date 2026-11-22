# Independent mathematical audit

## correctness

PASS

The indicator has support on the 44 fixed-point-free permutations; at a Walsh frequency its coefficient equals the ordinary integer permanent of the ±1 hollow 5×5 matrix. The 20 allowed off-diagonal cells form the connected bipartite support K5,5 minus its diagonal, with ten nodes and spanning tree of nine edges specified in RESULT.md. Row/column sign gauge fixes those nine signs (one global redundancy), leaving 11 free signs and hence 2048 normalized signings; each class has exactly 2^9 signings, with 2^5 extra inert diagonal frequency bits. Independently evaluated all 2048 signed derangement-monomial permanents and reproduced normalized |W| histogram 0:338,2:504,4:405,6:260,8:130,10:240,12:90,16:60,22:20,44:1. Independently performed a complete 2^20 integer Walsh transform on all 44 binary derangement matrices, reproducing the same histogram multiplied by512 (sum abs5,197,824), hence full 25-bit multiplicities by factor32. Exact zero count 338*2^14=5,537,792, rank28,016,640, min nonzero 2, pseudoinverse norm1/2, normalized 2048-case average |H|=1269/256 and zero probability338/2048=169/1024. Endpoint norms for Fourier projection onto the 44 derangement frequencies equal the kernel L1 norm; no unsupported claim of norm minimality among all projections is made for this record.

## originality

PASS

Compared the actual theorem and its implications against the listed primary source material and published mathematical records, including aliases and substantially broader methods. No decisive prior coverage was found in the accessible evidence; this is a bounded best-of-knowledge originality finding, with residual risks explicitly documented.

## value

PASS

The derangements of five elements form a canonical 44-point subfamily of all permutation matrices; order five is naturally distinguished by prior first-order covariance isotropy. Signed hollow permanents capture genuinely different full-order Walsh cancellations from full ±1 permanent tables or degree-one covariance. Exact zero probability, convolution nullity and sharp 44-frequency projection norm are natural intrinsic finite harmonics useful for restricted assignment models, without a claim about large n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
