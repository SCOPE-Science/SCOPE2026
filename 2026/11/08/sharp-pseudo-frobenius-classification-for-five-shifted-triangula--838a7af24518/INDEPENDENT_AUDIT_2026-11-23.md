# Independent mathematical audit

## correctness

PASS

The first 50 coin values agree with independent multiplicity enumeration. For n >= 40 an optimal representation of n+10 must contain a ten since the no-ten lower bound exceeds floor(n/10)+4. Thus the ten-shift induction is justified. In residue r, a representation with offset sum r+ja costs at least r+a(j+c(r+ja)); the lower bound j+ceil((r+18j)/10) excludes j >= 1 by the coin block formula, with r=5,8 checked with the stronger lower bound 4. Testing f+a shows that any PF f must be W_r-a; the r=0 option -a fails after adding a+1. The other generators give the two inequalities in (*), with the +1 exactly when there is a wrap. An interior r >= 10 fails at offset 10, and of the low exceptional r=2,5,8 only 5 and 8 pass (r=2 fails at offset 3). For a >= 30 the wrap inequalities at r=a-k are automatic and the other tests depend only on a mod 10. Independently enumerating coin multiplicities for a=30..39 recovers all ten K_s. Direct integer reachability, without using Apéry or coin lengths to determine membership, verifies the full PF sets over 18..99, including all twelve transitional a and disjoint residue contributions. At a=17 it gives {33,39,42,48,49}, with 24 the unique spurious prediction (24+18=42 remains a gap). Period 10 is least since the type 10 occurs in just one residue class. This proves sharpness for the full formula rather than inferring it from fitting data.

## originality

PASS

The priority assessment is for the exact closed classification and sharp starting bound, not the known shifted-family pseudo-Frobenius transport or the standard Apéry method. Best-of-knowledge only.

## value

PASS

An initial triangular prefix is a natural small non-arithmetic offset family. The complete PF set determines more than type or Frobenius number alone, and the exact boundary 18 answers how early the mechanism stabilizes in a case whose general sufficient condition only starts above 100. The least-period computation and persistent low residues describe real structure, not a list of arbitrary examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
