# Independent mathematical audit

## correctness

PASS

On the exact critical probability slice b in (0,1/3], simplex invariance follows because 1-b-2bi >= 1-3b >=0; first-infected y/v boundary cases are included. Direct symbolic elimination with x=1-u-y-v verifies z=u+2v, q=y-u-v, i=u+v obey z_next=z+2biq, q_next=(1-b-2bi)q-2bv, v_next=(1-b)v+2biy. An initially infected orbit generates v>0 by time 2; then q crosses to nonpositive and cannot recover. Positivity and eventual monotone z give limit L; if L>0, sum(-q)<infinity forces q,v->0 but recurrence v_next contains 2bi y tending to 2bL², contradiction. Thus z->0. The stable-response contraction lemma gives v/z²->2 and q/z²->-4, so z_next=z-8bz³(1+o(1)); summing reciprocal-square differences yields n z²->1/(16b). Therefore sqrt(n) u,y->1/(4sqrt b), n v->1/(8b), and sqrt(n)(1-x)->1/(2sqrt b). Infection-free seeds instead have y_n=(1-b)^n y_0. Independent SymPy simplification of all three recurrences and total mass produced zero residual; package VERIFY.py separately source-inspected.

## originality

PASS

Shoyimardonov 2020 specifies precisely the discrete SISI map, admissibility, and a global extinction conjecture at these critical inequalities; it does not prove this doubly critical slice or separate n^-1/2 and n^-1 stage constants. 2021 follow-up addresses fixed points and noncritical regions. Nearby published SIS/SIRS critical exponents arise in different models and cannot imply this four-compartment SISI result by parameter matching alone.

## value

PASS

The global resolution of a natural equality case in a named epidemic extinction conjecture plus two distinct universal compartment exponents is a motivated boundary result. The two rates distinguish infection-stage persistence even though all infection clears; no full nearby-parameter classification is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
