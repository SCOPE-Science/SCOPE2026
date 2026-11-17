# Independent mathematical audit

## correctness

PASS

PASS. The pinned source is one leaf, so the exact unforced count generator has (hub x, k leaves), hub birth lambda k, hub recovery 1, leaf birth x lambda(n-k) and leaf recovery k. The smooth potential u0(z)=int_0^z int_0^1 exp(t(a-y))dt dy and u1=u0+int_0^1 exp(t(a-z))dt, a=c², solves the limiting Poisson equations and u1(0)=(exp(a)-1)/a. Uniform Taylor errors at all k=0..n are O(lambda): z-weighted derivatives decay and the boundary rates vanish correctly. Starting from any initial configuration, leaf domination followed by a bounded-probability hub-recovery/no-reinfection extinction block of length O(log n) controls the first two extinction moments. Dynkin's stopped identity yields E S_n=(exp(c²)-1)/c²+O(log n/sqrt n). In the backward Harris dual a permanently infected leaf generates source-to-hub arrows, so p_hub=E[1-exp(-lambda S_n)] exactly. The moment correction is O((log n)²/n), and stationary ordinary-leaf birth/recovery balance gives E K_n=lambda E[H(n-K_n)]=exp(c²)-1+O((log n)²/sqrt n). All for c>0 fixed, ordinary leaves excluding pinned source; no inference of distributional limit or unforced survival. This is an analytic argument, not established by the 268-check verification log.

## originality

PASS

Originality assessed against semantic published research and the listed primary sources; substantial previously established components explicitly credited. The final model-specific statement is not shown implied by examined prior results; inaccessible full texts remain explicitly qualified.

## value

PASS

PASS. The permanent peripheral infection source is a natural epidemic boundary condition distinct from quasi-stationary regularizations. The nontrivial exact exponential burden at the n^(-1/2) hub-threshold scale is an independently useful model-specific limiting invariant and elucidates why vanishing hub prevalence coexists with O(1) total leaf load.

The dated certificate retains the supplied scientific assessment, sources and limitations.
