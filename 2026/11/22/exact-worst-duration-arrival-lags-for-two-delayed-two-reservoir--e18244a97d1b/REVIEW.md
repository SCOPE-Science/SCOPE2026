# Independent mathematical audit

## correctness

PASS

For t>=d, collecting the two exponential terms gives K(d)f(t-c(d)), with d-c(d)<1. Its rising branch therefore starts at the arrival discharge f(d); its peak is K(d)/e, and (log K)'=-de^{-d}/(1+e^{-d})^2. When 0<h<1/e and d<a_h, both crossings are after arrival and the duration is the strictly decreasing width L(h/K(d)); when d>b_h, the first interval has the fixed width b_h-a_h and the separate post-arrival width again strictly decreases. For a_h<=d<=b_h the first start is a_h and the final end is R=c(d)-W_{-1}(-h/K(d)); R>d+1 since Q_d(d+1)>1/e. Implicit differentiation gives R'=f'(R-d)/(f'(R)+f'(R-d))>0. The formulas agree at a_h and b_h, since an arrival-level contact contributes measure zero; at b_h the post-arrival rising crossing is precisely the arrival. Thus the only possible maximizers are 0 and b_h, with all ties determined by comparing the two exact durations. At h>=1/e the first pulse alone contributes no duration; the post-arrival width strictly favors zero lag while positive at zero lag, and every duration vanishes for h>=2/e. The peak bound attains equality only synchronously. Independent replay: python3 /workspace/checks/frozen_replay.py 2. At h=1/4 rational exponential enclosures give a_h<0.36, 2.15<b_h<2.16, Q_{b_h}(4.6)>1/4 and f(3.3)<1/8, implying staggered duration >4.24 versus synchronous <3.3. High-precision crossings give 4.29310005052455 and 3.11726433143898 (relative increase 0.37720115911466). Continuity and the synchronous advantage as h tends up to 1/e establish at least one crossover, not uniqueness.

## originality

PASS

The distinct claim supported by the inspected evidence is the global all-threshold duration optimizer for two equal instantaneous impulses through the same two-stage cascade. Gamma routing, Lambert-W crossing formulas and compound-event timing were already in use; none of the material compared supplies the two-candidate optimum for the sum's superlevel duration.

## value

PASS

The theorem reduces a continuous lag optimization for total exposure time, including separated episodes, to two physically interpretable choices and proves a sizable failure of peak-maximizing timing for that objective. It is a tractable benchmark for duration-based analysis, not a model of specific inundation or damage; its equal instantaneous inputs, common two-stage response and zero baseflow are essential scope limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
