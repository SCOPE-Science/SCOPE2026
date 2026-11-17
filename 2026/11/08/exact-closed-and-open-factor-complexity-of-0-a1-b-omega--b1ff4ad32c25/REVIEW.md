# Independent mathematical audit

## correctness

PASS

The primitive two-run period has one symbol transition of each kind. A starting position j into a run of length d, with r=d-j remaining letters, has first positive prefix-return displacement 1 when ell<r, p-j when ell=r, and p when ell>r, where p=a+b. Closedness is equivalent to the first return being exactly the factor length minus its proper-border length. For n<=p this yields unary words and balanced equal-wing two-transition words; for n=p+h it yields min(d,h-1) ordinary starts per run and one additional parity-compatible start if 1<=h<=d and h congruent to d mod 2. The period has p distinct phases for n>=p, and subtracting these closed counts from P(n)=min(n,a)+min(n,b) gives all open counts. At h=max(a,b), every phase closes; at h=max(a,b)-1 a phase is open, including a=b=1. Independent direct border and factor enumeration checked 936 length/parameter cases. Universal result rests on first-return proof.

## originality

PASS

The relevant first-return, closed-rich and periodicity papers give qualitative periodic behavior or global extremal bounds, not the exact two-parameter n-dependent closed/open profile. Resultary finds related 2-Abelian, tortoise and complement-factor results for the same period but different invariants. Best-of-knowledge PASS with unindexed-priority caveat.

## value

PASS

PASS: Closed/open complexity is a standard combinatorics-of-words invariant. The explicit parity-resolved full length profile and sharp last-open length for all two-run periods are not implied by a qualitative general eventual-closedness theorem, and the exact two-parameter boundary is reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
