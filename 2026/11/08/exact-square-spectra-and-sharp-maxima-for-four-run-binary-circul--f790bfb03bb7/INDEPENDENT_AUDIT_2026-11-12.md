# Independent mathematical audit

## correctness

PASS

PASS: With positive a,b,c,d and circle w=0^a1^b0^c1^d, a mixed square XX of length <=n has 3 or 4 letter transitions, forcing a conjugate of a two-run root. Four possible 3-transition forms with explicit necessary/sufficient containment inequalities, plus split forms at b=d or a=c with min(a,c)-1 and min(b,d)-1 distinct 4-transition words, give mixed count M=a+b if both pairs equal, min(b,d)+1 if a=c alone, min(a,c)+1 if b=d alone, else 1. Pure-letter squares contribute floor(max(a,c)/2)+floor(max(b,d)/2). A separate parity and run-length bound plus explicit attaining quadruples yields sharp H4(4)=2, H4(n)=floor(3n/4)-1 for n>=7 congruent 3 mod4 and floor(3n/4) otherwise. Fresh literal cyclic-square enumeration tested all 1,820 positive quadruples with n=4..16, every formula and all length maxima matched. The proof case analysis, not finite tests, covers all positive run lengths.

## originality

PASS

PASS (best of knowledge): Semantically searched all prior published records for ordinary distinct circular square factors conditioned on exactly four binary cyclic runs, their opposite-run equality spectrum and sharp maximum. Found earlier four-run complementary factors, antisquares, Abelian-square content and minimal unique factors, all different predicates. Primary Amit–Gawrychowski 2017 concerns unrestricted circular words with a 3.14n universal upper bound; later Li–Song 2026 and Hamai 2026 give improved unrestricted upper bounds but no run-conditioned exact count or sharp ~3n/4 bound. No prior theorem located that implies the current four-run pointwise formula or its extremal residue classes. Historical priority is provisional.

## value

PASS

PASS: Exactly four cyclic runs is a natural low-complexity structural slice for ordinary (non-Abelian) square factors, not an arbitrary numerical input table. Its equality-sensitive exact spectrum isolates the combinatorial transition mechanism and establishes a sharp all-length constrained extremum with residue-class exception; these exact facts could be used in run-restricted circular-word enumeration and algorithms independent of universal square bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
