# Independent mathematical audit

## correctness

PASS

Write r=(a,a+b,a+b+c) for the numbers of zeros preceding successive ones, and N=n-3. The three counts with two zeros are sums over r_i of binomial(r_i,2), r_i(N-r_i), and binomial(N-r_i,2); they depend exactly on N, T=sum r_i and Q=sum binomial(r_i,2). The two-ones counts are U=3a+b, 2(T-U) and 3N-2T+U; pure-symbol counts depend only on N. Conversely Q,U,T are read from 001,011,101, so (N,T,U,Q) is sufficient and necessary. Equal N,T,U force the gap shift t(1,-3,3,-1), which changes r by (t,-2t,t). Expanding the binomial squares yields exactly Q'-Q=t(c-b+3t), so the only possible distinct mate is the stated swap with t=(b-c)/3, subject to integrality and nonnegativity. It is involutive. Orient a pair by c>b and use c=b+3h, a=A+h: its unique nonnegative parameters satisfy N=A+d+2b+4h with h>=1. Counting A+d gives the double sum and multiplying the four geometric series gives the pair generating function. Each pair reduces the number of classes by one; subtract from the count of weight-three words. When n<3 there are no words, and N>=4 is necessary for pairs, with the first at n=7. Independent dynamic counts recover all classes and the complete pair map through n=19; that finite corroboration is separate from the all-n proof.

## originality

FAIL

Chrisnata et al. genuinely pose the exact rational function as Conjecture 1, not a theorem there. But distinct Resultary entry 39c59472a4df contains the same all-length proof, quadratic collision identity, gap involution and pair enumeration. Its statistics (A,B,F) are (U,3N-2T+U,Q), exactly an invertible change at fixed N. It parameterizes the very same pairs from the opposite representative. Other indexed findings independently establish mathematical overlap at the level of statements, including the one-position version of the collision map. This verifies equivalent coverage; the relationship and historical precedence of the records are not established.

## value

FAIL

An exact resolution of the named conjecture and a uniform collision classification are naturally useful, but both the conjecture resolution and the stronger pair criterion are already present in an exact covering record. No separate unresolved fixed-weight parameter regime, tool, or structural lemma remains in the submitted finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
