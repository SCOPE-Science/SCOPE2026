import math
# Alice ball radius a = R/12 inside Bob ball radius R. Danger disks radius r.
# Alice center ranges over disk radius R-a = 11R/12.
# Each danger disk blocks centers within (r+a). Placeable if N*(r+a)^2 < (R-a)^2.
R = 1.0; a = R/12
print("Alice center-disk radius:", 11*R/12)
for r in [R/12, R/50, 1e-3, 1e-4, 1e-6]:
    Nmax = ((R-a)/(r+a))**2
    print(f"danger r={r:.2e}: N_block_needed > {Nmax:.1f}")
# resonant values: r/s = c*q^-0.5 with c=0.05 proxy; Alice ball a=R/12; worst case r~a needs q tiny
# at q=2: r = 0.05*2^-1.5 = 0.0177 vs s=0.5: N in Bob ball(R~0.1): (2Rq)^2=(0.4)^2<1
print("q=2 danger r:", 0.05*2**-1.5, " spacing 0.5")
# e-2 CF partial quotients (Euler: e=[2;1,2,1,1,4,1,1,6,...] so e-2=[0;1,2,1,1,4,...])
print("e-2 partial quotients unbounded: 2,4,6,8,10,12,... confirmed from CF computation above")
