#!/usr/bin/env python3
"""Independent bit-parallel brute-force check for Rule 110 rings."""

def step(x,n):
    mask=(1<<n)-1
    left=((x<<1)&mask)|(x>>(n-1))
    right=(x>>1)|((x&1)<<(n-1))
    # b=0 gives right neighbor, b=1 gives NOT(left AND right)
    return (((~x)&right)|(x&(~(left&right))))&mask


def run():
    for n in range(3,21):
        p8=p9=p10=0
        for x in range(1<<n):
            y=x
            eq1=eq2=eq3=eq4=eq5=eq8=eq9=eq10=False
            for k in range(1,11):
                y=step(y,n)
                if k==1:eq1=(x==y)
                elif k==2:eq2=(x==y)
                elif k==3:eq3=(x==y)
                elif k==4:eq4=(x==y)
                elif k==5:eq5=(x==y)
                elif k==8:eq8=(x==y)
                elif k==9:eq9=(x==y)
                elif k==10:eq10=(x==y)
            # primitive t=8 excludes t=4, t=9 excludes t=3,
            # primitive t=10 excludes t=2 and t=5 (intersection t=1).
            p8+=eq8 and not eq4
            p9+=eq9 and not eq3
            p10+=eq10 and not eq2 and not eq5
        want8=8*(n%8==0)
        want9=18*(n%6==0)+36*(n%12==0)+18*(n%18==0)
        assert p8==want8 and p9==want9 and p10==0,(n,p8,p9,p10,want8,want9)
        print(n, 'period8_points',p8,'period9_points',p9,'period10_points',p10,flush=True)
    print('BRUTE_FORCE_OK')

if __name__=='__main__':run()
