# Independent mathematical audit

## correctness

PASS

The mechanical rotation cells have n+1 distinct factor codes, with boundary β_j swapping adjacent 01/10 at rank ceil(jα). T^k deletes the first min(k,#ones) ones and appends them, so exactly cuts j with j<=floor(k/α) merge; retained weight cuts distinguish others. A rightmost-remaining-digit argument rules out nonlocal collisions. Thus ρ=max(2,n+1-floor(k/α)) for all n,k>=1, including n=1. The older full proof also derives monotone phase-ordered images. Independent direct mechanical-factor/tortoise simulation matched 1,332 (α,n,k) checks across four irrational slopes, n<=37,k<=9; this does not substitute for the all-slope proof.

## originality

FAIL

The October 25 2026 published complete theorem All-iterate tortoise complexity of Sturmian words already proves exactly ρ=max(2,n+1-floor(k/α)) for every irrational α and n>=1, k>=2; its proof explicitly states it also works for k=1 and its test covers k=1. It also states the same abelian-agreement cutoff. Current theorem adds no distinct mathematical result: fiber phase-cut characterization is already implicit/explicit in the earlier cell-boundary proof. Universal formula and proof structure are covered, so novelty FAIL despite correctness.

## value

PASS

Computing a complete repeated-sorting complexity profile of Sturmian factor languages is mathematically motivated by an established stack-sorting question; the phase-boundary collapse and exact stabilization cutoff are useful structural information. Its significance does not restore originality against an earlier proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
