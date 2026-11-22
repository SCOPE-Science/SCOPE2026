#!/usr/bin/env python3
"""Independent direct binary-state enumeration for intact and rung-deleted prisms."""

def update(x,n,broken):
    y=0
    for rail in range(2):
        for col in range(n):
            left=(x>>((col-1)%n+n*rail))&1
            right=(x>>((col+1)%n+n*rail))&1
            own=(x>>(col+n*rail))&1
            if broken and col==0:
                output=own if left!=right else left
            else:
                opposite=(x>>(col+n*(1-rail)))&1
                output=int(left+right+opposite>=2)
            y|=output<<(col+n*rail)
    return y

expected={
 3:(4,22,4,22),
 4:(8,64,8,32),
 5:(14,124,18,108),
 6:(22,484,30,316),
 7:(32,844,44,608),
 8:(48,2304,64,1552),
 9:(76,5782,100,3838),
}
for n,anticipated in expected.items():
    observed=[]
    for broken in (False,True):
        f1=f2=0
        for state in range(1<<(2*n)):
            after=update(state,n,broken)
            f1+=after==state
            f2+=update(after,n,broken)==state
        observed.extend((f1,f2))
    assert tuple(observed)==anticipated,(n,observed,anticipated)
    print('prism columns',n,'intact/fault fixed and two-step:',observed)
print('DIRECT_ENUMERATION_OK')
