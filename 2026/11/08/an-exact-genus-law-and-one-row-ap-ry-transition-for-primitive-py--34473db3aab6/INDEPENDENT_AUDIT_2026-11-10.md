# Independent mathematical audit

## correctness

PASS

For n,p positive coprime, m>Q=n²+p², gcd(m,Q)=1 and m+n+p odd, A=2mn is positive and gcd(B,2m)=1 for B=m²-Q. Reduce an arbitrary S element uA+vD+xB+yC via z=y-x and s=min(x,y), replacing the s(B+C) pair shift with a nonnegative A multiple to some W(v0,z)=2mpv0+m²|z|+Qz, 0<=v0<n. The 2mn baseline W(v,z) for -m<=z<m are pairwise distinct residues modulo A; competing same-residue lifts have z=z0+2mk. Strict lower bounds exclude all k>=1 and k<=-2, and k=-1 except at z0=m-1. That boundary improves precisely the last t row entries for t satisfying pt≡Q-m mod n and ell=Q+p(n-t)-m>0, each by 2m ell. The standard genus=sum(Apéry)/A-(A-1)/2 yields exactly (m³-Q+1)/2+m(np-n-p)-t max(0,ell)/n. For n=1 take t=0. Independently computed shortest representatives by residue-Dijkstra over 105 admissible small (n,p,m), including four with active correction, all exact matches; the unrestricted proof rests on lift inequalities, not this finite check.

## originality

PASS

PASS best-of-knowledge. Hwang–Song (2026 arXiv:2609.21397, FULL 16-page text examined) establishes Frobenius MAXIMUM of the same four-generator semigroup, in coprime case m>=2Q; it discusses baseline residues but not genus via sum and not exact small-m one-row correction. Published 2026-10-04 subthreshold result gives the Frobenius maximum and membership residue decomposition for Q<m<2Q, and thus allows an algorithm to compute Apéry sets but does not state the submitted complete parameter-level genus formula and t-row replacement. Genus is a different natural invariant from Frobenius and is not generally determined by maximum of Apéry. The precise all-parameter count of replaced representatives and genus correction requires additional minimization/summation. Other Apéry transition records involve different semigroup generators. Remaining risk: clever summation of prior implicit decomposition may mechanically yield formula; comparison finds it nontrivial.

## value

PASS

Genus (total gaps) and Frobenius number (largest gap) are distinct central numerical-semigroup invariants. A complete exact Apéry representative classification in the natural four-generator Pythagorean-quadruple family covers the entire previously delicate Q<m<2Q band, supplies a sharp parameterized boundary-row phenomenon, and gives a closed genus formula. The exact fact can be used to study gaps/Hilbert series and is mathematically motivated independently of a further major theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
