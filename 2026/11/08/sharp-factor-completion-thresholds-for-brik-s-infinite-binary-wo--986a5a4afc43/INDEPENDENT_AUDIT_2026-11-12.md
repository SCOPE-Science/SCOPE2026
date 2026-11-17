# Independent mathematical audit

## correctness

PASS

For B_1=101, B_{i+1}=B_i B_i[i+1..], positions one-based, n>=3, the boundary-prefixing construction takes a legal k-factor v safely starting at p>=k+2 to 1v at f(p)=2^(p-2)+p and to 01v at f(p)-1; the suffix containment inequality and B_{p-1}'s final 01 are verified algebraically. Explicit safe bases at lengths 3 and 4 initiate a simultaneous induction bounding every nonconstant length-n first occurrence by r_(n-1). The first all-ones run starts r_n, and its immediate next symbol is 0 by Shallit's boundary construction, so 1^(n-1)0 is sharp; hence U(n)=r_n+n-1 for n>=2, U(1)=2. Direct first-occurrence checks n=2,3,4 corroborate r2=5,r3=13,r4=2061; finite code is not the infinite induction.

## originality

PASS

The evaluated two-level maximum of nonconstant factor onsets and exact factor-completion prefix are not stated by Shallit's factor-language/one-run theorems. Searches for equivalent prefix universality and Brik factor arrival instead found the source record and other, different spectra. Best-of-knowledge PASS; the proof critically credits Shallit's foundational results.

## value

PASS

Natural completion-time invariant of a specific infinite word whose legal language is easy to describe but earliest complete representative prefix is enormous; the unique delayed all-ones factor and exact penultimate threshold sharpen a genuine quantitative gap, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
