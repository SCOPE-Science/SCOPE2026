"""Direct exhaustive state-evolution verification of one-way cube arc toggles.
Run: python check_dynamics.py; q=4 uses two independent GF(2) bitplanes.
"""

def apply_binary(state, rows):
    z=0
    for i,mask in enumerate(rows):
        z |= ((state & mask).bit_count() & 1) << i
    return z

def rows_of(d, distance):
    m=1<<d
    a=[sum(1 <<(i^(1<<j)) for j in range(d)) for i in range(m)]
    a[0]^=1 <<((1<<distance)-1)
    return a

def next_state(z, rows, m, q):
    if q==2:
        return apply_binary(z,rows)
    mask=(1<<m)-1
    return apply_binary(z&mask,rows) | (apply_binary(z>>m,rows)<<m)

def expected(d,dist,q):
    m=1<<d;r=m//2
    if d%2==0:
        if dist==1:
            return {'by_time':[q*q,q**(r+1),q**m], 'period_points':{1:q, 2:q*q-q}}
        return {'by_time':[1,q**(r-1),q**(m-2),q**(m-1),q**m], 'period_points':{1:1}}
    if dist==1:
        return {'by_time':[q**(m-2),q**(m-1),q**m], 'period_points':{1:q**(r-1),2:q**(m-2)-q**(r-1)}}
    return {'by_time':[q**m], 'period_points':{1:q**(r-1),2:q**(m-2)-q**(r-1),4:q**m-q**(m-2)}}

def verify(d,dist,q):
    m=1<<d; rows=rows_of(d,dist)
    predicted=expected(d,dist,q)
    total=q**m
    clock_max=len(predicted['by_time'])-1
    count_time=[0]*(clock_max+1)
    point_period={1:0,2:0,4:0}
    for state in range(total):
        path=[];vis={};y=state
        for t in range(clock_max+6):
            if y in vis:
                entry=vis[y];per=t-entry
                assert per in (1,2,4),(d,dist,q,per)
                for j in range(entry,clock_max+1):count_time[j]+=1
                if entry==0:point_period[per]+=1
                break
            vis[y]=t;path.append(y)
            y=next_state(y,rows,m,q)
        else: raise AssertionError('No return in bounded horizon')
    assert count_time==predicted['by_time'],(d,dist,q,count_time,predicted['by_time'])
    got={k:v for k,v in point_period.items() if v}
    assert got==predicted['period_points'],(d,dist,q,got,predicted['period_points'])
    print('PASS d=%d distance=%d q=%d total=%d by_time=%s period_points=%s' %(d,dist,q,total,count_time,got))

if __name__=='__main__':
    cases=0
    for d in range(2,5):
        for dist in range(1,d+1):
            verify(d,dist,2);cases+=1
    for d in (2,3):
        for dist in range(1,d+1):
            verify(d,dist,4);cases+=1
    print('PASS: %d exhaustive dynamical case checks' % cases)
