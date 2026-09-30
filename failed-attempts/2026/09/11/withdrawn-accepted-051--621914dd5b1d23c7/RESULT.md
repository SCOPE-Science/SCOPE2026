# Universal interpolation-infeasibility barrier at the N=16/s=4/rate-1/4/rho=0.52 folded-RS window

## Context
Target: exhibit a rate-1/4 folded Reed–Solomon code list-decodable beyond the Johnson radius 1−sqrt(R)=0.5 with polynomial list, at the explicit window base RS [n=64,k=16] over F_257 folded with s=4 into N=16 bundles (rate 1/4), radius rho=0.52, list L<=16, via a multiplicity-2 interpolation degree count plus linear-algebraic pruning. The m=2 certificate attempt is blocked; extension reveals a structural all-multiplicity obstruction. The bare (rho,L) consequence holds only via a textbook folded-Johnson argument explicitly separated as non-original.

## Definitions
- Base code [n,k]=[64,16] over F_257, rate R=1/4, folded s=4 to N=16 bundles over F_257^4.
- Radius rho=0.52: bundle errors <=floor(8.32)=8, bundle agreement t=8; unfolded fractional agreement t_u=ceil(64*0.48)=31 (operative weakest premise); folded-induced minimum t>=32 (8 fully-correct bundles x4). Both t=31 and t=32 swept for Lemma 2.
- Standard existence-plus-multiplicity-lemma framework: nonzero Q exists when #coeffs(D,l)>#conditions(m) and decodes when D<t(m-l) with l<m.
- Settings: (i) bivariate Q(X,Y) through N=16 bundle points; (ii) bivariate Q(X,Y) through n=64 unfolded points; (iii) (s+1)-variate GR-type Q(X,Y1..Y4) under most generous unweighted count (true GR weighted count strictly smaller, so failure transfers as impossibility).

## Result (headline claim)
At the exact N=16/s=4/rate-1/4/rho=0.52 window, no triple (m,D,l) with m>=2 satisfies interpolation existence plus the multiplicity-lemma decoding inequality in any of the three settings above. Hence the standard interpolation-certificate framework cannot succeed at this window at any multiplicity; in particular the as-stated m=2 certificate is arithmetically impossible for every degree choice.

Companion diagnostic (NOT claimed as original): folded distance >=13 bundles, pairwise bundle agreement <=floor(15/4)=3, folded q-ary Johnson radius 1−sqrt(1−13/16)~=0.567>0.52; second-moment counting excludes L=6 (48.0 vs 45) hence all L>=6, so L<=5 (hence L<=16). Textbook corollary.

## Proof / evidence
- Lemma 1 (bivariate bundle): conditions 8m(m+1); weighted coeffs <=(l+1)(D+1); best decoding D+1=8(m−l); necessity s(m+1−s)>m(m+1), s=l+1; AM–GM s(m+1−s)<=floor((m+1)^2/4)<=m(m+1) for m>=1. Blocked all m>=2; sweep 2..500 confirms.
- Lemma 2 (bivariate unfolded): conditions 32m(m+1); best D+1=31(m−l) at t_u=31; necessity 31s(m+1−s)>32m(m+1); AM–GM gives 31(m+1)<=128m for m>=1. At t=32 necessity collapses to Lemma-1 AM–GM. Blocked under either bound; sweeps 2..500 at both confirm.
- Lemma 3 (multivariate GR generous): conditions 16C(m+4,5), coeffs 8(m−l)C(l+4,4) best case; Rtrue<=((1/3)(m−l)(l+4)^4)/((2/15)m^5)=2.5*((m−l)/m)*(((l+4)/m)^4), verified HOLDS 50<=m<=200; exhaustive m=2..200 zero feasible (worst ratio 0.4167 at m=2); tail m>=50 via u'=(m−l)/m, (l+4)/m<=1.08−u', max g*=27/125*(108/125)^4=3673320192/30517578125~=0.120367, R<=2.5g*~=0.301<1; overlap [50,200] doubly covered.
- All stdlib-only replay (see Reproducibility).

## Limitations
- Rules out only the standard existence-plus-multiplicity-lemma interpolation-certificate framework at this exact window; does not rule out non-interpolation decoders, different radii/windows, or the bare decodability consequence (which holds classically, L<=5).
- Lemma 3 generous-to-strict transfer valid only as impossibility transfer.
- No new decodable radius-rate-list triple claimed; value is the redirect.

## Reproducibility
- `output/artifacts/check_counts.py` -> `counts.log` (m=2 exhaustive, all NONE).
- `output/artifacts/check_allm.py` -> `allm.log` (all-m sweeps, chain verification, exact-rational tail).
- `output/artifacts/check_johnson.py` -> `johnson.log` (diagnostic only).
- Rerun: `python3 output/artifacts/check_*.py` (stdlib only).

## References
- Guruswami–Rudra, Explicit Capacity-Achieving List-Decodable Codes (folded RS).
- Guruswami, Linear-Algebraic List Decoding of Folded Reed-Solomon Codes.
- Kopparty–Ron-Zewi–Saraf–Wootters, Improved List Decoding of Folded RS and Multiplicity Codes.
- Tamo, Tighter List-Size Bounds for FRS/Multiplicity Codes.
- Chen–Zhang, Explicit FRS/Multiplicity Codes Achieve Relaxed Generalized Singleton Bounds.
- Srivastava, Improved List Size for Folded Reed-Solomon Codes (arXiv:2410.09031).
- Guruswami–Sudan list-decoding framework (existence + multiplicity lemma).
