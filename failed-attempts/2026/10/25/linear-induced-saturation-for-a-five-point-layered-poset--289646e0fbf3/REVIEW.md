# Independent mathematical audit

## correctness

FAIL

The family F_n={empty,[n],all singletons,all co-singletons} has exactly 2n+2 members for n>=4. Incomparable pairs cannot have a common strict upper 3-chain in F_n. Every missing S with 2<=|S|<=n-2 yields an induced P by two distinct singleton subsets of S, S, a co-singleton containing S and [n]. The cited 2023 legs theorem proves ONLY sat*(n,P)>=n+1, not the source asserted strict inequality sat*(n,P)>n+1 for n>3. No additional argument in the frozen package establishes the claimed n+2 lower bound for every n. This unsupported load-bearing lemma makes C FAIL for the joint two-sided claim, although the upper family is correct. Independently enumerated all missing sets and checked induced saturation for n=4,5,6. Also independently validated Freschi et al's *older stronger* family size n+5 for n=4..8. Thus correctness does not supply originality.

## originality

FAIL

DECISIVE PRIOR COVERAGE: Freschi, Piga, Sharifzadeh and Treglown, The Induced Saturation Problem for Posets (Combinatorial Theory 3(3), 2023), Section 2, Proposition 2.9, explicitly define wedge_{ell} as two incomparable legs with ell-point chain above and prove for ell=2 that n+1 <= sat*(n,wedge_3) <= n+5 for all n>=4. Our P is exactly wedge_3; its 2023 n+5 bound is strictly tighter than this submission's 2n+2 for n>=4, with strict inequality for n>3. Ivan and Jaffe 2025, Saturation for Sums of Posets and Antichains, Theorem 14, already establishes O(n) for *all* complete multipartite posets, including the same (2,1,1,1), while its Theorem 13 supplies linear lower bounds. The original headline Theta(n) and its upper bound are therefore covered. The numerical n+2 lower bound is a potential one-unit strengthening of the published n+1 bound, but the cited lemma in the package does not prove it. This cannot rescue a main classification and upper bound already covered by prior results.

## value

FAIL

The natural poset and invariant are motivated, but the all-n linear growth and even a sharper explicit upper were already established in 2023/2025. Only an unproved one-unit lower-bound strengthening is left in the 2026 package, without a demonstrated new mechanism or meaningful cutoff; the submitted main mathematical conclusion offers no significant improvement. This is a scientific value failure grounded in dominating primary results, not in inability to access sources or an arbitrary higher value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
