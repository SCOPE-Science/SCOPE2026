from clebsch_symmetry import *
for period,target in [(13,4),(16,5)]:
    reps=[int(x) for x in (ROOT/f'period{period}_reps.txt').read_text().split()]
    for r in reps:
        state=r; exc=[0]*16
        for _ in range(period):
            x=state
            for i in range(16):
                exc[i]+=int(x%3==1);x//=3
            state=successor(state)
        assert state==r
        assert exc==[target]*16,(period,r,exc)
    print(f'period {period}: verified every one of {len(reps)} cycles has {target} excitations per site per period')
