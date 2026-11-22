# Independent mathematical audit

## correctness

PASS

Substituting equal deviations delta_0=delta_1=t yields t(b+3t^2+t^4)=0, hence central and ±sqrt(z) with b=-3z-z^2. Explicit next-state matrices B0,B1 and current-state diagonal derivatives give M=B1^-1diag(1,1/3)B0^-1diag(1,1/2), tr M=N(z)/D(z), detM=1/D(z), where D=3(4z^2+5z-1)(8z^2+9z-2), N=(1-3z-4z^2)^2+9z+6. Independently recomputed the two rational identities and factorizations D-N+1=2z(2z+3)(20z^2+21z-10), D+N+1=2(56z^4+126z^3+44z^2-27z+7). Elementary Jury/Schur signs show stability iff z>z*=(sqrt(1241)-21)/40, equivalently b<b*, exclude D zero at z_±. At b=b* one multiplier +1, other 1/D in (0,1). Eliminating y variables yields B(m,d) and H(m,d)=0 for unequal deviations; verified H(sqrt(z*),0)=0 and H_d=6z*>0, H_m=-4z*(21+40z*) nonzero, so the implicit function theorem yields local crossing branches. Independent exact symbolic evaluation gives b*=-1.1936067079963324. No global basin or all-branch census is asserted.

## originality

PASS

Oliveira arXiv:2611.03336v1 Section 8.4 defines the exact alternating implicit model and derives local cusp reduction at (a,b)=(0,0), not the finite-amplitude b* transverse Floquet/Jury threshold nor the unequal-deviation branch at it. Published records of other implicit or two-cycle systems are not the same recurrence. The specified model is not new; its exact nonlocal stability classification is the claimed addition.

## value

PASS

The mathematical gap from local cusp existence to exact forward-branch sink stability and multistability is natural and consequential for implicit recurrences. Sharp algebraic threshold and exceptional singular-step parameters give useful rigorous limits for applying conventional Floquet multipliers in multivalued dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
