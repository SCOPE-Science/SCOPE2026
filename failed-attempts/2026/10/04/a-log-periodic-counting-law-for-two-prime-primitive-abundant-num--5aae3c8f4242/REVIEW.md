# Independent mathematical audit

## correctness

PASS

Odd two-prime-support numbers are deficient since product of maximal divisor-sum ratios <=(3/2)(5/4)=15/8<2. Write n=2^a p^b, B=2^(a+1), d=B-p>0. Strict abundance forces d p^b>B-1, while deficiency of n/p forces d p^(b-1)<B-1; if b>=2, (d-1)(p-1)<0, impossible. Thus b=1 and maximal-proper-divisor tests give 2^a<p<2^(a+1)-1, a>=2. Counting every completed dyadic block and partial current block yields P2(X)=pi(U)-2-M(U), U=min(X/2^m,2^(m+1)), X>=16, m=floor(log4 X). The number of Mersenne endpoints is O(log X), and uniform PNT for U/2^m in [1,2] gives phase 2min(r,2)/sqrt(r) with liminf2, limsup2sqrt2. Independently checked exact counts for X=16,20,88,1024,2000,10000,99999 with a separate small primality enumeration. The repository verifier to 500000 corroborates but is not the proof. Rendered RESULT.md has a form-feed/frac typographic glitch in one repeated display; the mathematical statement is also correctly displayed elsewhere.

## originality

FAIL

The phase claim is an immediate explicit counting/PNT consequence of the already established complete classification for even primitive-abundant numbers with exactly two prime factors; lack of verbatim asymptotic in surveyed tables is not sufficient for originality against this strong implication.

## value

PASS

The phase-dependent exact natural counting function and distinct liminf/limsup are useful arithmetic descriptors, with an exact Mersenne-prime exclusion and nonexistence of one constant asymptotic. They are mathematically motivated by primitive abundance with omega=2 rather than an arbitrary finite slice, though their immediate derivation from known classification and PNT prevents novelty-based acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
